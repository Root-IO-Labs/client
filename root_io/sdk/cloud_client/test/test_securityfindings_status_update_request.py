# coding: utf-8

"""
    Root.io API

    This is the API documentation for Root.io.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from root_io.sdk.cloud_client.models.securityfindings_status_update_request import SecurityfindingsStatusUpdateRequest

class TestSecurityfindingsStatusUpdateRequest(unittest.TestCase):
    """SecurityfindingsStatusUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SecurityfindingsStatusUpdateRequest:
        """Test SecurityfindingsStatusUpdateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SecurityfindingsStatusUpdateRequest`
        """
        model = SecurityfindingsStatusUpdateRequest()
        if include_optional:
            return SecurityfindingsStatusUpdateRequest(
                resolution = 'FixedOrPatched',
                status = 'Open'
            )
        else:
            return SecurityfindingsStatusUpdateRequest(
        )
        """

    def testSecurityfindingsStatusUpdateRequest(self):
        """Test SecurityfindingsStatusUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()