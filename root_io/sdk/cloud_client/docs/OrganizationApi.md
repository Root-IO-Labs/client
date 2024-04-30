# root_io.sdk.cloud_client.OrganizationApi

All URIs are relative to *https://api.root.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orgs_org_id_get**](OrganizationApi.md#orgs_org_id_get) | **GET** /orgs/{org_id} | Get organization by ID
[**orgs_org_id_role_bindings_post**](OrganizationApi.md#orgs_org_id_role_bindings_post) | **POST** /orgs/{org_id}/role_bindings | Links account to an organization
[**orgs_post**](OrganizationApi.md#orgs_post) | **POST** /orgs | Creates a new organization


# **orgs_org_id_get**
> Organization orgs_org_id_get(org_id)

Get organization by ID

Get an organization by its ID.

### Example

* Basic Authentication (BasicAuth):

```python
import root_io.sdk.cloud_client
from root_io.sdk.cloud_client.models.organization import Organization
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
    api_instance = root_io.sdk.cloud_client.OrganizationApi(api_client)
    org_id = 'org_id_example' # str | Organization ID

    try:
        # Get organization by ID
        api_response = await api_instance.orgs_org_id_get(org_id)
        print("The response of OrganizationApi->orgs_org_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->orgs_org_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 

### Return type

[**Organization**](Organization.md)

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

# **orgs_org_id_role_bindings_post**
> OrgRoleBinding orgs_org_id_role_bindings_post(org_id, org_role_binding_creation_request)

Links account to an organization

Links an account to organization, the lining information provided within payload.

### Example

* Basic Authentication (BasicAuth):

```python
import root_io.sdk.cloud_client
from root_io.sdk.cloud_client.models.org_role_binding import OrgRoleBinding
from root_io.sdk.cloud_client.models.org_role_binding_creation_request import OrgRoleBindingCreationRequest
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
    api_instance = root_io.sdk.cloud_client.OrganizationApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    org_role_binding_creation_request = root_io.sdk.cloud_client.OrgRoleBindingCreationRequest() # OrgRoleBindingCreationRequest | Role binding data

    try:
        # Links account to an organization
        api_response = await api_instance.orgs_org_id_role_bindings_post(org_id, org_role_binding_creation_request)
        print("The response of OrganizationApi->orgs_org_id_role_bindings_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->orgs_org_id_role_bindings_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **org_role_binding_creation_request** | [**OrgRoleBindingCreationRequest**](OrgRoleBindingCreationRequest.md)| Role binding data | 

### Return type

[**OrgRoleBinding**](OrgRoleBinding.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_post**
> Organization orgs_post(create_organization_request)

Creates a new organization

Creates a new organization with provided parameters. Account on whose behalf the organization is created automatically get the admin role as orgRoleBinding.

### Example

* Basic Authentication (BasicAuth):

```python
import root_io.sdk.cloud_client
from root_io.sdk.cloud_client.models.create_organization_request import CreateOrganizationRequest
from root_io.sdk.cloud_client.models.organization import Organization
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
    api_instance = root_io.sdk.cloud_client.OrganizationApi(api_client)
    create_organization_request = root_io.sdk.cloud_client.CreateOrganizationRequest() # CreateOrganizationRequest | Organization data

    try:
        # Creates a new organization
        api_response = await api_instance.orgs_post(create_organization_request)
        print("The response of OrganizationApi->orgs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->orgs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_organization_request** | [**CreateOrganizationRequest**](CreateOrganizationRequest.md)| Organization data | 

### Return type

[**Organization**](Organization.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

