from ting_file_management.linkedList import LinkedList
import pytest


@pytest.fixture
def values_list():
    return ["x", "a", "b", "l", "a", "u"]


def test_if_it_is_possible_to_add_value_to_the_view_and_access_them():
    li = LinkedList()
    li.add("x")
    li.add("a")

    assert li.get_first() == "x"
    assert li.get_last() == "a"

    li.add_first("op")
    assert li.get_first() == "op"


def test_if_it_is_possible_to_start_the_list_with_values(values_list):
    li = LinkedList(values_list)

    assert li.get_first() == "x"
    assert li.get_last() == "u"

    li = LinkedList("test")

    assert li.get_first() == "test"
    assert li.get_last() == "test"
