# ternary.IntegrationApi

All URIs are relative to *https://api.ternary.app:443/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenants_tenant_id_integrations_get**](IntegrationApi.md#tenants_tenant_id_integrations_get) | **GET** /tenants/{tenant_id}/integrations | List Integrations
[**tenants_tenant_id_integrations_integration_id_delete**](IntegrationApi.md#tenants_tenant_id_integrations_integration_id_delete) | **DELETE** /tenants/{tenant_id}/integrations/{integration_id} | Delete Integration
[**tenants_tenant_id_integrations_integration_id_put**](IntegrationApi.md#tenants_tenant_id_integrations_integration_id_put) | **PUT** /tenants/{tenant_id}/integrations/{integration_id} | Update Integration
[**tenants_tenant_id_integrations_integration_id_slack_channels_get**](IntegrationApi.md#tenants_tenant_id_integrations_integration_id_slack_channels_get) | **GET** /tenants/{tenant_id}/integrations/{integration_id}/slack_channels | List Channels for Slack Integration
[**tenants_tenant_id_integrations_slack_post**](IntegrationApi.md#tenants_tenant_id_integrations_slack_post) | **POST** /tenants/{tenant_id}/integrations/slack | Create Slack Integration


# **tenants_tenant_id_integrations_get**
> [ModelIntegration] tenants_tenant_id_integrations_get(tenant_id)

List Integrations

List all Integrations in the Tenant.

### Example

```python
import time
import ternary
from ternary.api import integration_api
from ternary.model.model_integration import ModelIntegration
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
    api_instance = integration_api.IntegrationApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID

    # example passing only required values which don't have defaults set
    try:
        # List Integrations
        api_response = api_instance.tenants_tenant_id_integrations_get(tenant_id)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling IntegrationApi->tenants_tenant_id_integrations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |

### Return type

[**[ModelIntegration]**](ModelIntegration.md)

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

# **tenants_tenant_id_integrations_integration_id_delete**
> tenants_tenant_id_integrations_integration_id_delete(tenant_id, integration_id, email)

Delete Integration

Delete an integration within a Tenant by its ID

### Example

```python
import time
import ternary
from ternary.api import integration_api
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
    api_instance = integration_api.IntegrationApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID
    integration_id = "integration_id_example" # str | Integration ID
    email = "email_example" # str | Email address

    # example passing only required values which don't have defaults set
    try:
        # Delete Integration
        api_instance.tenants_tenant_id_integrations_integration_id_delete(tenant_id, integration_id, email)
    except ternary.ApiException as e:
        print("Exception when calling IntegrationApi->tenants_tenant_id_integrations_integration_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |
 **integration_id** | **str**| Integration ID |
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

# **tenants_tenant_id_integrations_integration_id_put**
> ModelUser tenants_tenant_id_integrations_integration_id_put(tenant_id, integration_id, integration)

Update Integration

Update an existing integration

### Example

```python
import time
import ternary
from ternary.api import integration_api
from ternary.model.model_user import ModelUser
from ternary.model.model_integration import ModelIntegration
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
    api_instance = integration_api.IntegrationApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID
    integration_id = "integration_id_example" # str | Integration ID
    integration = ModelIntegration(
        id="id_example",
        jira={},
        name="name_example",
        slack=ModelIntegrationSlack(
            access_token="access_token_example",
            authed_user_id="authed_user_id_example",
            channel="channel_example",
            channel_display_name="channel_display_name_example",
            nonce="nonce_example",
            team="team_example",
            url="url_example",
        ),
    ) # ModelIntegration | Integration data

    # example passing only required values which don't have defaults set
    try:
        # Update Integration
        api_response = api_instance.tenants_tenant_id_integrations_integration_id_put(tenant_id, integration_id, integration)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling IntegrationApi->tenants_tenant_id_integrations_integration_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |
 **integration_id** | **str**| Integration ID |
 **integration** | [**ModelIntegration**](ModelIntegration.md)| Integration data |

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

# **tenants_tenant_id_integrations_integration_id_slack_channels_get**
> tenants_tenant_id_integrations_integration_id_slack_channels_get(tenant_id, integration_id, prefix)

List Channels for Slack Integration

For an existing, working Slack integration, list the channels starting with a given prefix.

### Example

```python
import time
import ternary
from ternary.api import integration_api
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
    api_instance = integration_api.IntegrationApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID
    integration_id = "integration_id_example" # str | Integration ID
    prefix = "prefix_example" # str | Channel Prefix

    # example passing only required values which don't have defaults set
    try:
        # List Channels for Slack Integration
        api_instance.tenants_tenant_id_integrations_integration_id_slack_channels_get(tenant_id, integration_id, prefix)
    except ternary.ApiException as e:
        print("Exception when calling IntegrationApi->tenants_tenant_id_integrations_integration_id_slack_channels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |
 **integration_id** | **str**| Integration ID |
 **prefix** | **str**| Channel Prefix |

### Return type

void (empty response body)

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

# **tenants_tenant_id_integrations_slack_post**
> tenants_tenant_id_integrations_slack_post(tenant_id)

Create Slack Integration

Kick off the process of creating a Slack integration and authentication to Slack for the user's team.

### Example

```python
import time
import ternary
from ternary.api import integration_api
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
    api_instance = integration_api.IntegrationApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID

    # example passing only required values which don't have defaults set
    try:
        # Create Slack Integration
        api_instance.tenants_tenant_id_integrations_slack_post(tenant_id)
    except ternary.ApiException as e:
        print("Exception when calling IntegrationApi->tenants_tenant_id_integrations_slack_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |

### Return type

void (empty response body)

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

