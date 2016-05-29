#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  stage 0.2
#  
#  Copyright 2016 kesha <kesha@c2037>

# about dynamc_proc ...
# may be dynamic adding modules could be realized
# with walking through folder
# but this coul be ponetially dangerous
# with corrupted or poisoned modules
# placed into folder

import sys
#import time
print ('running ',sys.argv)

# list_of_good_modules
list_of_good_modules = ['test_command_checker02',
'sample_proc_checker',
'sample_proc',
'test_ext_procedure_for_db_021',
'get_license_ID_from_db_021',
'clear_all_events_021',
]

#dict_of_good_modules = {'test_command_checker02':('sample_proc_checker',)}

#class dynamc_proc (object) :
	#def __init__(self , ext_proc) :
		###self.ext_proc = ext_proc # is not allowed ip Python
		##try :
			##from argument import *
			##print ('no error raised load and ckeck proc=', self.ext_proc )
			##return True
		##except:
			##print ('error while loading and ckecking proc=', self.ext_proc )
			##return False	
			

#def sample_proc_checker(module_name):
	#print ('sample_proc_checker runing with arg=',module_name)
	##print ('try to load and ckeck proc=', argument )
	##try :
		##from argument import *
		##print ('no error raised load and ckeck proc=', argument )
		##return True
	##except:
		##print ('error while loading and ckecking proc=', argument )
		##return False	
	#return False

def module_in_list_checker(module_name):
	#print ('module_in_list_checker runing with arg=',module_name)
	if module_name in list_of_good_modules :
		#print ('module_in_list_checker found listed as enabled module =',module_name)
		return True
	else :
		#print ('module_in_list_checker found as NOT enabled module =',module_name)
		return False
	return False
	
def multi_reply_module_checker(module_name):
	#print ('multi_reply_module_checker runing with arg=',module_name)
	if module_name in list_of_good_modules :
		#print ('multi_reply_module_checker found in list of good module =',module_name)
		return True , 200
	else :
		#print ('multi_reply_module_checker did not found as enabled module =',module_name)
		return False , 501
	return False , 500

