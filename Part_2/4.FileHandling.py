# Write a function which reads a file name, eg. `input.txt`, then print out all the lines in the files
# Additionally, display the lines in such a way that does not cause line misalignment
# Save all the printout into a separate file called `output.txt`
#
# ```
# 1.  ASDHKJAAS
# 2.  HNHSAFKSK
# ...
# 10. ASFASKFDS
# ...
# ```
def format_text_file(input_path: str):
    # ========================================================================
    f = open(input_path, "r")
    f1 = open("output.txt", "w")
    
    i = 1
    f.close
    for x in f:
        print(f"{i}.\t{x}")
        f1.write(f"{i}.\t{x}")
        i += 1
    f.close()
    f1.close()
    # ========================================================================
    


def main():
    format_text_file("input.txt")


if __name__ == "__main__":
    main()
