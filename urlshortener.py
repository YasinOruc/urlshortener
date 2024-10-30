import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = 'https://api.tinyurl.com/create'
API_TOKEN = os.getenv('TINYURL_API_TOKEN')

def shorten_url(long_url):
    payload = {
        'url': long_url,
        'domain': 'tiny.one'
    }
    headers = {
        'Authorization': f'Bearer {API_TOKEN}',
        'Content-Type': 'application/json'
    }
    response = requests.post(BASE_URL, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json().get('data', {}).get('tiny_url')
    else:
        return None

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("=" * 40)
    print("       Welcome to the TinyURL Shortener")
    print("=" * 40)
    print("1. Shorten a new URL")
    print("2. Exit")
    print("=" * 40)

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1 or 2): ").strip()
        
        if choice == '1':
            long_url = input("Enter the long URL: ").strip()
            print("\nShortening URL, please wait...\n")
            short_url = shorten_url(long_url)
            
            if short_url:
                print(f"Your shortened URL: {short_url}")
                print("\nCopy this link and paste it in your browser.")
            else:
                print("Failed to shorten URL. Please check the API connection or API token.")
            
            input("\nPress Enter to continue...")
        
        elif choice == '2':
            clear_screen()
            print("Thank you for using the TinyURL Shortener. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1 or 2.")
            input("\nPress Enter to continue...")

if __name__ == '__main__':
    main()
