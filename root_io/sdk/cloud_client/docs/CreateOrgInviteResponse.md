# CreateOrgInviteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**role** | **str** |  | [optional] 

## Example

```python
from root_io.sdk.cloud_client.models.create_org_invite_response import CreateOrgInviteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrgInviteResponse from a JSON string
create_org_invite_response_instance = CreateOrgInviteResponse.from_json(json)
# print the JSON string representation of the object
print(CreateOrgInviteResponse.to_json())

# convert the object into a dict
create_org_invite_response_dict = create_org_invite_response_instance.to_dict()
# create an instance of CreateOrgInviteResponse from a dict
create_org_invite_response_from_dict = CreateOrgInviteResponse.from_dict(create_org_invite_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


