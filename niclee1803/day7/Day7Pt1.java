import java.util.Scanner;

public class Day7Pt1 {
    public static void main(String[] args) {
        long totalSum = 0;
        Scanner sc = new Scanner(System.in);
        while (true) {
            String line = sc.nextLine();
            if (line.equalsIgnoreCase("done")) break;
            String[] parts = line.split(":");
            long result = Long.parseLong(parts[0].trim());
            String[] operandStrings = parts[1].trim().split("\\s+");
            long[] operands = new long[operandStrings.length];
            for (int i = 0; i < operandStrings.length; i++) {
                operands[i] = Long.parseLong(operandStrings[i]);
            }
            if(canOperandsEquate(result, operands)) {
                totalSum += result;
            }
        }
        System.out.println(totalSum);
    }

    private static boolean canOperandsEquate(long result, long[] operands) {
        return testOperands(result, operands, 0, operands[0]);
    }

    private static boolean testOperands(long result, long[] operands, int index, long current) {
        if (index == operands.length - 1) {
            return current == result;
        }

        long nextOperand = operands[index + 1];

        return testOperands(result, operands, index + 1, current + nextOperand) || // Addition
                testOperands(result, operands, index + 1, current * nextOperand); // Multiplication
    }
}


