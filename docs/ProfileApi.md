# ternary.ProfileApi

All URIs are relative to *https://api.ternary.app:443/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**profile_post**](ProfileApi.md#profile_post) | **POST** /profile | Update Own Profile


# **profile_post**
> profile_post(profile)

Update Own Profile

Update your own profile globally.

### Example

```python
import time
import ternary
from ternary.api import profile_api
from ternary.model.model_profile import ModelProfile
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
    api_instance = profile_api.ProfileApi(api_client)
    profile = ModelProfile(
        email="email_example",
        name="name_example",
        picture="picture_example",
    ) # ModelProfile | User profile structure (same as ID token payload)

    # example passing only required values which don't have defaults set
    try:
        # Update Own Profile
        api_instance.profile_post(profile)
    except ternary.ApiException as e:
        print("Exception when calling ProfileApi->profile_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile** | [**ModelProfile**](ModelProfile.md)| User profile structure (same as ID token payload) |

### Return type

void (empty response body)

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

