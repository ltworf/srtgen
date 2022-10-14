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
from pathlib import Path

from . import transcribe

def main() -> None:
    fname = Path(sys.argv[1])
    language = sys.argv[2]

    data = transcribe.transcribe_file(fname, language)

    destfile = Path(sys.argv[1][:-4] + '.srt')
    with destfile.open('wt') as f:
        for line in transcribe.srt_data(data):
            f.write(line)

if __name__ == '__main__':
    main()

