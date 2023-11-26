def is_equal_str(S, l, a, b):
    p = 10 ** 9 + 7
    x = 257
    arr_x = [1] * (len(S) + 1)
    arr_h = [0] * (len(S) + 1)

    for i in range(1, len(S) + 1):
        symb = ord(S[i - 1])
        if S[i-1].isdigit():
            symb = int(S[i-1])

        arr_h[i] = (arr_h[i - 1] * x + symb) % p
        arr_x[i] = (arr_x[i - 1] * x) % p

    h1 = (arr_h[a + l] + arr_h[b] * arr_x[l]) % p
    h2 = (arr_h[b + l] + arr_h[a] * arr_x[l]) % p
    return True if h1 == h2 else False


def is_equal_str_input():
    S = input().strip()
    q = int(input().strip())
    for _ in range(q):
        l, a, b = map(int, input().strip().split())
        print(is_equal_str(S, l, a, b))


def get_base_of_string(S):
    k = 0
    for i in range(len(S) - 1):
        if is_equal_str(S, i + 1, 0, len(S) - i - 1):
            k = i + 1
    return len(S) - k


def get_base_of_string_input():
    S = input().strip()
    print(get_base_of_string(S))


def z_function(S):
    z = [0] * len(S)
    left, right = 0, 0
    for i in range(1, len(S)):
        z[i] = max(0, min(z[i - left], right - i))
        while i + z[i] < len(S) and S[z[i]] == S[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left, right = i, i + z[i]
    return z


def z_function_input():
    S = input().strip()
    print(" ".join(map(str, z_function(S))))


def mirror(S):
    k = [len(S)]
    for i in range(1, len(S)):
        if is_equal_str(S, i, 0, len(S) - 2 * i):
            k.append(len(S) - i)
    return k[::-1]

def mirror_input():
    n, m = map(int, input().strip().split())
    S = input().strip().split()
    print(" ".join(map(str, mirror(S))))


def manacher_odd(s):
    s = '$' + s + '^'
    n = len(s)
    res = [0] * n
    l = 0
    r = 0
    for i in range(1, n - 1):
        res[i] = max(0, min(r - i, res[l + (r - i)]))
        while s[i - res[i]] == s[i + res[i]]:
            res[i] += 1
        if i + res[i] > r:
            l = i - res[i]
            r = i + res[i]
    return res[1:-1]

def manacher(s):
    res = manacher_odd('#' + '#'.join(s) + '#')[1:-1]
    return (sum([x // 2 for x in res[::2]]) + sum([x // 2 for x in res[1::2]]))

def manacher_input():
    s = input().strip()
    print(manacher(s))


if __name__ == "__main__":
    # is_equal_str_input()
    # get_base_of_string_input()
    z_function_input()
    # mirror_input()