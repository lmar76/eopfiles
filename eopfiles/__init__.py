from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from . import (
    aux_orbres,
    basic,
    headers,
    mpl_orbpre,
    times
)


context = XmlContext()
parser = XmlParser(context=context)
serializer = XmlSerializer(context=context, config=SerializerConfig(pretty_print=True))

__all__ = [
    "aux_orbres",
    "basic",
    "headers",
    "mpl_orbpre",
    "parser",
    "serializer",
    "times"
]

__version__ = "0.1"
