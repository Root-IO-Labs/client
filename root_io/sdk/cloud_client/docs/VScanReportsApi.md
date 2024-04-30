# root_io.sdk.cloud_client.VScanReportsApi

All URIs are relative to *https://api.root.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orgs_org_id_vscan_reports_upload_post**](VScanReportsApi.md#orgs_org_id_vscan_reports_upload_post) | **POST** /orgs/{org_id}/vscan_reports/upload | Upload VScan Report


# **orgs_org_id_vscan_reports_upload_post**
> VscanReportUpload orgs_org_id_vscan_reports_upload_post(org_id, file, scanner_name)

Upload VScan Report

Accepts a VScan report file and processes it on behalf of the organization.

### Example

* Basic Authentication (BasicAuth):

```python
import root_io.sdk.cloud_client
from root_io.sdk.cloud_client.models.vscan_report_upload import VscanReportUpload
from root_io.sdk.cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.root.io
# See configuration.py for a list of all supported configuration parameters.
configuration = root_io.sdk.cloud_client.Configuration(
    host = "https://api.root.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = root_io.sdk.cloud_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
async with root_io.sdk.cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = root_io.sdk.cloud_client.VScanReportsApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    file = None # bytearray | VSscan report file
    scanner_name = 'scanner_name_example' # str | Scanner name

    try:
        # Upload VScan Report
        api_response = await api_instance.orgs_org_id_vscan_reports_upload_post(org_id, file, scanner_name)
        print("The response of VScanReportsApi->orgs_org_id_vscan_reports_upload_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VScanReportsApi->orgs_org_id_vscan_reports_upload_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **file** | **bytearray**| VSscan report file | 
 **scanner_name** | **str**| Scanner name | 

### Return type

[**VscanReportUpload**](VscanReportUpload.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

