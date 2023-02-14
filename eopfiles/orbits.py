"""Orbit types."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Optional

from . import basic, times


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

    tai: str = field(
        metadata={
            "name": "TAI",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
            "pattern": times.TAI_DATE_TIME_PATTERN,
        }
    )
    utc: str = field(
        metadata={
            "name": "UTC",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
            "pattern": times.UTC_DATE_TIME_PATTERN,
        }
    )
    ut1: str = field(
        metadata={
            "name": "UT1",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
            "pattern": times.UT1_DATE_TIME_PATTERN,
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
    x: basic.PositionComponent = field(
        metadata={
            "name": "X",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    y: basic.PositionComponent = field(
        metadata={
            "name": "Y",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    z: basic.PositionComponent = field(
        metadata={
            "name": "Z",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    vx: basic.VelocityComponent = field(
        metadata={
            "name": "VX",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    vy: basic.VelocityComponent = field(
        metadata={
            "name": "VY",
            "type": "Element",
            "namespace": basic.__NAMESPACE__,
            "required": True,
        }
    )
    vz: basic.VelocityComponent = field(
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

    def to_dict(self) -> dict[str, Any]:
        """Convert `OSV` to dict.

        Returns
        -------
        dict[str, Any]
            `OSV` information.

        """
        return {
            "tai": datetime.strptime(self.tai[4:], "%Y-%m-%dT%H:%M:%S.%f"),
            "utc": datetime.strptime(self.utc[4:], "%Y-%m-%dT%H:%M:%S.%f"),
            "ut1": datetime.strptime(self.ut1[4:], "%Y-%m-%dT%H:%M:%S.%f"),
            "absolute_orbit": self.absolute_orbit.value,
            "x": self.x.value,
            "y": self.y.value,
            "z": self.z.value,
            "vx": self.vx.value,
            "vy": self.vy.value,
            "vz": self.vz.value,
            "quality": self.quality
        }


@dataclass
class ListOfOSVs:
    class Meta:
        name = "List_of_OSVs"

    osvs: list[OSV] = field(
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
