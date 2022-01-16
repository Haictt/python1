class Matrix:
    def __init__(self,matrix):
        self.matrix = matrix
    # def transformMatrix(self):
    #     matrixLength = len(self.matrix[0])
    #     colLength = len(self.matrix)
    #     newArr = flatten(self.matrix)
    #     newMatrix = []
    #     for i in range(matrixLength):
    #         row = []
    #         index=i
    #         for j in range(colLength):
    #             row.append(newArr[index])
    #             index+=matrixLength
    #         newMatrix.append(row)
    #     return newMatrix
    def multiplyMatrix(self):
        matrix = self.matrix
        # newMatrix = self.transformMatrix()
        multiMatrix = []
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix)):
                row.append(multi(matrix[i],matrix[j]))
            multiMatrix.append(row)
        return multiMatrix
def multi(a,b):
    res = 0
    for i in range(len(a)):
        res += a[i]*b[i]
    return res
# def flatten(arr):
#     flat_list = [item for sublist in arr for item in sublist]
#     return flat_list

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n,m = [int(x) for x in input().split()]
        matrix = []
        for i in range(n):
            a = [int(x) for x in input().split()]
            matrix.append(a)
        clsmtrx = Matrix(matrix)
        resMatrix = clsmtrx.multiplyMatrix()
        for i in resMatrix:
            for j in i:
                print(j,end=' ')
            print('')
