public class problem10 {

    public static boolean isPrime(int num) {

        int limit = new Double(Math.sqrt(num) + 1).intValue();

        for (int i = 2; i < limit; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String args[]) {

        long sum = 1,
            max = 2000000;

        for (int i = 1; i < max; i += 2) {
            if (isPrime(i)) {
                sum += i;
            }
        }
        System.out.println("Answer found: " + sum);
    }
}
