public class problem34 {

    public static long factorial(long num) {
        /* Can be hard coded: 1!  2!  3!  4!  5!  6!  7!  8!   9!
                              1   1   2   6   24  120 720 5040 40320
        */

        long fac = 1;

        for (long i = 1; i <= num; i++) {
            fac *= i;
        }
        return fac;
    }

    public static long factsum(long num) {

        long digit, sum = 0;

        while (num > 0) {
            digit = num % 10;
            sum += factorial(digit);
            num /= 10;
        }
        return sum;
    }

    public static void main(String args[]) {

        long sum = 0;

        // 1! and 2! don't count
        for (long num = 3; num < 1000000; num++) {
            if (factsum(num) == num) {
                sum += num;
                System.out.println("Found: " + num);
            }
        }
        System.out.println("Sum: " + sum);
    }
}
