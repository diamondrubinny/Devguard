import time
import threading
import pyperclip
import re
import json
import logging
from pystray import Icon as TrayIcon, MenuItem as Item
from PIL import Image, ImageDraw
from plyer import notification

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class ClipboardGuardApp:
    def __init__(self):
        self.last_content = ""
        self.running = True
        self.icon = None
        
        # Regex patterns for sensitive data
        self.patterns = {
            'AWS Key': r'AKIA[0-9A-Z]{16}',
            'Private Key': r'-----BEGIN PRIVATE KEY-----',
            'Generic Secret': r'[a-zA-Z0-9]{40,}', 
            'Email': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        }

    def create_image(self):
        # Create a basic tray icon programmatically
        width = 64
        height = 64
        color1 = "black"
        color2 = "#00FF00" 
        
        image = Image.new('RGB', (width, height), color1)
        dc = ImageDraw.Draw(image)
        dc.rectangle((width // 4, height // 4, width * 3 // 4, height * 3 // 4), fill=color2)
        
        return image

    def send_notification(self, title, message):
        notification.notify(
            title=title,
            message=message,
            app_name='DevGuard',
            timeout=5
        )

    def is_sensitive(self, text):
        for label, pattern in self.patterns.items():
            if re.search(pattern, text):
                return label
        return None

    def try_prettify_json(self, text):
        try:
            parsed = json.loads(text)
            formatted = json.dumps(parsed, indent=4)
            if text == formatted:
                return text
            return formatted
        except (json.JSONDecodeError, TypeError):
            return text

    def monitor_loop(self):
        while self.running:
            try:
                current_content = pyperclip.paste()

                if current_content != self.last_content:
                    self.last_content = current_content
                    
                    # Check for sensitive data
                    alert_type = self.is_sensitive(current_content)
                    if alert_type:
                        self.send_notification(
                            "Security Alert",
                            f"Sensitive data detected ({alert_type}). Review your clipboard."
                        )
                    
                    # Attempt JSON formatting
                    else:
                        pretty = self.try_prettify_json(current_content)
                        if pretty != current_content:
                            pyperclip.copy(pretty)
                            self.last_content = pretty
                            self.send_notification(
                                "JSON Formatted",
                                "Clipboard content auto-formatted to JSON."
                            )

            except Exception as e:
                logging.error(f"Error: {e}")
            
            time.sleep(1)

    def stop_app(self, icon, item):
        self.running = False
        icon.stop()

    def run(self):
        monitor_thread = threading.Thread(target=self.monitor_loop)
        monitor_thread.daemon = True
        monitor_thread.start()

        image = self.create_image()
        menu = (Item('Exit', self.stop_app),)
        self.icon = TrayIcon("DevGuard", image, "DevGuard - Active", menu)
        self.icon.run()

if __name__ == "__main__":
    app = ClipboardGuardApp()
    app.run()
