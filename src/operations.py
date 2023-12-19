from __future__ import annotations
import face_transformation as ft
import grid_transformation as gt
import icecream as ic
from constants import POSSIBLE_ROTATIONS, POSSIBLE_SHIFTS
from error import InvalidOperationError

from typing import Protocol, TYPE_CHECKING

if TYPE_CHECKING:
    from cube_init_m import RubixCube, Face


class Operation(Protocol):
    def verbose(func: function) -> function:
        ...
        # def wrapper(cube: RubixCube)

        # pass


class Rotations:
    # YOUR CODE HERE

    def verbose(func: function) -> function:
        def wrapper(cube: RubixCube, internal_req: bool = False):
            if not internal_req:
                for op in POSSIBLE_ROTATIONS:
                    if op == cube.current_operation:
                        print(op.value)
                        break
                else:
                    raise InvalidOperationError("Invalid Rotation Operation Requested!")
            func(cube)
            cube.current_operation = None

        return wrapper

    @verbose
    def rotate_up(cube: RubixCube, internal_req: bool = False) -> None:
        current = cube.current_perspective

        ## Getting transformed Left & Right Faces
        new_left_face = ft.RotateUp.transform_left_face(current)
        new_right_face = ft.RotateUp.transform_right_face(current)

        ## Getting transformed Left & Right Grids
        new_left_grid = gt.RotateUp.transform_left_face_grid(current)
        new_right_grid = gt.RotateUp.transform_right_face_grid(current)

        ## Getting transformed Front & Back Faces
        new_front_face = ft.RotateUp.transform_front_face(current)
        new_back_face = ft.RotateUp.transform_back_face(current)

        ## Getting transformed Back Grid
        new_front_grid = gt.RotateUp.transform_front_face_grid(current)
        new_back_grid = gt.RotateUp.transform_back_face_grid(current)

        ## Getting transformed Top & Bottom Faces
        new_top_face = ft.RotateUp.transform_top_face(current)
        new_bottom_face = ft.RotateUp.transform_bottom_face(current)

        ## Getting transformed Top Grid
        new_bottom_grid = gt.RotateUp.transform_bottom_face_grid(current)
        new_top_grid = gt.RotateUp.transform_top_face_grid(current)

        ## Updating grid for each transformed face
        new_left_face.grid = new_left_grid
        new_right_face.grid = new_right_grid
        new_top_face.grid = new_top_grid
        new_bottom_face.grid = new_bottom_grid
        new_back_face.grid = new_back_grid
        new_front_face.grid = new_front_grid

        ## Changing perspective to top face
        cube.current_perspective = cube.current_perspective.bottom

        ## Transferring transformed attribute values to original object
        Rotations.transfer_faces(cube.current_perspective, new_bottom_face)
        Rotations.transfer_faces(cube.current_perspective.right, new_right_face)
        Rotations.transfer_faces(cube.current_perspective.left, new_left_face)
        Rotations.transfer_faces(cube.current_perspective.top, new_front_face)
        Rotations.transfer_faces(cube.current_perspective.bottom, new_back_face)
        Rotations.transfer_faces(cube.current_perspective.opposite, new_top_face)

    @verbose
    def rotate_down(cube: RubixCube, internal_req: bool = False) -> None:
        current = cube.current_perspective

        ## Getting transformed Left & Right Faces
        new_left_face = ft.RotateDown.transform_left_face(current)
        new_right_face = ft.RotateDown.transform_right_face(current)

        ## Getting transformed Left & Right Grids
        new_left_grid = gt.RotateDown.transform_left_face_grid(current)
        new_right_grid = gt.RotateDown.transform_right_face_grid(current)

        ## Getting transformed Front & Back Faces
        new_front_face = ft.RotateDown.transform_front_face(current)
        new_back_face = ft.RotateDown.transform_back_face(current)

        ## Getting transformed Back Grid
        new_front_grid = gt.RotateDown.transform_front_face_grid(current)
        new_back_grid = gt.RotateDown.transform_back_face_grid(current)

        ## Getting transformed Top & Bottom Faces
        new_top_face = ft.RotateDown.transform_top_face(current)
        new_bottom_face = ft.RotateDown.transform_bottom_face(current)

        ## Getting transformed Top Grid
        new_top_grid = gt.RotateDown.transform_top_face_grid(current)
        new_bottom_grid = gt.RotateDown.transform_bottom_face_grid(current)

        ## Updating grid for each transformed face
        new_left_face.grid = new_left_grid
        new_right_face.grid = new_right_grid
        new_top_face.grid = new_top_grid
        new_bottom_face.grid = new_bottom_grid
        new_back_face.grid = new_back_grid
        new_front_face.grid = new_front_grid

        ## Changing perspective to top face
        cube.current_perspective = cube.current_perspective.top

        ## Transferring transformed attribute values to original object
        Rotations.transfer_faces(cube.current_perspective, new_top_face)
        Rotations.transfer_faces(cube.current_perspective.right, new_right_face)
        Rotations.transfer_faces(cube.current_perspective.left, new_left_face)
        Rotations.transfer_faces(cube.current_perspective.top, new_back_face)
        Rotations.transfer_faces(cube.current_perspective.bottom, new_front_face)
        Rotations.transfer_faces(cube.current_perspective.opposite, new_bottom_face)

    @verbose
    def rotate_left_vertically(cube: RubixCube, internal_req: bool = False):
        current = cube.current_perspective

        ## Getting transformed Top & Bottom Faces
        new_top_face = ft.RotateLeftVertical.transform_top_face(current)
        new_bottom_face = ft.RotateLeftVertical.transform_bottom_face(current)

        ## Getting transformed Top & Bottom Grids
        new_top_grid = gt.RotateLeftVertical.transform_top_face_grid(current)
        new_bottom_grid = gt.RotateLeftVertical.transform_bottom_face_grid(current)

        ## Getting transformed Left & Right Faces
        new_left_face = ft.RotateLeftVertical.transform_left_face(current)
        new_right_face = ft.RotateLeftVertical.transform_right_face(current)

        ## Getting transformed Left & Right Grids
        new_left_grid = gt.RotateLeftVertical.transform_left_face_grid(current)
        new_right_grid = gt.RotateLeftVertical.transform_right_face_grid(current)

        ## Getting transformed Front & Back Faces
        new_front_face = ft.RotateLeftVertical.transform_front_face(current)
        new_back_face = ft.RotateLeftVertical.transform_back_face(current)

        ## Getting transformed Front & Back Grids
        new_front_grid = gt.RotateLeftVertical.transform_front_face_grid(current)
        new_back_grid = gt.RotateLeftVertical.transform_back_face_grid(current)

        ## Updating grid for each transformed face
        new_top_face.grid = new_top_grid
        new_bottom_face.grid = new_bottom_grid
        new_left_face.grid = new_left_grid
        new_right_face.grid = new_right_grid
        new_front_face.grid = new_front_grid
        new_back_face.grid = new_back_grid

        ## Changing perspective to right face
        cube.current_perspective = cube.current_perspective.right

        ## Transferring transformed attribute values to original object
        Rotations.transfer_faces(cube.current_perspective.top, new_top_face)
        Rotations.transfer_faces(cube.current_perspective.bottom, new_bottom_face)
        Rotations.transfer_faces(cube.current_perspective, new_right_face)
        Rotations.transfer_faces(cube.current_perspective.opposite, new_left_face)
        Rotations.transfer_faces(cube.current_perspective.left, new_front_face)
        Rotations.transfer_faces(cube.current_perspective.right, new_back_face)

    @verbose
    def rotate_right_vertically(cube: RubixCube, internal_req: bool = False):
        current = cube.current_perspective

        ## Getting transformed Top & Bottom Faces
        new_top_face = ft.RotateRightVertical.transform_top_face(current)
        new_bottom_face = ft.RotateRightVertical.transform_bottom_face(current)

        ## Getting transformed Top & Bottom Grids
        new_top_grid = gt.RotateRightVertical.transform_top_face_grid(current)
        new_bottom_grid = gt.RotateRightVertical.transform_bottom_face_grid(current)

        ## Getting transformed Left & Right Faces
        new_left_face = ft.RotateRightVertical.transform_left_face(current)
        new_right_face = ft.RotateRightVertical.transform_right_face(current)

        ## Getting transformed Left & Right Grids
        new_left_grid = gt.RotateRightVertical.transform_left_face_grid(current)
        new_right_grid = gt.RotateRightVertical.transform_right_face_grid(current)

        ## Getting transformed Front & Back Faces
        new_front_face = ft.RotateRightVertical.transform_front_face(current)
        new_back_face = ft.RotateRightVertical.transform_back_face(current)

        ## Getting transformed Front & Back Faces
        new_front_grid = gt.RotateRightVertical.transform_front_face_grid(current)
        new_back_grid = gt.RotateRightVertical.transform_back_face_grid(current)

        ## Updating grid for each transformed face
        new_top_face.grid = new_top_grid
        new_bottom_face.grid = new_bottom_grid
        new_left_face.grid = new_left_grid
        new_right_face.grid = new_right_grid
        new_front_face.grid = new_front_grid
        new_back_face.grid = new_back_grid

        ## Changing perspective to left face
        cube.current_perspective = cube.current_perspective.left

        ## Transferring transformed attribute values to original object
        Rotations.transfer_faces(cube.current_perspective.top, new_top_face)
        Rotations.transfer_faces(cube.current_perspective.bottom, new_bottom_face)
        Rotations.transfer_faces(cube.current_perspective, new_left_face)
        Rotations.transfer_faces(cube.current_perspective.opposite, new_right_face)
        Rotations.transfer_faces(cube.current_perspective.left, new_back_face)
        Rotations.transfer_faces(cube.current_perspective.right, new_front_face)

    @verbose
    def rotate_left_horizontally(cube: RubixCube, internal_req: bool = False):
        current = cube.current_perspective

        ## Getting transformed Left & Right Faces
        new_right_face = ft.RotateLeftHorizontal.transform_right_face(current)
        new_left_face = ft.RotateLeftHorizontal.transform_left_face(current)

        ## Getting transformed Left & Right Grids
        new_right_grid = gt.RotateLeftHorizontal.transform_right_face_grid(current)
        new_left_grid = gt.RotateLeftHorizontal.transform_left_face_grid(current)

        ## Getting transformed Front & Back Faces
        new_front_face = ft.RotateLeftHorizontal.transform_front_face(current)
        new_back_face = ft.RotateLeftHorizontal.transform_back_face(current)

        ## Getting transformed Front & Back Grids
        new_front_grid = gt.RotateLeftHorizontal.transform_front_face_grid(current)
        new_back_grid = gt.RotateLeftHorizontal.transform_back_face_grid(current)

        ## Getting transformed Top & Bottom Faces
        new_top_face = ft.RotateLeftHorizontal.transform_top_face(current)
        new_bottom_face = ft.RotateLeftHorizontal.transform_bottom_face(current)

        ## Getting transformed Top & Bottom Faces
        new_top_grid = gt.RotateLeftHorizontal.transform_top_face_grid(current)
        new_bottom_grid = gt.RotateLeftHorizontal.transform_bottom_face_grid(current)

        ## Updating grid for each transformed face
        new_left_face.grid = new_left_grid
        new_right_face.grid = new_right_grid
        new_front_face.grid = new_front_grid
        new_back_face.grid = new_back_grid
        new_top_face.grid = new_top_grid
        new_bottom_face.grid = new_bottom_grid

        ## Transferring transformed attribute values to original object
        Rotations.transfer_faces(cube.current_perspective, new_front_face)
        Rotations.transfer_faces(cube.current_perspective.left, new_top_face)
        Rotations.transfer_faces(cube.current_perspective.right, new_bottom_face)
        Rotations.transfer_faces(cube.current_perspective.top, new_right_face)
        Rotations.transfer_faces(cube.current_perspective.bottom, new_left_face)
        Rotations.transfer_faces(cube.current_perspective.opposite, new_back_face)

    @verbose
    def rotate_right_horizontally(cube: RubixCube, internal_req: bool = False):
        current = cube.current_perspective

        ## Getting transformed Left & Right Faces
        new_right_face = ft.RotateRightHorizontal.transform_right_face(current)
        new_left_face = ft.RotateRightHorizontal.transform_left_face(current)

        ## Getting transformed Left & Right Grids
        new_right_grid = gt.RotateRightHorizontal.transform_right_face_grid(current)
        new_left_grid = gt.RotateRightHorizontal.transform_left_face_grid(current)

        ## Getting transformed Front & Back Faces
        new_front_face = ft.RotateRightHorizontal.transform_front_face(current)
        new_back_face = ft.RotateRightHorizontal.transform_back_face(current)

        ## Getting transformed Front & Back Grids
        new_front_grid = gt.RotateRightHorizontal.transform_front_face_grid(current)
        new_back_grid = gt.RotateRightHorizontal.transform_back_face_grid(current)

        ## Getting transformed Top & Bottom Faces
        new_top_face = ft.RotateRightHorizontal.transform_top_face(current)
        new_bottom_face = ft.RotateRightHorizontal.transform_bottom_face(current)

        ## Getting transformed Top & Bottom Grids
        new_top_grid = gt.RotateRightHorizontal.transform_top_face_grid(current)
        new_bottom_grid = gt.RotateRightHorizontal.transform_bottom_face_grid(current)

        ## Updating grid for each transformed face
        new_left_face.grid = new_left_grid
        new_right_face.grid = new_right_grid
        new_front_face.grid = new_front_grid
        new_back_face.grid = new_back_grid
        new_top_face.grid = new_top_grid
        new_bottom_face.grid = new_bottom_grid

        ## Transferring transformed attribute values to original object
        Rotations.transfer_faces(cube.current_perspective, new_front_face)
        Rotations.transfer_faces(cube.current_perspective.left, new_bottom_face)
        Rotations.transfer_faces(cube.current_perspective.right, new_top_face)
        Rotations.transfer_faces(cube.current_perspective.top, new_left_face)
        Rotations.transfer_faces(cube.current_perspective.bottom, new_right_face)
        Rotations.transfer_faces(cube.current_perspective.opposite, new_back_face)

    @verbose
    def invert_vertically(cube: RubixCube, internal_req: bool = False):
        current = cube.current_perspective

        ## Getting transformed Top & Bottom Faces
        new_top_face = ft.InvertVertical.transform_top_face(current)
        new_bottom_face = ft.InvertVertical.transform_bottom_face(current)

        ## Getting transformed Top & Bottom Grids
        new_top_grid = gt.InvertVertical.transform_top_face_grid(current)
        new_bottom_grid = gt.InvertVertical.transform_bottom_face_grid(current)

        ## Getting transformed Left & Right Faces
        new_left_face = ft.InvertVertical.transform_left_face(current)
        new_right_face = ft.InvertVertical.transform_right_face(current)

        ## Getting transformed Left & Right Grids
        new_left_grid = gt.InvertVertical.transform_left_face_grid(current)
        new_right_grid = gt.InvertVertical.transform_right_face_grid(current)

        ## Getting transformed Front & Back Faces
        new_front_face = ft.InvertVertical.transform_front_face(current)
        new_back_face = ft.InvertVertical.transform_back_face(current)

        ## Getting transformed Front & Back Grids
        new_front_grid = gt.InvertVertical.transform_front_face_grid(current)
        new_back_grid = gt.InvertVertical.transform_back_face_grid(current)

        ## Updating grid for each transformed face
        new_top_face.grid = new_top_grid
        new_bottom_face.grid = new_bottom_grid
        new_left_face.grid = new_left_grid
        new_right_face.grid = new_right_grid
        new_front_face.grid = new_front_grid
        new_back_face.grid = new_back_grid

        ## Changing perspective to opposite face
        cube.current_perspective = cube.current_perspective.opposite

        ## Transferring transformed attribute values to original object
        Rotations.transfer_faces(cube.current_perspective.top, new_top_face)
        Rotations.transfer_faces(cube.current_perspective.bottom, new_bottom_face)
        Rotations.transfer_faces(cube.current_perspective, new_back_face)
        Rotations.transfer_faces(cube.current_perspective.opposite, new_front_face)
        Rotations.transfer_faces(cube.current_perspective.left, new_right_face)
        Rotations.transfer_faces(cube.current_perspective.right, new_left_face)

    @verbose
    def invert_horizontally(cube: RubixCube, internal_req: bool = False):
        current = cube.current_perspective

        ## Getting transformed Top & Bottom Faces
        new_top_face = ft.InvertHorizontal.transform_top_face(current)
        new_bottom_face = ft.InvertHorizontal.transform_bottom_face(current)

        ## Getting transformed Top & Bottom Grids
        new_top_grid = gt.InvertHorizontal.transform_top_face_grid(current)
        new_bottom_grid = gt.InvertHorizontal.transform_bottom_face_grid(current)

        ## Getting transformed Front & Back Faces
        new_front_face = ft.InvertHorizontal.transform_front_face(current)
        new_back_face = ft.InvertHorizontal.transform_back_face(current)

        ## Getting transformed Front & Back Grids
        new_front_grid = gt.InvertHorizontal.transform_front_face_grid(current)
        new_back_grid = gt.InvertHorizontal.transform_back_face_grid(current)

        ## Getting transformed Left & Right Faces
        new_left_face = ft.InvertHorizontal.transform_left_face(current)
        new_right_face = ft.InvertHorizontal.transform_right_face(current)

        ## Getting transformed Left & Right Grids
        new_left_grid = gt.InvertHorizontal.transform_left_face_grid(current)
        new_right_grid = gt.InvertHorizontal.transform_right_face_grid(current)

        ## Updating grid for each transformed face
        new_left_face.grid = new_left_grid
        new_right_face.grid = new_right_grid
        new_top_face.grid = new_top_grid
        new_bottom_face.grid = new_bottom_grid
        new_back_face.grid = new_back_grid
        new_front_face.grid = new_front_grid

        ## Changing perspective to opposite face
        cube.current_perspective = cube.current_perspective.opposite

        ## Transferring transformed attribute values to original object
        Rotations.transfer_faces(cube.current_perspective, new_back_face)
        Rotations.transfer_faces(cube.current_perspective.right, new_right_face)
        Rotations.transfer_faces(cube.current_perspective.left, new_left_face)
        Rotations.transfer_faces(cube.current_perspective.top, new_bottom_face)
        Rotations.transfer_faces(cube.current_perspective.bottom, new_top_face)
        Rotations.transfer_faces(cube.current_perspective.opposite, new_front_face)

    def transfer_faces(old: Face, new: Face) -> None:
        try:
            old.left = new.left
            old.right = new.right
            old.top = new.top
            old.bottom = new.bottom
            old.front = new.front
            old.back = new.back
            # old.is_side_face = new.is_side_face
            old.orientation_to_cube = new.orientation_to_cube
            old.grid = new.grid
        except AttributeError:
            raise AttributeError()


