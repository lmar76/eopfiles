from __future__ import annotations
import os
import pathlib
import shutil
from pathlib import Path
from typing import Optional

import pytest

SAMPLES_BASE = os.getenv("SAMPLES_BASE")


class SamplesDir:

    def __init__(self, basedir: str | os.PathLike, name: str) -> None:
        self._outdir = None if basedir is None else Path(basedir, name)
        if self._outdir:
            shutil.rmtree(self._outdir, ignore_errors=True)
            self._outdir.mkdir(parents=True, exist_ok=True)

    def copy(self, file: str | os.PathLike) -> Optional[pathlib.Path]:
        if self._outdir is None:
            return None
        else:
            _file = Path(file)
            if _file.is_dir():
                dst = self._outdir / _file.name
                shutil.rmtree(dst, ignore_errors=True)
                return shutil.copytree(_file, dst)
            else:
                return shutil.copy2(_file, self._outdir)

    def write(self, text: str, filename: Optional[str] = "output"):
        if self._outdir is None:
            return None
        else:
            _file = self._outdir / filename
            _file.write_text(text)


@pytest.fixture(scope="module")
def samplesdir(request):
    return SamplesDir(SAMPLES_BASE, Path(request.fspath).stem)
