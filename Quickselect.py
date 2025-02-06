import random

def randomized_quickselect(arr, k):
    """
    Randomized Selection: Find the k-th smallest element using the
    Randomized Quickselect algorithm.
    """
    if len(arr) == 1:
        return arr[0]

    # Pick a random pivot
    pivot = random.choice(arr)

    # Partition the array into elements less than, equal to, or greater than pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    count = len([x for x in arr if x == pivot])

    if k < len(low):
        return randomized_quickselect(low, k)
    elif k < len(low) + count:
        return pivot
    else:
        return randomized_quickselect(high, k - len(low) - count)


if __name__ == "__main__":
    # Input array and k
    arr = list(map(int, input("Enter the elements of the array (space-separated): ").split()))
    k = int(input(f"Enter the value of k (1 to {len(arr)}): ")) - 1

    if 0 <= k < len(arr):
        result = randomized_quickselect(arr, k)
        print(f"The {k + 1}-th smallest element is: {result}")
    else:
        print("Invalid value of k!")
