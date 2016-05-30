#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  stage 02 -1
#  
#  Copyright 2016 kesha <kesha@c2037>
# stage 02 -1 added inter... faces for sql command

import sys
#import time
import sqlite3
print ('running ',sys.argv)

class zab_base_dat :
	#print ("hello I'm zab_base_dat object") # it's good 
	#~ pass
	def __init__(self,file_name):
		self.file_name = file_name
		self.is_zab_db = self.check_basic_open_db_file()
		#is_zab_db = check_basic_open_db_file(self)
			
			#try :
				##			
				#db_conn = sqlite3.connect(self.file_name)
				#db_curs = db_conn.cursor()
				##db_curs.execute('SELECT value FROM settings WHERE id = 1')
				##actual_data = db_curs.fetchall()
			#return db_curs
			

			#except :
				##
				#print ('db closed in by except')
				#db_conn.close()
			#finally :
				##
				#print ('db closed in finally')
				#db_conn.close()
			

	def print_db_name(self):
		print (self.file_name)
				
	def open_db_file(self):
		#
		try:
			try:
				db_file = self.file_name
			except:
				print ('could not open file file_name ' , self.file_name)			
			else:
				db_conn = sqlite3.connect(db_file)	
				db_curs = db_conn.cursor()
				db_curs.execute('SELECT value FROM settings WHERE id = 1')
				actual_data = db_curs.fetchall()
				db_conn.close()
				return actual_data
		except:
			print ('some error happens while opening and reading data file file_name' , self.file_name)
		return "nothing to return yet"
		
	def check_basic_open_db_file(self):
		'''Check if given file could be ZAB database
		
		This checks given file could be probably ZAB database
		Checks against filename exists, file could be opened,
		file is database and ZAB code present;
		did not yet suggest filename -> filename.ext
		did not yet workaround with licence broken.
		'''
		try:
			try:
				#print ('check file file_name ' , self.file_name) # it's good 
				if len(self.file_name) <4 :
					print ('too short read file file_name ' , self.file_name)
					# here could be suggester be added
					return False    				
				else :
					#print ('good file file_name ' , self.file_name) # it's good 
					#print ('check could be opened file_name ' , self.file_name) # it's good 
					try :
						#pass #
						file_handler=open(self.file_name)
						file_handler.close()
						#print ('file exists and could be opened file_name ' , self.file_name) # it's good 						
						#return True
						# next check ...
						#print ('check could be opened as databse file_name ' , self.file_name) # it's good 
						try :
							#pass
							db_conn = sqlite3.connect(self.file_name)
							db_curs = db_conn.cursor()
							db_curs.execute('SELECT value FROM settings WHERE id = 1')
							actual_data = db_curs.fetchall()
							db_conn.close()
							#print ('could be open as databse file_name ' , self.file_name)	# it's good 						
							#print ('sample data from databse  licence ID' , actual_data[0][0])
							#print ('sample data from databse  licence ID' , len(str(actual_data[0][0])[::-1]))
							if len ( str(actual_data[0][0]) ) == 19 :
								#print ('looks like ZAB database licence ID' , str(actual_data[0][0])[:4],'XXXX XXX XXXX',str(actual_data[0][0])[-4:]) # it's good 
								print ('ZAB database connected OK to file ' , self.file_name)
								return True
							else :
								print ('may be not a ZAB database or ID corrupted ? ', str(actual_data[0][0])[::-1] )
								return False 
							return True
							# next check ...
						except:
							print ('could not open as databse file_name ' , self.file_name)
							return False 
						
					except:
						print ('could not open file_name ' , self.file_name)
						return False 
					#return True
					# next check ...
				
			except:
				print ('could not read file file_name ' , self.file_name)
				return False
		except:
			print ('some error happens while opening and reading data file file_name' , self.file_name)
			return False


		

	
	def function_multi_param (self, command = '', *command_keys, **command_pairs ):
		''' This functions accepts and try to perform multi arg command.
		
		
		This functions accepts and try to perform multi arg command.
		It is test func .'''
		#pass
		try : # try to accept command
			print ('checking given command ', str(command))
			if command == '' :			
				print('command empty>',command,'<')
				return False
			elif command != '':
				if len(command) > 0 :
					# here next check should be
					#checking *command_keys and **command_pairs
					print ('--') 
					print ('got this command_keys',command_keys)
					for command_key in command_keys:
						print (command_key,)
					print ('--') 
					print ('got this command_pairs',command_pairs)
					for command_pair in command_pairs :
						print (command_pair,command_pairs[command_pair])
					print ()
					print('accepted command >',command,'<', 'lenght', len(command))
					return False
			else:
				print('accepted command >',command,'<','lenght is strange', len(command))
				return False
		except :
			print ('error accepting command' , command)
			return False

	def do_external_sql_querry(self, sql_querry):
		# some
		print ('try to perform sql_querry' , sql_querry)
		db_conn = sqlite3.connect(self.file_name)
		db_curs = db_conn.cursor()
		db_curs.execute(sql_querry) # here sql_querry insert
		actual_data = db_curs.fetchall()
		# coomit it need to test previous defs -test ok
		db_conn.commit() # :) thanks to dreamincode.net/forums/topic/210154-sqlite3-in-python/ and google
		db_curs.close() #
		db_conn.close()
		return actual_data
		

