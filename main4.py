def increment_string(string):
    numbers = ''
    if string[-1].isnumeric():
        for i in range(-1, -len(string), -1):
            if string[i].isnumeric():
                numbers+=(string[i])
            else:
                break
        string=list(string)
        for j in range(-1, -len(string), -1):
            if string[j].isnumeric():
                print(string[j])
                string.pop()
            else:
                pass

        # numbers=int(numbers)+1
        print(numbers)
        print(string)
        # print(string+numbers)
        # return numbers
    else:
        return string + "1"

print(increment_string("foobar01"))