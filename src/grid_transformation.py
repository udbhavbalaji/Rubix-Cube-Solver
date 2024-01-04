from __future__ import annotations
from typing import Protocol, TYPE_CHECKING
from constants import FacePositions
import numpy as np

if TYPE_CHECKING:
    from cube_init_m import Face


def update_piece_positions(face: Face) -> None:
    top_left_piece = face.grid[FacePositions.TOP_LEFT]
    top_center_piece = face.grid[FacePositions.TOP_CENTER]
    top_right_piece = face.grid[FacePositions.TOP_RIGHT]
    mid_left_piece = face.grid[FacePositions.MID_LEFT]
    mid_center_piece = face.grid[FacePositions.MID_CENTER]
    mid_right_piece = face.grid[FacePositions.MID_RIGHT]
    bottom_left_piece = face.grid[FacePositions.BOTTOM_LEFT]
    bottom_center_piece = face.grid[FacePositions.BOTTOM_CENTER]
    bottom_right_piece = face.grid[FacePositions.BOTTOM_RIGHT]

    top_left_piece.face_position = FacePositions.TOP_LEFT
    top_center_piece.face_position = FacePositions.TOP_CENTER
    top_right_piece.face_position = FacePositions.TOP_RIGHT
    mid_left_piece.face_position = FacePositions.MID_LEFT
    mid_center_piece.face_position = FacePositions.MID_CENTER
    mid_right_piece.face_position = FacePositions.MID_RIGHT
    bottom_left_piece.face_position = FacePositions.BOTTOM_LEFT
    bottom_center_piece.face_position = FacePositions.BOTTOM_CENTER
    bottom_right_piece.face_position = FacePositions.BOTTOM_RIGHT

    top_left_piece.face = face
    top_center_piece.face = face
    top_right_piece.face = face
    mid_left_piece.face = face
    mid_center_piece.face = face
    mid_right_piece.face = face
    bottom_left_piece.face = face
    bottom_center_piece.face = face
    bottom_right_piece.face = face


class GridTransformationProtocol(Protocol):
    # YOUR CODE HERE
    def transform_front_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        ...

    def transform_back_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        ...

    def transform_left_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        ...

    def transform_right_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        ...

    def transform_top_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        ...

    def transform_bottom_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        ...


class RotateUp:
    # YOUR CODE HERE
    def transform_front_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        return current_front.grid

    def transform_back_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        back_face = current_front.opposite.copy()
        old_face = back_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        back_face.grid[:, FacePositions.LEFT_COL] = np.flip(old_right_col)
        back_face.grid[:, FacePositions.RIGHT_COL] = np.flip(old_left_col)
        back_face.grid[FacePositions.TOP_ROW] = np.flip(old_bottom_row)
        back_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_top_row)

        update_piece_positions(back_face)

        return back_face.grid

    def transform_left_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        left_face = current_front.left.copy()
        old_face = left_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        left_face.grid[:, FacePositions.RIGHT_COL] = np.flip(old_bottom_row)
        left_face.grid[:, FacePositions.LEFT_COL] = np.flip(old_top_row)
        left_face.grid[FacePositions.TOP_ROW] = old_right_col
        left_face.grid[FacePositions.BOTTOM_ROW] = old_left_col

        update_piece_positions(left_face)

        return left_face.grid

    def transform_right_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        right_face = current_front.right.copy()
        old_face = right_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        right_face.grid[:, FacePositions.LEFT_COL] = old_bottom_row
        right_face.grid[:, FacePositions.RIGHT_COL] = old_top_row
        right_face.grid[FacePositions.TOP_ROW] = np.flip(old_left_col)
        right_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_right_col)

        update_piece_positions(right_face)

        return right_face.grid

    def transform_top_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        top_face = current_front.top.copy()
        old_face = top_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        top_face.grid[:, FacePositions.LEFT_COL] = np.flip(old_right_col)
        top_face.grid[:, FacePositions.RIGHT_COL] = np.flip(old_left_col)
        top_face.grid[FacePositions.TOP_ROW] = np.flip(old_bottom_row)
        top_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_top_row)

        update_piece_positions(top_face)

        return top_face.grid

    def transform_bottom_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        bottom_face = current_front.bottom.copy()

        update_piece_positions(bottom_face)

        return bottom_face.grid


