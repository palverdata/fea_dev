from requests import get
from cloudscraper import create_scraper
# >>> get('https://www.radios.com.br/')
# <Response [403]>
# >>> get('https://oantagonista.com.br/brasil/governo-lula-fica-em-silencio-sobre-a-eliminacao-do-lider-do-hamas/')
# <Response [403]>


def main():
    url = "https://www.radios.com.br/"
    response = get(url)
    print(f"Response status code: {response.status_code}")

    url = "https://oantagonista.com.br/brasil/governo-lula-fica-em-silencio-sobre-a-eliminacao-do-lider-do-hamas/"
    response = get(url)
    print(f"Response status code: {response.status_code}")

    scraper = create_scraper()

    url = "https://www.radios.com.br/"

    response = scraper.get(url)

    print(f"Response status code: {response.status_code} with Cloudflare bypass")

    url = "https://oantagonista.com.br/brasil/governo-lula-fica-em-silencio-sobre-a-eliminacao-do-lider-do-hamas/"

    response = scraper.get(url)

    print(f"Response status code: {response.status_code} with Cloudflare bypass")


if __name__ == "__main__":
    main()
