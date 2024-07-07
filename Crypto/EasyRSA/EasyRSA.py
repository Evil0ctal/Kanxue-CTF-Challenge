# 题目：在一次RSA密钥计算中，假设 P = A890768DCF26582145A87B24BE722E9B，Q = 8DD7C2DCB43AC1945F668E72F058EBBB，E = 10001，求解出D。

# 定义扩展欧几里得算法，用于计算模逆
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


# 计算模逆
def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Inverse doesn't exist")
    else:
        return x % m


# 十六进制转十进制
P = int('A890768DCF26582145A87B24BE722E9B', 16)
Q = int('8DD7C2DCB43AC1945F668E72F058EBBB', 16)
E = int('10001', 16)

# 计算 N = P * Q
N = P * Q

# 计算 φ(N) = (P - 1) * (Q - 1)
phi_N = (P - 1) * (Q - 1)

# 计算 D，使得 D * E ≡ 1 (mod φ(N))
D = mod_inverse(E, phi_N)

# 输出 D 的值，使用十六进制表示
print("D:", hex(D))

# Output:
# D: 0x3fb9954df90fe05207f2c044f0f5c34a45dce3066018def4eade48f2c48add31
