from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

from . import basic, times


@dataclass
class ValidityPeriod:
    class Meta:
        name = "Validity_Period"

    validity_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "Validity_Start",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
            "length": 23,
            "pattern": times.UTC_DATE_TIME_PATTERN,
        }
    )
    validity_stop: Optional[str] = field(
        default=None,
        metadata={
            "name": "Validity_Stop",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
            "length": 23,
            "pattern": times.UTC_DATE_TIME_PATTERN,
        }
    )


@dataclass
class Source:
    class Meta:
        name = "Source"

    system: Optional[str] = field(
        default=None,
        metadata={
            "name": "System",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    creator: Optional[str] = field(
        default=None,
        metadata={
            "name": "Creator",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    creator_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "Creator_Version",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    creation_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "Creation_Date",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
            "length": 23,
            "pattern": times.UTC_DATE_TIME_PATTERN,
        }
    )


@dataclass
class EEFixedHeaderTypeFFS1:
    class Meta:
        name = "Fixed_Header"

    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Name",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
            "pattern": basic.FILE_NAME_PATTERN_FFS1,
        }
    )
    file_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Description",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    notes: Optional[str] = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    mission: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mission",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    file_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Class",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
            "pattern": basic.FILE_CLASS_PATTERN,
        }
    )
    file_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Type",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
            "pattern": basic.FILE_TYPE_PATTERN,
        }
    )
    validity_period: Optional[ValidityPeriod] = field(
        default=None,
        metadata={
            "name": "Validity_Period",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    file_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Version",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
            "pattern": basic.FILE_VERSION_PATTERN,
        }
    )
    source: Optional[Source] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )


@dataclass
class EEFixedHeaderType:
    class Meta:
        name = "Fixed_Header"

    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Name",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
            "pattern": basic.FILE_NAME_PATTERN_FFS2,
        }
    )
    file_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Description",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    notes: Optional[str] = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    mission: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mission",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    file_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Class",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
            "pattern": basic.FILE_CLASS_PATTERN,
        }
    )
    file_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Type",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
            "pattern": basic.FILE_TYPE_PATTERN,
        }
    )
    validity_period: Optional[ValidityPeriod] = field(
        default=None,
        metadata={
            "name": "Validity_Period",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    file_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Version",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
            "pattern": basic.FILE_VERSION_PATTERN,
        }
    )
    source: Optional[Source] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )


@dataclass
class EOFixedHeaderType:
    class Meta:
        name = "Fixed_Header"

    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Name",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
            "pattern": basic.FILE_NAME_PATTERN_FFS3,
        }
    )
    file_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Description",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    notes: Optional[str] = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    mission: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mission",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    file_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Class",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
            "pattern": basic.FILE_CLASS_PATTERN,
        }
    )
    file_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Type",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
            "pattern": basic.FILE_TYPE_PATTERN,
        }
    )
    validity_period: Optional[ValidityPeriod] = field(
        default=None,
        metadata={
            "name": "Validity_Period",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    file_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Version",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
            "pattern": r"[0-9]{4}",
        }
    )
    eoffs_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "EOFFS_Version",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    source: Optional[Source] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
