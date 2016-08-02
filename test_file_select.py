#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  stage 0.3-0
#  
#  Copyright 2016 kesha <kesha@c2037>
# based on template_ext_procedure_for_db_021

#

'''Selects database file and turn it into work.

This is proc is for testing purposses to check 
which metod will be comfortable to select DB file 
then return it for work'''

#test_file_select
#https://www.ibm.com/developerworks/ru/library/l-python_part_8/

import sys, os, time
#import time
#import sqlite3
from test_db_object_021 import*

#warm-up
#print ('running ',sys.argv)
#print ('os.listdir() :')
#print ('--------------------------------')
#print ('current directory is :', os.getcwd())
#print ('')
#print ('--------------------------------')
#print ('list all directory :', os.listdir())
#print ('')
#print ('--------------------------------')
def walk(dir):
  for name in os.listdir(dir):
    path = os.path.join(dir, name)
    if os.path.isfile(path):
        print (path)
    else:
        walk(path)
        
def check_for_zabsbase_present_here(dir):
	for sysobject in os.listdir(dir) :
		fullpath = os.path.join(dir, sysobject)
		#print (fullpath , 'isfile :' , os.path.isfile(fullpath))
		if os.path.isfile(fullpath) :
			if fullpath.split('.')[-1] == 'dat' :
				print ('Found .dat file %s in directory %s' % (sysobject, dir))
				
def quick_check_for_zabsbase_present_here(dir):
	'''Check for zabs bases present in dir and list them.
	 '''
	count_any_dat_files = 0
	count_zabs_dat_files = 0
	list_zabs_dat_files = []
	for filename in os.listdir(dir) :
		if filename.split('.')[-1] == 'dat' :
			fullpath = os.path.join(dir, filename)
			if os.path.isfile(fullpath) :
				count_any_dat_files += 1
				#now check as zabs db file or not
				#test_db_object_021
				#print ('check_basic_open_db_file for ', filename , 'is' ,zab_base_dat(fullpath).check_basic_open_db_file())  #qiet please
				if zab_base_dat(fullpath).check_basic_open_db_file() :
					count_zabs_dat_files += 1
					list_zabs_dat_files.append(filename)
	print ('In directory \n %s \n found count_any_dat_files = %d \n       count_zabs_dat_files = %d' % (dir, count_any_dat_files, count_zabs_dat_files))
	if count_zabs_dat_files > 0 :
		return [True , list_zabs_dat_files]
	else:
		return [False]

