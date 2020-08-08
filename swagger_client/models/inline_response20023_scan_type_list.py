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


class InlineResponse20023ScanTypeList(object):
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
        'code': 'str',
        'instruments': 'list[str]'
    }

    attribute_map = {
        'display_name': 'display_name',
        'code': 'code',
        'instruments': 'instruments'
    }

    def __init__(self, display_name=None, code=None, instruments=None):  # noqa: E501
        """InlineResponse20023ScanTypeList - a model defined in Swagger"""  # noqa: E501

        self._display_name = None
        self._code = None
        self._instruments = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if code is not None:
            self.code = code
        if instruments is not None:
            self.instruments = instruments

    @property
    def display_name(self):
        """Gets the display_name of this InlineResponse20023ScanTypeList.  # noqa: E501


        :return: The display_name of this InlineResponse20023ScanTypeList.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this InlineResponse20023ScanTypeList.


        :param display_name: The display_name of this InlineResponse20023ScanTypeList.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def code(self):
        """Gets the code of this InlineResponse20023ScanTypeList.  # noqa: E501


        :return: The code of this InlineResponse20023ScanTypeList.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this InlineResponse20023ScanTypeList.


        :param code: The code of this InlineResponse20023ScanTypeList.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def instruments(self):
        """Gets the instruments of this InlineResponse20023ScanTypeList.  # noqa: E501


        :return: The instruments of this InlineResponse20023ScanTypeList.  # noqa: E501
        :rtype: list[str]
        """
        return self._instruments

    @instruments.setter
    def instruments(self, instruments):
        """Sets the instruments of this InlineResponse20023ScanTypeList.


        :param instruments: The instruments of this InlineResponse20023ScanTypeList.  # noqa: E501
        :type: list[str]
        """

        self._instruments = instruments

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
        if issubclass(InlineResponse20023ScanTypeList, dict):
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
        if not isinstance(other, InlineResponse20023ScanTypeList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other