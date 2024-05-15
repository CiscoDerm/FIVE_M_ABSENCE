# Discord Bot for Absence Declaration

This repository contains a Discord bot script that allows users to declare their absence through a Discord interaction. The bot is built using `discord.py`, a Python wrapper for the Discord API.

## Features

- **Absence Declaration Modal**: Users can declare their absence by filling out a form with their name, date, and reason for absence.
- **Embeds**: The bot sends an embed message with the declared absence details.

## Setup and Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Install dependencies**:

    Make sure you have `discord.py` installed. You can install it using pip:

    ```sh
    pip install discord.py
    ```

3. **Configure the bot**:

    - Replace `TOKEN_BOT` in the script with your actual Discord bot token.
    - Replace `ID_CHANNEL` with the ID of the Discord channel where you want the bot to send the absence declaration button.

4. **Run the bot**:

    ```sh
    python absence.py
    ```

## Usage

Once the bot is running, it will send a message in the specified channel with a button labeled "Absence". Users can click this button to open a modal where they can enter their name, the date of absence, and the reason for their absence. Upon submission, the bot will send an embed message with the provided information.

## Script Overview

- **AbsenceModal**: A modal class that defines the form for absence declaration.
- **AbsenceView**: A view class that defines the button for triggering the absence modal.
- **on_ready**: An event that sends the initial message with the absence button when the bot is ready.
- **Main Execution**: The bot is run using the provided token.

## Contributing

If you would like to contribute to this project, please open an issue or submit a pull request.

