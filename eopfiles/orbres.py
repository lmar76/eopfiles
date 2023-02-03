from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional

from . import basic


__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


class OrbitFileVariableHeaderRefFrame(Enum):
    BAR_MEAN_2000 = "BAR_MEAN_2000"
    HEL_MEAN_2000 = "HEL_MEAN_2000"
    GEO_MEAN_2000 = "GEO_MEAN_2000"
    MEAN_DATE = "MEAN_DATE"
    TRUE_DATE = "TRUE_DATE"
    EARTH_FIXED = "EARTH_FIXED"
    BAR_MEAN_1950 = "BAR_MEAN_1950"
    QUASI_MEAN_DATE = "QUASI_MEAN_DATE"
    PSE_TRUE_DATE = "PSE_TRUE_DATE"
    PSEUDO_EARTH_FIXED = "PSEUDO_EARTH_FIXED"


class OrbitFileVariableHeaderTimeReference(Enum):
    TAI = "TAI"
    UTC = "UTC"
    UT1 = "UT1"


@dataclass
class PositionComponentType:
    class Meta:
        name = "Position_Component_Type"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: str = field(
        init=False,
        default="m",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class SourceType:
    class Meta:
        name = "Source_Type"

    system: Optional[str] = field(
        default=None,
        metadata={
            "name": "System",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    creator: Optional[str] = field(
        default=None,
        metadata={
            "name": "Creator",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    creator_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "Creator_Version",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    creation_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "Creation_Date",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
            "length": 23,
            "pattern": r"UTC=.*",
        }
    )


@dataclass
class ValidityPeriodType:
    class Meta:
        name = "Validity_Period_Type"

    validity_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "Validity_Start",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
            "length": 23,
            "pattern": r"UTC=.*",
        }
    )
    validity_stop: Optional[str] = field(
        default=None,
        metadata={
            "name": "Validity_Stop",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
            "length": 23,
            "pattern": r"UTC=.*",
        }
    )


@dataclass
class VelocityComponentType:
    class Meta:
        name = "Velocity_Component_Type"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: str = field(
        init=False,
        default="m/s",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class FixedHeaderTypeFFS1:
    class Meta:
        name = "Fixed_Header_Type"

    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Name",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
            "pattern": basic.FILE_NAME_PATTERN_FFS1,
        }
    )
    file_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Description",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    notes: Optional[str] = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    mission: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mission",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    file_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Class",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
            "pattern": basic.FILE_CLASS_PATTERN,
        }
    )
    file_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Type",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
            "pattern": r"[A-Z0-9_]{10}",
        }
    )
    validity_period: Optional[ValidityPeriodType] = field(
        default=None,
        metadata={
            "name": "Validity_Period",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    file_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Version",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
            "pattern": r"[0-9]{4}",
        }
    )
    source: Optional[SourceType] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )


@dataclass
class FixedHeaderTypeFFS2:
    class Meta:
        name = "Fixed_Header_Type"

    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Name",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
            "pattern": basic.FILE_NAME_PATTERN_FFS2,
        }
    )
    file_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Description",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    notes: Optional[str] = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    mission: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mission",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    file_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Class",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
            "pattern": basic.FILE_CLASS_PATTERN,
        }
    )
    file_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Type",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
            "pattern": r"[A-Z0-9_]{10}",
        }
    )
    validity_period: Optional[ValidityPeriodType] = field(
        default=None,
        metadata={
            "name": "Validity_Period",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    file_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Version",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
            "pattern": r"[0-9]{4}",
        }
    )
    source: Optional[SourceType] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )


