# OperatorNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Determines whether this node is a condition node or an operator node. NOTE: If ConditionNode &amp; OperatorNode are not visible in the Swagger UI, please consult the Swagger json for details. | 
**operator** | **str** |  | [optional] 
**min** | **int** | The minimum number of child nodes that must match.  Only applies if the operator is OR. | [optional] 
**min_overridden** | **bool** |  | [optional] 
**proximity** | **int** | Optional proximity of the first child condition to the other child conditions.  If specified, the operator must be AND, and the child nodes must all be conditions (no operators).  There must be at least two child conditions and they must all be keyword or regex.  The child conditions must not have a minCount greater than 1, and must apply to the full content (not metadata fields). | [optional] 
**proximity_mode** | **str** |  | [optional] 
**early_out** | **bool** |  | [optional] 
**children** | [**list[Node]**](Node.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


