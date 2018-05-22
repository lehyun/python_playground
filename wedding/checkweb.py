import requests
import ctypes
import os.path
from pathlib import Path

last_index = 25

filename = Path("cache.txt")
if filename.is_file():
	file = open(filename, "r")
	line = file.readline()
	last_index = int(line)


link = "http://www.yakhyeon.or.kr/app/guide/inquiry.html"
f = requests.get(link)
#print(f.text)
content = f.text
found = content.find("<td>" + str(last_index) + "</td>")
if found >= 0:
	last_index = last_index + 1
	ctypes.windll.user32.MessageBoxW(0, "새로운 게시물이 있습니다.", "알림", 0)

file = open(filename, "w")
file.write(str(last_index))





