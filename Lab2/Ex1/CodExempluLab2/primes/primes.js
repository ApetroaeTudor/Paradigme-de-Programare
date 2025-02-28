class AcceptFilter {
    accept(n) {
        return true
    }
}

class DivisibleByFilter {
    constructor(number, next) {
        this.number = number;
        this.next = next;
    }

    accept(n) {
        var filter = this;
        while (filter != null) {
            if (n % filter.number === 0) {
                return false;
            }
            filter = filter.next;
        }
        return true;
    }
}

class Primes {
    constructor() {
        this.number = 2;
        this.filter = new AcceptFilter();
    }

    next() {
        while (!this.filter.accept(this.number)) {
            this.number++;
        }
        this.filter = new DivisibleByFilter(this.number, this.filter);
        return this.number;
    }
}

var primes = new Primes();
var primesArray = [];
for (let i = 0; i < 5000; i++) {
    primesArray.push(primes.next());
}
console.log(`Computed ${primesArray.length} prime numbers. ` +
`The last 5 are ${primesArray.slice(-5)}.`);
