from pydantic_settings import BaseSettings


class Config(BaseSettings):
    app_name: str = "My App"
    items_per_user: int = 50
    rpc_url: str = "http://localhost:8545"
    wallet_address: str = 'test_wallet'
    wallet_private_key: str = 'test_wallet_private_key'
    contract_bytecode: str = '6080806040523461001657611d41908161001c8239f35b600080fdfe6080604052600436101561001257600080fd5b60003560e01c80635490009414610d7957806369fe458214610c305780636a647de014610a5e578063a722ea89146100e7578063c00bd5bc146100b45763fd9a1d181461005e57600080fd5b346100af576100ad6020600161008b61007636611cd1565b93908160405193828580945193849201611ba9565b810184815203019020019061ff00825491151560081b169061ff001916179055565b005b600080fd5b346100af576100ad602060016100cc61007636611cd1565b810184815203019020019060ff801983541691151516179055565b346100af5760e03660031901126100af576004356001600160401b0381116100af57610117903690600401611b53565b6024356001600160401b0381116100af57610136903690600401611b53565b6044356001600160401b0381116100af57610155903690600401611b53565b6064356001600160401b0381116100af57610174903690600401611b53565b926084356001600160401b0381116100af57610194903690600401611b53565b60a4356001600160401b0381116100af576101b3903690600401611b53565b60c4356001600160401b0381116100af576101d2903690600401611b53565b91604051966101208801958887106001600160401b038811176105c55761023b97602097604052868a526000888b0152600060408b015260608a0152608089015260a088015260c087015260e08601526101008501528160405193828580945193849201611ba9565b810160018152030190209080519182516001600160401b0381116105c5576102638254611bcc565b601f8111610a1a575b506020601f82116001146109b257819293946000926109a7575b50508160011b916000199060031b1c19161781555b6102d9600182016102be60208501511515829060ff801983541691151516179055565b6040840151815461ff00191690151560081b61ff0016179055565b60608201519182516001600160401b0381116105c5576102fc6002840154611bcc565b601f811161095e575b506020601f82116001146108f057819293946000926108e5575b50508160011b916000199060031b1c19161760028301555b60808101519182516001600160401b0381116105c55761035a6003830154611bcc565b601f811161089e575b506020601f82116001146108305781929394600092610825575b50508160011b916000199060031b1c19161760038201555b60a08201519182516001600160401b0381116105c5576103b86004840154611bcc565b601f81116107de575b506020601f82116001146107705781929394600092610765575b50508160011b916000199060031b1c19161760048301555b60c08101519182516001600160401b0381116105c5576104166005830154611bcc565b601f811161071e575b506020601f82116001146106b057819293946000926106a5575b50508160011b916000199060031b1c19161760058201555b60e08201518051906001600160401b0382116105c5576104746006840154611bcc565b601f811161065a575b50602090601f83116001146105e657918061010094926007946000926105db575b50508160011b916000199060031b1c19161760068201555b019101519081516001600160401b0381116105c5576104d58254611bcc565b601f811161057d575b50602092601f821160011461051c5792819293600092610511575b5050600019600383901b1c191660019190911b179055005b0151905083806104f9565b601f198216938360005260206000209160005b868110610565575083600195961061054c575b505050811b019055005b015160001960f88460031b161c19169055838080610542565b9192602060018192868501518155019401920161052f565b826000526020600020601f830160051c810191602084106105bb575b601f0160051c01905b8181106105af57506104de565b600081556001016105a2565b9091508190610599565b634e487b7160e01b600052604160045260246000fd5b01519050868061049e565b90601f198316916006850160005260206000209260005b8181106106425750926001928592600796610100989610610629575b505050811b0160068201556104b6565b015160001960f88460031b161c19169055868080610619565b929360206001819287860151815501950193016105fd565b600684016000526020600020601f840160051c8101916020851061069b575b601f0160051c01905b81811061068f575061047d565b60008155600101610682565b9091508190610679565b015190508480610439565b6005830160005260206000209060005b601f19841681106107065750600193949583601f198116106106ed575b505050811b016005820155610451565b015160001960f88460031b161c191690558480806106dd565b9091602060018192858a0151815501930191016106c0565b600583016000526020600020601f830160051c81016020841061075e575b601f830160051c8201811061075257505061041f565b6000815560010161073c565b508061073c565b0151905084806103db565b6004840160005260206000209060005b601f19841681106107c65750600193949583601f198116106107ad575b505050811b0160048301556103f3565b015160001960f88460031b161c1916905584808061079d565b9091602060018192858a015181550193019101610780565b600484016000526020600020601f830160051c81016020841061081e575b601f830160051c820181106108125750506103c1565b600081556001016107fc565b50806107fc565b01519050848061037d565b6003830160005260206000209060005b601f19841681106108865750600193949583601f1981161061086d575b505050811b016003820155610395565b015160001960f88460031b161c1916905584808061085d565b9091602060018192858a015181550193019101610840565b600383016000526020600020601f830160051c8101602084106108de575b601f830160051c820181106108d2575050610363565b600081556001016108bc565b50806108bc565b01519050848061031f565b6002840160005260206000209060005b601f19841681106109465750600193949583601f1981161061092d575b505050811b016002830155610337565b015160001960f88460031b161c1916905584808061091d565b9091602060018192858a015181550193019101610900565b600284016000526020600020601f830160051c8101602084106109a0575b601f90920160051c01905b8181106109945750610305565b60008155600101610987565b508061097c565b015190508480610286565b8260005260206000209060005b601f1984168110610a025750600193949583601f198116106109e9575b505050811b01815561029b565b015160001960f88460031b161c191690558480806109dc565b9091602060018192858a0151815501930191016109bf565b826000526020600020601f830160051c810160208410610a57575b601f830160051c82018110610a4b57505061026c565b60008155600101610a35565b5080610a35565b346100af5760203660031901126100af576004356001600160401b0381116100af57610a8e903690600401611b53565b6040518181809351602081930191610aa592611ba9565b810160008152036020019020610aba81611c06565b610ac660018301611c06565b91610ad360028201611c06565b90610ae060038201611c06565b6004820154610af160058401611c06565b610afd60068501611c06565b610b0960078601611c06565b610b1560088701611c06565b91600987015493600a8801610b2990611c06565b95600b89015497600c8a01610b3d90611c06565b99600d015460ff169a6040519d8e809e6101e08083528201610b5e91611cac565b908082039060200152610b7091611cac565b8d810360408f0152610b8191611cac565b8c810360608e0152610b9291611cac565b9060808c01528a810360a08c0152610ba991611cac565b89810360c08b0152610bba91611cac565b88810360e08a0152610bcb91611cac565b878103610100890152610bdd91611cac565b90610120870152858103610140870152610bf691611cac565b9060ff8116151561016086015260081c60ff1615156101808501528381036101a0850152610c2391611cac565b9015156101c08301520390f35b346100af5760203660031901126100af576004356001600160401b0381116100af57610c60903690600401611b53565b6040518181809351602081930191610c7792611ba9565b810160018152036020019020610c8c81611c06565b600182015491610c9e60028201611c06565b90610cab60038201611c06565b610cb760048301611c06565b610cc360058401611c06565b91610cd060068501611c06565b93600701610cdd90611c06565b94604051978897610120808a528901610cf591611cac565b9060ff8116151560208a015260081c60ff16151560408901528781036060890152610d1f91611cac565b8681036080880152610d3091611cac565b85810360a0870152610d4191611cac565b84810360c0860152610d5291611cac565b83810360e0850152610d6391611cac565b828103610100840152610d7591611cac565b0390f35b346100af576101e03660031901126100af576004356001600160401b0381116100af57610daa903690600401611b53565b6024356001600160401b0381116100af57610dc9903690600401611b53565b6044356001600160401b0381116100af57610de8903690600401611b53565b906064356001600160401b0381116100af57610e08903690600401611b53565b9260a4356001600160401b0381116100af57610e28903690600401611b53565b60c4356001600160401b0381116100af57610e47903690600401611b53565b60e4356001600160401b0381116100af57610e66903690600401611b53565b610104356001600160401b0381116100af57610e86903690600401611b53565b610144356001600160401b0381116100af57610ea6903690600401611b53565b90610164359283151584036100af57610184359485151586036100af576101a4356001600160401b0381116100af57610ee3903690600401611b53565b966101c43515156101c435036100af576040519b8c6001600160401b036101e08281810110920111176105c557610f919b60408e60209d6101e0820183528d82528e820152015260608d015260843560808d015260a08c015260c08b015260e08a015261010089015261012435610120890152610140880152151561016087015215156101808601526101a08501526101c43515156101c08501528160405193828580945193849201611ba9565b810160008152030190209080519182516001600160401b0381116105c557610fb98254611bcc565b601f8111611aee575b506020601f8211600114611a865781929394600092611a7b575b50508160011b916000199060031b1c19161781555b60208201519182516001600160401b0381116105c5576110146001840154611bcc565b601f8111611a34575b506020601f82116001146119c657819293946000926119bb575b50508160011b916000199060031b1c19161760018301555b60408101519182516001600160401b0381116105c5576110726002830154611bcc565b601f8111611974575b506020601f821160011461190657819293946000926118fb575b50508160011b916000199060031b1c19161760028201555b60608201519182516001600160401b0381116105c5576110d06003840154611bcc565b601f81116118b4575b506020601f8211600114611846578192939460009261183b575b50508160011b916000199060031b1c19161760038301555b6080810151600483015560a08101519182516001600160401b0381116105c5576111386005830154611bcc565b601f81116117f4575b506020601f8211600114611786578192939460009261177b575b50508160011b916000199060031b1c19161760058201555b60c08201519182516001600160401b0381116105c5576111966006840154611bcc565b601f8111611734575b506020601f82116001146116c657819293946000926116bb575b50508160011b916000199060031b1c19161760068301555b60e08101519182516001600160401b0381116105c5576111f46007830154611bcc565b601f8111611674575b506020601f821160011461160657819293946000926115fb575b50508160011b916000199060031b1c19161760078201555b6101008201519182516001600160401b0381116105c5576112536008840154611bcc565b601f81116115b4575b506020601f8211600114611546578192939460009261153b575b50508160011b916000199060031b1c19161760088301555b61012081015160098301556101408101519182516001600160401b0381116105c5576112bd600a830154611bcc565b601f81116114f4575b506020601f8211600114611486578192939460009261147b575b50508160011b916000199060031b1c191617600a8201555b611338600b820161131c6101608501511515829060ff801983541691151516179055565b610180840151815461ff00191690151560081b61ff0016179055565b600c8101916101a08101519283516001600160401b0381116105c55761135e8254611bcc565b601f8111611433575b506020601f82116001146113c2579181600d94926101c0946100ad986000926113b7575b50508160011b916000199060031b1c19161790555b0151151591019060ff801983541691151516179055565b01519050888061138b565b601f198216958360005260206000209660005b81811061141b5750926100ad976101c0959360019383600d999710611402575b505050811b0190556113a0565b015160001960f88460031b161c191690558880806113f5565b838301518955600190980197602093840193016113d5565b826000526020600020601f830160051c81019160208410611471575b601f0160051c01905b8181106114655750611367565b60008155600101611458565b909150819061144f565b0151905084806112e0565b600a830160005260206000209060005b601f19841681106114dc5750600193949583601f198116106114c3575b505050811b01600a8201556112f8565b015160001960f88460031b161c191690558480806114b3565b9091602060018192858a015181550193019101611496565b600a83016000526020600020601f830160051c810160208410611534575b601f830160051c820181106115285750506112c6565b60008155600101611512565b5080611512565b015190508480611276565b6008840160005260206000209060005b601f198416811061159c5750600193949583601f19811610611583575b505050811b01600883015561128e565b015160001960f88460031b161c19169055848080611573565b9091602060018192858a015181550193019101611556565b600884016000526020600020601f830160051c8101602084106115f4575b601f830160051c820181106115e857505061125c565b600081556001016115d2565b50806115d2565b015190508480611217565b6007830160005260206000209060005b601f198416811061165c5750600193949583601f19811610611643575b505050811b01600782015561122f565b015160001960f88460031b161c19169055848080611633565b9091602060018192858a015181550193019101611616565b600783016000526020600020601f830160051c8101602084106116b4575b601f830160051c820181106116a85750506111fd565b60008155600101611692565b5080611692565b0151905084806111b9565b6006840160005260206000209060005b601f198416811061171c5750600193949583601f19811610611703575b505050811b0160068301556111d1565b015160001960f88460031b161c191690558480806116f3565b9091602060018192858a0151815501930191016116d6565b600684016000526020600020601f830160051c810160208410611774575b601f830160051c8201811061176857505061119f565b60008155600101611752565b5080611752565b01519050848061115b565b6005830160005260206000209060005b601f19841681106117dc5750600193949583601f198116106117c3575b505050811b016005820155611173565b015160001960f88460031b161c191690558480806117b3565b9091602060018192858a015181550193019101611796565b600583016000526020600020601f830160051c810160208410611834575b601f830160051c82018110611828575050611141565b60008155600101611812565b5080611812565b0151905084806110f3565b6003840160005260206000209060005b601f198416811061189c5750600193949583601f19811610611883575b505050811b01600383015561110b565b015160001960f88460031b161c19169055848080611873565b9091602060018192858a015181550193019101611856565b600384016000526020600020601f830160051c8101602084106118f4575b601f830160051c820181106118e85750506110d9565b600081556001016118d2565b50806118d2565b015190508480611095565b6002830160005260206000209060005b601f198416811061195c5750600193949583601f19811610611943575b505050811b0160028201556110ad565b015160001960f88460031b161c19169055848080611933565b9091602060018192858a015181550193019101611916565b600283016000526020600020601f830160051c8101602084106119b4575b601f830160051c820181106119a857505061107b565b60008155600101611992565b5080611992565b015190508480611037565b6001840160005260206000209060005b601f1984168110611a1c5750600193949583601f19811610611a03575b505050811b01600183015561104f565b015160001960f88460031b161c191690558480806119f3565b9091602060018192858a0151815501930191016119d6565b600184016000526020600020601f830160051c810160208410611a74575b601f830160051c82018110611a6857505061101d565b60008155600101611a52565b5080611a52565b015190508480610fdc565b8260005260206000209060005b601f1984168110611ad65750600193949583601f19811610611abd575b505050811b018155610ff1565b015160001960f88460031b161c19169055848080611ab0565b9091602060018192858a015181550193019101611a93565b826000526020600020601f830160051c810160208410611b2b575b601f830160051c82018110611b1f575050610fc2565b60008155600101611b09565b5080611b09565b90601f801991011681019081106001600160401b038211176105c557604052565b81601f820112156100af578035906001600160401b0382116105c55760405192611b87601f8401601f191660200185611b32565b828452602083830101116100af57816000926020809301838601378301015290565b60005b838110611bbc5750506000910152565b8181015183820152602001611bac565b90600182811c92168015611bfc575b6020831014611be657565b634e487b7160e01b600052602260045260246000fd5b91607f1691611bdb565b9060405191826000825492611c1a84611bcc565b908184526001948581169081600014611c895750600114611c46575b5050611c4492500383611b32565b565b9093915060005260209081600020936000915b818310611c71575050611c4493508201013880611c36565b85548884018501529485019487945091830191611c59565b915050611c4494506020925060ff191682840152151560051b8201013880611c36565b90602091611cc581518092818552858086019101611ba9565b601f01601f1916010190565b60406003198201126100af57600435906001600160401b0382116100af57611cfb91600401611b53565b9060243580151581036100af579056fea264697066735822122059a5d9d4eb2bfc52ea709dceb255d0588ea0f86fc038b68941a8d9354d1dba0364736f6c63430008120033'

    class Config:
        env_file = ".env"


config = Config()