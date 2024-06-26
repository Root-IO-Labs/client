# coding: utf-8

"""
    Root.io API

    This is the API documentation for Root.io.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from root_io.sdk.cloud_client.models.org_role_binding import OrgRoleBinding

class TestOrgRoleBinding(unittest.TestCase):
    """OrgRoleBinding unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrgRoleBinding:
        """Test OrgRoleBinding
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrgRoleBinding`
        """
        model = OrgRoleBinding()
        if include_optional:
            return OrgRoleBinding(
                account_id = '',
                created_at = '',
                id = '',
                organization = root_io.sdk.cloud_client.models.organization.Organization(
                    created_at = '', 
                    id = '', 
                    name = '', 
                    updated_at = '', ),
                organization_id = '',
                role = '',
                updated_at = ''
            )
        else:
            return OrgRoleBinding(
                account_id = '',
                organization_id = '',
                role = '',
        )
        """

    def testOrgRoleBinding(self):
        """Test OrgRoleBinding"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
