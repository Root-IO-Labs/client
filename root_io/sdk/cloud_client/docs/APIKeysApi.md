# root_io.sdk.cloud_client.APIKeysApi

All URIs are relative to *https://api.root.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_keys_get**](APIKeysApi.md#api_keys_get) | **GET** /api_keys | List API Keys
[**api_keys_id_delete**](APIKeysApi.md#api_keys_id_delete) | **DELETE** /api_keys/{id} | Delete API Key
[**api_keys_id_get**](APIKeysApi.md#api_keys_id_get) | **GET** /api_keys/{id} | Show API Key
[**api_keys_post**](APIKeysApi.md#api_keys_post) | **POST** /api_keys | Create API Key


# **api_keys_get**
> List[APIKey] api_keys_get()

List API Keys

Get all API keys for this account, including outdated and disabled ones. It will not return the key value itself, and you have no possibility to get it. It is only possible to see the key when it is created.

### Example

* Basic Authentication (BasicAuth):

```python
import root_io.sdk.cloud_client
from root_io.sdk.cloud_client.models.api_key import APIKey
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
    api_instance = root_io.sdk.cloud_client.APIKeysApi(api_client)

    try:
        # List API Keys
        api_response = await api_instance.api_keys_get()
        print("The response of APIKeysApi->api_keys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->api_keys_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[APIKey]**](APIKey.md)

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

# **api_keys_id_delete**
> api_keys_id_delete(id)

Delete API Key

Delete API key by it's ID. Pay attention to the fact that the ID is not a key itself.

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
    api_instance = root_io.sdk.cloud_client.APIKeysApi(api_client)
    id = 'id_example' # str | API Key ID

    try:
        # Delete API Key
        await api_instance.api_keys_id_delete(id)
    except Exception as e:
        print("Exception when calling APIKeysApi->api_keys_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| API Key ID | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Key successfully deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_keys_id_get**
> APIKey api_keys_id_get(id)

Show API Key

Show API key by it's ID. Pay attention to the fact that the ID is not a key itself. It will not return the key value itself, and you have no possibility to get it. It is only possible to see the key when it is created.

### Example

* Basic Authentication (BasicAuth):

```python
import root_io.sdk.cloud_client
from root_io.sdk.cloud_client.models.api_key import APIKey
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
    api_instance = root_io.sdk.cloud_client.APIKeysApi(api_client)
    id = 'id_example' # str | API Key ID

    try:
        # Show API Key
        api_response = await api_instance.api_keys_id_get(id)
        print("The response of APIKeysApi->api_keys_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->api_keys_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| API Key ID | 

### Return type

[**APIKey**](APIKey.md)

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

# **api_keys_post**
> APIKey api_keys_post(create_api_key_request)

Create API Key

Create new API Key. It's the only possibility to see the key itself.

### Example

* Basic Authentication (BasicAuth):

```python
import root_io.sdk.cloud_client
from root_io.sdk.cloud_client.models.api_key import APIKey
from root_io.sdk.cloud_client.models.create_api_key_request import CreateAPIKeyRequest
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
    api_instance = root_io.sdk.cloud_client.APIKeysApi(api_client)
    create_api_key_request = root_io.sdk.cloud_client.CreateAPIKeyRequest() # CreateAPIKeyRequest | API Key data

    try:
        # Create API Key
        api_response = await api_instance.api_keys_post(create_api_key_request)
        print("The response of APIKeysApi->api_keys_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->api_keys_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_api_key_request** | [**CreateAPIKeyRequest**](CreateAPIKeyRequest.md)| API Key data | 

### Return type

[**APIKey**](APIKey.md)

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

