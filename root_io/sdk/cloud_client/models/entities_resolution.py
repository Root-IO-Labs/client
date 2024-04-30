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


class EntitiesResolution(str, Enum):
    """
    EntitiesResolution
    """

    """
    allowed enum values
    """
    FIXEDORPATCHED = 'FixedOrPatched'
    WILLPATCH = 'WillPatch'
    AWAITINGPATCHAVAILABILITY = 'AwaitingPatchAvailability'
    COMPONENTNOTPRESENT = 'ComponentNotPresent'
    VULNERABLECODENOTPRESENT = 'VulnerableCodeNotPresent'
    VULNERABLECODENOTINEXECPATH = 'VulnerableCodeNotInExecPath'
    VULNERABLECODECANTBECONTROLLEDBYADVERSARY = 'VulnerableCodeCantBeControlledByAdversary'
    INLINEMITIGATIONALREADYEXISTS = 'InlineMitigationAlreadyExists'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EntitiesResolution from a JSON string"""
        return cls(json.loads(json_str))

