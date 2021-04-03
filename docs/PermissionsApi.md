# ternary.PermissionsApi

All URIs are relative to *https://api.ternary.app:443/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**permissions_get**](PermissionsApi.md#permissions_get) | **GET** /permissions | List Permissions


# **permissions_get**
> [ModelPermission] permissions_get()

List Permissions

List all known permission types in the system.

### Example

```python
import time
import ternary
from ternary.api import permissions_api
from ternary.model.api_http_error import ApiHttpError
from ternary.model.model_permission import ModelPermission
from pprint import pprint
# Defining the host is optional and defaults to https://api.ternary.app:443/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ternary.Configuration(
    host = "https://api.ternary.app:443/v1"
)


# Enter a context with an instance of the API client
with ternary.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = permissions_api.PermissionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Permissions
        api_response = api_instance.permissions_get()
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling PermissionsApi->permissions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[ModelPermission]**](ModelPermission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

