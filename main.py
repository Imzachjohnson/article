from newspaper import Article
import requests


API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def download_article(url):
    article = Article(url)
    article.download()
    article.parse()
    return article


def main():
    output = query(
        {
            "inputs": "Can you please let us know more details about your ",
        }
    )
    print(output)

    # url = "https://www.additudemag.com/productivity-hacks-chore-chart-adhd-brain/"
    # article = download_article(url)
    # print(article.text)


if __name__ == "__main__":
    main()
