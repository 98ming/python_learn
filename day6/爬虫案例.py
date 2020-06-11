# 爬虫前奏：
# 明确目的
# 找到数据对应的网页
# 分析网页的结构找到数据所在的标签位置
#
# 模拟HTTP请求，向服务器发送这个请求，获取到服务器返回给我们的HTML
# 用正则表达式提取我们要的数据（名字、人气）
from urllib import request
import re


class Spider():
    url = 'https://www.huya.com/g/lol'
    name_pattern = '<span class="avatar fl">(.*?)</span>'
    num_pattern = '<span class="num">(.*?)</span>'

    def _fetch_content(self):
        r = request.urlopen(self.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        # print(htmls)
        return htmls

    def analysis(self, htmls):
        htmls_name = re.findall(self.name_pattern, htmls, re.S)
        htmls_num = re.findall(self.num_pattern, htmls, re.S)
        anchors = []
        nums = []
        res = []
        for html in htmls_name:
            name = re.findall('>(.*?)</i>', html)
            anchors.append(name[0])
        for html in htmls_num:
            num = re.findall('<i class="js-num">(.*?)</i>', html)
            nums.append(num[0])

        for i in range(0, len(anchors)):
            author = anchors[i]
            num = nums[i]
            res_angle = {'author': author, 'num': num}
            res.append(res_angle)
        return res

    def data_sort(self, res):
        res = sorted(res, key=self.__sort_seed, reverse=True)
        return res

    def __sort_seed(self, angle):
        # print(angle)
        r = re.findall('\d*', angle['num'])
        number = float(r[0])
        if '万' in angle['num']:
            number *= 10000
        return number

    def show(self,res):
        for i in range(0,len(res)):
            print('rank '+str(i+1)+':'+res[i]['author']+'   '+res[i]['num'])

    def go(self):
        htmls = self._fetch_content()
        res = self.analysis(htmls)
        res = self.data_sort(res)
        self.show(res)


spider = Spider()
spider.go()