class Shifts:
    # YOUR CODE HERE

    def verbose(func: function) -> function:
        def wrapper(cube: RubixCube, internal_req: bool = False):
            if not internal_req:
                for op in POSSIBLE_SHIFTS:
                    ic.ic(op)
                    ic.ic(cube.current_operation)
                    if op == cube.current_operation:
                        print(op.value)
                        break
                else:
                    raise InvalidOperationError("Invalid Shift Operation Requested!")
            func(cube)
            cube.current_operation = None

        return wrapper

    @verbose
    def right_col_up(cube: RubixCube, internal_req: bool = False) -> None:
        # YOUR CODE HERE
        current = cube.current_perspective

        ## Getting new Right Face Grid
        new_right_grid = gt.RightColumnUp.transform_right_face_grid(current)
        new_left_grid = gt.RightColumnUp.transform_left_face_grid(current)

        ## Getting new Front & Back Grids
        new_front_grid = gt.RightColumnUp.transform_front_face_grid(current)
        new_back_grid = gt.RightColumnUp.transform_back_face_grid(current)

        ## Getting new Top & Bottom Grids
        new_top_grid = gt.RightColumnUp.transform_top_face_grid(current)
        new_bottom_grid = gt.RightColumnUp.transform_bottom_face_grid(current)

        ## Updating grids for all faces where there was a change
        current.grid = new_front_grid
        current.left.grid = new_left_grid
        current.right.grid = new_right_grid
        current.opposite.grid = new_back_grid
        current.top.grid = new_top_grid
        current.bottom.grid = new_bottom_grid

    @verbose
    def right_col_down(cube: RubixCube, internal_req: bool = False) -> None:
        # YOUR CODE HERE
        current = cube.current_perspective

        ## Getting new Right Face Grid
        new_right_grid = gt.RightColumnDown.transform_right_face_grid(current)
        new_left_grid = gt.RightColumnDown.transform_left_face_grid(current)

        ## Getting new Front & Back Grids
        new_front_grid = gt.RightColumnDown.transform_front_face_grid(current)
        new_back_grid = gt.RightColumnDown.transform_back_face_grid(current)

        ## Getting new Top & Bottom Grids
        new_top_grid = gt.RightColumnDown.transform_top_face_grid(current)
        new_bottom_grid = gt.RightColumnDown.transform_bottom_face_grid(current)

        ## Updating grids for all faces where there was a change
        current.grid = new_front_grid
        current.left.grid = new_left_grid
        current.right.grid = new_right_grid
        current.opposite.grid = new_back_grid
        current.top.grid = new_top_grid
        current.bottom.grid = new_bottom_grid

    @verbose
    def left_col_up(cube: RubixCube, internal_req: bool = False) -> None:
        # YOUR CODE HERE
        current = cube.current_perspective

        ## Getting new Left Face Grid
        new_left_grid = gt.LeftColumnUp.transform_left_face_grid(current)
        new_right_grid = gt.LeftColumnUp.transform_right_face_grid(current)

        ## Getting new Front & Back Grids
        new_front_grid = gt.LeftColumnUp.transform_front_face_grid(current)
        new_back_grid = gt.LeftColumnUp.transform_back_face_grid(current)

        ## Getting new Top & Bottom Grids
        new_top_grid = gt.LeftColumnUp.transform_top_face_grid(current)
        new_bottom_grid = gt.LeftColumnUp.transform_bottom_face_grid(current)

        ## Updating grids for all faces where there was a change
        current.grid = new_front_grid
        current.left.grid = new_left_grid
        current.right.grid = new_right_grid
        current.opposite.grid = new_back_grid
        current.top.grid = new_top_grid
        current.bottom.grid = new_bottom_grid

    @verbose
    def left_col_down(cube: RubixCube, internal_req: bool = False) -> None:
        current = cube.current_perspective

        ## Getting transformed Left Face Grid
        new_left_grid = gt.LeftColumnDown.transform_left_face_grid(current)
        new_right_grid = gt.LeftColumnDown.transform_right_face_grid(current)

        ## Getting transformed Front & Back Grids
        new_front_grid = gt.LeftColumnDown.transform_front_face_grid(current)
        new_back_grid = gt.LeftColumnDown.transform_back_face_grid(current)

        ## Getting transformed Top & Bottom Grids
        new_top_grid = gt.LeftColumnDown.transform_top_face_grid(current)
        new_bottom_grid = gt.LeftColumnDown.transform_bottom_face_grid(current)

        ## Updating grids for all faces where there was a change
        current.grid = new_front_grid
        current.left.grid = new_left_grid
        current.right.grid = new_right_grid
        current.opposite.grid = new_back_grid
        current.top.grid = new_top_grid
        current.bottom.grid = new_bottom_grid

    @verbose
    def top_row_left(cube: RubixCube, internal_req: bool = False) -> None:
        current = cube.current_perspective

        ## Getting transformed Top Grids
        new_top_grid = gt.TopRowLeft.transform_top_face_grid(current)
        new_bottom_grid = gt.TopRowLeft.transform_bottom_face_grid(current)

        ## Getting transformed Left & Right Grids
        new_left_grid = gt.TopRowLeft.transform_left_face_grid(current)
        new_right_grid = gt.TopRowLeft.transform_right_face_grid(current)

        ## Getting transformed Front & Back Grids
        new_front_grid = gt.TopRowLeft.transform_front_face_grid(current)
        new_back_grid = gt.TopRowLeft.transform_back_face_grid(current)

        ## Updating grids for all faces where there was a change
        current.grid = new_front_grid
        current.left.grid = new_left_grid
        current.right.grid = new_right_grid
        current.opposite.grid = new_back_grid
        current.top.grid = new_top_grid
        current.bottom.grid = new_bottom_grid

    @verbose
    def top_row_right(cube: RubixCube, internal_req: bool = False) -> None:
        current = cube.current_perspective

        ## Getting transformed Top Grids
        new_top_grid = gt.TopRowRight.transform_top_face_grid(current)
        new_bottom_grid = gt.TopRowRight.transform_bottom_face_grid(current)

        ## Getting transformed Left & Right Grids
        new_left_grid = gt.TopRowRight.transform_left_face_grid(current)
        new_right_grid = gt.TopRowRight.transform_right_face_grid(current)

        ## Getting transformed Front & Back Grids
        new_front_grid = gt.TopRowRight.transform_front_face_grid(current)
        new_back_grid = gt.TopRowRight.transform_back_face_grid(current)

        ## Updating grids for all faces where there was a change
        current.grid = new_front_grid
        current.left.grid = new_left_grid
        current.right.grid = new_right_grid
        current.opposite.grid = new_back_grid
        current.top.grid = new_top_grid
        current.bottom.grid = new_bottom_grid

    @verbose
    def bottom_row_left(cube: RubixCube, internal_req: bool = False) -> None:
        current = cube.current_perspective

        ## Getting transformed Top Grids
        new_top_grid = gt.BottomRowLeft.transform_top_face_grid(current)
        new_bottom_grid = gt.BottomRowLeft.transform_bottom_face_grid(current)

        ## Getting transformed Left & Right Grids
        new_left_grid = gt.BottomRowLeft.transform_left_face_grid(current)
        new_right_grid = gt.BottomRowLeft.transform_right_face_grid(current)

        ## Getting transformed Front & Back Grids
        new_front_grid = gt.BottomRowLeft.transform_front_face_grid(current)
        new_back_grid = gt.BottomRowLeft.transform_back_face_grid(current)

        ## Updating grids for all faces where there was a change
        current.grid = new_front_grid
        current.left.grid = new_left_grid
        current.right.grid = new_right_grid
        current.opposite.grid = new_back_grid
        current.top.grid = new_top_grid
        current.bottom.grid = new_bottom_grid

    @verbose
    def bottom_row_right(cube: RubixCube, internal_req: bool = False) -> None:
        current = cube.current_perspective

        ## Getting transformed Top Grids
        new_top_grid = gt.BottomRowRight.transform_top_face_grid(current)
        new_bottom_grid = gt.BottomRowRight.transform_bottom_face_grid(current)

        ## Getting transformed Left & Right Grids
        new_left_grid = gt.BottomRowRight.transform_left_face_grid(current)
        new_right_grid = gt.BottomRowRight.transform_right_face_grid(current)

        ## Getting transformed Front & Back Grids
        new_front_grid = gt.BottomRowRight.transform_front_face_grid(current)
        new_back_grid = gt.BottomRowRight.transform_back_face_grid(current)

        ## Updating grids for all faces where there was a change
        current.grid = new_front_grid
        current.left.grid = new_left_grid
        current.right.grid = new_right_grid
        current.opposite.grid = new_back_grid
        current.top.grid = new_top_grid
        current.bottom.grid = new_bottom_grid


ROTATIONS = [
    Rotations.rotate_up,
    Rotations.rotate_down,
    Rotations.rotate_left_vertically,
    Rotations.rotate_left_horizontally,
    Rotations.rotate_right_vertically,
    Rotations.rotate_right_horizontally,
    Rotations.invert_vertically,
    Rotations.invert_horizontally,
]

SHIFTS = [
    Shifts.right_col_up,
    Shifts.right_col_down,
    Shifts.left_col_up,
    Shifts.left_col_down,
    Shifts.top_row_left,
    Shifts.top_row_right,
    Shifts.bottom_row_left,
    Shifts.bottom_row_right,
]
