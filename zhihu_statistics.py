import re, xlrd, xlwt, time

file_path = "zhihu.txt"
gender_path = "Gender.xls"

id = u"识:[\s\S]*昵"
nickname = u"称:[\s\S]*, 性"
gender = u"别:[\s\S]*, 个"
signature = u"名:[\s\S]*"


def get_all_info_list(file_path):
    "获取标识和完整信息的列表(含去重的功能)"
    l = []
    info = []
    for line in open(file_path, encoding='utf-8'):
        s = re.search(id, line.strip())
        if s:
            ID = str(s.group()[3:-2])
            if ID not in l:
                l.append(str(s.group()[3:-2]))
                info.append(line.strip())
    return l, info


def get_gender_dic(info_list):
    "获取性别的个数"
    dic = {}
    for info in info_list:
        s = re.search(gender, info)
        if s:
            sex = str(s.group()[3:-3])
            if sex not in dic:
                dic[sex] = 1
            else:
                dic[sex] += 1
    return dic


def write_to_excel(excel_path, dictionary):
    "将内容写入Excel中"
    file = xlwt.Workbook(encoding='utf-8')
    table = file.add_sheet(excel_path)
    row = 0
    for item in dictionary:
        table.write(row, 0, item)
        table.write(row, 1, dictionary[item])
        row += 1
    file.save(excel_path)


def get_excel_info(file_name):
    "获取Excel表格信息"
    dictionary = {}
    excel = xlrd.open_workbook(file_name)
    table = excel.sheets()[0]
    sheet_by_name = excel.sheet_by_name(file_name)
    nrows = table.nrows
    for i in range(nrows):
        word = str(sheet_by_name.row_values(i)[0])
        number = int(sheet_by_name.row_values(i)[1])
        dictionary[word] = number
    return dictionary


def display_info(info_list):
    "打印完整信息"
    for info in info_list:
        print(info)
        time.sleep(0.3)


def main():
    id_list, info_list = get_all_info_list(file_path)
    gender_dic = get_gender_dic(info_list)
    write_to_excel(gender_path, gender_dic)
    print("完成!!")
    print("共", len(id_list), "条数据")
    # display_info(info_list)


if __name__ == '__main__':
    main()
