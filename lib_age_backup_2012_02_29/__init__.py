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

import sys, functools, argparse
from .safe_print import safe_print as print

DEFAULT_AGE_SIZE = 10
DEFAULT_AGE_COUNT = 7

class UserError(Exception):
    pass

def user_error_showing(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except UserError as e:
            print('user error: {}'.format(e), file=sys.stderr)
    
    return wrapper

def show_user_error(s):
    raise UserError(s)

def get_backup_group_list(backup_path):
    pass # TODO: ...

def do_backup_copy(source_path, backup_path):
    pass # TODO: ...

def do_age_action(backup_path, backup_list, age_count, is_extra=None):
    if is_extra is None:
        is_extra = False
    
    pass # TODO: ...

def age_backup(source_path, backup_path,
        age_size=None, age_count=None):
    if age_size is None:
        age_size = DEFAULT_AGE_SIZE
    if age_count is None:
        age_count = DEFAULT_AGE_COUNT
    
    # stage 1: get current backup-groups status, and remember it
    backup_group_list = get_backup_group_list(backup_path)
    
    # stage 2: do fresh backup copy
    do_backup_copy(source_path, backup_path)
    
    # stage 3: do actions for changing backup-groups status
    for age, backup_list in enumerate(backup_group_list):
        if age < age_count:
            is_extra = False
        else:
            is_extra = True
        
        do_age_action(backup_path, backup_list, age_size, is_extra=is_extra)

@user_error_showing
def main():
    parser = argparse.ArgumentParser(
        description='utility for periodical creating new '
                '(and removing outdated) backup copies')
    
    parser.add_argument('source_path', metavar='SOURCE-PATH',
            help='path to source directory')
    parser.add_argument('backup_path', metavar='BACKUP-PATH',
            help='path to destination backup directory')
    parser.add_argument('age_size', metavar='AGE-SIZE',
            type=int, nargs='?',
            help='how much backup-copies of one age. default is {}'.format(
            DEFAULT_AGE_SIZE))
    parser.add_argument('age_count', metavar='AGE-COUNT',
            type=int, nargs='?',
            help='how much ages. default is {}'.format(
            DEFAULT_AGE_COUNT))
    
    args = parser.parse_args()
    
    if args.age_size is not None and args.age_size < 1:
        show_user_error('invalid age size')
    
    if args.age_count is not None and args.age_count < 1:
        show_user_error('invalid age count')
    
    age_backup(
            args.source_path,
            args.backup_path,
            age_size=args.age_size,
            age_count=args.age_count,
            )
