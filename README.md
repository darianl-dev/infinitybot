# Infinity Discord Bot (Older Version)

Infinity is a Python-based Discord bot designed to enhance your server experience. This is the older version of the bot and comes with limited features, focused primarily on basic moderation and server management functionalities.

## Features
- Moderation: Kick, ban, mute, and warn users to maintain a healthy server environment.
- Server Management: Manage channels, roles, and permissions to customize your server.
- Informational Commands: Get server statistics, member information, and server rules.

## Installation
1. Clone this repository to your local machine.
   ```
   git clone https://github.com/itsretsu/infinity-bot.git
   ```

2. Install the required dependencies using pip.
   ```
   pip install -r requirements.txt
   ```

3. Rename the `config.example.py` file to `config.py`.

4. Edit the `config.py` file and provide your Discord bot token.

5. Run the bot using the following command:
   ```
   python infinity.py
   ```

## Configuration
Make sure to configure the `config.py` file before running the bot. You can set the bot token, prefix, and other settings according to your preferences.

## Usage
Once the bot is running and connected to your server, you can use the following commands:

- `i.kick @user reason`: Kick a user from the server.
- `i.ban @user reason`: Ban a user from the server.
- `i.mute @user duration reason`: Mute a user for a specified duration.
- `i.warn @user reason`: Warn a user for their behavior.

## Contributions
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and distribute this bot as per the license terms.
