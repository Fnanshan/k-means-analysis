# -*- encoding: utf-8 -*-
import xlwt  # 需要的模块

def txt_xls(filename, xlsname):
    """
    :文本转换成xls的函数
    :param filename txt文本文件名称、
    :param xlsname 表示转换后的excel文件名
    """
    try:
        f = open(filename)
        xls = xlwt.Workbook()
        # 生成excel的方法，声明excel
        sheet = xls.add_sheet('sheet1', cell_overwrite_ok=True)
        x = 0
        # 插入表头
        sheet.write(x, 0, 'taxiId')
        sheet.write(x, 1, 'dateTime')
        sheet.write(x, 2, 'longitude')
        sheet.write(x, 3, 'latitude')
        x = 1
        while True:
            # 按行循环，读取文本文件
            line = f.readline()
            if not line:
                break  # 如果没有内容，则退出循环
            for i in range(len(line.split(','))):
                item = line.split(',')[i]
                print('x :', x, '\ti :', i)
                sheet.write(x, i, item)  # x单元格维度，i 单元格经度
            x += 1  # excel另起一行
        f.close()
        xls.save(xlsname)  # 保存xls文件
    except:
        raise


if __name__ == "__main__":
    filename = "../data/1.txt"
    xlsname = "../data/1.xls"
    txt_xls(filename, xlsname)
