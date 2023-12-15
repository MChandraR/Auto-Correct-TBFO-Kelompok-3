import os
import time

node = {
    "q0" :{
        "a" : ["q1","a","R"],
        "b" : ["q2","b","R"],
        "k" : ["q11","k","R"],
        "s" : ["q19","s","R"],
        "y" : ["q25","y","R"],
        "e" : ["q5","e","R"],
        "c" : ["q3","c","R"],
        "m" : ["q13","m","R"],
        "t" : ["q20","t","R"]
    },
    "q1":{
        "a" : ["q1","a","R"],
        "c" : ["q3","c","R"],
        "e" : ["q5","e","R"],
        "r" : ["q18","r","R"],
        "b" : ["q2","b","R"],
        "a" : ["q1","p","R"],
        "o" : ["q1","p","R"],
        "k" : ["q11","k","R"],
        "l" : ["q4","p","R"],
        "m" : ["q13","m","R"],
        "n" : ["q14","n","R"],
        "y" : ["q25","y","R"],
        "s": ["q19","s","R"],
        "p": ["q16","p","R"],
        "l" : ["q12","l","R"],
        "t": ["q20","t","R"]
    },
    "q31":{
        "k" : ["q11","k","R"],
        "a" : ["q1","a","R"],
        "l" : ["q12","l","R"],
        "m" : ["q43","m","R"]
    },
    "q2":{
        "a" : ["q1","a","R"],
        "o" : ["q1","a","R"],
        "i" : ["q2","a","R"]
    },
    "q3":{
        "a" : ["q1","a","R"],
        "b" : ["q15","o","L"],
        "o" : ["q15","o","R"],
        "n" : ["q1","a","L"],
        "p" : ["q5","e","L"],
        "e" : ["q5","e","R"]
    },
    "q4":{
        "a" : ["q1","a","R"]
    },
    "q5":{
        "e" : ["q5","e","R"],
        "s" : ["q19","s","R"],
        "n" : ["q14","n","R"],
        "o" : ["q1","a","R"],
        "p" : ["q16","p","R"],
        "k" : ["q11","k","R"]
    },
    "q7":{
        "o" : ["q1","a","R"]
    },
    "q9":{
        "d" : ["q1","d","R"]
    },
    "q11":{
        "e" : ["q5","e","R"],
        "a" : ["q1","a","R"],
        "m" : ["q1","a","L"],
        "i" : ["q12","i","R"],
        "n" : ["q5","e","L"],
        "s" : ["q19","s","R"],
        "r" : ["q1","a","L"]
    },
    "q12":{
        "e" : ["q5","e","R"],
        "a" : ["q1","a","R"],
        "o" : ["q1","a","R"],
        "i" : ["q1","a","R"],
        "n" : ["q14","n","R"],
        "k" : ["q11","k","R"]
    },
    "q13":{
       
        "k" : ["q31","a","L"],
        "l" : ["q31","a","L"],
        "a" : ["q21","u","R"],
        "u" : ["q21","u","R"],
        "a" : ["q1","a","R"],
        "o" : ["q21","u","R"],
    },
    "q43":{
        "a" : ["q1","a","R"]
    },
    "q14":{
        "a" : ["q1","a","R"],
        "g" : ["q7","g","R"],
        "t" : ["q20","t","R"],
        "k" : ["q7","g","R"]
    },
    "q15":{
        "b" : ["q2","b","R"],
        "c" : ["q3","c","R"],
        "o" : ["q15","o","R"]
    },
    "q16":{
        "p" : ["q1","a","R"],
        "o" : ["q1","a","R"],
        "a" : ["q1","a","R"]
    },
    "q18":{
        "a" : ["q1","a","R"]
    },
    "q19":{
        "a" : ["q1","a","R"],
        "e" : ["q5","e","R"],
        "k" : ["q5","e","L"],
        "o" : ["q12","i","R"],
        "i" : ["q12","i","R"],
        "p" : ["q5","e","L"],
        "y" : ["q1","a","L"]
    },
    "q20":{
        "d" : ["q9","i","L"],
        "n" : ["q1","a","L"],
        "i" : ["q12","i","R"]
    },
    "q21":{
        "u" : ["q21","u","R"]
    },
    "q25":{
        "k" : ["q1","a","L"],
        "i" : ["q1","a","R"],
        "o" : ["q1","a","R"],
        "a" : ["q1","a","R"]
    },
    "q4":{
        "a" : ["q1","a","R"],
        "u" : ["q1","a","R"],
        "o" : ["q1","a","R"]
    },
    "q6":{
        "b" : ["q2","b","R"]
    }
}
    

def getFinalState(key):
    return "q" + str(ord(key)-96)

def turing(input_str):
  
    tape = list(input_str)
    head_pos = 0
    final = getFinalState(tape[len(tape)-1])
    state = "q0"
    result = []
    move = ""
    state_temp = state
    nextS = ""
    inp = tape[head_pos]
    
    while state!=final or head_pos<len(tape) :
        #print(head_pos, len(tape)-1)
        if head_pos >= (len(tape)-1) :
            break
        temp = tape[head_pos]
        move = "R"
        if tape[head_pos] in node[state]:
            inp = tape[head_pos]
            move = node[state][tape[head_pos]][2]
            nextS = node[state][tape[head_pos]][0]
            state_temp = state
            if move == 'L':
                tape = tape[:head_pos] + tape[head_pos:head_pos+1] + tape[head_pos:]
                result.append((( "𝛿("+state_temp+", "+inp+") = "+ nextS +" | "+temp +" => "+tape[head_pos] + " | move : " + move),"".join(tape),move))
            tape[head_pos] = node[state][tape[head_pos]][1]
            state = node[state][temp][0]
            #print(state,":",temp ,"->",tape[head_pos])
            result.append((( "𝛿("+state_temp+", "+inp+") = "+ nextS +" | "+temp +" => "+tape[head_pos] + " | move : " + move),"".join(tape),move))
            #print(tape)
            head_pos+= 1 if move == "R" else -1
        else:
            result.append((( "𝛿("+state_temp+", "+inp+") = Halt | "+inp+ " => "+inp+ " | move : - " ),"".join(tape),move))
            hasil = ''.join(tape)
            return hasil,result

        
        
        
        
    result.append((( "𝛿("+state_temp+", "+inp+") = "+ nextS +" | "+tape[len(tape)-1] + " => "+tape[len(tape)-1]+ " | move : " + move),"".join(tape),move))
    hasil = ''.join(tape)
    return hasil,result

# print(getFinalState('a'))
# input_string = "halo apa kabir ? sya siaoa siala ykin ykan ?"
# print(input_string)
# input_string = input_string.split(" ")
# kata_terkoreksi = ""
# for kata in input_string :
#     if kata != ",":
#         kata_terkoreksi += turing(kata) + " "
# print(kata_terkoreksi)
