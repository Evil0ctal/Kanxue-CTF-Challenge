import sympy

# 512-bit number
n = 0x60E303A2D6FFFF4BDF86EE10F13313F1236D7F067D52FFB4CAC84648CC87501394A798F7BBB1B5B488AA7386C374CD93DC0BA776477BDE07543F1397F130F9A9

# Factorize the number
factors = sympy.factorint(n)

# Get one of the prime factors
prime_factors = [factor for factor in factors.keys() if sympy.isprime(factor)]
prime_factor_hex = hex(prime_factors[0])

print(prime_factor_hex)
