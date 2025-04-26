def find_number(n, k):
    count_odd = (n + 1) // 2
    if k <= count_odd:
        return 2 * k - 1
    else:
        return 2 * (k - count_odd)

n, k = map(int, input().split())

print(find_number(n, k))
