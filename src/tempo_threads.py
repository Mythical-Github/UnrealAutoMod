import threading
import time

def background_task():
    """Function for the background thread."""
    while True:
        print("Background thread: Doing some work...")
        time.sleep(2)

# Create and start the background thread
background_thread = threading.Thread(target=background_task, daemon=True)
background_thread.start()
background_thread2 = threading.Thread(target=background_task, daemon=True)
background_thread2.start()
# Main script
try:
    # Main script continues running while background thread runs
    while True:
        print("Main thread: Continuing with other tasks...")
        time.sleep(1)
except KeyboardInterrupt:
    print("Main thread: Interrupted. Exiting...")