@dataclass
class OSVType:
    class Meta:
        name = "OSV_Type"

    tai: Optional[str] = field(
        default=None,
        metadata={
            "name": "TAI",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
            "pattern": basic.TAI_DATE_TIME_PATTERN,
        }
    )
    utc: Optional[str] = field(
        default=None,
        metadata={
            "name": "UTC",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
            "pattern": basic.UTC_DATE_TIME_PATTERN,
        }
    )
    ut1: Optional[str] = field(
        default=None,
        metadata={
            "name": "UT1",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
            "pattern": basic.UT1_DATE_TIME_PATTERN,
        }
    )
    absolute_orbit: Optional[int] = field(
        default=None,
        metadata={
            "name": "Absolute_Orbit",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    x: Optional[PositionComponentType] = field(
        default=None,
        metadata={
            "name": "X",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    y: Optional[PositionComponentType] = field(
        default=None,
        metadata={
            "name": "Y",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    z: Optional[PositionComponentType] = field(
        default=None,
        metadata={
            "name": "Z",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    vx: Optional[VelocityComponentType] = field(
        default=None,
        metadata={
            "name": "VX",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    vy: Optional[VelocityComponentType] = field(
        default=None,
        metadata={
            "name": "VY",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    vz: Optional[VelocityComponentType] = field(
        default=None,
        metadata={
            "name": "VZ",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    quality: Optional[str] = field(
        default=None,
        metadata={
            "name": "Quality",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )


@dataclass
class OrbitFileVariableHeader:
    class Meta:
        name = "Orbit_File_Variable_Header"

    ref_frame: Optional[OrbitFileVariableHeaderRefFrame] = field(
        default=None,
        metadata={
            "name": "Ref_Frame",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    time_reference: Optional[OrbitFileVariableHeaderTimeReference] = field(
        default=None,
        metadata={
            "name": "Time_Reference",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )


@dataclass
class EarthExplorerHeaderTypeFFS1:
    class Meta:
        name = "Earth_Explorer_Header_Type"

    fixed_header: Optional[FixedHeaderTypeFFS1] = field(
        default=None,
        metadata={
            "name": "Fixed_Header",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    variable_header: Optional[basic.AnyTypeType] = field(
        default=None,
        metadata={
            "name": "Variable_Header",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )


@dataclass
class EarthExplorerHeaderTypeFFS2:
    class Meta:
        name = "Earth_Explorer_Header_Type"

    fixed_header: Optional[FixedHeaderTypeFFS2] = field(
        default=None,
        metadata={
            "name": "Fixed_Header",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    variable_header: Optional[basic.AnyTypeType] = field(
        default=None,
        metadata={
            "name": "Variable_Header",
            "type": "Element",
            "namespace": __NAMESPACE__,
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
class ListofOSVsType:
    class Meta:
        name = "List_of_OSVs_Type"

    osv: List[OSVType] = field(
        default_factory=list,
        metadata={
            "name": "OSV",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "min_occurs": 1,
        }
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class RestitutedOrbitHeaderTypeFFS1:
    class Meta:
        name = "Restituted_Orbit_Header_Type"

    fixed_header: Optional[FixedHeaderTypeFFS1] = field(
        default=None,
        metadata={
            "name": "Fixed_Header",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    variable_header: Optional[OrbitFileVariableHeader] = field(
        default=None,
        metadata={
            "name": "Variable_Header",
            "type": "Element",
            "namespace": __NAMESPACE__,
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
class RestitutedOrbitHeaderTypeFFS2:
    class Meta:
        name = "Restituted_Orbit_Header_Type"

    fixed_header: Optional[FixedHeaderTypeFFS2] = field(
        default=None,
        metadata={
            "name": "Fixed_Header",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    variable_header: Optional[OrbitFileVariableHeader] = field(
        default=None,
        metadata={
            "name": "Variable_Header",
            "type": "Element",
            "namespace": __NAMESPACE__,
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
class EarthExplorerHeaderFFS1(RestitutedOrbitHeaderTypeFFS1):
    class Meta:
        name = "Earth_Explorer_Header"
        namespace = __NAMESPACE__


@dataclass
class EarthExplorerHeaderFFS2(RestitutedOrbitHeaderTypeFFS2):
    class Meta:
        name = "Earth_Explorer_Header"
        namespace = __NAMESPACE__


@dataclass
class RestitutedOrbitDataBlockType:
    class Meta:
        name = "Restituted_Orbit_Data_Block_Type"

    list_of_osvs: Optional[ListofOSVsType] = field(
        default=None,
        metadata={
            "name": "List_of_OSVs",
            "type": "Element",
            "namespace": __NAMESPACE__,
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
class DataBlock(RestitutedOrbitDataBlockType):
    class Meta:
        name = "Data_Block"
        namespace = __NAMESPACE__


@dataclass
class RestitutedOrbitFileTypeFFS1:
    class Meta:
        name = "Restituted_Orbit_File_Type"

    earth_explorer_header: Optional[RestitutedOrbitHeaderTypeFFS1] = field(
        default=None,
        metadata={
            "name": "Earth_Explorer_Header",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    data_block: Optional[RestitutedOrbitDataBlockType] = field(
        default=None,
        metadata={
            "name": "Data_Block",
            "type": "Element",
            "namespace": __NAMESPACE__,
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
class RestitutedOrbitFileTypeFFS2:
    class Meta:
        name = "Restituted_Orbit_File_Type"

    earth_explorer_header: Optional[RestitutedOrbitHeaderTypeFFS2] = field(
        default=None,
        metadata={
            "name": "Earth_Explorer_Header",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    data_block: Optional[RestitutedOrbitDataBlockType] = field(
        default=None,
        metadata={
            "name": "Data_Block",
            "type": "Element",
            "namespace": __NAMESPACE__,
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
class EarthExplorerFileFFS1(RestitutedOrbitFileTypeFFS1):
    class Meta:
        name = "Earth_Explorer_File"
        namespace = __NAMESPACE__


@dataclass
class EarthExplorerFileFFS2(RestitutedOrbitFileTypeFFS2):
    class Meta:
        name = "Earth_Explorer_File"
        namespace = __NAMESPACE__
