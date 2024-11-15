import curses
import random
import time

def lazy_cli(stdscr):
    curses.curs_set(0)  # Hide cursor
    current_row = 0

    options = [
        "Effortless Commanding",
        "Instant Excuses Generator",
        "It's Not My Job Delegator",
        "LazyLink Finder",
        "Rapid Report Faker",
        "Quit"
    ]

    def print_menu():
        height, width = stdscr.getmaxyx()
        
        # Check if the terminal is large enough
        if len(options) + 2 > height or max(len(row) for row in options) + 2 > width:
            stdscr.clear()
            stdscr.addstr(0, 0, "Terminal too small! Resize and try again.", curses.A_BOLD)
            stdscr.refresh()
            stdscr.getch()  # Wait for user to acknowledge
            return False  # Indicate menu cannot be displayed

        stdscr.clear()
        stdscr.addstr(0, 0, "Welcome to LazyCLI: Because working hard is overrated.", curses.A_BOLD)
        for idx, row in enumerate(options):
            # Truncate row if it exceeds terminal width
            truncated_row = row if len(row) < width - 4 else row[:width - 7] + "..."
            if idx == current_row:
                stdscr.addstr(idx + 1, 0, f"> {truncated_row}", curses.A_REVERSE)
            else:
                stdscr.addstr(idx + 1, 0, f"  {truncated_row}")
        stdscr.refresh()
        return True  # Indicate successful menu display

    while True:
        if not print_menu():  # If the menu couldn't be displayed, keep waiting
            continue
        
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(options) - 1:
            current_row += 1
        elif key == ord('\n'):  # Enter key pressed
            stdscr.clear()
            if current_row == len(options) - 1:  # Quit option
                stdscr.addstr(0, 0, "Goodbye! Stay efficient!", curses.A_BOLD)
                stdscr.refresh()
                time.sleep(2)
                break
            elif current_row == 0:  # Effortless Commanding
                stdscr.addstr(0, 0, "Launching Effortless Commanding...", curses.A_BOLD)
            elif current_row == 1:  # Instant Excuses Generator
                excuses = [
                    "Sorry, my cat deleted the file.",
                    "Oops, I was stuck in traffic (on a Saturday).",
                    "Technical difficulties (my internet took a nap)."
                ]
                stdscr.addstr(0, 0, f"Generated Excuse: {random.choice(excuses)}")
            elif current_row == 2:  # It's Not My Job Delegator
                stdscr.addstr(0, 0, "Delegating to... *rolling dice* You! Task assigned.")
            elif current_row == 3:  # LazyLink Finder
                stdscr.addstr(0, 0, "Finding your link: Here it is: https://lazywork.com")
            elif current_row == 4:  # Rapid Report Faker
                stdscr.addstr(0, 0, "Report: This is a sample report. Real one? Maybe later.")
            
            stdscr.refresh()
            stdscr.addstr("\n\nPress any key to return to the menu...")
            stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(lazy_cli)
