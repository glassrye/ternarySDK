# ternary.ResourcesApi

All URIs are relative to *https://api.ternary.app:443/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenants_tenant_id_resources_get**](ResourcesApi.md#tenants_tenant_id_resources_get) | **GET** /tenants/{tenant_id}/resources | List Resources
[**tenants_tenant_id_resources_id_delete**](ResourcesApi.md#tenants_tenant_id_resources_id_delete) | **DELETE** /tenants/{tenant_id}/resources/{id} | Delete Resource
[**tenants_tenant_id_resources_id_get**](ResourcesApi.md#tenants_tenant_id_resources_id_get) | **GET** /tenants/{tenant_id}/resources/{id} | Get Resource
[**tenants_tenant_id_resources_id_put**](ResourcesApi.md#tenants_tenant_id_resources_id_put) | **PUT** /tenants/{tenant_id}/resources/{id} | Update Resource
[**tenants_tenant_id_resources_post**](ResourcesApi.md#tenants_tenant_id_resources_post) | **POST** /tenants/{tenant_id}/resources | Create Resource


# **tenants_tenant_id_resources_get**
> [ModelResource] tenants_tenant_id_resources_get()

List Resources

Get all Resources in the Tenant matching a specified query.

### Example

```python
import time
import ternary
from ternary.api import resources_api
from ternary.model.model_resource import ModelResource
from ternary.model.api_http_error import ApiHttpError
from pprint import pprint
# Defining the host is optional and defaults to https://api.ternary.app:443/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ternary.Configuration(
    host = "https://api.ternary.app:443/v1"
)


# Enter a context with an instance of the API client
with ternary.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = resources_api.ResourcesApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID (optional)
    parents = [
        "parents_example",
    ] # [str] | Filter matching any parent Resource or Cloud Key(s) (optional)
    ids = [
        "ids_example",
    ] # [str] | Filter matching any Resource ID/s (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Resources
        api_response = api_instance.tenants_tenant_id_resources_get(tenant_id=tenant_id, parents=parents, ids=ids)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling ResourcesApi->tenants_tenant_id_resources_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID | [optional]
 **parents** | **[str]**| Filter matching any parent Resource or Cloud Key(s) | [optional]
 **ids** | **[str]**| Filter matching any Resource ID/s | [optional]

### Return type

[**[ModelResource]**](ModelResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_tenant_id_resources_id_delete**
> tenants_tenant_id_resources_id_delete(tenant_id, id)

Delete Resource

Delete a Resource within a Tenant by its ID

### Example

```python
import time
import ternary
from ternary.api import resources_api
from ternary.model.api_http_error import ApiHttpError
from pprint import pprint
# Defining the host is optional and defaults to https://api.ternary.app:443/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ternary.Configuration(
    host = "https://api.ternary.app:443/v1"
)


# Enter a context with an instance of the API client
with ternary.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = resources_api.ResourcesApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID
    id = "id_example" # str | Resource ID

    # example passing only required values which don't have defaults set
    try:
        # Delete Resource
        api_instance.tenants_tenant_id_resources_id_delete(tenant_id, id)
    except ternary.ApiException as e:
        print("Exception when calling ResourcesApi->tenants_tenant_id_resources_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |
 **id** | **str**| Resource ID |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_tenant_id_resources_id_get**
> ModelResource tenants_tenant_id_resources_id_get(tenant_id, id)

Get Resource

Get a Resource in your Tenant by its ID.

### Example

```python
import time
import ternary
from ternary.api import resources_api
from ternary.model.model_resource import ModelResource
from ternary.model.api_http_error import ApiHttpError
from pprint import pprint
# Defining the host is optional and defaults to https://api.ternary.app:443/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ternary.Configuration(
    host = "https://api.ternary.app:443/v1"
)


# Enter a context with an instance of the API client
with ternary.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = resources_api.ResourcesApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID
    id = "id_example" # str | Resource ID

    # example passing only required values which don't have defaults set
    try:
        # Get Resource
        api_response = api_instance.tenants_tenant_id_resources_id_get(tenant_id, id)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling ResourcesApi->tenants_tenant_id_resources_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |
 **id** | **str**| Resource ID |

### Return type

[**ModelResource**](ModelResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_tenant_id_resources_id_put**
> ModelResource tenants_tenant_id_resources_id_put(id, tenant_id, resource)

Update Resource

Update information or configuration in an existing Resource

### Example

```python
import time
import ternary
from ternary.api import resources_api
from ternary.model.model_resource import ModelResource
from ternary.model.api_http_error import ApiHttpError
from pprint import pprint
# Defining the host is optional and defaults to https://api.ternary.app:443/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ternary.Configuration(
    host = "https://api.ternary.app:443/v1"
)


# Enter a context with an instance of the API client
with ternary.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = resources_api.ResourcesApi(api_client)
    id = "id_example" # str | Resource ID
    tenant_id = "tenant_id_example" # str | Tenant ID
    resource = ModelResource(
        id="id_example",
        kind="kind_example",
        lineage=[
            "lineage_example",
        ],
        name="name_example",
    ) # ModelResource | Resource JSON

    # example passing only required values which don't have defaults set
    try:
        # Update Resource
        api_response = api_instance.tenants_tenant_id_resources_id_put(id, tenant_id, resource)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling ResourcesApi->tenants_tenant_id_resources_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Resource ID |
 **tenant_id** | **str**| Tenant ID |
 **resource** | [**ModelResource**](ModelResource.md)| Resource JSON |

### Return type

[**ModelResource**](ModelResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_tenant_id_resources_post**
> ModelResource tenants_tenant_id_resources_post(tenant_id, resource)

Create Resource

Create a new Resource in your Tenant.

### Example

```python
import time
import ternary
from ternary.api import resources_api
from ternary.model.model_resource import ModelResource
from ternary.model.api_http_error import ApiHttpError
from pprint import pprint
# Defining the host is optional and defaults to https://api.ternary.app:443/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ternary.Configuration(
    host = "https://api.ternary.app:443/v1"
)


# Enter a context with an instance of the API client
with ternary.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = resources_api.ResourcesApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID
    resource = ModelResource(
        id="id_example",
        kind="kind_example",
        lineage=[
            "lineage_example",
        ],
        name="name_example",
    ) # ModelResource | Resource contents

    # example passing only required values which don't have defaults set
    try:
        # Create Resource
        api_response = api_instance.tenants_tenant_id_resources_post(tenant_id, resource)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling ResourcesApi->tenants_tenant_id_resources_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |
 **resource** | [**ModelResource**](ModelResource.md)| Resource contents |

### Return type

[**ModelResource**](ModelResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