class RotateDown:
    # YOUR CODE HERE
    def transform_front_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        return current_front.grid

    def transform_back_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        back_face = current_front.opposite.copy()
        old_face = back_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        back_face.grid[:, FacePositions.LEFT_COL] = np.flip(old_right_col)
        back_face.grid[:, FacePositions.RIGHT_COL] = np.flip(old_left_col)
        back_face.grid[FacePositions.TOP_ROW] = np.flip(old_bottom_row)
        back_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_top_row)

        update_piece_positions(back_face)

        return back_face.grid

    def transform_left_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        left_face = current_front.left.copy()
        old_face = left_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        left_face.grid[:, FacePositions.RIGHT_COL] = old_top_row
        left_face.grid[:, FacePositions.LEFT_COL] = old_bottom_row
        left_face.grid[FacePositions.TOP_ROW] = np.flip(old_left_col)
        left_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_right_col)

        update_piece_positions(left_face)

        return left_face.grid

    def transform_right_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        right_face = current_front.right.copy()
        old_face = right_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        right_face.grid[:, FacePositions.LEFT_COL] = np.flip(old_top_row)
        right_face.grid[:, FacePositions.RIGHT_COL] = np.flip(old_bottom_row)
        right_face.grid[FacePositions.TOP_ROW] = old_right_col
        right_face.grid[FacePositions.BOTTOM_ROW] = old_left_col

        update_piece_positions(right_face)

        return right_face.grid

    def transform_top_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        top_face = current_front.top.copy()

        update_piece_positions(top_face)

        return top_face.grid

    def transform_bottom_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        bottom_face = current_front.bottom.copy()
        old_face = bottom_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        bottom_face.grid[:, FacePositions.LEFT_COL] = np.flip(old_right_col)
        bottom_face.grid[:, FacePositions.RIGHT_COL] = np.flip(old_left_col)
        bottom_face.grid[FacePositions.TOP_ROW] = np.flip(old_bottom_row)
        bottom_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_top_row)

        update_piece_positions(bottom_face)

        return bottom_face.grid


class RotateLeftVertical:
    # YOUR CODE HERE
    def transform_front_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        front_face = current_front.copy()

        update_piece_positions(front_face)

        return front_face.grid

    def transform_back_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        back_face = current_front.opposite.copy()

        update_piece_positions(back_face)

        return back_face.grid

    def transform_left_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        left_face = current_front.left.copy()

        update_piece_positions(left_face)

        return left_face.grid

    def transform_right_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        right_face = current_front.right.copy()

        update_piece_positions(right_face)

        return right_face.grid

    def transform_top_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        top_face = current_front.top.copy()
        old_face = top_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        top_face.grid[:, FacePositions.RIGHT_COL] = old_top_row
        top_face.grid[:, FacePositions.LEFT_COL] = old_bottom_row
        top_face.grid[FacePositions.TOP_ROW] = np.flip(old_left_col)
        top_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_right_col)

        update_piece_positions(top_face)

        return top_face.grid

    def transform_bottom_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        bottom_face = current_front.bottom.copy()
        old_face = bottom_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        bottom_face.grid[:, FacePositions.RIGHT_COL] = np.flip(old_bottom_row)
        bottom_face.grid[:, FacePositions.LEFT_COL] = np.flip(old_top_row)
        bottom_face.grid[FacePositions.TOP_ROW] = old_right_col
        bottom_face.grid[FacePositions.BOTTOM_ROW] = old_left_col

        update_piece_positions(bottom_face)

        return bottom_face.grid


