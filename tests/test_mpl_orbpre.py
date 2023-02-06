"""Test the `eopfiles.mpl_orbpre` module."""
import pytest
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from eopfiles import basic, mpl_orbpre


class TestEEPredictedOrbitFile:
    """Test the `EEPredictedOrbitFile` class."""

    @pytest.mark.parametrize(
        "filename, ffs",
        [
            (
                "CS_TEST_MPL_ORBPRE_20100409T105738_20100410T015421_0007.EEF",
                "FFS1"
            ),
            (
                "S1A_TEST_MPL_ORBPRE_20140404T183104_20140405T091945_0004.EOF",
                "FFS2"
            ),
            (
                "MA1_TEST_MPL_ORBPRE_20210401T174620_20210402T085834_0001.EOF",
                "FFS3"
            ),
        ]
    )
    def test_from_file(self, samplesdir, datadir, filename, ffs):
        """Test instance creation from XML file."""
        file = datadir / filename
        parser = XmlParser(context=XmlContext())
        if ffs == "FFS1":
            predicted_orbit_file = parser.parse(file, mpl_orbpre.EEPredictedOrbitFileFFS1)
            assert isinstance(predicted_orbit_file, mpl_orbpre.EEPredictedOrbitFileFFS1)
        elif ffs == "FFS2":
            predicted_orbit_file = parser.parse(file, mpl_orbpre.EEPredictedOrbitFile)
            assert isinstance(predicted_orbit_file, mpl_orbpre.EEPredictedOrbitFile)
        else:
            predicted_orbit_file = parser.parse(file, mpl_orbpre.EOPredictedOrbitFile)
            assert isinstance(predicted_orbit_file, mpl_orbpre.EOPredictedOrbitFile)
        serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))
        nsmap = {None: basic.__NAMESPACE__}
        samplesdir.write(serializer.render(predicted_orbit_file, nsmap), filename)
