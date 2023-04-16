# Veronika Musijaka 221RDB124 13.gr

def read_input():
    if input_type == "I":
        pattern = input().strip()
        text = input().strip()
    elif input_tipe == "F"
        file_name == input().strip()
        with open(file_name, 'r') as f:
            pattern = f.readLine().strip()
            text = f.readLine().strip()
    
    return (pattern, text)

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    occurrences = []
    p = 10**9+7
    x = 263

    pattern_hash = 0
    text_hash = 0
    x_len_pattern = 1

    for i in range(len(pattern)):
        pattern_hash = (pattern_hash*x + ord(pattern[i]))%p
        text_hash = (text_hash*x + ord(text[i]))%p
        x_len_pattern = (x_len_pattern*x)%p
    
    for i in range(len(text)-len(pattern)+1):
        if pattern_hash == text_hash:
            if pattern == text[i:i+len(pattern):]
                occurrences.append(i)
        if i < len(text)-len(pattern):
            text_hash = (text_hash - ord(text[i])*x_len_pattern)%p
            text_hash = (text_hash*x - ord(text[i+len(ppattern)]))%p

    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

