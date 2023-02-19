# Maksims Jepifanovs 221RDB137 10.grupa
# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])
opening_brackets_stack = []


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):

    li = 0
    
    for i, next in enumerate(text):

        if next in "([{":
            # Process opening bracket
            opening_brackets_stack.append(Bracket(next, i+1))
            li = i
            pass

        if next in ")]}":
            # Process closing bracket
            if len(opening_brackets_stack) < 1 or are_matching(opening_brackets_stack[len(opening_brackets_stack)-1].char, next) == False:
                li = i
                return li+1

            opening_brackets_stack.pop()


            pass
    if len(opening_brackets_stack) == 0:
        return 0
    else:
        return li+1


def main():
    text = input()

    mismatch = find_mismatch(text)

    # Printing answer
    if mismatch == 0:
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
