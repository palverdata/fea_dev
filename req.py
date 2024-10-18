from requests import get


def main():
    url = "https://www.google.com"
    response = get(url)  # 200
    print(f"Response status code: {response.status_code}")
    # print(f"Response content: {response.content}")

    url = "https://www.google.com/404"
    response = get(url)  # 404
    print(f"Response status code: {response.status_code}")
    # print(f"Response content: {response.content}")

    url = "https://mercury-api.anax.com.br/api/whatsapp/medias"
    response = get(url)  # 403
    print(f"Response status code: {response.status_code}")

    # https://servicodados.ibge.gov.br/api/docs/localidades
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/distritos/abc"
    response = get(url)  # 500
    print(f"Response status code: {response.status_code}")

    url = "https://servicodados.ibge.gov.br/api/v1/localidades/distritos"
    response = get(url, headers={"Accept": "application/json"})  # 200
    print(f"Response status code: {response.status_code}")
    print(response.json())


if __name__ == "__main__":
    main()
