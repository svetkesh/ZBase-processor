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

This adds client with given name , ip 
and ID is counted as current max(of IDs) +1

sql string looks like ...

This from real DB

delete from computerToGroupLink (check 780 records > -> 260 )

select t.computer_id from computerToGroupLink t where t.computer_id IN
( select y.id
--, y.name, y.ip, y.deleted , y.app_version, y.base_version, y.product_type  
from computer y  where  y.deleted != 0  or y.app_version=NULL  or y.app_version=''  or y.base_version=NULL  or y.product_type=0 )
>>520 rec ... 520 IDs with problems


delete from computerToGroupLink where computer_id IN
( select y.id
--, y.name, y.ip, y.deleted , y.app_version, y.base_version, y.product_type  
from computer y  where  y.deleted != 0  or y.app_version=NULL  or y.app_version=''  or y.base_version=NULL  or y.product_type=0 )




delete from computer_license (check 123 > 114)

select id from computer_license where id IN
( select y.id
--, y.name, y.ip, y.deleted , y.app_version, y.base_version, y.product_type  
from computer y  where  y.deleted != 0  or y.app_version=NULL  or y.app_version=''  or y.base_version=NULL  or y.product_type=0 )
>> 9 records


delete from history (check 10015 > 9535)

select computer_id from history where computer_id IN
( select y.id
--, y.name, y.ip, y.deleted , y.app_version, y.base_version, y.product_type  
from computer y  where  y.deleted != 0  or y.app_version=NULL  or y.app_version=''  or y.base_version=NULL  or y.product_type=0 )
>>480 records

delete from history where computer_id IN
( select y.id
--, y.name, y.ip, y.deleted , y.app_version, y.base_version, y.product_type  
from computer y  where  y.deleted != 0  or y.app_version=NULL  or y.app_version=''  or y.base_version=NULL  or y.product_type=0 )



delete from threat_log_new (check 4898119 > 4860261)

select client_id from threat_log_new where client_id  --=5
--select client_id from threat_log_new where client_id !=5
IN
( select y.id
-- --, y.name, y.ip, y.deleted , y.app_version, y.base_version, y.product_type  
from computer y  where  y.deleted != 0  or y.app_version=NULL  or y.app_version=''  or y.base_version=NULL  or y.product_type=0 )
order by client_id 
>>37858 


delete from computer (check 783 > 256)

--( 
select id
-- --, y.name, y.ip, y.deleted , y.app_version, y.base_version, y.product_type  
from computer  where  deleted != 0  or app_version=NULL  or app_version=''  or base_version=NULL  or product_type=0
-- )
>>527'''

import sys
#import time
#import sqlite3
print ('running ',sys.argv)

from test_db_object_021 import *

def repair_db(base_db_name, client_name,client_ip):
	print ('add_client_021 runing with arg=',base_db_name, ' client_name' , client_name, 'client_ip', client_ip)
	
	# try to create db connection
	try:
		#pass
		print ('try to create db connection base_db = zab_base_dat(zab_base_dat)')
		base_db = zab_base_dat(base_db_name)
		#print ('----')
		#print ('base_db', base_db , '\n','type(base_db)' , type(base_db))
		#print ('----')
		
		# no more ugly typing :)
		# from table computerToGroupLink delete problematic Clients IDs
		querry_string = "delete from computerToGroupLink where computer_id IN ( select y.id from computer y  where  y.deleted != 0  or y.app_version=NULL  or y.app_version=''  or y.base_version=NULL  or y.product_type=0 )"
		#
		#print (base_db.print())                                                  # this is bad cause yet not implemented print() 
		#base_db.do_external_sql_querry(querry_string)                            #  each could lead to run query
		#print(base_db.do_external_sql_querry(querry_string))                     #  so debug it with caution
		#print (base_db.do_external_sql_querry(querry_string))                    #  if you dont want to get
		#                                                                         #  dublicated or even triple :0
        #                                                                         #  results ... like delete
        # from table computer_license delete problematic Clients IDs
        querry_string = "DELETE from computer_license where id IN ( select y.id from computer y where y.deleted != 0  or y.app_version=NULL  or y.app_version='' or y.base_version=NULL or y.product_type=0)"
		#
        #
        base_db.do_external_sql_querry(querry_string)
        
        # from table history delete problematic Clients IDs
        querry_string = "delete from history where computer_id IN ( select y.id from computer y  where  y.deleted != 0  or y.app_version=NULL  or y.app_version=''  or y.base_version=NULL  or y.product_type=0 )"
        base_db.do_external_sql_querry(querry_string)
        # from table threat_log_new delete problematic Clients IDs
        querry_string = "DELETE from threat_log_new where client_id IN ( select y.id from computer y  where  y.deleted != 0  or y.app_version=NULL  or y.app_version=''  or y.base_version=NULL  or y.product_type=0 )"
        base_db.do_external_sql_querry(querry_string)
        # last in DELETE row
        # from table computer delete problematic Clients IDs
        querry_string = "from computer  where  deleted != 0  or app_version=NULL  or app_version=''  or base_version=NULL  or product_type=0"
        base_db.do_external_sql_querry(querry_string)
        # updating sequences - computer
        querry_string = 'update sqlite_sequence set seq = ( select count (*) from computer ) where name = "computer" '
        base_db.do_external_sql_querry(querry_string)
        # updating sequences - history
        querry_string = 'update sqlite_sequence set seq = ( select count (*) from history ) where name = "history"'
		return base_db.do_external_sql_querry(querry_string)                      
		# return 'Some data and Some success code' # Next round for
		
		##                                                               # here should be placed stat_refresh > refresh made here with updating
		
	except:
		print ('connection to db was not successfull or not all proc works as exprcted')
		# return 'Some error code' # Next round for
		return False
	
	#base_db.do_external_sql_querry('some OTHER text as fake querry') # unmask error
	#base_db.do_external_sql_querry('SELECT value FROM settings WHERE id = 1') # unmask error


# local test run 
repair_db('base.dat') # ? local
