"""Test the `eopfiles.orbits` module."""
import re
from dataclasses import fields
from datetime import datetime

import pandas
import pytest

from eopfiles import basic, exceptions, orbits


class TestPositionComponent:
    """Test the `PositionComponent` class."""

    @pytest.mark.parametrize(
        "params",
        [
            {
                "value": basic.FloatingFmtValue("-1606749.988")
            },
            {
                "value": basic.FloatingFmtValue(-1606749.988)
            },
            {
                "value": basic.FloatingFmtValue(-1606749988e-3)
            },
            {
                "value": basic.FloatingFmtValue(-1606749.988),
                "unit": "xxx"
            },
        ]
    )
    def test_creation(self, params):
        """Test instance creation."""
        obj = orbits.PositionComponent(**params)
        assert isinstance(obj, orbits.PositionComponent)
        assert isinstance(obj.value, basic.FloatingFmtValue)
        assert obj.value == params["value"]
        expected_unit = params.get("unit") or orbits.POSITION_COMPONENT_UNIT
        assert obj.unit == expected_unit

    @pytest.mark.parametrize(
        "params, result",
        [
            (
                {"value": basic.FloatingFmtValue(-1606749988e-3)},
                True
            ),
            (
                {"value": basic.FloatingFmtValue(-1606749.988), "unit": "xxx"},
                False
            )
        ]
    )
    def test_valid_unit(self, params, result):
        """Test the `PositionComponent.valid_unit` method."""
        obj = orbits.PositionComponent(**params)
        assert obj.valid_unit() is result

    @pytest.mark.parametrize(
        "params, exc",
        [
            (
                {"value": basic.FloatingFmtValue(-1606749988e-3)},
                None
            ),
            (
                {"value": basic.FloatingFmtValue(-1606749.988), "unit": "xxx"},
                exceptions.PositionComponentUnitError
            )
        ]
    )
    def test_validate_unit(self, params, exc):
        """Test the `PositionComponent.validate_unit` method."""
        obj = orbits.PositionComponent(**params)
        if exc:
            with pytest.raises(exc):
                obj.validate_unit()
        else:
            obj.validate_unit()


class TestVelocityComponentType:
    """Test the `VelocityComponent` class."""

    @pytest.mark.parametrize(
        "params",
        [
            {
                "value": basic.FloatingFmtValue("-2876.652288")
            },
            {
                "value": basic.FloatingFmtValue(-2876.652288)
            },
            {
                "value": basic.FloatingFmtValue(-2876652288e-6)
            },
            {
                "value": basic.FloatingFmtValue(-2876.652288),
                "unit": "xxx"
            },
        ]
    )
    def test_creation(self, params):
        """Test instance creation."""
        obj = orbits.VelocityComponent(**params)
        assert isinstance(obj, orbits.VelocityComponent)
        assert isinstance(obj.value, basic.FloatingFmtValue)
        assert obj.value == params["value"]
        expected_unit = params.get("unit") or orbits.VELOCITY_COMPONENT_UNIT
        assert obj.unit == expected_unit

    @pytest.mark.parametrize(
        "params, result",
        [
            (
                {"value": basic.FloatingFmtValue(-2876652288e-6)},
                True
            ),
            (
                {"value": basic.FloatingFmtValue(-2876.652288), "unit": "xxx"},
                False
            )
        ]
    )
    def test_valid_unit(self, params, result):
        """Test the `VelocityComponent.valid_unit` method."""
        obj = orbits.VelocityComponent(**params)
        assert obj.valid_unit() is result

    @pytest.mark.parametrize(
        "params, exc",
        [
            (
                {"value": basic.FloatingFmtValue(-2876652288e-6)},
                None
            ),
            (
                {"value": basic.FloatingFmtValue(-2876.652288), "unit": "xxx"},
                exceptions.VelocityComponentUnitError
            )
        ]
    )
    def test_validate_unit(self, params, exc):
        """Test the `VelocityComponent.validate_unit` method."""
        obj = orbits.VelocityComponent(**params)
        if exc:
            with pytest.raises(exc):
                obj.validate_unit()
        else:
            obj.validate_unit()


