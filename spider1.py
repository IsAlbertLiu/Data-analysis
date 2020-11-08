from urllib import request
import re
import pandas as pd

# 定义将要获取数据的 URL
# url = "https://wh.lianjia.com/zufang/"
url = "https://wh.lianjia.com/zufang/pg1/#contentList"


# 获取每个信息的内容
root_pattern = '<div class="content__list--item--main">([\s\S]*?)</div>'
# 获取地区
get_area = '>\n([\s\S]*?)</a>\n'
get_area1 = '/">([\s\S]*?)</a>-<a href="'
# 定义获取小区名正则表达式
get_name = '</a>-<a title="([\s\S]*?)" href="/zufang'
# 定义获取价格正则表达式
get_price = '<span class="content__list--item-price"><em>([\s\S]*?)</em>'
# 定义获取户型正则表达式
get_huxing = '<i>/</i>\n          ([\s\S]*?)        <span class="hide">'
# 定义获取小区面积正则表达式
get_square = '<i>/</i>\n        ([\s\S]*?)㎡'


# 打开网址
r = request.urlopen(url)
# 获取的网址是 字节码（bytes）
htmls = r.read()
# 将字节码转换为html文本
htmls = str(htmls, encoding='utf-8')
# 输出获取的网址
# print(htmls)


# 定义想获取的根内容
root_htmls = re.findall(root_pattern,htmls)
print(type(root_htmls[1]))


# 定义数组，储存获取的地区数据
areas = []
# 定义数组，储存获取的价格数据
prices =[]
# 定义数组，储存获取的户型数据
huxings =[]
# 定义数组，储存获取的面积数据
squares =[]
# 定义数组，储存获取的小区名数据
names =[]

for html in root_htmls:
    # 获取数据
    area = re.findall(get_area1,html)
    price = re.findall(get_price,html)
    huxing = re.findall(get_huxing,html)
    square = re.findall(get_square,html)
    name = re.findall(get_name,html)

    # 将获取的数据进行类型转换，从 list 转换成 str 并且储存进定义的数组里面
    areas.append("".join(area))
    prices.append("".join(price))
    huxings.append("".join(huxing))
    squares.append("".join(square))
    names.append("".join(name))

    # 数据输出测试，查看输出的内容是否正确！！！
    # print(type(area),area)
    # print(price)
    # print(huxing)
    # print(square)
    # print(name)
    # areas = {'地区':area,'小区':name,'户型':huxing,'面积':square,'价格':price}
    # areass.append(areas)

# 定义 dataframe 类型，并且将 dataframe 类型储存进 csv 文件内
dataframe = pd.DataFrame({'地区':areas,'小区':names,'户型':huxings,'面积':squares,'价格':prices})
dataframe.to_csv("test1.csv", index=False, sep=',')
