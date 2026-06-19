import time
import requests


async def fetch_all(urls):
    results = []
    for url in urls:
        time.sleep(1)
        resp = requests.get(url)
        results.append(resp.text)
    return results


async def main():
    fetch_all(["https://example.com"])
