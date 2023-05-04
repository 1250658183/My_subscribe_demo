import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print(f"Focus for {seconds // 60} minute(s) and {seconds % 60} second(s) remaining.")
        time.sleep(1)
        seconds -= 1
    print("Time's up! Take a break.")

focus_timer(25) # 25分钟专注时间，可以根据需要修改时间
