# from ting_file_management.priority_queue import PriorityQueue
from ting_file_management.priority_queue import PriorityQueue
import pytest


@pytest.fixture
def high_priority():
    return {
        "nome_do_arquivo": "dir/xablau.txt",
        "qtd_linhas": 4,
        "linhas_do_arquivo": ["bla", "xablau", "new", "map"],
    }


@pytest.fixture
def regular_priority():
    return {
        "nome_do_arquivo": "dir/regular.txt",
        "qtd_linhas": 6,
        "linhas_do_arquivo": [
            "bla",
            "regular",
            "xablau",
            "new",
            "map",
            "milk",
        ],
    }


def test_basic_priority_queueing(high_priority, regular_priority):
    priority_queue = PriorityQueue()

    priority_queue.enqueue(regular_priority)
    assert len(priority_queue) == 1
    assert priority_queue.search(0) == regular_priority

    priority_queue.enqueue(high_priority)
    assert len(priority_queue) == 2
    assert priority_queue.search(0) == high_priority

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(10)

    assert priority_queue.dequeue() == high_priority
    assert priority_queue.search(0) == regular_priority
    assert len(priority_queue) == 1

    assert priority_queue.dequeue() == regular_priority
    assert len(priority_queue) == 0
