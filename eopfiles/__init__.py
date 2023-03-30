__all__ = [
    "aux_orbres",
    "basic",
    "exceptions",
    "get_parser",
    "get_serializer",
    "headers",
    "mpl_orbpre",
    "times",
]
__version__ = "0.6"

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from . import (
    aux_orbres,
    basic,
    exceptions,
    headers,
    mpl_orbpre,
    times
)


def get_parser() -> XmlParser:
    """Get `XmlParser` instance.

    Returns
    ----------
    xsdata.formats.dataclass.parsers.XmlParser
        XML parser.

    """
    return XmlParser(context=XmlContext())


def get_serializer(pretty_print: bool = True) -> XmlSerializer:
    """Get `XmlSerializer` instance.

    Returns
    -------
    xsdata.formats.dataclass.serializers.XmlSerializer
        XML serializer.

    """
    return XmlSerializer(config=SerializerConfig(pretty_print=pretty_print))
