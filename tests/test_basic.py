"""Test the `eopfiles.basic` module."""
import pytest

from eopfiles import basic


class TestPositionComponentType:
    """Test the `PositionComponent` class."""

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
        obj = basic.PositionComponent(**params)
        assert isinstance(obj, basic.PositionComponent)
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
        """Test the `PositionComponent.from_float` class method."""
        obj = basic.PositionComponent.from_float(value)
        assert isinstance(obj, basic.PositionComponent)
        assert obj.text == expected


class TestVelocityComponentType:
    """Test the `VelocityComponent` class."""

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
        obj = basic.VelocityComponent(**params)
        assert isinstance(obj, basic.VelocityComponent)
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
        """Test the `VelocityComponent.from_float` class method."""
        obj = basic.VelocityComponent.from_float(value)
        assert isinstance(obj, basic.VelocityComponent)
        assert obj.text == expected
