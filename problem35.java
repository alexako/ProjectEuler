import java.util.ArrayList;

public class problem35 {

    public static boolean isPrime(int num) {

        int limit = new Double(Math.sqrt(num) + 1).intValue();

        for (long i = 2; i < limit; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static String rotate(String num, Integer numSize) {

        String rotated;

        if (numSize == 1) {
            return num;
        }

        // Rotate array
        rotated = num.substring(1, numSize) + num.charAt(0);

        return rotated;
    }

    public static void main(String args[]) {

        Integer limit = 1000000,
            counter = 0,
            numLength;

        String test;

        boolean prime = false;

        // Loop through numbers
        for (int i = 2; i < limit; i++) {
            test = Integer.toString(i);
            numLength = test.length();

            // Loop through rotations
            for (int j = 0; j < numLength; j++) {
                if (isPrime(Integer.parseInt(test))) {
                    test = rotate(test, numLength);
                    prime = true;
                }
                else {
                    prime = false;
                    break;
                }
            }
            if (prime) {
                counter += 1;
            }
        }
    System.out.println("Answer found: " + counter);
    }
}
