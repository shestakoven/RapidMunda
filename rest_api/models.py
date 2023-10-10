from pydantic import BaseModel, Field


class ProcessDefinitionModel(BaseModel):
    id: str
    category: str
    name: str
    key: str
    version: int
    resourceName: str
    deploymentId: str
    diagramResourceName: str
    tenantId: str
    historyTimeToLive: int
    description: str
    hasStartFormKey: bool
    isSuspended: bool
    versionTag: str
    is_startable_in_tasklist: bool = Field(alias='isStartableInTasklist')

