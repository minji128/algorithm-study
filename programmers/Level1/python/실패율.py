def solution(N, stages):
    fail_rate = {}
    stage_player_cnt = len(stages)

    for i in range(1, N+1):
        if stage_player_cnt != 0:
            fail_rate[i] = stages.count(i) / stage_player_cnt
            stage_player_cnt -= stages.count(i)
        else:
            fail_rate[i] = 0

    return sorted(fail_rate, key=lambda x:fail_rate[x], reverse=True)