# SecurityFindingResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activities** | [**SecurityfindingsSecurityFindingActivityResource**](SecurityfindingsSecurityFindingActivityResource.md) |  | [optional] 
**cvss** | **float** |  | [optional] 
**cvss_vector** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**discovered_at** | **str** |  | [optional] 
**external_vuln_id** | **str** |  | [optional] 
**fixed_in** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**image_build_digest** | **str** |  | [optional] 
**image_build_repo** | **str** |  | [optional] 
**image_build_tag** | **str** |  | [optional] 
**nvd_link** | **str** |  | [optional] 
**package_distro** | **str** |  | [optional] 
**package_ecosystem** | **str** |  | [optional] 
**package_name** | **str** |  | [optional] 
**package_version** | **str** |  | [optional] 
**published_at** | **str** |  | [optional] 
**resolution** | [**EntitiesResolution**](EntitiesResolution.md) |  | [optional] 
**scanner_name** | [**EntitiesScannerName**](EntitiesScannerName.md) |  | [optional] 
**severity** | [**EntitiesSecurityFindingSeverity**](EntitiesSecurityFindingSeverity.md) |  | [optional] 
**status** | [**EntitiesFindingStatus**](EntitiesFindingStatus.md) |  | [optional] 

## Example

```python
from root_io.sdk.cloud_client.models.security_finding_resource import SecurityFindingResource

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityFindingResource from a JSON string
security_finding_resource_instance = SecurityFindingResource.from_json(json)
# print the JSON string representation of the object
print(SecurityFindingResource.to_json())

# convert the object into a dict
security_finding_resource_dict = security_finding_resource_instance.to_dict()
# create an instance of SecurityFindingResource from a dict
security_finding_resource_from_dict = SecurityFindingResource.from_dict(security_finding_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


