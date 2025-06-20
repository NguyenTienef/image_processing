import os
import time

try:
    from gpiozero import PWMOutputDevice
    USING_GPIO = True
except ImportError:
    USING_GPIO = False

class PassiveBuzzer:
    NOTE_FREQ = {
        'B': 494,  # Si
        'A': 440,  # La
    }

    def __init__(self, pin=None):
        if USING_GPIO and pin is not None:
            self.buzzer = PWMOutputDevice(pin)
        else:
            self.buzzer = None

    def play_note(self, note, duration=0.3):
        freq = self.NOTE_FREQ.get(note.upper(), 440)
        if self.buzzer:
            self.buzzer.frequency = freq
            self.buzzer.value = 0.5  
            time.sleep(duration)
            self.buzzer.off()
        else:
            print(f"[SIM] Playing note {note} ({freq}Hz) for {duration}s")
            os.system("echo \a")  
            time.sleep(duration)
