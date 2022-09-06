# https://school.programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    answer = []
    file_list  = [[]]*10
    prior_list = [ (i,v) for i, v in enumerate(priorities)]

    for i in range(1, 10):
        if i in priorities:
            file_list[i] = list(filter(lambda x : x[1]==i, prior_list))

    standard_idx = -1
    tmp = []

    for i in range(9, 0, -1): 
        if file_list[i]:
            for index, value in file_list[i]:
                if index > standard_idx:
                    answer.append(index)
                    standard_idx = index
                else:
                    tmp.append(index)
                    continue

            for m in tmp:
                answer.append(m)
                standard_idx = m
            else:
                tmp = []

    return answer.index(location)+1
