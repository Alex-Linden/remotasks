def binary_search_square_root(n, l = 0, r = n):
    if r >= n:
        return 0
    while l < r:
        mid = l + (r-l) //2

        if mid >= n // mid:
            r = mid - 1
        else:
            l = mid + 1
    while l*l < n:
        l += 1
    if l*l == n:
        return l
    else:
        return -1


print(binary_search_square_root(100))