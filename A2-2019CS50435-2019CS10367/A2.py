import copy
import sys
from operator import itemgetter
import json

import csv

arr = ['M','A','E','R']
array = ['M','E','A','R']
#array1 = ['a','r','e','m']

def transpose(state,n,d):
    temp = []
    for i in range(n):
        empty = []
        for j in range(d):
            empty.append(state[j][i])
        temp.append(empty)
    return temp

def iscomplete(state,n,d):
    for i in range(d):
        for j in range(n):
            if state[i][j] == '':
                return False
    return True

class my_dictionary(dict):
    def __init__(self):
        self = dict()
    def add(self,key,value):
        self[key] = value


def build_dictionary(state,n,d):
    Result_dict = my_dictionary()
    for time in range(n):
        for im in range(d):
            Key = "N" + str(time) +"_" + str(im)
            Value = str(New_List[time][im])
                        #print(Value)
            Result_dict.add(Key,Value)
                        #print(result_dict)
                #print(result_dict) 
    result_list = []
    result_list.append(Result_dict)
    return result_list



    
def unassigned(state,n,d):
    index = [0,0]
    for i in range(d):
        for j in range(n):
            if state[i][j] == '':
                index[0] = i
                index[1] = j
                return index
    return [-1,-1]
   
def a1_solution(n,d,values):
    state =[]
    fle= []
    for j in range(n):
        fle.append('')
    for i in range(d):
        state.append(fle)

    if d>6:
        if 7*values[3] < n:
            return "NO-SOLUTION"
        else:
            rest_weeks = d//7
            #print(rest_weeks)
            for i in range(rest_weeks):
                total_rests = values[3]*7
                start_index = 7*i
                end_index = 0

                if(n%values[3] == 0):
                    end_index = n//values[3] 
                else:
                    end_index = n//values[3] + 1
                end_index += 7*i  
                #print(end_index)
                
                ind = [7*i,n-1]
                
                while total_rests >0 and ind[0] < end_index:
                    #print(end_index)
                    #print(values[3])
                    for timer in range(values[3]):
                        #print(ind[0])
                        empt =[]
                        for count in range(n):
                            if count == ind[1]-timer:
                                empt.append('R')
                            else:
                                empt.append(state[ind[0]][count])
                        #print(empt)
                        state[ind[0]] = empt   
                    #print(state)
                    ind[0] +=1
                    ind[1] -=values[3]
                    total_rests -= values[3]
            
    if n != values[0]+values[1]+values[2]+values[3] or (values[3] ==0 and d>6):
        return "NO-SOLUTION"
    if (2*values[0] > n-values[2]):
        return "NO-SOLUTION"
    send_val = copy.deepcopy(values)
    send_val[3] = 0
    #print(state)
    #print(send_val)
    #print(values)
    return backtrack(state,n,d,values)

def backtrack(state,n,d,values):
    
    #print(node.val_used)
    #print(state)
    
    if iscomplete(state,n,d):
        return state

    unass_index = unassigned(state,n,d)
    #print(state[unass_index[0]])

    usedval = copy.deepcopy(values)
    for time in range(n):
        if state[unass_index[0]][time] != '':
            index = arr.index(state[unass_index[0]][time])
            usedval[index] -= 1
    #print(usedval)
    #print(unass_index)
    #print(unass_index)
    #prev_var = state[unass_index[0]-1][unass_index[1]]

    for i in array:
        if unass_index[0] == 0 or (unass_index[0] > 0 and (state[unass_index[0]-1][unass_index[1]]== 'M' or state[unass_index[0]-1][unass_index[1]] == 'E') and i != 'M') or (unass_index[0] > 0 and state[unass_index[0]-1][unass_index[1]] != 'M' and state[unass_index[0]-1][unass_index[1]]!= 'E'):
            #print(arr.index(i))

            if(usedval[arr.index(i)] > 0):

                new_state = copy.deepcopy(state)
                #new_val = copy.deepcopy(usedval)
                #print(new_state)
                dup_arr = copy.deepcopy(new_state[unass_index[0]])
                empt =[]
                for count in range(n):
                    if count == unass_index[1]:
                        empt.append(i)
                    else:
                        empt.append(dup_arr[count])
                new_state[unass_index[0]] = empt

                result = backtrack(new_state,n,d,values)
                if result != "NO-SOLUTION":
                    return result


    return "NO-SOLUTION"


def a2_solution(n,d,values):
    state = a1_solution(n,d,values)
    if state == "NO-SOLUTION":
        return "NO-SOLUTION"
    transposed = transpose(state,n,d)
    pair = []
    for i in range(n):
        count = 0
        for j in range(d):
            if transposed[i][j] == 'M' or transposed[i][j] == 'E':
                count +=1
        
        pair.append([transposed[i],count])
    New_pair = sorted(pair,key=itemgetter(1),reverse=True)
    #print(New_pair)
    New_list = []
    for node in New_pair:
        New_list.append(node[0])

    return New_list



file_name = sys.argv[1]
if(file_name== "input_a.csv"):
    with open("input_a.csv", 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            n = int(row[0])
            d = int(row[1])
            m = int(row[2])
            a = int(row[3])
            e = int(row[4])
            if n < m+a+e:
                with open("solution.json",'w') as file1:
                    json.dump({},file1)
                    file1.write("\n")
            else:
                values = [m,a,e,n-m-a-e]
                if a1_solution(n,d,values) == "NO-SOLUTION":
                    with open("solution.json",'w') as file1:
                        json.dump({},file1)
                        file1.write("\n")
                else:
                    New_List = transpose(a1_solution(n,d,values),n,d)
                    result_list = build_dictionary(New_List,n,d)
                    #print(result_list)
                    with open("solution.json",'w') as file2:
                        for node in result_list:
                            json.dump(node,file2)
                            file2.write("\n")
if(file_name == "input_b.csv"):
    with open("input_b.csv",'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            n = int(row[0])
            d = int(row[1])
            m = int(row[2])
            a = int(row[3])
            e = int(row[4])
            if n < m+a+e:
                with open("solution.json",'w') as file1:
                    json.dump({},file1)
                    file1.write("\n")
            else:
                values = [m,a,e,n-m-a-e]
                New_List = a2_solution(n,d,values)
                if New_List == "NO-SOLUTION":
                    with open("solution.json",'w') as file1:
                        json.dump({},file1)
                        file1.write("\n")
                else:
                    result_list = build_dictionary(New_List,n,d)
                    #print(result_list)
                    with open("solution.json",'w') as file2:
                        for node in result_list:
                            json.dump(node,file2)
                            file2.write("\n")



    
