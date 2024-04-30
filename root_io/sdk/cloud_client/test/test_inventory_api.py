# coding: utf-8

"""
    Root.io API

    This is the API documentation for Root.io.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from root_io.sdk.cloud_client.api.inventory_api import InventoryApi


class TestInventoryApi(unittest.TestCase):
    """InventoryApi unit test stubs"""

    def setUp(self) -> None:
        self.api = InventoryApi()

    def tearDown(self) -> None:
        pass

    def test_orgs_org_id_inventory_image_builds_get(self) -> None:
        """Test case for orgs_org_id_inventory_image_builds_get

        List images' builds
        """
        pass

    def test_orgs_org_id_inventory_package_summaries_get(self) -> None:
        """Test case for orgs_org_id_inventory_package_summaries_get

        List package summaries
        """
        pass

    def test_orgs_org_id_inventory_release_tags_get(self) -> None:
        """Test case for orgs_org_id_inventory_release_tags_get

        List release tags
        """
        pass


if __name__ == '__main__':
    unittest.main()
