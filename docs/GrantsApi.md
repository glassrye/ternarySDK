# ternary.GrantsApi

All URIs are relative to *https://api.ternary.app:443/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenants_tenant_id_grants_email_delete**](GrantsApi.md#tenants_tenant_id_grants_email_delete) | **DELETE** /tenants/{tenant_id}/grants/{email} | Delete Grant
[**tenants_tenant_id_grants_get**](GrantsApi.md#tenants_tenant_id_grants_get) | **GET** /tenants/{tenant_id}/grants | List Grants
[**tenants_tenant_id_grants_post**](GrantsApi.md#tenants_tenant_id_grants_post) | **POST** /tenants/{tenant_id}/grants | Create/Update Grant


# **tenants_tenant_id_grants_email_delete**
> tenants_tenant_id_grants_email_delete(tenant_id, email)

Delete Grant

Delete a Grant by its ID (UUID)

### Example

```python
import time
import ternary
from ternary.api import grants_api
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
    api_instance = grants_api.GrantsApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID
    email = "email_example" # str | User Email

    # example passing only required values which don't have defaults set
    try:
        # Delete Grant
        api_instance.tenants_tenant_id_grants_email_delete(tenant_id, email)
    except ternary.ApiException as e:
        print("Exception when calling GrantsApi->tenants_tenant_id_grants_email_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |
 **email** | **str**| User Email |

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_tenant_id_grants_get**
> [ModelGrant] tenants_tenant_id_grants_get(tenant_id)

List Grants

Get Grants matching all of the given criteria. Specify at most one of tenant_id, cloud_id, resource_id.

### Example

```python
import time
import ternary
from ternary.api import grants_api
from ternary.model.model_grant import ModelGrant
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
    api_instance = grants_api.GrantsApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID
    email = "email_example" # str | User Email (optional)
    cloud_id = "cloud_id_example" # str | Cloud ID (optional)
    resources = [
        "resources_example",
    ] # [str] | Resource ID(s) (optional)
    permission = "permission_example" # str | Permission (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Grants
        api_response = api_instance.tenants_tenant_id_grants_get(tenant_id)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling GrantsApi->tenants_tenant_id_grants_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Grants
        api_response = api_instance.tenants_tenant_id_grants_get(tenant_id, email=email, cloud_id=cloud_id, resources=resources, permission=permission)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling GrantsApi->tenants_tenant_id_grants_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |
 **email** | **str**| User Email | [optional]
 **cloud_id** | **str**| Cloud ID | [optional]
 **resources** | **[str]**| Resource ID(s) | [optional]
 **permission** | **str**| Permission | [optional]

### Return type

[**[ModelGrant]**](ModelGrant.md)

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

# **tenants_tenant_id_grants_post**
> ModelGrant tenants_tenant_id_grants_post(tenant_id, user)

Create/Update Grant

Create a new permission grant or set an existing one

### Example

```python
import time
import ternary
from ternary.api import grants_api
from ternary.model.model_grant import ModelGrant
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
    api_instance = grants_api.GrantsApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID
    user = ModelGrant(
        email="email_example",
        id="id_example",
        permissions=[
            "permissions_example",
        ],
        resource="resource_example",
    ) # ModelGrant | Grant contents

    # example passing only required values which don't have defaults set
    try:
        # Create/Update Grant
        api_response = api_instance.tenants_tenant_id_grants_post(tenant_id, user)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling GrantsApi->tenants_tenant_id_grants_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |
 **user** | [**ModelGrant**](ModelGrant.md)| Grant contents |

### Return type

[**ModelGrant**](ModelGrant.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

