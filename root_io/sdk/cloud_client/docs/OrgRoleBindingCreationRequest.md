# OrgRoleBindingCreationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from root_io.sdk.cloud_client.models.org_role_binding_creation_request import OrgRoleBindingCreationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrgRoleBindingCreationRequest from a JSON string
org_role_binding_creation_request_instance = OrgRoleBindingCreationRequest.from_json(json)
# print the JSON string representation of the object
print(OrgRoleBindingCreationRequest.to_json())

# convert the object into a dict
org_role_binding_creation_request_dict = org_role_binding_creation_request_instance.to_dict()
# create an instance of OrgRoleBindingCreationRequest from a dict
org_role_binding_creation_request_from_dict = OrgRoleBindingCreationRequest.from_dict(org_role_binding_creation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


