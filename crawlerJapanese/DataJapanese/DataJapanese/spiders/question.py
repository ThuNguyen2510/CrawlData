# from scrapy.spiders import Spider
# from scrapy.selector import Selector
# from DataJapanese.question import question
# import random


# hiragana = ["あ", "い", "う", "え", "お", "か", "き", "く", "け", "こ", "が", "ぎ","ぐ","げ","ご","さ","し","す","せ","そ","ざ","じ","ず",	"ぜ","ぞ, ","た","ち","つ",	"て"	,"と",	"だ"	,"ぢ"	,"づ"	,"で",	"ど",	"な",	"に",	"ぬ"	,"ね",	"の",	"は",	"ひ"	,"ふ",	"へ",	"ほ",	"ば",	"び",	"ぶ",	"べ"	,"ぼ",	"ぱ",	"ぴ",	"ぷ",	"ぺ",	"ぽ",	"ま",	"み",	"む"	,"め"	,"も",	"や"	,	"ゆ"	,	"よ",	"ら"	,"り",	"る","れ"	,"ろ",	"わ"	,"ん"	,"を",
# "きゃ","きゅ","きょ","しゃ","しゅ","しょ","ちゃ","ちゅ","ちょ","にゃ","にゅ","にょ","ひゃ","ひゅ","ひょ","みゃ","みゅ","みょ","りゃ","りゅ","りょ","ぎゃ","ぎゅ","ぎょ","じゃ","じゅ","じょ","びゃ","びゅ","びょ","ぴゃ","ぴゅ","ぴょ" ]

# katakana =["ア", "イ", "ウ", "エ", "オ", "カ", "キ", "ク", "ケ", "コ", "ガ", "ギ","グ","ゲ","ゴ","サ","シ","ス","セ","ソ","ザ","ジ","ズ",	"ゼ","ゾ, ","タ","チ","ツ",	"テ"	,"ト",	"ダ"	,"ヂ"	,"ヅ"	,"デ",	"ド",	"ナ",	"ニ",	"ヌ"	,"ネ",	"ノ",	"ハ",	"ヒ"	,"フ",	"ヘ",	"ホ",	"バ",	"ビ",	"ブ",	"ベ"	,"ボ",	"パ",	"ピ",	"プ",	"ペ",	"ポ",	"マ",	"ミ",	"ム"	,"メ"	,"モ",	"ヤ"	,	"ユ"	,	"ヨ",	"ラ"	,"リ",	"ル","レ"	,"ロ",	"ワ"	,"ン"	,"ヲ",
# "キャ","キュ","キョ","シャ","シュ","ショ","チャ","チュ","チョ","ニャ","ニュ","ニョ","ヒャ","ヒュ","ヒョ","ミャ","ミュ","ミョ","リャ","リュ","リョ","ギャ","ギュ","ギョ","ジャ","ジュ","ジョ","ビャ","ビュ","ビョ","ピャ","ピュ","ピョ" ]
 
 
# class CrawlerSpider(Spider):
#     name = "DataJapanese"
#     allowed_domains = ["thegioididong.com"]
#     start_urls = [
#         "https://www.thegioididong.com/dong-ho-thong-minh-apple#i:1",
#     ]

#     def parse(self, response):
#         # questions = Selector(response).xpath(
#         #     '///ul[@class="homeproduct filter-cate zoom2020"]/li')
#         # questions= 104
#         for a in range(len(hiragana)):
#             print(a)
#             item = question()
#             # item['lesson_id'] = 1
#             # item['content'] = hiragana[a]
#             item['lesson_id'] = 2
#             item['content'] = katakana[a]
#             yield item
