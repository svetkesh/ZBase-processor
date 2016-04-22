#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  stage 0.2-1
#  
#  Copyright 2016 kesha <kesha@c2037>
# test_ext_procedure_for_db_021

import sys
#import time
#import sqlite3
print ('running ',sys.argv)

from test_db_object_021 import *

def get_license_ID_from_db_021(base_db_name):
	print ('get_license_ID_from_db_021 runing with arg=',base_db_name)
	
	# try to create db connection
	try:
		#pass
		print ('try to create db connection base_db = zab_base_dat(zab_base_dat)')
		base_db = zab_base_dat(base_db_name)
		#print ('----')
		#print ('base_db', base_db , '\n','type(base_db)' , type(base_db))
		#print ('----')
		
		#print (base_db.print()) this is bad cause yet not implemented print()
		base_db.do_external_sql_querry('SELECT value FROM settings WHERE id = 1')
		print(base_db.do_external_sql_querry('SELECT value FROM settings WHERE id = 1'))
		#print (base_db.do_external_sql_querry('SELECT value FROM settings WHERE id = 1'))
		
	except:
		print ('connection to db was not successfull')
	
	#base_db.do_external_sql_querry('some OTHER text as fake querry') # unmask error
	#base_db.do_external_sql_querry('SELECT value FROM settings WHERE id = 1') # unmask error


# local test run 
#get_license_ID_from_db_021('base.dat') # good
	

