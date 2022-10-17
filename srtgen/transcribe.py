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
from typing import NamedTuple, Iterator

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


def _format_timestamp(timestamp: float) -> str:
    '''
    Format a seconds timestamp into the srt format
    '''
    millis = int(timestamp - int(timestamp)) * 1000
    itimestamp = int(timestamp)

    seconds = int(itimestamp % 60)
    minutes = int(itimestamp // 60) % 60
    hours = int(itimestamp // 3600)

    return f'{hours:02}:{minutes:02}:{seconds:02},{millis:03}'


def srt_data(data: TranscribedText) -> Iterator[str]:
    for c, i in enumerate(data.segments):
        yield f'{c * 100}\n'
        yield f'{_format_timestamp(i.start)} --> {_format_timestamp(i.end)}\n'
        yield i.text.strip()
        yield '\n\n'
