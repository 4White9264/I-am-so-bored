import xlrd
import xlwt

# part of the code take from https://blog.csdn.net/u013250071/article/details/81911434



def read_excel_xls(path):
    output = []
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    for i in range(1, worksheet.nrows):
        for j in range(0, worksheet.ncols):
            print(worksheet.cell_value(i, j))  # 逐行逐列读取数据


            output.append((worksheet.cell_value(i, j)))



        # print() # 逐行逐列读取数据
    return output



def encrypt_last(data):
    name_number_output = []
    for name_number in data:

        if data.index(name_number)%2 == 0:
            if len(name_number)<= 2: #如果姓名字数小于或等于两个字
                name_number = name_number[0]+"*"
            elif len(name_number) ==3 or len(name_number) == 4: #如果姓名字数是三个字或者四个字
                name_number = name_number[0:1] + "**"
            else: #如果姓名字数在五个字或以上
                name_number = name_number[0] + (len(name_number)-1)*"*"
            name_number_output.append(name_number)
        else:
            name_number = str(name_number)[0:3] + "****" + str(name_number)[7:11]
            name_number_output.append(name_number)

    return name_number_output

# print(encrypt_last(data))

def write_excel_xls(path, input):
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet("加密后的姓名和电话")  # 在工作簿中新建一个表格
    sheet.write(0,0,"加密后的姓名")
    sheet.write(0,1,"加密后的电话")
    row = 1
    count = 0
    for index in range(0,len(input),2):
        sheet.write(row,0,input[index]) #填写加密后姓名
        sheet.write(row,1,input[index+1]) #填写加密后的电话
        row += 1
        print(input[index])




    workbook.save(path)  # 保存工作簿
    print("xls格式表格写入数据成功！")



data = read_excel_xls("加密前.xlsx")
write_excel_xls("加密后.xls",encrypt_last(data))