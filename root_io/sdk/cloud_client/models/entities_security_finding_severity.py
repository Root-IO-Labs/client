# coding: utf-8

"""
    Root.io API

    This is the API documentation for Root.io.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class EntitiesSecurityFindingSeverity(str, Enum):
    """
    EntitiesSecurityFindingSeverity
    """

    """
    allowed enum values
    """
    CRITICAL = 'Critical'
    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'Low'
    UNKNOWN = 'Unknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EntitiesSecurityFindingSeverity from a JSON string"""
        return cls(json.loads(json_str))

