import gspread
from google.oauth2.service_account import Credentials
import random
## Constants for grid size and number of ships
GRID_SIZE = 5
NUM_SHIPS = 3

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Authenticate and connect to the Google Sheet
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

SHEET_NAME = 'module'
SHEET = GSPREAD_CLIENT.open(SHEET_NAME).sheet1

# Funtion to initialize the game grid
def init_grid(size):
    return [['O'] * size for _ in range(size)]

# Funtion to place ships randmomly to the grid
def place_ships(grid, num_ships):
    ships = []
    while len(ships) < num_ships:
        x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        if grid[x][y] == 'O':
            grid[x][y] = 'S'
            ships.append((x, y))
    return ships

# Function to update the game grid n Googe Sheets
def update_sheet(sheet, grid, start_now):
    cell_list = sheet.range(start_row, 1, start_row + GRID_SIZE)
    for i, cell in enumerate(cell_list):
        row = i // GRIDE_SIZE
        col = i % GRID_SIZE
        cell.value = grid[row][col]
    sheet.update_cells(cell_list)

# Initialize grids for both player and computer
player_grid = init_grid(GRID_SIZE)
computer_grid = init_grid(GRID_SIZE)

# Place ships on the computer's grid
computer_ships = place_ships(computer_grid, NUM_SHIPS)

# Number of turns the player gets
turns = 10

update_sheet(SHEET, player_grid, 1)  # Update the sheet with the player's grid





     


    


    
   







  





