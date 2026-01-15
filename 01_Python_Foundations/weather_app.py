import requests
import sys

def get_weather(city_name):
    """
    Fetches weather data from wttr.in
    format=3 gives a one-line summary.
    """
    try:
        print(f"\n Connecting to satellite for {city_name}...")
        
        # The URL for the API
        url = f"https://wttr.in/{city_name}"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            print("\n" + "="*40)
            print(response.text) # The ASCII art is here
            print("="*40 + "\n")
        else:
            print(" Error: Could not find that city.")
            
    except Exception as e:
        print(f" Connection Error: {e}")

def main():
    print("--- ATMOSPHERE CLI v1.0 ---")
    
    while True:
        city = input("Enter City Name (or 'q' to quit): ").strip()
        
        if city.lower() == 'q':
            print("Disconnecting.")
            break
            
        if not city:
            print("Please enter a valid city name.")
            continue
            
        get_weather(city)

if __name__ == "__main__":
    # Check if user passed a city argument (e.g., python weather.py London)
    if len(sys.argv) > 1:
        get_weather(sys.argv[1])
    else:
        main()