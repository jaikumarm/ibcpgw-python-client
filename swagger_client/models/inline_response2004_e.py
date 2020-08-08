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


class InlineResponse2004E(object):
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
        'nm': 'str',
        'i': 'str',
        'ui': 'str',
        'a': 'str'
    }

    attribute_map = {
        'nm': 'NM',
        'i': 'I',
        'ui': 'UI',
        'a': 'A'
    }

    def __init__(self, nm=None, i=None, ui=None, a=None):  # noqa: E501
        """InlineResponse2004E - a model defined in Swagger"""  # noqa: E501

        self._nm = None
        self._i = None
        self._ui = None
        self._a = None
        self.discriminator = None

        if nm is not None:
            self.nm = nm
        if i is not None:
            self.i = i
        if ui is not None:
            self.ui = ui
        if a is not None:
            self.a = a

    @property
    def nm(self):
        """Gets the nm of this InlineResponse2004E.  # noqa: E501

        device name  # noqa: E501

        :return: The nm of this InlineResponse2004E.  # noqa: E501
        :rtype: str
        """
        return self._nm

    @nm.setter
    def nm(self, nm):
        """Sets the nm of this InlineResponse2004E.

        device name  # noqa: E501

        :param nm: The nm of this InlineResponse2004E.  # noqa: E501
        :type: str
        """

        self._nm = nm

    @property
    def i(self):
        """Gets the i of this InlineResponse2004E.  # noqa: E501

        device id  # noqa: E501

        :return: The i of this InlineResponse2004E.  # noqa: E501
        :rtype: str
        """
        return self._i

    @i.setter
    def i(self, i):
        """Sets the i of this InlineResponse2004E.

        device id  # noqa: E501

        :param i: The i of this InlineResponse2004E.  # noqa: E501
        :type: str
        """

        self._i = i

    @property
    def ui(self):
        """Gets the ui of this InlineResponse2004E.  # noqa: E501

        unique device id  # noqa: E501

        :return: The ui of this InlineResponse2004E.  # noqa: E501
        :rtype: str
        """
        return self._ui

    @ui.setter
    def ui(self, ui):
        """Sets the ui of this InlineResponse2004E.

        unique device id  # noqa: E501

        :param ui: The ui of this InlineResponse2004E.  # noqa: E501
        :type: str
        """

        self._ui = ui

    @property
    def a(self):
        """Gets the a of this InlineResponse2004E.  # noqa: E501

        device is enabled or not 0-true, 1-false.  # noqa: E501

        :return: The a of this InlineResponse2004E.  # noqa: E501
        :rtype: str
        """
        return self._a

    @a.setter
    def a(self, a):
        """Sets the a of this InlineResponse2004E.

        device is enabled or not 0-true, 1-false.  # noqa: E501

        :param a: The a of this InlineResponse2004E.  # noqa: E501
        :type: str
        """

        self._a = a

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
        if issubclass(InlineResponse2004E, dict):
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
        if not isinstance(other, InlineResponse2004E):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other