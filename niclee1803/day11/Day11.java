import java.util.HashMap;
import java.util.Map;

public class Day11 {
    public static void main(String[] args) {
        long[] numbers = {6563348, 67, 395, 0, 6, 4425, 89567, 739318};
        // store counts of each number to avoid duplicate processing of repeated numbers
        HashMap<Long, Long> numberCounts = new HashMap<>();
        for (long number : numbers) {
            numberCounts.put(number, numberCounts.getOrDefault(number, 0L) + 1);
        }
        for (int i = 0; i < 75; i++) {
            HashMap<Long,Long> nextCounts = new HashMap<>();
            for (Map.Entry<Long,Long> entry : numberCounts.entrySet()) {
                long number = entry.getKey();
                long count = entry.getValue();
                if (number == 0) {
                    nextCounts.put(1L, nextCounts.getOrDefault(1L, 0L) + count);
                } else if (numDigits(number) % 2 == 0) {
                    long left = getLeftHalfDigits(number);
                    long right = getRightHalfDigits(number);
                    nextCounts.put(left, nextCounts.getOrDefault(left, 0L) + count);
                    nextCounts.put(right, nextCounts.getOrDefault(right, 0L) + count);
                } else {
                    nextCounts.put(number * 2024, nextCounts.getOrDefault(number * 2024, 0L) + count);
                }
            }
            numberCounts = nextCounts;
        }
        long size = 0;
        for (long values : numberCounts.values()) {
            size += values;
        }
        System.out.println(size);
    }

    private static int numDigits(long num) {
        return (int) Math.log10(num) + 1;
    }

    private static long getRightHalfDigits(long num) {
        int digits = numDigits(num);
        int rightHalfDigits = digits / 2;
        return (long) (num % Math.pow(10, rightHalfDigits));
    }

    private static long getLeftHalfDigits(long num) {
        int digits = numDigits(num);
        int rightHalfDigits = digits / 2;
        return num / (long) Math.pow(10, rightHalfDigits);
    }
}