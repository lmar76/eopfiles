"""Test the `eopfiles.basic` module."""
from dataclasses import fields
from decimal import Decimal

import pytest

from eopfiles import basic


class TestPositionComponentType:
    """Test the `PositionComponentType` class."""

    @pytest.mark.parametrize(
        "value",
        [Decimal(10), Decimal(10.5)]
    )
    def test_creation(self, value):
        """Test instance creation."""
        obj = basic.PositionComponentType(value)
        fs = fields(obj)
        assert [f.name for f in fs] == ["value", "unit"]
        assert isinstance(obj, basic.PositionComponentType)
        assert obj.value == value
        assert obj.unit == next(f for f in fs if f.name == "unit").default


class TestVelocityComponentType:
    """Test the `VelocityComponentType` class."""

    @pytest.mark.parametrize(
        "value",
        [Decimal(10), Decimal(10.5)]
    )
    def test_creation(self, value):
        """Test instance creation."""
        obj = basic.VelocityComponentType(value)
        fs = fields(obj)
        assert [f.name for f in fs] == ["value", "unit"]
        assert isinstance(obj, basic.VelocityComponentType)
        assert obj.value == value
        assert obj.unit == next(f for f in fs if f.name == "unit").default
