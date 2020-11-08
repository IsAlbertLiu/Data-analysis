from urllib import request
import re


# <div class="room-anchor card-text p-relative" data-v-191d6a08>
# <span title="小由伊" data-v-191d6a08>小由伊</span>
# <div class="popular-ctnr p-absolute" data-v-191d6a08>
# <i class="icon-font icon-popular v-middle dp-i-block" data-v-191d6a08></i>
# <span class="v-middle" data-v-191d6a08>2.3 万</span>
# </div>
# </div>


class Spider():
    url = "https://live.bilibili.com/p/eden/area-tags?parentAreaId=2&areaId=0&visit_id=42jfqisk5ma0"
    root_pattern = '<div class="room-anchor card-text p-relative" data-v-191d6a08>([\s\S]*?)</div>'
    root_pattern_getAuthor = '<span title="[\s\S]*?" data-v-191d6a08>([\s\S]*?)</span>'
    root_pattern_get_author_number = '<span class="v-middle" data-v-191d6a08>([\s\S]*?)</span>'

    # 私有方法
    def __fetch_content(self):
        # 模拟浏览器访问地址
        r = request.urlopen(Spider.url)
        # bytes
        htmls = r.read()
        # 将字节码转换为html文本
        htmls = str(htmls, encoding='utf-8')
        return htmls

    # 分析获取的htmls,并且提取出主播的昵称和当前播放量
    def __analysis(self, htmls):
        root_htmls = re.findall(Spider.root_pattern, htmls)
        authors = []
        for html in root_htmls:
            name = re.findall(Spider.root_pattern_getAuthor, html)
            number = re.findall(Spider.root_pattern_get_author_number, html)
            author = {'name': name, 'number': number}
            authors.append(author)

        print('authors', authors)
        return authors

    # 对获取的作者姓名和数量格式进行调整
    def __refine(self, authors):
        l = lambda author: {
            'name': author['name'][0],
            'number': author['number'][0]
        }
        return map(l, authors)

    # 对作者列表进行排序
    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__sort_seed,reverse=True)
        return anchors

    def __sort_seed(self, anchor):
        # 查询出数字
        r = re.findall('\d*', anchor['number'])
        # 把查询出来的文本转换成数字
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    def __show(self, anchors):
        for anchor in anchors:
            print(anchor['name'] + '----------' + anchor['number'])

    # 入口方法
    def go(self):
        htmls = self.__fetch_content()
        authors = self.__analysis(htmls)
        authors = list(self.__refine(authors))
        # 进行排序
        anchors = self.__sort(authors)
        self.__show(anchors)


spider = Spider()
spider.go()