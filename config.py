# Add in format of the news channels as follows: (<Channel Name>, <Channel website>, <Sections of the channel to
# scrap>, <Attribute name of HTML element>, <Attribute content>)
news_channels = [
    ("Bloomberg", "https://www.bloomberg.com/", ["economics", "markets"], {"data-component": "headline"}),
    ("Wsj", "https://www.wsj.com/", ["economy", "markets"], {"class": "css-dihi6s", "class": "css-1wlqxh"})
]
