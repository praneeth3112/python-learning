arr = ['trying', 'failed', 'done']
n = 1


def calc(a, b):
    return (a + len(arr[b]) - len(arr) + n) % len(arr)


k = len(arr) - 1
while k >= 0:
    n = calc(k, n)

    if (n + k) % 2 == 0:
        n = (n + len(arr[k]) - k) % len(arr)
        k -= 1

print(arr[(n + len(arr[0]) - len(arr[1]) - len(arr) - 1) % len(arr)])

