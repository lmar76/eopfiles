from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from . import basic, headers, orbits


@dataclass
class RestitutedOrbitFileVariableHeader:
    class Meta:
        name = "Variable_Header"

    ref_frame: Optional[orbits.RefFrame] = field(
        default=None,
        metadata={
            "name": "Ref_Frame",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    time_reference: Optional[orbits.TimeReference] = field(
        default=None,
        metadata={
            "name": "Time_Reference",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )


@dataclass
class RestitutedOrbitFileDataBlockType:
    class Meta:
        name = "Data_Block"

    list_of_osvs: orbits.ListOfOSVs = field(
        metadata={
            "name": "List_of_OSVs",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    type: str = field(
        init=False,
        default="xml",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    schema_version: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
        }
    )


@dataclass
class EERestitutedOrbitHeaderTypeFFS1:
    class Meta:
        name = "Earth_Explorer_Header"

    fixed_header: Optional[headers.EEFixedHeaderTypeFFS1] = field(
        default=None,
        metadata={
            "name": "Fixed_Header",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    variable_header: Optional[RestitutedOrbitFileVariableHeader] = field(
        default=None,
        metadata={
            "name": "Variable_Header",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    schema_version: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
        }
    )


@dataclass
class EERestitutedOrbitHeaderType:
    class Meta:
        name = "Earth_Explorer_Header"

    fixed_header: Optional[headers.EEFixedHeaderType] = field(
        default=None,
        metadata={
            "name": "Fixed_Header",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    variable_header: Optional[RestitutedOrbitFileVariableHeader] = field(
        default=None,
        metadata={
            "name": "Variable_Header",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    schema_version: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
        }
    )


@dataclass
class EORestitutedOrbitHeaderType:
    class Meta:
        name = "Earth_Observation_Header"

    fixed_header: Optional[headers.EOFixedHeaderType] = field(
        default=None,
        metadata={
            "name": "Fixed_Header",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    variable_header: Optional[RestitutedOrbitFileVariableHeader] = field(
        default=None,
        metadata={
            "name": "Variable_Header",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    schema_version: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
        }
    )


@dataclass
class EERestitutedOrbitFileFFS1:
    class Meta:
        name = "Earth_Explorer_File"
        namespace = basic.__NAMESPACE__

    schema_location: Optional[str] = field(
        default=f"{basic.__NAMESPACE__} {basic.SCHEMA_URLS['aux_orbres_ffs1']}",
        metadata={
            'name': 'schemaLocation',
            'type': 'Attribute',
            'namespace': 'http://www.w3.org/2001/XMLSchema-instance',
            'init': False
        }
    )

    header: Optional[EERestitutedOrbitHeaderTypeFFS1] = field(
        default=None,
        metadata={
            "name": "Earth_Explorer_Header",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    data_block: Optional[RestitutedOrbitFileDataBlockType] = field(
        default=None,
        metadata={
            "name": "Data_Block",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    schema_version: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class EERestitutedOrbitFile:
    class Meta:
        name = "Earth_Explorer_File"
        namespace = basic.__NAMESPACE__

    schema_location: Optional[str] = field(
        default=f"{basic.__NAMESPACE__} {basic.SCHEMA_URLS['aux_orbres_ffs2']}",
        metadata={
            'name': 'schemaLocation',
            'type': 'Attribute',
            'namespace': 'http://www.w3.org/2001/XMLSchema-instance',
            'init': False
        }
    )

    header: Optional[EERestitutedOrbitHeaderType] = field(
        default=None,
        metadata={
            "name": "Earth_Explorer_Header",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    data_block: Optional[RestitutedOrbitFileDataBlockType] = field(
        default=None,
        metadata={
            "name": "Data_Block",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    schema_version: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class EORestitutedOrbitFile:
    class Meta:
        name = "Earth_Observation_File"
        namespace = basic.__NAMESPACE__

    schema_location: Optional[str] = field(
        default=f"{basic.__NAMESPACE__} {basic.SCHEMA_URLS['aux_orbres_ffs3']}",
        metadata={
            'name': 'schemaLocation',
            'type': 'Attribute',
            'namespace': 'http://www.w3.org/2001/XMLSchema-instance',
            'init': False
        }
    )

    header: Optional[EORestitutedOrbitHeaderType] = field(
        default=None,
        metadata={
            "name": "Earth_Observation_Header",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    data_block: Optional[RestitutedOrbitFileDataBlockType] = field(
        default=None,
        metadata={
            "name": "Data_Block",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    schema_version: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class EEOrbitStateVectorFileFFS1(EERestitutedOrbitFileFFS1):

    class Meta:
        name = "Earth_Explorer_File"
        namespace = basic.__NAMESPACE__


@dataclass
class EEOrbitStateVectorFile(EERestitutedOrbitFile):

    class Meta:
        name = "Earth_Explorer_File"
        namespace = basic.__NAMESPACE__


@dataclass
class EOOrbitStateVectorFile(EORestitutedOrbitFile):

    class Meta:
        name = "Earth_Observation_File"
        namespace = basic.__NAMESPACE__

