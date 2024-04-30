# coding: utf-8

"""
    Root.io API

    This is the API documentation for Root.io.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from root_io.sdk.cloud_client.models.securityfindings_security_finding_detailed_activity_resource import SecurityfindingsSecurityFindingDetailedActivityResource

class TestSecurityfindingsSecurityFindingDetailedActivityResource(unittest.TestCase):
    """SecurityfindingsSecurityFindingDetailedActivityResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SecurityfindingsSecurityFindingDetailedActivityResource:
        """Test SecurityfindingsSecurityFindingDetailedActivityResource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SecurityfindingsSecurityFindingDetailedActivityResource`
        """
        model = SecurityfindingsSecurityFindingDetailedActivityResource()
        if include_optional:
            return SecurityfindingsSecurityFindingDetailedActivityResource(
                account_id = '',
                account_name = '',
                activity = '',
                comment = '',
                comment_id = '',
                comment_parent_id = '',
                created_at = '',
                new_status = 'Open',
                old_status = 'Open',
                resolution = 'FixedOrPatched'
            )
        else:
            return SecurityfindingsSecurityFindingDetailedActivityResource(
        )
        """

    def testSecurityfindingsSecurityFindingDetailedActivityResource(self):
        """Test SecurityfindingsSecurityFindingDetailedActivityResource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()