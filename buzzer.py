import os
import time
try:
    from gpiozero import Buzzer  
    USING_GPIO = True
except ImportError:
    USING_GPIO = False  

class ActiveBuzzer:
    def __init__(self, pin=None):
        if USING_GPIO and pin is not None:
            self.buzzer = Buzzer(pin)
        else:
            self.buzzer = None  

    def on(self):
        if self.buzzer:
            self.buzzer.on()
        else:
            print("[ACTIVE] Buzzer ON")
            os.system("echo \a")  

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
            
            pass  
        else:
            print(f"[PASSIVE] Playing tone {freq}Hz for {duration}s")
            os.system("echo \a")  
            time.sleep(duration)
