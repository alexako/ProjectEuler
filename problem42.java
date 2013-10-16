import java.util.ArrayList;
import java.util.List;
import java.io.*;

public class problem42 {

    public static Integer convert(String word) {

        String alpha = "abcdefghijklmnopqrstuvwxyz";
        Integer sum = 0, letterValue;
        char letter;
        boolean isAlpha = true;


        if (word.equals(",")) {
            isAlpha = false;
        }

        if (isAlpha) {
            for (int i = 0; i < word.length(); i++) {
                letter = word.toLowerCase().charAt(i);
                letterValue = (alpha.indexOf(letter)) + 1;
                sum += letterValue;
            }
        }
        return sum;
    }

    public static void main(String args[]) {

        List<Integer> triNums = new ArrayList<Integer>();
        Integer triNum, counter = 0;
        String word;

        // Create list of triangle numbers
        for (Integer i = 1; i < 20; i++) {
            triNum = (i * (i+1))/2;
            triNums.add(triNum);
        }

        // Read and check if word value is a triangle number
        try {
            File file = new File("42.txt");
            BufferedReader buffer = new BufferedReader(new FileReader(file));
            String line = null;
            String [] tokens = null;

            // Read words into tokens string array
            while ((line = buffer.readLine()) != null) {
                tokens = line.split("\"*\"");
            }

            // Iterate through words and compare
            for (int i = 0; i < tokens.length; i++) {
                word = tokens[i];

                if (triNums.contains(convert(word))) {
                    counter += 1;
                }
            }
        }
        catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println("Answer found: " + counter);
    }
}
