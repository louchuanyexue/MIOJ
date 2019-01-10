line1=input()
def solution(line):
    list1=[]
    result=0
    list1=line.strip().split()
    for i in range(len(list1)):
        result^=int(list1[i])
    return result
print(solution(line1))
    
