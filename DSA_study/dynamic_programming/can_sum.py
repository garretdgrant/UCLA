def can_sum(target, arr, memo={}):
    """Takes in target and arr, sees if there is a possible sum in arr
    arguments in arr can be used as many times as needed"""
    if target < 0: return False
    if target == 0: return True
    if target in memo: return memo[target]

    for num in arr:
        remainder = target - num
        if can_sum(remainder, arr, memo):
            memo[target] = True
            return True
    memo[target] = False
    return False

print (can_sum(7, [2,3])) #true
print (can_sum(300, [7,14])) #true

