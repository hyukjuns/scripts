
def work(progresses, speeds):
    progresses_list = list(progresses)

    target_tuple = zip(progresses_list,speeds)

    target_list = []
    for target in target_tuple:
        target_list.append(list(target))
    
    result = []
    while target_list:
        
        for target in target_list:
            if target[0] < 100:
                target[0] += target[1]
            else:
                continue
        cnt=0
        while target_list:
            if target_list[0][0] >= 100:
               cnt += 1
               target_list.pop(0)
            else:
                break
        
        if cnt != 0:
            result.append(cnt)

    return result
        


if __name__ == "__main__":
    inputs = {
            (93, 30, 55): [1, 30, 5],
            (95, 90, 99, 99, 80, 99): [1, 1, 1, 1, 1, 1]
        }

    for input in inputs.items():
        print(work(input[0],input[1]))


