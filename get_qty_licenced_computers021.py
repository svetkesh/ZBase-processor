#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  stage 0.2-1
#  
#  Copyright 2016 kesha <kesha@c2037>
# get_qty_licenced_computers021.py

'''Return quantity of all computers.

This proc counts all records in 'computer' table
and returns either number ether False.'''

import sys
#import time
#import sqlite3
print ('running with get_qty_licenced_computers021.py',sys.argv)

from test_db_object_021 import *

def get_qty_licenced_computers(base_db_name): 
	'''
	Count licenced computers.
	
	
	This count computers wich has acvive
	 and valid licences.'''
	print ('get_qty_licenced_computers runing runnng with DB',base_db_name)
	
	# try to create db connection
	try:
		#pass
		base_db = zab_base_dat(base_db_name)		
		base_db.do_external_sql_querry('SELECT COUNT (*) FROM computer')
		print(base_db.do_external_sql_querry('SELECT COUNT (*) FROM computer'))
		#print (base_db.do_external_sql_querry('SELECT value FROM settings WHERE id = 1'))
		return base_db.do_external_sql_querry('SELECT COUNT (*) FROM computer')[0][0]
	except:
		print ('connection to db was not successfull')
		return False
	
	#base_db.do_external_sql_querry('some OTHER text as fake querry') # unmask error
	#base_db.do_external_sql_querry('SELECT value FROM settings WHERE id = 1') # unmask error


# local test run 
#get_license_ID_from_db_021('base.dat') # good
	

