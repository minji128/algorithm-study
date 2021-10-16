def solution(numbers):
    all_numbers = [num for num in range(10)]

    return sum(list(set(all_numbers) - set(numbers)))