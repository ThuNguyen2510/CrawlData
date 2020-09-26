from scrapy.spiders import Spider
from scrapy.selector import Selector
from DataJapanese.comment import comment
import random


contents = ["Một trong những điều tuyệt nhất khi du ngoạn các ngọn núi ở Nhật Bản là mỗi ngọn núi đều mang một vẻ quyến rũ riêng. ",
            "Bộ mô hình diorama dễ thương lấy cảm hứng từ phim Công chúa Kaguya của Ghibli",
            "Vào mùa thu, sườn núi và các thung lũng được bao phủ bởi sắc màu rực rỡ.",
            "Bạn này mặc áo dài vào y như con gái việt nam vậy", "Mặt lúc nghiêm túc thì trông bảnh vl ra mà bình thường cứ ngáo ngáo thế nào ấy",
            "Nó thú vị Nhưng ko có mắc cười lắm Chứng tỏ nhà mầy càng gần biển muối càng trôi hết ra biển :)))))",
            "thực tế thì Adachin bây giờ còn nổi hơn cả linh vật chính thức là Byuubou (ビュー坊)"]


class CrawlerSpider(Spider):
    name = "DataJapanese"
    allowed_domains = ["jes.edu.vn"]
    start_urls = [
        "https://jes.edu.vn/luyen-thi-tieng-nhat",
    ]

    def parse(self, response):
        questions = Selector(response).xpath(
            '//aside[@class="widget widget_recent_entries"]/ul/li')
        for question in questions:
            item = comment()
            item['user_id'] = random.randrange(30) + 1
            item['blog_id'] = random.randrange(8) + 23
            item['content'] = contents[random.randrange(7)]
            yield item
