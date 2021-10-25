def solution(priorities, location):
    new = priorities.copy()
    idx = [i for i in range(len(priorities))]
    i = 0

    while True:
        if new[i] < max(new[i+1:]):
            new.append(new.pop(i))
            idx.append(idx.pop(i))
        else:
            i += 1

        if new == sorted(new, reverse=True):
            break
    return idx.index(location) +1
