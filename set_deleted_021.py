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
or False if error raised.
Set computer with given computer_id "deleted".
Marks computer with ID "computer_id" as deleted from serv list.
Actualy do 
--update computer set deleted =1 where id=computer_id'''

import sys
#import time
#import sqlite3
print ('running ',sys.argv)

from test_db_object_021 import *

def set_deleted(base_db_name, computer_id):
	print ('clear_all_passwords_021 runing with arg=',base_db_name)
	
	# try to create db connection
	try:
		#print ('computer_id' , computer_id)
		#print ('type of computer_id' , type(computer_id))
		
		#pass
		print ('try to create db connection base_db = zab_base_dat(zab_base_dat)')
		base_db = zab_base_dat(base_db_name)
		#print ('----')
		#print ('base_db', base_db , '\n','type(base_db)' , type(base_db))
		#print ('----')
		
		# no more ugly typing :)
		querry_string = 'update computer set deleted =1 where id='+str(computer_id)
		
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
#set_deleted('base.dat',132) # 
#try :
	#set_deleted('base.dat',1) # 
#except :
	#print ('some erroe w proc call')

