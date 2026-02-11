import time
from datetime import datetime

cil = datetime(2026, 2, 4, 13, 20, 0)
ted = datetime.now()
delta = cil - ted

while True:
    if ted > cil:
        print("🔔 Upozornění: je 4. 2. 2026 13:20!")
    else:
        print(delta)
        time.sleep(1)

