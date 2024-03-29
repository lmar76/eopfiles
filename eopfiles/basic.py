"""Basic types and global variables."""

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"

from dataclasses import dataclass, field
from decimal import Decimal
from typing import Any, List, Optional

from xsdata.formats.converter import Converter, ConverterError, converter


# ===============================================
# Namespace and schema files
# ===============================================


SCHEMA_URLS = {
    "aux_orbres_ffs1": f"{__NAMESPACE__}/EE_CFI_SCHEMAS/EO_OPER_AUX_ORBRES_0105.XSD",
    "aux_orbres_ffs2": f"{__NAMESPACE__}/EE_CFI_SCHEMAS/EO_OPER_AUX_ORBRES_0203.XSD",
    "aux_orbres_ffs3": f"{__NAMESPACE__}/EE_CFI_SCHEMAS/EO_OPER_AUX_ORBRES_0300.XSD",
    "mpl_orbpre_ffs1": f"{__NAMESPACE__}/EE_CFI_SCHEMAS/EO_OPER_MPL_ORBPRE_0105.XSD",
    "mpl_orbpre_ffs2": f"{__NAMESPACE__}/EE_CFI_SCHEMAS/EO_OPER_MPL_ORBPRE_0203.XSD",
    "mpl_orbpre_ffs3": f"{__NAMESPACE__}/EE_CFI_SCHEMAS/EO_OPER_MPL_ORBPRE_0300.XSD"
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

    content: List[Any] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


# ===============================================
# Numeric types
# ===============================================


class FloatingFmtValue(float):
    pass


class IntFmtValue(int):
    pass


class FloatingFmtValueConverter(Converter):
    """Converter for `FloatingFmtValue` class."""

    def deserialize(self, value: str, **kwargs: Any) -> FloatingFmtValue:
        try:
            return FloatingFmtValue(value)
        except ValueError as err:
            raise ConverterError(err)

    def serialize(self, value: FloatingFmtValue, **kwargs: Any) -> str:
        if kwargs.get("format"):
            return kwargs["format"].format(value)
        return str(value)


class IntFmtValueConverter(Converter):
    """Converter for `IntFmtValue` class."""

    def deserialize(self, value: str, **kwargs: Any) -> IntFmtValue:
        try:
            return IntFmtValue(value)
        except ValueError as err:
            raise ConverterError(err)

    def serialize(self, value: IntFmtValue, **kwargs: Any) -> str:
        if kwargs.get("format"):
            return kwargs["format"].format(value)
        return str(value)


converter.register_converter(FloatingFmtValue, FloatingFmtValueConverter())
converter.register_converter(IntFmtValue, IntFmtValueConverter())


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
