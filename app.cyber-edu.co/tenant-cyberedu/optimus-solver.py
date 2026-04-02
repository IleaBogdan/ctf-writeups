M = (1 << 64) - 1
E = bytes.fromhex("64a862093c805ccb70857cfb4ee661c0e9c5918afe6d80d69d5490873079bf8c865944af9cfad84143d721a134a64093feecf9ec9f27352e190806dfdc97a557c5bb658221")

def u(x):
    return x & M

def f(x):
    r = 0
    for i in range(8):
        r ^= (x >> (i * 8)) & 0xff
    return r

def solve():
    n = 689
    a = [0] * (n + 1)
    p1 = [0] * (n + 1)
    p2 = [0] * (n + 1)
    p3 = [0] * (n + 1)
    p4 = [0] * (n + 1)
    s = [0] * (n + 1)

    p1[0] = p2[0] = p3[0] = p4[0] = 2
    s[1] = 2

    for i in range(1, n + 1):
        if i == 1:
            a[i] = u(3 ^ 0x37)
        else:
            a[i] = u(((i + 2) * p1[i - 2]) ^ 0x37)
            s[i] = u(s[i - 1] + a[i])

        x = u(((i + 3) * s[i]) ^ 0x37)
        p4[i] = u(p4[i - 1] + x)

        x = u(((i + 3) * p4[i - 1]) ^ 0x37)
        p3[i] = u(p3[i - 1] + x)

        x = u(((i + 3) * p3[i - 1]) ^ 0x37)
        p2[i] = u(p2[i - 1] + x)

        x = u(((i + 3) * p2[i - 1]) ^ 0x37)
        p1[i] = u(p1[i - 1] + x)

    b = [0] * (n + 1)
    sa = [2] * (n + 1)
    b[0] = b[1] = 1

    for i in range(2, n + 1):
        sa[i] = u(sa[i - 1] + a[i])
        b[i] = u(((i + 2) * sa[i - 1]) ^ 0x37)

    sb = [0] * (n + 2)
    for i in range(n + 1):
        sb[i + 1] = u(sb[i] + b[i])

    out = []
    for i, c in enumerate(E, 1):
        x = u((i * 10 + 2) * sb[i * 10])
        out.append(f(x) ^ 0x37 ^ c)

    return bytes(out).decode()

print(solve())