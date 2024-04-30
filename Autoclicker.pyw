import wx
import time
import threading
import pyautogui
import webbrowser

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="AutoClicker", size=(300, 250))
        self.icon = wx.Icon("icon.ico", wx.BITMAP_TYPE_ICO)  # Load icon from file
        self.SetIcon(self.icon)
        panel = wx.Panel(self)
        panel.SetBackgroundColour(wx.Colour(240, 240, 240))

        self.interval_text = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(100, -1))
        self.interval_text.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

        self.action_choices = ["Shift", "Space", "Enter", "Right Click", "Left Click"]
        self.action_combo = wx.ComboBox(panel, choices=self.action_choices, style=wx.CB_READONLY)

        self.selected_action = self.action_choices[self.action_combo.GetSelection()]  # Default action

        self.action_combo.Bind(wx.EVT_COMBOBOX, self.on_action_select)

        self.start_stop_button = wx.Button(panel, label="Start")
        self.start_stop_button.SetBackgroundColour(wx.Colour(0, 128, 0))  # Set button color
        self.start_stop_button.SetForegroundColour(wx.WHITE)  # Set text color
        self.start_stop_button.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))  # Set font

        self.countdown_text = wx.StaticText(panel, label="      No actions to be performed")
        countdown_box = wx.BoxSizer(wx.HORIZONTAL)
        countdown_box.AddStretchSpacer()
        countdown_box.Add(self.countdown_text, flag=wx.LEFT, border=25)

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(wx.StaticText(panel, label="Interval (seconds):"), flag=wx.TOP, border=20)
        hbox.Add((10, 10), 0)
        hbox.Add(self.interval_text, flag=wx.EXPAND|wx.LEFT|wx.TOP, border=15)
        vbox.Add(hbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP|wx.BOTTOM, border=20)
        vbox.Add(wx.StaticText(panel, label="Action:"), flag=wx.LEFT|wx.BOTTOM, border=10)
        vbox.Add(self.action_combo, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM, border=10)
        vbox.Add(self.start_stop_button, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM, border=-5)

        # Add bottom message and LinkedIn icon
        hbox_bottom = wx.BoxSizer(wx.HORIZONTAL)
        hbox_bottom.AddStretchSpacer()
        created_by_text = wx.StaticText(panel, label="Created with ♥ by @nacholmedina", style=wx.ALIGN_CENTER_VERTICAL)
        created_by_text.SetMinSize(created_by_text.GetBestSize())  # Adjust size to fit text
        hbox_bottom.Add(created_by_text, flag=wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, border=20)
        linkedin_button = wx.BitmapButton(panel, bitmap=wx.Bitmap("linkedin_icon.ico", wx.BITMAP_TYPE_ICO ), size=(24, 24))
        linkedin_button.Bind(wx.EVT_BUTTON, self.on_open_linkedin)
        hbox_bottom.Add(linkedin_button, flag=wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, border=15)
        hbox_bottom.AddStretchSpacer()

        vbox.Add(hbox_bottom, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM, border=10)

        panel.SetSizer(vbox)

        self.start_stop_button.Bind(wx.EVT_BUTTON, self.on_toggle_start_stop)

        self.interval = 7

        self.autoclick_thread = None
        self.keep_running = threading.Event()
        self.is_running = False

    def on_toggle_start_stop(self, event):
        if not self.is_running:
            try:
                interval = int(self.interval_text.GetValue())
                if interval <= 0:
                    raise ValueError
            except ValueError:
                wx.MessageBox("Please enter a valid positive integer for interval", "Error", wx.OK | wx.ICON_ERROR)
                return
            self.start_stop_button.SetBackgroundColour(wx.RED)
            self.interval = interval
            self.selected_action = self.action_choices[self.action_combo.GetSelection()]  # Assign action based on current selection
            self.keep_running.set()
            self.autoclick_thread = threading.Thread(target=self.auto_click)
            self.autoclick_thread.start()
            self.start_stop_button.SetLabel("Stop")
            self.interval_text.SetFocus()
            self.is_running = True
        else:
            self.keep_running.clear()
            self.countdown_text.SetLabel("      No actions to be performed")
            self.start_stop_button.SetLabel("Start")
            self.start_stop_button.SetBackgroundColour(wx.Colour(0, 128, 0))
            self.is_running = False

    def on_action_select(self, event):
        self.selected_action = self.action_choices[event.GetSelection()]

    def countdown(self, starting_time):
        for i in range(starting_time):
            self.countdown_text.SetLabel(f"      Next action in: {starting_time}")
            time.sleep(1)
            starting_time -= 1

    def auto_click(self):
        selected_action = self.selected_action
        while self.keep_running.is_set():
            if selected_action == "Right Click":
                self.countdown(self.interval)
                if self.is_running == True:
                    pyautogui.rightClick()
            elif selected_action == "Left Click":
                self.countdown(self.interval)
                if self.is_running == True:
                    pyautogui.leftClick()
            elif selected_action == "Shift":
                self.countdown(self.interval)
                if self.is_running == True:
                    pyautogui.press("shift")
            elif selected_action == "Space":
                self.countdown(self.interval)
                if self.is_running == True:
                    pyautogui.press("space")
            elif selected_action == "Enter":
                self.countdown(self.interval)
                if self.is_running == True:
                    pyautogui.press("enter")

    def on_open_linkedin(self, event):
        webbrowser.open("https://www.linkedin.com/in/nacholmedina/")

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
