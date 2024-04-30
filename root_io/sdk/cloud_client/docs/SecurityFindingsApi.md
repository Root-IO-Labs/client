# root_io.sdk.cloud_client.SecurityFindingsApi

All URIs are relative to *https://api.root.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orgs_org_id_security_findings_finding_id_comments_comment_id_delete**](SecurityFindingsApi.md#orgs_org_id_security_findings_finding_id_comments_comment_id_delete) | **DELETE** /orgs/{orgID}/security_findings/{findingID}/comments/{commentID} | Delete a comment from a security finding
[**orgs_org_id_security_findings_finding_id_comments_comment_id_put**](SecurityFindingsApi.md#orgs_org_id_security_findings_finding_id_comments_comment_id_put) | **PUT** /orgs/{orgID}/security_findings/{findingID}/comments/{commentID} | Update a comment to a security finding
[**orgs_org_id_security_findings_finding_id_comments_post**](SecurityFindingsApi.md#orgs_org_id_security_findings_finding_id_comments_post) | **POST** /orgs/{org_id}/security_findings/{finding_id}/comments | Adds a comment to a security finding
[**orgs_org_id_security_findings_finding_id_status_put**](SecurityFindingsApi.md#orgs_org_id_security_findings_finding_id_status_put) | **PUT** /orgs/{org_id}/security_findings/{finding_id}/status | Updates security finding status and resolution
[**orgs_org_id_security_findings_get**](SecurityFindingsApi.md#orgs_org_id_security_findings_get) | **GET** /orgs/{org_id}/security_findings | List security findings
[**orgs_org_id_security_findings_report_get**](SecurityFindingsApi.md#orgs_org_id_security_findings_report_get) | **GET** /orgs/{org_id}/security_findings/report | Export a security findings file


# **orgs_org_id_security_findings_finding_id_comments_comment_id_delete**
> SecurityFindingResource orgs_org_id_security_findings_finding_id_comments_comment_id_delete(org_id, finding_id, comment_id)

Delete a comment from a security finding

Delete a comment from a security finding

### Example

* Basic Authentication (BasicAuth):

```python
import root_io.sdk.cloud_client
from root_io.sdk.cloud_client.models.security_finding_resource import SecurityFindingResource
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
    api_instance = root_io.sdk.cloud_client.SecurityFindingsApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    finding_id = 'finding_id_example' # str | Security finding ID
    comment_id = 'comment_id_example' # str | Comment ID to delete

    try:
        # Delete a comment from a security finding
        api_response = await api_instance.orgs_org_id_security_findings_finding_id_comments_comment_id_delete(org_id, finding_id, comment_id)
        print("The response of SecurityFindingsApi->orgs_org_id_security_findings_finding_id_comments_comment_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityFindingsApi->orgs_org_id_security_findings_finding_id_comments_comment_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **finding_id** | **str**| Security finding ID | 
 **comment_id** | **str**| Comment ID to delete | 

### Return type

[**SecurityFindingResource**](SecurityFindingResource.md)

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

# **orgs_org_id_security_findings_finding_id_comments_comment_id_put**
> SecurityFindingResource orgs_org_id_security_findings_finding_id_comments_comment_id_put(org_id, finding_id, comment_id, comment_request)

Update a comment to a security finding

Update a comment for a security finding.

### Example

* Basic Authentication (BasicAuth):

```python
import root_io.sdk.cloud_client
from root_io.sdk.cloud_client.models.security_finding_resource import SecurityFindingResource
from root_io.sdk.cloud_client.models.securityfindings_comment_request import SecurityfindingsCommentRequest
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
    api_instance = root_io.sdk.cloud_client.SecurityFindingsApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    finding_id = 'finding_id_example' # str | Security finding ID
    comment_id = 'comment_id_example' # str | Comment ID to update
    comment_request = root_io.sdk.cloud_client.SecurityfindingsCommentRequest() # SecurityfindingsCommentRequest | Comment data

    try:
        # Update a comment to a security finding
        api_response = await api_instance.orgs_org_id_security_findings_finding_id_comments_comment_id_put(org_id, finding_id, comment_id, comment_request)
        print("The response of SecurityFindingsApi->orgs_org_id_security_findings_finding_id_comments_comment_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityFindingsApi->orgs_org_id_security_findings_finding_id_comments_comment_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **finding_id** | **str**| Security finding ID | 
 **comment_id** | **str**| Comment ID to update | 
 **comment_request** | [**SecurityfindingsCommentRequest**](SecurityfindingsCommentRequest.md)| Comment data | 

### Return type

[**SecurityFindingResource**](SecurityFindingResource.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_org_id_security_findings_finding_id_comments_post**
> SecurityFindingResource orgs_org_id_security_findings_finding_id_comments_post(org_id, finding_id, comment_request)

Adds a comment to a security finding

Add a comment (or a reply to a comment) to a security finding. A reply is defined as a comment with a parent comment id.

### Example

* Basic Authentication (BasicAuth):

```python
import root_io.sdk.cloud_client
from root_io.sdk.cloud_client.models.security_finding_resource import SecurityFindingResource
from root_io.sdk.cloud_client.models.securityfindings_comment_request import SecurityfindingsCommentRequest
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
    api_instance = root_io.sdk.cloud_client.SecurityFindingsApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    finding_id = 'finding_id_example' # str | Security finding ID
    comment_request = root_io.sdk.cloud_client.SecurityfindingsCommentRequest() # SecurityfindingsCommentRequest | Comment and parent id (if its a reply) data

    try:
        # Adds a comment to a security finding
        api_response = await api_instance.orgs_org_id_security_findings_finding_id_comments_post(org_id, finding_id, comment_request)
        print("The response of SecurityFindingsApi->orgs_org_id_security_findings_finding_id_comments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityFindingsApi->orgs_org_id_security_findings_finding_id_comments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **finding_id** | **str**| Security finding ID | 
 **comment_request** | [**SecurityfindingsCommentRequest**](SecurityfindingsCommentRequest.md)| Comment and parent id (if its a reply) data | 

### Return type

[**SecurityFindingResource**](SecurityFindingResource.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_org_id_security_findings_finding_id_status_put**
> SecurityFindingResource orgs_org_id_security_findings_finding_id_status_put(org_id, finding_id, status_update_request)

Updates security finding status and resolution

Resolution can be updated only if the current status is Mitigated/Closed, or if the provided status is Mitigated or Closed. Resolution is Mandatory if moving from a status that is not Mitigated/Closed to Mitigated/Closed

### Example

* Basic Authentication (BasicAuth):

```python
import root_io.sdk.cloud_client
from root_io.sdk.cloud_client.models.security_finding_resource import SecurityFindingResource
from root_io.sdk.cloud_client.models.securityfindings_status_update_request import SecurityfindingsStatusUpdateRequest
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
    api_instance = root_io.sdk.cloud_client.SecurityFindingsApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    finding_id = 'finding_id_example' # str | Security finding ID
    status_update_request = root_io.sdk.cloud_client.SecurityfindingsStatusUpdateRequest() # SecurityfindingsStatusUpdateRequest | Status and Resolution update data

    try:
        # Updates security finding status and resolution
        api_response = await api_instance.orgs_org_id_security_findings_finding_id_status_put(org_id, finding_id, status_update_request)
        print("The response of SecurityFindingsApi->orgs_org_id_security_findings_finding_id_status_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityFindingsApi->orgs_org_id_security_findings_finding_id_status_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **finding_id** | **str**| Security finding ID | 
 **status_update_request** | [**SecurityfindingsStatusUpdateRequest**](SecurityfindingsStatusUpdateRequest.md)| Status and Resolution update data | 

### Return type

[**SecurityFindingResource**](SecurityFindingResource.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_org_id_security_findings_get**
> List[SecurityFindingResource] orgs_org_id_security_findings_get(org_id, release_tag=release_tag, package_name=package_name, package_ecosystem=package_ecosystem, package_distro=package_distro)

List security findings

Get list of security findings for an organization, specified by ID, filtered by the release tag and the params for \"package summary tuple\": package name, package ecosystem, package distro - where all or none of the tuple is required.

### Example

* Basic Authentication (BasicAuth):

```python
import root_io.sdk.cloud_client
from root_io.sdk.cloud_client.models.security_finding_resource import SecurityFindingResource
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
    api_instance = root_io.sdk.cloud_client.SecurityFindingsApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    release_tag = 'release_tag_example' # str | Release tag (optional)
    package_name = 'package_name_example' # str | Package name (optional)
    package_ecosystem = 'package_ecosystem_example' # str | Package ecosystem (optional)
    package_distro = 'package_distro_example' # str | Package distro (optional)

    try:
        # List security findings
        api_response = await api_instance.orgs_org_id_security_findings_get(org_id, release_tag=release_tag, package_name=package_name, package_ecosystem=package_ecosystem, package_distro=package_distro)
        print("The response of SecurityFindingsApi->orgs_org_id_security_findings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityFindingsApi->orgs_org_id_security_findings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **release_tag** | **str**| Release tag | [optional] 
 **package_name** | **str**| Package name | [optional] 
 **package_ecosystem** | **str**| Package ecosystem | [optional] 
 **package_distro** | **str**| Package distro | [optional] 

### Return type

[**List[SecurityFindingResource]**](SecurityFindingResource.md)

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

# **orgs_org_id_security_findings_report_get**
> bytearray orgs_org_id_security_findings_report_get(org_id, release_tag=release_tag, format=format)

Export a security findings file

Export a detailed list of security findings for an organization, specified by release_tag.

### Example

* Basic Authentication (BasicAuth):

```python
import root_io.sdk.cloud_client
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
    api_instance = root_io.sdk.cloud_client.SecurityFindingsApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    release_tag = 'release_tag_example' # str | Release tag (optional)
    format = 'format_example' # str | file format, surrently supports 'csv' (optional)

    try:
        # Export a security findings file
        api_response = await api_instance.orgs_org_id_security_findings_report_get(org_id, release_tag=release_tag, format=format)
        print("The response of SecurityFindingsApi->orgs_org_id_security_findings_report_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityFindingsApi->orgs_org_id_security_findings_report_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **release_tag** | **str**| Release tag | [optional] 
 **format** | **str**| file format, surrently supports &#39;csv&#39; | [optional] 

### Return type

**bytearray**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

