# ModelNotificationTarget

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**broadcast_id** | **str** | Optional. Set exactly one of UserID or BroadcastID. Specifies an integration specific destination for this notification that overrides the default. | [optional] 
**integration_id** | **str** | Required. Can be one of the special values \&quot;EMAIL\&quot; or \&quot;WEB\&quot; which does not require tenant-level configuration, and delivers notifications via email or an in-app notification respectively. Alternatively, specify the record ID of an integration inside that tenant. | [optional] 
**user_id** | **str** | Optional. Set exactly one of UserID or BroadcastID. UserID is the record ID, within a tenant, to whom this notification should be directed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


