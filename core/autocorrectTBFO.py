import os
import time

node = {
    "q0" :{
        "a" : ["q1","a","R"],
        "b" : ["q2","b","R"],
        "d" : ["q4","d","R"],
        "k" : ["q11","k","R"],
        "s" : ["q19","s","R"],
        "y" : ["q25","y","R"],
        "e" : ["q5","e","R"],
        "f" : ["q6","f","R"],
        "c" : ["q3","c","R"],
        "m" : ["q13","m","R"],
        "t" : ["q20","t","R"],
        "g" : ["q9","g","R"],
        "B" : ["q99","B","R"]
    },
    "q1":{
        "a" : ["q1","a","R"],
        "c" : ["q3","c","R"],
        "e" : ["q5","e","R"],
        "r" : ["q18","r","R"],
        "b" : ["q2","b","R"],
        "a" : ["q1","p","R"],
        "h" : ["q8","h","R"],
        "o" : ["q1","p","R"],
        "k" : ["q11","k","R"],
        "l" : ["q4","p","R"],
        "m" : ["q13","m","R"],
        "n" : ["q14","n","R"],
        "y" : ["q25","y","R"],
        "s": ["q19","s","R"],
        "p": ["q16","p","R"],
        "l" : ["q12","l","R"],
        "t": ["q20","t","R"],
        "B" : ["q99","B","R"]
    },
    "q31":{
        "k" : ["q11","k","R"],
        "a" : ["q1","a","R"],
        "l" : ["q12","l","R"],
        "m" : ["q43","m","R"],
        "B" : ["q99","B","R"]
    },
    "q2":{
        "a" : ["q1","a","R"],
        "e" : ["q5","e","R"],
        "r" : ["q5","e","L"],
        "o" : ["q1","a","R"],
        "i" : ["q9","i","R"],
        "B" : ["q99","B","R"]
    },
    "q3":{
        "a" : ["q1","a","R"],
        "b" : ["q15","o","L"],
        "o" : ["q15","o","R"],
        "n" : ["q1","a","L"],
        "p" : ["q5","e","L"],
        "e" : ["q5","e","R"],
        "B" : ["q99","B","R"]
    },
    "q4":{
        "a" : ["q1","a","R"],
        "e" : ["q5","e","R"],
        "i" : ["q9","i","R"],
        "m" : ["q9","i","L"],
        "n" : ["q5","e","L"],
        "r" : ["q18","a","L"],
        "u" : ["q21","u","R"],
        "B" : ["q99","B","R"]
    },
    "q34":{
        "a" : ["q1","a","R"],
        "r" : ["q1","a","L"],
        "o" : ["q21","u","R"],
        "B" : ["q99","B","R"]
    },
    "q5":{
        "b" : ["q2","b","R"],
        "e" : ["q5","e","R"],
        "d" : ["q4","d","R"],
        "m" : ["q43","m","R"],
        "r" : ["q18","r","R"],
        "g" : ["q9","g","R"],
        "s" : ["q19","s","R"],
        "n" : ["q14","n","R"],
        "o" : ["q1","a","R"],
        "p" : ["q16","p","R"],
        "k" : ["q11","k","R"],
        "l" : ["q12","l","R"],
        "B" : ["q99","B","R"]
    },
    "q6":{
        "l" : ["q12","l","R"],
        "b" : ["q2","b","R"],
        "B" : ["q99","B","R"]
    },
    "q7":{
        "o" : ["q1","a","R"],
        "n" : ["q1","a","L"],
        "a" : ["q1","a","R"],
        "B" : ["q99","B","R"]
    },
    "q9":{
        "d" : ["q4","d","R"],
        "m" : ["q13","m","R"],
        "e" : ["q5","e","R"],
        "r" : ["q5","e","L"],
        "t" : ["q20","t","R"],
        "B" : ["q99","B","R"]
    },
    "q11":{
        "e" : ["q5","e","R"],
        "a" : ["q1","a","R"],
        "m" : ["q1","a","L"],
        "i" : ["q12","i","R"],
        "n" : ["q5","e","L"],
        "s" : ["q19","s","R"],
        "r" : ["q1","a","L"],
        "B" : ["q99","B","R"]
    },
    "q12":{
        "d" : ["q34","d","R"],
        "g" : ["q9","g","R"],
        "e" : ["q5","e","R"],
        "a" : ["q1","a","R"],
        "o" : ["q1","a","R"],
        "i" : ["q1","a","R"],
        "n" : ["q14","n","R"],
        "k" : ["q11","k","R"],
        "B" : ["q99","B","R"]
    },
    "q42":{
        "e" : ["q5","e","R"],
        "a" : ["q1","a","R"],
        "o" : ["q1","a","R"],
        "i" : ["q1","a","R"],
        "n" : ["q14","n","R"],
        "k" : ["q11","k","R"],
        "B" : ["q99","B","R"]
    },
    "q13":{
        "t" : ["q1","a","L"],
        "e" : ["q5","e","R"],
        "r" : ["q1","a","L"],
        "k" : ["q31","a","L"],
        "l" : ["q31","a","L"],
        "a" : ["q21","u","R"],
        "u" : ["q21","u","R"],
        "a" : ["q1","a","R"],
        "n" : ["q1","a","L"],
        "p" : ["q16","p","R"],
        "o" : ["q21","u","R"],
        "s" : ["q19","s","R"],
        "B" : ["q99","B","R"]
    },
    "q43":{
        "a" : ["q1","a","R"],
        "u" : ["q21","u","R"],
        "n" : ["q1","a","L"],
        "l" : ["q21","u","L"],
        "B" : ["q99","B","R"]
    },
    "q14":{
        "a" : ["q1","a","R"],
        "i" : ["q9","i","R"],
        "d" : ["q4","d","R"],
        "g" : ["q7","g","R"],
        "t" : ["q20","t","R"],
        "k" : ["q7","g","R"],
        "B" : ["q99","B","R"]
    },
    "q15":{
        "b" : ["q2","b","R"],
        "c" : ["q3","c","R"],
        "o" : ["q15","o","R"],
        "B" : ["q99","B","R"]
    },
    "q16":{
        "p" : ["q1","a","R"],
        "o" : ["q1","a","R"],
        "a" : ["q1","a","R"],
        "u" : ["q21","u","R"],
        "B" : ["q99","B","R"]
    },
    "q18":{
        "r" : ["q1","a","R"],
        "a" : ["q1","a","R"],
        "d" : ["q4","d","R"],
        "B" : ["q99","B","R"]
    },
    "q19":{
        "a" : ["q1","a","R"],
        "l" : ["q5","e","L"],
        "e" : ["q5","e","R"],
        "k" : ["q5","e","L"],
        "o" : ["q12","i","R"],
        "i" : ["q12","i","R"],
        "p" : ["q5","e","L"],
        "t" : ["q1","a","L"],
        "y" : ["q1","a","L"],
        "B" : ["q99","B","R"]
    },
    "q20":{
        "g" : ["q9","i","L"],
        "d" : ["q9","i","L"],
        "n" : ["q1","a","L"],
        "i" : ["q12","i","R"],
        "B" : ["q99","B","R"]
    },
    "q21":{
        "u" : ["q21","u","R"],
        "s" : ["q19","s","R"],
        "m" : ["q13","m","R"],
        "r" : ["q18","r","R"],
        "l" : ["q12","l","R"],
        "B" : ["q99","B","R"]
    },
    "q25":{
        "k" : ["q1","a","L"],
        "i" : ["q1","a","R"],
        "o" : ["q1","a","R"],
        "a" : ["q1","a","R"],
        "B" : ["q99","B","R"]
    },
    # "q4":{
    #     "a" : ["q1","a","R"],
    #     "u" : ["q1","a","R"],
    #     "o" : ["q1","a","R"]
    # },
    "q99":{
        "-" : ["q99","-","R"]
    }
}
    

