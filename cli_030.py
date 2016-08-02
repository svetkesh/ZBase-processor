#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  stage 0.3-0
#  
#  Copyright 2016 kesha <kesha@c2037>
# template_ext_procedure_for_db_021

# it's template for procedures
#
# importting db_object (for this ver is test_db_object_021)
# for zab_base_dat object 
# .do_external_sql_querry procedure is called
# and  db_object.function_multi_param('')
# returns somethig expected or error
#

'''This is proc template.

This proc creates instance of zab_base_dat
forms some querry 
call this querry with .do_external_sql_querry 
then perform sql querry analisys and may be parse
then returns result # and success code <-- later
                    # next step
                    # and error code
or False if error raised.

This adds client with given name , ip 
and ID is counted as current max(of IDs) +1

sql string looks like
INSERT INTO computer ('id' , 'name','ip')
 VALUES (
 (SELECT max(id) FROM computer)+1 ,
  'bbb',
  '10.10.0.2')'''

import sys
#import time
#import sqlite3
print ('running ',sys.argv)

#from test_db_object_021 import *

class cli_030 :
	def __init__(self):
		pass
		# user
		# working file
		# command
		# state
		# output
		# history
		# end state



# local test run 

