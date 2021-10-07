def solution(lottos, win_nums):
    answer = [0, 0]
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt = 0
    zero_cnt = lottos.count(0)
    for i in lottos:
        if i in win_nums:
            cnt += 1
    answer[0], answer[1] = rank[cnt+zero_cnt], rank[cnt]
    return answer