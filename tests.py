def party_planner(cookies, people):
    leftovers = None
    num_each = None
    try:
        check = cookies / people
    except ZeroDivisionError:
        print('Cannot divide by 0, insert a positive number.')
    num_each = cookies // people
    leftovers = cookies % people

    return (num_each, leftovers)