class AcceptFilter:
    def accept(self, n):
        return True


class DivisibleByFilter:
    number = None
    next_item = None

    def __init__(self, number, next_item):
        self.number = number
        self.next_item = next_item

    def accept(self, n):
        self_filter = self
        while self_filter is not None and type(self_filter) == DivisibleByFilter:
            if n % self_filter.number == 0:
                return False
            self_filter = self_filter.next_item
        return True


class PrimeChecker:
    def __init__(self):
        self.number = 2
        self.applied_filter = AcceptFilter()

    def next_item(self):
        while not self.applied_filter.accept(self.number):
            self.number += 1
        self.applied_filter = DivisibleByFilter(self.number, self.applied_filter)
        return self.number


if __name__ == '__main__':
    checker = PrimeChecker()
    primes = []
    for _ in range(5000):
        primes.append(checker.next_item())
    print(f'Computed {len(primes)} prime numbers')
    print(f'The last 5 are: {primes[-5:]}')
