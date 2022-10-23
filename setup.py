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

from setuptools import setup

setup(
    version='0.5',
    name='srtgen',
    description='TODO',
    packages=('srtgen',),
    keywords='TODO',
    author="Salvo 'LtWorf' Tomaselli",
    author_email='tiposchi@tiscali.it',
    maintainer="Salvo 'LtWorf' Tomaselli",
    maintainer_email='tiposchi@tiscali.it',
    url='https://github.com/ltworf/srtgen',
    license='AGPL3',
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    entry_points={
        'console_scripts': [
            'srtgen = srtgen:main',
        ]
    }
)
