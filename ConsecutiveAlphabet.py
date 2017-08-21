__author__ = 'achandelkar'

def ConsecutiveAlphabets(S1):
    output_string = ""
    ch = 0
    i = 0
    count = 0

    while i < len(input_string):
        ch = input_string[i]
        i +=1
        count +=1

        while i < len(input_string) and ch == input_string[i]:
            i+=1
            count+=1
        output_string = output_string + ch
        output_string = output_string + str(count)


    return output_string


if __name__ == '__main__':
    input_string = eval(input("Enter a string with consecutive alphabets::"))
    res = ConsecutiveAlphabets(input_string)
    print("The new string is :: {}".format(res))