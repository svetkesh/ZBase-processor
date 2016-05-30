#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  stage 0.2-1
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
or False if error raised.'''

import sys
#import time
#import sqlite3
print ('running ',sys.argv)

from test_db_object_021 import *

def clear_all_passwords(base_db_name):
	print ('clear_all_passwords_021 runing with arg=',base_db_name)
	
	# try to create db connection
	try:
		#pass
		print ('try to create db connection base_db = zab_base_dat(zab_base_dat)')
		base_db = zab_base_dat(base_db_name)
		#print ('----')
		#print ('base_db', base_db , '\n','type(base_db)' , type(base_db))
		#print ('----')
		
		# no more ugly typing :)
		querry_string = 'update settings set value =NULL where id=2 or id=3 or id =4 or id=5 or id=6 or id=7'
		
		#print (base_db.print()) this is bad cause yet not implemented print()
		base_db.do_external_sql_querry(querry_string)
		print(base_db.do_external_sql_querry(querry_string))
		#print (base_db.do_external_sql_querry(querry_string))
		return base_db.do_external_sql_querry(querry_string)
		# return 'Some data and Some success code' # Next round for
	except:
		print ('connection to db was not successfull')
		# return 'Some error code' # Next round for
		return False
	
	#base_db.do_external_sql_querry('some OTHER text as fake querry') # unmask error
	#base_db.do_external_sql_querry('SELECT value FROM settings WHERE id = 1') # unmask error


# local test run 
#get_license_ID_from_db_021('base.dat') # good
