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

import sys
import argparse
from pathlib import Path
from typing import NamedTuple

from typedload import load

from . import transcribe


class Args(NamedTuple):
    language: str
    files: tuple[Path, ...]


def get_args() -> Args:
    '''
    Parse the command line
    '''
    parser = argparse.ArgumentParser(
        prog="srtgen", description="Generate .srt files transcribing the audio using magic"
    )
    parser.add_argument(
        '--language', '-l',
        default='Italian',
        choices=['Italian', 'Swedish', 'English'],
        help="name of the whisper model to use",
    )
    parser.add_argument("files", nargs='+', type=str, help="files to subtitle")
    args = load(parser.parse_args(), Cmdline)


def main() -> None:
    args = get_args()
    for file in args.files
        assert file.exists()
        data = transcribe.transcribe_file(file, args.language)
        with open(str(file)[:-4] + '.srt', 'wt') as f:
            for line in transcribe.srt_data(data):
                f.write(line)


if __name__ == '__main__':
    main()
