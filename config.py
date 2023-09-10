# Add in format of the news channels as follows: (<Channel Name>, <Channel website>, <Sections of the channel to
# scrap>, <Attribute name of HTML element>, <Attribute content>)
news_channels = [
    ("Wsj", "https://www.wsj.com/", ["economy", "markets"], "class", "WSJTheme--headlineText--He1ANr9C "),
    ("Bloomberg", "https://www.bloomberg.com/", ["economics", "markets"], "data-component", "headline")
]
