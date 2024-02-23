# Print out a pattern like this programmatically with n
# n = the number of star equivalent to how wide the wing is
# there is 1 space in between the * on each line
# eg. in this case n = 4
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
#
# eg. in this case n = 1
# *
# * *
# *
def print_pattern(n: int):
    # ========================================================================
    str_print = ""
    # to print from '1' to 'n+1' row in increasing order
    for i in range(n+1):
        str_print = str_print + "* "
        print(str_print)

    # to print from 'n' to '1' row in decreasing order
    for i in range(n):
        str_ln = len(str_print)
        str_print = str_print[2:str_ln]
        print(str_print)

    # ========================================================================
    


def main():
    print_pattern(1)
    print_pattern(4)
    print_pattern(10)


if __name__ == "__main__":
    main()
