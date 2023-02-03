from __future__ import annotations
from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional


NO_REF_DATE_TIME_PATTERN = (
    r"(\d{4}-(((01|03|05|07|08|10|12)-(0[1-9]|[1,2][0-9]|3[0,1]))|((04|06|09|11)"
    r"-(0[1-9]|[1,2][0-9]|30))|(02-(0[1-9]|[1,2][0-9])))T([0,1][0-9]|2[0-3])(:[0-5][0-9]){2}"
    r"|0000-00-00T00:00:00|9999-99-99T99:99:99)(.\d*)?"
)
MISSION_DATE_TIME_PATTERN = (
    r"[A-Z0-9]{3}=(\d{4}-(((01|03|05|07|08|10|12)-(0[1-9]|[1,2][0-9]|3[0,1]))"
    r"|((04|06|09|11)-(0[1-9]|[1,2][0-9]|30))|(02-(0[1-9]|[1,2][0-9])))T"
    r"([0,1][0-9]|2[0-3])(:[0-5][0-9]){2}|0000-00-00T00:00:00|9999-99-99T99:99:99)(.\d*)?"
)
TAI_DATE_TIME_PATTERN = r"TAI=.*"
UTC_DATE_TIME_PATTERN = r"UTC=.*"
UT1_DATE_TIME_PATTERN = r"UT1=.*"
UTC_BOM_DATE_TIME_PATTERN = r"UTC=0000-00-00T00:00:00"
UTC_EOM_DATE_TIME_PATTERN = r"UTC=9999-99-99T99:99:99"


class TimeReferenceType(Enum):
    UTC = "UTC"
    UT1 = "UT1"
    TAI = "TAI"
    GPS = "GPS"


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
class SecondsDurationType(SecondsTimeType):
    class Meta:
        name = "Seconds_Duration_Type"