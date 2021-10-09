def solution(board, moves):
    basket = []
    answer = 0
    boardNumber = []

    for i in zip(*board):
        boardNumber.append(list(filter(lambda x : x != 0, list(i))))
        for move in moves:
            if boardNumber[move-1]:
                popDoll = boardNumber[move-1].pop(0)
                if len(basket)>=1 and basket[len(basket)-1] == popDoll:
                    basket.pop(-1)
                    answer += 2
                else:
                    basket.append(popDoll)
    return answer
