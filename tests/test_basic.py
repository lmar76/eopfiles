"""Test the `eopfiles.basic` module."""
import pytest

from eopfiles import basic


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
                "value": basic.FloatingFmtValue("-4135675.595"),
                "unit": "xxxxxx"
            }
        ]
    )
    def test_creation(self, params):
        """Test instance creation."""
        obj = basic.PositionComponent(**params)
        assert isinstance(obj, basic.PositionComponent)
        assert isinstance(obj.value, basic.FloatingFmtValue)
        assert obj.value == params["value"]
        if "unit" in params:
            assert obj.unit == params["unit"]


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
                "value": basic.FloatingFmtValue("+5985.303441"),
                "unit": "aaa"
            }
        ]
    )
    def test_creation(self, params):
        """Test instance creation."""
        obj = basic.VelocityComponent(**params)
        assert isinstance(obj, basic.VelocityComponent)
        assert isinstance(obj.value, basic.FloatingFmtValue)
        assert obj.value == params["value"]
        if "unit" in params:
            assert obj.unit == params["unit"]
