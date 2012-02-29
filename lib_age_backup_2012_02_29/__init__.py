# -*- mode: python; coding: utf-8 -*-
#
# Copyright 2012 Andrej A Antonov <polymorphm@gmail.com>.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

assert str is not bytes

import argparse
from .safe_print import safe_print as print

DEFAULT_AGE_SIZE = 10
DEFAULT_AGE_COUNT = 7

class UserError(Exception):
    pass

def main():
    parser = argparse.ArgumentParser(
        description='utility for periodical creating new '
                '(and removing outdated) backup copies')
    
    parser.add_argument('source',
            help='source directory')
    parser.add_argument('backup',
            help='destination backup directory')
    parser.add_argument('age-size', type=int, nargs='?',
            help='how much backup-copies of one age. default is {}'.format(
            DEFAULT_AGE_SIZE))
    parser.add_argument('age-count', type=int, nargs='?',
            help='how much ages. default is {}'.format(
            DEFAULT_AGE_COUNT))
    
    args = parser.parse_args()
    
    # TODO: ...
