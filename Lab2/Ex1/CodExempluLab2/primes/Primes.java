interface Filter {
    public boolean accept(int n);
}

class AcceptFilter implements Filter {
    public AcceptFilter() {}

    public boolean accept(int n) {
        return true;
    }
}

class DivisibleByFilter implements Filter {
    private final int number;
    private final Filter next;

    public DivisibleByFilter(int number, Filter next) {
        this.number = number;
        this.next = next;
    }

    public boolean accept(int n) {
        Filter filter = this;
        while(filter != null && filter instanceof DivisibleByFilter) {
            if(n % ((DivisibleByFilter) filter).number == 0)
                return false;
            filter = ((DivisibleByFilter) filter).next;
        }
        return true;
    }
}

class PrimeChecker {
    private int number;
    private Filter filter;

    public PrimeChecker() {
        this.number = 2;
        this.filter = new AcceptFilter();
    }

    public int next() {
        while (!this.filter.accept(this.number))
            this.number += 1;
        this.filter = new DivisibleByFilter(this.number, this.filter);
        return this.number;
    }

}

public class Primes {

    public static void main(String[] args) {
        PrimeChecker checker = new PrimeChecker();
        int[] primes = new int[5000];
        int count = 0;
        for(int i = 0; i < 5000; i++)
            primes[i] = checker.next();
        System.out.printf("Computed %d prime numbers\n", primes.length);
        System.out.print("The last five are: ");
        for(int i = 4994; i < 5000; i++)
            System.out.printf("%d ", primes[i]);
    }
}
