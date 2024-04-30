# VulnerablePackageSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**critical** | **int** |  | [optional] 
**ecosystem** | **str** |  | [optional] 
**high** | **int** |  | [optional] 
**impacted_versions** | **List[str]** |  | [optional] 
**low** | **int** |  | [optional] 
**medium** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**os_distro_release** | **str** |  | [optional] 

## Example

```python
from root_io.sdk.cloud_client.models.vulnerable_package_summary import VulnerablePackageSummary

# TODO update the JSON string below
json = "{}"
# create an instance of VulnerablePackageSummary from a JSON string
vulnerable_package_summary_instance = VulnerablePackageSummary.from_json(json)
# print the JSON string representation of the object
print(VulnerablePackageSummary.to_json())

# convert the object into a dict
vulnerable_package_summary_dict = vulnerable_package_summary_instance.to_dict()
# create an instance of VulnerablePackageSummary from a dict
vulnerable_package_summary_from_dict = VulnerablePackageSummary.from_dict(vulnerable_package_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


