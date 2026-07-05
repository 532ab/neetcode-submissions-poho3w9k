class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        
        # Loop through every single cell in the 9x9 grid
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # If the cell is empty ('.'), skip it
                if val == '.':
                    continue
                
                # Create unique string formulas representing where we saw this number
                row_key = f"{val} in row {r}"
                col_key = f"{val} in col {c}"
                box_key = f"{val} in box {r // 3}-{c // 3}"
                
                # If any of these unique descriptions are already in our set, it's a duplicate!
                if row_key in seen or col_key in seen or box_key in seen:
                    return False
                
                # Otherwise, add them to our history and keep moving
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)
                
        return True