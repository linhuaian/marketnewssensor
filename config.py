# Add in format of the news channels as follows: (<Channel Name>, <Channel website>, <Sections of the channel to
# scrap>, <Attribute name of HTML element>, <Attribute content>)
news_channels = [
    ("SCMP", "https://www.scmp.com/", ["int-1"],
     {"class": ["article__link", "article-title__article-link article-link"]}),
    # Seperator
    ("Bloomberg", "https://www.bloomberg.com/", ["economics", "markets"],
     {"data-component": ["headline"]}),
    # Seperator
    ("Wsj", "https://www.wsj.com/", ["economy", "markets"],
     {"class": ["css-dihi6s", "css-1wlqxh"]})
]
