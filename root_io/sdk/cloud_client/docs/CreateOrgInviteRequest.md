# CreateOrgInviteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 

## Example

```python
from root_io.sdk.cloud_client.models.create_org_invite_request import CreateOrgInviteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrgInviteRequest from a JSON string
create_org_invite_request_instance = CreateOrgInviteRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrgInviteRequest.to_json())

# convert the object into a dict
create_org_invite_request_dict = create_org_invite_request_instance.to_dict()
# create an instance of CreateOrgInviteRequest from a dict
create_org_invite_request_from_dict = CreateOrgInviteRequest.from_dict(create_org_invite_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


