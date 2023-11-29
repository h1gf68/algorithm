def z_function(S):
    z = [0] * len(S)
    left, right = 0, 0
    for i in range(1, len(S)):
        z[i] = max(0, min(z[i-left], right-i))
        while i + z[i] < len(S) and S[z[i]] == S[i+z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left, right = i, i + z[i]
    return z

def z_func_mirror(s, n):
    z = [0 for _ in range(n)]
    z[0] = 1
    for i in range(1, n):
        l = 0
        while i-l >= 0 and s[i-l] == s[l]:
            z[i] += 1
            l += 1
            d, m = divmod((i+1), 2)
            if l == d:
                z[i] += l + m
                break
    return z

def z_func_mirror_input():
    n = int(input().strip())
    s = input().strip()

    print(" ".join(map(str, z_func_mirror(s, n))))
    print(z_function(s))

if __name__ == "__main__":
    z_func_mirror_input()