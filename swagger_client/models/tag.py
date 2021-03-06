# coding: utf-8

"""
    Veritas Information Classifier (VIC)

    APIs

    OpenAPI spec version: Resource Specific
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Tag(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, tag=None, description=None, properties=None, custom=None):
        """
        Tag - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'tag': 'str',
            'description': 'str',
            'properties': 'list[TagProperty]',
            'custom': 'bool'
        }

        self.attribute_map = {
            'tag': 'tag',
            'description': 'description',
            'properties': 'properties',
            'custom': 'custom'
        }

        self._tag = tag
        self._description = description
        self._properties = properties
        self._custom = custom

    @property
    def tag(self):
        """
        Gets the tag of this Tag.

        :return: The tag of this Tag.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this Tag.

        :param tag: The tag of this Tag.
        :type: str
        """

        self._tag = tag

    @property
    def description(self):
        """
        Gets the description of this Tag.

        :return: The description of this Tag.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Tag.

        :param description: The description of this Tag.
        :type: str
        """

        self._description = description

    @property
    def properties(self):
        """
        Gets the properties of this Tag.

        :return: The properties of this Tag.
        :rtype: list[TagProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this Tag.

        :param properties: The properties of this Tag.
        :type: list[TagProperty]
        """

        self._properties = properties

    @property
    def custom(self):
        """
        Gets the custom of this Tag.

        :return: The custom of this Tag.
        :rtype: bool
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """
        Sets the custom of this Tag.

        :param custom: The custom of this Tag.
        :type: bool
        """

        self._custom = custom

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Tag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