class TestOSV:
    """Test the `OSV` class."""

    @pytest.mark.parametrize(
        "parameters",
        [
            {
                "tai": datetime(2014, 6, 11, 10, 50, 40, 855382),
                "utc": datetime(2014, 6, 11, 10, 51, 15, 855382),
                "ut1": datetime(2014, 6, 11, 10, 51, 15, 155381),
                "absolute_orbit": orbits.AbsoluteOrbit(basic.IntFmtValue(0)),
                "x": orbits.PositionComponent(basic.FloatingFmtValue(-2025630.454)),
                "y": orbits.PositionComponent(basic.FloatingFmtValue(6765565.948)),
                "z": orbits.PositionComponent(basic.FloatingFmtValue(0445518.75)),
                "vx": orbits.VelocityComponent(basic.FloatingFmtValue(1655.255131)),
                "vy": orbits.VelocityComponent(basic.FloatingFmtValue(-2.394418)),
                "vz": orbits.VelocityComponent(basic.FloatingFmtValue(7415.236254)),
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
            assert isinstance(getattr(osv, attr), datetime)
            assert getattr(osv, attr) == parameters[attr]
        assert isinstance(osv.absolute_orbit, orbits.AbsoluteOrbit)
        assert isinstance(osv.absolute_orbit.value, basic.IntFmtValue)
        assert osv.absolute_orbit.value == parameters["absolute_orbit"].value
        for attr in ("x", "y", "z"):
            value = getattr(osv, attr)
            assert isinstance(value, orbits.PositionComponent)
            assert value.value == parameters[attr].value
            assert value.unit == parameters[attr].unit
        for attr in ("vx", "vy", "vz"):
            value = getattr(osv, attr)
            assert isinstance(value, orbits.VelocityComponent)
            assert value.value == parameters[attr].value
            assert value.unit == parameters[attr].unit
        assert isinstance(osv.quality, str)
        assert osv.quality == parameters["quality"]
        assert re.match(next(f for f in fs if f.name == "quality").metadata["pattern"], osv.quality)


class TestListOfOSVs:
    """Test the `ListOfOSVs` class."""

    @pytest.mark.parametrize(
        "parameters",
        [
            {
                "osvs": [
                    orbits.OSV(
                        tai=datetime(2014, 6, 11, 10, 50, 40, 855382),
                        utc=datetime(2014, 6, 11, 10, 51, 15, 855382),
                        ut1=datetime(2014, 6, 11, 10, 51, 15, 155381),
                        absolute_orbit=orbits.AbsoluteOrbit(basic.IntFmtValue(0)),
                        x=orbits.PositionComponent(basic.FloatingFmtValue(-2025630.454)),
                        y=orbits.PositionComponent(basic.FloatingFmtValue(6765565.948)),
                        z=orbits.PositionComponent(basic.FloatingFmtValue(0445518.75)),
                        vx=orbits.VelocityComponent(basic.FloatingFmtValue(1655.255131)),
                        vy=orbits.VelocityComponent(basic.FloatingFmtValue(-2.394418)),
                        vz=orbits.VelocityComponent(basic.FloatingFmtValue(7415.236254)),
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
        assert len(list_of_osvs.osvs) == len(parameters["osvs"])

    @pytest.mark.parametrize(
        "parameters",
        [
            {
                "osvs": [
                    orbits.OSV(
                        tai=datetime(2014, 6, 11, 10, 50, 40, 855382),
                        utc=datetime(2014, 6, 11, 10, 51, 15, 855382),
                        ut1=datetime(2014, 6, 11, 10, 51, 15, 155381),
                        absolute_orbit=orbits.AbsoluteOrbit(basic.IntFmtValue(0)),
                        x=orbits.PositionComponent(basic.FloatingFmtValue(-2025630.454)),
                        y=orbits.PositionComponent(basic.FloatingFmtValue(6765565.948)),
                        z=orbits.PositionComponent(basic.FloatingFmtValue(0445518.75)),
                        vx=orbits.VelocityComponent(basic.FloatingFmtValue(1655.255131)),
                        vy=orbits.VelocityComponent(basic.FloatingFmtValue(-2.394418)),
                        vz=orbits.VelocityComponent(basic.FloatingFmtValue(7415.236254)),
                        quality="0000000000000"
                    )
                ],
                "count": 1
            }
        ]
    )
    def test_to_dataframe(self, parameters):
        """Test `ListOfOSVs.to_dataframe` method."""
        df = orbits.ListOfOSVs(**parameters).to_dataframe()
        assert isinstance(df, pandas.DataFrame)
        assert df.shape[0] == len(parameters["osvs"])
        assert df.shape[0] == parameters["count"]
        for param in ("tai", "ut1", "utc"):
            assert param in df
            assert df[param].to_list() == [getattr(osv, param) for osv in parameters["osvs"]]
        for param in ("absolute_orbit", "x", "y", "z", "vx", "vy", "vz"):
            assert param in df
            assert df[param].to_list() == [getattr(osv, param).value for osv in parameters["osvs"]]
