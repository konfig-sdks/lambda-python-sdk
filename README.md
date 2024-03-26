<div align="center">

[![Visit Lambda](./header.png)](https://lambdalabs.com)

# Lambda<a id="lambda"></a>

API for interacting with the Lambda GPU Cloud


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`lambda.file_system.get_list`](#lambdafile_systemget_list)
  * [`lambda.instance.create_instances`](#lambdainstancecreate_instances)
  * [`lambda.instance.get_details`](#lambdainstanceget_details)
  * [`lambda.instance.list_running_instances`](#lambdainstancelist_running_instances)
  * [`lambda.instance.restart_instances`](#lambdainstancerestart_instances)
  * [`lambda.instance.terminate_instance`](#lambdainstanceterminate_instance)
  * [`lambda.instance_type.get_list`](#lambdainstance_typeget_list)
  * [`lambda.key.add_ssh_key`](#lambdakeyadd_ssh_key)
  * [`lambda.key.get_list`](#lambdakeyget_list)
  * [`lambda.ssh_key.remove`](#lambdassh_keyremove)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Lambda&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from lambda_python_sdk import Lambda, ApiException

lambda = Lambda(

    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD',

    access_token = 'YOUR_BEARER_TOKEN'
)

try:
    # List file systems
    get_list_response = lambda.file_system.get_list()
    print(get_list_response)
except ApiException as e:
    print("Exception when calling FileSystemApi.get_list: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from lambda_python_sdk import Lambda, ApiException

lambda = Lambda(

    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD',

    access_token = 'YOUR_BEARER_TOKEN'
)

async def main():
    try:
        # List file systems
        get_list_response = await lambda.file_system.aget_list()
        print(get_list_response)
    except ApiException as e:
        print("Exception when calling FileSystemApi.get_list: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from lambda_python_sdk import Lambda, ApiException

lambda = Lambda(

    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD',

    access_token = 'YOUR_BEARER_TOKEN'
)

try:
    # List file systems
    get_list_response = lambda.file_system.raw.get_list()
    pprint(get_list_response.body)
    pprint(get_list_response.body["data"])
    pprint(get_list_response.headers)
    pprint(get_list_response.status)
    pprint(get_list_response.round_trip_time)
except ApiException as e:
    print("Exception when calling FileSystemApi.get_list: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `lambda.file_system.get_list`<a id="lambdafile_systemget_list"></a>

Retrieve the list of file systems

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = lambda.file_system.get_list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`FileSystemGetListResponse`](./lambda_python_sdk/pydantic/file_system_get_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/file-systems` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lambda.instance.create_instances`<a id="lambdainstancecreate_instances"></a>

Launches one or more instances of a given instance type.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_instances_response = lambda.instance.create_instances(
    region_name="us-tx-1",
    instance_type_name="gpu_1x_a100",
    ssh_key_names=[
        "string_example"
    ],
    file_system_names=[
        "string_example"
    ],
    quantity=1,
    name="training-node-1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### region_name: `str`<a id="region_name-str"></a>

Short name of a region

##### instance_type_name: `str`<a id="instance_type_name-str"></a>

Name of an instance type

##### ssh_key_names: List[`SshKeyName`]<a id="ssh_key_names-listsshkeyname"></a>

Names of the SSH keys to allow access to the instances. Currently, exactly one SSH key must be specified.

##### file_system_names: List[`str`]<a id="file_system_names-liststr"></a>

Names of the file systems to attach to the instances. Currently, only one (if any) file system may be specified.

##### quantity: `int`<a id="quantity-int"></a>

Number of instances to launch

##### name: [`InstanceName`](./lambda_python_sdk/type/instance_name.py)<a id="name-instancenamelambda_python_sdktypeinstance_namepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`InstanceCreateInstancesRequest`](./lambda_python_sdk/type/instance_create_instances_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`InstanceCreateInstancesResponse`](./lambda_python_sdk/pydantic/instance_create_instances_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/instance-operations/launch` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lambda.instance.get_details`<a id="lambdainstanceget_details"></a>

Retrieves details of a specific instance, including whether or not the instance is running.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = lambda.instance.get_details(
    id="0920582c7ff041399e34823a0be62549",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The unique identifier (ID) of the instance

#### 🔄 Return<a id="🔄-return"></a>

[`InstanceGetDetailsResponse`](./lambda_python_sdk/pydantic/instance_get_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/instances/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lambda.instance.list_running_instances`<a id="lambdainstancelist_running_instances"></a>

Retrieves a detailed list of running instances.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_running_instances_response = lambda.instance.list_running_instances()
```

#### 🔄 Return<a id="🔄-return"></a>

[`InstanceListRunningInstancesResponse`](./lambda_python_sdk/pydantic/instance_list_running_instances_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/instances` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lambda.instance.restart_instances`<a id="lambdainstancerestart_instances"></a>

Restarts the given instances.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
restart_instances_response = lambda.instance.restart_instances(
    instance_ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### instance_ids: List[`str`]<a id="instance_ids-liststr"></a>

The unique identifiers (IDs) of the instances to restart

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`InstanceRestartInstancesRequest`](./lambda_python_sdk/type/instance_restart_instances_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`InstanceRestartInstancesResponse`](./lambda_python_sdk/pydantic/instance_restart_instances_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/instance-operations/restart` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lambda.instance.terminate_instance`<a id="lambdainstanceterminate_instance"></a>

Terminates a given instance.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
terminate_instance_response = lambda.instance.terminate_instance(
    instance_ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### instance_ids: List[`str`]<a id="instance_ids-liststr"></a>

The unique identifiers (IDs) of the instances to terminate

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`InstanceTerminateInstanceRequest`](./lambda_python_sdk/type/instance_terminate_instance_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`InstanceTerminateInstanceResponse`](./lambda_python_sdk/pydantic/instance_terminate_instance_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/instance-operations/terminate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lambda.instance_type.get_list`<a id="lambdainstance_typeget_list"></a>

Returns a detailed list of the instance types offered by Lambda GPU Cloud. The details include the regions, if any, in which each instance type is currently available.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = lambda.instance_type.get_list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`InstanceTypeGetListResponse`](./lambda_python_sdk/pydantic/instance_type_get_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/instance-types` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lambda.key.add_ssh_key`<a id="lambdakeyadd_ssh_key"></a>

Add an SSH key

To use an existing key pair, enter the public key for the `public_key` property of the request body.

To generate a new key pair, omit the `public_key` property from the request body. Save the `private_key` from the response somewhere secure. For example, with curl:

```
curl https://cloud.lambdalabs.com/api/v1/ssh-keys \
  --fail \
  -u ${LAMBDA_API_KEY}: \
  -X POST \
  -d '{"name": "new key"}' \
  | jq -r '.data.private_key' > key.pem

chmod 400 key.pem
```

Then, after you launch an instance with `new key` attached to it:
```
ssh -i key.pem <instance IP>
```


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_ssh_key_response = lambda.key.add_ssh_key(
    name="macbook-pro",
    public_key="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDfKpav4ILY54InZe27G user",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: [`SshKeyName`](./lambda_python_sdk/type/ssh_key_name.py)<a id="name-sshkeynamelambda_python_sdktypessh_key_namepy"></a>

##### public_key: [`SshPublicKey`](./lambda_python_sdk/type/ssh_public_key.py)<a id="public_key-sshpublickeylambda_python_sdktypessh_public_keypy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`KeyAddSshKeyRequest`](./lambda_python_sdk/type/key_add_ssh_key_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`KeyAddSshKeyResponse`](./lambda_python_sdk/pydantic/key_add_ssh_key_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/ssh-keys` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lambda.key.get_list`<a id="lambdakeyget_list"></a>

Retrieve the list of SSH keys

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = lambda.key.get_list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`KeyGetListResponse`](./lambda_python_sdk/pydantic/key_get_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/ssh-keys` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lambda.ssh_key.remove`<a id="lambdassh_keyremove"></a>

Delete an SSH key.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
lambda.ssh_key.remove(
    id="0920582c7ff041399e34823a0be62548",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The unique identifier (ID) of the SSH key

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/ssh-keys/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
