# coding: utf-8

"""
    Root.io API

    This is the API documentation for Root.io.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from root_io.sdk.cloud_client.models.vulnerable_package_summary import VulnerablePackageSummary

class TestVulnerablePackageSummary(unittest.TestCase):
    """VulnerablePackageSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VulnerablePackageSummary:
        """Test VulnerablePackageSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VulnerablePackageSummary`
        """
        model = VulnerablePackageSummary()
        if include_optional:
            return VulnerablePackageSummary(
                critical = 56,
                ecosystem = '',
                high = 56,
                impacted_versions = [
                    ''
                    ],
                low = 56,
                medium = 56,
                name = '',
                os_distro_release = ''
            )
        else:
            return VulnerablePackageSummary(
        )
        """

    def testVulnerablePackageSummary(self):
        """Test VulnerablePackageSummary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
