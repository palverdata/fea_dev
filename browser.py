import asyncio

from playwright.async_api import async_playwright
from playwright_stealth import stealth_async
import random


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(
            "https://oantagonista.com.br/analise/padrao-datena-sobrinho-de-dilma-ameaca-cadeirada-em-nikolas/"
        )
        print(await page.title())
        content = await page.content()
        print(content)
        await browser.close()


async def main2():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)
        page = await browser.new_page(
            locale="en-US",
            timezone_id="UTC",
        )

        await stealth_async(page)

        await page.goto("https://www.radios.com.br/", timeout=60_000)

        await asyncio.sleep(1)

        for _ in range(random.randint(1, 3)):
            await page.evaluate(f"window.scrollBy(0, {random.randint(10, 100)})")
            await asyncio.sleep(random.randint(0, 1))

        await asyncio.sleep(1)

        print(await page.title())


if __name__ == "__main__":
    asyncio.run(main())
