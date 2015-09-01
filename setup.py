#!/usr/bin/env python
# -*- coding: utf-8 -*-
### BEGIN LICENSE
# Copyright (C) 2010 Mads Chr. Olesen <mchro@cs.aau.dk>
#This program is free software: you can redistribute it and/or modify it 
#under the terms of the GNU General Public License version 3, as published 
#by the Free Software Foundation.
#
#This program is distributed in the hope that it will be useful, but 
#WITHOUT ANY WARRANTY; without even the implied warranties of 
#MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR 
#PURPOSE.  See the GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License along 
#with this program.  If not, see <http://www.gnu.org/licenses/>.
### END LICENSE

###################### DO NOT TOUCH THIS (HEAD TO THE SECOND PART) ######################

try:
    import DistUtilsExtra.auto
except ImportError:
    import sys
    print >> sys.stderr, 'To build pyuppaal you need https://launchpad.net/python-distutils-extra'
    sys.exit(1)

assert DistUtilsExtra.auto.__version__ >= '2.10', 'needs DistUtilsExtra.auto >= 2.10'
import os

        
##################################################################################
###################### YOU SHOULD MODIFY ONLY WHAT IS BELOW ######################
##################################################################################

from distutils.command.install_lib import install_lib
#command to build parser tables after installation
class install_lib_build_parser_tables(install_lib):
    def run(self):
        # Call parent 
        install_lib.run(self)
        # Execute commands
        #import pdb; pdb.set_trace()

        print "Would build parser tables"
        self.execute(self.build_tables, [])

    def build_tables(self):
        prevdir = os.path.abspath(os.curdir)
        try:
            os.chdir(os.path.join(self.install_dir, 'pyuppaal', 'ulp'))

            print "Building parser tables"
            os.system("python _build_tables.py")
        finally:
            os.chdir(prevdir)

DistUtilsExtra.auto.setup(
    name='pyuppaal',
    version='0.4',
    license='GPL-3',
    author='Mads Chr. Olesen',
    author_email='mchro@cs.aau.dk',
    description='Python library for manipulating UPPAAL xml files',
    #long_description='Here a longer description',
    url='https://launchpad.net/pyuppaal',
    cmdclass={"install_data": install_lib_build_parser_tables},
    )

