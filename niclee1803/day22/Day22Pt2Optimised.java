import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Day22Pt2Optimised {
    private static final int SEQUENCE_LENGTH = 4;
    private static final int REQUIRED_LENGTH = 2000;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<int[]> sequences = new ArrayList<>();


        while (true) {
            String line = sc.nextLine();
            if (line.isEmpty()) break;
            sequences.add(generateSequence(Long.parseLong(line)));
        }

        System.out.println(findMaxPrice(sequences));
    }

    private static int[] generateSequence(long initialNumber) {
        int[] sequence = new int[REQUIRED_LENGTH];
        long number = initialNumber;

        for (int i = 0; i < REQUIRED_LENGTH; i++) {
            sequence[i] = (int) (number % 10);
            number = secretNumber(number);
        }

        return sequence;
    }

    private static int findMaxPrice(ArrayList<int[]> sequences) {

        Map<String, Integer> patternPrices = new HashMap<>();


        for (int[] sequence : sequences) {

            Map<String, Integer> seenPatterns = new HashMap<>();

            for (int i = SEQUENCE_LENGTH; i < REQUIRED_LENGTH; i++) {

                StringBuilder pattern = new StringBuilder();
                for (int j = 0; j < SEQUENCE_LENGTH; j++) {
                    if (j > 0) pattern.append(",");
                    pattern.append(sequence[i - j] - sequence[i - j - 1]);
                }
                String patternKey = pattern.toString();


                if (!seenPatterns.containsKey(patternKey)) {
                    seenPatterns.put(patternKey, sequence[i]);
                    patternPrices.merge(patternKey, sequence[i], Integer::sum);
                }
            }
        }

        return patternPrices.values().stream()
                .mapToInt(Integer::intValue)
                .max()
                .orElse(0);
    }

    private static long secretNumber(long number) {
        long secretNumber = number;
        number *= 64;
        number = mix(secretNumber, number);
        number = prune(number);
        secretNumber = number;
        number /= 32;
        number = mix(secretNumber, number);
        number = prune(number);
        secretNumber = number;
        number *= 2048;
        number = mix(secretNumber, number);
        number = prune(number);
        return number;
    }

    private static long mix(long secretNumber, long number) {
        return secretNumber ^ number;
    }

    private static long prune(long number) {
        return number % 16777216;
    }
}