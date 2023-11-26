def partition(arr, left, right, x):
    if not len(arr) or len(arr) == 1:
        return 0

    while True:
        while left < len(arr) and arr[left] < x:
            left += 1

        while arr[right] >= x and right >= 0:
            right -= 1

        if left >= right:
            return right + 1

        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

def partition_input():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    x = int(input().strip())
    ind = partition(a, 0, n - 1, x)
    print(ind)
    print(n - ind)


import random
def partition(a, l, r):
    pivot, l_, r_ = a[l], l, r
    i = l_
    while i <= r_:
        if a[i] < pivot:
            a[l_], a[i] = a[i], a[l_]
            l_ += 1
        elif a[i] > pivot:
            a[r_], a[i] = a[i], a[r_]
            r_ -= 1
            i -= 1
        i += 1
    return l_, r_

def quicksort(a, l, r):
    if l >= r:
        return a

    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition(a, l, r)
    quicksort(a, l, m1 - 1)
    quicksort(a, m2 + 1, r)
    return a

def quicksort_input():
    n = int(input().strip())
    if n > 0:
        a = list(map(int, input().strip().split()))
        print(" ".join(map(str, quicksort(a, 0, n - 1))))
    else:
        print("")


def merge(n, an, m, am):
    if not n and not m: return []
    if not n: return am
    if not m: return an

    i = j = 0
    a = []

    while i < n and j < m:
        if an[i] <= am[j]:
            a.append(an[i])
            i += 1
        else:
            a.append(am[j])
            j += 1
    a += an[i:] + am[j:]
    return a

def merge_input():
    n = int(input().strip())
    an = list(map(int, input().strip().split()))
    m = int(input().strip())
    am = list(map(int, input().strip().split()))
    print(" ".join(map(str, merge(n, an, m, am))))


def merge_sort(n, a):
    if n < 2:
        return a
    b = n // 2
    return merge(b, merge_sort(b, a[:b]), n - b, merge_sort(n - b, a[b:]))

def merge_sort_input():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    print(" ".join(map(str, merge_sort(n, a))))


def radix_sort(n, a):
    print("Initial array:")
    print(", ".join(a).strip(', '))
    print("**********")

    for i in range(len(a[0])):
        b = [[] for _ in range(10)]
        for x in a:
            d = int(x) // 10 ** i % 10
            b[d].append(x)

        a = []
        print(f"Phase {i + 1}")
        for j in range(len(b)):
            if len(b[j]):
                print(f"Bucket {j}: {', '.join(b[j]).strip(',')}")
            else:
                print(f"Bucket {j}: empty")
            a += b[j]
        print("**********")

    print("Sorted array:")
    print(", ".join(a).strip(", "))


def radix_sort_input():
    n = int(input().strip())
    a = []
    for i in range(n):
        a.append(input().strip())
    radix_sort(n, a)

if __name__ == "__main__":
    # partition_input()
    # quicksort_input()
    # merge_input()
    # merge_sort_input()
    radix_sort_input()