class RotateLeftHorizontal:
    # YOUR CODE HERE
    def transform_front_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        front_face = current_front.copy()
        old_face = front_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        front_face.grid[:, FacePositions.RIGHT_COL] = np.flip(old_bottom_row)
        front_face.grid[:, FacePositions.LEFT_COL] = np.flip(old_top_row)
        front_face.grid[FacePositions.TOP_ROW] = old_right_col
        front_face.grid[FacePositions.BOTTOM_ROW] = old_left_col

        update_piece_positions(front_face)

        return front_face.grid

    def transform_back_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        back_face = current_front.opposite.copy()
        old_face = back_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        back_face.grid[:, FacePositions.RIGHT_COL] = old_top_row
        back_face.grid[:, FacePositions.LEFT_COL] = old_bottom_row
        back_face.grid[FacePositions.TOP_ROW] = np.flip(old_left_col)
        back_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_right_col)

        update_piece_positions(back_face)

        return back_face.grid

    def transform_left_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        left_face = current_front.left.copy()
        old_face = left_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        left_face.grid[:, FacePositions.RIGHT_COL] = np.flip(old_bottom_row)
        left_face.grid[:, FacePositions.LEFT_COL] = np.flip(old_top_row)
        left_face.grid[FacePositions.TOP_ROW] = old_right_col
        left_face.grid[FacePositions.BOTTOM_ROW] = old_left_col

        update_piece_positions(left_face)

        return left_face.grid

    def transform_right_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        right_face = current_front.right.copy()
        old_face = right_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        right_face.grid[:, FacePositions.RIGHT_COL] = np.flip(old_bottom_row)
        right_face.grid[:, FacePositions.LEFT_COL] = np.flip(old_top_row)
        right_face.grid[FacePositions.TOP_ROW] = old_right_col
        right_face.grid[FacePositions.BOTTOM_ROW] = old_left_col

        update_piece_positions(right_face)

        return right_face.grid

    def transform_top_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        top_face = current_front.top.copy()
        old_face = top_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        top_face.grid[:, FacePositions.RIGHT_COL] = np.flip(old_bottom_row)
        top_face.grid[:, FacePositions.LEFT_COL] = np.flip(old_top_row)
        top_face.grid[FacePositions.TOP_ROW] = old_right_col
        top_face.grid[FacePositions.BOTTOM_ROW] = old_left_col

        update_piece_positions(top_face)

        return top_face.grid

    def transform_bottom_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        bottom_face = current_front.bottom.copy()
        old_face = bottom_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        bottom_face.grid[:, FacePositions.RIGHT_COL] = np.flip(old_bottom_row)
        bottom_face.grid[:, FacePositions.LEFT_COL] = np.flip(old_top_row)
        bottom_face.grid[FacePositions.TOP_ROW] = old_right_col
        bottom_face.grid[FacePositions.BOTTOM_ROW] = old_left_col

        update_piece_positions(bottom_face)

        return bottom_face.grid


class RotateRightVertical:
    # YOUR CODE HERE
    def transform_front_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        front_face = current_front.copy()

        update_piece_positions(front_face)

        return front_face.grid

    def transform_back_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        back_face = current_front.opposite.copy()

        update_piece_positions(back_face)

        return back_face.grid

    def transform_left_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        left_face = current_front.left.copy()

        update_piece_positions(left_face)

        return left_face.grid

    def transform_right_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        right_face = current_front.right.copy()

        update_piece_positions(right_face)

        return right_face.grid

    def transform_top_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        top_face = current_front.top.copy()
        old_face = top_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        top_face.grid[:, FacePositions.RIGHT_COL] = np.flip(old_bottom_row)
        top_face.grid[:, FacePositions.LEFT_COL] = np.flip(old_top_row)
        top_face.grid[FacePositions.TOP_ROW] = old_right_col
        top_face.grid[FacePositions.BOTTOM_ROW] = old_left_col

        update_piece_positions(top_face)

        return top_face.grid

    def transform_bottom_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        bottom_face = current_front.bottom.copy()
        old_face = bottom_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        bottom_face.grid[:, FacePositions.RIGHT_COL] = old_top_row
        bottom_face.grid[:, FacePositions.LEFT_COL] = old_bottom_row
        bottom_face.grid[FacePositions.TOP_ROW] = np.flip(old_left_col)
        bottom_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_right_col)

        update_piece_positions(bottom_face)

        return bottom_face.grid


