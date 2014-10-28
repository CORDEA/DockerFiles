#!/usr/bin/env python
# encoding:utf-8
#
#
#
__Author__  =  "CORDEA"
__date__    =  "2014-10-28"
__version__ =  "0.1.0 (Beta)"

import os
from optparse import OptionParser

def optSettings():
    usage   = "%prog [-ioce] [options] [-s] [file]\nDetailed options -h or --help"
    version = __version__
    parser  = OptionParser(usage=usage, version=version)

    parser.add_option(
            '-u', '--user',
            action  = 'store',
            type    = 'str',
            dest    = 'user',
            # user nameのデフォルト値
            default = 'huge',
            )

    parser.add_option(
            '-n', '--name',
            action  = 'store',
            type    = 'str',
            dest    = 'name',
            # container nameのデフォルト値
            default = 'hoge',
            )

    parser.add_option(
            '-w', '--work',
            action  = 'store',
            type    = 'str',
            dest    = 'work_dir',
            # working directoryのデフォルト値
            default = '/home/huge',
            )

    return parser.parse_args()

def main():
    options, args = optSettings()
    user_op = '-u '     + str(options.user)     + ' '
    name_op = '--name ' + str(options.name)     + ' '
    work_op = '-w '     + str(options.work_dir) + ' '
    oth_op  = ''
    for op in args:
        oth_op += str(op) + ' '

    # -itオプションが不要な場合ここを編集して下さい。
    os.system('docker run -it ' + user_op + work_op + name_op + oth_op)

if __name__ == '__main__':
    main()
