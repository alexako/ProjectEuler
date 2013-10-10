public class problem07 {

    public static boolean isPrime(Integer num) {

        double limit = Math.sqrt(num) + 1;

        for (double i = 2; i < limit; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main (String args[]) {

        Integer counter = 0,
                num = 0,
                target = 10000;

        while (counter <= target) {
            num += 1;
            if (isPrime(num)) {
                counter += 1;
                System.out.println(counter + ": " + num);
            }
        }

        System.out.println("Answer found: " + num);

    }

}
