
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.budgets_api import BudgetsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from ternary.api.budgets_api import BudgetsApi
from ternary.api.clouds_api import CloudsApi
from ternary.api.custom_labels_api import CustomLabelsApi
from ternary.api.grants_api import GrantsApi
from ternary.api.integration_api import IntegrationApi
from ternary.api.notification_api import NotificationApi
from ternary.api.permissions_api import PermissionsApi
from ternary.api.profile_api import ProfileApi
from ternary.api.query_api import QueryApi
from ternary.api.recommendation_types_api import RecommendationTypesApi
from ternary.api.recommendations_api import RecommendationsApi
from ternary.api.resources_api import ResourcesApi
from ternary.api.tenants_api import TenantsApi
from ternary.api.users_api import UsersApi
