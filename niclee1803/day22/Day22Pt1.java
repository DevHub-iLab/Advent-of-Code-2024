import java.util.Scanner;

public class Day22Pt1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long sum = 0;
        while (true) {
            String line = sc.nextLine();
            if (line.isEmpty()) break;
            long number = Long.parseLong(line);
            for (int i = 0; i < 2000; i++) {
                number = secretNumber(number);
            }
            sum += number;
        }
        System.out.println(sum);

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
