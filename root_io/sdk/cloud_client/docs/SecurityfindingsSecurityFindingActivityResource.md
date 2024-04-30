# SecurityfindingsSecurityFindingActivityResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detailed** | [**List[SecurityfindingsSecurityFindingDetailedActivityResource]**](SecurityfindingsSecurityFindingDetailedActivityResource.md) |  | [optional] 
**summary** | [**SecurityfindingsSecurityFindingActivitySummaryResource**](SecurityfindingsSecurityFindingActivitySummaryResource.md) |  | [optional] 

## Example

```python
from root_io.sdk.cloud_client.models.securityfindings_security_finding_activity_resource import SecurityfindingsSecurityFindingActivityResource

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityfindingsSecurityFindingActivityResource from a JSON string
securityfindings_security_finding_activity_resource_instance = SecurityfindingsSecurityFindingActivityResource.from_json(json)
# print the JSON string representation of the object
print(SecurityfindingsSecurityFindingActivityResource.to_json())

# convert the object into a dict
securityfindings_security_finding_activity_resource_dict = securityfindings_security_finding_activity_resource_instance.to_dict()
# create an instance of SecurityfindingsSecurityFindingActivityResource from a dict
securityfindings_security_finding_activity_resource_from_dict = SecurityfindingsSecurityFindingActivityResource.from_dict(securityfindings_security_finding_activity_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


