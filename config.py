# Add in format of the news channels as follows: (<Channel Name>, <Channel website>, <Sections of the channel to
# scrap>, <Attribute name of HTML element>, <Attribute content>)
output_columns = ["date", "week", "time", "headline", "news_channel", "section", "headline_attributes"]
news_channels = [
    ("SCMP", "https://www.scmp.com/", ["main", "economy/global-economy"],
     {"class": ["article__link", "article-title__article-link article-link"]}),
    # Seperator
    ("Bloomberg", "https://www.bloomberg.com/", ["economics", "markets"],
     {"data-component": ["headline"]}),
    # Seperator
    ("Wsj", "https://www.wsj.com/", ["economy", "markets"],
     {"class": ["css-dihi6s", "css-1wlqxh"]}),
    # Separator
    ("ChinaDaily", "https://www.chinadaily.com.cn/", ["world"],
     {"target": ["_blank"], "class": ["txt1", "txt2"]}),
    # Separator
    ("JapanTimes", "https://www.japantimes.co.jp/", ["news/world/"],
     {}),
    ("StraitsTimes", "https://www.straitstimes.com/", ["world"],
     {"class": ["card-title"]}),
    # Separator
    ("KoreanTimes", "https://www.koreatimes.co.kr/", ["www/section_602.html"],
     {"class": ["index_more_headline LoraMedium",
                "top_side_photo_top_headline LoraMedium",
                "top_side_sub_headline LoraMedium",
                "top_side_sub_headline LoraMedium",
                "aside_top10_headline LoraMedium"]}),
    # Separator
    ("Nikkei", "https://asia.nikkei.com/", ["Business/Markets"],
     {"class": ["ezstring-field"]}),
    # Separator
    ("CNBC", "https://www.cnbc.com/", ["world"],
     {"class": ["LatestNews-headline",
                "RiverHeadline-headline RiverHeadline-hasThumbnail",
                "Card-title"]})
]
