# root_io.sdk.cloud_client.AccountApi

All URIs are relative to *https://api.root.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**me_get**](AccountApi.md#me_get) | **GET** /me | Get account information


# **me_get**
> Account me_get()

Get account information

Get account with all needed information: account itself, it's orgRoleBindings and organizations to these bindings.

### Example

* Basic Authentication (BasicAuth):

```python
import root_io.sdk.cloud_client
from root_io.sdk.cloud_client.models.account import Account
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
    api_instance = root_io.sdk.cloud_client.AccountApi(api_client)

    try:
        # Get account information
        api_response = await api_instance.me_get()
        print("The response of AccountApi->me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->me_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Account**](Account.md)

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

