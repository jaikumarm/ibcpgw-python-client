# coding: utf-8

"""
    Client Portal Web API

    Production version of the Client Portal Web API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class OrderApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def iserver_account_account_id_order_order_id_delete(self, account_id, order_id, **kwargs):  # noqa: E501
        """Delete Order  # noqa: E501

        Deletes an open order. Must call /iserver/accounts endpoint prior to deleting an order. Use /iservers/account/orders endpoint to review open-order(s).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.iserver_account_account_id_order_order_id_delete(account_id, order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: account id (required)
        :param str order_id: Customer order id, use /iservers/account/orders endpoint to query orderId. (required)
        :return: list[InlineResponse20017]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.iserver_account_account_id_order_order_id_delete_with_http_info(account_id, order_id, **kwargs)  # noqa: E501
        else:
            (data) = self.iserver_account_account_id_order_order_id_delete_with_http_info(account_id, order_id, **kwargs)  # noqa: E501
            return data

    def iserver_account_account_id_order_order_id_delete_with_http_info(self, account_id, order_id, **kwargs):  # noqa: E501
        """Delete Order  # noqa: E501

        Deletes an open order. Must call /iserver/accounts endpoint prior to deleting an order. Use /iservers/account/orders endpoint to review open-order(s).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.iserver_account_account_id_order_order_id_delete_with_http_info(account_id, order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: account id (required)
        :param str order_id: Customer order id, use /iservers/account/orders endpoint to query orderId. (required)
        :return: list[InlineResponse20017]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'order_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method iserver_account_account_id_order_order_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `iserver_account_account_id_order_order_id_delete`")  # noqa: E501
        # verify the required parameter 'order_id' is set
        if ('order_id' not in params or
                params['order_id'] is None):
            raise ValueError("Missing the required parameter `order_id` when calling `iserver_account_account_id_order_order_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501
        if 'order_id' in params:
            path_params['orderId'] = params['order_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/iserver/account/{accountId}/order/{orderId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InlineResponse20017]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def iserver_account_account_id_order_order_id_post(self, account_id, order_id, body, **kwargs):  # noqa: E501
        """Modify Order  # noqa: E501

        Modifies an open order. Must call /iserver/accounts endpoint prior to modifying an order. Use /iservers/account/orders endpoint to review open-order(s).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.iserver_account_account_id_order_order_id_post(account_id, order_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: account id (required)
        :param str order_id: Customer order id, use /iservers/account/orders endpoint to query orderId. (required)
        :param ModifyOrder body: modify-order request (required)
        :return: list[InlineResponse20017]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.iserver_account_account_id_order_order_id_post_with_http_info(account_id, order_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.iserver_account_account_id_order_order_id_post_with_http_info(account_id, order_id, body, **kwargs)  # noqa: E501
            return data

    def iserver_account_account_id_order_order_id_post_with_http_info(self, account_id, order_id, body, **kwargs):  # noqa: E501
        """Modify Order  # noqa: E501

        Modifies an open order. Must call /iserver/accounts endpoint prior to modifying an order. Use /iservers/account/orders endpoint to review open-order(s).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.iserver_account_account_id_order_order_id_post_with_http_info(account_id, order_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: account id (required)
        :param str order_id: Customer order id, use /iservers/account/orders endpoint to query orderId. (required)
        :param ModifyOrder body: modify-order request (required)
        :return: list[InlineResponse20017]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'order_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method iserver_account_account_id_order_order_id_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `iserver_account_account_id_order_order_id_post`")  # noqa: E501
        # verify the required parameter 'order_id' is set
        if ('order_id' not in params or
                params['order_id'] is None):
            raise ValueError("Missing the required parameter `order_id` when calling `iserver_account_account_id_order_order_id_post`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `iserver_account_account_id_order_order_id_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501
        if 'order_id' in params:
            path_params['orderId'] = params['order_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/iserver/account/{accountId}/order/{orderId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InlineResponse20017]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def iserver_account_account_id_order_post(self, account_id, body, **kwargs):  # noqa: E501
        """Place Order  # noqa: E501

        Please note here, sometimes this endpoint alone can't make sure you submit the order successfully, you could receive some questions in the response, you have to to answer them in order to submit the order successfully. You can use \"/iserver/reply/{replyid}\" endpoint to answer questions   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.iserver_account_account_id_order_post(account_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: account id (required)
        :param OrderRequest body: order request info (required)
        :return: list[InlineResponse20014]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.iserver_account_account_id_order_post_with_http_info(account_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.iserver_account_account_id_order_post_with_http_info(account_id, body, **kwargs)  # noqa: E501
            return data

    def iserver_account_account_id_order_post_with_http_info(self, account_id, body, **kwargs):  # noqa: E501
        """Place Order  # noqa: E501

        Please note here, sometimes this endpoint alone can't make sure you submit the order successfully, you could receive some questions in the response, you have to to answer them in order to submit the order successfully. You can use \"/iserver/reply/{replyid}\" endpoint to answer questions   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.iserver_account_account_id_order_post_with_http_info(account_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: account id (required)
        :param OrderRequest body: order request info (required)
        :return: list[InlineResponse20014]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method iserver_account_account_id_order_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `iserver_account_account_id_order_post`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `iserver_account_account_id_order_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/iserver/account/{accountId}/order', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InlineResponse20014]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def iserver_account_account_id_order_whatif_post(self, account_id, body, **kwargs):  # noqa: E501
        """Preview Order  # noqa: E501

        This endpoint allows you to preview order without actually submitting the order and you can get commission information in the response.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.iserver_account_account_id_order_whatif_post(account_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: account id (required)
        :param OrderRequest body: order info (required)
        :return: InlineResponse20016
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.iserver_account_account_id_order_whatif_post_with_http_info(account_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.iserver_account_account_id_order_whatif_post_with_http_info(account_id, body, **kwargs)  # noqa: E501
            return data

    def iserver_account_account_id_order_whatif_post_with_http_info(self, account_id, body, **kwargs):  # noqa: E501
        """Preview Order  # noqa: E501

        This endpoint allows you to preview order without actually submitting the order and you can get commission information in the response.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.iserver_account_account_id_order_whatif_post_with_http_info(account_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: account id (required)
        :param OrderRequest body: order info (required)
        :return: InlineResponse20016
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method iserver_account_account_id_order_whatif_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `iserver_account_account_id_order_whatif_post`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `iserver_account_account_id_order_whatif_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/iserver/account/{accountId}/order/whatif', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20016',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def iserver_account_account_id_orders_post(self, account_id, body, **kwargs):  # noqa: E501
        """Place Orders (Support bracket orders)  # noqa: E501

        You can pass a list of orders here   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.iserver_account_account_id_orders_post(account_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: account id (required)
        :param Body5 body: order request info (required)
        :return: list[InlineResponse20014]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.iserver_account_account_id_orders_post_with_http_info(account_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.iserver_account_account_id_orders_post_with_http_info(account_id, body, **kwargs)  # noqa: E501
            return data

    def iserver_account_account_id_orders_post_with_http_info(self, account_id, body, **kwargs):  # noqa: E501
        """Place Orders (Support bracket orders)  # noqa: E501

        You can pass a list of orders here   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.iserver_account_account_id_orders_post_with_http_info(account_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: account id (required)
        :param Body5 body: order request info (required)
        :return: list[InlineResponse20014]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method iserver_account_account_id_orders_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `iserver_account_account_id_orders_post`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `iserver_account_account_id_orders_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/iserver/account/{accountId}/orders', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InlineResponse20014]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def iserver_account_orders_get(self, **kwargs):  # noqa: E501
        """Live Orders  # noqa: E501

        The endpoint is meant to be used in polling mode, e.g. requesting every x seconds. The response will contain two objects, one is notification, the other is orders.  Orders is the list of orders (cancelled, filled, submitted) with activity in the current day.  Notifications contains information about execute orders as they happen, see status field.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.iserver_account_orders_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20013
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.iserver_account_orders_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.iserver_account_orders_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def iserver_account_orders_get_with_http_info(self, **kwargs):  # noqa: E501
        """Live Orders  # noqa: E501

        The endpoint is meant to be used in polling mode, e.g. requesting every x seconds. The response will contain two objects, one is notification, the other is orders.  Orders is the list of orders (cancelled, filled, submitted) with activity in the current day.  Notifications contains information about execute orders as they happen, see status field.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.iserver_account_orders_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20013
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method iserver_account_orders_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/iserver/account/orders', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20013',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def iserver_reply_replyid_post(self, replyid, body, **kwargs):  # noqa: E501
        """Place Order Reply  # noqa: E501

        Reply to questions when placing orders and submit orders  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.iserver_reply_replyid_post(replyid, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str replyid: Please use the \"id\" from the response of \"Place Order\" endpoint (required)
        :param Body6 body: Answer to question (required)
        :return: list[InlineResponse20015]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.iserver_reply_replyid_post_with_http_info(replyid, body, **kwargs)  # noqa: E501
        else:
            (data) = self.iserver_reply_replyid_post_with_http_info(replyid, body, **kwargs)  # noqa: E501
            return data

    def iserver_reply_replyid_post_with_http_info(self, replyid, body, **kwargs):  # noqa: E501
        """Place Order Reply  # noqa: E501

        Reply to questions when placing orders and submit orders  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.iserver_reply_replyid_post_with_http_info(replyid, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str replyid: Please use the \"id\" from the response of \"Place Order\" endpoint (required)
        :param Body6 body: Answer to question (required)
        :return: list[InlineResponse20015]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['replyid', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method iserver_reply_replyid_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'replyid' is set
        if ('replyid' not in params or
                params['replyid'] is None):
            raise ValueError("Missing the required parameter `replyid` when calling `iserver_reply_replyid_post`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `iserver_reply_replyid_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'replyid' in params:
            path_params['replyid'] = params['replyid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/iserver/reply/{replyid}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InlineResponse20015]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
