def solution(answers):
    people_1 = [1, 2, 3, 4, 5]
    people_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    people_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0, 0, 0, 0]

    for i in range(len(answers)):
        cnt[1] += 1 if (answers[i] == people_1[i % len(people_1)]) else 0
        cnt[2] += 1 if (answers[i] == people_2[i % len(people_2)]) else 0
        cnt[3] += 1 if (answers[i] == people_3[i % len(people_3)]) else 0

    return [i for i in range(1, len(cnt)) if cnt[i] == max(cnt[1], cnt[2], cnt[3])]