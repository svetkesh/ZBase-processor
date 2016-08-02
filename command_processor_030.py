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

'''This is CLI.

This proc creates instance of command_processor
which orgarize comand line interface with user
Reads input and tries to run it if recognize command.
If command is not recognized tries to find similiar 
command to user's input.
Hint : empty line get list of all commands.
For partially entered command propose numbered list
of fully qualified command. Entering number selects command.
If only one command selectable it is proposed to be selected.
Usial keywords as starting poinst to search commands are 
listed in list_help_keywords[] and are like:
check, list, clear, add, set, get, delete
Later will be extended to 
-compare to the list of command
-run command or 
-return avaliable command similar to the text entered and
-store history'''

import sys
#import time
#import sqlite3
print ('running ',sys.argv)

from test_command_checker02 import *
from get_computers_summary_021 import *

#here should be placed loader for all modules

#from test_db_object_021 import *


list_of_all_items= ['test_command_checker02',
'sample_proc_checker',
'sample_proc',
'test_ext_procedure_for_db_021',
'get_license_ID_from_db_021',
'clear_all_events_021',
'clear_all_passwords_021',
'set_deleted_021',
'add_client_021',
'clear_all_clients_021',
'test',
]
list_help_keywords = ['l',
'L',
'list',
'LIST',
'List',
'LIst',
'h',
'H',
'help',
'Help',
'HElp',
'HELP',
]


