# APIKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**created_at** | **str** |  | [optional] 
**expires_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from root_io.sdk.cloud_client.models.api_key import APIKey

# TODO update the JSON string below
json = "{}"
# create an instance of APIKey from a JSON string
api_key_instance = APIKey.from_json(json)
# print the JSON string representation of the object
print(APIKey.to_json())

# convert the object into a dict
api_key_dict = api_key_instance.to_dict()
# create an instance of APIKey from a dict
api_key_from_dict = APIKey.from_dict(api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


