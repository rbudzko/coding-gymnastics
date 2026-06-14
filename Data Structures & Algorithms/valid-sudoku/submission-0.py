class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_nums = {}
        cell_nums = {}
        box_nums = {}
        
        for row_idx in range(0, len(board)):
            for cell_idx in range(0, len(board[row_idx])):
                num = board[row_idx][cell_idx]
                if num == '.': continue

                rn = row_nums.setdefault(row_idx, set())
                cn = cell_nums.setdefault(cell_idx, set())

                if num in rn or num in cn:
                    return False
                
                rn.add(num)
                cn.add(num)

                box_hash = (row_idx // 3, cell_idx // 3)
                bn = box_nums.setdefault(box_hash, set())

                if num in bn:
                    return False

                bn.add(num)

        return True                

                

        