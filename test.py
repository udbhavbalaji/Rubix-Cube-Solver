from Constraints import Colours

# class Piece:
#     def __init__(self, colour, piece_type):
#         # List of attributes in Piece
#         self.colour = colour
#         self.piece_type = piece_type
#         # self.position = init_position
#         pass
    
# class EdgePiece(Piece):
#     def __init__(self, neighbour_colour):
#         Piece.__init__(self, 'Red', 'Edge')
#         # List of attributes in EdgePiece
#         self.neighbour_colour = neighbour_colour
#         self.is_valid = True    # Have to write a method that can determine this
#         pass
    
# class CornerPiece(Piece):
#     def __init__(self, neighbour1_colour, neighbour2_colour):
#         # List of attributes in CornerPiece
#         self.neighbour1_colour = neighbour1_colour
#         self.neighbour2_colour = neighbour2_colour
#         self.is_valid = True    # Have to write a method that can determine this
#         pass
    
# class Face:
#     def __init__(self, center_colour):
#         # List of attributes in Face
#         self.center_colour = center_colour
#         self.right
#         self.left
#         self.top
#         self.bottom
#         pass
    
# class Cube:
#     def __init__(self):
#         # List of attributes in Cube
#         pass
    
#     def initialize_random_cube(self):
#         pass


# # Solving steps
# # 1. Identify Face with white center
# # 2. Identify other white edge pieces
# # 3. Create a plus sign on the white face
# # 4. Identify where the corner white pieces are
# # 5. Get them in positions to and insert them into the white face at their required positions
# # 6. Ensure that 1st layer is done

# test1 = EdgePiece('White')
# print(test1.piece_type)
    
    
# class LinkedList:
#     def __init__(self):
#         self.value = 5
        
#     def copy(self):
#         return LinkedList()
    
# lhs = LinkedList()
# rhs = lhs.copy()
# rhs.value = 10
# print(f'LHS Value = {lhs.value}\nRHS Value = {rhs.value}')

# CLRS = [Colours.BLUE, Colours.ORANGE, Colours.GREEN, Colours.RED, Colours.WHITE, Colours.YELLOW]

# for i in range(1, 5):
#     print(f'{CLRS[i-1]} - {CLRS[i]}')

# class Alphabet:
#     def __init__(self, value, next=None, prev=None):
#         self.value = value
#         self.next = next
#         self.prev = prev
        
#     def copy(self):
#         return(Alphabet(self.value, self.next, self.prev))
    
#     def output(self):
#         if self.prev is None:
#             print('\nPrev: None')
#         else:
#             print(f'\nPrev: {self.prev.value}')
#         print(f'Value: {self.value}')
#         if self.next is None:
#             print('Next: None\n')
#         else:
#             print(f'Next: {self.next.value}\n')
        
        
# a = Alphabet('A')
# b = Alphabet('B')
# c = Alphabet('C')
# d = Alphabet('D')

# e = a

# a.next = b

# b.prev = a
# b.next = c

# c.prev = b
# c.next = d

# d.prev = c
# d.next = e

# e.prev = d

# a.output()
# b.output()
# c.output()
# d.output()
# e.output()

# e.value = 'E'

# a.output()
# e.output()

# class Piece:
#     def __init__(self):
#         self.face_position = 1
        
# class CornerPiece(Piece):
#     def __init__(self):
#         Piece.__init__(self)
        
# piece = CornerPiece()
# print(piece.face_position)

import numpy as np
# from Constraints import FacePositions

class A:
    
    def __init__(self, value):
        self.value = value
    
    def get_value():
        return 'Bottom'
    
    BOTTOM = get_value()

# array = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
# matrix = array.copy()
# matrix[0,0] = 10
# print(array)
# print(matrix)
a1 = A('a1')
a2 = A('a2')
array = np.array([a1, a2])
print(array)
print(np.flip(array))
copy = array.copy()

print(copy)

# # array = np.zeros(9)
# # np.reshape(array, (1,-1))
# # array[:,0] = [10, 11, 12]
# print(array[:,FacePositions.LEFT_COL])
# print(array[FacePositions.TOP_ROW])
# array = np.array([1, 2, 3])
# print(np.flip(array))
# print(A.BOTTOM)