class command_processor() :
    def __init__(self, list_of_all_items , list_help_keywords):
        pass
        # user
        # working file
        # command = "" # may be need non-local
        # state
        # output
        # history
        # end state
        self.list_of_all_items = list_of_all_items
        self.list_help_keywords = list_help_keywords
    def talk (self) :
        command = input ('please enter command ')
        print ('you entered' , command)
        # its for check_is_command_warg
        self.command = command 
        
        self.check_in_list()
        #print ('afterburner self.check_in_list()')
        
    def talk_while (self) :
        waiting_for_command = True
        while waiting_for_command :                 
            command = input ('please enter command \'h\' for help or \'q\' to quit ')
            if command == "q" or command == "Q" or command == "Quit" or command == "quit" or command == "QUIT" :
                print ('ok, bye.' , command)
                waiting_for_command = False
                #return True
            else :          
                print ('you entered' , command)
                # its for check_is_command_warg
                self.command = command              
                #self.silent_check_in_list()
                #print ( 'self.silent_check_in_list() <---? ',self.silent_check_in_list() )
                if not self.silent_check_in_list() :  # calling this func permits at least one run of silent_check_in_list()                
                    try :
                        #print ('trying to guess command')
                        self.guess_command()
                        print ('changed self.command after self.guess_command() became ',self.command)      #dbg only tmp
                    except:
                        print ('error while guess command')
                #
                print ('... ready to run this ' , self.command)         #... ready to run this ' , self.command
                self.command_runner(self.command , 'base.dat')
                #return True
        return True
                
    def check_is_command (self , text):
        self.command = text
        print ('you entered before this:' , self.command)
        try :
            #pass
            print ('testing given text to be command' ,self.command)
            print ( module_in_list_checker(self.command)) 
            # return True
        except:
            return False
            
    def check_is_command_warg (self ):                                  #useless
        #check variable self.command
        try :
            #pass
            print ('warg testing given text to be command' ,self.command)
            print ( module_in_list_checker(self.command))
            # return True
        except:
            return False
            
    def check_in_list (self ):

        
        #check variable self.command present in ..some list
        list_of_all_items= ['test_command_checker02',
                            'sample_proc_checker',
                            'sample_proc',
                            'test_ext_procedure_for_db_021',
                            'get_license_ID_from_db_021',
                            'clear_all_events_021',
                            'clear_all_passwords_021',
                            'set_deleted_021',
                            'add_client_021',
                            'clear_all_clients_021',
                            'help',
                            ]
        try :
            #pass
            print ('running check_in_list ...')
            print ('checking against command ' , self.command)
            if self.command in list_of_all_items :
                print ('found item' , self.command)
                #print ( get_computers_summary_021('base.dat') ) # not working
                #print ( get_computers_summary('base.dat') ) # key runner . working . then plug, gag, stopper, peg, bung, stopgap
                #
                try :
                    #pass
                    self.command_runner(self.command)
                except:
                    print ('error calling command_runner(self.command)')
                
                #self.command_runner()
                #command_runner( self.command )
                return True
            else :
                print ('could not find item in list' , self.command)
                next_command = input ('if you want to list items type \'L\' or \'Q\' to quit ')
                print ('you typed' , next_command)
                if next_command == "q" or next_command == "Q" or next_command == "Quit" or next_command == "quit" or next_command == "QUIT" :
                    print ('ok, bye. You typed' , next_command)
                    return False
                elif next_command == "l" or next_command == "L" or next_command == "List" or next_command == "list" or next_command == "LIST" :
                    print (list_of_all_items)
                    print ('See you later. You typed' , next_command)
                    return False
                else :
                    print ('Can not understand, bye!' , next_command)
                    return False                                                    
            # return True
        except:
            return False
            
    # silent_check_in_list silent_check_in_list silent_check_in_list silent_check_in_list silent_check_in_list silent_check_in_list     

    def silent_check_in_list ( self ):
        #
        #check variable self.command present in ..some list
        
        #check given paraneter and exit options     
        #print ('self.command', self.command)
        #return True
        

        try :
            #print ('running silent_check_in_list ...')
            print ('checking against list of available commands ' , self.command)
            if self.command in self.list_help_keywords :
                print ('accepted help-list command')
                for item in self.list_of_all_items :
                    print (item)
                return True                 
            else :
                if self.command in self.list_of_all_items :
                    #
                    print ('known command accepted' , self.command)
                    #try to call run given command      
                    try :
                        self.command_runner(self.command)
                        return True
                    except:
                        print ('error calling command_runner(self.command)')
                        return False                                        
                else :
                    print ('could not recognize command' , self.command)
                    return False
        except :
            print ('error while checking command' , self.command)
            return False
    
    def guess_command (self) :
        #
        try :
            #
            #pass
            list_partial_matches = []
            print ('trying to guess from', self.command)
            for item in self.list_of_all_items :
                #print ('try to compare with',item) 
                if item == self.command:
                    print ('got exact match',item)
                else:
                    #print ('not match')
                    #print ('going to search throught partial match length', len(self.command))    
                    if self.command in item  :
                        print ('got partial match',item)
                        list_partial_matches.append(item)
                    #else :
                        #print ('not match')
            #print ( 'list_partial_matches', list_partial_matches ) 
            #print ( 'len of list_partial_matches', len (list_partial_matches) )  
            
            if len (list_partial_matches) == 0 :
                print ('Can not even guess which command to propose you, sorry. Try again or \'L\' to list available commands')
                return False
            elif len (list_partial_matches) == 1 :
                print ( 'Found the only occurence to guess is', list_partial_matches[0] )
                guess_input_and_accept = input ('Press ENTER to accept or Space to start entering new command ')
                if guess_input_and_accept == "" :
                    self.command = list_partial_matches[0]
                    return True
                else :
                    print ('Seems my wrong guess as you have entered ', guess_input_and_accept)
                    return False
            else :
                index_partial_matches = 0
                print ('Please look through commands similar to what you have typed')
                for partial_match in list_partial_matches :
                    print ( index_partial_matches , partial_match )
                    index_partial_matches += 1
                try :
                    
                    try :
                        input_partial_match = int (input ('Now you have an oppurtunity to select command typing it\'s number ') )
                        #print ('list_partial_matches[input_partial_match]',list_partial_matches[input_partial_match])
                        self.command = list_partial_matches[input_partial_match]
                        #print ('updated self.command', self.command)
                        return True
                    except :
                        print ('Can not accept this selection')
                        return False
                    #print ('You typed input_partial_match', input_partial_match)
                    
                except:
                    print ('Can not accept this selection')
                    return False
        except :
            return False



            

            
    def command_runner (self , command , dat_file):
        #print ('command_runner with ' , self.command)
        #print ( get_computers_summary('base.dat') )
        try:
            #pass
            print ('command_runner with ' , self.command , 'dat_file', dat_file)
            print ( get_computers_summary( dat_file ) )
            return True
        except:
            return False
            
    def test_loader (self , command ):
        try :
            pass
            #get_computers_summary_021('base.dat')
            #from command import *
        except:
            return False
    
    def file_select (self) :
        #select dat file and return it
        pass
        return False
        
        
        



# local test run 
conversation = command_processor(list_of_all_items , list_help_keywords)
#conversation.talk()
conversation.talk_while()

#conversation.check_is_command_warg()
#print (conversation.check_is_command('some text'))
#print (conversation.check_is_command('get_computers_summary_021.py'))
#print ('conversation.check_in_list() is ...',conversation.check_in_list())
#print (conversation.check_is_command('clear_all_clients_021'))
#print ('conversation.check_in_list() is ...',conversation.check_in_list())
#conversation.check_is_command_warg()
#from .. current import *

#print ('--test run--')
#from get_computers_summary_021 import *
#main_out_computers_summary = get_computers_summary_021('base.dat')
#main_out_computers_summary = get_computers_summary('base.dat')
#print ('main_out_p',main_out_computers_summary)
