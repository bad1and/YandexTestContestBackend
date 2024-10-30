matrix = []
time_matrix = []

def matrix_create(entry):
    new_row = [entry[3]] + entry[:3] + entry[4:]
    matrix.append(new_row)

def calculate_total_minutes(start, end):

    days_diff = int(end[1]) - int(start[1])
    hours_diff = int(end[2]) - int(start[2])
    minutes_diff = int(end[3]) - int(start[3])


    total_time = days_diff * 24 * 60 + hours_diff * 60 + minutes_diff
    return total_time

def doit(matrix):

    matrix.sort(key=lambda row: (int(row[0]), int(row[1]), int(row[2]), int(row[3])))

    grouped = {}

    for x in range(len(matrix) - 1):
        if matrix[x][0] == matrix[x + 1][0]:
            if matrix[x][-1] == "A" and (matrix[x + 1][-1] in ["C", "S"]):
                total_time = calculate_total_minutes(matrix[x], matrix[x + 1])
                rocket_id = int(matrix[x][0])


                if rocket_id in grouped:
                    grouped[rocket_id] += total_time
                else:
                    grouped[rocket_id] = total_time


    result = " ".join(str(grouped[rocket_id]) for rocket_id in sorted(grouped.keys()))
    print(result)


for _ in range(int(input())):
    test = input().split()
    if test[-1] != "B":
        matrix_create(test)

doit(matrix)
