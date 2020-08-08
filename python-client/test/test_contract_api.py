# coding: utf-8

"""
    Client Portal Web API

    Production version of the Client Portal Web API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.contract_api import ContractApi  # noqa: E501
from swagger_client.rest import ApiException


class TestContractApi(unittest.TestCase):
    """ContractApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.contract_api.ContractApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_iserver_contract_conid_info_get(self):
        """Test case for iserver_contract_conid_info_get

        Contract Info  # noqa: E501
        """
        pass

    def test_iserver_secdef_info_get(self):
        """Test case for iserver_secdef_info_get

        Get available conids of future/option/warrant/cash/CFD  # noqa: E501
        """
        pass

    def test_iserver_secdef_search_post(self):
        """Test case for iserver_secdef_search_post

        Search by symbol or name  # noqa: E501
        """
        pass

    def test_iserver_secdef_strikes_get(self):
        """Test case for iserver_secdef_strikes_get

        Get strikes for Options/Warrant  # noqa: E501
        """
        pass

    def test_trsrv_futures_get(self):
        """Test case for trsrv_futures_get

        Security Futures by Symbol  # noqa: E501
        """
        pass

    def test_trsrv_secdef_post(self):
        """Test case for trsrv_secdef_post

        Secdef by Conid  # noqa: E501
        """
        pass

    def test_trsrv_stocks_get(self):
        """Test case for trsrv_stocks_get

        Security Stocks by Symbol  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
