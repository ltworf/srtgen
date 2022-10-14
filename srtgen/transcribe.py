# srtgen
# Copyright (C) 2022 Salvo "LtWorf" Tomaselli
#
# srtgen is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# author Salvo "LtWorf" Tomaselli <tiposchi@tiscali.it>

from pathlib import Path
from typing import NamedTuple

import whisper
from typedload import load


class Segment(NamedTuple):
    id: int
    seek: int
    start: float
    end: float
    text: str
    tokens: tuple[int, ...]
    temperature: float
    avg_logprob: float
    compression_ratio: float
    no_speech_prob: float


class TranscribedText(NamedTuple):
    text: str
    language: str
    segments: tuple[Segment, ...]


def transcribe_file(filename: Path, language: str) -> TranscribedText:
    model = whisper.load_model('base')
    result = model.transcribe(
        str(filename),
        verbose=True,
        language=language
    )
    return load(result, TranscribedText)
