def median_of_medians(arr, k):
    """
    Deterministic Selection: Find the k-th smallest element in the array
    using the Median of Medians algorithm.
    """
    if len(arr) <= 5:
        return sorted(arr)[k]

    # Divide into sublists of 5 and sort each sublist
    sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]

    # Recursively find the median of the medians
    pivot = median_of_medians(medians, len(medians) // 2)

    # Partition the array around the pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    count = len([x for x in arr if x == pivot])

    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + count:
        return pivot
    else:
        return median_of_medians(high, k - len(low) - count)


if __name__ == "__main__":
    # Input array and k
    arr = list(map(int, input("Enter the elements of the array (space-separated): ").split()))
    k = int(input(f"Enter the value of k (1 to {len(arr)}): ")) - 1

    if 0 <= k < len(arr):
        result = median_of_medians(arr, k)
        print(f"The {k + 1}-th smallest element is: {result}")
    else:
        print("Invalid value of k!")
