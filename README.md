# Battleship Game with Google Sheets Integration

This Python script implements a simple Battleship game where the player's grid and game status are updated in real-time on a Google Sheet.

## Overview

The script connects to a Google Sheet using the `gspread` library and Google Sheets API. It initializes a game grid, places ships on the computer's grid, and allows the player to make guesses. The results of the player's guesses are updated on the Google Sheet.

## Requirements

- Python 3.x
- `gspread` library
- `google-auth` library
- A Google Cloud Platform project with the Google Sheets API and Google Drive API enabled
- A service account with access to the Google Sheets and Drive APIs
- A `creds.json` file for authentication

## Installation

1. **Install the necessary libraries:**

   ```bash
   pip3 install -r requirements.txt
   ```

2. **Set up Google Sheets API and Google Drive API:**

   - Create a project in the [Google Cloud Console](https://console.cloud.google.com/).
   - Enable the Google Sheets API and Google Drive API.
   - Create a service account and download the `creds.json` file.

3. **Share your Google Sheet with the service account email address** (found in `creds.json) with edit access.

## Usage

1. **Prepare your Google Sheet:**

   - Create a new Google Sheet and name it `module` or adjust the `SHEET_NAME` variable in the script to match your sheet's name.
   - The script updates the first sheet (Sheet1) of the Google Sheets file.

2. **Run the script:**

   ```bash
   python run.py
   ```

   - The game will prompt you to enter your guesses in the format `x y` where `x` and `y` are coordinates on the grid.
   - The game will display "Hit!" if you guess correctly, or "Miss!" otherwise.
   - The grid and game state are updated in the Google Sheet in real-time.

## Functions

- `init_grid(size)`: Initializes a grid of size `size x size` with all cells set to `'O'`.
- `place_ships(grid, num_ships)`: Randomly places `num_ships` ships (`'S'`) on the grid and returns their positions.
- `update_sheet(sheet, grid, start_row)`: Updates the Google Sheet with the current grid state starting from `start_row`.

## Notes

- The game is limited to 10 turns.
- Adjust the `GRID_SIZE` and `NUM_SHIPS` constants as needed for different grid sizes or ship counts.
- The script assumes a grid size of 5x5 and 3 ships.

## Troubleshooting

- Ensure that the `creds.json` file is in the same directory as the script and is correctly configured.
- Verify that the Google Sheet name matches the `SHEET_NAME` variable.
- Ensure the Google Sheet is shared with the service account email.

