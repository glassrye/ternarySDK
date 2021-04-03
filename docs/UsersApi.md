# ternary.UsersApi

All URIs are relative to *https://api.ternary.app:443/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenants_tenant_id_users_email_delete**](UsersApi.md#tenants_tenant_id_users_email_delete) | **DELETE** /tenants/{tenant_id}/users/{email} | Delete User
[**tenants_tenant_id_users_email_get**](UsersApi.md#tenants_tenant_id_users_email_get) | **GET** /tenants/{tenant_id}/users/{email} | Get Single User by Email
[**tenants_tenant_id_users_email_put**](UsersApi.md#tenants_tenant_id_users_email_put) | **PUT** /tenants/{tenant_id}/users/{email} | Update User
[**tenants_tenant_id_users_get**](UsersApi.md#tenants_tenant_id_users_get) | **GET** /tenants/{tenant_id}/users | List Users
[**tenants_tenant_id_users_post**](UsersApi.md#tenants_tenant_id_users_post) | **POST** /tenants/{tenant_id}/users | Create User


# **tenants_tenant_id_users_email_delete**
> tenants_tenant_id_users_email_delete(tenant_id, email)

Delete User

Delete a user within a Tenant by its email

### Example

```python
import time
import ternary
from ternary.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID
    email = "email_example" # str | Email address

    # example passing only required values which don't have defaults set
    try:
        # Delete User
        api_instance.tenants_tenant_id_users_email_delete(tenant_id, email)
    except ternary.ApiException as e:
        print("Exception when calling UsersApi->tenants_tenant_id_users_email_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |
 **email** | **str**| Email address |

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_tenant_id_users_email_get**
> V1UserWithProfile tenants_tenant_id_users_email_get(email, tenant_id, email2)

Get Single User by Email

Get a single User by Email

### Example

```python
import time
import ternary
from ternary.api import users_api
from ternary.model.v1_user_with_profile import V1UserWithProfile
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
    api_instance = users_api.UsersApi(api_client)
    email = "email_example" # str | Email address
    tenant_id = "tenant_id_example" # str | Tenant ID
    email2 = "email_example" # str | User Email

    # example passing only required values which don't have defaults set
    try:
        # Get Single User by Email
        api_response = api_instance.tenants_tenant_id_users_email_get(email, tenant_id, email2)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling UsersApi->tenants_tenant_id_users_email_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email address |
 **tenant_id** | **str**| Tenant ID |
 **email2** | **str**| User Email |

### Return type

[**V1UserWithProfile**](V1UserWithProfile.md)

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

# **tenants_tenant_id_users_email_put**
> ModelUser tenants_tenant_id_users_email_put(email, tenant_id, user)

Update User

Update an existing user of a tenant

### Example

```python
import time
import ternary
from ternary.api import users_api
from ternary.model.model_user import ModelUser
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
    api_instance = users_api.UsersApi(api_client)
    email = "email_example" # str | Email address
    tenant_id = "tenant_id_example" # str | Tenant ID
    user = ModelUser(
        default_scope="default_scope_example",
        id="id_example",
        notifications=ModelUserNotifications(
            anomalies=ModelNotificationProfile(
                all=True,
                method="method_example",
                owned=True,
                scoped=True,
            ),
            budgets=ModelNotificationProfile(
                all=True,
                method="method_example",
                owned=True,
                scoped=True,
            ),
            recommendations=ModelNotificationProfile(
                all=True,
                method="method_example",
                owned=True,
                scoped=True,
            ),
            system=ModelNotificationProfile(
                all=True,
                method="method_example",
                owned=True,
                scoped=True,
            ),
        ),
    ) # ModelUser | user

    # example passing only required values which don't have defaults set
    try:
        # Update User
        api_response = api_instance.tenants_tenant_id_users_email_put(email, tenant_id, user)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling UsersApi->tenants_tenant_id_users_email_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email address |
 **tenant_id** | **str**| Tenant ID |
 **user** | [**ModelUser**](ModelUser.md)| user |

### Return type

[**ModelUser**](ModelUser.md)

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

# **tenants_tenant_id_users_get**
> [V1UserWithProfile] tenants_tenant_id_users_get(tenant_id)

List Users

Get all Users in the Tenant.

### Example

```python
import time
import ternary
from ternary.api import users_api
from ternary.model.v1_user_with_profile import V1UserWithProfile
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
    api_instance = users_api.UsersApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID

    # example passing only required values which don't have defaults set
    try:
        # List Users
        api_response = api_instance.tenants_tenant_id_users_get(tenant_id)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling UsersApi->tenants_tenant_id_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |

### Return type

[**[V1UserWithProfile]**](V1UserWithProfile.md)

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

# **tenants_tenant_id_users_post**
> ModelUser tenants_tenant_id_users_post(tenant_id, user)

Create User

Create a new user inside this tenant.

### Example

```python
import time
import ternary
from ternary.api import users_api
from ternary.model.model_user import ModelUser
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
    api_instance = users_api.UsersApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID
    user = ModelUser(
        default_scope="default_scope_example",
        id="id_example",
        notifications=ModelUserNotifications(
            anomalies=ModelNotificationProfile(
                all=True,
                method="method_example",
                owned=True,
                scoped=True,
            ),
            budgets=ModelNotificationProfile(
                all=True,
                method="method_example",
                owned=True,
                scoped=True,
            ),
            recommendations=ModelNotificationProfile(
                all=True,
                method="method_example",
                owned=True,
                scoped=True,
            ),
            system=ModelNotificationProfile(
                all=True,
                method="method_example",
                owned=True,
                scoped=True,
            ),
        ),
    ) # ModelUser | user

    # example passing only required values which don't have defaults set
    try:
        # Create User
        api_response = api_instance.tenants_tenant_id_users_post(tenant_id, user)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling UsersApi->tenants_tenant_id_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |
 **user** | [**ModelUser**](ModelUser.md)| user |

### Return type

[**ModelUser**](ModelUser.md)

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
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

