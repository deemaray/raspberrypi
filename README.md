Raspberry Pi project
Automating Event Reminders on Raspberry Pi Using Khal 
Student number: 2846890
Introduction
In today's fast-paced world, keeping track of important events and deadlines is crucial for personal and professional productivity. This project aims to address this need by automating event reminders on a Raspberry Pi, a versatile and affordable computing platform. The goal was to ensure timely alerts for scheduled events, leveraging a simple, reliable, and local calendar system. Initially, the project explored integrating popular cloud-based calendar services such as Google Calendar and Outlook Calendar. However, these attempts faced several challenges, particularly with authentication and access permissions. This led to the decision to utilize khal, a terminal-based calendar program, which offered a straightforward and efficient solution for managing local calendar events. By automating reminders through this setup, the project demonstrates an effective way to enhance productivity without relying on complex or third-party cloud services. 

Virtual - The Code
1. Defined a `main()` function as the entry point of the script.
2. Set the start and end times for retrieving events within the next 5 minutes using the `datetime` module.
3. Converted the start and end times to string format.
4. Executed the Khal command `khal list` with the specified time range using `subprocess.Popen()`.
5. Captured the output from the Khal process and decoded it from bytes to a string format.
6. Checked if there are any events within the specified time range.
7. If events are found, printed the output from Khal to debug and called a function to check for alerts in the events.
8. If no events are found, printed a message indicating that no upcoming events were found.
9. Used `if __name__ == "__main__":` to ensure that the `main()` function is only executed if the script is run directly, not imported as a module.
10. Initialized the Pygame mixer module for handling audio playback.
11. The pyttsx3 library was used to convert event details into speech.
12. The system now announces details such as the event title and time, providing a more informative and user-friendly alert.

Challenges and Solutions
The journey to automate event reminders on the Raspberry Pi encountered several specific challenges and required precise solutions to overcome them. Here's a detailed account of these challenges and how each was addressed:
1. Google Calendar Integration:
   - Challenge:  Integrating Google Calendar using gcalcli encountered significant issues with OAuth2 authentication. The process required frequent manual intervention to authenticate, and Google often flagged the attempts as suspicious, blocking access.
   - Solution: After multiple attempts and troubleshooting sessions to stabilize the OAuth2 flow, it became clear that the integration was unreliable. This led to the decision to seek alternative calendar solutions that could operate more smoothly with the Raspberry Pi.
2. Outlook Calendar Integration:
   - Challenge: Outlook Calendar was considered next due to its robustness and widespread use in professional environments. However, the integration process faced hurdles with complex API configurations. The API required intricate setup steps and continuous authentication refreshes, which were cumbersome to maintain.
   - Solution: Despite trying various methods to streamline the API integration and automate the authentication refresh process, the complexities and ongoing maintenance challenges made this option impractical. The decision was made to explore simpler, more straightforward calendar applications.
3. Switching to Khal:
   - Challenge: The transition to khal, a terminal-based calendar application, required configuring and adapting to a different workflow. Initial configuration issues included setting up the calendar correctly and ensuring it operated as expected on the Raspberry Pi.
   - Solution: To address these issues, detailed steps were followed to install and configure khal:
     ```bash
     sudo apt-get update
     sudo apt-get install khal
     khal configure
     ```
     During configuration, the default calendar was set up, and the configuration file was verified for correctness. This setup process was repeated and fine-tuned until khal operated smoothly.
4. Adding Events and Script Development:
   - Challenge:*Adding events via the terminal needed precise date and time formatting. Additionally, writing a Python script to check for upcoming events and trigger alerts required parsing khal’s output accurately.
   - Solution: Manually added events were tested thoroughly to ensure the correct format:
     ```bash
     khal new "2024-05-21 09:00 1h Meeting with Team"
     ```
     The Python script was developed with detailed error handling and debugging statements to ensure it correctly parsed event dates and times. The script was refined iteratively, fixing issues like incorrect date parsing and handling edge cases
Through these steps, each challenge was systematically addressed, leading to a reliable and efficient automated event reminder system using khal on the Raspberry Pi.

Future Improvements
To enhance the functionality and user experience of the alarm system, several future improvements can be considered. First, integrating the alarm system with various calendar applications, such as Google Calendar or Microsoft Outlook, would allow for broader usability and convenience. Implementing a more sophisticated alert mechanism, including customizable sound notifications and visual pop-ups, could provide more effective alerts. Additionally, adding a user-friendly interface with options to set custom alert times, repeat notifications, and snooze functionality would make the system more versatile. Another potential improvement is incorporating machine learning algorithms to predict and prioritize important events based on user behavior and preferences. Finally, ensuring the system is compatible with multiple operating systems and devices, such as smartphones and smart home devices, would increase its accessibility and usefulness.

Video
This is a video about the Raspberry Pi Project. I introduced more details and the process of this project including the construction and the code. Here is the video link:____
Conclusions
Despite initial setbacks with cloud-based calendar services, the project successfully implemented a reliable and straightforward local calendar solution using khal. This approach eliminated dependency on external services, ensuring consistent and timely event reminders. The final solution is a testament to the effectiveness of leveraging local tools and scripting for automation tasks on the Raspberry Pi. Initially, the system was designed to alert users through a simple audio alarm. However, to enhance functionality and user experience, the final implementation uses a text-to-speech feature to announce the event details.. The final implementation goes beyond a basic audio alarm by incorporating text-to-speech technology, which announces event details to users. This enhancement provides a clearer, more detailed, and user-friendly alert system. 


