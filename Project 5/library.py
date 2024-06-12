import sys

def main():
    #Body of python script

    input_book = sys.argv[1] # Assign file path to variable
    three_letter_code = input_book.split('.')[0] # Grab 3 letter code only
    
    def longest(data):
        '''
        1: Initialize max_line string and line_location int variables
        2: Check if length of max_line is less than or equal to line
        2.1: and check if line_location is less than line being looked at
        3: Replace max_line and note the line_number if True, continue if not
        4: Return longest, latest line in list and its line number
        '''
        max_line = ''
        line_location = 0
        for line in data:
            if len(max_line) <= len(line[0]):
                max_line = line[0]
                line_location = int(line[1])
                
        return max_line, line_location
    
    def avg_len(data):
        '''
        1: Initialize sum_of_chars variable and define num_of_lines
        2: Sum all characters from lines
        3: Return the average line char length, round to nearest whole number
        '''
        sum_of_chars = 0
        num_of_lines = len(lines)
        for line in data:
            sum_of_chars += len(line[0])
        return round(sum_of_chars / num_of_lines)

    # Open and read input file and assign contents to a list of lists variable
    with open(input_book, 'r') as book:
        text = book.readlines()
        lines = [line.split('|')for line in text]

    # Find the average char length of all lines, assign to variable
    avg_line = avg_len(lines)

    # Sort the lines by line #, ascending, and assign to variable
    ordered_lines = sorted(lines, key = lambda line: int(line[1]))

    # After sorting lines, find longest line, assign text and line # to 2 vars
    longest_line, long_line_num = longest(ordered_lines)

    # Open/create new txt file, write each line as required by project
    with open(f'{three_letter_code}_book.txt', 'w') as writer:
        '''
        Line 1: Three letter code
        Line 2: Longest line and its line number
        Line 3: Average line character length
        Line 4 to end: Write each newly sorted line to individual line
        '''
        writer.write(f'{three_letter_code}\n')                            # 1
        writer.write(f'Longest line ({long_line_num}): {longest_line}\n') # 2
        writer.write(f'Average length: {avg_line}\n')                     # 3
        for line in ordered_lines:                                        # 4+
            writer.write(f'{line[0]}\n')

if __name__ == '__main__':
    main()