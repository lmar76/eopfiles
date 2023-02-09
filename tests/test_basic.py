"""Test the `eopfiles.basic` module."""
from dataclasses import fields

import pytest

from eopfiles import basic


class TestPositionComponentType:
    """Test the `PositionComponentType` class."""

    @pytest.mark.parametrize(
        "params",
        [
            {
                "text": "-1606749.988"
            },
            {
                "text": "-4135675.595",
                "unit": "xxxxxx"
            }
        ]
    )
    def test_creation(self, params):
        """Test instance creation."""
        obj = basic.PositionComponentType(**params)
        assert isinstance(obj, basic.PositionComponentType)
        assert obj.text == params["text"]
        if "unit" in params:
            assert obj.unit == params["unit"]
        assert obj.to_float() == float(params["text"])

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
        assert obj.text == expected


class TestVelocityComponentType:
    """Test the `VelocityComponentType` class."""

    @pytest.mark.parametrize(
        "params",
        [
            {
                "text": "-2876.652288"
            },
            {
                "text": "+5985.303441",
                "unit": "aaa"
            }
        ]
    )
    def test_creation(self, params):
        """Test instance creation."""
        obj = basic.VelocityComponentType(**params)
        assert isinstance(obj, basic.VelocityComponentType)
        assert obj.text == params["text"]
        if "unit" in params:
            assert obj.unit == params["unit"]
        assert obj.to_float() == float(params["text"])

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
        assert obj.text == expected
