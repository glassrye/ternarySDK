# ternary.QueryApi

All URIs are relative to *https://api.ternary.app:443/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenants_tenant_id_clouds_cloud_id_projects_get**](QueryApi.md#tenants_tenant_id_clouds_cloud_id_projects_get) | **GET** /tenants/{tenant_id}/clouds/{cloud_id}/projects | List Projects for Tenant&#39;s Cloud
[**tenants_tenant_id_cubejs_token_post**](QueryApi.md#tenants_tenant_id_cubejs_token_post) | **POST** /tenants/{tenant_id}/cubejs-token | Generate Cube Access Token
[**zendesk_token_post**](QueryApi.md#zendesk_token_post) | **POST** /zendesk-token | Generate Zendesk Access Token


# **tenants_tenant_id_clouds_cloud_id_projects_get**
> ModelProjectListResponse tenants_tenant_id_clouds_cloud_id_projects_get(tenant_id, cloud_id)

List Projects for Tenant's Cloud

Given a tenant and a cloud, materialize a list of all of the corresponding project IDs

### Example

```python
import time
import ternary
from ternary.api import query_api
from ternary.model.api_http_error import ApiHttpError
from ternary.model.model_project_list_response import ModelProjectListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.ternary.app:443/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ternary.Configuration(
    host = "https://api.ternary.app:443/v1"
)


# Enter a context with an instance of the API client
with ternary.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = query_api.QueryApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID
    cloud_id = "cloud_id_example" # str | Cloud ID

    # example passing only required values which don't have defaults set
    try:
        # List Projects for Tenant's Cloud
        api_response = api_instance.tenants_tenant_id_clouds_cloud_id_projects_get(tenant_id, cloud_id)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling QueryApi->tenants_tenant_id_clouds_cloud_id_projects_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |
 **cloud_id** | **str**| Cloud ID |

### Return type

[**ModelProjectListResponse**](ModelProjectListResponse.md)

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

# **tenants_tenant_id_cubejs_token_post**
> CubeCubeAccessToken tenants_tenant_id_cubejs_token_post(tenant_id)

Generate Cube Access Token

Generate an access token for cube data server, scoped to the specified tenant.

### Example

```python
import time
import ternary
from ternary.api import query_api
from ternary.model.cube_cube_access_token import CubeCubeAccessToken
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
    api_instance = query_api.QueryApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID

    # example passing only required values which don't have defaults set
    try:
        # Generate Cube Access Token
        api_response = api_instance.tenants_tenant_id_cubejs_token_post(tenant_id)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling QueryApi->tenants_tenant_id_cubejs_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |

### Return type

[**CubeCubeAccessToken**](CubeCubeAccessToken.md)

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

# **zendesk_token_post**
> CubeCubeAccessToken zendesk_token_post()

Generate Zendesk Access Token

Generate an access token for use by Zendesk.

### Example

```python
import time
import ternary
from ternary.api import query_api
from ternary.model.cube_cube_access_token import CubeCubeAccessToken
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
    api_instance = query_api.QueryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Generate Zendesk Access Token
        api_response = api_instance.zendesk_token_post()
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling QueryApi->zendesk_token_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CubeCubeAccessToken**](CubeCubeAccessToken.md)

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

