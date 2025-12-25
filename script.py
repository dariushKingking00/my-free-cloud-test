‎script.py‎
+7
Lines changed: 7 additions & 0 deletions
Original file line number	Diff line number	Diff line change
@@ -0,0 +1,7 @@
import time
print("--- شروع عملیات در ابر ---")
# اینجا می‌توانید کدهای پیچیده خود را قرار دهید
for i in range(1, 11):
    print(f"در حال انجام پردازش مرحله {i}...")
    time.sleep(2) # شبیه‌سازی زمان‌بر بودن
print("--- پایان موفقیت‌آمیز عملیات ---")
