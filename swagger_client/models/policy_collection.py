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


class PolicyCollection(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, total_items=None, items=None, engine_rule_sets=None, revision=None):
        """
        PolicyCollection - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'total_items': 'int',
            'items': 'list[Policy]',
            'engine_rule_sets': 'list[str]',
            'revision': 'int'
        }

        self.attribute_map = {
            'total_items': 'totalItems',
            'items': 'items',
            'engine_rule_sets': 'engineRuleSets',
            'revision': 'revision'
        }

        self._total_items = total_items
        self._items = items
        self._engine_rule_sets = engine_rule_sets
        self._revision = revision

    @property
    def total_items(self):
        """
        Gets the total_items of this PolicyCollection.

        :return: The total_items of this PolicyCollection.
        :rtype: int
        """
        return self._total_items

    @total_items.setter
    def total_items(self, total_items):
        """
        Sets the total_items of this PolicyCollection.

        :param total_items: The total_items of this PolicyCollection.
        :type: int
        """

        self._total_items = total_items

    @property
    def items(self):
        """
        Gets the items of this PolicyCollection.

        :return: The items of this PolicyCollection.
        :rtype: list[Policy]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this PolicyCollection.

        :param items: The items of this PolicyCollection.
        :type: list[Policy]
        """

        self._items = items

    @property
    def engine_rule_sets(self):
        """
        Gets the engine_rule_sets of this PolicyCollection.
        Rules used by the policies, in a format specific to the classification engine.

        :return: The engine_rule_sets of this PolicyCollection.
        :rtype: list[str]
        """
        return self._engine_rule_sets

    @engine_rule_sets.setter
    def engine_rule_sets(self, engine_rule_sets):
        """
        Sets the engine_rule_sets of this PolicyCollection.
        Rules used by the policies, in a format specific to the classification engine.

        :param engine_rule_sets: The engine_rule_sets of this PolicyCollection.
        :type: list[str]
        """

        self._engine_rule_sets = engine_rule_sets

    @property
    def revision(self):
        """
        Gets the revision of this PolicyCollection.
        Revision number for this collection of policies The revision number increases when anything changes that affects the policy collection, for example enabling or disabling a policy, or changes to the rules for a policy.

        :return: The revision of this PolicyCollection.
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this PolicyCollection.
        Revision number for this collection of policies The revision number increases when anything changes that affects the policy collection, for example enabling or disabling a policy, or changes to the rules for a policy.

        :param revision: The revision of this PolicyCollection.
        :type: int
        """

        self._revision = revision

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
        if not isinstance(other, PolicyCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
