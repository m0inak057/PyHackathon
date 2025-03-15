import speech_recognition as sr
import pyttsx3
import re  
import dateparser  

# Initialize speech and TTS engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    command = command.lower()
    if "hello" in command:
        return 'Hey there! Hope you doing fine. How can I help you'
    
    # Handle "exit" first
    if 'exit' in command or 'quit' in command or 'stop' in command:
        speak("Goodbye!")
        exit()

    # Lights control
    if 'lights' in command:
        if 'on' in command:
            return "Turning the lights on."
        elif 'off' in command: 
            return "Turning the lights off."

    # Temperature control
    elif 'temperature' in command:
        if 'increase' in command or 'up' in command: 
            return "Increasing the temperature by 2 degrees."
        elif 'decrease' in command or 'down' in command: 
            return "Decreasing the temperature by 2 degrees."

    elif 'alarm' in command and 'set' in command:  
        parsed_time = dateparser.parse(command, settings={'PREFER_DATES_FROM': 'future'})
        if parsed_time:
            formatted_time = parsed_time.strftime("%I:%M %p")
            return f"Alarm set for {formatted_time}."
        
        return "Could not detect a valid time. Please try again."
    return "Sorry, I am still in my learning phase and didn't understand that command."

def main():
    print("Virtual Assistant Activated. Say 'exit' to quit.")
    speak("Hello! How can I assist you today?")

    while True:
        try:
            with sr.Microphone() as source:
                print("\nListening...")
                audio = recognizer.listen(source, timeout=5)
                text = recognizer.recognize_google(audio)
                print(f"User Command: {text}")

                response = process_command(text)
                print(f"Assistant: {response}")
                speak(response)

        except sr.UnknownValueError:
            print("Could not understand audio.")
            speak("Please repeat your command.")
        except sr.RequestError:
            print("API error.")
            speak("Network issue. Try again later.")
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()