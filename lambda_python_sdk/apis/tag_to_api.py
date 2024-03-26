import typing_extensions

from lambda_python_sdk.apis.tags import TagValues
from lambda_python_sdk.apis.tags.instance_api import InstanceApi
from lambda_python_sdk.apis.tags.key_api import KeyApi
from lambda_python_sdk.apis.tags.file_system_api import FileSystemApi
from lambda_python_sdk.apis.tags.ssh_key_api import SSHKeyApi
from lambda_python_sdk.apis.tags.instance_type_api import InstanceTypeApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.INSTANCE: InstanceApi,
        TagValues.KEY: KeyApi,
        TagValues.FILE_SYSTEM: FileSystemApi,
        TagValues.SSHKEY: SSHKeyApi,
        TagValues.INSTANCE_TYPE: InstanceTypeApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.INSTANCE: InstanceApi,
        TagValues.KEY: KeyApi,
        TagValues.FILE_SYSTEM: FileSystemApi,
        TagValues.SSHKEY: SSHKeyApi,
        TagValues.INSTANCE_TYPE: InstanceTypeApi,
    }
)
