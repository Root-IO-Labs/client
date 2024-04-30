# root_io.sdk.cloud_client.InviteApi

All URIs are relative to *https://api.root.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orgs_org_id_invites_invite_id_acceptance_post**](InviteApi.md#orgs_org_id_invites_invite_id_acceptance_post) | **POST** /orgs/{org_id}/invites/{invite_id}/acceptance | Accepts an organization invite
[**orgs_org_id_invites_post**](InviteApi.md#orgs_org_id_invites_post) | **POST** /orgs/{org_id}/invites | Creates an organization invite


# **orgs_org_id_invites_invite_id_acceptance_post**
> OrgRoleBinding orgs_org_id_invites_invite_id_acceptance_post(org_id, invite_id)

Accepts an organization invite

Accepts an organization invite and adds the authenticated user to the organization with the specified role.

### Example

* Basic Authentication (BasicAuth):

```python
import root_io.sdk.cloud_client
from root_io.sdk.cloud_client.models.org_role_binding import OrgRoleBinding
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
    api_instance = root_io.sdk.cloud_client.InviteApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    invite_id = 'invite_id_example' # str | Invite ID

    try:
        # Accepts an organization invite
        api_response = await api_instance.orgs_org_id_invites_invite_id_acceptance_post(org_id, invite_id)
        print("The response of InviteApi->orgs_org_id_invites_invite_id_acceptance_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InviteApi->orgs_org_id_invites_invite_id_acceptance_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **invite_id** | **str**| Invite ID | 

### Return type

[**OrgRoleBinding**](OrgRoleBinding.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_org_id_invites_post**
> CreateOrgInviteResponse orgs_org_id_invites_post(org_id, create_org_invite_request)

Creates an organization invite

### Example

* Basic Authentication (BasicAuth):

```python
import root_io.sdk.cloud_client
from root_io.sdk.cloud_client.models.create_org_invite_request import CreateOrgInviteRequest
from root_io.sdk.cloud_client.models.create_org_invite_response import CreateOrgInviteResponse
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
    api_instance = root_io.sdk.cloud_client.InviteApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    create_org_invite_request = root_io.sdk.cloud_client.CreateOrgInviteRequest() # CreateOrgInviteRequest | Invite data

    try:
        # Creates an organization invite
        api_response = await api_instance.orgs_org_id_invites_post(org_id, create_org_invite_request)
        print("The response of InviteApi->orgs_org_id_invites_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InviteApi->orgs_org_id_invites_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **create_org_invite_request** | [**CreateOrgInviteRequest**](CreateOrgInviteRequest.md)| Invite data | 

### Return type

[**CreateOrgInviteResponse**](CreateOrgInviteResponse.md)

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

