# ternary.TenantsApi

All URIs are relative to *https://api.ternary.app:443/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenants_get**](TenantsApi.md#tenants_get) | **GET** /tenants | List Tenants
[**tenants_tenant_id_get**](TenantsApi.md#tenants_tenant_id_get) | **GET** /tenants/{tenant_id} | Get Tenant
[**tenants_tenant_id_put**](TenantsApi.md#tenants_tenant_id_put) | **PUT** /tenants/{tenant_id} | Update Tenant


# **tenants_get**
> [ModelTenant] tenants_get()

List Tenants

Get all Tenants in Ternary that you have access to.

### Example

```python
import time
import ternary
from ternary.api import tenants_api
from ternary.model.model_tenant import ModelTenant
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
    api_instance = tenants_api.TenantsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Tenants
        api_response = api_instance.tenants_get()
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling TenantsApi->tenants_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[ModelTenant]**](ModelTenant.md)

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

# **tenants_tenant_id_get**
> ModelTenant tenants_tenant_id_get(tenant_id)

Get Tenant

Get a tenant by its ID.

### Example

```python
import time
import ternary
from ternary.api import tenants_api
from ternary.model.model_tenant import ModelTenant
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
    api_instance = tenants_api.TenantsApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID

    # example passing only required values which don't have defaults set
    try:
        # Get Tenant
        api_response = api_instance.tenants_tenant_id_get(tenant_id)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling TenantsApi->tenants_tenant_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |

### Return type

[**ModelTenant**](ModelTenant.md)

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

# **tenants_tenant_id_put**
> ModelTenant tenants_tenant_id_put(tenant_id, tenant)

Update Tenant

Update an existing Tenant

### Example

```python
import time
import ternary
from ternary.api import tenants_api
from ternary.model.model_tenant import ModelTenant
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
    api_instance = tenants_api.TenantsApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID
    tenant = ModelTenant(
        anomaly_profile=ModelTenantAnomalyProfile(
            lookback_period_seconds=1,
            standard_deviations=3.14,
            threshold=1,
        ),
        data_dataset_id="data_dataset_id_example",
        data_project_id="data_project_id_example",
        display_name="display_name_example",
        id="id_example",
        service_account_id="service_account_id_example",
    ) # ModelTenant | tenant

    # example passing only required values which don't have defaults set
    try:
        # Update Tenant
        api_response = api_instance.tenants_tenant_id_put(tenant_id, tenant)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling TenantsApi->tenants_tenant_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |
 **tenant** | [**ModelTenant**](ModelTenant.md)| tenant |

### Return type

[**ModelTenant**](ModelTenant.md)

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
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

