# ternary.NotificationApi

All URIs are relative to *https://api.ternary.app:443/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenants_tenant_id_notifications_get**](NotificationApi.md#tenants_tenant_id_notifications_get) | **GET** /tenants/{tenant_id}/notifications | List User Notifications


# **tenants_tenant_id_notifications_get**
> [ModelNotification] tenants_tenant_id_notifications_get(tenant_id)

List User Notifications

Get latest notifications for your own user.

### Example

```python
import time
import ternary
from ternary.api import notification_api
from ternary.model.model_notification import ModelNotification
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
    api_instance = notification_api.NotificationApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID

    # example passing only required values which don't have defaults set
    try:
        # List User Notifications
        api_response = api_instance.tenants_tenant_id_notifications_get(tenant_id)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling NotificationApi->tenants_tenant_id_notifications_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |

### Return type

[**[ModelNotification]**](ModelNotification.md)

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

