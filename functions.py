from bs4 import BeautifulSoup
from pathlib import Path
from requests import get


def get_soup(url):
    return BeautifulSoup(get(url).text, "lxml")

def get_pictures(url, path, level):
    """
    获取指定页面的所有图片。
    这部分的代码怎么看怎么丑，但是没想到该怎么改，欢迎意见！
    """
    soup = get_soup(url)
    title = soup.h1.text
    print(f"{level * '  '}正在获取 {title}")
    Path(path + title).mkdir(exist_ok=True)
    # 前两个tag分别是封面和erocool的logo。
    urls = [tag["src"] for tag in soup.find_all("img", {"data-src": False})[2:]]
    for i, url in enumerate(urls):
        print(f"{(level + 1) * '  '}{url}")
        with open(f"{path}{title}/{i + 1}.jpg", "wb") as jpg:
            jpg.write(get(url).content)


if __name__ == "__main__":
    # 测试用本，好像是纯爱。
    get_pictures("https://zha.erocool.me/detail/1789763o338230.html", "./", 1)
