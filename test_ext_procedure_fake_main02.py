#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  stage 0.2
#  
#  Copyright 2016 kesha <kesha@c2037>

import sys
#import time
#import sqlite3
print ('running ',sys.argv)

# try from import
#from test_ext_procedure import sample_proc # this 2 lines working good
#sample_proc('aaaaaaaaaaaaaaaaaa')          # :)

# try import
#import test_ext_procedure # this does not work
#sample_proc('bbbbbbb')    # and this


##
## testing 02-1
## check module exists in enabled list
## then run module with param
## return reply as array (True,200) or (False,501)
##

##try import *
#from test_ext_procedure import *    # works fine
#sample_proc('bbbbbbb')              # and this

#from test_command_checker02 import *
#print (module_in_list_checker(''))

##sample_proc and module_in_list_checker
#print ('--')
#print (module_in_list_checker('it is string arg for sample_proc'))
#sample_proc('it is string arg for sample_proc')

##sample_proc and multi_reply_module_checker
#print ('--')
#print (multi_reply_module_checker('sample_proc'))
#print (multi_reply_module_checker('sample_proc'))
#print (multi_reply_module_checker('sample_proc')[0])
#print (multi_reply_module_checker('sample_proc')[1])

#sample_proc('it is string arg for sample_proc')

# before proc called it should be checked against
# enabled list in coomend_checker
#
#if multi_reply_module_checker('sample_proc')[0] :
	#print ('ENABBLED')

##
## testing 02-1 end
##

#
# testing 02-2
# try to create DB object and reform operation
#
#from test_db_object_02 import * # good
#basedat = zab_base_dat('base.dat') # good

from test_command_checker02 import *


#from test_ext_procedure_for_db_021 import *

##print (multi_reply_module_checker('get_license_ID_from_db_021')) # good

## get_qty_licenced_computers #good
#get_license_ID_from_db_021('base.dat')
#print ("from get_qty_licenced_computers021 import *")

##from get_qty_licenced_computers021 import *
#main_out_get_qty_licenced_computers = get_qty_licenced_computers('base.dat')
#print ('main_out_p',main_out_get_qty_licenced_computers)

## get_computers_summary_021 retested  OK
#from get_computers_summary_021 import *
##main_out_computers_summary = get_computers_summary_021('base.dat')
#main_out_computers_summary = get_computers_summary('base.dat')
#print ('main_out_p',main_out_computers_summary)

## clear_all_events_021 retested ok
#from clear_all_events_021 import *
#main_out_clear_all_events_021 = clear_all_events_021('base.dat')
#print ('main_out_p', main_out_clear_all_events_021)

## clear_all_passwords_021 - ok
#from clear_all_passwords_021 import *
#main_out_clear_all_passwords_021 = clear_all_passwords('base.dat')
#print ('main_out_p', main_out_clear_all_passwords_021)

## set_deleted_021 - ok
#from set_deleted_021 import *
#main_out_set_deleted_021 = set_deleted('base.dat',1)
#print ('main_out_set_deleted_021 ', main_out_set_deleted_021)

## add_client_021 - ok
#from add_client_021 import *
#print( add_client('base.dat' , 'ccaa','10.0.0.5'))


## clear_all_clients_021
#from clear_all_clients_021 import *
#print( clear_all_clients('base.dat'))


#
# testing 02-2 end
#




