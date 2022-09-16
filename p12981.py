def solution(n, words):
    for i in range(len(words)):
        if i != 0 and words[i][0] != words[i-1][-1]:
            break
        if words[i] in words[:i]:
            break
    else:
        return [0,0]
    
    number = n if (i+1)%n == 0 else (i+1)%n
    turn   = (i+1)//n +1 if (i+1)%n > 0 else (i+1)//n
    return [number, turn]
