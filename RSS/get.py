import feedparser

# Replace this with the URL of the RSS feed you want to scrape
rss_url = 'https://aws.amazon.com/about-aws/whats-new/recent/feed/'

# Parse the RSS feed using the feedparser library
feed = feedparser.parse(rss_url)

# Loop through the entries in the feed and print out the title and link of each one
for entry in feed.entries:
    print(f'Title: {entry.title}')
    print(f'Link: {entry.link}\n')