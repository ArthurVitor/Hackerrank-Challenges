def runner_up_score(array):
    array = set(array)
    array = list(array)
    array = sorted(array)
    return array[-2]

print(runner_up_score([-7, -7, -7, -7, -6]))