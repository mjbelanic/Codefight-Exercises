bool CheckRows(char[] row){
    Dictionary<char, int> charList = new Dictionary<char, int>();
    for(int i = 0; i < row.Length; i++){
        if(charList.ContainsKey(row[i])){
            return false;
        }
        if(row[i] != '.'){
            charList.Add(row[i] , 1);
        }
    }
    return true;
}

char[][] rotateGrid(char[][] a) {
    int n = a.Length;
    for(int i = 0; i < n/2 ; i++){
        for(int j = 0; j < Math.Ceiling(((double) n) / 2 ); j++){
            char temp = a[i][j];
            a[i][j] = a[n-1-j][i]; 
            a[n-1-j][i] = a[n-1-i][n-1-j]; 
            a[n-1-i][n-1-j] = a[j][n-1-i]; 
            a[j][n-1-i] = temp; 
        }
    }
    return a;
}


bool BoxChecker(char[][] grid){
    for (int block = 0; block < 9; block++) {
		bool[] m = new bool[9];
		for (int i = block / 3 * 3; i < block / 3 * 3 + 3; i++) {
			for (int j = block % 3 * 3; j < block % 3 * 3 + 3; j++) {
				if (grid[i][j] != '.') {
					if (m[(int) (grid[i][j] - '1')]) {
						return false;
					}
					m[(int) (grid[i][j] - '1')] = true;
				}
			}
		}
	}
	return true;
}

bool sudoku2(char[][] grid) {
    bool RowsWork = true;
    bool ColsWork = true;
    bool BoxesWork = true;
    // Check rows
    for(int i = 0; i < grid.GetLength(0); i++){
        RowsWork = CheckRows(grid[i]);
        if(!RowsWork){
            break;
        }
    }
    // Rotate Grid
    rotateGrid(grid);
    
    // Check col
    for(int i = 0; i < grid.GetLength(0); i++){
        ColsWork = CheckRows(grid[i]);
        if(!ColsWork){
            break;
        }
    }
    // Check 3x3
    BoxesWork = BoxChecker(grid);
    
    // All Criteria is passed?
    if(RowsWork && ColsWork && BoxesWork){
        return true;
    }else{
        return false;
    }
}