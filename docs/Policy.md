# Policy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**list[Link]**](Link.md) |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** | Display name | [optional] 
**description** | **str** |  | [optional] 
**enabled** | **bool** | If true, the policy is active for the tenant and will be used for document classification. | [optional] 
**categories** | **list[str]** | A list of categories that the policy falls into.  Categories may be hierarchical, e.g. industry/medical | [optional] 
**tags** | **list[str]** | The tags returned from a classification operation when the policy matches a document. | [optional] 
**body** | [**PolicyBody**](PolicyBody.md) | Policy body that defines how rules are used to enforce the policy. | [optional] 
**engine_body** | **str** | Policy body in its raw engine-specific form. May be empty for custom policies. | [optional] 
**custom** | **bool** | If true the policy is a custom policy defined by a user.  If false, the policy is a standard built-in policy. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


