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


class InlineResponse20023InstrumentList(object):
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
        'display_name': 'str',
        'type': 'str',
        'filters': 'list[str]'
    }

    attribute_map = {
        'display_name': 'display_name',
        'type': 'type',
        'filters': 'filters'
    }

    def __init__(self, display_name=None, type=None, filters=None):  # noqa: E501
        """InlineResponse20023InstrumentList - a model defined in Swagger"""  # noqa: E501

        self._display_name = None
        self._type = None
        self._filters = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if type is not None:
            self.type = type
        if filters is not None:
            self.filters = filters

    @property
    def display_name(self):
        """Gets the display_name of this InlineResponse20023InstrumentList.  # noqa: E501


        :return: The display_name of this InlineResponse20023InstrumentList.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this InlineResponse20023InstrumentList.


        :param display_name: The display_name of this InlineResponse20023InstrumentList.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def type(self):
        """Gets the type of this InlineResponse20023InstrumentList.  # noqa: E501


        :return: The type of this InlineResponse20023InstrumentList.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse20023InstrumentList.


        :param type: The type of this InlineResponse20023InstrumentList.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def filters(self):
        """Gets the filters of this InlineResponse20023InstrumentList.  # noqa: E501


        :return: The filters of this InlineResponse20023InstrumentList.  # noqa: E501
        :rtype: list[str]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this InlineResponse20023InstrumentList.


        :param filters: The filters of this InlineResponse20023InstrumentList.  # noqa: E501
        :type: list[str]
        """

        self._filters = filters

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
        if issubclass(InlineResponse20023InstrumentList, dict):
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
        if not isinstance(other, InlineResponse20023InstrumentList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
