"""Orbit types."""
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List, Optional

from . import basic, times
from .exceptions import PositionComponentUnitError, VelocityComponentUnitError


POSITION_COMPONENT_UNIT = "m"
VELOCITY_COMPONENT_UNIT = "m/s"


class RefFrame(Enum):
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


class TimeReference(Enum):
    TAI = "TAI"
    UTC = "UTC"
    UT1 = "UT1"


@dataclass
class PositionComponent:
    class Meta:
        name = "Position_Component"

    value: basic.FloatingFmtValue = field(
        metadata={
            "required": True,
            "format": "{:+012.3f}"
        }
    )
    unit: str = field(
        default=POSITION_COMPONENT_UNIT,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

    def valid_unit(self) -> bool:
        return self.unit == POSITION_COMPONENT_UNIT

    def validate_unit(self) -> None:
        if not self.valid_unit():
            raise PositionComponentUnitError(f"Wrong unit '{self.unit}'")


@dataclass
class VelocityComponent:
    class Meta:
        name = "Velocity_Component"

    value: basic.FloatingFmtValue = field(
        metadata={
            "required": True,
            "format": "{:+012.6f}"
        }
    )
    unit: str = field(
        default=VELOCITY_COMPONENT_UNIT,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

    def valid_unit(self) -> bool:
        return self.unit == VELOCITY_COMPONENT_UNIT

    def validate_unit(self) -> None:
        if not self.valid_unit():
            raise VelocityComponentUnitError(f"Wrong unit '{self.unit}'")


@dataclass
class AbsoluteOrbit:

    value: basic.IntFmtValue = field(
        metadata={
            "required": True,
            "format": r"{:+06d}"
        }
    )


@dataclass
class OSV:
    class Meta:
        name = "OSV"

    tai: datetime = field(
        metadata={
            "name": "TAI",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
            "pattern": times.TAI_DATE_TIME_PATTERN_USEC,
            "format": "TAI=%Y-%m-%dT%H:%M:%S.%f"
        }
    )
    utc: datetime = field(
        metadata={
            "name": "UTC",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
            "pattern": times.UTC_DATE_TIME_PATTERN_USEC,
            "format": "UTC=%Y-%m-%dT%H:%M:%S.%f"
        }
    )
    ut1: datetime = field(
        metadata={
            "name": "UT1",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
            "pattern": times.UT1_DATE_TIME_PATTERN_USEC,
            "format": "UT1=%Y-%m-%dT%H:%M:%S.%f"
        }
    )
    absolute_orbit: AbsoluteOrbit = field(
        metadata={
            "name": "Absolute_Orbit",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    x: PositionComponent = field(
        metadata={
            "name": "X",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    y: PositionComponent = field(
        metadata={
            "name": "Y",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    z: PositionComponent = field(
        metadata={
            "name": "Z",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    vx: VelocityComponent = field(
        metadata={
            "name": "VX",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    vy: VelocityComponent = field(
        metadata={
            "name": "VY",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    vz: VelocityComponent = field(
        metadata={
            "name": "VZ",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    quality: str = field(
        default="0000000000000",
        metadata={
            "name": "Quality",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
            "pattern": r"0{13}"
        }
    )


@dataclass
class ListOfOSVs:
    class Meta:
        name = "List_of_OSVs"

    osvs: List[OSV] = field(
        default_factory=list,
        metadata={
            "name": "OSV",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
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
