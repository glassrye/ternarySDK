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
from ternary.model.model_recommendation import ModelRecommendation
from ternary.model.model_recommendation_comment import ModelRecommendationComment


class RecommendationsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __tenants_tenant_id_recommendations_get(
            self,
            tenant_id,
            **kwargs
        ):
            """List Recommendations  # noqa: E501

            Get a recommendation by its ID.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.tenants_tenant_id_recommendations_get(tenant_id, async_req=True)
            >>> result = thread.get()

            Args:
                tenant_id (str): Tenant ID

            Keyword Args:
                ancestors ([str]): Recommendations matching Ancestor/s. [optional]
                assignees ([str]): Recommendations matching Assignee Email/s. [optional]
                categories ([str]): Recommendations matching Recommendation Category/ies. [optional]
                kind (str): Recommendations matching a certain Kind (anomaly or recommendation). [optional]
                resources ([str]): Recommendations matching Resource ID/s. [optional]
                types ([str]): Recommendations matching Recommendation Type/s. [optional]
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
                ModelRecommendation
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

        self.tenants_tenant_id_recommendations_get = _Endpoint(
            settings={
                'response_type': (ModelRecommendation,),
                'auth': [],
                'endpoint_path': '/tenants/{tenant_id}/recommendations',
                'operation_id': 'tenants_tenant_id_recommendations_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'tenant_id',
                    'ancestors',
                    'assignees',
                    'categories',
                    'kind',
                    'resources',
                    'types',
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
                    'ancestors':
                        ([str],),
                    'assignees':
                        ([str],),
                    'categories':
                        ([str],),
                    'kind':
                        (str,),
                    'resources':
                        ([str],),
                    'types':
                        ([str],),
                },
                'attribute_map': {
                    'tenant_id': 'tenant_id',
                    'ancestors': 'ancestors',
                    'assignees': 'assignees',
                    'categories': 'categories',
                    'kind': 'kind',
                    'resources': 'resources',
                    'types': 'types',
                },
                'location_map': {
                    'tenant_id': 'path',
                    'ancestors': 'query',
                    'assignees': 'query',
                    'categories': 'query',
                    'kind': 'query',
                    'resources': 'query',
                    'types': 'query',
                },
                'collection_format_map': {
                    'ancestors': 'csv',
                    'assignees': 'csv',
                    'categories': 'csv',
                    'resources': 'csv',
                    'types': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__tenants_tenant_id_recommendations_get
        )

        def __tenants_tenant_id_recommendations_id_comments_get(
            self,
            tenant_id,
            id,
            **kwargs
        ):
            """Get Recommendation Comments  # noqa: E501

            Get comments for a specific recommendation ID.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.tenants_tenant_id_recommendations_id_comments_get(tenant_id, id, async_req=True)
            >>> result = thread.get()

            Args:
                tenant_id (str): Tenant ID
                id (str): Recommendation ID

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
                [ModelRecommendationComment]
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
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.tenants_tenant_id_recommendations_id_comments_get = _Endpoint(
            settings={
                'response_type': ([ModelRecommendationComment],),
                'auth': [],
                'endpoint_path': '/tenants/{tenant_id}/recommendations/{id}/comments',
                'operation_id': 'tenants_tenant_id_recommendations_id_comments_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'tenant_id',
                    'id',
                ],
                'required': [
                    'tenant_id',
                    'id',
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
                    'id':
                        (str,),
                },
                'attribute_map': {
                    'tenant_id': 'tenant_id',
                    'id': 'id',
                },
                'location_map': {
                    'tenant_id': 'path',
                    'id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__tenants_tenant_id_recommendations_id_comments_get
        )

        def __tenants_tenant_id_recommendations_id_comments_post(
            self,
            tenant_id,
            id,
            recommendation,
            **kwargs
        ):
            """Create Recommendation Comment  # noqa: E501

            Create a new recommendation comment.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.tenants_tenant_id_recommendations_id_comments_post(tenant_id, id, recommendation, async_req=True)
            >>> result = thread.get()

            Args:
                tenant_id (str): Tenant ID
                id (str): Recommendation ID
                recommendation (ModelRecommendationComment): comment

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
                ModelRecommendationComment
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
            kwargs['id'] = \
                id
            kwargs['recommendation'] = \
                recommendation
            return self.call_with_http_info(**kwargs)

        self.tenants_tenant_id_recommendations_id_comments_post = _Endpoint(
            settings={
                'response_type': (ModelRecommendationComment,),
                'auth': [],
                'endpoint_path': '/tenants/{tenant_id}/recommendations/{id}/comments',
                'operation_id': 'tenants_tenant_id_recommendations_id_comments_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'tenant_id',
                    'id',
                    'recommendation',
                ],
                'required': [
                    'tenant_id',
                    'id',
                    'recommendation',
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
                    'id':
                        (str,),
                    'recommendation':
                        (ModelRecommendationComment,),
                },
                'attribute_map': {
                    'tenant_id': 'tenant_id',
                    'id': 'id',
                },
                'location_map': {
                    'tenant_id': 'path',
                    'id': 'path',
                    'recommendation': 'body',
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
            callable=__tenants_tenant_id_recommendations_id_comments_post
        )

        def __tenants_tenant_id_recommendations_id_delete(
            self,
            id,
            tenant_id,
            **kwargs
        ):
            """Delete Recommendation  # noqa: E501

            Delete a recommendation by its ID.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.tenants_tenant_id_recommendations_id_delete(id, tenant_id, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): Recommendation ID
                tenant_id (str): Tenant ID

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
            kwargs['id'] = \
                id
            kwargs['tenant_id'] = \
                tenant_id
            return self.call_with_http_info(**kwargs)

        self.tenants_tenant_id_recommendations_id_delete = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/tenants/{tenant_id}/recommendations/{id}',
                'operation_id': 'tenants_tenant_id_recommendations_id_delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'tenant_id',
                ],
                'required': [
                    'id',
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
                    'id':
                        (str,),
                    'tenant_id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'tenant_id': 'tenant_id',
                },
                'location_map': {
                    'id': 'path',
                    'tenant_id': 'path',
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
            callable=__tenants_tenant_id_recommendations_id_delete
        )

        def __tenants_tenant_id_recommendations_id_get(
            self,
            tenant_id,
            id,
            **kwargs
        ):
            """Get Recommendation  # noqa: E501

            Get a recommendation by its ID.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.tenants_tenant_id_recommendations_id_get(tenant_id, id, async_req=True)
            >>> result = thread.get()

            Args:
                tenant_id (str): Tenant ID
                id (str): Recommendation ID

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
                ModelRecommendation
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
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.tenants_tenant_id_recommendations_id_get = _Endpoint(
            settings={
                'response_type': (ModelRecommendation,),
                'auth': [],
                'endpoint_path': '/tenants/{tenant_id}/recommendations/{id}',
                'operation_id': 'tenants_tenant_id_recommendations_id_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'tenant_id',
                    'id',
                ],
                'required': [
                    'tenant_id',
                    'id',
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
                    'id':
                        (str,),
                },
                'attribute_map': {
                    'tenant_id': 'tenant_id',
                    'id': 'id',
                },
                'location_map': {
                    'tenant_id': 'path',
                    'id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__tenants_tenant_id_recommendations_id_get
        )

        def __tenants_tenant_id_recommendations_id_put(
            self,
            tenant_id,
            id,
            recommendation,
            **kwargs
        ):
            """Update Recommendation  # noqa: E501

            Update recommendation data. Depending on what fields you modify, different permissions are required. Most humans will need recommendation.writeMetadata to change typical fields like assignee and disposition. Ternary and custom recommenders use recommendation.write to update key information about the recommendation.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.tenants_tenant_id_recommendations_id_put(tenant_id, id, recommendation, async_req=True)
            >>> result = thread.get()

            Args:
                tenant_id (str): Tenant ID
                id (str): Recommendation ID
                recommendation (ModelRecommendation): recommendation

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
                ModelRecommendation
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
            kwargs['id'] = \
                id
            kwargs['recommendation'] = \
                recommendation
            return self.call_with_http_info(**kwargs)

        self.tenants_tenant_id_recommendations_id_put = _Endpoint(
            settings={
                'response_type': (ModelRecommendation,),
                'auth': [],
                'endpoint_path': '/tenants/{tenant_id}/recommendations/{id}',
                'operation_id': 'tenants_tenant_id_recommendations_id_put',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'tenant_id',
                    'id',
                    'recommendation',
                ],
                'required': [
                    'tenant_id',
                    'id',
                    'recommendation',
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
                    'id':
                        (str,),
                    'recommendation':
                        (ModelRecommendation,),
                },
                'attribute_map': {
                    'tenant_id': 'tenant_id',
                    'id': 'id',
                },
                'location_map': {
                    'tenant_id': 'path',
                    'id': 'path',
                    'recommendation': 'body',
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
            callable=__tenants_tenant_id_recommendations_id_put
        )

        def __tenants_tenant_id_recommendations_post(
            self,
            tenant_id,
            recommendation,
            **kwargs
        ):
            """Create Recommendation  # noqa: E501

            Create a new recommendation. Used internally by Ternary and if you create your own recommenders.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.tenants_tenant_id_recommendations_post(tenant_id, recommendation, async_req=True)
            >>> result = thread.get()

            Args:
                tenant_id (str): Tenant ID
                recommendation (ModelRecommendation): recommendation

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
                ModelRecommendation
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
            kwargs['recommendation'] = \
                recommendation
            return self.call_with_http_info(**kwargs)

        self.tenants_tenant_id_recommendations_post = _Endpoint(
            settings={
                'response_type': (ModelRecommendation,),
                'auth': [],
                'endpoint_path': '/tenants/{tenant_id}/recommendations',
                'operation_id': 'tenants_tenant_id_recommendations_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'tenant_id',
                    'recommendation',
                ],
                'required': [
                    'tenant_id',
                    'recommendation',
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
                    'recommendation':
                        (ModelRecommendation,),
                },
                'attribute_map': {
                    'tenant_id': 'tenant_id',
                },
                'location_map': {
                    'tenant_id': 'path',
                    'recommendation': 'body',
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
            callable=__tenants_tenant_id_recommendations_post
        )