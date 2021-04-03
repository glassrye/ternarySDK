# ModelBigQueryMonitoring

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info_schema_table** | **str** | Information schema table to use. Should be one of &#x60;JOBS_BY_ORGANIZATION&#x60;, &#x60;JOBS_BY_FOLDER&#x60;, &#x60;JOBS_BY_PROJECT&#x60; In all cases the specified project ID is used for the query. TODO(joshk): JOBS_BY_ORGANIZATION cannot be used outside one&#39;s own organization; you will receive an error. | [optional] 
**project_id** | **str** | Inspect the information schema of BigQuery from this project using the tenant service account. | [optional] 
**regions** | **[str]** | Include these regions for BigQuery analysis. You must manually specify all regions where you have BigQuery activity. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


