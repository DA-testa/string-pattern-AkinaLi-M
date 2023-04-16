# Veronika Musijaka 221RDB124 13.gr

def read_input():
    # This function allows the user to provide input from the keyboard or a file.
    # The capital letter "I" or "F" is used to indicate which input type will follow.
    input_type = input().rstrip()
    file = "tests/06"
    if input_type == "I":
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == "F":
        with open(file, mode="r") as f:
            pattern = f.readLine().rstrip()
            text = f.readLine().rstrip()
    
    # Return both lines in one return statement, with the rstrip function to remove any trailing white space.
    return pattern, text

def print_occurrences(output):
    # This function prints the output and does not require any return statement.
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # This function uses the Rabin Karp algorithm to find the occurrences.
    pt = len(pattern)
    tx = len(text)
    result = []

    for i in range(tx - pt + 1):
        if pattern == text[i:i+pt]:
            result.append(i)

    return result


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

