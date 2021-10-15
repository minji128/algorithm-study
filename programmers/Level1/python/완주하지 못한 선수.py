from collections import Counter

def solution(participant, completion):
    answer = ''
    participant_dict = Counter(participant)
    completion_dict = Counter(completion)

    for k, v in participant_dict.items():
        if k in completion_dict.keys():
            participant_dict[k] -= completion_dict[k]

    for k, v in participant_dict.items():
        if participant_dict[k] != 0:
            return k