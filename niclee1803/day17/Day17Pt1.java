import java.util.ArrayList;
import java.util.Scanner;

public class Day17Pt1 {
    static long regA;
    static long regB;
    static long regC;

    public static void main(String[] args) {


        Scanner sc = new Scanner(System.in);

        regA = Long.parseLong(sc.nextLine().split(": ")[1].trim());

        regB = Long.parseLong(sc.nextLine().split(": ")[1].trim());

        regC = Long.parseLong(sc.nextLine().split(": ")[1].trim());

        sc.nextLine();

        String programInput = sc.nextLine().split(": ")[1].trim();
        String[] programNumbers = programInput.split(",");

        int[] program = new int[programNumbers.length];

        ArrayList<Long> outputs = new ArrayList<>();

        for (int i = 0; i < programNumbers.length; i++) {
            program[i] = Integer.parseInt(programNumbers[i].trim());
        }

        for (int i = 0; i < program.length; i += 2) {
            switch (program[i]) {
                case 0 -> {
                    long numerator = regA;
                    long denom = (long) Math.pow(2, comboOperand(program[i + 1]));
                    regA = numerator / denom;
                }
                case 1 -> {
                    regB ^= program[i + 1];
                }
                case 2 -> {
                    regB = comboOperand(program[i + 1]) % 8;
                }
                case 3 -> {
                    if (regA != 0) {
                        i = program[i + 1] - 2;
                    }
                }
                case 4 -> {
                    regB = regB ^ regC;
                }
                case 5 -> {
                    outputs.add(comboOperand(program[i + 1]) % 8);
                }
                case 6 -> {
                    long numerator = regA;
                    long denom = (long) Math.pow(2, comboOperand(program[i + 1]));
                    regB = numerator / denom;
                }
                case 7 -> {
                    long numerator = regA;
                    long denom = (long) Math.pow(2, comboOperand(program[i + 1]));
                    regC = numerator / denom;
                }
            }
        }
        for (int i = 0; i < outputs.size(); i++) {
            System.out.print(outputs.get(i) + ",");
        }
    }


    private static long comboOperand(int operand) {
        if (operand == 1 || operand == 2 || operand == 3) {
            return operand;
        }
        if (operand == 4) return regA;
        if (operand == 5) return regB;
        if (operand == 6) return regC;
        return -1;
    }

}