class RotateRightHorizontal:
    # YOUR CODE HERE
    def transform_front_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        front_face = current_front.copy()
        old_face = front_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        front_face.grid[:, FacePositions.RIGHT_COL] = old_top_row
        front_face.grid[:, FacePositions.LEFT_COL] = old_bottom_row
        front_face.grid[FacePositions.TOP_ROW] = np.flip(old_left_col)
        front_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_right_col)

        update_piece_positions(front_face)

        return front_face.grid

    def transform_back_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        back_face = current_front.opposite.copy()
        old_face = back_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        back_face.grid[:, FacePositions.RIGHT_COL] = np.flip(old_bottom_row)
        back_face.grid[:, FacePositions.LEFT_COL] = np.flip(old_top_row)
        back_face.grid[FacePositions.TOP_ROW] = old_right_col
        back_face.grid[FacePositions.BOTTOM_ROW] = old_left_col

        update_piece_positions(back_face)

        return back_face.grid

    def transform_left_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        left_face = current_front.left.copy()
        old_face = left_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        left_face.grid[:, FacePositions.RIGHT_COL] = old_top_row
        left_face.grid[:, FacePositions.LEFT_COL] = old_bottom_row
        left_face.grid[FacePositions.TOP_ROW] = np.flip(old_left_col)
        left_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_right_col)

        update_piece_positions(left_face)

        return left_face.grid

    def transform_right_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        right_face = current_front.right.copy()
        old_face = right_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        right_face.grid[:, FacePositions.RIGHT_COL] = old_top_row
        right_face.grid[:, FacePositions.LEFT_COL] = old_bottom_row
        right_face.grid[FacePositions.TOP_ROW] = np.flip(old_left_col)
        right_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_right_col)

        update_piece_positions(right_face)

        return right_face.grid

    def transform_top_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        top_face = current_front.top.copy()
        old_face = top_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        top_face.grid[:, FacePositions.RIGHT_COL] = old_top_row
        top_face.grid[:, FacePositions.LEFT_COL] = old_bottom_row
        top_face.grid[FacePositions.TOP_ROW] = np.flip(old_left_col)
        top_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_right_col)

        update_piece_positions(top_face)

        return top_face.grid

    def transform_bottom_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        bottom_face = current_front.bottom.copy()
        old_face = bottom_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        bottom_face.grid[:, FacePositions.RIGHT_COL] = old_top_row
        bottom_face.grid[:, FacePositions.LEFT_COL] = old_bottom_row
        bottom_face.grid[FacePositions.TOP_ROW] = np.flip(old_left_col)
        bottom_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_right_col)

        update_piece_positions(bottom_face)

        return bottom_face.grid


class InvertVertical:
    # YOUR CODE HERE
    def transform_front_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        front_face = current_front.copy()

        update_piece_positions(front_face)

        return front_face.grid

    def transform_back_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        back_face = current_front.opposite.copy()

        update_piece_positions(back_face)

        return back_face.grid

    def transform_left_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        left_face = current_front.left.copy()

        update_piece_positions(left_face)

        return left_face.grid

    def transform_right_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        right_face = current_front.right.copy()

        update_piece_positions(right_face)

        return right_face.grid

    def transform_top_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        top_face = current_front.top.copy()
        old_face = top_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        top_face.grid[:, FacePositions.RIGHT_COL] = np.flip(old_left_col)
        top_face.grid[:, FacePositions.LEFT_COL] = np.flip(old_right_col)
        top_face.grid[FacePositions.TOP_ROW] = np.flip(old_bottom_row)
        top_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_top_row)

        update_piece_positions(top_face)

        return top_face.grid

    def transform_bottom_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        bottom_face = current_front.bottom.copy()
        old_face = bottom_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        bottom_face.grid[:, FacePositions.RIGHT_COL] = np.flip(old_left_col)
        bottom_face.grid[:, FacePositions.LEFT_COL] = np.flip(old_right_col)
        bottom_face.grid[FacePositions.TOP_ROW] = np.flip(old_bottom_row)
        bottom_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_top_row)

        update_piece_positions(bottom_face)

        return bottom_face.grid


