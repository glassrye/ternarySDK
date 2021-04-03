# ModelNotification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**ModelNotificationContent**](ModelNotificationContent.md) |  | [optional] 
**creation_timestamp** | **str** | When this notification was created. (By extension, the notification content is also associated with this time.) | [optional] 
**id** | **str** | Internal record or row ID of this notification. | [optional] 
**target** | [**ModelNotificationTarget**](ModelNotificationTarget.md) |  | [optional] 
**tenant_id** | **str** | The tenant to which this notification belongs. | [optional] 
**viewed** | **bool** | Has this notification been viewed in the interface? Ignored for active notifications (email, slack etc.) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


