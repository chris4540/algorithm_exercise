public class Percolation {

    // we use a 2d-array to represent the percolation grid
    private boolean [][] grid;

    // the number of open sites
    private int numOpenSites = 0;

    /*
        creates n-by-n grid, with all sites initially blocked
    */
    public Percolation(int n){
        if (n < 1){
            throw new IllegalArgumentException(
                "the size of the grid should be greater then 0");
        }

        // initialize the grid with traditional nested for loop
        grid = new boolean[n][n];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                // Initialize all sites to be blocked
                grid[i][j] = false;
            }
        }
    }

    // opens the site (row, col) if it is not open already
    public void open(int row, int col){
        grid[row][col] = true;
        numOpenSites += 1
    }

    // is the site (row, col) open?
    public boolean isOpen(int row, int col){
        return grid[row][col];
    }

    // is the site (row, col) full?
    public boolean isFull(int row, int col){

    }

    // returns the number of open sites
    public int numberOfOpenSites(){
        return numOpenSites;
    }

    // does the system percolate?
    // public boolean percolates()

    // test client (optional)
    public static void main(String[] args){
        int size = Integer.parseInt(args[0]);
        Percolation percolation = new Percolation(size);

        int row = 3;
        int col = 2;
        boolean isGridOpen = percolation.isOpen(row, col);
        System.out.format("the grid(%d, %d) open = %b \n", row, col, isGridOpen);
    }
}
