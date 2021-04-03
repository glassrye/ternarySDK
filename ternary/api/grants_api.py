"""
    Ternary Platform API

    Ternary Platform API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ternary.api_client import ApiClient, Endpoint as _Endpoint
from ternary.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from ternary.model.api_http_error import ApiHttpError
from ternary.model.model_grant import ModelGrant


class GrantsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __tenants_tenant_id_grants_email_delete(
            self,
            tenant_id,
            email,
            **kwargs
        ):
            """Delete Grant  # noqa: E501

            Delete a Grant by its ID (UUID)  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.tenants_tenant_id_grants_email_delete(tenant_id, email, async_req=True)
            >>> result = thread.get()

            Args:
                tenant_id (str): Tenant ID
                email (str): User Email

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['tenant_id'] = \
                tenant_id
            kwargs['email'] = \
                email
            return self.call_with_http_info(**kwargs)

        self.tenants_tenant_id_grants_email_delete = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/tenants/{tenant_id}/grants/{email}',
                'operation_id': 'tenants_tenant_id_grants_email_delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'tenant_id',
                    'email',
                ],
                'required': [
                    'tenant_id',
                    'email',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'tenant_id':
                        (str,),
                    'email':
                        (str,),
                },
                'attribute_map': {
                    'tenant_id': 'tenant_id',
                    'email': 'email',
                },
                'location_map': {
                    'tenant_id': 'path',
                    'email': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    '*/*'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__tenants_tenant_id_grants_email_delete
        )

        def __tenants_tenant_id_grants_get(
            self,
            tenant_id,
            **kwargs
        ):
            """List Grants  # noqa: E501

            Get Grants matching all of the given criteria. Specify at most one of tenant_id, cloud_id, resource_id.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.tenants_tenant_id_grants_get(tenant_id, async_req=True)
            >>> result = thread.get()

            Args:
                tenant_id (str): Tenant ID

            Keyword Args:
                email (str): User Email. [optional]
                cloud_id (str): Cloud ID. [optional]
                resources ([str]): Resource ID(s). [optional]
                permission (str): Permission. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [ModelGrant]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['tenant_id'] = \
                tenant_id
            return self.call_with_http_info(**kwargs)

        self.tenants_tenant_id_grants_get = _Endpoint(
            settings={
                'response_type': ([ModelGrant],),
                'auth': [],
                'endpoint_path': '/tenants/{tenant_id}/grants',
                'operation_id': 'tenants_tenant_id_grants_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'tenant_id',
                    'email',
                    'cloud_id',
                    'resources',
                    'permission',
                ],
                'required': [
                    'tenant_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'tenant_id':
                        (str,),
                    'email':
                        (str,),
                    'cloud_id':
                        (str,),
                    'resources':
                        ([str],),
                    'permission':
                        (str,),
                },
                'attribute_map': {
                    'tenant_id': 'tenant_id',
                    'email': 'email',
                    'cloud_id': 'cloud_id',
                    'resources': 'resources',
                    'permission': 'permission',
                },
                'location_map': {
                    'tenant_id': 'path',
                    'email': 'query',
                    'cloud_id': 'query',
                    'resources': 'query',
                    'permission': 'query',
                },
                'collection_format_map': {
                    'resources': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__tenants_tenant_id_grants_get
        )

        def __tenants_tenant_id_grants_post(
            self,
            tenant_id,
            user,
            **kwargs
        ):
            """Create/Update Grant  # noqa: E501

            Create a new permission grant or set an existing one  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.tenants_tenant_id_grants_post(tenant_id, user, async_req=True)
            >>> result = thread.get()

            Args:
                tenant_id (str): Tenant ID
                user (ModelGrant): Grant contents

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ModelGrant
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['tenant_id'] = \
                tenant_id
            kwargs['user'] = \
                user
            return self.call_with_http_info(**kwargs)

        self.tenants_tenant_id_grants_post = _Endpoint(
            settings={
                'response_type': (ModelGrant,),
                'auth': [],
                'endpoint_path': '/tenants/{tenant_id}/grants',
                'operation_id': 'tenants_tenant_id_grants_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'tenant_id',
                    'user',
                ],
                'required': [
                    'tenant_id',
                    'user',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'tenant_id':
                        (str,),
                    'user':
                        (ModelGrant,),
                },
                'attribute_map': {
                    'tenant_id': 'tenant_id',
                },
                'location_map': {
                    'tenant_id': 'path',
                    'user': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__tenants_tenant_id_grants_post
        )