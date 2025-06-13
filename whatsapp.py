import pyautogui
import time
import webbrowser

# Step 1: Open WhatsApp Web chat with the target number
webbrowser.open("https://web.whatsapp.com/send?phone=918010364015")  # Change number here
time.sleep(15)  # Wait for page to load and user to scan QR

# Step 2: Send "hi" 100 times
for _ in range(100):
    pyautogui.typewrite("hi")
    pyautogui.press("enter")
    time.sleep(100)
