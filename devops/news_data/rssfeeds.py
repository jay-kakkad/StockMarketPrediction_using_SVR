from newsplease import NewsPlease
import newspaper

source_urls = ["www.bloombergquint.com/markets"]
paper = newspaper.build("https://www.bloombergquint.com/", fetch_images=False,
                                number_threads=3, request_timeout=3, memoize_articles=False)

for article in paper.articles:
    url = article.url
    if any(source_url in url for source_url in source_urls):
        pass
    else:
        continue
    article = NewsPlease.from_url(url)

    title = article.title
    date_publish = article.date_modify
    description = article.description
    text = article.text
    print(date_publish)
    print(text)