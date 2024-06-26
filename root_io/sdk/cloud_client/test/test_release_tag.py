# coding: utf-8

"""
    Root.io API

    This is the API documentation for Root.io.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from root_io.sdk.cloud_client.models.release_tag import ReleaseTag

class TestReleaseTag(unittest.TestCase):
    """ReleaseTag unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReleaseTag:
        """Test ReleaseTag
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReleaseTag`
        """
        model = ReleaseTag()
        if include_optional:
            return ReleaseTag(
                tag = ''
            )
        else:
            return ReleaseTag(
        )
        """

    def testReleaseTag(self):
        """Test ReleaseTag"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
