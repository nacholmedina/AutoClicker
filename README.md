#AUTOCLICKER
AutoClicker is a Python application designed to automate mouse clicks and keyboard presses at specified intervals using PyautoGUI. Its main purpose it's to avoid inactivity ban from games or apps, and also excecuting simple tasks that require only one action to be performed in a determined time interval.

#INSTALLATION / DOWNLOAD
##To review/modify the code or execute the script via IDE
Download the Repository: Clone or download the repository to your local machine.
Install Dependencies: Ensure you have Python installed on your system. Install the required dependencies using pip:
bash
Copy code
pip install -r requirements.txt
Open terminal and excecute command: Python Autoclicker.pyw
To buid a .exe file just execute the command: 
pyinstaller --onefile --windowed --icon=icon.ico --add-data="icon.ico;." Autoclicker.py
Make sure your icon.ico file its inside the same folder as the main script, if you are still having truble loading the icon, make sure to add the file path to the command: 
pyinstaller --onefile --windowed --icon=icon.ico --add-data="YourIconFilePath";." Autoclicker.py
After following this process you will create a dist folder with an Autoclicker.exe file isnide it, just open it to execute the software. 

##To execute the file as it is to use it right away
Download the Autoclicker.exe file from [here](https://github.com/nacholmedina/AutoClicker/blob/main/dist/) (Might be detected as a suspicious download given its nature and main purpose) and open it, the soft will start inmediately. 

##Usage
Set Interval and Action: Enter the desired interval (in seconds) between each action and select the action to perform from the dropdown menu.
Start/Stop: Click the "Start" button to begin the automated actions. Click "Stop" to pause the automation.
![image](https://github.com/nacholmedina/AutoClicker/assets/54557023/3af381ff-ef0b-4b71-8538-2a7e84606f7d)

###If you have any doubts about this software, or want to contact me for any other reason feel free to reach out to me via [Linkedin](https://www.linkedin.com/in/nacholmedina/).
