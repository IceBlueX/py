
###pytho日期处理函数 parse
```python
from dateutil.parser import parse
parse("2003/09/25")
```
> 此函数可以处理任意格式的字符串类型日期，会返回一个datetime类型的日期

```python
import csv
def output_csv(path, data, csv_head):
    with open(path, 'w', encoding='UTF-8', newline='') as f:
        csv_write = csv.writer(f, dialect='excel')  # , dialect='excel'
        csv_write.writerow(csv_head)
        for row in data:
            csv_write.writerow(row)
    print(path, ' 写入完成！ 共 %d 条。 ' % len(data))
```
> 此函数将数据输出到csv

```python
import csv
import sys
from openpyxl import load_workbook

def reprint(*args):
    """
    实时刷新输出
    :param param:
    :return:
    """
    sys.stdout.write("\r" + str(args))
    sys.stdout.flush()

def read_xlsx(path, column_name):
    """
    # xlsx读取
    :param path:
    :param column_name:
    :return:
    """
    wb = load_workbook(path)
    ws = wb.active
    max_row = ws.max_row
    max_column = ws.max_column

    data = []
    field = {}

    # 查找前10行 填充字段对应的列数
    row = 0
    is_ok = False
    while row < max_row:
        reprint("当前进度:{}".format(row))
        # if row == 0:
        #     print([ws.cell(row + 1, (col + 1)).value for col in range(max_column)])

        if len(field) == len(column_name):
            is_ok = True
        else:
            for col in range(max_column):
                cell_data = ws.cell(row + 1, (col + 1)).value
                if cell_data in column_name:
                    field[col] = cell_data
        # print(field)
        if is_ok:
            # 开始读取
            data.append({
                field[col]: ws.cell(row + 1, (col + 1)).value for col in field.keys()
            })
        row += 1

    print(path, '读取完毕!')
    wb.close()
    return data


def read_csv(path, column_name):
    """
    # Csv 文件读取
    :param path:
    :param column_name:
    :return:
    """

    data = []
    field = {}
    with open(path, 'rt') as f:
        csv_r = csv.reader(f)

        # 查找前十行 填充对应字段的列数
        i = 1
        is_ok = False
        for row_csv in csv_r:
            # print(row_csv)
            reprint("当前进度:{}".format(i))

            if i == 1:
                col_count = len(row_csv)
                # print(row_csv)
                # print('最大列数', col_count)

            if len(field) == len(column_name):
                is_ok = True
            else:
                for col in range(col_count):

                    # print(row_csv[col], field, len(field), len(column_name))
                    if row_csv[col] in column_name:
                        field[col] = row_csv[col]

            if is_ok:
                data.append({
                    field[col]: row_csv[col] for col in field.keys() if len(row_csv) >= col_count
                })
            i += 1

    print(path, ' 读取完毕！ 共 %d 条。 ' % len(data))
    return data


```
> 此函数可以读取xlsx和csv 的指定列，可根据需要进行更改

```python
from functools import reduce

def list_dict_set(data):
    """
    list嵌套字典 专用去重
    :param data:
    :return:
    """
    run_function = lambda x, y: x if y in x else x + [y]
    return reduce(run_function, [[], ] + data)


def dict_slice(ori_dict, start, end):
    """
    字典类切片
    :param ori_dict: 字典
    :param start: 起始
    :param end: 终点
    :return:
    """
    slice_dict = {k: ori_dict[k] for k in list(ori_dict.keys())[start:end]}
    return slice_dict


def is_int_or_float(x):
    if isinstance(x, int) or isinstance(x, float):
        return True
    return False


def is_number(n):
    is_num = True
    try:
        num = float(n)
        # 检查 "nan"
        is_num = num == num   # 或者使用 `math.isnan(num)`
    except ValueError:
        is_num = False
    return is_num


def to_float(n):
    """
    将非数字的n转为0，其他转为float
    :param n: 
    :return: 
    """
    n = float(n) if is_int_or_float(n) else 0.0
    return n

```
> 各种数据处理函数