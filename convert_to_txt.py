import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup


book = epub.read_epub(' Luo Guanzhong (Moss Roberts trans ), - Three Kingdoms (2014) - libgen.li.epub')

with open('threeKingdoms.txt', 'w') as f:
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_body_content())
            f.write(soup.get_text())
