"""Test the `eopfiles.orbits` module."""
import re
from dataclasses import fields
from datetime import datetime

import pytest
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser

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
                "x": basic.PositionComponentType.from_float(-2025630.454),
                "y": basic.PositionComponentType.from_float(6765565.948),
                "z": basic.PositionComponentType.from_float(0445518.75),
                "vx": basic.VelocityComponentType.from_float(1655.255131),
                "vy": basic.VelocityComponentType.from_float(-2.394418),
                "vz": basic.VelocityComponentType.from_float(7415.236254),
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
            assert isinstance(value, basic.PositionComponentType)
            assert value.text == parameters[attr].text
            assert value.unit == parameters[attr].unit
        for attr in ("vx", "vy", "vz"):
            value = getattr(osv, attr)
            assert isinstance(value, basic.VelocityComponentType)
            assert value.text == parameters[attr].text
            assert value.unit == parameters[attr].unit
        assert isinstance(osv.quality, str)
        assert osv.quality == parameters["quality"]
        assert re.match(next(f for f in fs if f.name == "quality").metadata["pattern"], osv.quality)

    @pytest.mark.parametrize(
        "s, expected",
        [
            (
                """
                <OSV>
                    <TAI>TAI=2014-06-11T10:50:40.855382</TAI>
                    <UTC>UTC=2014-06-11T10:51:15.855382</UTC>
                    <UT1>UT1=2014-06-11T10:51:16.155381</UT1>
                    <Absolute_Orbit>+00000</Absolute_Orbit>
                    <X unit="m">-2025630.454</X>
                    <Y unit="m">+6765565.948</Y>
                    <Z unit="m">+0445518.754</Z>
                    <VX unit="m/s">+1655.255131</VX>
                    <VY unit="m/s">-0002.394418</VY>
                    <VZ unit="m/s">+7415.236254</VZ>
                    <Quality>0000000000000</Quality>
                </OSV>""",
                orbits.OSV(
                    tai="TAI=2014-06-11T10:50:40.855382",
                    utc="UTC=2014-06-11T10:51:15.855382",
                    ut1="UT1=2014-06-11T10:51:16.155381",
                    absolute_orbit=orbits.AbsoluteOrbit.from_int(0),
                    x=basic.PositionComponentType.from_float(-2025630.454),
                    y=basic.PositionComponentType.from_float(6765565.948),
                    z=basic.PositionComponentType.from_float(0445518.75),
                    vx=basic.VelocityComponentType.from_float(1655.255131),
                    vy=basic.VelocityComponentType.from_float(-2.394418),
                    vz=basic.VelocityComponentType.from_float(7415.236254),
                    quality="0000000000000"
                )
            )
        ]
    )
    def from_string(self, s, expected):
        """Test instance creation from XML string."""
        parser = XmlParser(context=XmlContext())
        osv = parser.from_string(s)
        assert isinstance(osv, orbits.OSV)
        fs = fields(osv)
        assert (
            [f.name for f in fs]
            == ["tai", "utc", "ut1", "absolute_orbit",
                "x", "y", "z", "vx", "vy", "vz", "quality"]
        )
        for attr in ("tai", "utc", "utc"):
            assert isinstance(getattr(osv, attr), str)
            assert getattr(osv, attr) == getattr(expected, attr)
        assert isinstance(osv.absolute_orbit, int)
        assert osv.absolute_orbit == expected.absolute_orbit
        for attr in ("x", "y", "z"):
            value = getattr(osv, attr)
            assert isinstance(value, basic.PositionComponentType)
            assert value.text == getattr(expected, attr).text
            assert value.unit == getattr(expected, attr).unit
        for attr in ("vx", "vy", "vz"):
            value = getattr(osv, attr)
            assert isinstance(value, basic.VelocityComponentType)
            assert value.text == getattr(expected, attr).text
            assert value.unit == getattr(expected, attr).unit
        assert isinstance(osv.quality, str)
        assert osv.quality == expected.quality
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
                    "x": basic.PositionComponentType.from_float(-2025630.454),
                    "y": basic.PositionComponentType.from_float(6765565.948),
                    "z": basic.PositionComponentType.from_float(0445518.75),
                    "vx": basic.VelocityComponentType.from_float(1655.255131),
                    "vy": basic.VelocityComponentType.from_float(-2.394418),
                    "vz": basic.VelocityComponentType.from_float(7415.236254),
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
                        x=basic.PositionComponentType.from_float(-2025630.454),
                        y=basic.PositionComponentType.from_float(6765565.948),
                        z=basic.PositionComponentType.from_float(0445518.75),
                        vx=basic.VelocityComponentType.from_float(1655.255131),
                        vy=basic.VelocityComponentType.from_float(-2.394418),
                        vz=basic.VelocityComponentType.from_float(7415.236254),
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

    @pytest.mark.parametrize(
        "s, expected",
        [
            (
                """
                <List_of_OSVs count=1>
                    <OSV>
                        <TAI>TAI=2014-06-11T10:50:40.855382</TAI>
                        <UTC>UTC=2014-06-11T10:51:15.855382</UTC>
                        <UT1>UT1=2014-06-11T10:51:16.155381</UT1>
                        <Absolute_Orbit>+00000</Absolute_Orbit>
                        <X unit="m">-2025630.454</X>
                        <Y unit="m">+6765565.948</Y>
                        <Z unit="m">+0445518.754</Z>
                        <VX unit="m/s">+1655.255131</VX>
                        <VY unit="m/s">-0002.394418</VY>
                        <VZ unit="m/s">+7415.236254</VZ>
                        <Quality>0000000000000</Quality>
                    </OSV>
                </List_of_OSVs>""",
                orbits.ListOfOSVs(
                    osvs=[
                        orbits.OSV(
                            tai="TAI=2014-06-11T10:50:40.855382",
                            utc="UTC=2014-06-11T10:51:15.855382",
                            ut1="UT1=2014-06-11T10:51:16.155381",
                            absolute_orbit=orbits.AbsoluteOrbit.from_int(0),
                            x=basic.PositionComponentType.from_float(-2025630.454),
                            y=basic.PositionComponentType.from_float(6765565.948),
                            z=basic.PositionComponentType.from_float(0445518.75),
                            vx=basic.VelocityComponentType.from_float(1655.255131),
                            vy=basic.VelocityComponentType.from_float(-2.394418),
                            vz=basic.VelocityComponentType.from_float(7415.236254),
                            quality="0000000000000"
                        )
                    ],
                    count=1
                )
            )
        ]
    )
    def from_string(self, s, expected):
        """Test instance creation from XML string."""
        parser = XmlParser(context=XmlContext())
        list_of_osvs = parser.from_string(s)
        assert isinstance(list_of_osvs, orbits.ListOfOSVs)
        fs = fields(list_of_osvs)
        assert [f.name for f in fs] == ["osvs", "count"]
        assert len(list_of_osvs.osvs) == expected.osvs
        assert list_of_osvs.count == expected.count
