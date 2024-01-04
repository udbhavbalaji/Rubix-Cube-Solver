from cube_init_m import RubixCube
from constants import FacePositions, PossibleRotations, PossibleShifts
import icecream as ic
from validity_check import CubeValidity
from error import ShuffleError


def main() -> None:
    cube = RubixCube()
    print(cube)
    # print(CubeValidity.are_edge_piece_complements_correct(cube))
    # print(CubeValidity.are_corner_piece_complements_correct(cube))
    # cube.rotate(PossibleRotations.ROTATE_DOWN) # # print(cube) # cube.rotate(PossibleRotations.ROTATE_LEFT_HORIZONTALLY) # # print(cube) # cube.rotate(PossibleRotations.ROTATE_LEFT_VERTICALLY)
    # # print(cube)
    # cube.rotate(PossibleRotations.ROTATE_UP)
    # # print(cube)
    # cube.rotate(PossibleRotations.INVERT_VERTICALLY)
    # # print(cube)
    # cube.rotate(PossibleRotations.ROTATE_RIGHT_VERTICALLY)
    # # print(cube)
    # cube.rotate(PossibleRotations.INVERT_HORIZONTALLY)
    # # print(cube)
    # cube.rotate(PossibleRotations.ROTATE_RIGHT_HORIZONTALLY)
    # print(cube)
    # cube.reset_perspective()
    # print(cube)
    # cube.shift(PossibleShifts.RIGHT_COL_UP)
    # print(cube)
    error_stack = cube.shuffle_cube()
    if len(error_stack) > 0:
        raise ShuffleError(
            "One or more operations weren't successful! Shuffle operation failed!"
        )
    print(cube)
    print(cube.current_perspective.grid[FacePositions.TOP_LEFT].position)
    # for i in range(63):
    #     cube.shift(PossibleShifts.BOTTOM_ROW_LEFT)
    #     cube.shift(PossibleShifts.LEFT_COL_DOWN)
    #     #! ERROR operations
    """
    Pattern 1: TOP row left - left column up - sat
    Pattern 2: TOP row right - right column up - sat
    Pattern 3: BOTTOM row left - left column down - not sat (error)
    Pattern 4: BOTTOM row right - right column down - sat
    """
    # cube.shift(PossibleShifts.BOTTOM_ROW_LEFT)
    # cube.shift(PossibleShifts.RIGHT_COL_DOWN)
    # print(cube)
    # ic.ic(op_stack)
    # ic.ic(error_stack)


if __name__ == "__main__":
    # YOUR CODE HERE
    main()
