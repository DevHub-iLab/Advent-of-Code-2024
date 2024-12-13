import java.util.*;

public class Day12Pt2 {
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
            System.out.println("Corner " + region.corners);
            cost += (long) region.area * region.corners;
        }
        System.out.println(cost);
    }

    private static int[] exploreRegion(char[][] grid, boolean[][] visited, int row, int col, char regionChar) {
        int rows = grid.length;
        int cols = grid[0].length;
        int area = 0;
        int corners = 0;

        // Directions for moving up, down, left, right, topleft, topright, bottomleft, bottomright
        int[] dRow = {-1, 1, 0, 0, -1, -1, 1, 1};
        int[] dCol = {0, 0, -1, 1, -1, 1, -1, 1};

        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{row, col});
        visited[row][col] = true;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int currRow = current[0];
            int currCol = current[1];
            area++;

            // If top and right and top right OOB
            if (oobOrNotChar(grid, currRow + dRow[0], currCol + dCol[0], regionChar) && oobOrNotChar(grid, currRow + dRow[3], currCol + dCol[3], regionChar) && oobOrNotChar(grid, currRow + dRow[5], currCol + dCol[5], regionChar)) {
                corners++;
            }
            // if top and left and top left oob
            if (oobOrNotChar(grid, currRow + dRow[0], currCol + dCol[0], regionChar) && oobOrNotChar(grid, currRow + dRow[2], currCol + dCol[2], regionChar) && oobOrNotChar(grid, currRow + dRow[4], currCol + dCol[4], regionChar)) {
                corners++;
            }
            // if bottom and left and bottom left oob
            if (oobOrNotChar(grid, currRow + dRow[1], currCol + dCol[1], regionChar) && oobOrNotChar(grid, currRow + dRow[2], currCol + dCol[2], regionChar) && oobOrNotChar(grid, currRow + dRow[6], currCol + dCol[6], regionChar)) {
                corners++;
            }
            // if bottom and right and bottom right oob
            if (oobOrNotChar(grid, currRow + dRow[1], currCol + dCol[1], regionChar) && oobOrNotChar(grid, currRow + dRow[3], currCol + dCol[3], regionChar) && oobOrNotChar(grid, currRow + dRow[7], currCol + dCol[7], regionChar)) {
                corners++;
            }

            // if top and left not oob but top left oob
            if (!oobOrNotChar(grid, currRow + dRow[0], currCol + dCol[0], regionChar) && !oobOrNotChar(grid, currRow + dRow[2], currCol + dCol[2], regionChar) && oobOrNotChar(grid, currRow + dRow[4], currCol + dCol[4], regionChar)) {
                corners++;
            }
            // if top and right not oob but top right oob
            if (!oobOrNotChar(grid, currRow + dRow[0], currCol + dCol[0], regionChar) && !oobOrNotChar(grid, currRow + dRow[3], currCol + dCol[3], regionChar) && oobOrNotChar(grid, currRow + dRow[5], currCol + dCol[5], regionChar)) {
                corners++;
            }
            // if bottom and left not oob but bottom left oob
            if (!oobOrNotChar(grid, currRow + dRow[1], currCol + dCol[1], regionChar) && !oobOrNotChar(grid, currRow + dRow[2], currCol + dCol[2], regionChar) && oobOrNotChar(grid, currRow + dRow[6], currCol + dCol[6], regionChar)) {
                corners++;
            }
            // if bottom and right not oob but bottom right oob
            if (!oobOrNotChar(grid, currRow + dRow[1], currCol + dCol[1], regionChar) && !oobOrNotChar(grid, currRow + dRow[3], currCol + dCol[3], regionChar) && oobOrNotChar(grid, currRow + dRow[7], currCol + dCol[7], regionChar)) {
                corners++;
            }

            // if top and left oob but top left not oob
            if (oobOrNotChar(grid, currRow + dRow[0], currCol + dCol[0], regionChar) && oobOrNotChar(grid, currRow + dRow[2], currCol + dCol[2], regionChar) && !oobOrNotChar(grid, currRow + dRow[4], currCol + dCol[4], regionChar)) {
                corners++;
            }
            // if top and right oob but top right not oob
            if (oobOrNotChar(grid, currRow + dRow[0], currCol + dCol[0], regionChar) && oobOrNotChar(grid, currRow + dRow[3], currCol + dCol[3], regionChar) && !oobOrNotChar(grid, currRow + dRow[5], currCol + dCol[5], regionChar)) {
                corners++;
            }
            // if bottom and left oob but bottom left not oob
            if (oobOrNotChar(grid, currRow + dRow[1], currCol + dCol[1], regionChar) && oobOrNotChar(grid, currRow + dRow[2], currCol + dCol[2], regionChar) && !oobOrNotChar(grid, currRow + dRow[6], currCol + dCol[6], regionChar)) {
                corners++;
            }
            // if bottom and right oob but bottom right not oob
            if (oobOrNotChar(grid, currRow + dRow[1], currCol + dCol[1], regionChar) && oobOrNotChar(grid, currRow + dRow[3], currCol + dCol[3], regionChar) && !oobOrNotChar(grid, currRow + dRow[7], currCol + dCol[7], regionChar)) {
                corners++;
            }

            // BFS
            for (int i = 0; i < 4; i++) {
                int newRow = currRow + dRow[i];
                int newCol = currCol + dCol[i];
                if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols && grid[newRow][newCol] == regionChar && !visited[newRow][newCol]) {
                    queue.add(new int[]{newRow, newCol});
                    visited[newRow][newCol] = true;
                }
            }

        }

        return new int[]{area, corners};
    }

    static class Region {
        char character;
        int area;
        int corners;

        public Region(char character, int area, int corners) {
            this.character = character;
            this.area = area;
            this.corners = corners;
        }
    }

    private static boolean oobOrNotChar(char[][] grid, int i, int j, char regionChar) {
        int rows = grid.length;
        int cols = grid[0].length;
        if (i < 0 || i >= rows || j < 0 || j >= cols) {
            return true;
        } else return grid[i][j] != regionChar;
    }
}
