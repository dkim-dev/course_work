#!/usr/bin/env python3

import os
import sys
import types
total_mark = 0
bonus_mark = 0
ID = input('Please enter your Seneca ID: ')
path = ('./ur_'+ID+'.py')

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def read_file_list_split(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    f = open(file_name).read().split()
    list_res = []
    for item in f:
        list_res.append(item.strip())
    return list_res

def read_file_list_split_n(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    f = open(file_name).read().split('\n')
    list_res = []
    for item in f:
        list_res.append(item.strip())
    return list_res

if __name__ == '__main__':
    if not os.path.isfile(path):
        print('=' * 70)
        print('Your A2 script file',path,'is not in the current direcoty')
        print('Please copy this script to the directory that contains your')
        print('A2 script file and run the this test run script again.')
        print('=' * 70)
        sys.exit()

    if not os.path.isfile("checking_script_repo/ur_answer.py"):
        cmd_file = 'git clone https://github.com/dkim151-seneca/checking_script_repo/'
        os.system(cmd_file)
    cmod = 'chmod 777 checking_script_repo -R'
    os.system(cmod)
    answer_file = 'checking_script_repo/ur_answer.py'     
#answer_1   
    answer_1 = os.popen(answer_file+' -h').read()
    answer_1 = answer_1.split()
    answer_1 = answer_1[2:98]
#answer_2
    answer_2 = os.popen(answer_file+' -l user usage_data_file').read()
    answer_2 = answer_2.split("\n")
    answer_2 = answer_2[2:]    
#answer_3
    answer_3 = os.popen(answer_file+' -l host usage_data_file').read()
    answer_3 = answer_3.split("\n")
    answer_3 = answer_3[2:]
    
#answer_4
    answer_4 = os.popen(answer_file+' -u rchan -t daily usage_data_file').read()
    answer_4 = answer_4.split()
    answer_4 = answer_4[10:]
#answer_5
    answer_5 = os.popen(answer_file+' -u cwsmith -t daily usage_data_file').read()
    answer_5 = answer_5.split()
    answer_5 = answer_5[10:]
#answer_6
    answer_6 = os.popen(answer_file+' -r 10.40.105.130 -t daily usage_data_file').read()
    answer_6 = answer_6.split()
    answer_6 = answer_6[10:]
#answer_7
    answer_7 = os.popen(answer_file+' -u rchan -t weekly usage_data_file').read()
    answer_7 = answer_7.split()
    answer_7 = answer_7[11:]
#answer_8
    answer_8 = os.popen(answer_file+' -u cwsmith -t weekly usage_data_file').read()
    answer_8 = answer_8.split()
    answer_8 = answer_8[11:]
#answer_9
    answer_9 = os.popen(answer_file+' -r 10.40.105.130 -t weekly usage_data_file').read()
    answer_9 = answer_9.split()
    answer_9 = answer_9[11:]
#answer_10
    answer_10 = os.popen(answer_file+' -l user last').read()
    answer_10 = answer_10.split()
    answer_10 = answer_10[5:]


#Test1
    test_01 = os.popen(path+' -h').read()
    test_01 = test_01.split()
    test_01 = test_01[2:98]
    resultatus = set(answer_1) & set(test_01)
    if resultatus == set(answer_1):
	    print('TEST 1 '+path+' -h', color.GREEN,'\t\t\t\t\t\tPASSED',color.END)
	    total_mark = total_mark + 1
    else:
	    print("TEST 1 "+path+" -h", color.RED," \t\t\t\t\t\tFAILED",color.END)
	    test_01 = os.popen(path+' -h').read()
	    print(test_01)

#Test2


    test_02 = os.popen(path+' -l user usage_data_file').read()
    test_02 = test_02.split("\n")
    test_02 = test_02[2:]
    if set(test_02) == set(answer_2):
	    total_mark = total_mark + 1
	    print('TEST 2 '+path+' -l user usage_data_file', color.GREEN,'\t\t\tPASSED',color.END)
    else:
	    print("TEST 2 "+path+" -l user usage_data_file",color.RED," \t\t\tFAILED",color.END)
	    test_02 = os.popen(path+' -l user usage_data_file').read()
	    print(test_02)

#test_03

    test_03 = os.popen(path+' -l host usage_data_file').read()
    test_03 = test_03.split("\n")
    test_03 = test_03[2:]
    if set(test_03) == set(answer_3):
        total_mark = total_mark + 1
        print('TEST 3 '+path+' -l host usage_data_file', color.GREEN,'\t\t\tPASSED',color.END)
    else:
	    print("TEST 3 "+path+" -l host usage_data_file", color.RED," \t\t\tFAILED",color.END)
	    test_03 = os.popen(path+' -l host usage_data_file').read()
	    print(test_03)
	     
#test_04

    test_04 = os.popen(path+' -u rchan -t daily usage_data_file').read()
    test_04 = test_04.split()
    test_04 = test_04[10:]
    if set(test_04) == set(answer_4):
	    total_mark = total_mark + 1
	    print('TEST 4 '+path+' -u rchan -t daily usage_data_file', color.GREEN,'\t\tPASSED',color.END)
    else:
	    print("TEST 4 "+path+" -u rchan -t daily usage_data_file", color.RED,"\t\tFAILED",color.END)
	    test_04 = os.popen(path+' -u rchan -t daily usage_data_file').read()
	    print(test_04)

#test_05

    test_05 = os.popen(path+' -u cwsmith -t daily usage_data_file').read()
    test_05 = test_05.split()
    test_05 = test_05[10:]
    if set(test_05) == set(answer_5):
	    total_mark = total_mark + 1
	    print('TEST 5 '+path+' -u cwsmith -t daily usage_data_file', color.GREEN,'\t\tPASSED',color.END)
    else:
	    print("TEST 5 "+path+" -u cwsmith -t daily usage_data_file",color.RED,"\t\tFAILED",color.END)
	    test_05 = os.popen(path+' -u cwsmith -t daily usage_data_file').read()
	    print(test_05)

#test_06

    test_06 = os.popen(path+' -r 10.40.105.130 -t daily usage_data_file').read()
    test_06 = test_06.split()
    test_06 = test_06[10:]
    if set(test_06) == set(answer_6):
	    total_mark = total_mark + 1
	    print('TEST 6 '+path+' -r 10.40.105.130 -t daily usage_data_file', color.GREEN,'\tPASSED',color.END)
    else:
	    print("TEST 6 "+path+" -r 10.40.105.130 -t daily usage_data_file", color.RED,"\tFAILED",color.END)
	    test_06 = os.popen(path+' -r 10.40.105.130 -t daily usage_data_file').read()
	    print(test_06)

#test_07

    test_07 = os.popen(path+' -u rchan -t weekly usage_data_file').read()
    test_07 = test_07.split()
    test_07 = test_07[11:]
    if set(test_07) == set(answer_7):
	    total_mark = total_mark + 1
	    print('TEST 7 '+path+' -u rchan -t weekly usage_data_file', color.GREEN,'\t\tPASSED',color.END)
    else:
	    print('TEST 7 '+path+' -u rchan -t weekly usage_data_file', color.RED,'\t\tFAILED',color.END)
	    test_07 = os.popen(path+' -u rchan -t weekly usage_data_file').read()
	    print(test_07)
	    
#test_08

    test_08 = os.popen(path+' -u cwsmith -t weekly usage_data_file').read()
    test_08 = test_08.split()
    test_08 = test_08[11:]
    if set(test_08) == set(answer_8):
	    total_mark = total_mark + 1
	    print('TEST 8 '+path+' -u cwsmith -t weekly usage_data_file', color.GREEN,'\t\tPASSED',color.END)
    else:
	    print('TEST 8 '+path+' -u cwsmith -t weekly usage_data_file', color.RED,'\t\tFAILED',color.END)
	    test_08 = os.popen(path+' -u cwsmith -t weekly usage_data_file').read()
	    print(test_08)
	    
#test_09

    test_09 = os.popen(path+' -r 10.40.105.130 -t weekly usage_data_file').read()
    test_09 = test_09.split()
    test_09 = test_09[11:]
    if set(test_09) == set(answer_9):
	    total_mark = total_mark + 1
	    print('TEST 9 '+path+' -r 10.40.105.130 -t weekly usage_data_file', color.GREEN,'\tPASSED',color.END)
    else:
	    print('TEST 9 '+path+' -r 10.40.105.130 -t weekly usage_data_file', color.RED,'\tFAILED',color.END)
	    test_09 = os.popen(path+' -r 10.40.105.130 -t weekly usage_data_file').read()
	    print(test_09)
#test_10
    print()
    print(color.GREEN,'Bonus test:',color.END)
    test_10 = os.popen(path+' -l user last').read()
    test_10 = test_10.split()
    test_10 = test_10[5:]    
    print()
    if set(test_10) == set(answer_10):
	    bonus_mark = bonus_mark + 1
	    print(' BONUS TEST '+path+' -l user last', color.GREEN,'\tPASSED',color.END)
    else:
	    print(' BONUS TEST '+path+' -l user last', color.RED,'\tFAILED',color.END)   
    print()

total_mark = ('Total Marks: '+str((total_mark/9)*100))
os.system("rm -rf checking_script_repo")
print()
print(color.GREEN,total_mark,color.END)
if bonus_mark == 1:
	print(color.GREEN,'Bonus Mark:  '+str(bonus_mark),color.END)
else:
	print(color.RED,'Bonus Mark:  '+str(bonus_mark),color.END)
print()
