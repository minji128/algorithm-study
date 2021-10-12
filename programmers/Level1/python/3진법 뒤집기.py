def solution(n):
    n_3 = ""
    while n>0:
        n, r = divmod(n, 3)
        n_3 += str(r)
    return int(n_3, 3)