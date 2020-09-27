from scrapy.spiders import Spider
from scrapy.selector import Selector
from DataJapanese.answer import answer
import random


hiragana = ["あ", "い", "う", "え", "お", "か", "き", "く", "け", "こ", "が", "ぎ", "ぐ", "げ", "ご", "さ", "し", "す", "せ", "そ", "ざ", "じ", "ず",	"ぜ", "ぞ, ", "た", "ち", "つ",	"て"	, "と",	"だ"	, "ぢ"	, "づ"	, "で",	"ど",	"な",	"に",	"ぬ"	, "ね",	"の",	"は",	"ひ"	, "ふ",	"へ",	"ほ",	"ば",	"び",	"ぶ",	"べ"	, "ぼ",	"ぱ",	"ぴ",	"ぷ",	"ぺ",	"ぽ",	"ま",	"み",	"む"	, "め"	, "も",	"や"	,	"ゆ"	,	"よ",	"ら"	, "り",	"る", "れ"	, "ろ",	"わ"	, "ん"	, "を",
            "きゃ", "きゅ", "きょ", "しゃ", "しゅ", "しょ", "ちゃ", "ちゅ", "ちょ", "にゃ", "にゅ", "にょ", "ひゃ", "ひゅ", "ひょ", "みゃ", "みゅ", "みょ", "りゃ", "りゅ", "りょ", "ぎゃ", "ぎゅ", "ぎょ", "じゃ", "じゅ", "じょ", "びゃ", "びゅ", "びょ", "ぴゃ", "ぴゅ", "ぴょ"]

katakana = ["ア", "イ", "ウ", "エ", "オ", "カ", "キ", "ク", "ケ", "コ", "ガ", "ギ", "グ", "ゲ", "ゴ", "サ", "シ", "ス", "セ", "ソ", "ザ", "ジ", "ズ",	"ゼ", "ゾ, ", "タ", "チ", "ツ",	"テ"	, "ト",	"ダ"	, "ヂ"	, "ヅ"	, "デ",	"ド",	"ナ",	"ニ",	"ヌ"	, "ネ",	"ノ",	"ハ",	"ヒ"	, "フ",	"ヘ",	"ホ",	"バ",	"ビ",	"ブ",	"ベ"	, "ボ",	"パ",	"ピ",	"プ",	"ペ",	"ポ",	"マ",	"ミ",	"ム"	, "メ"	, "モ",	"ヤ"	,	"ユ"	,	"ヨ",	"ラ"	, "リ",	"ル", "レ"	, "ロ",	"ワ"	, "ン"	, "ヲ",
            "キャ", "キュ", "キョ", "シャ", "シュ", "ショ", "チャ", "チュ", "チョ", "ニャ", "ニュ", "ニョ", "ヒャ", "ヒュ", "ヒョ", "ミャ", "ミュ", "ミョ", "リャ", "リュ", "リョ", "ギャ", "ギュ", "ギョ", "ジャ", "ジュ", "ジョ", "ビャ", "ビュ", "ビョ", "ピャ", "ピュ", "ピョ"]

ans = ["a", "i", "u", "e", "o", "ka", "ki", "ku", "ke", "ko", "ga", "gi", "gu", "ge", "go", "sa", "shi", "su", "se", "so", "za", "ji", "zu",	"ze", "zo, ", "ta", "chi", "tsu",	"te"	, "to",	"da"	, "ji"	, "zu"	, "de",	"do",	"na",	"ni",	"nu"	, "ne",	"no",	"ha",	"hi"	, "fu",	"he",	"ho",	"ba",	"bi",	"bu",	"be"	, "bo",	"pa",	"pi",	"pu",	"pe",	"po",	"ma",	"mi",	"mu"	, "me"	, "mo",	"ya"	,	"yu"	,	"yo",	"ra"	, "ri",	"ru", "re"	, "ro",	"wa"	, "n"	, "wo",
       "kya", "kyu", "kyo", "sha", "shu", "sho", "cha", "chu", "cho", "nya", "nyu", "nyo", "hya", "hyu", "hyo", "mya", "myu", "myo", "rya", "ryu", "ryo", "gya", "gyu", "gyo", "ja", "ju", "jo", "bya", "byu", "byo", "pya", "pyu", "pyo"]


class CrawlerSpider(Spider):
    name = "DataJapanese"
    allowed_domains = ["thegioididong.com"]
    start_urls = [
        "https://www.thegioididong.com/dong-ho-thong-minh-apple#i:1",
    ]

    def parse(self, response):
        for a in range(len(ans)):  # mot cau hoi
            item = answer()
            item['question_id'] = 105 + a
            item['content'] = ans[a]
            item['is_true'] = 1
            yield item
        # for a in range(len(hiragana)):
        #     item = answer()
        #     item['question_id'] = a
        #     item['content'] = ans[random.choice(range(1,a)+range(a+1,len(hiragana)))]    
        #     item['is_true'] =0
