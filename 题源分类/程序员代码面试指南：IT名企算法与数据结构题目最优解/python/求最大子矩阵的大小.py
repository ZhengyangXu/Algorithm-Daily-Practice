# 【题目】给定一个整型矩阵map，其中的值只有0和1两种，
# 求其中全是1的所有矩形区域中，最大的矩形区域为1的数量。
# 例如：[插图]其中，最大的矩形区域有3个1，所以返回3。
# 再如：[插图]其中，最大的矩形区域有6个1，所以返回6。【难度】校 ★★★☆


def maxRecFromBottom(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    height = [0] * cols
    for row in range(rows):
        for col in range(cols):
            height[col] = height[col] + 1 if matrix[row][col] != 0 else 0

    stack = []
    maxArea = float('-inf')
    for i in range(len(height)):
        while stack and height[i] <= height[stack[-1]]:
            cur = stack.pop()
            k = -1 if not stack else stack[-1]
            maxArea = max(maxArea, height[cur] * (i - k - 1))
        stack.append(i)

    while stack:
        cur = stack.pop()
        k = -1 if stack else stack[-1]
        curArea = (i - k - 1) * height[cur]
        maxArea = max(maxArea, curArea)

    return maxArea


if __name__ == "__main__":

    matrix = [[1, 0, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0]]

    print(maxRecFromBottom(matrix))
