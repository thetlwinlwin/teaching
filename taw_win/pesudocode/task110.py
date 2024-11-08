def is_perfect_num(val: int) -> bool:
    divisors = []
    for i in range(1, val):
        if val % i == 0:
            divisors.append(i)
    return sum(divisors) == val


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def perfect_num_generator(limit: int) -> list[int]:
    results = []
    counter = 1
    is_found = False
    while not is_found:
        part_1 = (2**counter) - 1
        if is_prime(part_1):
            perfect_num = part_1 * (2 ** (counter - 1))
            if perfect_num > limit:
                is_found = True
            else:
                results.append(perfect_num)
        counter += 1
    return results


def main():
    print("Perfect Number Between 1 and 10_000")
    for i in range(1, 10_001):
        if is_perfect_num(i):
            print(i)


print(perfect_num_generator(10_000))
