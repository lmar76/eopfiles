"""Test the `eopfiles.basic` module."""
from dataclasses import fields
from decimal import Decimal

import pytest

from eopfiles import basic


class TestPositionComponentType:
    """Test the `PositionComponentType` class."""

    @pytest.mark.parametrize(
        "value",
        ["-1606749.988", "-4135675.595"]
    )
    def test_creation(self, value):
        """Test instance creation."""
        obj = basic.PositionComponentType(value)
        fs = fields(obj)
        assert [f.name for f in fs] == ["value", "unit"]
        assert isinstance(obj, basic.PositionComponentType)
        assert obj.value == value
        assert obj.to_float() == float(value)
        assert obj.unit == next(f for f in fs if f.name == "unit").default

    @pytest.mark.parametrize(
        "value, expected",
        [
            (34.4567, "+0000034.457")
        ]
    )
    def test_from_float(self, value, expected):
        """Test the `PositionComponentType.from_float` class method."""
        obj = basic.PositionComponentType.from_float(value)
        assert isinstance(obj, basic.PositionComponentType)
        assert obj.value == expected


class TestVelocityComponentType:
    """Test the `VelocityComponentType` class."""

    @pytest.mark.parametrize(
        "value",
        ["-2876.652288", "+5985.303441"]
    )
    def test_creation(self, value):
        """Test instance creation."""
        obj = basic.VelocityComponentType(value)
        fs = fields(obj)
        assert [f.name for f in fs] == ["value", "unit"]
        assert isinstance(obj, basic.VelocityComponentType)
        assert obj.value == value
        assert obj.to_float() == float(value)
        assert obj.unit == next(f for f in fs if f.name == "unit").default

    @pytest.mark.parametrize(
        "value, expected",
        [
            (34.45678999, "+0034.456790")
        ]
    )
    def test_from_float(self, value, expected):
        """Test the `VelocityComponentType.from_float` class method."""
        obj = basic.VelocityComponentType.from_float(value)
        assert isinstance(obj, basic.VelocityComponentType)
        assert obj.value == expected
