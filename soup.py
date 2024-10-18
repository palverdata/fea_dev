from requests import get
from bs4 import BeautifulSoup
import json


def main():
    url = "https://g1.globo.com/sp/sao-paulo/eleicoes/2024/noticia/2024/10/18/nunes-cancela-participacao-em-debates-pela-3a-vez-e-sbt-revoga-encontro-que-aconteceria-nesta-sexta-feira.ghtml"
    response = get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.find("h1", class_="content-head__title")

    print(title.text)

    subtitle = soup.find("h2", class_="content-head__subtitle")

    print(subtitle.text)

    content = soup.find("article", attrs={"itemprop": "articleBody"})

    paragraphs = content.find_all("p")

    for paragraph in paragraphs:
        print(paragraph.text)

    meta_tags = soup.find_all("meta", attrs={"content": True})

    for meta_tag in meta_tags:
        label = (
            meta_tag.get("name") or meta_tag.get("property") or meta_tag.get("itemprop")
        )
        print(f"[{label}]", meta_tag["content"][:30] + "...")

    ld_json_list = soup.find_all("script", type="application/ld+json")

    for ld_json in ld_json_list:
        parsed = json.loads(ld_json.string)

        print(parsed)


if __name__ == "__main__":
    main()
