# VscanReportUpload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**external_scan_ids** | **str** |  | [optional] 
**file_url** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**scanner_name** | [**EntitiesScannerName**](EntitiesScannerName.md) |  | [optional] 
**status** | [**EntitiesVscanReportUploadStatus**](EntitiesVscanReportUploadStatus.md) |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from root_io.sdk.cloud_client.models.vscan_report_upload import VscanReportUpload

# TODO update the JSON string below
json = "{}"
# create an instance of VscanReportUpload from a JSON string
vscan_report_upload_instance = VscanReportUpload.from_json(json)
# print the JSON string representation of the object
print(VscanReportUpload.to_json())

# convert the object into a dict
vscan_report_upload_dict = vscan_report_upload_instance.to_dict()
# create an instance of VscanReportUpload from a dict
vscan_report_upload_from_dict = VscanReportUpload.from_dict(vscan_report_upload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


