# SecurityfindingsCommentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** |  | [optional] 
**parent_comment_id** | **str** |  | [optional] 

## Example

```python
from root_io.sdk.cloud_client.models.securityfindings_comment_request import SecurityfindingsCommentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityfindingsCommentRequest from a JSON string
securityfindings_comment_request_instance = SecurityfindingsCommentRequest.from_json(json)
# print the JSON string representation of the object
print(SecurityfindingsCommentRequest.to_json())

# convert the object into a dict
securityfindings_comment_request_dict = securityfindings_comment_request_instance.to_dict()
# create an instance of SecurityfindingsCommentRequest from a dict
securityfindings_comment_request_from_dict = SecurityfindingsCommentRequest.from_dict(securityfindings_comment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


