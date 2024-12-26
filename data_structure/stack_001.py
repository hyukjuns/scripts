inputs = [1,2,3]

def reverse(target_list):

    result = []
    while True:
        result.append(target_list.pop())
        if not target_list:
            return result

if __name__ == "__main__":
    print(reverse(inputs))
