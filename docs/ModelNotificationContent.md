# ModelNotificationContent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_event** | [**ModelBudgetEvent**](ModelBudgetEvent.md) |  | [optional] 
**daily_report_event** | [**ModelDailyReportEvent**](ModelDailyReportEvent.md) |  | [optional] 
**follow_caption** | **str** | Optional. Label associated with |followURL| | [optional] 
**follow_url** | **str** | Optional. Link that is associated with this message. Web: The link that the user travels to after seeing this notification. Email: A button is shown | [optional] 
**image_url** | **str** | Optional. URL of an image that is associated with this message. Web: Is not shown (instead, the user should be shown this image by clicking on the URL.) | [optional] 
**recommendation_event** | [**ModelRecommendationEvent**](ModelRecommendationEvent.md) |  | [optional] 
**summary** | **str** | Optional. Longer message, Markdown formatted. This version could be longer and is more appropriate for emails and Slack. The long message should not depend on the short message for context. | [optional] 
**title** | **str** | Required. Short message, NO formatting allowed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


