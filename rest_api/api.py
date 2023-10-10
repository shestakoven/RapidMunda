import asyncio
import json

import uvicorn
from fastapi import FastAPI, Body
from web3 import AsyncWeb3

from config import config
from rest_api.models import ProcessDefinitionModel

CONTRACT_ADDRESS = '0xdE41896526D3235a94C0250778792AC22C32146E'

app = FastAPI()
provider = AsyncWeb3.AsyncHTTPProvider(config.rpc_url)
w3 = AsyncWeb3(provider=provider)
account = config.wallet_address
private_key = config.wallet_private_key
w3.eth.default_account = account
with open('rest_api/contract_abi.json') as abi_file:
    abi = json.loads(abi_file.read())


@app.post('/deploy')
async def add_process_definition(
        process_definition: ProcessDefinitionModel = Body(...),
):
    contract = w3.eth.contract(
        bytecode=config.contract_bytecode, abi=abi, address=w3.to_checksum_address(CONTRACT_ADDRESS)
    )
    process_vars = process_definition.model_dump().values()
    tx = contract.functions.addProcessDefinition(
        *process_vars
    )
    gas_estimate, gas_price, nonce = await asyncio.gather(
        tx.estimate_gas(),
        w3.eth.gas_price,
        w3.eth.get_transaction_count(account),
    )
    tx = await tx.build_transaction(
        {
            'from': account,
            'nonce': nonce,
            'gas': gas_estimate,
            'gasPrice': gas_price,
        }
    )
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    tx_hash = await w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    await w3.eth.wait_for_transaction_receipt(tx_hash)
    definition = await contract.functions.processDefinitions(process_definition.id).call()
    # TODO save contract address to db
    return definition


@app.post('/run_instance')
async def run_instance(
        id: str = Body(...),
        process_instance_id: str = Body(..., alias='processInstanceId'),
        tenant_id: str = Body(..., alias='tenantId'),
        process_definition_id: str = Body(..., alias='processDefinitionId'),
        business_key: str = Body(..., alias='businessKey'),
        root_process_instance_id: str = Body(..., alias='rootProcessInstanceId'),
        case_instance_id: str = Body(..., alias='caseInstanceId'),
):
    contract_address = w3.to_checksum_address(CONTRACT_ADDRESS)
    contract = w3.eth.contract(address=contract_address, abi=abi)
    add_process_instance_call = contract.functions.addProcessInstance(
        id,
        process_instance_id,
        tenant_id,
        process_definition_id,
        business_key,
        root_process_instance_id,
        case_instance_id,
    )
    gas_estimate = await add_process_instance_call.estimate_gas()
    gas_price = await w3.eth.gas_price
    tx = await add_process_instance_call.build_transaction(
        {
            'from': account,
            'nonce': w3.eth.get_transaction_count(account),
            'gas': gas_estimate,
            'gasPrice': gas_price,
        }
    )
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    tx_hash = await w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_receipt = await w3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_receipt


async def deploy_contract(nonce: int = 0):
    contract = w3.eth.contract(bytecode=config.contract_bytecode, abi=abi)
    create_call = contract.constructor()
    gas_estimate = await create_call.estimate_gas()
    gas_price = w3.eth.gas_price
    tx = await contract.constructor().build_transaction(
        {
            'from': account,
            'nonce': nonce or w3.eth.get_transaction_count(account),
            'gas': gas_estimate,
            'gasPrice': gas_price,
        }
    )
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    tx_hash = await w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_receipt = await w3.eth.wait_for_transaction_receipt(tx_hash)
    contract_address = tx_receipt['contractAddress']
    return contract_address


if __name__ == '__main__':
    uvicorn.run('api:app', host='localhost', port=8000, reload=True)
