import time
import xlrd
from datetime import datetime, timedelta

time_now = time.asctime()
print(time_now)


def update_graf():
    duty_graf = xlrd.open_workbook("back/Расписание_дежурств_Тех_поддержка_Октябрь_2023.xlsx")
    worksheet = duty_graf.sheet_by_index(0)
    rows = 15
    columns = 8
    result = []

    for row in range(rows):
        for column in range(columns):
            # Print the cell values with tab space
            x = worksheet.cell_value(row, column)
            y = worksheet.cell_value(row - 1, column) if row % 2 == 0 else x
            result.append([x, y])

    result2 = []
    for x in result:
        for y in x:
            if type(y) ==float:
                y = xlrd.xldate_as_datetime(y, 0)
            if y in ['Альберт', 'Александр', 'Юлия', 'Илья', 'Евгений', 'Михаил']:
                result2.append(x)

    for index, item in enumerate(result2):
        for index1, item1 in enumerate(item):
            if type(item1) == float:
                item[index1] = f"{xlrd.xldate_as_datetime(item1, 0) + timedelta(hours=8)}"
        item.sort()
    result2.sort()
    string = "\n".join([" ".join(x) for x in result2])
    with open("graf.txt", 'w+', encoding="utf-8") as file:
        file.write(string)


def get_duty():
    with open("graf.txt", "r", encoding="utf-8") as file:
        lines = [line.rstrip() for line in file]
        date = str(datetime.now()).split()[0]
        for x in lines:
            if date in x:
                x = x.split()[-1]
                with open("front/only_duty.txt", "w+", encoding="utf-8") as file2:
                    file2.write(x)
update_graf()
get_duty()
print(datetime.now())