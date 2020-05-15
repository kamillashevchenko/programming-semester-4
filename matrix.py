"""
program matrix
"""
import copy


class Matrix:
    """
    class matrix
    """
    @staticmethod
    def _check_dimensions(mat, mat_str, mat_clm):
        if len(mat) != mat_str:
            raise Exception("Invalid matrix height, expected="\
                             + str(mat_str) + ", actual=" + str(len(mat)))
        for i, val in enumerate(mat):
            if len(val) != mat_clm:
                raise Exception("Invalid matrix width, expected="\
                             + str(mat_clm) + ", actual=" + str(len(val)))

    def __init__(self, mat_str, mat_clm, val=None):
        if val is None:
            self.val = [[0] * mat_str] * mat_clm
        else:
            Matrix._check_dimensions(val, mat_str, mat_clm)
            self.val = copy.deepcopy(val)

    def __add__(self, other):
        self._check_argument(other)
        new_mat = Matrix(self.get_m(), self.get_n(), self.val)
        for i, row in enumerate(other):
            for j, row_val in enumerate(row):
                new_mat.val[i][j] += row_val
        return new_mat

    def __sub__(self, other):
        self._check_argument(other)
        new_mat = Matrix(self.get_m(), self.get_n(), self.val)
        for i, row in enumerate(other):
            for j, row_val in enumerate(row):
                new_mat.val[i][j] -= row_val
        return new_mat

    def __iter__(self):
        return iter(self.val)

    def __getitem__(self, item):
        return self.val[item]

    def __setitem__(self, key, value):
        self.val[key] = value

    def __mul__(self, other):
        if isinstance(other, int):
            new_mat = Matrix(self.get_m(), self.get_n(), self.val)
            for i, row in enumerate(new_mat.val):
                for j in range(len(row)):
                    new_mat.val[i][j] *= other
            return new_mat
        if isinstance(other, Matrix):
            if self.get_n() != other.get_m():
                raise Exception("Invalid dimensions for matrix product")
            new_mat = Matrix(self.get_m(), other.get_n())
            for i in range(new_mat.get_m()):
                for j in range(new_mat.get_n()):
                    res = 0
                    for k in range(self.get_n()):
                        res += self[i][k] * other[k][j]
                    new_mat[i][j] = res
            return new_mat
        raise Exception(
            "Invalid type of argument, expected " + str(Matrix) + " or "\
             + str(int) + ", actual=" + str(type(other)))

    def __neg__(self):
        return self * -1

    def __str__(self):
        return str(self.val)

    def get_m(self):
        """
        get quantity of strings
        """
        return len(self.val)

    def get_n(self):
        """
        get quantity of columns
        """
        return len(self.val[0])

    def _check_argument(self, other):
        if self.get_n() != other.get_n() or self.get_m() != other.get_m():
            raise Exception("Invalid dimensions")


if __name__ == '__main__':
    A = Matrix(1, 2, [[1, 2]])
    B = Matrix(1, 2, [[5, 6]])
    C = Matrix(2, 1, [[5], [6]])
    print(A - B)
    print(A + B)
    print(A * C)
    print(A * -2)
