from collections import deque

numOfOperations  = int(input())
dq = deque([])

while(numOfOperations > 0):
    command = input().split(" ")
     
    if(command[0] == "append"):
        dq.append(int(command[1]))
    elif(command[0] == "pop"):
        dq.pop()
    elif(command[0] == "popleft"):
        dq.popleft()
    elif(command[0] == "appendleft"):
        dq.appendleft(int(command[1]))    
                    
    
    numOfOperations = numOfOperations - 1
    
for elem in dq:
    print(elem,end=" ")
