def solution(R):
    # I must optimize, currently it is O(n^2)
    scooter_time = {"A": 5, "S": 40}
    foot_time = {"A": 20, "S": 30}
    accumulated_sum = [0] * (len(R) + 1)
    i = 0
    while i < len(accumulated_sum):
        length_r = len(R)
        j = 0
        pivot = length_r - i
        while j < length_r:
            if j >= pivot:
                accumulated_sum[i] += foot_time[R[j]]
            else:
                accumulated_sum[i] += scooter_time[R[j]]
            j += 1
        i += 1
    return sorted(accumulated_sum).pop(0)


cases = ["ASAASS", "SSA", "SSSSAAA"]

for case in cases:
    print('for {} sum is {}'.format(case, solution(case)))
