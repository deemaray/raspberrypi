import subprocess
import datetime
from dateutil import parser
from dateutil.relativedelta import relativedelta
import time
import pygame
from gtts import gTTS

def get_upcoming_events():
    # Get the current time and 5 minutes later
    now = datetime.datetime.now()
    later = now + relativedelta(minutes=5)  # 5 minutes from now

    # Format the current and later time into strings
    date_str = now.strftime('%Y-%m-%d')
    later_str = later.strftime('%Y-%m-%d %H:%M')

    # Use subprocess to run 'khal list' command to get upcoming events
    result = subprocess.run(['khal', 'list', date_str, later_str],
                            capture_output=True, text=True)

    # Print debug information
    print("Debug - Checking events from:", date_str, "to", later_str)
    print("Debug - Khal Output:", result.stdout)

    return result.stdout

def check_events_for_alerts(events):
    # Get the current time
    current_time = datetime.datetime.now()

    # Loop through each line in the events output
    for line in events.strip().split('\n'):
        line = line.strip()  # Remove leading and trailing whitespaces

        # Check if line is not empty and contains a time range
        if line and "-" in line:
            try:
                # Split the line into datetime and event title
                date_time_part, title = line.split(' ', 1)

                # Extract the datetime part and parse it
                event_time = parser.parse(date_time_part.split('-')[0])
                print("Debug - Event Time:", event_time)  # Show parsed event time for debugging

                # Check if the event is about to start within the next 5 minutes
                if 0 <= (event_time - current_time).total_seconds() <= 300:
                    message = f"Hurry up! Your event '{title}' is about to start."
                    print(message)
                    text_to_speech(message)  # Convert message to speech
            except Exception as e:
                # Print error message if parsing fails
                print(f"Error parsing line '{line}': {e}")

def text_to_speech(message):
    # Create a TTS object and save the speech to a file
    tts = gTTS(text=message, lang='en')
    tts.save('/home/pi/sounds/event_notification.mp3')

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load and play the TTS file
    pygame.mixer.music.load('/home/pi/sounds/event_notification.mp3')
    pygame.mixer.music.play()

def main():
    while True:
        events = get_upcoming_events()  # Get upcoming events
        if events:
            check_events_for_alerts(events)  # Check if any event is about to start
        else:
            print("No upcoming events found.")
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()