class InvertHorizontal:
    # YOUR CODE HERE
    def transform_front_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        front_face = current_front.copy()
        old_face = front_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        front_face.grid[:, FacePositions.RIGHT_COL] = np.flip(old_left_col)
        front_face.grid[:, FacePositions.LEFT_COL] = np.flip(old_right_col)
        front_face.grid[FacePositions.TOP_ROW] = np.flip(old_bottom_row)
        front_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_top_row)

        update_piece_positions(front_face)

        return front_face.grid

    def transform_back_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        back_face = current_front.opposite.copy()
        old_face = back_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        back_face.grid[:, FacePositions.RIGHT_COL] = np.flip(old_left_col)
        back_face.grid[:, FacePositions.LEFT_COL] = np.flip(old_right_col)
        back_face.grid[FacePositions.TOP_ROW] = np.flip(old_bottom_row)
        back_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_top_row)

        update_piece_positions(back_face)

        return back_face.grid

    def transform_left_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        left_face = current_front.left.copy()
        old_face = left_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        left_face.grid[:, FacePositions.RIGHT_COL] = np.flip(old_left_col)
        left_face.grid[:, FacePositions.LEFT_COL] = np.flip(old_right_col)
        left_face.grid[FacePositions.TOP_ROW] = np.flip(old_bottom_row)
        left_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_top_row)

        update_piece_positions(left_face)

        return left_face.grid

    def transform_right_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        right_face = current_front.right.copy()
        old_face = right_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        right_face.grid[:, FacePositions.RIGHT_COL] = np.flip(old_left_col)
        right_face.grid[:, FacePositions.LEFT_COL] = np.flip(old_right_col)
        right_face.grid[FacePositions.TOP_ROW] = np.flip(old_bottom_row)
        right_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_top_row)

        update_piece_positions(right_face)

        return right_face.grid

    def transform_top_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        top_face = current_front.top.copy()
        old_face = top_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        top_face.grid[:, FacePositions.RIGHT_COL] = np.flip(old_left_col)
        top_face.grid[:, FacePositions.LEFT_COL] = np.flip(old_right_col)
        top_face.grid[FacePositions.TOP_ROW] = np.flip(old_bottom_row)
        top_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_top_row)

        update_piece_positions(top_face)

        return top_face.grid

    def transform_bottom_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        bottom_face = current_front.bottom.copy()
        old_face = bottom_face.copy()

        old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
        old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
        old_left_col = old_face.grid[:, FacePositions.LEFT_COL].copy()
        old_right_col = old_face.grid[:, FacePositions.RIGHT_COL].copy()

        bottom_face.grid[:, FacePositions.RIGHT_COL] = np.flip(old_left_col)
        bottom_face.grid[:, FacePositions.LEFT_COL] = np.flip(old_right_col)
        bottom_face.grid[FacePositions.TOP_ROW] = np.flip(old_bottom_row)
        bottom_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_top_row)

        update_piece_positions(bottom_face)

        return bottom_face.grid


############################################
##         SHIFT TRANSFORMATIONS
############################################


