# ModelTenant

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anomaly_profile** | [**ModelTenantAnomalyProfile**](ModelTenantAnomalyProfile.md) |  | [optional] 
**data_dataset_id** | **str** |  | [optional] 
**data_project_id** | **str** | First party dataset information for this Tenant, that the ServiceAccountID has full permissions on. | [optional] 
**display_name** | **str** | Display name of this Tenant that is used in the UI. | [optional] 
**id** | **str** | Unique ID of this Tenant. | [optional] 
**service_account_id** | **str** | Utility service account for BigQuery access for tenant datasets. Not to be populated by customers but automatically by the system. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


