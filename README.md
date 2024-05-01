AUTOCLICKER
AutoClicker is a Python application designed to automate mouse clicks and keyboard presses at specified intervals. It is particularly useful for tasks that require repetitive actions, such as gaming or software testing.

USAGE
Download the Repository: Clone or download the repository to your local machine.
Install Dependencies: Ensure you have Python installed on your system. Install the required dependencies using pip:
bash
Copy code
pip install -r requirements.txt
Run the Application: Execute the Python script Autoclicker.py to start the AutoClicker application.
Set Interval and Action: Enter the desired interval (in seconds) between each action and select the action to perform from the dropdown menu.
Start/Stop: Click the "Start" button to begin the automated actions. Click "Stop" to pause the automation.
BUILD
To build the AutoClicker application into an executable file, follow these steps:

Install PyInstaller: If you haven't already, install PyInstaller using pip:
bash
Copy code
pip install pyinstaller
Navigate to the Project Directory: Open a terminal or command prompt and navigate to the directory containing the Autoclicker.py script.
Run PyInstaller Command: Use PyInstaller to build the executable file:
bash
Copy code
pyinstaller --onefile --windowed --icon=icon.ico --add-data="icon.ico;." Autoclicker.py
Find the Executable: After PyInstaller completes, navigate to the dist directory within your project folder. You will find the built executable file (Autoclicker.exe on Windows) there.
Run the Executable: Double-click the executable file to run the AutoClicker application without needing Python or any dependencies installed.
