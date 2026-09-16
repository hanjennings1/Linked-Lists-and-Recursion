from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations 
    like insertion, recursion-based sum, search, and reverse.
    """

    # 1) Create a LinkedList instance
    my_list = LinkedList()

    # 2) Insert some sample data
    my_list.insert_at_front(11)
    my_list.insert_at_front(21)
    my_list.insert_at_front(10)
    my_list.insert_at_end(29)

    # 3) Display the list to verify insertion
    print("Initial list:")
    my_list.display()

    # 4) Call recursive_sum and print the result
    print("Sum of list:", my_list.recursive_sum())

    # 5) Call recursive_search with a target and print result
    print("Search for 11:", my_list.recursive_search(11))
    print("Search for 99:", my_list.recursive_search(99))

    # 6) Call recursive_reverse, then display the reversed list
    my_list.recursive_reverse()
    print("Reversed list:")
    my_list.display()