def getFinalState(key):
    return "q" + str(ord(key)-96)

def turing(input_str):
    tape = list(input_str+"B")
    head_pos = 0
    final = "q99"
    state = "q0"
    result = []
    move = ""
    state_temp = state
    nextS = ""
    inp = tape[head_pos]
    add = 0
    
    while state!=final :
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
                result.append((( "𝛿("+state_temp+", "+inp+") = "+ nextS +" | "+temp +" => "+tape[head_pos] + " | move : " + move),"".join(tape[:len(tape)-1]),move))
            tape[head_pos] = node[state][tape[head_pos]][1]
            state = node[state][temp][0]
            #print(state,":",temp ,"->",tape[head_pos])
            result.append((( "𝛿("+state_temp+", "+inp+") = "+ nextS +" | "+temp +" => "+tape[head_pos] + " | move : " + move),"".join(tape[:len(tape)-1]),move))
            #print(tape)
            head_pos+= 1 if move == "R" else -1
        else:
            result.append((( "𝛿("+state_temp+", "+inp+") = Halt | "+inp+ " => "+inp+ " | move : - " ),"".join(tape[:len(tape)-1]),move))
            hasil = ''.join(tape[:len(tape)-1])
            return hasil,result

        
        
    print(tape[:len(tape)-1])
    result.append((( "𝛿("+state_temp+", "+inp+") = "+ nextS +" | "+tape[len(tape)-1] + " => FINAL |\nmove : " + move + " [Diterima]"),"".join(tape[:len(tape)-1]),move))
    hasil = ''.join(tape[:len(tape)-1])
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
