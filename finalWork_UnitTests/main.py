
from controller import controller


def main():
    list_numbers = controller([8, 0, 15, 4], [8, 3, 9, 7])

    avg = list_numbers.averages_lists()

    print(avg[0])
    print(avg[1])

    list_numbers.value_compare()


if __name__ == "__main__":
    main()
