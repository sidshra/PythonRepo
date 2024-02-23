from typing import List


# Assign the list ['a', 'b', 'c', 'd', 'e'] to a variable.
# Reverse the list, then insert ‘z’ at index 3, and finally append ‘o’ to the end.
def transform_list(input_list: List[str]) -> List[str]:
    output_list: List[str] = []
    # ========================================================================
    j = len(input_list)
    
    for i in range(j):
        if i == 3:
            output_list.append("z")
        output_list.append(input_list.pop())
    
    output_list.append("o")                              
    # ========================================================================
    return output_list


def main():
    result: List[str] = transform_list(["a", "b", "c", "d", "e"])
    expected: List[str] = ["e", "d", "c", "z", "b", "a", "o"]
    assert sorted(expected) == sorted(result)


if __name__ == "__main__":
    main()
