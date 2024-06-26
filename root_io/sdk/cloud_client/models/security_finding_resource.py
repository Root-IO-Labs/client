# coding: utf-8

"""
    Root.io API

    This is the API documentation for Root.io.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from root_io.sdk.cloud_client.models.entities_finding_status import EntitiesFindingStatus
from root_io.sdk.cloud_client.models.entities_resolution import EntitiesResolution
from root_io.sdk.cloud_client.models.entities_scanner_name import EntitiesScannerName
from root_io.sdk.cloud_client.models.entities_security_finding_severity import EntitiesSecurityFindingSeverity
from root_io.sdk.cloud_client.models.securityfindings_security_finding_activity_resource import SecurityfindingsSecurityFindingActivityResource
from typing import Optional, Set
from typing_extensions import Self

class SecurityFindingResource(BaseModel):
    """
    SecurityFindingResource
    """ # noqa: E501
    activities: Optional[SecurityfindingsSecurityFindingActivityResource] = None
    cvss: Optional[Union[StrictFloat, StrictInt]] = None
    cvss_vector: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    discovered_at: Optional[StrictStr] = None
    external_vuln_id: Optional[StrictStr] = None
    fixed_in: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    image_build_digest: Optional[StrictStr] = None
    image_build_repo: Optional[StrictStr] = None
    image_build_tag: Optional[StrictStr] = None
    nvd_link: Optional[StrictStr] = None
    package_distro: Optional[StrictStr] = None
    package_ecosystem: Optional[StrictStr] = None
    package_name: Optional[StrictStr] = None
    package_version: Optional[StrictStr] = None
    published_at: Optional[StrictStr] = None
    resolution: Optional[EntitiesResolution] = None
    scanner_name: Optional[EntitiesScannerName] = None
    severity: Optional[EntitiesSecurityFindingSeverity] = None
    status: Optional[EntitiesFindingStatus] = None
    __properties: ClassVar[List[str]] = ["activities", "cvss", "cvss_vector", "description", "discovered_at", "external_vuln_id", "fixed_in", "id", "image_build_digest", "image_build_repo", "image_build_tag", "nvd_link", "package_distro", "package_ecosystem", "package_name", "package_version", "published_at", "resolution", "scanner_name", "severity", "status"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SecurityFindingResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of activities
        if self.activities:
            _dict['activities'] = self.activities.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SecurityFindingResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "activities": SecurityfindingsSecurityFindingActivityResource.from_dict(obj["activities"]) if obj.get("activities") is not None else None,
            "cvss": obj.get("cvss"),
            "cvss_vector": obj.get("cvss_vector"),
            "description": obj.get("description"),
            "discovered_at": obj.get("discovered_at"),
            "external_vuln_id": obj.get("external_vuln_id"),
            "fixed_in": obj.get("fixed_in"),
            "id": obj.get("id"),
            "image_build_digest": obj.get("image_build_digest"),
            "image_build_repo": obj.get("image_build_repo"),
            "image_build_tag": obj.get("image_build_tag"),
            "nvd_link": obj.get("nvd_link"),
            "package_distro": obj.get("package_distro"),
            "package_ecosystem": obj.get("package_ecosystem"),
            "package_name": obj.get("package_name"),
            "package_version": obj.get("package_version"),
            "published_at": obj.get("published_at"),
            "resolution": obj.get("resolution"),
            "scanner_name": obj.get("scanner_name"),
            "severity": obj.get("severity"),
            "status": obj.get("status")
        })
        return _obj


