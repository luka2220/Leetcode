
def containsDuplicate(nums) -> bool:
    hashset = set()

    for num in nums:

        if num not in hashset:
            hashset.add(num)
        else:
            return True

    return False


# test
print(containsDuplicate([1, 2, 3, 1]))
