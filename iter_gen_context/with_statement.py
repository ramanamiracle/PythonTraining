import pathlib
import logging

with open("hello.txt", mode="w") as file:
    file.write("Hello, World!")

with open("input.txt") as in_file, open("output.txt", "w") as out_file:
    # Read content from input.txt
    # Transform the content
    # Write the transformed content to output.txt
    pass

file_path = pathlib.Path("hello.txt")

try:
    with file_path.open(mode="w") as file:
        file.write("Hello, World!")
except OSError as error:
    logging.error("Writing to file %s failed due to: %s", file_path, error)