# ModelResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A natural key identifying this resource within the entire Tenant. Should be globally unique (project, folder, org IDs are safe if namespaced.) | [optional] 
**kind** | **str** | Type of Resource. Only needs to make sense to the Resource. | [optional] 
**lineage** | **[str]** | A full denormalized snapshot of resource Keys (stringed) that this Resource is a child of. If the resource or any of its parents are re-parented, this will not be instantly updated and this will affect visibility and RBAC in the intermediate time. | [optional] 
**name** | **str** | The human readable name of this object as returned by the cloud provider. An instance name, bucket name, load balancer name, etc. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


