# buzzer_control.py

import os
import time
try:
    from gpiozero import Buzzer  # Chạy thật trên Raspberry Pi
    USING_GPIO = True
except ImportError:
    USING_GPIO = False  # Dùng giả lập nếu không có phần cứng

class ActiveBuzzer:
    def __init__(self, pin=None):
        if USING_GPIO and pin is not None:
            self.buzzer = Buzzer(pin)
        else:
            self.buzzer = None  # Dùng beep giả lập nếu không có GPIO

    def on(self):
        if self.buzzer:
            self.buzzer.on()
        else:
            print("[ACTIVE] Buzzer ON")
            os.system("echo \a")  # Tiếng beep giả

    def off(self):
        if self.buzzer:
            self.buzzer.off()
        else:
            print("[ACTIVE] Buzzer OFF")

class PassiveBuzzer:
    def __init__(self, pin=None):
        if USING_GPIO and pin is not None:
            self.buzzer = Buzzer(pin)
        else:
            self.buzzer = None

    def play_tone(self, freq, duration=0.5):
        if self.buzzer:
            # Với buzzer thụ động thật → dùng PWM ngoài
            pass  # Để bạn tùy chỉnh sau
        else:
            print(f"[PASSIVE] Playing tone {freq}Hz for {duration}s")
            os.system("echo \a")  # Giả lập
            time.sleep(duration)
