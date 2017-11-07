def firstDuplicate(a):
    nums = set()
    for i,v in enumerate(a):
        if v in nums:
            return v
        else:
            nums.add(v)
    return -1