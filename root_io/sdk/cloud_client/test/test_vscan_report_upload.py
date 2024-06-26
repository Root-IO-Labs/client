# coding: utf-8

"""
    Root.io API

    This is the API documentation for Root.io.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from root_io.sdk.cloud_client.models.vscan_report_upload import VscanReportUpload

class TestVscanReportUpload(unittest.TestCase):
    """VscanReportUpload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VscanReportUpload:
        """Test VscanReportUpload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VscanReportUpload`
        """
        model = VscanReportUpload()
        if include_optional:
            return VscanReportUpload(
                created_at = '',
                external_scan_ids = '',
                file_url = '',
                id = '',
                organization_id = '',
                scanner_name = 'Twistlock',
                status = 'PENDING',
                updated_at = ''
            )
        else:
            return VscanReportUpload(
        )
        """

    def testVscanReportUpload(self):
        """Test VscanReportUpload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
