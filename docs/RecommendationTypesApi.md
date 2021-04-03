# ternary.RecommendationTypesApi

All URIs are relative to *https://api.ternary.app:443/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recommendation_types_get**](RecommendationTypesApi.md#recommendation_types_get) | **GET** /recommendationTypes | List Recommendation Types
[**recommendation_types_id_get**](RecommendationTypesApi.md#recommendation_types_id_get) | **GET** /recommendationTypes/{id} | Get Recommendation Type


# **recommendation_types_get**
> [ModelRecommendationType] recommendation_types_get()

List Recommendation Types

List all known recommendation types in the system.

### Example

```python
import time
import ternary
from ternary.api import recommendation_types_api
from ternary.model.model_recommendation_type import ModelRecommendationType
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
    api_instance = recommendation_types_api.RecommendationTypesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Recommendation Types
        api_response = api_instance.recommendation_types_get()
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling RecommendationTypesApi->recommendation_types_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[ModelRecommendationType]**](ModelRecommendationType.md)

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

# **recommendation_types_id_get**
> ModelRecommendationType recommendation_types_id_get(id)

Get Recommendation Type

Get a single recommendation type by its ID.

### Example

```python
import time
import ternary
from ternary.api import recommendation_types_api
from ternary.model.model_recommendation_type import ModelRecommendationType
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
    api_instance = recommendation_types_api.RecommendationTypesApi(api_client)
    id = "id_example" # str | Recommendation Type ID

    # example passing only required values which don't have defaults set
    try:
        # Get Recommendation Type
        api_response = api_instance.recommendation_types_id_get(id)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling RecommendationTypesApi->recommendation_types_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Recommendation Type ID |

### Return type

[**ModelRecommendationType**](ModelRecommendationType.md)

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

