public class problem09 {

    public static void main(String args[]) {

        double a, b, c, prod;

        for (int n = 2; n < 1000; n++) {
            for (int m = 1; m < n; m++) {
                a = Math.pow(n, 2) - Math.pow(m, 2);
                b = 2 * n * m;
                c = Math.pow(n, 2) + Math.pow(m, 2);

                if (a + b + c == 1000) {
                    prod = a * b * c;
                    System.out.println("Product: " + prod);
                }
            }
        }
    }
}