class RightColumnUp:
    # YOUR CODE HERE
    def transform_front_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        front_face = current_front.copy()
        old_face = front_face.copy()

        bottom_face = old_face.bottom.copy()

        bottom_col = bottom_face.grid[:, FacePositions.RIGHT_COL].copy()
        front_face.grid[:, FacePositions.RIGHT_COL] = bottom_col

        update_piece_positions(front_face)

        return front_face.grid

    def transform_back_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        back_face = current_front.opposite.copy()
        old_face = back_face.copy()

        top_face = old_face.top.copy()

        top_right_col = top_face.grid[:, FacePositions.RIGHT_COL].copy()
        back_face.grid[:, FacePositions.LEFT_COL] = np.flip(top_right_col)

        update_piece_positions(back_face)

        return back_face.grid

    def transform_left_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        return current_front.left.grid

    def transform_right_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        return RotateUp.transform_right_face_grid(current_front)

    def transform_top_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        top_face = current_front.top.copy()
        old_face = top_face.copy()

        front_face = old_face.front.copy()

        front_right_col = front_face.grid[:, FacePositions.RIGHT_COL].copy()
        top_face.grid[:, FacePositions.RIGHT_COL] = front_right_col

        update_piece_positions(top_face)

        return top_face.grid

    def transform_bottom_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        bottom_face = current_front.bottom.copy()
        old_face = bottom_face.copy()

        back_face = old_face.back.copy()

        back_left_col = back_face.grid[:, FacePositions.LEFT_COL].copy()
        bottom_face.grid[:, FacePositions.RIGHT_COL] = np.flip(back_left_col)

        update_piece_positions(bottom_face)

        return bottom_face.grid


class RightColumnDown:
    # YOUR CODE HERE
    def transform_front_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        front_face = current_front.copy()
        old_face = front_face.copy()

        top_face = old_face.top.copy()

        top_col = top_face.grid[:, FacePositions.RIGHT_COL].copy()
        front_face.grid[:, FacePositions.RIGHT_COL] = top_col

        update_piece_positions(front_face)

        return front_face.grid

    def transform_back_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        back_face = current_front.opposite.copy()
        old_face = back_face.copy()

        bottom_face = old_face.bottom.copy()

        bottom_right_col = bottom_face.grid[:, FacePositions.RIGHT_COL].copy()
        back_face.grid[:, FacePositions.LEFT_COL] = np.flip(bottom_right_col)

        update_piece_positions(back_face)

        return back_face.grid

    def transform_left_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        return current_front.left.grid

    def transform_right_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        return RotateDown.transform_right_face_grid(current_front)

    def transform_top_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        top_face = current_front.top.copy()
        old_face = top_face.copy()

        back_face = old_face.back.copy()

        back_left_col = back_face.grid[:, FacePositions.LEFT_COL].copy()
        top_face.grid[:, FacePositions.RIGHT_COL] = np.flip(back_left_col)

        update_piece_positions(top_face)

        return top_face.grid

    def transform_bottom_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        bottom_face = current_front.bottom.copy()
        old_face = bottom_face.copy()

        front_face = old_face.front.copy()

        front_right_col = front_face.grid[:, FacePositions.RIGHT_COL].copy()
        bottom_face.grid[:, FacePositions.RIGHT_COL] = front_right_col

        update_piece_positions(bottom_face)

        return bottom_face.grid


class LeftColumnUp:
    # YOUR CODE HERE
    def transform_front_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        front_face = current_front.copy()
        old_face = front_face.copy()

        bottom_face = old_face.bottom.copy()

        bottom_col = bottom_face.grid[:, FacePositions.LEFT_COL].copy()
        front_face.grid[:, FacePositions.LEFT_COL] = bottom_col

        update_piece_positions(front_face)

        return front_face.grid

    def transform_back_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        back_face = current_front.opposite.copy()
        old_face = back_face.copy()

        top_face = old_face.top.copy()

        top_left_col = top_face.grid[:, FacePositions.LEFT_COL].copy()
        back_face.grid[:, FacePositions.RIGHT_COL] = np.flip(top_left_col)

        update_piece_positions(back_face)

        return back_face.grid

    def transform_left_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        return RotateUp.transform_left_face_grid(current_front)

    def transform_right_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        return current_front.right.grid

    def transform_top_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        top_face = current_front.top.copy()
        old_face = top_face.copy()

        front_face = old_face.front.copy()

        front_left_col = front_face.grid[:, FacePositions.LEFT_COL].copy()
        top_face.grid[:, FacePositions.LEFT_COL] = front_left_col

        update_piece_positions(top_face)

        return top_face.grid

    def transform_bottom_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        bottom_face = current_front.bottom.copy()
        old_face = bottom_face.copy()

        back_face = old_face.back.copy()

        back_right_col = back_face.grid[:, FacePositions.RIGHT_COL].copy()
        bottom_face.grid[:, FacePositions.LEFT_COL] = np.flip(back_right_col)

        update_piece_positions(bottom_face)

        return bottom_face.grid


