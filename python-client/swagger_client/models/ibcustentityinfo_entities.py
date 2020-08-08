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


class IbcustentityinfoEntities(object):
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
        'can_trade': 'bool',
        'can_sign': 'bool',
        'type': 'str',
        'name': 'IbcustentityinfoName',
        'address': 'IbcustentityinfoAddress',
        'ident_docs': 'list[object]'
    }

    attribute_map = {
        'can_trade': 'canTrade',
        'can_sign': 'canSign',
        'type': 'type',
        'name': 'name',
        'address': 'address',
        'ident_docs': 'identDocs'
    }

    def __init__(self, can_trade=None, can_sign=None, type=None, name=None, address=None, ident_docs=None):  # noqa: E501
        """IbcustentityinfoEntities - a model defined in Swagger"""  # noqa: E501

        self._can_trade = None
        self._can_sign = None
        self._type = None
        self._name = None
        self._address = None
        self._ident_docs = None
        self.discriminator = None

        if can_trade is not None:
            self.can_trade = can_trade
        if can_sign is not None:
            self.can_sign = can_sign
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if address is not None:
            self.address = address
        if ident_docs is not None:
            self.ident_docs = ident_docs

    @property
    def can_trade(self):
        """Gets the can_trade of this IbcustentityinfoEntities.  # noqa: E501


        :return: The can_trade of this IbcustentityinfoEntities.  # noqa: E501
        :rtype: bool
        """
        return self._can_trade

    @can_trade.setter
    def can_trade(self, can_trade):
        """Sets the can_trade of this IbcustentityinfoEntities.


        :param can_trade: The can_trade of this IbcustentityinfoEntities.  # noqa: E501
        :type: bool
        """

        self._can_trade = can_trade

    @property
    def can_sign(self):
        """Gets the can_sign of this IbcustentityinfoEntities.  # noqa: E501


        :return: The can_sign of this IbcustentityinfoEntities.  # noqa: E501
        :rtype: bool
        """
        return self._can_sign

    @can_sign.setter
    def can_sign(self, can_sign):
        """Sets the can_sign of this IbcustentityinfoEntities.


        :param can_sign: The can_sign of this IbcustentityinfoEntities.  # noqa: E501
        :type: bool
        """

        self._can_sign = can_sign

    @property
    def type(self):
        """Gets the type of this IbcustentityinfoEntities.  # noqa: E501


        :return: The type of this IbcustentityinfoEntities.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IbcustentityinfoEntities.


        :param type: The type of this IbcustentityinfoEntities.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this IbcustentityinfoEntities.  # noqa: E501


        :return: The name of this IbcustentityinfoEntities.  # noqa: E501
        :rtype: IbcustentityinfoName
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IbcustentityinfoEntities.


        :param name: The name of this IbcustentityinfoEntities.  # noqa: E501
        :type: IbcustentityinfoName
        """

        self._name = name

    @property
    def address(self):
        """Gets the address of this IbcustentityinfoEntities.  # noqa: E501


        :return: The address of this IbcustentityinfoEntities.  # noqa: E501
        :rtype: IbcustentityinfoAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this IbcustentityinfoEntities.


        :param address: The address of this IbcustentityinfoEntities.  # noqa: E501
        :type: IbcustentityinfoAddress
        """

        self._address = address

    @property
    def ident_docs(self):
        """Gets the ident_docs of this IbcustentityinfoEntities.  # noqa: E501


        :return: The ident_docs of this IbcustentityinfoEntities.  # noqa: E501
        :rtype: list[object]
        """
        return self._ident_docs

    @ident_docs.setter
    def ident_docs(self, ident_docs):
        """Sets the ident_docs of this IbcustentityinfoEntities.


        :param ident_docs: The ident_docs of this IbcustentityinfoEntities.  # noqa: E501
        :type: list[object]
        """

        self._ident_docs = ident_docs

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
        if issubclass(IbcustentityinfoEntities, dict):
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
        if not isinstance(other, IbcustentityinfoEntities):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other