from pywinauto import application
from pywinauto.keyboard import send_keys
import lackey
import time
# 方式一：创建应用程序时可以，指定应用程序的合适的backend，start方法中指定启动的应用程序
# app = application.Application().start(r'F:\Program Files (x86)\Tencent\QQ\Bin\QQ.exe')
app = application.Application().start(r'F:\Program Files (x86)\DingDing\DingtalkLauncher.exe')
time.sleep(1)
# send_keys("{VK_RETURN}")

lackey.click(r'E:\project1\photo\ddhaoma.png')
time.sleep(2)
lackey.type("3091356800")
time.sleep(2)
# lackey.click(r'G:\daima\js\photo\qqmima.png')
lackey.doubleClick(r'E:\project1\photo\ddmima.png')
time.sleep(2)
lackey.type("3091")
# lackey.click(r"G:\daima\js\photo\qqdenglu.png")
#
