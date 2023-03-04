"""Test the `eopfiles.aux_orbres` module."""
import pytest

from eopfiles import basic, aux_orbres, get_parser, get_serializer


class TestRestitutedOrbitFile:
    """
    Test the `EERestitutedOrbitFileFFS1`, `EERestitutedOrbitFile` and
    `EERestitutedOrbitFile` classes.
    """

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
        parser = get_parser()
        if ffs == "FFS1":
            restituted_orbit_file = parser.parse(file, aux_orbres.EERestitutedOrbitFileFFS1)
            assert isinstance(restituted_orbit_file, aux_orbres.EERestitutedOrbitFileFFS1)
        elif ffs == "FFS2":
            restituted_orbit_file = parser.parse(file, aux_orbres.EERestitutedOrbitFile)
            assert isinstance(restituted_orbit_file, aux_orbres.EERestitutedOrbitFile)
        else:
            restituted_orbit_file = parser.parse(file, aux_orbres.EORestitutedOrbitFile)
            assert isinstance(restituted_orbit_file, aux_orbres.EORestitutedOrbitFile)
        serializer = get_serializer()
        nsmap = {None: basic.__NAMESPACE__}
        samplesdir.write(serializer.render(restituted_orbit_file, nsmap), filename)


class TestOrbitStateVectorFileFile:
    """
    Test the `EEOrbitStateVectorFileFFS1`, `EEOrbitStateVectorFile` and
    `EOOrbitStateVectorFile` classes.
    """

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
        parser = get_parser()
        if ffs == "FFS1":
            restituted_orbit_file = parser.parse(file, aux_orbres.EEOrbitStateVectorFileFFS1)
            assert isinstance(restituted_orbit_file, aux_orbres.EEOrbitStateVectorFileFFS1)
        elif ffs == "FFS2":
            restituted_orbit_file = parser.parse(file, aux_orbres.EEOrbitStateVectorFile)
            assert isinstance(restituted_orbit_file, aux_orbres.EEOrbitStateVectorFile)
        else:
            restituted_orbit_file = parser.parse(file, aux_orbres.EOOrbitStateVectorFile)
            assert isinstance(restituted_orbit_file, aux_orbres.EOOrbitStateVectorFile)
        serializer = get_serializer()
        nsmap = {None: basic.__NAMESPACE__}
        samplesdir.write(serializer.render(restituted_orbit_file, nsmap), filename)
