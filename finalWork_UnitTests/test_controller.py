import pytest
from finalWork_UnitTests.controller import controller

@pytest.fixture()
def lst1():
    return [1, 2, 3, 4, 5]


@pytest.fixture()
def lst2():
    return [3, 4, 5, 6, 7]


def test_init(lst1, lst2):
    list_ = controller(lst1, lst2)

    assert list_.list1 == lst1
    assert list_.list2 == lst2


def test_averages_lists(lst1, lst2):
    list_ = controller(lst1, lst2)
    assert list_.averages_lists() == (3, 5)


def test_value_first_list_greater(lst1, lst2, capfd):
    list_ = controller(lst2, lst1)

    list_.value_compare()
    captured = capfd.readouterr()

    assert captured.out.strip() == 'Первый список имеет большее среднее значение'


def test_value_second_list_greater(lst1, lst2, capfd):
    list_ = controller(lst1, lst2)

    list_.value_compare()
    captured = capfd.readouterr()

    assert captured.out.strip() == 'Второй список имеет большее среднее значение'


def test_values_equal(lst1, capfd):
    list_ = controller(lst1, lst1)

    list_.value_compare()
    captured = capfd.readouterr()

    assert captured.out.strip() == 'Средние значения равны'


@pytest.mark.parametrize('lst1, lst2, res', [
    ([], [1, 2, 3], (0, 2)),
    ([1, 2, 3], [], (2, 0)),
    ([], [], (0, 0))
])
def test_for_empty_list(lst1, lst2, res):
    list_ = controller(lst1, lst2)

    assert list_.averages_lists() == res


@pytest.mark.parametrize('lst1, lst2, res', [
    ([1], [1, 2, 3], (1, 2)),
    ([1, 2, 3], [1], (2, 1)),
    ([1], [1], (1, 1))
])
def test_one_item_list(lst1, lst2, res):
    list_ = controller(lst1, lst2)

    assert list_.averages_lists() == res


@pytest.mark.parametrize('lst1, lst2, res', [
    ([-4], [1, 2, 3], (-4, 2)),
    ([1, 2, 3], [-7], (2, -7)),
    ([-5], [-3], (-5, -3))
])
def test_negative_value(lst1, lst2, res):
    list_ = controller(lst1, lst2)

    assert list_.averages_lists() == res
