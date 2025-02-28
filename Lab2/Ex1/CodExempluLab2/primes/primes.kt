internal interface Filter {
    fun accept(n: Int): Boolean
}

internal class AcceptFilter : Filter {
    override fun accept(n: Int): Boolean {
        return true
    }
}

internal class DivisibleByFilter(private val number: Int, private val next: Filter) : Filter {
    override fun accept(n: Int): Boolean {
        var filter: Filter = this
        while (filter != null && filter is DivisibleByFilter) {
            if (n % filter.number == 0) return false
            filter = filter.next
        }
        return true
    }
}

internal class PrimeChecker {
    private var number = 2
    private var filter: Filter
    operator fun next(): Int {
        while (!filter.accept(number)) number += 1
        filter = DivisibleByFilter(number, filter)
        return number
    }

    init {
        filter = AcceptFilter()
    }
}


fun main(args: Array<String>) {
    val checker = PrimeChecker()
    val primes = IntArray(5000)
    val count = 0
    for (i in 0..4999) primes[i] = checker.next()
    println("Computed " + primes.size + " prime numbers")
    print("The last five are: ")
    for (i in 4994..4999) print("" + primes[i] + " ")
}
