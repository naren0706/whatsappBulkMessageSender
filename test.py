import pywhatkit as py
import keyboard
import time
from datetime import datetime
import pandas as pd

def sendMessage(number,message):
    # Get the current date and time
    current_datetime = datetime.now()

    # Extract the hour from the datetime object
    current_hour = current_datetime.hour
    current_minute = current_datetime.minute

    # Simulate pressing and releasing the Enter key
    # py.sendwhatmsg("+918667516608","hi da boi",current_hour,int(current_minute)+1)
    py.sendwhatmsg("+91"+str(number),message,current_hour,int(current_minute)+1)
    keyboard.press_and_release("enter")

    time.sleep(3)
    # Press and release Ctrl+w
    keyboard.press_and_release('ctrl+w')
def readMessage():
    # Specify the file path
    file_path = 'D:/naren/piston/whatsappbulk message 2/message.txt'
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read the entire content of the file
        file_content = file.read()
    return file_content
def readXlFile():
    excel_file_path = 'path/to/your/excel/file.xlsx'
    df = pd.read_excel(excel_file_path)
