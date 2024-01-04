from typing import List, Union, TYPE_CHECKING
from constants import PossibleRotations, PossibleShifts
from operations import Rotations, Shifts

OP_INVERSE_MAP = {
    Rotations.rotate_down: Rotations.rotate_up,
    Rotations.rotate_up: Rotations.rotate_down,
    Rotations.rotate_left_horizontally: Rotations.rotate_right_horizontally,
    Rotations.rotate_right_horizontally: Rotations.rotate_left_horizontally,
    Rotations.rotate_left_vertically: Rotations.rotate_right_vertically,
    Rotations.rotate_right_vertically: Rotations.rotate_left_vertically,
    Rotations.invert_vertically: Rotations.invert_vertically,
    Rotations.invert_horizontally: Rotations.invert_horizontally,
    Shifts.left_col_down: Shifts.left_col_up,
    Shifts.left_col_up: Shifts.left_col_down,
    Shifts.right_col_down: Shifts.right_col_up,
    Shifts.right_col_up: Shifts.right_col_down,
    Shifts.top_row_left: Shifts.top_row_right,
    Shifts.top_row_right: Shifts.top_row_left,
    Shifts.bottom_row_left: Shifts.bottom_row_right,
    Shifts.bottom_row_right: Shifts.bottom_row_left,
}


def reverse_stack(
    stack: List[Union[PossibleShifts, PossibleRotations]]
) -> List[Union[PossibleShifts, PossibleRotations]]:
    reversed_stack = []
    for _ in range(len(stack)):
        last_op = stack.pop()
        inverse_op = OP_INVERSE_MAP[last_op]
        reversed_stack.append(inverse_op)

    return reversed_stack
