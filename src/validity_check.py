from __future__ import annotations
from typing import TYPE_CHECKING
from predicate import FacePredicate

if TYPE_CHECKING:
    from cube_init_m import RubixCube


class CubeValidity:
    def is_cube_valid(cube: RubixCube) -> bool:
        if CubeValidity.are_opposite_faces_correct(cube):
            return False
        # Add more conditions to ensure structure and integrity of cube is maintained
        return True

    def are_opposite_faces_correct(cube: RubixCube) -> bool:
        cube_copy = cube.copy()
        cube_copy.reset_perspective()

        if not FacePredicate.are_faces_equal(
            cube.current_perspective.opposite.opposite, cube.current_perspective
        ) and not FacePredicate.are_faces_equal(
            cube.current_perspective.opposite, cube.current_perspective.opposite
        ):
            return False

        if not FacePredicate.are_faces_equal(
            cube.current_perspective.left.opposite, cube.current_perspective.right
        ) and not FacePredicate.are_faces_equal(
            cube.current_perspective.right.opposite, cube.current_perspective.left
        ):
            return False

        if not FacePredicate.are_faces_equal(
            cube.current_perspective.top.opposite, cube.current_perspective.bottom
        ) and not FacePredicate.are_faces_equal(
            cube.current_perspective.bottom.opposite, cube.current_perspective.top
        ):
            return False
        return True

    def is_connection_integrity_maintained() -> bool:
        pass
