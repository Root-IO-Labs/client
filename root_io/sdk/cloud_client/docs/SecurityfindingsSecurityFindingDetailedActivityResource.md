# SecurityfindingsSecurityFindingDetailedActivityResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**account_name** | **str** |  | [optional] 
**activity** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**comment_id** | **str** |  | [optional] 
**comment_parent_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**new_status** | [**EntitiesFindingStatus**](EntitiesFindingStatus.md) | Activity specific | [optional] 
**old_status** | [**EntitiesFindingStatus**](EntitiesFindingStatus.md) |  | [optional] 
**resolution** | [**EntitiesResolution**](EntitiesResolution.md) |  | [optional] 

## Example

```python
from root_io.sdk.cloud_client.models.securityfindings_security_finding_detailed_activity_resource import SecurityfindingsSecurityFindingDetailedActivityResource

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityfindingsSecurityFindingDetailedActivityResource from a JSON string
securityfindings_security_finding_detailed_activity_resource_instance = SecurityfindingsSecurityFindingDetailedActivityResource.from_json(json)
# print the JSON string representation of the object
print(SecurityfindingsSecurityFindingDetailedActivityResource.to_json())

# convert the object into a dict
securityfindings_security_finding_detailed_activity_resource_dict = securityfindings_security_finding_detailed_activity_resource_instance.to_dict()
# create an instance of SecurityfindingsSecurityFindingDetailedActivityResource from a dict
securityfindings_security_finding_detailed_activity_resource_from_dict = SecurityfindingsSecurityFindingDetailedActivityResource.from_dict(securityfindings_security_finding_detailed_activity_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


