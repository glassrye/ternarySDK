# ModelCustomLabel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID for this CustomLabel | [optional] 
**matched** | [**[ModelCustomLabelMatcher]**](ModelCustomLabelMatcher.md) | Existing labels against which to match rows All matchers must match -- they are combined with an AND operator | [optional] 
**output** | [**[ModelCustomLabelOutput]**](ModelCustomLabelOutput.md) | Key-value pairs to generate for each matching row | [optional] 
**sort_key** | **int** | Specifies the order in which to be applied | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


