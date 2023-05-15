def logging(arr):
    def logg(data):
        arr.append(data)
    return logg



def find_count(pos, rem_len, history, log):
    history = history.copy()
    if abs(pos[0]) + abs(pos[1]) > rem_len:
        return 0
    if rem_len == 0:
        if pos == (0,0):
            log(history)
            return 1
        else:
            return 0
    if pos in history:
        return 0
    else:
        history.append(pos)
    sum = 0
    sum += find_count((pos[0] - 1, pos[1]), rem_len - 1, history, log)
    sum += find_count((pos[0] + 1, pos[1]), rem_len - 1, history, log)
    sum += find_count((pos[0], pos[1] - 1), rem_len - 1, history, log)
    sum += find_count((pos[0], pos[1] + 1), rem_len - 1, history, log)
    return sum

def count_of(n):
    data = []
    log = logging(data)
    num = find_count((0,0), n, [], log) // 2 // n
    return num, data

def change_for_command(data):
    n = len(data[0])
    new_data = []
    dict_commands = {(-1, 0):"Влево", (1, 0):"Вправо", (0, 1):"Вниз", (0, -1):"Вверх"}
    for log in data:
        new_data.append([])
        for i in range(n - 1):
            new_data[-1].append(dict_commands[(log[i + 1][0] - log[i][0], log[i + 1][1] - log[i][1])])
        new_data[-1].append(dict_commands[(log[0][0] - log[-1][0], log[0][1] - log[-1][1])])
    return new_data

def change_order(item):
    item = item.copy()
    change_dict = {"Вправо":"Влево", "Вверх":"Вниз", "Влево":"Вправо", "Вниз":"Вверх"}
    return list(reversed([change_dict[i] for i in item]))

def remove_repetition(data):
    n = len(data[0])
    data = data.copy()
    index = 0
    while index < len(data):
        item = data[index]
        #print(f'main item {item}')
        #print(f'delete miror {change_order(item)}')
        data.remove(change_order(item))
        for i in range(n-1):
            item = item[1:] + item[:1]
            #print(f'delete cycl {item}')
            data.remove(item)
            data.remove(change_order(item))
        index += 1
    return data

def create_poly_coords(item):
    coords = [(480, 400)]
    dict_command = {"Вверх":(0, -40), "Вниз":(0, 40), "Вправо":(40, 0), "Влево":(-40, 0)}
    for i in item:
        coords.append((coords[-1][0] + dict_command[i][0], coords[-1][1] + dict_command[i][1]))
    return coords

#data = remove_repetition(change_for_command(count_of(20)[1]))
#for item in data:
    #print(item)
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"For {2 * i} - {count_of(2 * i)[0]}")
    