def navigate():
	'''Navigate and select working folder and zabs database.
	'''
	#
	#try ...
	#
	folder_is_selected = False
	folder_selected = os.getcwd()
	list_of_subfolders = []
	file_is_selected = False
	file_selected = ''
	file_selected_ind = 0
	while not folder_is_selected :
		#print ('--------------------------------')
		#print ('Hint for zabs files present here')
		#quick_check_for_zabsbase_present_here(folder_selected)
		#print hint list of subfolders
		list_of_subfolders = []
		for sysobject in os.listdir(folder_selected) :
			fullpath = os.path.join(folder_selected, sysobject)
			#print (fullpath , 'isfile :' , os.path.isfile(fullpath))
			if os.path.isdir(fullpath) :
				#print ('%s' % sysobject , end = ' ') #no more nessecary
				list_of_subfolders.append(sysobject)
		#print ('len (list_of_subfolders)',len (list_of_subfolders)) #DBG
		if len (list_of_subfolders) > 0 :
			print ('Subfolders here are :' , end = ' ')
			for subfolder in list_of_subfolders :
				print (subfolder , end = ' ; ')
		else :
			print ('No subfolders here in %s' % folder_selected, end = ' ')
					
		#
		print ()
		print ('Type ".." - level up ; "q" to quit ; ENTER to select')
		answer_typed = input ('Path is %s%s' % (folder_selected, os.sep))
		#
		print ('--------------------------------')
		if answer_typed == '':
			quick_check_for_zabsbase_present_here(folder_selected)
			answer_typed = input ('Press ENTER to confirm this folder selected')
			if answer_typed == '' :
				folder_is_selected = True
		elif answer_typed == '..':
			folder_selected = os.path.split(folder_selected)[0]
			#print('os.path.split(folder_selected)[0] set to %s' % os.path.split(folder_selected)[0]) #DBG
			#print('folder_selected now became upper diectory %s' % folder_selected) #DBG 		
		elif answer_typed == 'q' or answer_typed == 'Q':
			if os.path.isdir(os.path.join(folder_selected, answer_typed)) :
				print ('Sorry found directory name looks like command you\'ve typed')
				print ('Please use ".." or ENTER key at the next step')
				print ('Directory changed to %s' % os.path.join(folder_selected, answer_typed))
				folder_selected = os.path.join(folder_selected, answer_typed)
			else :
				print ('Quit typed directory not changed') 	
				folder_is_selected = True
		else :
			if os.path.isdir(os.path.join(folder_selected, answer_typed)) :
				#print ('check path os.path.join(folder_selected, answer_typed) : %s' % str (os.path.join(folder_selected, answer_typed))) #DBG
				#print ('os.path.isdir is dir %s' % str( os.path.isdir(os.path.join(folder_selected, answer_typed) ) )) #DBG
				folder_selected = os.path.join(folder_selected, answer_typed)
			else :
				print ('Check path : %s' % str (os.path.join(folder_selected, answer_typed))) #DBG
				#print ('Not a valid directory name os.path.isdir is dir %s' % str( os.path.isdir(os.path.join(folder_selected, answer_typed) ) )) #DBG				
				similiar_subfolders = 0				
				for subfolder in list_of_subfolders :
					if answer_typed in subfolder :
						similiar_subfolders += 1
						similiar_subfolder = subfolder
				if similiar_subfolders ==0:
					print ('Not a valid directory name %s' % str( os.path.isdir(os.path.join(folder_selected, answer_typed) ) )) #DBG		
				elif similiar_subfolders ==1:
					print ('Guess %s ?' % similiar_subfolder)
					folder_selected = os.path.join(folder_selected, similiar_subfolder)
				else :
					print ('Probably you mean one of :' , end = ' ')
					for subfolder in list_of_subfolders :
						if answer_typed in subfolder :
							print (subfolder , end = ' ; ')
					print ()

		
		#
		#print ('You typed %s' %answer_typed)
		#print ('check whether folder_selected if folder')                                     #DBG
		#print ('os.path.isdir(folder_selected) is %s' % str( os.path.isdir(folder_selected) )) #DBG
		#print ('--------------------------------')                                           #DBG
		#print ('check path splitted for folder_selected')                                     #DBG
		#print ('os.path.split(folder_selected) is %s' % str( os.path.split(folder_selected) )) #DBG
		#print ('--------------------------------')                                           #DBG
		#print ('check new path folder_selected %s' % str (os.path.join(folder_selected, answer_typed)))                  #DBG
		#print ('os.path.isdir this path is    %s' % str( os.path.isdir(os.path.join(folder_selected, answer_typed) ) )) #DBG
		#print ('--------------------------------')                                                                     #DBG
		#folder_selected
		#
	print ('--------------------------------')  
	print ('Selected folder is %s' %folder_selected)
	#print ('Hint for zabs files present here')
	quick_check_for_zabsbase_present_here(folder_selected)
	
	#File .dat zabs database selection
	#warm up ...

	
	if quick_check_for_zabsbase_present_here(folder_selected)[0]:
		#quiet please
		bool_zabsbase_present_here = quick_check_for_zabsbase_present_here(folder_selected)[0]
		list_databases = quick_check_for_zabsbase_present_here(folder_selected)[1]		
		
		print ('----datafiles here = ',len(list_databases))
		if len(list_databases) == 1 :
			file_selected = list_databases[0]
		elif len(list_databases) > 1 :
			for item in list_databases :
				print ( list_databases.index(item) , ' --' , item)
			while not file_is_selected :
				try :
					file_selected_ind = int (input ('Select file by index please'))
					#print ('--------------------------------')
					#print (file_selected_ind)
					#print (list_databases[file_selected_ind])
					#print (str(list_databases[file_selected_ind]))
					#print ('--------------------------------')
					
					file_selected = str(list_databases[file_selected_ind])
					print ('You selected ',file_selected)
					file_is_selected = True
				except:
					print ('File not selected')
					answer_typed = input ('Try again? or "q" to quit ')
					if answer_typed == 'q' or answer_typed == 'Q' :
						print ('File not selected now')
						break
		
	 
	
	#
	#except ...
	#	
	return [True , folder_selected, file_selected]

def bark():
	print ('Bark')
	

#walk(os.getcwd())
#print ('')
#print ('--------------------------------')
#print ('Setting working directory with ZABS database')
#print ('')
#print ('--------------------------------')
##set_as_wdir = input ('Set current directory as working directory ? YN \n %s \n'  %os.getcwd()) 
##print ('You answered', set_as_wdir)
##print ('check path_isfile')
#print ('--------------------------------')
##quick_check_for_zabsbase_present_here(os.getcwd())
print ('')
print ('--------------------------------')

#navigate()
print (navigate())

