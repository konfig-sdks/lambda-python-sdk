# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from lambda_python_sdk.paths.file_systems import Api

from lambda_python_sdk.paths import PathValues

path = PathValues.FILESYSTEMS