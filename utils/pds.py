import pandas as pd


def cf(lines, filePath) -> bool:
    """
    summary: 将一个商品模板excel按照行数拆分成多个excel
    lines:需要拆分的行数
    """
    df = pd.read_excel(filePath)  # 源文件
    first_sheet = True
    for i in range(len(df)):
        if i % lines == 0:
            print(df[i:i + lines])
            if first_sheet:
                new_df = df[i:i + lines]
            else:
                new_df = pd.concat([df[1:5], df[i:i + lines]])  # df[1:5]是公共表头信息
            first_sheet = False
            new_df.to_excel(r'D:\test{}.xls'.format(i), index=False)  # 需要存储拆分excel表格的目录
    return True


if __name__ == "__main__":
    file_path = r'D:\goods_templates.xls'
    cf(lines=1000, filePath=file_path)
