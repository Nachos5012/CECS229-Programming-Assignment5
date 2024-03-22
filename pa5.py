from vec import Vec


class Matrix:

  def __init__(self, rowsp):
    self.rowsp = rowsp
    self.colsp = self._construct_colsp(rowsp)

  def set_row(self, i, new_row):
    if len(self.rowsp[0]) != len(new_row):
      raise ValueError("Incompatible row length.")
    self.rowsp[i-1] = new_row
    self.colsp = self._construct_colsp(self.row_space())

  def set_col(self, j, new_col):
    if len(self.colsp[0]) != len(new_col):
      raise ValueError("Incompatible column length.")
    self.colsp[j-1] = new_col
    self.rowsp = self._construct_rowsp(self.col_space())

  def set_entry(self, i, j, val):
    if not (1 <= i <= len(self.row_space())) or not (1 <= j <= len(self.col_space())):
      raise IndexError
    self.rowsp[i-1][j-1] = self.colsp[j-1][i-1] = val

  def get_row(self, i):
    if len(self.row_space()) < i:
      raise IndexError
    return self.rowsp[i-1]

  def get_col(self, j):
    if len(self.col_space()) < j:
      raise IndexError
    return self.colsp[j-1]

  def get_entry(self, i, j):
    if not (1 <= i <= len(self.row_space())) or not (1 <= j <= len(self.col_space())):
      raise IndexError
    return self.rowsp[i-1][j-1]

  def col_space(self):
    return self.colsp

  def row_space(self):
    return self.rowsp

  def get_diag(self, k):
    r = []
    i = 0
    try:
      while True:
        r.append(self.rowsp[i][i+k] if k >= 0 else self.rowsp[i+abs(k)][i])
        i += 1
    except IndexError:
      return r

  def _construct_colsp(self, rowsp):
    return [[rowsp[j][i] for j in range(len(rowsp))] for i in range(len(rowsp[0]))]

  def _construct_rowsp(self, colsp):
    return [[colsp[j][i] for j in range(len(colsp))] for i in range(len(colsp[0]))]

  def __add__(self, other):
    if len(self.row_space()) != len(other.row_space()) or len(self.col_space()) != len(other.col_space()):
      raise ValueError
    return Matrix([[self.rowsp[i][j] + other.rowsp[i][j] for j in range(len(other.rowsp[0]))] for i in range(len(other.rowsp))])

  def __sub__(self, other):
    if len(self.row_space()) != len(other.row_space()) or len(self.col_space()) != len(other.col_space()):
      raise ValueError
    return Matrix([[self.rowsp[i][j] - other.rowsp[i][j] for j in range(len(other.rowsp[0]))] for i in range(len(other.rowsp))])

  def __mul__(self, other):
    if type(other) == float or type(other) == int:
      return Matrix([[n * other for n in row] for row in self.row_space()])
    elif type(other) == Matrix:
      if len(self.col_space()) != len(other.row_space()):
        raise ValueError
      r = []
      for row in self.row_space():
        r.append([[row[i] * col[i] for i in range(len(col))] for col in other.col_space()])
      return Matrix([[sum(cur_row) for cur_row in row] for row in r])
    elif type(other) == Vec:
      if len(self.col_space()) != len(other.elements):
        raise ValueError
      r = []
      for row in self.row_space():
        r.append([row[i] * other.elements[i] for i in range(len(other.elements))])
      return Vec([sum(e) for e in r])
    else:
      print("ERROR: Unsupported Type.")
    return

  def __rmul__(self, other):
    if type(other) == float or type(other) == int:
      return Matrix([[n * other for n in row] for row in self.row_space()])
    else:
      print("ERROR: Unsupported Type.")
    return

  '''-------- ALL METHODS BELOW THIS LINE ARE FULLY IMPLEMENTED -------'''

  def __str__(self):
    """prints the rows and columns in matrix form """
    mat_str = ""
    for row in self.rowsp:
      mat_str += str(row) + "\n"
    return mat_str

  def __eq__(self, other):
    """overloads the == operator to return True if 
      two Matrix objects have the same row space and column space"""
    return self.row_space() == other.row_space() and self.col_space(
    ) == other.col_space()

  def __req__(self, other):
    """overloads the == operator to return True if 
      two Matrix objects have the same row space and column space"""
    return self.row_space() == other.row_space() and self.col_space(
    ) == other.col_space()