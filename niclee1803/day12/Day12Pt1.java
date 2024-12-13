import java.util.*;

public class Day12Pt1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder inputStringBuilder = new StringBuilder();

        while (true) {
            String line = sc.nextLine();
            if (line.equals("done")) break; // done to signify end of input
            inputStringBuilder.append(line).append("\n");
        }

        String[] lines = inputStringBuilder.toString().split("\n");
        int rows = lines.length;
        int cols = lines[0].length();

        char[][] grid = new char[rows][cols];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                grid[i][j] = lines[i].charAt(j);
            }
        }

        boolean[][] visited = new boolean[rows][cols];
        List<Region> regions = new ArrayList<>(); 



        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (!visited[i][j]) {
                    char regionChar = grid[i][j];
                    int[] properties = exploreRegion(grid, visited, i, j, regionChar);
                    regions.add(new Region(regionChar, properties[0], properties[1]));
                }
            }
        }

        long cost = 0;

        for (Region region : regions) {
            System.out.println(region.character);
            System.out.println("Area " + region.area);
            System.out.println("Perimeter " + region.perimeter);
            cost += (long) region.area * region.perimeter;
        }
        System.out.println(cost);
    }

    private static int[] exploreRegion(char[][] grid, boolean[][] visited, int row, int col, char regionChar) {
        int rows = grid.length;
        int cols = grid[0].length;
        int area = 0;
        int perimeter = 0;

        // Directions for moving up, down, left, right
        int[] dRow = {-1, 1, 0, 0};
        int[] dCol = {0, 0, -1, 1};

        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{row, col});
        visited[row][col] = true;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int currRow = current[0];
            int currCol = current[1];
            area++;

            // Check all 4 directions BFS
            for (int i = 0; i < 4; i++) {
                int newRow = currRow + dRow[i];
                int newCol = currCol + dCol[i];

                if (newRow < 0 || newRow >= rows || newCol < 0 || newCol >= cols) {
                    perimeter++;
                } else if (grid[newRow][newCol] != regionChar) {
                    perimeter++;
                } else if (!visited[newRow][newCol]) {
                    queue.add(new int[]{newRow, newCol});
                    visited[newRow][newCol] = true;
                }
            }
        }

        return new int[]{area, perimeter};
    }

    static class Region {
        char character;
        int area;
        int perimeter;

        public Region(char character, int area, int perimeter) {
            this.character = character;
            this.area = area;
            this.perimeter = perimeter;
        }
    }
}
