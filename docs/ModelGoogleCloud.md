# ModelGoogleCloud

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**big_query_monitoring** | [**[ModelBigQueryMonitoring]**](ModelBigQueryMonitoring.md) | If defined, customer can gain visibility over BigQuery utilization in the scope defined in this structure. | [optional] 
**billing_account_id** | **str** | Alphanumeric + hyphenated billing account ID. Used to assess projects linked to a given billing account. The billing account needs to be linked to all projects underneath the root element. | [optional] 
**billing_export_source** | [**ModelBigQueryTable**](ModelBigQueryTable.md) |  | [optional] 
**cud_sharing_enabled** | **bool** | If cross-project committed usage discount sharing is enabled, purchased CUDs will apply to all projects with the selected billing account.  If not, CUDs apply to a specific project. See Google documentation to enable or view status: https://cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#turning_on_committed_use_discount_sharing | [optional] 
**root_element** | **str** | Define the root element URI for this GoogleCloud. Valid elements would be folders and organizations. When instantiating the GoogleCloudDriver, we will try to list the contents of the RootElement. Valid entries: - organizations/XXX/folders/YYY - organizations/XXX | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