class LeftColumnDown:
    # YOUR CODE HERE
    def transform_front_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        front_face = current_front.copy()
        old_face = front_face.copy()

        top_face = old_face.top.copy()

        top_col = top_face.grid[:, FacePositions.LEFT_COL].copy()
        front_face.grid[:, FacePositions.LEFT_COL] = top_col

        update_piece_positions(front_face)

        return front_face.grid

    def transform_back_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        back_face = current_front.opposite.copy()
        old_face = back_face.copy()

        bottom_face = old_face.bottom.copy()

        bottom_left_col = bottom_face.grid[:, FacePositions.LEFT_COL].copy()
        back_face.grid[:, FacePositions.RIGHT_COL] = np.flip(bottom_left_col)

        update_piece_positions(back_face)

        return back_face.grid

    def transform_left_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        return RotateDown.transform_left_face_grid(current_front)

    def transform_right_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        return current_front.right.grid

    def transform_top_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        top_face = current_front.top.copy()
        old_face = top_face.copy()

        back_face = old_face.back.copy()

        back_right_col = back_face.grid[:, FacePositions.RIGHT_COL].copy()
        top_face.grid[:, FacePositions.LEFT_COL] = np.flip(back_right_col)

        update_piece_positions(top_face)

        return top_face.grid

    def transform_bottom_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        bottom_face = current_front.bottom.copy()
        old_face = bottom_face.copy()

        front_face = old_face.front.copy()

        front_left_col = front_face.grid[:, FacePositions.LEFT_COL].copy()
        bottom_face.grid[:, FacePositions.LEFT_COL] = front_left_col

        update_piece_positions(bottom_face)

        return bottom_face.grid


class TopRowRight:
    # YOUR CODE HERE
    def transform_front_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        face = current_front.copy()

        left_face = face.left.copy()

        left_top_row = left_face.grid[FacePositions.TOP_ROW].copy()
        face.grid[FacePositions.TOP_ROW] = left_top_row

        update_piece_positions(face)

        return face.grid

    def transform_back_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        face = current_front.opposite.copy()

        left_face = face.left.copy()

        left_top_row = left_face.grid[FacePositions.TOP_ROW].copy()
        face.grid[FacePositions.TOP_ROW] = left_top_row

        update_piece_positions(face)

        return face.grid

    def transform_left_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        face = current_front.left.copy()

        left_face = face.left.copy()

        left_top_row = left_face.grid[FacePositions.TOP_ROW].copy()
        face.grid[FacePositions.TOP_ROW] = left_top_row

        update_piece_positions(face)

        return face.grid

    def transform_right_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        face = current_front.right.copy()

        left_face = face.left.copy()

        left_top_row = left_face.grid[FacePositions.TOP_ROW].copy()
        face.grid[FacePositions.TOP_ROW] = left_top_row

        update_piece_positions(face)

        return face.grid

    def transform_top_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        return RotateRightVertical.transform_top_face_grid(current_front)

    def transform_bottom_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        return current_front.bottom.grid


