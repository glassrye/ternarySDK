"""
    Ternary Platform API

    Ternary Platform API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import ternary
from ternary.api.users_api import UsersApi  # noqa: E501


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_tenants_tenant_id_users_email_delete(self):
        """Test case for tenants_tenant_id_users_email_delete

        Delete User  # noqa: E501
        """
        pass

    def test_tenants_tenant_id_users_email_get(self):
        """Test case for tenants_tenant_id_users_email_get

        Get Single User by Email  # noqa: E501
        """
        pass

    def test_tenants_tenant_id_users_email_put(self):
        """Test case for tenants_tenant_id_users_email_put

        Update User  # noqa: E501
        """
        pass

    def test_tenants_tenant_id_users_get(self):
        """Test case for tenants_tenant_id_users_get

        List Users  # noqa: E501
        """
        pass

    def test_tenants_tenant_id_users_post(self):
        """Test case for tenants_tenant_id_users_post

        Create User  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
