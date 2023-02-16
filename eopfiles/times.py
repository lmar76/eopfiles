"""Time-related types and global variables."""
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional


NO_REF_DATE_TIME_PATTERN = (
    r"(\d{4}-(((01|03|05|07|08|10|12)-(0[1-9]|[1,2][0-9]|3[0,1]))|((04|06|09|11)"
    r"-(0[1-9]|[1,2][0-9]|30))|(02-(0[1-9]|[1,2][0-9])))T([0,1][0-9]|2[0-3])(:[0-5][0-9]){2})"
)
UTC_DATE_TIME_PATTERN = r"UTC=" + NO_REF_DATE_TIME_PATTERN
VALIDITY_START_DATE_TIME_PATTERN = (
    r"UTC=((\d{4}-(((01|03|05|07|08|10|12)-(0[1-9]|[1,2][0-9]|3[0,1]))|((04|06|09|11)"
    r"-(0[1-9]|[1,2][0-9]|30))|(02-(0[1-9]|[1,2][0-9])))T([0,1][0-9]|2[0-3])(:[0-5][0-9]){2}))"
    r"|(0000-00-00T00:00:00)"
)
VALIDITY_STOP_DATE_TIME_PATTERN = (
    r"UTC=((\d{4}-(((01|03|05|07|08|10|12)-(0[1-9]|[1,2][0-9]|3[0,1]))|((04|06|09|11)"
    r"-(0[1-9]|[1,2][0-9]|30))|(02-(0[1-9]|[1,2][0-9])))T([0,1][0-9]|2[0-3])(:[0-5][0-9]){2}))"
    r"|(9999-99-99T99:99:99)"
)

NO_REF_DATE_TIME_PATTERN_FSEC = NO_REF_DATE_TIME_PATTERN + r"(.\d*)?"

NO_REF_DATE_TIME_PATTERN_MSEC = NO_REF_DATE_TIME_PATTERN + r".\d{3}"
UTC_DATE_TIME_PATTERN_MSEC = r"UTC=" + NO_REF_DATE_TIME_PATTERN_MSEC

NO_REF_DATE_TIME_PATTERN_USEC = NO_REF_DATE_TIME_PATTERN + r".\d{6}"
TAI_DATE_TIME_PATTERN_USEC = r"TAI=" + NO_REF_DATE_TIME_PATTERN_FSEC
UTC_DATE_TIME_PATTERN_USEC = r"UTC=" + NO_REF_DATE_TIME_PATTERN_FSEC
UT1_DATE_TIME_PATTERN_USEC = r"UT1=" + NO_REF_DATE_TIME_PATTERN_FSEC


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
