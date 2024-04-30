# ImageBuildResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**digest** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**repository** | **str** |  | [optional] 
**scanned_at** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 

## Example

```python
from root_io.sdk.cloud_client.models.image_build_response import ImageBuildResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImageBuildResponse from a JSON string
image_build_response_instance = ImageBuildResponse.from_json(json)
# print the JSON string representation of the object
print(ImageBuildResponse.to_json())

# convert the object into a dict
image_build_response_dict = image_build_response_instance.to_dict()
# create an instance of ImageBuildResponse from a dict
image_build_response_from_dict = ImageBuildResponse.from_dict(image_build_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


