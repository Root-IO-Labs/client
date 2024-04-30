# Account


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**email** | **str** |  | 
**external_id** | **str** |  | 
**id** | **str** |  | [optional] 
**last_login_at** | **str** |  | [optional] 
**name** | **str** |  | 
**org_role_bindings** | [**List[OrgRoleBinding]**](OrgRoleBinding.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from root_io.sdk.cloud_client.models.account import Account

# TODO update the JSON string below
json = "{}"
# create an instance of Account from a JSON string
account_instance = Account.from_json(json)
# print the JSON string representation of the object
print(Account.to_json())

# convert the object into a dict
account_dict = account_instance.to_dict()
# create an instance of Account from a dict
account_from_dict = Account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


