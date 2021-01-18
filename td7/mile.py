from math import sqrt

class DimensionError(Exception):
    def __init__(self, message):
        self.message = message
class Matrix:
    def __init__(self, value):
        self.value = value
        self.lines = len(value)

        columnsArray = []
        for i in range(self.lines):
            columnsArray.append(len(value[i]))
        
        for i in range(1, self.lines):
            if columnsArray[i] != columnsArray[i-1]:
                raise DimensionError("Matrix is irregular hence cannot exist")
        
        self.columns = columnsArray[0]

        if self.lines == self.columns:
            self.__class__ = SquareMatrix
            self.__init__(self.value)
    def __str__(self):
        output = ""

        for i in range(len(self.value)):
            output += "[ "
            for j in self.value[i]:
                output += str(j) + " "
            output += "]\n"

        return output
    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.lines == other.lines and self.columns == other.columns:
                output = []
                for i in range(self.lines):
                    output.append([])
                    for j in range(self.columns):
                        output[i].append(self.value[i][j] + other.value[i][j])
                return Matrix(output)
            else:
                raise DimensionError("Different numbers of lines and columns in operands matrices")
        else:
            raise TypeError
    def __iadd__(self, other):
        return self+other
    def transpose(self):
        "Returns the transposed matrix"
        tempOutput = []
        for i in range(self.lines):
            for j in range(self.columns):
                tempOutput.append(self.value[i][j])
        output = []
        for i in range(self.columns):
            output.append([])
            for j in range(self.lines):
                output[i].append(tempOutput[i+(j*self.columns)])
        return Matrix(output)
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            output = []
            for i in range(self.lines):
                output.append([])
                for j in range(len(self.value[i])):
                    output[i].append(self.value[i][j] * other)
            return Matrix(output)
        else:
            return NotImplemented
    def __imul__(self, other):
        return self*other
    def __rmul__(self, other):
        return self*other
    def __rimul__(self, other):
        return self*other
    def __matmul__(self, other):
        if isinstance(other, Matrix):
            if self.columns == other.lines:
                output = []
                for i in range(self.lines):
                    output.append([])
                    for j in range(other.columns):
                        futureOutput = 0
                        for k in range(self.columns):
                            futureOutput += self.value[i][k] * other.value[k][j]
                        output[i].append(futureOutput)
                return Matrix(output)
            else:
                raise DimensionError("Different numbers of lines and columns in operands matrices")
        else:
            return NotImplemented
    def __rmatmul__(self, other):
        return self@other
    def __imatmul__(self, other):
        return self@other
    def __rimatmul__(self, other):
        return self@other
    def __truediv__(self, other):
        return self*(1/other)
    def __rtruediv__(self, other):
        return self*(1/other)
    def __idiv__(self, other):
        return self*(1/other)
    def __ridiv__(self, other):
        return self*(1/other)
    def hamadard(self, other):
        if isinstance(other, Matrix):
            if self.lines == other.lines and self.columns == other.columns:
                output = []
                for i in range(self.lines):
                    output.append([])
                    for j in range(len(self.value[i])):
                        output[i].append(self.value[i][j] * other.value[i][j])
                return Matrix(output)
            else:
                raise DimensionError("Different numbers of lines and columns in operands matrices")
        else:
            return NotImplemented
    def kronecker(self, other):
        if isinstance(other, Matrix):
            output = []
            tempOutput = []
            for i in range(self.lines * other.lines):
                output.append([])
            for i in range(self.lines):
                for j in range(self.columns):
                    for k in range(other.lines):
                        for l in range(other.columns):
                            tempOutput.append(self.value[i][j] * other.value[k][l])
            for i in range(len(tempOutput)):
                if i % sqrt(len(tempOutput)) >= sqrt(len(tempOutput)) // 2:
                    output[i // len(tempOutput) + 1 + self.lines // 2].append(tempOutput[i])
                else:
                    output[i // len(tempOutput) + self.lines // 2].append(tempOutput[i])
            return Matrix(output)

        else:
            return NotImplemented
    def __neg__(self):
        return self*(-1)
    def augment(self, other):
        if isinstance(other, Matrix):
            if self.lines == other.lines:
                output = self.value
                for i in range(other.lines):
                    for j in range(other.columns):
                        output[i].append(other.value[i][j])
                return Matrix(output)
            else:
                raise DimensionError("Different numbers of lines and columns in operands matrices")
        else:
            return NotImplemented
class SquareMatrix(Matrix):
    def __init__(self, value):
        self.value = value
        self.lines = len(value)
        columnsArray = []
        for i in range(self.lines):
            columnsArray.append(len(value[i]))
        for i in range(1, self.lines):
            if columnsArray[i] != columnsArray[i-1]:
                raise DimensionError("Matrix is irregular hence cannot exist")
        self.columns = columnsArray[0]
        if self.lines != self.columns:
            raise DimensionError("Square matrix has different number of lines and columns")
        det1, det2 = self.value[0][0], self.value[self.lines-1][0]
        for i in range(self.lines):
            if i != 0:
                det1 *= self.value[i][i]
                det2 *= self.value[self.lines-i-1][i]
        self.determinant = det1 - det2
        output = 0
        for i in range (self.lines):
            output += self.value[i][i]
        self.trace = output
    
    def invert(self):
        if self.lines == 2:
            output = self
            output.value[0][1] = -output.value[0][1]
            output.value[1][0] = -output.value[1][0]
            output *= 1/self.determinant
            return Matrix(output.value)
        if self.lines == 3:
            cofactor = []
            for i in range(3):
                cofactor.append([])
                for _ in range(3):
                    cofactor[i].append(0)
            cofactor[0][0] = self.value[1][1] * self.value[2][2] - self.value[1][2] * self.value[2][1]
            cofactor[0][1] = -(self.value[0][1] * self.value[2][2] - self.value[0][2] * self.value[2][1])
            cofactor[0][2] = self.value[0][1] * self.value[1][2] - self.value[0][2] * self.value[1][1]
            cofactor[1][0] = -(self.value[1][0] * self.value[2][2] - self.value[1][2] * self.value[2][0])
            cofactor[1][1] = self.value[0][0] * self.value[2][2] - self.value[0][2] * self.value[2][0]
            cofactor[1][2] = -(self.value[0][0] * self.value[2][1] - self.value[0][1] * self.value[2][0])
            cofactor[2][0] = self.value[1][0] * self.value[2][1] - self.value[1][1] * self.value[2][0]
            cofactor[2][1] = -(self.value[0][0] * self.value[1][2] - self.value[0][2] * self.value[1][0])
            cofactor[2][2] = self.value[0][0] * self.value[1][1] - self.value[0][1] * self.value[1][0]
            cofactor = Matrix(cofactor)
            return SquareMatrix((cofactor * (1/self.determinant)).value)
    
    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self*(1/other)
        
        if isinstance(other, SquareMatrix):
            if self.lines == other.lines:
                return self*(other.invert())

    def __rtruediv__(self, other):
        return self/other
    
    def __idiv__(self, other):
        return self/other

    def __ridiv__(self, other):
        return self/other

codingTable = SquareMatrix([[1, 3], [2, 8]])
codingTable2 = pow(codingTable.determinant, -1, 255) * codingTable.transpose()
print(codingTable2)



""" codage = input("Decoding ? [Y/N]: ")
if codage.lower() in ["y", "yes"]:
    codingTable = SquareMatrix([[4, 126], [254, 128]])

characters = [ord(i) for i in input("Enter a message to encode: ")]
if len(characters) % codingTable.columns != 0:
    for i in range(len(characters) % codingTable.columns):
        characters.append(ord(" "))

charactersTables = []
for i in range(len(characters) // codingTable.columns):
    charactersTables.append(Matrix([characters[i*codingTable.columns:codingTable.columns*(i+1)]]).transpose())

for i in range(len(charactersTables)):
    charactersTables[i] = codingTable @ charactersTables[i]
    for j in range(len(charactersTables[i].value)):
        for k in range(len(charactersTables[i].value[j])):
            charactersTables[i].value[j][k] %= 255

finalChain = []
for i in charactersTables:
    for j in i.value:
        for k in j:
            finalChain.append(k)

finalChain = [chr(int(i)) for i in finalChain]

print("".join(finalChain)) """