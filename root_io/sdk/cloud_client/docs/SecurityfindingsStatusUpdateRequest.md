# SecurityfindingsStatusUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolution** | [**EntitiesResolution**](EntitiesResolution.md) | nolint: lll | [optional] 
**status** | [**EntitiesFindingStatus**](EntitiesFindingStatus.md) |  | [optional] 

## Example

```python
from root_io.sdk.cloud_client.models.securityfindings_status_update_request import SecurityfindingsStatusUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityfindingsStatusUpdateRequest from a JSON string
securityfindings_status_update_request_instance = SecurityfindingsStatusUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(SecurityfindingsStatusUpdateRequest.to_json())

# convert the object into a dict
securityfindings_status_update_request_dict = securityfindings_status_update_request_instance.to_dict()
# create an instance of SecurityfindingsStatusUpdateRequest from a dict
securityfindings_status_update_request_from_dict = SecurityfindingsStatusUpdateRequest.from_dict(securityfindings_status_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


