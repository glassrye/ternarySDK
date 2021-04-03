# ModelRecommendation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicable** | **bool** | The recommendation is still applicable (as far as the system knows.) If set to false, a user could have implemented the recommendation, or the condition could have disappeared on its own. This field does not distinguish between the two outcomes. | [optional] 
**assignee** | **str** | The person (User ID) assigned to review this recommendation. | [optional] 
**creation_timestamp** | **str** | When this Recommendation was created. | [optional] 
**details** | [**[ModelRecommendationDetail]**](ModelRecommendationDetail.md) | Recommendation Type specific details as key-value pairs. The Type may specify a format for the details, if not, they will be rendered as-is. | [optional] 
**estimate_usd** | **float** | Recommendations: An estimate of potential cost savings from implementing this recommendation Anomalies: How much has already been wasted due to this anomaly | [optional] 
**external_url** | **str** | External tracker link (e.g. JIRA, GitHub, GitLab issue) | [optional] 
**id** | **str** |  | [optional] 
**image_url** | **str** | ImageURL shows useful information like a graph related to this recommendation, which is suitable for inclusion in an email. | [optional] 
**kind** | **str** | The kind of recommendation: \&quot;recommendation\&quot; or \&quot;anomaly\&quot; | [optional] 
**lineage** | **[str]** | The lineage of the resource (lazy copy from the resource key above) which can be used for searching. | [optional] 
**participants** | **[str]** | List of User IDs who have ever participated in this recommendation. | [optional] 
**resource** | **str** | PRIMARY: The resource Key (string) that is to be changed in this recommendation. | [optional] 
**state** | **str** | The user-defined state of this recommendation (New is automatically set.) | [optional] 
**type** | **str** | PRIMARY: The type of recommendation (informs what page this is shown on and the documentation that is shown in the details pane.) A recommendation type is in the format: \&quot;cloud/camelCaseType\&quot; and must be matched by a registered recommendation type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


