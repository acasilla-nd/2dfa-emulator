"""
nDFA emulator
Similar spiel as 2DFA since this is a generalization after all
Has some nicer printing and stuff as a bonus

Input parameters:
First, the number of heads
n
Then, a comma-seperated list of states. Ex:
q1,q2,q3,q4
Then, a single initial state. Ex:
q1
Then, a comma-seperated list of accepting states. Ex:
q2,q4
Then line-by-line transitions:
Q,W,W,...->Q,D,D,...
Where Q is a state, W is an element of the alphabet (_ is blank, don't add), and D is a direction, between L, S, or R (for left, stay, or right)
There will be n Ws and n Ds, corresponding to each of the heads
This ends simply with a blank line at the end
Note: the alphabet will be assumed to be all ascii characters except for the newline and special characters like ctrl+c (reasonably whatever the computer can read in without errors) since it won't affect performance to add extra characters to the alphabet.

After the nDFA is given, you can enter strings to check if the nDFA accepts or rejects them. The code will output a trace of current state and current head positions after each step and finally return either accept or reject.
Press ctrl+c to end the code.
"""

def printState(state,heads,tape,mode=0):
	if(mode==0):
		out="State: "+state
		for i in range(len(heads)):
			out+=" - head"+str(i+1)+": "+str(heads[i])+" "+tape[heads[i]]
		print(out)
	elif(mode==1):
		print()
		print("State:",state)
		out=""
		for i in range(len(tape)):
			blank=True
			for j in range(len(heads)):
				if(heads[j]==i):
					out+=str(j+1)+" "
					blank=False
			if(blank):
				out+="  "
		print(out)
		for i in range(len(out)):
			if(out[i]!=" "):
				out=out[:i]+"|"+out[i+1:]
		print(out)
		print(out.replace("|","v"))
		print(" ".join(tape))

def genKey(state,states,heads,n):
	key=0
	for i in range(len(heads)):
		key+=(n+2)**i*heads[i]
	key+=states.index(state)*(n+2)**len(heads)
	return key

#might want to add a read in for files
def readIn():
	numh=int(input())
	states=input().split(",")
	first=input()
	finals=input().split(",")
	moves={}
	x=input()
	while(x):
		x=x.split("->")
		tin=tuple(x[0].split(","))
		tout=x[1].split(",")
		moves[tin]=tout
		x=input()
	return (numh,states,first,finals,moves)

def run(machine,word,killLoop=True,mode=1):
	n=len(word)
	seen=set() #if we are ever in the same state with the same head positions, we are in a neverending loop and can kill and reject
	dirs={"L":-1,"S":0,"R":1}
	numh,states,first,finals,moves=machine

	tape="_"+word+"_" #2dfa gets padded with empty space to left and right
	#_ will be used as the special empty symbol i guess since i would like to use spaces in strings
	
	heads=[1]*numh #heads all start at pos 1
	state=first
	printState(state,heads,tape,mode)
	key=genKey(state,states,heads,n) #for loop killing
	seen.add(key)
	while(state not in finals):
		try:
			res=moves[(state,*[tape[x] for x in heads])]
			state,hdir=res[0],res[1:]
			heads=[min(n+1,max(0,a+dirs[b])) for a,b in zip(heads,hdir)]
			printState(state,heads,tape,mode)
			key=genKey(state,states,heads,n)
			if(killLoop and key in seen):
				print("Loop reached")
				return False
			seen.add(key)
		except KeyError:
			return False #no valid transition
	return True

machine=readIn()
while(True):
	word=input("Enter in a word to check if it is accepted\n")
	res=run(machine,word)
	if(res):
		print("accept")
	else:
		print("reject")	
