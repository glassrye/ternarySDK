# ternary.BudgetsApi

All URIs are relative to *https://api.ternary.app:443/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_tenants_tenant_id_budgets_budget_id_delete**](BudgetsApi.md#v1_tenants_tenant_id_budgets_budget_id_delete) | **DELETE** /v1/tenants/{tenant_id}/budgets/{budget_id} | Delete Budget
[**v1_tenants_tenant_id_budgets_budget_id_get**](BudgetsApi.md#v1_tenants_tenant_id_budgets_budget_id_get) | **GET** /v1/tenants/{tenant_id}/budgets/{budget_id} | Get Budget
[**v1_tenants_tenant_id_budgets_budget_id_put**](BudgetsApi.md#v1_tenants_tenant_id_budgets_budget_id_put) | **PUT** /v1/tenants/{tenant_id}/budgets/{budget_id} | Update Budget
[**v1_tenants_tenant_id_budgets_get**](BudgetsApi.md#v1_tenants_tenant_id_budgets_get) | **GET** /v1/tenants/{tenant_id}/budgets | List Budgets
[**v1_tenants_tenant_id_budgets_post**](BudgetsApi.md#v1_tenants_tenant_id_budgets_post) | **POST** /v1/tenants/{tenant_id}/budgets | Create Budget


# **v1_tenants_tenant_id_budgets_budget_id_delete**
> v1_tenants_tenant_id_budgets_budget_id_delete(budget_id, tenant_id)

Delete Budget

Delete an existing Budget within a specific Tenant by its ID

### Example

```python
import time
import ternary
from ternary.api import budgets_api
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
    api_instance = budgets_api.BudgetsApi(api_client)
    budget_id = "budget_id_example" # str | Budget ID
    tenant_id = "tenant_id_example" # str | Tenant ID

    # example passing only required values which don't have defaults set
    try:
        # Delete Budget
        api_instance.v1_tenants_tenant_id_budgets_budget_id_delete(budget_id, tenant_id)
    except ternary.ApiException as e:
        print("Exception when calling BudgetsApi->v1_tenants_tenant_id_budgets_budget_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| Budget ID |
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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_tenants_tenant_id_budgets_budget_id_get**
> ModelBudget v1_tenants_tenant_id_budgets_budget_id_get(budget_id, tenant_id)

Get Budget

Get a Budget by its ID.

### Example

```python
import time
import ternary
from ternary.api import budgets_api
from ternary.model.api_http_error import ApiHttpError
from ternary.model.model_budget import ModelBudget
from pprint import pprint
# Defining the host is optional and defaults to https://api.ternary.app:443/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ternary.Configuration(
    host = "https://api.ternary.app:443/v1"
)


# Enter a context with an instance of the API client
with ternary.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = budgets_api.BudgetsApi(api_client)
    budget_id = "budget_id_example" # str | Budget ID
    tenant_id = "tenant_id_example" # str | Tenant ID

    # example passing only required values which don't have defaults set
    try:
        # Get Budget
        api_response = api_instance.v1_tenants_tenant_id_budgets_budget_id_get(budget_id, tenant_id)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling BudgetsApi->v1_tenants_tenant_id_budgets_budget_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| Budget ID |
 **tenant_id** | **str**| Tenant ID |

### Return type

[**ModelBudget**](ModelBudget.md)

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

# **v1_tenants_tenant_id_budgets_budget_id_put**
> ModelBudget v1_tenants_tenant_id_budgets_budget_id_put(budget_id, tenant_id, budget)

Update Budget

Update an existing Budget

### Example

```python
import time
import ternary
from ternary.api import budgets_api
from ternary.model.api_http_error import ApiHttpError
from ternary.model.model_budget import ModelBudget
from pprint import pprint
# Defining the host is optional and defaults to https://api.ternary.app:443/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ternary.Configuration(
    host = "https://api.ternary.app:443/v1"
)


# Enter a context with an instance of the API client
with ternary.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = budgets_api.BudgetsApi(api_client)
    budget_id = "budget_id_example" # str | Budget ID
    tenant_id = "tenant_id_example" # str | Tenant ID
    budget = ModelBudget(
        amount=ModelBudgetAmount(
            last_period_amount={},
            specified_amount=ModelBudgetSpecifiedAmount(
                amount=3.14,
            ),
        ),
        credit_treatment="credit_treatment_example",
        id="id_example",
        metadata={
            "key": "key_example",
        },
        name="name_example",
        scopes=[
            ModelBudgetScope(
                key="key_example",
                values=[
                    "values_example",
                ],
            ),
        ],
        source="source_example",
        status=ModelBudgetStatus(
            actual=3.14,
            breached_thresholds=[
                ModelBudgetThreshold(
                    percent=1,
                    spend_basis="spend_basis_example",
                ),
            ],
            forecasted=3.14,
            last_evaluation="last_evaluation_example",
        ),
        thresholds=[
            ModelBudgetThreshold(
                percent=1,
                spend_basis="spend_basis_example",
            ),
        ],
    ) # ModelBudget | Budget JSON

    # example passing only required values which don't have defaults set
    try:
        # Update Budget
        api_response = api_instance.v1_tenants_tenant_id_budgets_budget_id_put(budget_id, tenant_id, budget)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling BudgetsApi->v1_tenants_tenant_id_budgets_budget_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| Budget ID |
 **tenant_id** | **str**| Tenant ID |
 **budget** | [**ModelBudget**](ModelBudget.md)| Budget JSON |

### Return type

[**ModelBudget**](ModelBudget.md)

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

# **v1_tenants_tenant_id_budgets_get**
> ModelBudget v1_tenants_tenant_id_budgets_get(tenant_id)

List Budgets

Get all Budgets.

### Example

```python
import time
import ternary
from ternary.api import budgets_api
from ternary.model.api_http_error import ApiHttpError
from ternary.model.model_budget import ModelBudget
from pprint import pprint
# Defining the host is optional and defaults to https://api.ternary.app:443/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ternary.Configuration(
    host = "https://api.ternary.app:443/v1"
)


# Enter a context with an instance of the API client
with ternary.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = budgets_api.BudgetsApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID

    # example passing only required values which don't have defaults set
    try:
        # List Budgets
        api_response = api_instance.v1_tenants_tenant_id_budgets_get(tenant_id)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling BudgetsApi->v1_tenants_tenant_id_budgets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |

### Return type

[**ModelBudget**](ModelBudget.md)

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

# **v1_tenants_tenant_id_budgets_post**
> ModelBudget v1_tenants_tenant_id_budgets_post(tenant_id, budget)

Create Budget

Create a new budget for the specified Tenant.

### Example

```python
import time
import ternary
from ternary.api import budgets_api
from ternary.model.api_http_error import ApiHttpError
from ternary.model.model_budget import ModelBudget
from pprint import pprint
# Defining the host is optional and defaults to https://api.ternary.app:443/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ternary.Configuration(
    host = "https://api.ternary.app:443/v1"
)


# Enter a context with an instance of the API client
with ternary.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = budgets_api.BudgetsApi(api_client)
    tenant_id = "tenant_id_example" # str | Tenant ID
    budget = ModelBudget(
        amount=ModelBudgetAmount(
            last_period_amount={},
            specified_amount=ModelBudgetSpecifiedAmount(
                amount=3.14,
            ),
        ),
        credit_treatment="credit_treatment_example",
        id="id_example",
        metadata={
            "key": "key_example",
        },
        name="name_example",
        scopes=[
            ModelBudgetScope(
                key="key_example",
                values=[
                    "values_example",
                ],
            ),
        ],
        source="source_example",
        status=ModelBudgetStatus(
            actual=3.14,
            breached_thresholds=[
                ModelBudgetThreshold(
                    percent=1,
                    spend_basis="spend_basis_example",
                ),
            ],
            forecasted=3.14,
            last_evaluation="last_evaluation_example",
        ),
        thresholds=[
            ModelBudgetThreshold(
                percent=1,
                spend_basis="spend_basis_example",
            ),
        ],
    ) # ModelBudget | Budget JSON

    # example passing only required values which don't have defaults set
    try:
        # Create Budget
        api_response = api_instance.v1_tenants_tenant_id_budgets_post(tenant_id, budget)
        pprint(api_response)
    except ternary.ApiException as e:
        print("Exception when calling BudgetsApi->v1_tenants_tenant_id_budgets_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID |
 **budget** | [**ModelBudget**](ModelBudget.md)| Budget JSON |

### Return type

[**ModelBudget**](ModelBudget.md)

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

