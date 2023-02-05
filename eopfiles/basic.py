from __future__ import annotations
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Any, Optional


# ===============================================
# Namespace and schema files
# ===============================================


__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"
SCHEMA_URLS = {
    "orbres_ffs1": f"{__NAMESPACE__}/EE_CFI_SCHEMAS/EO_OPER_AUX_ORBRES_0105.XSD",
    "orbres_ffs2": f"{__NAMESPACE__}/EE_CFI_SCHEMAS/EO_OPER_AUX_ORBRES_0203.XSD",
    "orbres_ffs3": f"{__NAMESPACE__}/EE_CFI_SCHEMAS/EO_OPER_AUX_ORBRES_0300.XSD"
}


# ===============================================
# Files
# ===============================================


FILE_NAME_PATTERN_FFS1 = r"([A-Z_]){2}_([A-Z0-9_]){4}_([A-Z0-9_]){10}_([A-Z0-9_]){1,41}"
FILE_NAME_PATTERN_FFS2 = r"([A-Z0-9_]){3}_([A-Z0-9_]){4}_([A-Z0-9_]){10}_([A-Z0-9_]){1,41}"
FILE_NAME_PATTERN_FFS3 = FILE_NAME_PATTERN_FFS2
FILE_CLASS_PATTERN = (
    r"OPER|OFFL|NRT_|RPRO|STV[0-3]|GSOV|TEST|TD[0-9][0-9]|Routine Operations"
    r"|Off-Line Processing|near-real-Time Processing|Re-Processing|"
    r"Satellite Validation Test [0-3]|Ground Segment Overall Validation test"
    r"|Generated test files|Test Data Set [0-9][0-9]"
)
FILE_TYPE_PATTERN = r"[A-Z0-9_]{10}"
FILE_VERSION_PATTERN = r"[0-9]{4}"


# ===============================================
# Data Volume
# ===============================================


@dataclass
class TotSizeType:
    class Meta:
        name = "Tot_Size_Type"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: str = field(
        init=False,
        default="bytes",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


# ===============================================
# Any type
# ===============================================


@dataclass
class AnyTypeType:
    class Meta:
        name = "AnyType_Type"

    content: list[Any] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


# ===============================================
# Angles
# ===============================================


@dataclass
class AngleType:
    class Meta:
        name = "Angle_Type"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: str = field(
        init=False,
        default="deg",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class LatType:
    class Meta:
        name = "Lat_Type"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: str = field(
        init=False,
        default="10-6deg",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class LongType:
    class Meta:
        name = "Long_Type"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: str = field(
        init=False,
        default="10-6deg",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class EquatorCrossLongType:
    class Meta:
        name = "Equator_Cross_Long_Type"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: str = field(
        init=False,
        default="10-6deg",
        metadata={
            "type": "Attribute",
        }
    )


# ===============================================
# Position
# ===============================================


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


# ===============================================
# Velocity
# ===============================================


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
