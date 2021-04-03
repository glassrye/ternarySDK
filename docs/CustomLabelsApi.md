# ternary.CustomLabelsApi

All URIs are relative to *https://api.ternary.app:443/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenants_tenant_id_clouds_cloud_id_custom_labels_custom_label_id_delete**](CustomLabelsApi.md#tenants_tenant_id_clouds_cloud_id_custom_labels_custom_label_id_delete) | **DELETE** /tenants/{tenant_id}/clouds/{cloud_id}/custom_labels/{custom_label_id} | Delete Custom Label
[**tenants_tenant_id_clouds_cloud_id_custom_labels_custom_label_id_get**](CustomLabelsApi.md#tenants_tenant_id_clouds_cloud_id_custom_labels_custom_label_id_get) | **GET** /tenants/{tenant_id}/clouds/{cloud_id}/custom_labels/{custom_label_id} | Get Custom Label
[**tenants_tenant_id_clouds_cloud_id_custom_labels_custom_label_id_put**](CustomLabelsApi.md#tenants_tenant_id_clouds_cloud_id_custom_labels_custom_label_id_put) | **PUT** /tenants/{tenant_id}/clouds/{cloud_id}/custom_labels/{custom_label_id} | Update Custom Label
[**tenants_tenant_id_clouds_cloud_id_custom_labels_get**](CustomLabelsApi.md#tenants_tenant_id_clouds_cloud_id_custom_labels_get) | **GET** /tenants/{tenant_id}/clouds/{cloud_id}/custom_labels | List Custom Labels
[**tenants_tenant_id_clouds_cloud_id_custom_labels_post**](CustomLabelsApi.md#tenants_tenant_id_clouds_cloud_id_custom_labels_post) | **POST** /tenants/{tenant_id}/clouds/{cloud_id}/custom_labels | Create Custom Labels
[**v1_tenants_tenant_id_clouds_cloud_id_all_labels_get**](CustomLabelsApi.md#v1_tenants_tenant_id_clouds_cloud_id_all_labels_get) | **GET** /v1/tenants/{tenant_id}/clouds/{cloud_id}/all_labels | List All Labels in Billing Export


# **tenants_tenant_id_clouds_cloud_id_custom_labels_custom_label_id_delete**
> tenants_tenant_id_clouds_cloud_id_custom_labels_custom_label_id_delete(tenant_id, cloud_id)

Delete Custom Label

Delete an existing Custom Label within a specific Tenant and Cloud by its ID

### Example

```python
import time
import ternary
from ternary.api import custom_labels_api
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
    api_instance = custom_labels_api.CustomLabelsApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID
    cloud_id = "cloud_id_example" # str | Cloud ID

    # example passing only required values which don't have defaults set
    try:
        # Delete Custom Label
        api_instance.tenants_tenant_id_clouds_cloud_id_custom_labels_custom_label_id_delete(tenant_id, cloud_id)
    except ternary.ApiException as e:
        print("Exception when calling CustomLabelsApi->tenants_tenant_id_clouds_cloud_id_custom_labels_custom_label_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |
 **cloud_id** | **str**| Cloud ID |

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

# **tenants_tenant_id_clouds_cloud_id_custom_labels_custom_label_id_get**
> ModelCustomLabel tenants_tenant_id_clouds_cloud_id_custom_labels_custom_label_id_get(tenant_id, cloud_id, custom_label_id)

Get Custom Label

Get a Custom Label in a Tenant's Cloud by its ID.

### Example

```python
import time
import ternary
from ternary.api import custom_labels_api
from ternary.model.api_http_error import ApiHttpError
from ternary.model.model_custom_label import ModelCustomLabel
from pprint import pprint
# Defining the host is optional and defaults to https://api.ternary.app:443/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ternary.Configuration(
    host = "https://api.ternary.app:443/v1"
)


# Enter a context with an instance of the API client
with ternary.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = custom_labels_api.CustomLabelsApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID
    cloud_id = "cloud_id_example" # str | Cloud ID
    custom_label_id = "custom_label_id_example" # str | Custom Label ID

    # example passing only required values which don't have defaults set
    try:
        # Get Custom Label
        api_response = api_instance.tenants_tenant_id_clouds_cloud_id_custom_labels_custom_label_id_get(tenant_id, cloud_id, custom_label_id)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling CustomLabelsApi->tenants_tenant_id_clouds_cloud_id_custom_labels_custom_label_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |
 **cloud_id** | **str**| Cloud ID |
 **custom_label_id** | **str**| Custom Label ID |

### Return type

[**ModelCustomLabel**](ModelCustomLabel.md)

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

# **tenants_tenant_id_clouds_cloud_id_custom_labels_custom_label_id_put**
> ModelCustomLabel tenants_tenant_id_clouds_cloud_id_custom_labels_custom_label_id_put(tenant_id, cloud_id, custom_label_id, custom_label)

Update Custom Label

Update an existing Custom Label

### Example

```python
import time
import ternary
from ternary.api import custom_labels_api
from ternary.model.api_http_error import ApiHttpError
from ternary.model.model_custom_label import ModelCustomLabel
from pprint import pprint
# Defining the host is optional and defaults to https://api.ternary.app:443/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ternary.Configuration(
    host = "https://api.ternary.app:443/v1"
)


# Enter a context with an instance of the API client
with ternary.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = custom_labels_api.CustomLabelsApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID
    cloud_id = "cloud_id_example" # str | Cloud ID
    custom_label_id = "custom_label_id_example" # str | Custom Label ID
    custom_label = ModelCustomLabel(
        id="id_example",
        matched=[
            ModelCustomLabelMatcher(
                key="key_example",
                operator="operator_example",
                values=[
                    "values_example",
                ],
            ),
        ],
        output=[
            ModelCustomLabelOutput(
                key="key_example",
                value="value_example",
            ),
        ],
        sort_key=1,
    ) # ModelCustomLabel | Custom Label JSON

    # example passing only required values which don't have defaults set
    try:
        # Update Custom Label
        api_response = api_instance.tenants_tenant_id_clouds_cloud_id_custom_labels_custom_label_id_put(tenant_id, cloud_id, custom_label_id, custom_label)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling CustomLabelsApi->tenants_tenant_id_clouds_cloud_id_custom_labels_custom_label_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |
 **cloud_id** | **str**| Cloud ID |
 **custom_label_id** | **str**| Custom Label ID |
 **custom_label** | [**ModelCustomLabel**](ModelCustomLabel.md)| Custom Label JSON |

### Return type

[**ModelCustomLabel**](ModelCustomLabel.md)

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

# **tenants_tenant_id_clouds_cloud_id_custom_labels_get**
> [ModelCustomLabel] tenants_tenant_id_clouds_cloud_id_custom_labels_get(tenant_id, cloud_id)

List Custom Labels

Get all Custom labels in the Tenant's Cloud.

### Example

```python
import time
import ternary
from ternary.api import custom_labels_api
from ternary.model.api_http_error import ApiHttpError
from ternary.model.model_custom_label import ModelCustomLabel
from pprint import pprint
# Defining the host is optional and defaults to https://api.ternary.app:443/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ternary.Configuration(
    host = "https://api.ternary.app:443/v1"
)


# Enter a context with an instance of the API client
with ternary.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = custom_labels_api.CustomLabelsApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID
    cloud_id = "cloud_id_example" # str | Cloud ID

    # example passing only required values which don't have defaults set
    try:
        # List Custom Labels
        api_response = api_instance.tenants_tenant_id_clouds_cloud_id_custom_labels_get(tenant_id, cloud_id)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling CustomLabelsApi->tenants_tenant_id_clouds_cloud_id_custom_labels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |
 **cloud_id** | **str**| Cloud ID |

### Return type

[**[ModelCustomLabel]**](ModelCustomLabel.md)

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

# **tenants_tenant_id_clouds_cloud_id_custom_labels_post**
> [ModelCustomLabel] tenants_tenant_id_clouds_cloud_id_custom_labels_post(tenant_id, cloud_id, custom_labels)

Create Custom Labels

Create new Custom Labels in the Tenant's Cloud.

### Example

```python
import time
import ternary
from ternary.api import custom_labels_api
from ternary.model.api_http_error import ApiHttpError
from ternary.model.model_custom_label import ModelCustomLabel
from pprint import pprint
# Defining the host is optional and defaults to https://api.ternary.app:443/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ternary.Configuration(
    host = "https://api.ternary.app:443/v1"
)


# Enter a context with an instance of the API client
with ternary.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = custom_labels_api.CustomLabelsApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID
    cloud_id = "cloud_id_example" # str | Cloud ID
    custom_labels = [
        ModelCustomLabel(
            id="id_example",
            matched=[
                ModelCustomLabelMatcher(
                    key="key_example",
                    operator="operator_example",
                    values=[
                        "values_example",
                    ],
                ),
            ],
            output=[
                ModelCustomLabelOutput(
                    key="key_example",
                    value="value_example",
                ),
            ],
            sort_key=1,
        ),
    ] # [ModelCustomLabel] | Custom Labels JSON

    # example passing only required values which don't have defaults set
    try:
        # Create Custom Labels
        api_response = api_instance.tenants_tenant_id_clouds_cloud_id_custom_labels_post(tenant_id, cloud_id, custom_labels)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling CustomLabelsApi->tenants_tenant_id_clouds_cloud_id_custom_labels_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |
 **cloud_id** | **str**| Cloud ID |
 **custom_labels** | [**[ModelCustomLabel]**](ModelCustomLabel.md)| Custom Labels JSON |

### Return type

[**[ModelCustomLabel]**](ModelCustomLabel.md)

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

# **v1_tenants_tenant_id_clouds_cloud_id_all_labels_get**
> [ModelKeyValues] v1_tenants_tenant_id_clouds_cloud_id_all_labels_get(tenant_id, cloud_id)

List All Labels in Billing Export

Materialize a list of all of the keys and corresponding values that currently exist in the billing export including Custom Labels

### Example

```python
import time
import ternary
from ternary.api import custom_labels_api
from ternary.model.model_key_values import ModelKeyValues
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
    api_instance = custom_labels_api.CustomLabelsApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID
    cloud_id = "cloud_id_example" # str | Cloud ID

    # example passing only required values which don't have defaults set
    try:
        # List All Labels in Billing Export
        api_response = api_instance.v1_tenants_tenant_id_clouds_cloud_id_all_labels_get(tenant_id, cloud_id)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling CustomLabelsApi->v1_tenants_tenant_id_clouds_cloud_id_all_labels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |
 **cloud_id** | **str**| Cloud ID |

### Return type

[**[ModelKeyValues]**](ModelKeyValues.md)

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

