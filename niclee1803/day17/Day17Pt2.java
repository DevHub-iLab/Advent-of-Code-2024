import java.util.ArrayList;
import java.util.List;

public class Day17Pt2 {
    static long[] program = new long[]{2,4,1,4,7,5,4,1,1,4,5,5,0,3,3,0};

    static long regA;
    static long regB;
    static long regC;

    public static void main(String[] args) {
        System.out.println(getLeastA(0, program.length - 1));
    }

    private static long comboOperand(long operand) {
        if (operand == 1 || operand == 2 || operand == 3) {
            return operand;
        }
        if (operand == 4) return regA;
        if (operand == 5) return regB;
        if (operand == 6) return regC;
        return -1;
    }

    private static List<Long> runProgram(long initialA) {
        List<Long> outputs = new ArrayList<>();
        regA = initialA;
        regB = 0;
        regC = 0;
        for (int i = 0; i < program.length; i += 2) {
            switch ((int) program[i]) {
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
                        i = (int) (program[i + 1] - 2);
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
        return outputs;
    }

    private static boolean outputsMatch(List<Long> outputs, int startIndex) {
        if (outputs.size() != program.length - startIndex) return false;
        for (int i = 0; i < outputs.size(); i++) {
            if (outputs.get(i) != program[startIndex + i]) return false;
        }
        return true;
    }

    private static long getLeastA(long soFar, int programIndex) {
        for (int i = 0; i < 8; i++) {
            long candidate = soFar * 8 + i;
            List<Long> outputs = runProgram(candidate);
            if (outputsMatch(outputs, programIndex)) {
                if (programIndex == 0) {
                    return candidate;
                }
                long result = getLeastA(candidate, programIndex - 1);
                if (result != -1) {
                    return result;
                }
            }
        }
        return -1;
    }
}