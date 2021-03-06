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


class PoliciesApi(object):
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

    def create_policy(self, body, **kwargs):
        """
        Create policy
        Create a custom policy.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_policy(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Policy body: New policy (required)
        :param str tenant_id: The tenant identifier
        :return: Policy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_policy_with_http_info(body, **kwargs)
        else:
            (data) = self.create_policy_with_http_info(body, **kwargs)
            return data

    def create_policy_with_http_info(self, body, **kwargs):
        """
        Create policy
        Create a custom policy.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_policy_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Policy body: New policy (required)
        :param str tenant_id: The tenant identifier
        :return: Policy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'tenant_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_policy`")


        collection_formats = {}

        resource_path = '/management/policies'.replace('{format}', 'json')
        path_params = {}

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

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Policy',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_policy(self, id, **kwargs):
        """
        Delete policy
        Delete a custom policy.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_policy(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The policy identifier (required)
        :param str tenant_id: The tenant identifier
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_policy_with_http_info(id, **kwargs)
        else:
            (data) = self.delete_policy_with_http_info(id, **kwargs)
            return data

    def delete_policy_with_http_info(self, id, **kwargs):
        """
        Delete policy
        Delete a custom policy.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_policy_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The policy identifier (required)
        :param str tenant_id: The tenant identifier
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'tenant_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_policy`")


        collection_formats = {}

        resource_path = '/management/policies/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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

    def get_metadata_definitions(self, **kwargs):
        """
        List metadata definitions
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_metadata_definitions(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: The tenant identifier
        :return: MetadataDefinitionCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_metadata_definitions_with_http_info(**kwargs)
        else:
            (data) = self.get_metadata_definitions_with_http_info(**kwargs)
            return data

    def get_metadata_definitions_with_http_info(self, **kwargs):
        """
        List metadata definitions
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_metadata_definitions_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: The tenant identifier
        :return: MetadataDefinitionCollection
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
                    " to method get_metadata_definitions" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/management/policies/metadata'.replace('{format}', 'json')
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
                                        response_type='MetadataDefinitionCollection',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_policy(self, id, **kwargs):
        """
        Get policy
        Retrieve a policy
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_policy(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The policy identifier (required)
        :param str tenant_id: The tenant identifier
        :return: Policy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_policy_with_http_info(id, **kwargs)
        else:
            (data) = self.get_policy_with_http_info(id, **kwargs)
            return data

    def get_policy_with_http_info(self, id, **kwargs):
        """
        Get policy
        Retrieve a policy
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_policy_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The policy identifier (required)
        :param str tenant_id: The tenant identifier
        :return: Policy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'tenant_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_policy`")


        collection_formats = {}

        resource_path = '/management/policies/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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
                                        response_type='Policy',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_policy_collection(self, **kwargs):
        """
        List policies
        Retrieve the policies for a tenant.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_policy_collection(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: The tenant identifier
        :param bool include_disabled: Include disabled policies (as well as enabled ones)
        :param bool include_engine_body: Include the engine body for policies, and the engine rule sets.
        :param str if_none_match:
        :return: PolicyCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_policy_collection_with_http_info(**kwargs)
        else:
            (data) = self.get_policy_collection_with_http_info(**kwargs)
            return data

    def get_policy_collection_with_http_info(self, **kwargs):
        """
        List policies
        Retrieve the policies for a tenant.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_policy_collection_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: The tenant identifier
        :param bool include_disabled: Include disabled policies (as well as enabled ones)
        :param bool include_engine_body: Include the engine body for policies, and the engine rule sets.
        :param str if_none_match:
        :return: PolicyCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id', 'include_disabled', 'include_engine_body', 'if_none_match']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_policy_collection" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/management/policies'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'tenant_id' in params:
            query_params['tenantId'] = params['tenant_id']
        if 'include_disabled' in params:
            query_params['includeDisabled'] = params['include_disabled']
        if 'include_engine_body' in params:
            query_params['includeEngineBody'] = params['include_engine_body']

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
                                        response_type='PolicyCollection',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def patch_policy(self, id, patch, **kwargs):
        """
        Patch policy
        Update part of a policy.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_policy(id, patch, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The policy identifier (required)
        :param list[JsonPatchDocument] patch: A patch containing instructions for how the policy should be modified. See RFC 6902. (required)
        :param str tenant_id: The tenant identifier
        :return: Policy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.patch_policy_with_http_info(id, patch, **kwargs)
        else:
            (data) = self.patch_policy_with_http_info(id, patch, **kwargs)
            return data

    def patch_policy_with_http_info(self, id, patch, **kwargs):
        """
        Patch policy
        Update part of a policy.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_policy_with_http_info(id, patch, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The policy identifier (required)
        :param list[JsonPatchDocument] patch: A patch containing instructions for how the policy should be modified. See RFC 6902. (required)
        :param str tenant_id: The tenant identifier
        :return: Policy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'patch', 'tenant_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `patch_policy`")
        # verify the required parameter 'patch' is set
        if ('patch' not in params) or (params['patch'] is None):
            raise ValueError("Missing the required parameter `patch` when calling `patch_policy`")


        collection_formats = {}

        resource_path = '/management/policies/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'tenant_id' in params:
            query_params['tenantId'] = params['tenant_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'patch' in params:
            body_params = params['patch']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'application/json-patch+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PATCH',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Policy',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def reset_policy(self, id, **kwargs):
        """
        Reset policy to defaults
        Reset a policy to its default settings.  Only valid for built-in policies.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.reset_policy(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The policy identifier (required)
        :param str tenant_id: The tenant identifier
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.reset_policy_with_http_info(id, **kwargs)
        else:
            (data) = self.reset_policy_with_http_info(id, **kwargs)
            return data

    def reset_policy_with_http_info(self, id, **kwargs):
        """
        Reset policy to defaults
        Reset a policy to its default settings.  Only valid for built-in policies.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.reset_policy_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The policy identifier (required)
        :param str tenant_id: The tenant identifier
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'tenant_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reset_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `reset_policy`")


        collection_formats = {}

        resource_path = '/management/policies/{id}/overrides'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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

    def update_policy(self, id, body, **kwargs):
        """
        Update policy
        Update a policy.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_policy(id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The policy identifier (required)
        :param Policy body: Updated policy (required)
        :param str tenant_id: The tenant identifier
        :return: Policy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_policy_with_http_info(id, body, **kwargs)
        else:
            (data) = self.update_policy_with_http_info(id, body, **kwargs)
            return data

    def update_policy_with_http_info(self, id, body, **kwargs):
        """
        Update policy
        Update a policy.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_policy_with_http_info(id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The policy identifier (required)
        :param Policy body: Updated policy (required)
        :param str tenant_id: The tenant identifier
        :return: Policy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body', 'tenant_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_policy`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_policy`")


        collection_formats = {}

        resource_path = '/management/policies/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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
                                        response_type='Policy',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
