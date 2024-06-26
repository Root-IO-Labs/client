# coding: utf-8

"""
    Root.io API

    This is the API documentation for Root.io.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from root_io.sdk.cloud_client.api.organization_api import OrganizationApi


class TestOrganizationApi(unittest.TestCase):
    """OrganizationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OrganizationApi()

    def tearDown(self) -> None:
        pass

    def test_orgs_org_id_get(self) -> None:
        """Test case for orgs_org_id_get

        Get organization by ID
        """
        pass

    def test_orgs_org_id_role_bindings_post(self) -> None:
        """Test case for orgs_org_id_role_bindings_post

        Links account to an organization
        """
        pass

    def test_orgs_post(self) -> None:
        """Test case for orgs_post

        Creates a new organization
        """
        pass


if __name__ == '__main__':
    unittest.main()
