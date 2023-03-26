if __name__ == '__main__':
    N = int(input())
    listt = []
    while(N > 0):
        command = input().split(" ")
        if command[0] == "insert":
            listt.insert(int(command[1]),int(command[2]))
        if command[0] == "remove":
            listt.remove(int(command[1]))
        if command[0] == "append":
            listt.append(int(command[1]))
        if command[0] == "sort":
            listt.sort()
        if command[0] == "pop":
            listt.pop()
        if command[0] == "reverse":
            listt.reverse()
        if command[0] == "print":
            print(listt)   
        N = N - 1
