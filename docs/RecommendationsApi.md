# ternary.RecommendationsApi

All URIs are relative to *https://api.ternary.app:443/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenants_tenant_id_recommendations_get**](RecommendationsApi.md#tenants_tenant_id_recommendations_get) | **GET** /tenants/{tenant_id}/recommendations | List Recommendations
[**tenants_tenant_id_recommendations_id_comments_get**](RecommendationsApi.md#tenants_tenant_id_recommendations_id_comments_get) | **GET** /tenants/{tenant_id}/recommendations/{id}/comments | Get Recommendation Comments
[**tenants_tenant_id_recommendations_id_comments_post**](RecommendationsApi.md#tenants_tenant_id_recommendations_id_comments_post) | **POST** /tenants/{tenant_id}/recommendations/{id}/comments | Create Recommendation Comment
[**tenants_tenant_id_recommendations_id_delete**](RecommendationsApi.md#tenants_tenant_id_recommendations_id_delete) | **DELETE** /tenants/{tenant_id}/recommendations/{id} | Delete Recommendation
[**tenants_tenant_id_recommendations_id_get**](RecommendationsApi.md#tenants_tenant_id_recommendations_id_get) | **GET** /tenants/{tenant_id}/recommendations/{id} | Get Recommendation
[**tenants_tenant_id_recommendations_id_put**](RecommendationsApi.md#tenants_tenant_id_recommendations_id_put) | **PUT** /tenants/{tenant_id}/recommendations/{id} | Update Recommendation
[**tenants_tenant_id_recommendations_post**](RecommendationsApi.md#tenants_tenant_id_recommendations_post) | **POST** /tenants/{tenant_id}/recommendations | Create Recommendation


# **tenants_tenant_id_recommendations_get**
> ModelRecommendation tenants_tenant_id_recommendations_get(tenant_id)

List Recommendations

Get a recommendation by its ID.

### Example

```python
import time
import ternary
from ternary.api import recommendations_api
from ternary.model.api_http_error import ApiHttpError
from ternary.model.model_recommendation import ModelRecommendation
from pprint import pprint
# Defining the host is optional and defaults to https://api.ternary.app:443/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ternary.Configuration(
    host = "https://api.ternary.app:443/v1"
)


# Enter a context with an instance of the API client
with ternary.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = recommendations_api.RecommendationsApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID
    ancestors = [
        "ancestors_example",
    ] # [str] | Recommendations matching Ancestor/s (optional)
    assignees = [
        "assignees_example",
    ] # [str] | Recommendations matching Assignee Email/s (optional)
    categories = [
        "categories_example",
    ] # [str] | Recommendations matching Recommendation Category/ies (optional)
    kind = "kind_example" # str | Recommendations matching a certain Kind (anomaly or recommendation) (optional)
    resources = [
        "resources_example",
    ] # [str] | Recommendations matching Resource ID/s (optional)
    types = [
        "types_example",
    ] # [str] | Recommendations matching Recommendation Type/s (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Recommendations
        api_response = api_instance.tenants_tenant_id_recommendations_get(tenant_id)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling RecommendationsApi->tenants_tenant_id_recommendations_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Recommendations
        api_response = api_instance.tenants_tenant_id_recommendations_get(tenant_id, ancestors=ancestors, assignees=assignees, categories=categories, kind=kind, resources=resources, types=types)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling RecommendationsApi->tenants_tenant_id_recommendations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |
 **ancestors** | **[str]**| Recommendations matching Ancestor/s | [optional]
 **assignees** | **[str]**| Recommendations matching Assignee Email/s | [optional]
 **categories** | **[str]**| Recommendations matching Recommendation Category/ies | [optional]
 **kind** | **str**| Recommendations matching a certain Kind (anomaly or recommendation) | [optional]
 **resources** | **[str]**| Recommendations matching Resource ID/s | [optional]
 **types** | **[str]**| Recommendations matching Recommendation Type/s | [optional]

### Return type

[**ModelRecommendation**](ModelRecommendation.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_tenant_id_recommendations_id_comments_get**
> [ModelRecommendationComment] tenants_tenant_id_recommendations_id_comments_get(tenant_id, id)

Get Recommendation Comments

Get comments for a specific recommendation ID.

### Example

```python
import time
import ternary
from ternary.api import recommendations_api
from ternary.model.model_recommendation_comment import ModelRecommendationComment
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
    api_instance = recommendations_api.RecommendationsApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID
    id = "id_example" # str | Recommendation ID

    # example passing only required values which don't have defaults set
    try:
        # Get Recommendation Comments
        api_response = api_instance.tenants_tenant_id_recommendations_id_comments_get(tenant_id, id)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling RecommendationsApi->tenants_tenant_id_recommendations_id_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |
 **id** | **str**| Recommendation ID |

### Return type

[**[ModelRecommendationComment]**](ModelRecommendationComment.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_tenant_id_recommendations_id_comments_post**
> ModelRecommendationComment tenants_tenant_id_recommendations_id_comments_post(tenant_id, id, recommendation)

Create Recommendation Comment

Create a new recommendation comment.

### Example

```python
import time
import ternary
from ternary.api import recommendations_api
from ternary.model.model_recommendation_comment import ModelRecommendationComment
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
    api_instance = recommendations_api.RecommendationsApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID
    id = "id_example" # str | Recommendation ID
    recommendation = ModelRecommendationComment(
        email="email_example",
        id="id_example",
        integration="integration_example",
        message="message_example",
        timestamp="timestamp_example",
    ) # ModelRecommendationComment | comment

    # example passing only required values which don't have defaults set
    try:
        # Create Recommendation Comment
        api_response = api_instance.tenants_tenant_id_recommendations_id_comments_post(tenant_id, id, recommendation)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling RecommendationsApi->tenants_tenant_id_recommendations_id_comments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |
 **id** | **str**| Recommendation ID |
 **recommendation** | [**ModelRecommendationComment**](ModelRecommendationComment.md)| comment |

### Return type

[**ModelRecommendationComment**](ModelRecommendationComment.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_tenant_id_recommendations_id_delete**
> tenants_tenant_id_recommendations_id_delete(id, tenant_id)

Delete Recommendation

Delete a recommendation by its ID.

### Example

```python
import time
import ternary
from ternary.api import recommendations_api
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
    api_instance = recommendations_api.RecommendationsApi(api_client)
    id = "id_example" # str | Recommendation ID
    tenant_id = "tenant_id_example" # str | Tenant ID

    # example passing only required values which don't have defaults set
    try:
        # Delete Recommendation
        api_instance.tenants_tenant_id_recommendations_id_delete(id, tenant_id)
    except ternary.ApiException as e:
        print("Exception when calling RecommendationsApi->tenants_tenant_id_recommendations_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Recommendation ID |
 **tenant_id** | **str**| Tenant ID |

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

# **tenants_tenant_id_recommendations_id_get**
> ModelRecommendation tenants_tenant_id_recommendations_id_get(tenant_id, id)

Get Recommendation

Get a recommendation by its ID.

### Example

```python
import time
import ternary
from ternary.api import recommendations_api
from ternary.model.api_http_error import ApiHttpError
from ternary.model.model_recommendation import ModelRecommendation
from pprint import pprint
# Defining the host is optional and defaults to https://api.ternary.app:443/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ternary.Configuration(
    host = "https://api.ternary.app:443/v1"
)


# Enter a context with an instance of the API client
with ternary.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = recommendations_api.RecommendationsApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID
    id = "id_example" # str | Recommendation ID

    # example passing only required values which don't have defaults set
    try:
        # Get Recommendation
        api_response = api_instance.tenants_tenant_id_recommendations_id_get(tenant_id, id)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling RecommendationsApi->tenants_tenant_id_recommendations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |
 **id** | **str**| Recommendation ID |

### Return type

[**ModelRecommendation**](ModelRecommendation.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_tenant_id_recommendations_id_put**
> ModelRecommendation tenants_tenant_id_recommendations_id_put(tenant_id, id, recommendation)

Update Recommendation

Update recommendation data. Depending on what fields you modify, different permissions are required. Most humans will need recommendation.writeMetadata to change typical fields like assignee and disposition. Ternary and custom recommenders use recommendation.write to update key information about the recommendation.

### Example

```python
import time
import ternary
from ternary.api import recommendations_api
from ternary.model.api_http_error import ApiHttpError
from ternary.model.model_recommendation import ModelRecommendation
from pprint import pprint
# Defining the host is optional and defaults to https://api.ternary.app:443/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ternary.Configuration(
    host = "https://api.ternary.app:443/v1"
)


# Enter a context with an instance of the API client
with ternary.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = recommendations_api.RecommendationsApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID
    id = "id_example" # str | Recommendation ID
    recommendation = ModelRecommendation(
        applicable=True,
        assignee="assignee_example",
        creation_timestamp="creation_timestamp_example",
        details=[
            ModelRecommendationDetail(
                key="key_example",
                value={},
            ),
        ],
        estimate_usd=3.14,
        external_url="external_url_example",
        id="id_example",
        image_url="image_url_example",
        kind="kind_example",
        lineage=[
            "lineage_example",
        ],
        participants=[
            "participants_example",
        ],
        resource="resource_example",
        state="state_example",
        type="type_example",
    ) # ModelRecommendation | recommendation

    # example passing only required values which don't have defaults set
    try:
        # Update Recommendation
        api_response = api_instance.tenants_tenant_id_recommendations_id_put(tenant_id, id, recommendation)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling RecommendationsApi->tenants_tenant_id_recommendations_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |
 **id** | **str**| Recommendation ID |
 **recommendation** | [**ModelRecommendation**](ModelRecommendation.md)| recommendation |

### Return type

[**ModelRecommendation**](ModelRecommendation.md)

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

# **tenants_tenant_id_recommendations_post**
> ModelRecommendation tenants_tenant_id_recommendations_post(tenant_id, recommendation)

Create Recommendation

Create a new recommendation. Used internally by Ternary and if you create your own recommenders.

### Example

```python
import time
import ternary
from ternary.api import recommendations_api
from ternary.model.api_http_error import ApiHttpError
from ternary.model.model_recommendation import ModelRecommendation
from pprint import pprint
# Defining the host is optional and defaults to https://api.ternary.app:443/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ternary.Configuration(
    host = "https://api.ternary.app:443/v1"
)


# Enter a context with an instance of the API client
with ternary.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = recommendations_api.RecommendationsApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID
    recommendation = ModelRecommendation(
        applicable=True,
        assignee="assignee_example",
        creation_timestamp="creation_timestamp_example",
        details=[
            ModelRecommendationDetail(
                key="key_example",
                value={},
            ),
        ],
        estimate_usd=3.14,
        external_url="external_url_example",
        id="id_example",
        image_url="image_url_example",
        kind="kind_example",
        lineage=[
            "lineage_example",
        ],
        participants=[
            "participants_example",
        ],
        resource="resource_example",
        state="state_example",
        type="type_example",
    ) # ModelRecommendation | recommendation

    # example passing only required values which don't have defaults set
    try:
        # Create Recommendation
        api_response = api_instance.tenants_tenant_id_recommendations_post(tenant_id, recommendation)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling RecommendationsApi->tenants_tenant_id_recommendations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |
 **recommendation** | [**ModelRecommendation**](ModelRecommendation.md)| recommendation |

### Return type

[**ModelRecommendation**](ModelRecommendation.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

