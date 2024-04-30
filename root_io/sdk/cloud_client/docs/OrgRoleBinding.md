# OrgRoleBinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**created_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**organization** | [**Organization**](Organization.md) |  | [optional] 
**organization_id** | **str** |  | 
**role** | **str** |  | 
**updated_at** | **str** |  | [optional] 

## Example

```python
from root_io.sdk.cloud_client.models.org_role_binding import OrgRoleBinding

# TODO update the JSON string below
json = "{}"
# create an instance of OrgRoleBinding from a JSON string
org_role_binding_instance = OrgRoleBinding.from_json(json)
# print the JSON string representation of the object
print(OrgRoleBinding.to_json())

# convert the object into a dict
org_role_binding_dict = org_role_binding_instance.to_dict()
# create an instance of OrgRoleBinding from a dict
org_role_binding_from_dict = OrgRoleBinding.from_dict(org_role_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


