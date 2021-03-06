# coding: utf-8

"""
    Veritas Information Classifier (VIC)

    APIs

    OpenAPI spec version: Resource Specific
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.tags_api import TagsApi


class TestTagsApi(unittest.TestCase):
    """ TagsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.tags_api.TagsApi()

    def tearDown(self):
        pass

    def test_create_or_update_tag(self):
        """
        Test case for create_or_update_tag

        Create or update tag
        """
        pass

    def test_delete_tag(self):
        """
        Test case for delete_tag

        Delete tag
        """
        pass

    def test_get_policies_by_tag(self):
        """
        Test case for get_policies_by_tag

        List policies that use a tag
        """
        pass

    def test_get_tag(self):
        """
        Test case for get_tag

        Get tag
        """
        pass

    def test_get_tag_property_definitions(self):
        """
        Test case for get_tag_property_definitions

        List tag property definitions
        """
        pass

    def test_get_tags_collection(self):
        """
        Test case for get_tags_collection

        List tags
        """
        pass


if __name__ == '__main__':
    unittest.main()
