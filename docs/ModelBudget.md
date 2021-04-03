# ModelBudget

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**ModelBudgetAmount**](ModelBudgetAmount.md) |  | [optional] 
**credit_treatment** | **str** | Specify how to treat credits when comparing MTD spend to threshold amount. | [optional] 
**id** | **str** |  | [optional] 
**metadata** | **{str: (str,)}** | Metadata | [optional] 
**name** | **str** | Display name for this budget. | [optional] 
**scopes** | [**[ModelBudgetScope]**](ModelBudgetScope.md) | Scopes, in key-values format, of spend that this budget encompasses. It is valid for multiple budgets to exist over the same scope, or for a redundant scope to be specified inside this list (e.g. one scope is fully contained within the other.) All scopes must match -- they are combined with an AND operator. | [optional] 
**source** | **str** | If set, this budget was imported from a remote source or cloud provider. Provider-specific data for this budget might be in |Metadata|. | [optional] 
**status** | [**ModelBudgetStatus**](ModelBudgetStatus.md) |  | [optional] 
**thresholds** | [**[ModelBudgetThreshold]**](ModelBudgetThreshold.md) | Threshold rules to notify for the budget. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


