
import uiautomator2 as ui

import time

d = ui.connect()

d(resourceId="com.kakao.talk:id/message_edit_text").click()

for i in range(10):
    d.send_keys("안녕하세요.", clear=True)
    d(resourceId="com.kakao.talk:id/send_layout").click()
    # time.sleep(0.5)

