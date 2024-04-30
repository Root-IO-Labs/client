# coding: utf-8

"""
    Root.io API

    This is the API documentation for Root.io.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from root_io.sdk.cloud_client.models.security_finding_resource import SecurityFindingResource

class TestSecurityFindingResource(unittest.TestCase):
    """SecurityFindingResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SecurityFindingResource:
        """Test SecurityFindingResource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SecurityFindingResource`
        """
        model = SecurityFindingResource()
        if include_optional:
            return SecurityFindingResource(
                activities = root_io.sdk.cloud_client.models.securityfindings/security_finding_activity_resource.securityfindings.SecurityFindingActivityResource(
                    detailed = [
                        root_io.sdk.cloud_client.models.securityfindings/security_finding_detailed_activity_resource.securityfindings.SecurityFindingDetailedActivityResource(
                            account_id = '', 
                            account_name = '', 
                            activity = '', 
                            comment = '', 
                            comment_id = '', 
                            comment_parent_id = '', 
                            created_at = '', 
                            new_status = root_io.sdk.cloud_client.models.new_status.new_status(), 
                            old_status = 'Open', 
                            resolution = 'FixedOrPatched', )
                        ], 
                    summary = root_io.sdk.cloud_client.models.securityfindings/security_finding_activity_summary_resource.securityfindings.SecurityFindingActivitySummaryResource(
                        number_of_comments = 56, ), ),
                cvss = 1.337,
                cvss_vector = '',
                description = '',
                discovered_at = '',
                external_vuln_id = '',
                fixed_in = '',
                id = '',
                image_build_digest = '',
                image_build_repo = '',
                image_build_tag = '',
                nvd_link = '',
                package_distro = '',
                package_ecosystem = '',
                package_name = '',
                package_version = '',
                published_at = '',
                resolution = 'FixedOrPatched',
                scanner_name = 'Twistlock',
                severity = 'Critical',
                status = 'Open'
            )
        else:
            return SecurityFindingResource(
        )
        """

    def testSecurityFindingResource(self):
        """Test SecurityFindingResource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
