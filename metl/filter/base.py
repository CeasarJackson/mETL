
# -*- coding: utf-8 -*-

"""
mETLapp is a Python tool for do ETL processes with easy config.
Copyright (C) 2013, Bence Faludi (b.faludi@mito.hu)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, <see http://www.gnu.org/licenses/>.
"""

import metl.manipulation, demjson

class Filter( metl.manipulation.Manipulation ):

    # bool
    def isFiltered( self, record ):

    	raise RuntimeError( 'Filter.isFiltered() function is not implemented yet.' ) 

    # list<FieldSet>
    def getRecords( self ):

        for record in self.getReader().getRecords():
            if not self.isFiltered( record ):
                yield record

            else:
                self.log( record )