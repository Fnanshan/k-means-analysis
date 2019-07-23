'''
1.读取carData文件夹下的所有文件；
2.缺失值分析/异常值分析xls
    缺失值分析：
        缺失属性值：处理掉本行数据
            # 缺失值处理不完善，等待优化
                if len(item) != 0:
                    sheet.write(x, i, item)  # x 单元格经度，i 单元格纬度
                else:
                    break
        文件为空：过滤掉空文件——完成
    异常值分析：
        箱型图分析
3.打开文件；
    显示文件内容

'''

'''
如果文件很小，read()一次性读取最方便；
如果不能确定文件大小，反复调用read(size)比较保险；
调用readline()可以每次读取一行内容;
调用readlines()一次读取所有内容并按行返回list (如果是配置文件，调用readlines()最方便)
'''


# -*- encoding: utf-8 -*-
import xlwt  # 需要的模块


def txt_xls(filename, xlsname):
    """
    :文本转换成xls的函数
    :param filename txt文本文件名称
    :param xlsname 表示转换后的excel文件名
    文本格式：
        8 2008-02-04 07:01:13 116.36606 39.6841
        111,2008-02-02 17:37:18,116.62423,39.83224
        所以，先判断一下文本的分隔符是什么，然后再分割到表格。
            如果分割的空格为5个，则此文本以空格分割；
            如果分割的逗号为4个，则慈文本以逗号分割。

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
        # isCreate 是否创建xls文件
        isCreate = 1
        #  param txtSplitSymbol 文本的分割符号，可能是空格，可能是逗号
        txtSplitSymbol = ' '
        flag = 1
        while True:
            # 按行循环，读取文本文件
            line = f.readline()
            print('print line :\t', line)
            if not line:
                break  # 如果没有内容，则退出循环
            if len(line.split(' ')) == 5:
                txtSplitSymbol = ' '
            elif len(line.split(',')) == 4:
                txtSplitSymbol = ','
            for i in range(len(line.split(txtSplitSymbol))):
                # print('line.split(''):\t', line.split(txtSplitSymbol))
                item = line.split(txtSplitSymbol)[i]
                print('item :------', str(item), 'len(item) :------', len(item))
                # print('x:', x, 'i:', i, '--->', item)
                sheet.write(x, i, item)  # x 单元格维度，i 单元格经度
                # 判断本行有无缺失值，如果没有缺失值，则将本行插入到表格中；如果有缺失值，则判断下一行。
            x += 1  # excel另起一行
        f.close()
        # 根据isCreate的值判断是否创建xls
        with open(filename, 'r') as f:
            isCreate = len(f.read(1))
            print(isCreate)
        if isCreate:
            xls.save(xlsname)  # 保存xls文件
    except:
        raise


if __name__ == "__main__":
    filename = "../data/1.txt"
    xlsname = "../data/1.xls"
    txt_xls(filename, xlsname)
