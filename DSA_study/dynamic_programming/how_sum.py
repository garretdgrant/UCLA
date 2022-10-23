def how_sum(target_sum, numbers, memo = None):
    """
    Takes in a target sum and arr of nums as args
    function returns new array containg combos of
    elements that add to target, else null.
    If multiple combos exist, one is returned
    """
    if memo is None:
        memo = {}
    if target_sum in memo:
        return memo[target_sum]
    if target_sum < 0:
        return None
    if target_sum == 0:
        return []

    for num in numbers:
        remainder = target_sum - num
        result = how_sum(remainder, numbers, memo)
        if result is not None:
            memo[target_sum] = [*result, num]
            return [*result, num]

    memo[target_sum] = None
    return None

print(how_sum(7, [2,3]))
print(how_sum(7, [5,3,4,7]))
print(how_sum(7, [2,4]))
print(how_sum(8, [2,3,5]))
print(how_sum(300, [7,14]))


