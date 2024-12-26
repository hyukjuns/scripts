

array = [1, 5, 2, 6, 3, 7, 4]
commands = 	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
def sol(array, commands):

    result = []
    for command in commands:
        sliced_array = array[command[0]-1:command[1]]
        sliced_array.sort()
        res = sliced_array[command[2]-1]
        result.append(res)

    return result

if __name__ == "__main__":
    print(sol(array,commands))