line=input()
def solution(line):
    ato = 1
    i=1
    list1=[]
    list1=line.split()
    count=(len(list1))
    while 1:
        ato+=int(list1[i-1])
        if(int(list[i-1])==0):
            ato+=1
        i=ato
        if(ato>=count or i==count):
            break
    """cc=int(list1[-1])
    ato=ato-cc"""
    if(ato>=count):
        return "true"
    else:
        return "false"
print(solution(line))  

