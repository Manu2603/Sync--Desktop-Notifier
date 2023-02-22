from plyer import notification
import time
title = '❌❌❌STUDY Alert❌❌❌!! \nIt\'s morning get up fast😊....\n'
message = 'Good Morning😊..\nToday you work tomorrow you achieve.'
count=0
while(count<3):
    notification.notify(title=title,
                    message=message,
                    app_icon=None,
                    timeout=10,
                    toast=False)
    count=count+1
    time.sleep(10)
