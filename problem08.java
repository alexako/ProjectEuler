import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class problem08 {

    // Read file
    public static String readFile(String filename) {
        String content = null;
        File file = new File(filename);
        try {
            FileReader reader = new FileReader(file);
            char[] chars = new char[(int) file.length()];
            reader.read(chars);
            content = new String(chars);
            reader.close();
        }
        catch (IOException e) {
            e.printStackTrace();
        }
        return content;
    }

    public static int findProd(String num) {
        int product = 1;
        for (int i = 0; i < num.length(); i++) {
            product *= Character.getNumericValue(num.charAt(i));
        }
        return product;
    }

    public static void main (String args[]) {

        int prod, largest = 0;

        //Read numbers from 08.txt
        String numbers = readFile("08.txt");

        //Find largest product
        for (int i = 0; i < numbers.length()-5; i++) {
            String buffer = numbers.substring(i, i+5);
            prod = findProd(numbers.substring(i, i+5));

            System.out.println("Multiplying " + buffer);
            System.out.println("Product: " + prod);

            if (prod > largest) {
                largest = prod;
            }
        }

        System.out.println("\nLargest product: " + largest);
    }
}
