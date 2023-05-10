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
    assert len(li) == 3


def test_if_it_is_possible_to_start_the_list_with_values(values_list):
    li = LinkedList(values_list)

    assert li.get_first() == "x"
    assert li.get_last() == "u"
    assert len(li) == 6

    li = LinkedList("test")

    assert li.get_first() == "test"
    assert li.get_last() == "test"
    assert len(li) == 1


def test_if_it_is_possible_to_remove_the_first_and_last_item_from_the_list(
    values_list,
):
    li = LinkedList(values_list)

    assert len(li) == 6
    assert li.pop_first() == "x"
    assert li.pop_last() == "u"
    assert len(li) == 4


def test_if_the_linked_list_is_iterable(values_list):
    li = LinkedList(values_list)

    result = list(li)

    assert result == values_list
    assert len(result) == len(li)


def test_if_it_is_possible_to_extend_the_linked_list(values_list):
    values = ["test", "one", "two", "three"]
    list_one = LinkedList(values_list)
    list_two = LinkedList(values)

    list_one.extend(list_two)

    assert list_one.get_first() == "x"
    assert list_one.get_last() == "three"
    assert list(list_one) == values_list + values
    assert len(list_one) == 10
