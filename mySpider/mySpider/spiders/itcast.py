import scrapy


# class ItcastSpider(scrapy.Spider):
#     name = "itcast"
#     allowed_domains = ["itcast.cn"]
#     start_urls = ["https://www.itcast.cn/channel/teacher.shtml"]
#
#     def parse(self, response):
#         filename = 'teacher.html'
#         open(filename, 'wb').write(response.body)


from mySpider.items import ItcastItem


class Opp2Spider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.com']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):# 获取网站标题
        context = response.xpath('/html/head/title/text()')

        # 提取网站标题
        title = context.extract_first()
        print(title)

        # 存放老师信息的集合
        items = []
        test = response.xpath("//div[@class='li_txt']")
        for each in response.xpath("//div[@class='li_txt']"):
            # 将我们得到的数据封装到一个 `ItcastItem` 对象
            item = ItcastItem()
            # extract()方法返回的都是unicode字符串
            name = each.xpath("h3/text()").extract()
            title = each.xpath("h4/text()").extract()
            info = each.xpath("p/text()").extract()

            # xpath返回的是包含一个元素的列表
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            print(item)
            items.append(item)

        # 直接返回最后数据
        return items