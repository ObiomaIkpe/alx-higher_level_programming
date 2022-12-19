def safe_print_list(my_list=[], x=0):
    num_of_items = 0

    try:
        for i  in range(x):
            print(my_list[i], end="")
            num_of_items += 1
    except IndexError:
        pass
    finally:
        print("")

    return (num_of_items)
