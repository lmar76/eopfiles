from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlTime


__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


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
class AnyTypeType:
    class Meta:
        name = "AnyType_Type"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class CycleLengthType:
    class Meta:
        name = "Cycle_Length_Type"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: str = field(
        init=False,
        default="orbit",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class DeltaUT1Type:
    class Meta:
        name = "Delta_UT1_Type"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: str = field(
        init=False,
        default="s",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class DistanceType:
    class Meta:
        name = "Distance_Type"

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


@dataclass
class FreqType:
    class Meta:
        name = "Freq_Type"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: str = field(
        init=False,
        default="MHz",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class HarmonicTermType:
    class Meta:
        name = "Harmonic_Term_Type"

    reference_time: Optional["HarmonicTermType.ReferenceTime"] = field(
        default=None,
        metadata={
            "name": "Reference_Time",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    period: Optional["HarmonicTermType.Period"] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    amplitude_sin: Optional["HarmonicTermType.AmplitudeSin"] = field(
        default=None,
        metadata={
            "name": "Amplitude_Sin",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    amplitude_cos: Optional["HarmonicTermType.AmplitudeCos"] = field(
        default=None,
        metadata={
            "name": "Amplitude_Cos",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    seq: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class ReferenceTime:
        value: str = field(
            default="",
            metadata={
                "required": True,
                "pattern": r"(\d{4}-(((01|03|05|07|08|10|12)-(0[1-9]|[1,2][0-9]|3[0,1]))|((04|06|09|11)-(0[1-9]|[1,2][0-9]|30))|(02-(0[1-9]|[1,2][0-9])))T([0,1][0-9]|2[0-3])(:[0-5][0-9]){2}|0000-00-00T00:00:00|9999-99-99T99:99:99)(.\d*)?",
            }
        )
        time_ref: str = field(
            init=False,
            default="UT1",
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class Period:
        value: Optional[Decimal] = field(
            default=None,
            metadata={
                "required": True,
            }
        )
        unit: str = field(
            init=False,
            default="day",
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class AmplitudeSin:
        value: Optional[Decimal] = field(
            default=None,
            metadata={
                "required": True,
            }
        )
        unit: str = field(
            init=False,
            default="s",
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class AmplitudeCos:
        value: Optional[Decimal] = field(
            default=None,
            metadata={
                "required": True,
            }
        )
        unit: str = field(
            init=False,
            default="s",
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
class MLSTDriftType:
    class Meta:
        name = "MLST_Drift_Type"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: str = field(
        init=False,
        default="s/day",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


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


class OrbitScenarioVariableHeaderTimeReference(Enum):
    UT1 = "UT1"


@dataclass
class OrbitType:
    class Meta:
        name = "Orbit_Type"

    absolute_orbit: Optional[int] = field(
        default=None,
        metadata={
            "name": "Absolute_Orbit",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    relative_orbit: Optional[int] = field(
        default=None,
        metadata={
            "name": "Relative_Orbit",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    cycle_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "Cycle_Number",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    phase_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "Phase_Number",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )


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
class PositionType:
    class Meta:
        name = "Position_Type"

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
class ProductConfidenceDataType:
    class Meta:
        name = "Product_Confidence_Data_Type"

    num_isps: Optional[int] = field(
        default=None,
        metadata={
            "name": "Num_ISPs",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    num_missing_isps: Optional[int] = field(
        default=None,
        metadata={
            "name": "Num_Missing_ISPs",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    num_error_isps: Optional[int] = field(
        default=None,
        metadata={
            "name": "Num_Error_ISPs",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    num_discarded_isps: Optional[int] = field(
        default=None,
        metadata={
            "name": "Num_Discarded_ISPs",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    num_rs_isps: Optional[int] = field(
        default=None,
        metadata={
            "name": "Num_RS_ISPs",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    num_rs_corrections: Optional[int] = field(
        default=None,
        metadata={
            "name": "Num_RS_Corrections",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )


class RefractionModelType(Enum):
    NO_REF = "NO_REF"
    STD_REF = "STD_REF"
    USER_REF = "USER_REF"
    PRED_REF = "PRED_REF"


@dataclass
class RelTimeASCNodeType:
    class Meta:
        name = "Rel_Time_ASC_Node_Type"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    unit: str = field(
        init=False,
        default="s",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class RepeatCycleType:
    class Meta:
        name = "Repeat_Cycle_Type"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: str = field(
        init=False,
        default="day",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class SecondsTimeType:
    class Meta:
        name = "Seconds_Time_Type"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: str = field(
        init=False,
        default="s",
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
class TimeofANXType:
    class Meta:
        name = "Time_of_ANX_Type"

    tai: Optional[str] = field(
        default=None,
        metadata={
            "name": "TAI",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
            "pattern": r"TAI=.*",
        }
    )
    utc: Optional[str] = field(
        default=None,
        metadata={
            "name": "UTC",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
            "pattern": r"UTC=.*",
        }
    )
    ut1: Optional[str] = field(
        default=None,
        metadata={
            "name": "UT1",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
            "pattern": r"UT1=.*",
        }
    )


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


@dataclass
class ValidityPeriodBOMEOMType:
    class Meta:
        name = "Validity_Period_BOM_EOM_Type"

    validity_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "Validity_Start",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
            "pattern": r"UTC=0000-00-00T00:00:00",
        }
    )
    validity_stop: Optional[str] = field(
        default=None,
        metadata={
            "name": "Validity_Stop",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
            "pattern": r"UTC=9999-99-99T99:99:99",
        }
    )


@dataclass
class ValidityPeriodEOMType:
    class Meta:
        name = "Validity_Period_EOM_Type"

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
            "pattern": r"UTC=9999-99-99T99:99:99",
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
class VelocityType:
    class Meta:
        name = "Velocity_Type"

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
class AzimuthType(AngleType):
    class Meta:
        name = "Azimuth_Type"


@dataclass
class Declination(AngleType):
    pass


@dataclass
class ElevationType(AngleType):
    class Meta:
        name = "Elevation_Type"


@dataclass
class FixedHeaderBOMEOMType:
    class Meta:
        name = "Fixed_Header_BOM_EOM_Type"

    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Name",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
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
            "pattern": r"OPER|OFFL|NRT_|RPRO|STV[0-3]|GSOV|TEST|TD[0-9][0-9]|Routine Operations|Off-Line Processing|near-real-Time Processing|Re-Processing|Satellite Validation Test [0-3]|Ground Segment Overall Validation test|Generated test files|Test Data Set [0-9][0-9]",
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
    validity_period: Optional[ValidityPeriodBOMEOMType] = field(
        default=None,
        metadata={
            "name": "Validity_Period",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    file_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "File_Version",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
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
class FixedHeaderEOMType:
    class Meta:
        name = "Fixed_Header_EOM_Type"

    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Name",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
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
            "pattern": r"OPER|OFFL|NRT_|RPRO|STV[0-3]|GSOV|TEST|TD[0-9][0-9]|Routine Operations|Off-Line Processing|near-real-Time Processing|Re-Processing|Satellite Validation Test [0-3]|Ground Segment Overall Validation test|Generated test files|Test Data Set [0-9][0-9]",
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
    validity_period: Optional[ValidityPeriodEOMType] = field(
        default=None,
        metadata={
            "name": "Validity_Period",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    file_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "File_Version",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
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
class FixedHeaderType:
    class Meta:
        name = "Fixed_Header_Type"

    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Name",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
            "pattern": r"([A-Z_]){2}_([A-Z0-9_]){4}_([A-Z0-9_]){10}_([A-Z0-9_]){1,41}",
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
            "pattern": r"OPER|OFFL|NRT_|RPRO|STV[0-3]|GSOV|TEST|TD[0-9][0-9]|Routine Operations|Off-Line Processing|near-real-Time Processing|Re-Processing|Satellite Validation Test [0-3]|Ground Segment Overall Validation test|Generated test files|Test Data Set [0-9][0-9]",
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
class HeightType(DistanceType):
    class Meta:
        name = "Height_Type"


@dataclass
class LatitudeType(AngleType):
    class Meta:
        name = "Latitude_Type"


@dataclass
class LongitudeType(AngleType):
    class Meta:
        name = "Longitude_Type"


@dataclass
class MLSTNonlinearDriftType:
    class Meta:
        name = "MLST_Nonlinear_Drift_Type"

    linear_approx_validity: Optional["MLSTNonlinearDriftType.LinearApproxValidity"] = field(
        default=None,
        metadata={
            "name": "Linear_Approx_Validity",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    quadratic_term: Optional["MLSTNonlinearDriftType.QuadraticTerm"] = field(
        default=None,
        metadata={
            "name": "Quadratic_Term",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    harmonics_terms: Optional["MLSTNonlinearDriftType.HarmonicsTerms"] = field(
        default=None,
        metadata={
            "name": "Harmonics_Terms",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )

    @dataclass
    class LinearApproxValidity:
        value: Optional[int] = field(
            default=None,
            metadata={
                "required": True,
            }
        )
        unit: str = field(
            init=False,
            default="orbit",
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class QuadraticTerm:
        value: Optional[Decimal] = field(
            default=None,
            metadata={
                "required": True,
            }
        )
        unit: str = field(
            init=False,
            default="s/day^2",
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class HarmonicsTerms:
        harmonic_term: List[HarmonicTermType] = field(
            default_factory=list,
            metadata={
                "name": "Harmonic_Term",
                "type": "Element",
                "namespace": __NAMESPACE__,
                "max_occurs": 2,
            }
        )
        num: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass
class MPHType:
    class Meta:
        name = "MPH_Type"

    product: Optional[str] = field(
        default=None,
        metadata={
            "name": "Product",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    proc_stage_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Proc_Stage_Code",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    ref_doc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref_Doc",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    proc_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "Proc_Time",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    software_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "Software_Version",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    phase: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phase",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    cycle: Optional[int] = field(
        default=None,
        metadata={
            "name": "Cycle",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    rel_orbit: Optional[int] = field(
        default=None,
        metadata={
            "name": "Rel_Orbit",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    abs_orbit: Optional[int] = field(
        default=None,
        metadata={
            "name": "Abs_Orbit",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    state_vector_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "State_Vector_Time",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
            "pattern": r"UTC=.*",
        }
    )
    delta_ut1: Optional[DeltaUT1Type] = field(
        default=None,
        metadata={
            "name": "Delta_UT1",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    x_position: Optional[PositionType] = field(
        default=None,
        metadata={
            "name": "X_Position",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    y_position: Optional[PositionType] = field(
        default=None,
        metadata={
            "name": "Y_Position",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    z_position: Optional[PositionType] = field(
        default=None,
        metadata={
            "name": "Z_Position",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    x_velocity: Optional[VelocityType] = field(
        default=None,
        metadata={
            "name": "X_Velocity",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    y_velocity: Optional[VelocityType] = field(
        default=None,
        metadata={
            "name": "Y_Velocity",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    z_velocity: Optional[VelocityType] = field(
        default=None,
        metadata={
            "name": "Z_Velocity",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    state_vector_source: Optional[str] = field(
        default=None,
        metadata={
            "name": "State_Vector_Source",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
            "pattern": r"..",
        }
    )
    product_err: Optional[int] = field(
        default=None,
        metadata={
            "name": "Product_Err",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    tot_size: Optional[TotSizeType] = field(
        default=None,
        metadata={
            "name": "Tot_Size",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )


@dataclass
class MispointingAnglesType:
    class Meta:
        name = "Mispointing_Angles_Type"

    pitch: Optional[AngleType] = field(
        default=None,
        metadata={
            "name": "Pitch",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    roll: Optional[AngleType] = field(
        default=None,
        metadata={
            "name": "Roll",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    yaw: Optional[AngleType] = field(
        default=None,
        metadata={
            "name": "Yaw",
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
            "pattern": r"TAI=.*",
        }
    )
    utc: Optional[str] = field(
        default=None,
        metadata={
            "name": "UTC",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
            "pattern": r"UTC=.*",
        }
    )
    ut1: Optional[str] = field(
        default=None,
        metadata={
            "name": "UT1",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
            "pattern": r"UT1=.*",
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
class OrbitInformationType:
    class Meta:
        name = "Orbit_Information_Type"

    sensing_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sensing_Start",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
            "pattern": r"TAI=.*",
        }
    )
    abs_orbit_start: Optional[int] = field(
        default=None,
        metadata={
            "name": "Abs_Orbit_Start",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    rel_time_asc_node_start: Optional[RelTimeASCNodeType] = field(
        default=None,
        metadata={
            "name": "Rel_Time_ASC_Node_Start",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    sensing_stop: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sensing_Stop",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
            "pattern": r"TAI=.*",
        }
    )
    abs_orbit_stop: Optional[int] = field(
        default=None,
        metadata={
            "name": "Abs_Orbit_Stop",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    rel_time_asc_node_stop: Optional[RelTimeASCNodeType] = field(
        default=None,
        metadata={
            "name": "Rel_Time_ASC_Node_Stop",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    equator_cross_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "Equator_Cross_Time",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    equator_cross_long: Optional[EquatorCrossLongType] = field(
        default=None,
        metadata={
            "name": "Equator_Cross_Long",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    ascending_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ascending_Flag",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
            "length": 1,
        }
    )


@dataclass
class OrbitScenarioVariableHeader:
    class Meta:
        name = "Orbit_Scenario_Variable_Header"

    time_reference: Optional[OrbitScenarioVariableHeaderTimeReference] = field(
        default=None,
        metadata={
            "name": "Time_Reference",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )


@dataclass
class ProductLocationType:
    class Meta:
        name = "Product_Location_Type"

    start_lat: Optional[LatType] = field(
        default=None,
        metadata={
            "name": "Start_Lat",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    start_long: Optional[LongType] = field(
        default=None,
        metadata={
            "name": "Start_Long",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    stop_lat: Optional[LatType] = field(
        default=None,
        metadata={
            "name": "Stop_Lat",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    stop_long: Optional[LongType] = field(
        default=None,
        metadata={
            "name": "Stop_Long",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )


@dataclass
class RefractionType:
    class Meta:
        name = "Refraction_Type"

    model: Optional[RefractionModelType] = field(
        default=None,
        metadata={
            "name": "Model",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    freq: Optional[FreqType] = field(
        default=None,
        metadata={
            "name": "Freq",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )


@dataclass
class RightAsc(AngleType):
    class Meta:
        name = "Right_Asc"


@dataclass
class SecondsDurationType(SecondsTimeType):
    class Meta:
        name = "Seconds_Duration_Type"


@dataclass
class CycleType:
    class Meta:
        name = "Cycle_Type"

    repeat_cycle: Optional[RepeatCycleType] = field(
        default=None,
        metadata={
            "name": "Repeat_Cycle",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    cycle_length: Optional[CycleLengthType] = field(
        default=None,
        metadata={
            "name": "Cycle_Length",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    anx_longitude: Optional[LongitudeType] = field(
        default=None,
        metadata={
            "name": "ANX_Longitude",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    mlst: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "MLST",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    mlst_drift: Optional[MLSTDriftType] = field(
        default=None,
        metadata={
            "name": "MLST_Drift",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    mlst_nonlinear_drift: Optional[MLSTNonlinearDriftType] = field(
        default=None,
        metadata={
            "name": "MLST_Nonlinear_Drift",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )


@dataclass
class EarthExplorerHeaderType:
    class Meta:
        name = "Earth_Explorer_Header_Type"

    fixed_header: Optional[FixedHeaderType] = field(
        default=None,
        metadata={
            "name": "Fixed_Header",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    variable_header: Optional[AnyTypeType] = field(
        default=None,
        metadata={
            "name": "Variable_Header",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )


@dataclass
class GeoLocation2DType:
    class Meta:
        name = "Geo_Location_2D_Type"

    long: Optional[LongitudeType] = field(
        default=None,
        metadata={
            "name": "Long",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    lat: Optional[LatitudeType] = field(
        default=None,
        metadata={
            "name": "Lat",
            "type": "Element",
            "namespace": __NAMESPACE__,
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
class PointingDirectionType:
    class Meta:
        name = "Pointing_Direction_Type"

    az: Optional[AzimuthType] = field(
        default=None,
        metadata={
            "name": "Az",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    el: Optional[ElevationType] = field(
        default=None,
        metadata={
            "name": "El",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )


@dataclass
class RestitutedOrbitHeaderType:
    class Meta:
        name = "Restituted_Orbit_Header_Type"

    fixed_header: Optional[FixedHeaderType] = field(
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
class SPHType:
    class Meta:
        name = "SPH_Type"

    sph_descriptor: Optional[str] = field(
        default=None,
        metadata={
            "name": "SPH_Descriptor",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    orbit_information: Optional[OrbitInformationType] = field(
        default=None,
        metadata={
            "name": "Orbit_Information",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    product_location: Optional[ProductLocationType] = field(
        default=None,
        metadata={
            "name": "Product_Location",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    product_confidence_data: Optional[ProductConfidenceDataType] = field(
        default=None,
        metadata={
            "name": "Product_Confidence_Data",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )


@dataclass
class EarthExplorerHeader(RestitutedOrbitHeaderType):
    class Meta:
        name = "Earth_Explorer_Header"
        namespace = __NAMESPACE__


@dataclass
class GeoLocationType(GeoLocation2DType):
    class Meta:
        name = "Geo_Location_Type"

    alt: Optional[HeightType] = field(
        default=None,
        metadata={
            "name": "Alt",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )


@dataclass
class OrbitChangeType:
    class Meta:
        name = "Orbit_Change_Type"

    orbit: Optional[OrbitType] = field(
        default=None,
        metadata={
            "name": "Orbit",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    cycle: Optional[CycleType] = field(
        default=None,
        metadata={
            "name": "Cycle",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )
    time_of_anx: Optional[TimeofANXType] = field(
        default=None,
        metadata={
            "name": "Time_of_ANX",
            "type": "Element",
            "namespace": __NAMESPACE__,
            "required": True,
        }
    )


@dataclass
class PolygonTypeType:
    class Meta:
        name = "Polygon_Type_Type"

    polygon_pt: List[GeoLocation2DType] = field(
        default_factory=list,
        metadata={
            "name": "Polygon_Pt",
            "type": "Element",
            "namespace": __NAMESPACE__,
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
class ListofOrbitChangesType:
    class Meta:
        name = "List_of_Orbit_Changes_Type"

    orbit_change: List[OrbitChangeType] = field(
        default_factory=list,
        metadata={
            "name": "Orbit_Change",
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
class RestitutedOrbitFileType:
    class Meta:
        name = "Restituted_Orbit_File_Type"

    earth_explorer_header: Optional[RestitutedOrbitHeaderType] = field(
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
class EarthExplorerFile(RestitutedOrbitFileType):
    class Meta:
        name = "Earth_Explorer_File"
        namespace = __NAMESPACE__
