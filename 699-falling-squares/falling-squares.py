class Solution(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        res = []
        prev_squares = []
        for i in range(len(positions)):
            left, side = positions[i]
            right = left + side
            base_height = 0
            for prev_left, prev_right, height_of_prev in prev_squares:
                if left < prev_right and right > prev_left:
                    base_height = max(base_height, height_of_prev)
            new_height = base_height + side
            res.append(max(new_height, res[-1] if res else 0))

            prev_squares.append((left, right, new_height))
        return res
        