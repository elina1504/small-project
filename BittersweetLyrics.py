##created by ElinaSaufi

import time
import sys
import threading
from playsound import playsound

print ("created by Elina*___*")
song_thread = threading.Thread(target=lambda: playsound(r"C:\Users\L E N O V O\Desktop\Programming\Python\automation\simple project\BittersweetLyrics\bittersweet.mp3"))
song_thread.start()

def print_chorus():

    chorus = [
        "Now that it's over, you blame it all on me", #1
        "I know I should be bitter, but baby, right now I'm bittersweet", #2
        "I'm gettin' over what you put me through", #3
        "And I'd say I'm done cryin'", #4
        "but baby, I don't lie like you do ", #5
        "you~~ do~",#6
        "right now im bittersweet, emm~~", #7
        "right now im bittersweet~~",#8
        "One day I'll wake up sad", #9
        "but go to bed so glad", #10
        "Knowin' you know what you could've had ", #11
        "Now I'm choosin' me, it wasn't so easy ", #12
        "God forbid forever on my knees", #13
        "Know you want make it right, can't look me in the eyes", #14
        "Good for you",#15
        "I always think I knew", #16
    ]

    # Custom delay after each line (in seconds)
    delays = [1.5, 2.3, 1.5, 1.5,1.5,5,6.5,5,1.4,1.0, 1.5, 2.3, 2.3,2.5, 2.5,2.5,2.5]

    print("Bittersweet Chorus:\n")
    time.sleep(1.0)

    start_time = time.time()

    for i, line in enumerate(chorus):
        # Typing effect character by character
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)  # Adjust speed here

        print()  # Move to next line
        time.sleep(delays[i])  # Pause before next line

    # Keep terminal open
    input("\nPress Enter to exit...")

# Run the function
print_chorus()  
song_thread.join()

