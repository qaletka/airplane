from src.plane import Plane
from assertpy import assert_that


def test_new_plane_has_total_flew_distance_is_0():
    plane_1 = Plane("new_plane", 200)
    assert plane_1.total_flew_distance == 0


def test_new_plane_has_0_occupied_seats():
    plane_1 = Plane("new_plane", 200)
    assert plane_1.number_of_occupied_seats == 0


def test_method_fly_single_usege():
    plane_1 = Plane("new_plane", 200)
    plane_1.fly(5000)
    assert plane_1.total_flew_distance == 5000


def test_method_fly_repeated_usege():
    plane_1 = Plane("new_plane", 200)
    plane_1.fly(5000)
    plane_1.fly(3000)
    assert plane_1.total_flew_distance == 8000


def test_plane_doesnt_require_a_service_after_9999_distance():
    plane_1 = Plane("new_plane", 200)
    plane_1.fly(9999)
    assert plane_1.is_service_required() is False


def test_plane_requires_a_service_after_10001_distance():
    plane_1 = Plane("new_plane", 200)
    plane_1.fly(10001)
    assert plane_1.is_service_required() is True


def test_method_board_passengers():
    plane_1 = Plane("new_plane", 200)
    assert plane_1.get_available_seats() == 200
    plane_1.board_passengers(180)
    assert plane_1.get_available_seats() == 20


def test_method_board_passengers_exceeding_number_of_seats():
    plane_1 = Plane("new_plane", 200)
    plane_1.board_passengers(201)
    assert plane_1.get_available_seats() == 0
    assert plane_1.number_of_occupied_seats == 200
