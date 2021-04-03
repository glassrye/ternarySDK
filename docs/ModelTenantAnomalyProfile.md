# ModelTenantAnomalyProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lookback_period_seconds** | **int** | Lookback period. Defaults to 12 hours. | [optional] 
**standard_deviations** | **float** | The number of standard deviations of difference in prior hour mean spend and current hour spend, for an anomaly to be triggered. Defaults to 2. | [optional] 
**threshold** | **int** | The difference between prior hour mean spend for this (project ID, category) and the current hour spend for the same, that can trigger an anomaly. Defaults to 200. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


