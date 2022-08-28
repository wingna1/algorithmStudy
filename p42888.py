# https://school.programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    action_list = {"Enter":"들어왔습니다", "Leave":"나갔습니다"}
    member_list = {}
    system_log = []
    
    for i in record:
        user_info = list(i.split())
        if user_info[0] != "Change":
            system_log.append([user_info[0], user_info[1]]) # 아이디와 출입변경 
        if user_info[0] != "Leave":
            member_list[user_info[1]] = user_info[2] # 아이디와 닉네임 기록
            
    for act, user_id in system_log:
        answer.append(f"{member_list[user_id]}님이 {action_list[act]}.")
    
    return answer
