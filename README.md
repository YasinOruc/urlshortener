**Description of the TinyURL URL Shortener App**

This application is a simple CLI-based URL shortener that uses the TinyURL API to convert long URLs into shorter versions. Users input a long URL, and the app generates a shortened version that can be directly copied and used. The app utilizes a `.env` file to securely store the API token, ensuring security and flexibility.

**Usage Example**

1. Start the application, and you’ll see a menu with options.
2. Select option `1` to enter a new URL.
3. Enter the long URL, such as: https://www.youtube.com.
4. The app generates a shortened URL, like https://tiny.one/abc123, and displays it directly in the console.
5. Copy the shortened URL and paste it into your browser.

**Notes**
- Choose option 2 from the main menu to exit the application.
- If the API token is invalid or the API is unreachable, an error message will be displayed.
