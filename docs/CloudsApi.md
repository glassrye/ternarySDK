# ternary.CloudsApi

All URIs are relative to *https://api.ternary.app:443/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenants_tenant_id_clouds_get**](CloudsApi.md#tenants_tenant_id_clouds_get) | **GET** /tenants/{tenant_id}/clouds | List Clouds
[**tenants_tenant_id_clouds_id_delete**](CloudsApi.md#tenants_tenant_id_clouds_id_delete) | **DELETE** /tenants/{tenant_id}/clouds/{id} | Delete Cloud
[**tenants_tenant_id_clouds_id_get**](CloudsApi.md#tenants_tenant_id_clouds_id_get) | **GET** /tenants/{tenant_id}/clouds/{id} | Get Cloud
[**tenants_tenant_id_clouds_id_put**](CloudsApi.md#tenants_tenant_id_clouds_id_put) | **PUT** /tenants/{tenant_id}/clouds/{id} | Update Cloud
[**tenants_tenant_id_clouds_id_validate_post**](CloudsApi.md#tenants_tenant_id_clouds_id_validate_post) | **POST** /tenants/{tenant_id}/clouds/{id}/validate | Validate Cloud
[**tenants_tenant_id_clouds_post**](CloudsApi.md#tenants_tenant_id_clouds_post) | **POST** /tenants/{tenant_id}/clouds | Create Cloud


# **tenants_tenant_id_clouds_get**
> [ModelCloud] tenants_tenant_id_clouds_get(tenant_id)

List Clouds

Get all Clouds in the Tenant.

### Example

```python
import time
import ternary
from ternary.api import clouds_api
from ternary.model.model_cloud import ModelCloud
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
    api_instance = clouds_api.CloudsApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID

    # example passing only required values which don't have defaults set
    try:
        # List Clouds
        api_response = api_instance.tenants_tenant_id_clouds_get(tenant_id)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling CloudsApi->tenants_tenant_id_clouds_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |

### Return type

[**[ModelCloud]**](ModelCloud.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_tenant_id_clouds_id_delete**
> tenants_tenant_id_clouds_id_delete(tenant_id, id)

Delete Cloud

Delete a Cloud within a Tenant by its ID

### Example

```python
import time
import ternary
from ternary.api import clouds_api
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
    api_instance = clouds_api.CloudsApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID
    id = "id_example" # str | Cloud ID

    # example passing only required values which don't have defaults set
    try:
        # Delete Cloud
        api_instance.tenants_tenant_id_clouds_id_delete(tenant_id, id)
    except ternary.ApiException as e:
        print("Exception when calling CloudsApi->tenants_tenant_id_clouds_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |
 **id** | **str**| Cloud ID |

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

# **tenants_tenant_id_clouds_id_get**
> ModelCloud tenants_tenant_id_clouds_id_get(tenant_id, id)

Get Cloud

Get a Cloud in your Tenant by its ID.

### Example

```python
import time
import ternary
from ternary.api import clouds_api
from ternary.model.model_cloud import ModelCloud
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
    api_instance = clouds_api.CloudsApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID
    id = "id_example" # str | Cloud ID

    # example passing only required values which don't have defaults set
    try:
        # Get Cloud
        api_response = api_instance.tenants_tenant_id_clouds_id_get(tenant_id, id)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling CloudsApi->tenants_tenant_id_clouds_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |
 **id** | **str**| Cloud ID |

### Return type

[**ModelCloud**](ModelCloud.md)

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

# **tenants_tenant_id_clouds_id_put**
> ModelCloud tenants_tenant_id_clouds_id_put(id, tenant_id, cloud)

Update Cloud

Update information or configuration in an existing Cloud

### Example

```python
import time
import ternary
from ternary.api import clouds_api
from ternary.model.model_cloud import ModelCloud
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
    api_instance = clouds_api.CloudsApi(api_client)
    id = "id_example" # str | Cloud ID
    tenant_id = "tenant_id_example" # str | Tenant ID
    cloud = ModelCloud(
        google_cloud=ModelGoogleCloud(
            big_query_monitoring=[
                ModelBigQueryMonitoring(
                    info_schema_table="info_schema_table_example",
                    project_id="project_id_example",
                    regions=[
                        "regions_example",
                    ],
                ),
            ],
            billing_account_id="billing_account_id_example",
            billing_export_source=ModelBigQueryTable(
                dataset_id="dataset_id_example",
                key="key_example",
                project_id="project_id_example",
                table_id="table_id_example",
            ),
            cud_sharing_enabled=True,
            root_element="root_element_example",
        ),
        id="id_example",
        name="name_example",
        status=ModelCloudStatus(
            code=1,
            validations=[
                ModelCloudCapability(
                    error="error_example",
                    name="name_example",
                    success=True,
                ),
            ],
        ),
    ) # ModelCloud | Cloud JSON

    # example passing only required values which don't have defaults set
    try:
        # Update Cloud
        api_response = api_instance.tenants_tenant_id_clouds_id_put(id, tenant_id, cloud)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling CloudsApi->tenants_tenant_id_clouds_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cloud ID |
 **tenant_id** | **str**| Tenant ID |
 **cloud** | [**ModelCloud**](ModelCloud.md)| Cloud JSON |

### Return type

[**ModelCloud**](ModelCloud.md)

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

# **tenants_tenant_id_clouds_id_validate_post**
> ModelCloud tenants_tenant_id_clouds_id_validate_post(id, tenant_id)

Validate Cloud

Initiate validation of a Cloud. On success, returns updated model.Cloud object which is already written back to store.

### Example

```python
import time
import ternary
from ternary.api import clouds_api
from ternary.model.model_cloud import ModelCloud
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
    api_instance = clouds_api.CloudsApi(api_client)
    id = "id_example" # str | Cloud ID
    tenant_id = "tenant_id_example" # str | Tenant ID

    # example passing only required values which don't have defaults set
    try:
        # Validate Cloud
        api_response = api_instance.tenants_tenant_id_clouds_id_validate_post(id, tenant_id)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling CloudsApi->tenants_tenant_id_clouds_id_validate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cloud ID |
 **tenant_id** | **str**| Tenant ID |

### Return type

[**ModelCloud**](ModelCloud.md)

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

# **tenants_tenant_id_clouds_post**
> ModelCloud tenants_tenant_id_clouds_post(tenant_id, cloud)

Create Cloud

Create a new Cloud in your Tenant.

### Example

```python
import time
import ternary
from ternary.api import clouds_api
from ternary.model.model_cloud import ModelCloud
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
    api_instance = clouds_api.CloudsApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID
    cloud = ModelCloud(
        google_cloud=ModelGoogleCloud(
            big_query_monitoring=[
                ModelBigQueryMonitoring(
                    info_schema_table="info_schema_table_example",
                    project_id="project_id_example",
                    regions=[
                        "regions_example",
                    ],
                ),
            ],
            billing_account_id="billing_account_id_example",
            billing_export_source=ModelBigQueryTable(
                dataset_id="dataset_id_example",
                key="key_example",
                project_id="project_id_example",
                table_id="table_id_example",
            ),
            cud_sharing_enabled=True,
            root_element="root_element_example",
        ),
        id="id_example",
        name="name_example",
        status=ModelCloudStatus(
            code=1,
            validations=[
                ModelCloudCapability(
                    error="error_example",
                    name="name_example",
                    success=True,
                ),
            ],
        ),
    ) # ModelCloud | Cloud contents

    # example passing only required values which don't have defaults set
    try:
        # Create Cloud
        api_response = api_instance.tenants_tenant_id_clouds_post(tenant_id, cloud)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling CloudsApi->tenants_tenant_id_clouds_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |
 **cloud** | [**ModelCloud**](ModelCloud.md)| Cloud contents |

### Return type

[**ModelCloud**](ModelCloud.md)

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

