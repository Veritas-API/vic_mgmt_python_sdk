# coding: utf-8

"""
    Veritas Information Classifier (VIC)

    APIs

    OpenAPI spec version: Resource Specific
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class TagsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_or_update_tag(self, tag, body, **kwargs):
        """
        Create or update tag
        Create or update a tag.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_or_update_tag(tag, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tag: (required)
        :param Tag body: Tag (required)
        :param str tenant_id: The tenant identifier
        :return: Tag
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_or_update_tag_with_http_info(tag, body, **kwargs)
        else:
            (data) = self.create_or_update_tag_with_http_info(tag, body, **kwargs)
            return data

    def create_or_update_tag_with_http_info(self, tag, body, **kwargs):
        """
        Create or update tag
        Create or update a tag.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_or_update_tag_with_http_info(tag, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tag: (required)
        :param Tag body: Tag (required)
        :param str tenant_id: The tenant identifier
        :return: Tag
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag', 'body', 'tenant_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_or_update_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tag' is set
        if ('tag' not in params) or (params['tag'] is None):
            raise ValueError("Missing the required parameter `tag` when calling `create_or_update_tag`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_or_update_tag`")


        collection_formats = {}

        resource_path = '/management/tags/{tag}'.replace('{format}', 'json')
        path_params = {}
        if 'tag' in params:
            path_params['tag'] = params['tag']

        query_params = {}
        if 'tenant_id' in params:
            query_params['tenantId'] = params['tenant_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Tag',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_tag(self, tag, **kwargs):
        """
        Delete tag
        Delete a custom tag.  (Built-in tags cannot be deleted.)
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_tag(tag, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tag: (required)
        :param str tenant_id: The tenant identifier
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_tag_with_http_info(tag, **kwargs)
        else:
            (data) = self.delete_tag_with_http_info(tag, **kwargs)
            return data

    def delete_tag_with_http_info(self, tag, **kwargs):
        """
        Delete tag
        Delete a custom tag.  (Built-in tags cannot be deleted.)
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_tag_with_http_info(tag, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tag: (required)
        :param str tenant_id: The tenant identifier
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag', 'tenant_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tag' is set
        if ('tag' not in params) or (params['tag'] is None):
            raise ValueError("Missing the required parameter `tag` when calling `delete_tag`")


        collection_formats = {}

        resource_path = '/management/tags/{tag}'.replace('{format}', 'json')
        path_params = {}
        if 'tag' in params:
            path_params['tag'] = params['tag']

        query_params = {}
        if 'tenant_id' in params:
            query_params['tenantId'] = params['tenant_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_policies_by_tag(self, tag, **kwargs):
        """
        List policies that use a tag
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_policies_by_tag(tag, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tag: (required)
        :param str tenant_id: The tenant identifier
        :return: PolicyCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_policies_by_tag_with_http_info(tag, **kwargs)
        else:
            (data) = self.get_policies_by_tag_with_http_info(tag, **kwargs)
            return data

    def get_policies_by_tag_with_http_info(self, tag, **kwargs):
        """
        List policies that use a tag
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_policies_by_tag_with_http_info(tag, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tag: (required)
        :param str tenant_id: The tenant identifier
        :return: PolicyCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag', 'tenant_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_policies_by_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tag' is set
        if ('tag' not in params) or (params['tag'] is None):
            raise ValueError("Missing the required parameter `tag` when calling `get_policies_by_tag`")


        collection_formats = {}

        resource_path = '/management/tags/{tag}/policies'.replace('{format}', 'json')
        path_params = {}
        if 'tag' in params:
            path_params['tag'] = params['tag']

        query_params = {}
        if 'tenant_id' in params:
            query_params['tenantId'] = params['tenant_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PolicyCollection',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_tag(self, tag, **kwargs):
        """
        Get tag
        Get a tag.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_tag(tag, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tag: (required)
        :param str tenant_id: The tenant identifier
        :return: Tag
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_tag_with_http_info(tag, **kwargs)
        else:
            (data) = self.get_tag_with_http_info(tag, **kwargs)
            return data

    def get_tag_with_http_info(self, tag, **kwargs):
        """
        Get tag
        Get a tag.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_tag_with_http_info(tag, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tag: (required)
        :param str tenant_id: The tenant identifier
        :return: Tag
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag', 'tenant_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tag' is set
        if ('tag' not in params) or (params['tag'] is None):
            raise ValueError("Missing the required parameter `tag` when calling `get_tag`")


        collection_formats = {}

        resource_path = '/management/tags/{tag}'.replace('{format}', 'json')
        path_params = {}
        if 'tag' in params:
            path_params['tag'] = params['tag']

        query_params = {}
        if 'tenant_id' in params:
            query_params['tenantId'] = params['tenant_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Tag',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_tag_property_definitions(self, **kwargs):
        """
        List tag property definitions
        Get definitions of properties that can be associated with a tag. This is useful, for example, for user interfaces that need to know the supported values for such properties. Generally the tag properties are application-specific and not part of the core service functionality.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_tag_property_definitions(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: The tenant identifier
        :return: TagPropertyDefinitionCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_tag_property_definitions_with_http_info(**kwargs)
        else:
            (data) = self.get_tag_property_definitions_with_http_info(**kwargs)
            return data

    def get_tag_property_definitions_with_http_info(self, **kwargs):
        """
        List tag property definitions
        Get definitions of properties that can be associated with a tag. This is useful, for example, for user interfaces that need to know the supported values for such properties. Generally the tag properties are application-specific and not part of the core service functionality.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_tag_property_definitions_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: The tenant identifier
        :return: TagPropertyDefinitionCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tag_property_definitions" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/management/tags/propertyDefinitions'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'tenant_id' in params:
            query_params['tenantId'] = params['tenant_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TagPropertyDefinitionCollection',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_tags_collection(self, **kwargs):
        """
        List tags
        Retrieve all of the tags for a tenant.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_tags_collection(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: The tenant identifier
        :param str if_none_match:
        :return: TagsCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_tags_collection_with_http_info(**kwargs)
        else:
            (data) = self.get_tags_collection_with_http_info(**kwargs)
            return data

    def get_tags_collection_with_http_info(self, **kwargs):
        """
        List tags
        Retrieve all of the tags for a tenant.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_tags_collection_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: The tenant identifier
        :param str if_none_match:
        :return: TagsCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id', 'if_none_match']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tags_collection" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/management/tags'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'tenant_id' in params:
            query_params['tenantId'] = params['tenant_id']

        header_params = {}
        if 'if_none_match' in params:
            header_params['If-None-Match'] = params['if_none_match']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TagsCollection',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
