# AutoSearch

AutoSearch is a Python script designed to automate random web searches by simulating mouse movements and keyboard inputs. It leverages the `pyautogui` library for controlling the mouse and keyboard, and the `random` and `string` libraries for generating random search queries.

## Usage

1. **Installation**: Make sure you have the necessary libraries installed. You can install them using `pip` with the following command:

    ```bash
    pip install pyautogui
    ```

2. **Initial Setup**: Place your cursor at the starting position and wait for 5 seconds.

3. **Run the Script**: Execute the script `autosearch.py` using Python. The script will then start performing random searches.

    ```bash
    python autosearch.py
    ```

## Script Explanation

- `random_mouse_movement()`: This function generates random mouse movements within a specified range.

- `type_and_enter(word)`: Types a given word and presses the 'enter' key to perform a search.

- `wait_for_page_to_load()`: It pauses script execution to wait for the page to load after a search.

- `close_and_open_tab()`: Closes the current browser tab and opens a new one.

- `search_word_randomly(num_searches)`: This function initiates random searches based on the provided number.

## Configuration

- `num_searches`: This variable defines the number of searches to perform. The default value is set to 20000. You can modify this value to control the number of searches.

## Requirements

- Python 3.x
- `pyautogui` library

## Running the Script

You can run the script using the following command:

```bash
python autosearch.py
