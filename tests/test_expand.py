
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

import unittest
from metl.config import Config
from metl.configparser import ConfigParser
from metl.manager import Manager
from metl.field import Field
from metl.fieldset import FieldSet
from metl.fieldmap import FieldMap
from metl.fieldtype.stringfieldtype import StringFieldType
from metl.fieldtype.integerfieldtype import IntegerFieldType
from metl.expand.appendbysourceexpand import AppendBySourceExpand
from metl.expand.appendexpand import AppendExpand
from metl.source.staticsource import StaticSource
from metl.source.csvsource import CSVSource

class Test_Expand( unittest.TestCase ):

    def setUp( self ):

        self.reader = StaticSource(
            FieldSet([
                Field( 'name', StringFieldType() ),
                Field( 'email', StringFieldType() )
            ],
            FieldMap({
                'name': 0,
                'email': 1
            }))
        )
        self.reader.setResource([
            [ 'Ochala Wild', 'Ochala Wild@metl-test-data.com' ],
            [ 'Sina Venomous', 'Sina Venomous@metl-test-data.com' ],
            [ 'Akassa Savage Phalloz', 'Akassa Savage Phalloz@metl-test-data.com' ],
            [ 'Sermak Bad', 'Sermak Bad@metl-test-data.com' ],
            [ 'Olivia Deadly Dawod', 'Olivia Deadly Dawod@metl-test-data.com' ],
            [ 'Pendus Inhuman', 'Pendus Inhuman@metl-test-data.com' ],
            [ 'Naria Cold-blodded Greste', 'Naria Cold-blodded Greste@metl-test-data.com' ],
            [ 'Shard Brutal', 'Shard Brutal@metl-test-data.com' ],
            [ 'Sina Cruel', 'Sina Cruel@metl-test-data.com' ],
            [ 'Deadly Ohmar', 'Deadly Ohmar@metl-test-data.com' ],
            [ 'Mylenedriz Cold-blodded', 'Mylenedriz Cold-blodded@metl-test-data.com' ],
            [ 'Calden Frigid', 'Calden Frigid@metl-test-data.com' ],
            [ 'Acid Reaper', 'Acid Reaper@metl-test-data.com' ],
            [ 'Raven Seth', 'Raven Seth@metl-test-data.com' ],
            [ 'Rivatha Todal', 'Rivatha Todal@metl-test-data.com' ],
            [ 'Panic Oliviaezit', 'Panic Oliviaezit@metl-test-data.com' ],
            [ 'Tomara Wild', 'Tomara Wild@metl-test-data.com' ],
            [ 'Venessa Metalhead', 'Venessa Metalhead@metl-test-data.com' ]
        ])

    def test_append_by_source( self ):

        static_source = StaticSource(
            FieldSet([
                Field( 'name', StringFieldType() ),
                Field( 'email', StringFieldType() ),
                Field( 'year', IntegerFieldType() )
            ], 
            FieldMap({
                'name': 0,
                'email': 1,
                'year': 2
            }))
        )
        static_source.setResource([
            [ 'El Agent', 'El Agent@metl-test-data.com', 2008 ],
            [ 'Serious Electron', 'Serious Electron@metl-test-data.com', 2008 ],
            [ 'Brave Wizard', 'Brave Wizard@metl-test-data.com', 2008 ],
            [ 'Forgotten Itchy Emperor', 'Forgotten Itchy Emperor@metl-test-data.com', 2008 ],
            [ 'The Moving Monkey', 'The Moving Monkey@metl-test-data.com', 2008 ],
            [ 'Evil Ghostly Brigadier', 'Evil Ghostly Brigadier@metl-test-data.com', 2008 ],
            [ 'Strangely Oyster', 'Strangely Oyster@metl-test-data.com', 2008 ],
            [ 'Anaconda Silver', 'Anaconda Silver@metl-test-data.com', 2006 ],
            [ 'Hawk Tough', 'Hawk Tough@metl-test-data.com', 2004 ],
            [ 'The Disappointed Craw', 'The Disappointed Craw@metl-test-data.com', 2008 ],
            [ 'The Raven', 'The Raven@metl-test-data.com', 1999 ],
            [ 'Ruby Boomerang', 'Ruby Boomerang@metl-test-data.com', 2008 ],
            [ 'Skunk Tough', 'Skunk Tough@metl-test-data.com', 2010 ],
            [ 'The Nervous Forgotten Major', 'The Nervous Forgotten Major@metl-test-data.com', 2008 ],
            [ 'Bursting Furious Puppet', 'Bursting Furious Puppet@metl-test-data.com', 2011 ],
            [ 'Neptune Eagle', 'Neptune Eagle@metl-test-data.com', 2011 ],
            [ 'The Skunk', 'The Skunk@metl-test-data.com', 2008 ],
            [ 'Lone Demon', 'Lone Demon@metl-test-data.com', 2008 ],
            [ 'The Skunk', 'The Skunk@metl-test-data.com', 1999 ],
            [ 'Gamma Serious Spear', 'Gamma Serious Spear@metl-test-data.com', 2008 ],
            [ 'Sleepy Dirty Sergeant', 'Sleepy Dirty Sergeant@metl-test-data.com', 2008 ],
            [ 'Red Monkey', 'Red Monkey@metl-test-data.com', 2008 ],
            [ 'Striking Tiger', 'Striking Tiger@metl-test-data.com', 2005 ],
            [ 'Sliding Demon', 'Sliding Demon@metl-test-data.com', 2011 ],
            [ 'Lone Commander', 'Lone Commander@metl-test-data.com', 2008 ],
            [ 'Dragon Insane', 'Dragon Insane@metl-test-data.com', 2013 ],
            [ 'Demon Skilled', 'Demon Skilled@metl-test-data.com', 2011 ],
            [ 'Vulture Lucky', 'Vulture Lucky@metl-test-data.com', 2003 ],
            [ 'The Ranger', 'The Ranger@metl-test-data.com', 2013 ],
            [ 'Morbid Snake', 'Morbid Snake@metl-test-data.com', 2011 ],
            [ 'Dancing Skeleton', 'Dancing Skeleton@metl-test-data.com', 2001 ],
            [ 'The Psycho', 'The Psycho@metl-test-data.com', 2005 ],
            [ 'Jupiter Rider', 'Jupiter Rider@metl-test-data.com', 2011 ],
            [ 'Green Dog', 'Green Dog@metl-test-data.com', 2011 ],
            [ 'Brutal Wild Colonel', 'Brutal Wild Colonel@metl-test-data.com', 2008 ],
            [ 'Random Leader', 'Random Leader@metl-test-data.com', 2008 ],
            [ 'Pluto Brigadier', 'Pluto Brigadier@metl-test-data.com', 2008 ],
            [ 'Southern Kangaroo', 'Southern Kangaroo@metl-test-data.com', 2008 ],
            [ 'Serious Flea', 'Serious Flea@metl-test-data.com', 2001 ],
            [ 'Nocturnal Raven', 'Nocturnal Raven@metl-test-data.com', 2008 ],
            [ 'Risky Flea', 'Risky Flea@metl-test-data.com', 2005 ],
            [ 'The Corporal', 'The Corporal@metl-test-data.com', 2013 ],
            [ 'The Lucky Barbarian', 'The Lucky Barbarian@metl-test-data.com', 2008 ],
            [ 'Rocky Serious Dog', 'Rocky Serious Dog@metl-test-data.com', 2008 ],
            [ 'The Frozen Guardian', 'The Frozen Guardian@metl-test-data.com', 2008 ],
            [ 'Freaky Frostbite', 'Freaky Frostbite@metl-test-data.com', 2008 ],
            [ 'The Tired Raven', 'The Tired Raven@metl-test-data.com', 2008 ],
            [ 'Disappointed Frostbite', 'Disappointed Frostbite@metl-test-data.com', 2008 ],
            [ 'The Craw', 'The Craw@metl-test-data.com', 2003 ],
            [ 'Gutsy Strangely Chief', 'Gutsy Strangely Chief@metl-test-data.com', 2008 ],
            [ 'Queen Angry', 'Queen Angry@metl-test-data.com', 2008 ],
            [ 'Pluto Albatross', 'Pluto Albatross@metl-test-data.com', 2003 ],
            [ 'Endless Invader', 'Endless Invader@metl-test-data.com', 2003 ],
            [ 'Beta Young Sergeant', 'Beta Young Sergeant@metl-test-data.com', 2008 ],
            [ 'The Demon', 'The Demon@metl-test-data.com', 2003 ],
            [ 'Lone Monkey', 'Lone Monkey@metl-test-data.com', 2011 ],
            [ 'Bursting Electron', 'Bursting Electron@metl-test-data.com', 2003 ],
            [ 'Gangster Solid', 'Gangster Solid@metl-test-data.com', 2005 ],
            [ 'The Gladiator', 'The Gladiator@metl-test-data.com', 2001 ],
            [ 'Flash Frostbite', 'Flash Frostbite@metl-test-data.com', 2005 ],
            [ 'The Rainbow Pluto Demon', 'The Rainbow Pluto Demon@metl-test-data.com', 2011 ],
            [ 'Poseidon Rider', 'Poseidon Rider@metl-test-data.com', 2008 ],
            [ 'The Old Alpha Brigadier', 'The Old Alpha Brigadier@metl-test-data.com', 2008 ],
            [ 'Rough Anaconda', 'Rough Anaconda@metl-test-data.com', 2001 ],
            [ 'Tough Dinosaur', 'Tough Dinosaur@metl-test-data.com', 2011 ],
            [ 'The Lost Dinosaur', 'The Lost Dinosaur@metl-test-data.com', 2008 ],
            [ 'The Raven', 'The Raven@metl-test-data.com', 2005 ],
            [ 'The Agent', 'The Agent@metl-test-data.com', 2011 ],
            [ 'Brave Scarecrow', 'Brave Scarecrow@metl-test-data.com', 2008 ],
            [ 'Flash Skeleton', 'Flash Skeleton@metl-test-data.com', 2008 ],
            [ 'The Admiral', 'The Admiral@metl-test-data.com', 1998 ],
            [ 'The Tombstone', 'The Tombstone@metl-test-data.com', 2013 ],
            [ 'Golden Arrow', 'Golden Arrow@metl-test-data.com', 2008 ],
            [ 'White Guardian', 'White Guardian@metl-test-data.com', 2011 ],
            [ 'The Black Eastern Power', 'The Black Eastern Power@metl-test-data.com', 2008 ],
            [ 'Ruthless Soldier', 'Ruthless Soldier@metl-test-data.com', 2008 ],
            [ 'Dirty Clown', 'Dirty Clown@metl-test-data.com', 2008 ],
            [ 'Alpha Admiral', 'Alpha Admiral@metl-test-data.com', 2008 ],
            [ 'Lightning Major', 'Lightning Major@metl-test-data.com', 2008 ],
            [ 'The Rock Demon', 'The Rock Demon@metl-test-data.com', 2008 ],
            [ 'Wild Tiger', 'Wild Tiger@metl-test-data.com', 2008 ],
            [ 'The Pointless Bandit', 'The Pointless Bandit@metl-test-data.com', 2008 ],
            [ 'The Sergeant', 'The Sergeant@metl-test-data.com', 1998 ],
            [ 'Western Ogre', 'Western Ogre@metl-test-data.com', 1998 ],
            [ 'Sergeant Strawberry', 'Sergeant Strawberry@metl-test-data.com', 2008 ]
        ])

        expand  = AppendBySourceExpand( self.reader, static_source ).initialize()
        records = [ r for r in expand.getRecords() ]

        self.assertEqual( len( records ), 103 )
        self.assertEqual( len( records[0].getFieldNames() ), 2 )
        self.assertEqual( records[-1].getField('name').getValue(), 'Sergeant Strawberry' )

    def test_append( self ):

        source = CSVSource( FieldSet(
            fields = [
                Field( 'NUMBERS', StringFieldType() )
            ],
            fieldmap = FieldMap({
                'NUMBERS': 0
            })
        ) )
        source.setResource('tests/test_sources/test_csv_append.csv')
        expand = AppendExpand( source, 'tests/test_sources/test_csv_appended.csv' )
        expand.initialize()
        records = [ r for r in expand.getRecords() ]
        expand.finalize()

        self.assertEqual( len( records ), 6 )
        self.assertEqual( records[0].getField('NUMBERS').getValue(), 'First' )
        self.assertEqual( records[-1].getField('NUMBERS').getValue(), 'Sixth' )

if __name__ == '__main__':
    unittest.main()