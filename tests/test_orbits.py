"""Test the `eopfiles.orbits` module."""
import re
from dataclasses import fields
from datetime import datetime

import pytest

from eopfiles import basic, orbits


class TestOSV:
    """Test the `OSV` class."""

    @pytest.mark.parametrize(
        "parameters",
        [
            {
                "tai": "TAI=2014-06-11T10:50:40.855382",
                "utc": "UTC=2014-06-11T10:51:15.855382",
                "ut1": "UT1=2014-06-11T10:51:16.155381",
                "absolute_orbit": orbits.AbsoluteOrbit.from_int(0),
                "x": basic.PositionComponent.from_float(-2025630.454),
                "y": basic.PositionComponent.from_float(6765565.948),
                "z": basic.PositionComponent.from_float(0445518.75),
                "vx": basic.VelocityComponent.from_float(1655.255131),
                "vy": basic.VelocityComponent.from_float(-2.394418),
                "vz": basic.VelocityComponent.from_float(7415.236254),
                "quality": "0000000000000"
            }
        ]
    )
    def test_creation(self, parameters):
        """Test instance creation."""
        osv = orbits.OSV(**parameters)
        assert isinstance(osv, orbits.OSV)
        fs = fields(osv)
        assert (
            [f.name for f in fs]
            == ["tai", "utc", "ut1", "absolute_orbit",
                "x", "y", "z", "vx", "vy", "vz", "quality"]
        )
        for attr in ("tai", "utc", "utc"):
            assert isinstance(getattr(osv, attr), str)
            assert getattr(osv, attr) == parameters[attr]
        assert isinstance(osv.absolute_orbit, orbits.AbsoluteOrbit)
        assert osv.absolute_orbit.text == parameters["absolute_orbit"].text
        for attr in ("x", "y", "z"):
            value = getattr(osv, attr)
            assert isinstance(value, basic.PositionComponent)
            assert value.text == parameters[attr].text
            assert value.unit == parameters[attr].unit
        for attr in ("vx", "vy", "vz"):
            value = getattr(osv, attr)
            assert isinstance(value, basic.VelocityComponent)
            assert value.text == parameters[attr].text
            assert value.unit == parameters[attr].unit
        assert isinstance(osv.quality, str)
        assert osv.quality == parameters["quality"]
        assert re.match(next(f for f in fs if f.name == "quality").metadata["pattern"], osv.quality)

    @pytest.mark.parametrize(
        "parameters, expected",
        [
            (
                {
                    "tai": "TAI=2014-06-11T10:50:40.855382",
                    "utc": "UTC=2014-06-11T10:51:15.855382",
                    "ut1": "UT1=2014-06-11T10:51:16.155381",
                    "absolute_orbit": orbits.AbsoluteOrbit.from_int(0),
                    "x": basic.PositionComponent.from_float(-2025630.454),
                    "y": basic.PositionComponent.from_float(6765565.948),
                    "z": basic.PositionComponent.from_float(0445518.75),
                    "vx": basic.VelocityComponent.from_float(1655.255131),
                    "vy": basic.VelocityComponent.from_float(-2.394418),
                    "vz": basic.VelocityComponent.from_float(7415.236254),
                    "quality": "0000000000000"
                },
                dict(
                    tai=datetime(2014, 6, 11, 10, 50, 40, 855382),
                    utc=datetime(2014, 6, 11, 10, 51, 15, 855382),
                    ut1=datetime(2014, 6, 11, 10, 51, 16, 155381),
                    absolute_orbit=0,
                    x=-2025630.454,
                    y=+6765565.948,
                    z=+0445518.750,
                    vx=+1655.255131,
                    vy=-0002.394418,
                    vz=+7415.236254,
                    quality="0000000000000"
                )
            )
        ]
    )
    def test_to_dict(self, parameters, expected):
        """Test the `OSV.to_dict` method."""
        osv = orbits.OSV(**parameters)
        assert osv.to_dict() == expected


class TestListOfOSVs:
    """Test the `ListOfOSVs` class."""

    @pytest.mark.parametrize(
        "parameters",
        [
            {
                "osvs": [
                    orbits.OSV(
                        tai="TAI=2014-06-11T10:50:40.855382",
                        utc="UTC=2014-06-11T10:51:15.855382",
                        ut1="UT1=2014-06-11T10:51:16.155381",
                        absolute_orbit=orbits.AbsoluteOrbit.from_int(0),
                        x=basic.PositionComponent.from_float(-2025630.454),
                        y=basic.PositionComponent.from_float(6765565.948),
                        z=basic.PositionComponent.from_float(0445518.75),
                        vx=basic.VelocityComponent.from_float(1655.255131),
                        vy=basic.VelocityComponent.from_float(-2.394418),
                        vz=basic.VelocityComponent.from_float(7415.236254),
                        quality="0000000000000"
                    )
                ],
                "count": 1
            }
        ]
    )
    def test_creation(self, parameters):
        """Test instance creation."""
        list_of_osvs = orbits.ListOfOSVs(**parameters)
        assert isinstance(list_of_osvs, orbits.ListOfOSVs)
        assert hasattr(list_of_osvs, "osvs")
        assert isinstance(list_of_osvs.osvs, list)
        for item in list_of_osvs.osvs:
            assert isinstance(item, orbits.OSV)
        assert isinstance(list_of_osvs.count, int)
        assert list_of_osvs.count == parameters["count"]
