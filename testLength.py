"""
2DFA emulator
Input parameters:
First, a comma-seperated list of states. Ex:
q1,q2,q3,q4
Then, a single initial state. Ex:
q1
Then, a comma-seperated list of accepting states. Ex:
q2,q4
Then line-by-line transitions:
Q,W,W->Q,D,D
Where Q is a state, W is an element of the alphabet (_ is blank, don't add), and D is a direction, between L, S, or R (for left, stay, or right)
This ends simply with a blank line at the end

Note: the alphabet will be assumed to be all ascii characters except for the newline and special characters like ctrl+c
(reasonably whatever the computer can read in without errors) since it won't affect performance to add extra characters to the alphabet.

After the 2DFA is given, you can enter strings to check if the 2DFA accepts or rejects them.
The code will output a trace of current state and current head positions after each step and finally return either accept or reject.
Press ctrl+c to end the code.
"""
import main
import time


def run(i, machine,word):
        start = time.time()
        n=i*3
        dirs={"L":-1,"S":0,"R":1}
        states,first,finals,moves=machine

        tape="_"+word+"_" #2dfa gets padded with empty space to left and right
        #_ will be used as the special empty symbol to add spaces to strings

        #head locations
        h1=1 #starts on first non-blank
        h2=1
        state=first
        #print("state:",state,"- head 1:",tape[h1],"- head2:",tape[h2])
        while(state not in finals):
                try:
                        state,d1,d2=moves[state][tape[h1]][tape[h2]]
                        h1+=dirs[d1]
                        h2+=dirs[d2]
                        if(h1<0):
                                h1=0
                        elif(h1>1+n):
                                h1=1+n
                        if(h2<0):
                                h2=0
                        elif(h2>1+n):
                                h2=1+n
                        #print("state:",state,"- head 1:",tape[h1],"- head2:",tape[h2])
                except KeyError:
                        return False #no valid transition
        end = time.time()
        print(i , end-start)
        return True

machine=main.readInFile()
'''while(True):
        word=input("Enter in a word to check if it is accepted\n")
        res=run(machine,word)
        if(res):
                print("accept")
        else:
                print("reject")
'''


def abc (n):
        a = ""
        b = ""
        c = ""
        for i in range(n):
                a += 'a'
                b += 'b'
                c += 'c'
        return a + b + c

if __name__ == '__main__':
    inputs = [1, 10, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000]

    for i in inputs:
            run(i, machine, abc(i))