# coding: utf-8

"""
    Client Portal Web API

    Production version of the Client Portal Web API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Contract(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'r_t_h': 'bool',
        'con_id': 'str',
        'company_name': 'str',
        'exchange': 'str',
        'local_symbol': 'str',
        'instrument_type': 'str',
        'currency': 'str',
        'category': 'str',
        'industry': 'str',
        'rules': 'ContractRules'
    }

    attribute_map = {
        'r_t_h': 'r_t_h',
        'con_id': 'con_id',
        'company_name': 'company_name',
        'exchange': 'exchange',
        'local_symbol': 'local_symbol',
        'instrument_type': 'instrument_type',
        'currency': 'currency',
        'category': 'category',
        'industry': 'industry',
        'rules': 'rules'
    }

    def __init__(self, r_t_h=None, con_id=None, company_name=None, exchange=None, local_symbol=None, instrument_type=None, currency=None, category=None, industry=None, rules=None):  # noqa: E501
        """Contract - a model defined in Swagger"""  # noqa: E501

        self._r_t_h = None
        self._con_id = None
        self._company_name = None
        self._exchange = None
        self._local_symbol = None
        self._instrument_type = None
        self._currency = None
        self._category = None
        self._industry = None
        self._rules = None
        self.discriminator = None

        if r_t_h is not None:
            self.r_t_h = r_t_h
        if con_id is not None:
            self.con_id = con_id
        if company_name is not None:
            self.company_name = company_name
        if exchange is not None:
            self.exchange = exchange
        if local_symbol is not None:
            self.local_symbol = local_symbol
        if instrument_type is not None:
            self.instrument_type = instrument_type
        if currency is not None:
            self.currency = currency
        if category is not None:
            self.category = category
        if industry is not None:
            self.industry = industry
        if rules is not None:
            self.rules = rules

    @property
    def r_t_h(self):
        """Gets the r_t_h of this Contract.  # noqa: E501

        true means you can trade outside RTH(regular trading hours)  # noqa: E501

        :return: The r_t_h of this Contract.  # noqa: E501
        :rtype: bool
        """
        return self._r_t_h

    @r_t_h.setter
    def r_t_h(self, r_t_h):
        """Sets the r_t_h of this Contract.

        true means you can trade outside RTH(regular trading hours)  # noqa: E501

        :param r_t_h: The r_t_h of this Contract.  # noqa: E501
        :type: bool
        """

        self._r_t_h = r_t_h

    @property
    def con_id(self):
        """Gets the con_id of this Contract.  # noqa: E501

        same as that in request  # noqa: E501

        :return: The con_id of this Contract.  # noqa: E501
        :rtype: str
        """
        return self._con_id

    @con_id.setter
    def con_id(self, con_id):
        """Sets the con_id of this Contract.

        same as that in request  # noqa: E501

        :param con_id: The con_id of this Contract.  # noqa: E501
        :type: str
        """

        self._con_id = con_id

    @property
    def company_name(self):
        """Gets the company_name of this Contract.  # noqa: E501


        :return: The company_name of this Contract.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this Contract.


        :param company_name: The company_name of this Contract.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def exchange(self):
        """Gets the exchange of this Contract.  # noqa: E501


        :return: The exchange of this Contract.  # noqa: E501
        :rtype: str
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this Contract.


        :param exchange: The exchange of this Contract.  # noqa: E501
        :type: str
        """

        self._exchange = exchange

    @property
    def local_symbol(self):
        """Gets the local_symbol of this Contract.  # noqa: E501

        for exmple FB  # noqa: E501

        :return: The local_symbol of this Contract.  # noqa: E501
        :rtype: str
        """
        return self._local_symbol

    @local_symbol.setter
    def local_symbol(self, local_symbol):
        """Sets the local_symbol of this Contract.

        for exmple FB  # noqa: E501

        :param local_symbol: The local_symbol of this Contract.  # noqa: E501
        :type: str
        """

        self._local_symbol = local_symbol

    @property
    def instrument_type(self):
        """Gets the instrument_type of this Contract.  # noqa: E501

        for example STK  # noqa: E501

        :return: The instrument_type of this Contract.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this Contract.

        for example STK  # noqa: E501

        :param instrument_type: The instrument_type of this Contract.  # noqa: E501
        :type: str
        """

        self._instrument_type = instrument_type

    @property
    def currency(self):
        """Gets the currency of this Contract.  # noqa: E501


        :return: The currency of this Contract.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Contract.


        :param currency: The currency of this Contract.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def category(self):
        """Gets the category of this Contract.  # noqa: E501


        :return: The category of this Contract.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Contract.


        :param category: The category of this Contract.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def industry(self):
        """Gets the industry of this Contract.  # noqa: E501


        :return: The industry of this Contract.  # noqa: E501
        :rtype: str
        """
        return self._industry

    @industry.setter
    def industry(self, industry):
        """Sets the industry of this Contract.


        :param industry: The industry of this Contract.  # noqa: E501
        :type: str
        """

        self._industry = industry

    @property
    def rules(self):
        """Gets the rules of this Contract.  # noqa: E501


        :return: The rules of this Contract.  # noqa: E501
        :rtype: ContractRules
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this Contract.


        :param rules: The rules of this Contract.  # noqa: E501
        :type: ContractRules
        """

        self._rules = rules

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Contract, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Contract):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