class TopRowLeft:
    # YOUR CODE HERE
    def transform_front_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        face = current_front.copy()

        right_face = face.right.copy()

        right_top_row = right_face.grid[FacePositions.TOP_ROW].copy()
        face.grid[FacePositions.TOP_ROW] = right_top_row

        update_piece_positions(face)

        return face.grid

    def transform_back_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        face = current_front.opposite.copy()

        right_face = face.right.copy()

        right_top_row = right_face.grid[FacePositions.TOP_ROW].copy()
        face.grid[FacePositions.TOP_ROW] = right_top_row

        update_piece_positions(face)

        return face.grid

    def transform_left_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        face = current_front.left.copy()

        right_face = face.right.copy()

        right_top_row = right_face.grid[FacePositions.TOP_ROW].copy()
        face.grid[FacePositions.TOP_ROW] = right_top_row

        update_piece_positions(face)

        return face.grid

    def transform_right_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        face = current_front.right.copy()

        right_face = face.right.copy()

        right_top_row = right_face.grid[FacePositions.TOP_ROW].copy()
        face.grid[FacePositions.TOP_ROW] = right_top_row

        update_piece_positions(face)

        return face.grid

    def transform_top_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        return RotateLeftVertical.transform_top_face_grid(current_front)

    def transform_bottom_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        return current_front.bottom.grid


class BottomRowRight:
    # YOUR CODE HERE
    def transform_front_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        face = current_front.copy()

        left_face = face.left.copy()

        left_bottom_row = left_face.grid[FacePositions.BOTTOM_ROW].copy()
        face.grid[FacePositions.BOTTOM_ROW] = left_bottom_row

        update_piece_positions(face)

        return face.grid

    def transform_back_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        face = current_front.opposite.copy()

        left_face = face.left.copy()

        left_bottom_row = left_face.grid[FacePositions.BOTTOM_ROW].copy()
        face.grid[FacePositions.BOTTOM_ROW] = left_bottom_row

        update_piece_positions(face)

        return face.grid

    def transform_left_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        face = current_front.left.copy()

        left_face = face.left.copy()

        left_bottom_row = left_face.grid[FacePositions.BOTTOM_ROW].copy()
        face.grid[FacePositions.BOTTOM_ROW] = left_bottom_row

        update_piece_positions(face)

        return face.grid

    def transform_right_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        face = current_front.right.copy()

        left_face = face.left.copy()

        left_bottom_row = left_face.grid[FacePositions.BOTTOM_ROW].copy()
        face.grid[FacePositions.BOTTOM_ROW] = left_bottom_row

        update_piece_positions(face)

        return face.grid

    def transform_top_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        return current_front.top.grid

    def transform_bottom_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        return RotateRightVertical.transform_bottom_face_grid(current_front)


class BottomRowLeft:
    # YOUR CODE HERE
    def transform_front_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        face = current_front.copy()

        right_face = face.right.copy()

        right_bottom_row = right_face.grid[FacePositions.BOTTOM_ROW].copy()
        face.grid[FacePositions.BOTTOM_ROW] = right_bottom_row

        update_piece_positions(face)

        return face.grid

    def transform_back_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        face = current_front.opposite.copy()

        right_face = face.right.copy()

        right_bottom_row = right_face.grid[FacePositions.BOTTOM_ROW].copy()
        face.grid[FacePositions.BOTTOM_ROW] = right_bottom_row

        update_piece_positions(face)

        return face.grid

    def transform_left_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        face = current_front.left.copy()

        right_face = face.right.copy()

        right_bottom_row = right_face.grid[FacePositions.BOTTOM_ROW].copy()
        face.grid[FacePositions.BOTTOM_ROW] = right_bottom_row

        update_piece_positions(face)

        return face.grid

    def transform_right_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        face = current_front.right.copy()

        right_face = face.right.copy()

        right_bottom_row = right_face.grid[FacePositions.BOTTOM_ROW].copy()
        face.grid[FacePositions.BOTTOM_ROW] = right_bottom_row

        update_piece_positions(face)

        return face.grid

    def transform_top_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        return current_front.top.grid

    def transform_bottom_face_grid(
        current_front: Face, is_test: bool = False
    ) -> np.ndarray:
        return RotateLeftVertical.transform_bottom_face_grid(current_front)
