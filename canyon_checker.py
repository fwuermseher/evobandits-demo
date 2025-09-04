import requests
from bs4 import BeautifulSoup
import time
import datetime
import random
from win10toast import ToastNotifier
import winsound

# List of product URLs to check
URLS = {
    "Silber Canyon": "https://www.canyon.com/de-de/rennrad/endurance-rennrad/endurace/allroad/endurace-allroad/4164.html?dwvar_4164_pv_rahmenfarbe=R138_P01&dwvar_4164_pv_rahmengroesse=XS",
    "Lila Canyon": "https://www.canyon.com/de-de/rennrad/endurance-rennrad/endurace/allroad/endurace-allroad/4164.html?dwvar_4164_pv_rahmenfarbe=R138_P02&dwvar_4164_pv_rahmengroesse=XS",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
]

toaster = ToastNotifier()
BELL_SOUND_PATH = "loud_bell.wav"

def play_bell_sound():
    for _ in range(5):  # repeat 5 times
        winsound.PlaySound(BELL_SOUND_PATH, winsound.SND_FILENAME | winsound.SND_ASYNC)
        time.sleep(1)  # short pause between repetitions

def get_random_headers():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept-Language": random.choice(["en-US,en;q=0.9", "de-DE,de;q=0.9", "fr-FR,fr;q=0.9"]),
        # Optionally add Referer or other headers here
    }

def check_availability():
    for variant_name, url in URLS.items():
        headers = get_random_headers()
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            # Look for the "Add to cart" button
            add_to_cart_button = soup.find("button", class_="js-addToCart-button")

            if add_to_cart_button and "In den Warenkorb" in add_to_cart_button.get_text():
                print(f"\n[{datetime.datetime.now()}] ✅ {variant_name} AVAILABLE!\n🔗 {url}\n")
                toaster.show_toast(
                    f"{variant_name} Available!",
                    f"The product variant '{variant_name}' is available on the page!",
                    duration=10, threaded=True
                )
                play_bell_sound()
            else:
                print(f"[{datetime.datetime.now()}] ❌ {variant_name} NOT available.")
        except Exception as e:
            print(f"[{datetime.datetime.now()}] ⚠️ Error checking {variant_name}: {e}")


def main():
    while True:
        check_availability()
        sleep_time = random.randint(30, 90)  # Random delay between 4.5 and 5.5 minutes
        print(f"Sleeping for {sleep_time} seconds...")
        time.sleep(sleep_time)

if __name__ == "__main__":
    main()
