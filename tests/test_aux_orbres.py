"""Test the `eopfiles.aux_orbres` module."""
import pytest
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from eopfiles import basic, aux_orbres


class TestEERestitutedOrbitFile:
    """Test the `EERestitutedOrbitFile` class."""

    @pytest.mark.parametrize(
        "filename, ffs",
        [
            (
                "CS_TEST_AUX_ORBRES_20100616T175926_20100616T180826_0007.EEF",
                "FFS1"
            ),
            (
                "S1A_TEST_AUX_ORBRES_20140611T105116_20140611T110016_0004.EOF",
                "FFS2"
            ),
            (
                "MA1_TEST_AUX_ORBRES_20210610T050853_20210610T051753_0001.EOF",
                "FFS3"
            ),
        ]
    )
    def test_from_file(self, samplesdir, datadir, filename, ffs):
        """Test instance creation from XML file."""
        file = datadir / filename
        parser = XmlParser(context=XmlContext())
        if ffs == "FFS1":
            restituted_orbit_file = parser.parse(file, aux_orbres.EERestitutedOrbitFileFFS1)
            assert isinstance(restituted_orbit_file, aux_orbres.EERestitutedOrbitFileFFS1)
        elif ffs == "FFS2":
            restituted_orbit_file = parser.parse(file, aux_orbres.EERestitutedOrbitFile)
            assert isinstance(restituted_orbit_file, aux_orbres.EERestitutedOrbitFile)
        else:
            restituted_orbit_file = parser.parse(file, aux_orbres.EORestitutedOrbitFile)
            assert isinstance(restituted_orbit_file, aux_orbres.EORestitutedOrbitFile)
        serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))
        nsmap = {None: basic.__NAMESPACE__}
        samplesdir.write(serializer.render(restituted_orbit_file, nsmap), filename)
