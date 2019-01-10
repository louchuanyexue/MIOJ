line1 = input()


def solution(line):
    ato = 1
    list1 = line.split()
    count = len(list1)
    for item in list1:
        index = int(item)
        if index == 0:
            break
        ato += index
        if ato >= count:
            break
    if ato >= count:
        return "true"
    else:
        return "false"


print(solution(line1))

