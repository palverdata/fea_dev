from requests import get


def main():
    response = get("https://httpbin.org/headers")
    data = response.json()

    print(data["headers"]["User-Agent"])

    response = get(
        "https://httpbin.org/headers",
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
        },
    )

    data = response.json()

    print(data["headers"]["User-Agent"])


if __name__ == "__main__":
    main()
