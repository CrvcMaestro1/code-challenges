from itertools import permutations


def is_palindrome(s):
    if s.startswith("0"):
        return False
    return s == s[::-1]

# Non-optimal solution
# def solution(S):
#     palindromes = []
#     for i in range(1, len(S) + 1):
#         for c in permutations(S, i):
#             value = "".join(c)
#             if is_palindrome(value) and not value.startswith("0"):
#                 palindromes.append(int(value))
#     sorted_palindromes = sorted(palindromes, reverse=True)
#     if len(sorted_palindromes) == 0:
#         return "0"
#     else:
#         return sorted_palindromes.pop(0)


def solution(S):
    # Greedy algorithm
    if is_palindrome(S) and not S.startswith("0"):
        return S
    length = len(S)
    occurrences = dict()
    for i in range(0, length):
        number = int(S[i])
        if number not in occurrences:
            occurrences[number] = 1
        else:
            occurrences[number] += 1
    largest = [None] * length
    palindromes = []
    front = 0
    for i in range(9, -1, -1):
        if i in occurrences:
            if occurrences[i] % 2 != 0:
                division = length // 2
                largest[division] = chr(i + 48)
                occurrences[i] -= 1
                while occurrences[i] > 0:
                    largest[front] = chr(i + 48)
                    largest[length - front - 1] = chr(i + 48)
                    occurrences[i] -= 2
                    front += 1
            else:
                while occurrences[i] > 0:
                    largest[front] = chr(i + 48)
                    largest[length - front - 1] = chr(i + 48)
                    occurrences[i] -= 2
                    front += 1
            palindrome = "".join([lg for lg in largest if lg])
            if is_palindrome(palindrome):
                palindromes.append(int(palindrome))
    if len(palindromes) == 0:
        return "0"
    sorted_palindromes = sorted(palindromes, reverse=True)
    return sorted_palindromes.pop(0)


values = ["39878", "00900", "0000", "54321", "999999", "3444", "331", "313551", "12525"]

for s in values:
    print(solution(s))

for number in range(1, 100000):
    print(solution(str(number)))
