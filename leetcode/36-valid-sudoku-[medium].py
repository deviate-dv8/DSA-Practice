class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # checks row
        for i in range(9):
            filteredRow = list(filter(lambda x: x != ".", board[i]))
            nums = set(filteredRow)
            if len(filteredRow) != len(nums):
                return False
        # checks column
        for i in range(9):
            col = []
            for j in range(9):
                col.append(board[j][i])
            filteredCol = list(filter(lambda x: x != ".", col))
            nums = set(filteredCol)
            if len(filteredCol) != len(nums):
                return False

        startTileX = 0
        startTileY = 0
        flag = False
        # checks tiles
        while not flag:
            tileNumbers = []
            for i in range(startTileX, startTileX + 3):
                for j in range(startTileY, startTileY + 3):
                    tileNumbers.append(board[i][j])
            startTileY += 3
            if startTileY == 9 and startTileX == 6:
                flag = True
            if startTileY == 9:
                startTileX += 3
                startTileY = 0
            filteredTile = list(filter(lambda x: x != ".", tileNumbers))
            nums = set(filteredTile)
            if len(filteredTile) != len(nums):
                return False
        return True
