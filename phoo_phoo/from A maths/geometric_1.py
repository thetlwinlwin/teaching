n = 1
total = 0
while True:
    u_n = 1*(3**(n-1))
    total = total + u_n
    if total > 2_000_000:
        break
    n = n + 1
print(n)
