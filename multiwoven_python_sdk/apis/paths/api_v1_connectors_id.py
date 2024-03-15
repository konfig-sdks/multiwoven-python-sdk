from multiwoven_python_sdk.paths.api_v1_connectors_id.get import ApiForget
from multiwoven_python_sdk.paths.api_v1_connectors_id.put import ApiForput
from multiwoven_python_sdk.paths.api_v1_connectors_id.delete import ApiFordelete


class ApiV1ConnectorsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
