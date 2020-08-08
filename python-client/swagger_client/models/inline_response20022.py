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


class InlineResponse20022(object):
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
        'call': 'list[str]',
        'put': 'list[str]'
    }

    attribute_map = {
        'call': 'call',
        'put': 'put'
    }

    def __init__(self, call=None, put=None):  # noqa: E501
        """InlineResponse20022 - a model defined in Swagger"""  # noqa: E501

        self._call = None
        self._put = None
        self.discriminator = None

        if call is not None:
            self.call = call
        if put is not None:
            self.put = put

    @property
    def call(self):
        """Gets the call of this InlineResponse20022.  # noqa: E501


        :return: The call of this InlineResponse20022.  # noqa: E501
        :rtype: list[str]
        """
        return self._call

    @call.setter
    def call(self, call):
        """Sets the call of this InlineResponse20022.


        :param call: The call of this InlineResponse20022.  # noqa: E501
        :type: list[str]
        """

        self._call = call

    @property
    def put(self):
        """Gets the put of this InlineResponse20022.  # noqa: E501


        :return: The put of this InlineResponse20022.  # noqa: E501
        :rtype: list[str]
        """
        return self._put

    @put.setter
    def put(self, put):
        """Sets the put of this InlineResponse20022.


        :param put: The put of this InlineResponse20022.  # noqa: E501
        :type: list[str]
        """

        self._put = put

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
        if issubclass(InlineResponse20022, dict):
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
        if not isinstance(other, InlineResponse20022):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
