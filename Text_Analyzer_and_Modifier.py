def get_num_of_characters(inputStr):
    count = 0
    for i in range(len(inputStr)):
        count += 1
    return count

def output_without_whitespace():
    no_whitespaces = inputStr.replace(' ', '')
    print('String with no whitespace: %s' % no_whitespaces)

if __name__ == '__main__':
    inputStr = input(str('Enter a sentence or phrase: \n'))
    print('You entered: %s\n' % inputStr)
    print('Number of characters:', get_num_of_characters(inputStr))   
    output_without_whitespace()
