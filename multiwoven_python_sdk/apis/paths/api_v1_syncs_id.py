from multiwoven_python_sdk.paths.api_v1_syncs_id.get import ApiForget
from multiwoven_python_sdk.paths.api_v1_syncs_id.put import ApiForput
from multiwoven_python_sdk.paths.api_v1_syncs_id.delete import ApiFordelete


class ApiV1SyncsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
