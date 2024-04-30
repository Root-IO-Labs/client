# root_io.sdk.cloud_client.InventoryApi

All URIs are relative to *https://api.root.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orgs_org_id_inventory_image_builds_get**](InventoryApi.md#orgs_org_id_inventory_image_builds_get) | **GET** /orgs/{org_id}/inventory/image_builds | List images&#39; builds
[**orgs_org_id_inventory_package_summaries_get**](InventoryApi.md#orgs_org_id_inventory_package_summaries_get) | **GET** /orgs/{org_id}/inventory/package_summaries | List package summaries
[**orgs_org_id_inventory_release_tags_get**](InventoryApi.md#orgs_org_id_inventory_release_tags_get) | **GET** /orgs/{org_id}/inventory/release_tags | List release tags


# **orgs_org_id_inventory_image_builds_get**
> List[ImageBuildResponse] orgs_org_id_inventory_image_builds_get(org_id)

List images' builds

Retrieves an images' build list for given organization.

### Example

* Basic Authentication (BasicAuth):

```python
import root_io.sdk.cloud_client
from root_io.sdk.cloud_client.models.image_build_response import ImageBuildResponse
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
    api_instance = root_io.sdk.cloud_client.InventoryApi(api_client)
    org_id = 'org_id_example' # str | Organization ID

    try:
        # List images' builds
        api_response = await api_instance.orgs_org_id_inventory_image_builds_get(org_id)
        print("The response of InventoryApi->orgs_org_id_inventory_image_builds_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->orgs_org_id_inventory_image_builds_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 

### Return type

[**List[ImageBuildResponse]**](ImageBuildResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_org_id_inventory_package_summaries_get**
> List[VulnerablePackageSummary] orgs_org_id_inventory_package_summaries_get(org_id, release_tag)

List package summaries

Retrieves package summaries for a given organization and release tags.

### Example

* Basic Authentication (BasicAuth):

```python
import root_io.sdk.cloud_client
from root_io.sdk.cloud_client.models.vulnerable_package_summary import VulnerablePackageSummary
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
    api_instance = root_io.sdk.cloud_client.InventoryApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    release_tag = 'release_tag_example' # str | Release tags for which package summaries will be returned for

    try:
        # List package summaries
        api_response = await api_instance.orgs_org_id_inventory_package_summaries_get(org_id, release_tag)
        print("The response of InventoryApi->orgs_org_id_inventory_package_summaries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->orgs_org_id_inventory_package_summaries_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **release_tag** | **str**| Release tags for which package summaries will be returned for | 

### Return type

[**List[VulnerablePackageSummary]**](VulnerablePackageSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_org_id_inventory_release_tags_get**
> List[ReleaseTag] orgs_org_id_inventory_release_tags_get(org_id)

List release tags

Retrieves release tags for given organization.

### Example

* Basic Authentication (BasicAuth):

```python
import root_io.sdk.cloud_client
from root_io.sdk.cloud_client.models.release_tag import ReleaseTag
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
    api_instance = root_io.sdk.cloud_client.InventoryApi(api_client)
    org_id = 'org_id_example' # str | Organization ID

    try:
        # List release tags
        api_response = await api_instance.orgs_org_id_inventory_release_tags_get(org_id)
        print("The response of InventoryApi->orgs_org_id_inventory_release_tags_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->orgs_org_id_inventory_release_tags_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 

### Return type

[**List[ReleaseTag]**](ReleaseTag.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

