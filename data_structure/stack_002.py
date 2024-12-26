

def deduplicate(arr):
    
    result = []
    for i in arr:
        if not result:
            result.append(i)
        else:
            if result[-1] == i:
                continue
            else:
                result.append(i)
    return result

if __name__ == "__main__":
    inputs = [[1,1,3,3,0,1,1],[4,4,4,3,3]]

    for input in inputs:
        print(deduplicate(input))
