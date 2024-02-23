from typing import List, Dict


# Given 2 lists, 1 each for string keys and int values
# Convert and return a single dictionary, 100x the int values.
def convert_to_dict(key_list: List[str], value_list: List[int]) -> Dict[str, int]:
    output_dict: Dict[str, int] = {}
    # ========================================================================
    
    for i in range(len(key_list)):
        output_dict[key_list[i]] = value_list[i] * 100
  
    # ========================================================================
    return output_dict


def main():
    result: Dict[str, int] = convert_to_dict(["Ten", "Twenty", "Thirty"], [10, 20, 30])
    expected: Dict[str, int] = {"Ten": 1000, "Twenty": 2000, "Thirty": 3000}
    assert result == expected


if __name__ == "__main__":
    main()
