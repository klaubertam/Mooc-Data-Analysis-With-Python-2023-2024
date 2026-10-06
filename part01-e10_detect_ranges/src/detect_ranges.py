def detect_ranges(L):
    nums = sorted(L) 
    result = []

    start = nums[0]
    end = nums[0]

    for i in range(1, len(nums)):
        if nums[i] == end + 1:
            end = nums[i]
        else:
            if start == end:
                result.append(start)
            else:
                result.append((start, end + 1))  
            start = end = nums[i]
    if start == end:
        result.append(start)
    else:
        result.append((start, end + 1))

    return result


def main():
    print(detect_ranges([2,5,4,8,12,6,7,10,13]))


if __name__ == "__main__":
    main()