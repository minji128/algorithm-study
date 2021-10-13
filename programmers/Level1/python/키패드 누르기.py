def solution(numbers, hand):
    answer = ""
    right = '#'
    left = '*'

    for num in numbers:
        if num in [1, 4, 7]:
            answer += "L"
            left = num
        elif num in [3, 6, 9]:
            answer += "R"
            right = num
        else:
            r_distance = distance(num, right)
            l_distance = distance(num, left)

            if r_distance == l_distance:
                if hand == "right":
                    answer += "R"
                    right = num
                else:
                    answer += "L"
                    left = num
            elif r_distance < l_distance:
                answer += "R"
                right = num
            else:
                answer += "L"
                left = num
    return answer


def distance(numbers, hands_loc):
    loc = {'1': (0, 0), '2': (1, 0), '3': (2, 0)
        , '4': (0, 1), '5': (1, 1), '6': (2, 1)
        , '7': (0, 2), '8': (1, 2), '9': (2, 2)
        , '*': (0, 3), '0': (1, 3), '#': (2, 3)}

    x_h, y_h = loc[str(hands_loc)]
    x_n, y_n = loc[str(numbers)]

    return abs(x_n - x_h) + abs(y_n - y_h)