########################################################################################################
# Projet : Content Folder                                                                              #
# Auteur : Soradev                                                                                     #
# Version : 1.0.0                                                                                      #
########################################################################################################
# Description :                                                                                        #
#   Generates the file tree of a selected folder                                                       #
########################################################################################################
# For any questions or contributions, please contact the author at sora.dev.pro@gmail.com              #
########################################################################################################

import os
import wx

class ContentFolderApp(wx.Frame):
    def __init__(self, btn_choose_text="Choose Folder", btn_copy_text="Copy"):
        super().__init__(None, title="ContentFolder", size=(800, 600))

        # Set the icon
        icon_path = "icon.ico"
        if os.path.exists(icon_path):
            self.SetIcon(wx.Icon(icon_path))

        # Allow modification of button text
        self.btn_choose_text = btn_choose_text
        self.btn_copy_text = btn_copy_text

        # Interface
        self.initUI()

    def initUI(self):
        panel = wx.Panel(self)
        panel.SetBackgroundColour("#2E2E2E")  # Dark background color

        vbox = wx.BoxSizer(wx.VERTICAL)

        # Text area to display the directory tree
        self.text_area = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL, size=(780, 450))
        self.text_area.SetBackgroundColour("#1E1E1E")  # Slightly darker background for text area
        self.text_area.SetForegroundColour("#D4D4D4")  # Light gray text
        self.text_area.SetFont(wx.Font(12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        vbox.Add(self.text_area, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        # Button to choose the folder
        self.btn_choose_folder = wx.Button(panel, label=self.btn_choose_text)
        self.btn_choose_folder.SetBackgroundColour("#3A3D41")  # Button dark gray background
        self.btn_choose_folder.SetForegroundColour("#D4D4D4")  # Light gray text
        self.btn_choose_folder.Bind(wx.EVT_BUTTON, self.choose_folder)
        vbox.Add(self.btn_choose_folder, flag=wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, border=5)

        # Button to copy to clipboard
        self.btn_copy = wx.Button(panel, label=self.btn_copy_text)
        self.btn_copy.SetBackgroundColour("#3A3D41")  # Button dark gray background
        self.btn_copy.SetForegroundColour("#D4D4D4")  # Light gray text
        self.btn_copy.Disable()
        self.btn_copy.Bind(wx.EVT_BUTTON, self.copy_to_clipboard)
        vbox.Add(self.btn_copy, flag=wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, border=5)

        panel.SetSizer(vbox)

    def generate_tree(self, path, prefix=""):
        tree = ""
        try:
            items = os.listdir(path)
            items.sort()
            pointers = ['├── '] * (len(items) - 1) + ['└── ']

            for pointer, item in zip(pointers, items):
                item_path = os.path.join(path, item)
                tree += prefix + pointer + item + "\n"
                if os.path.isdir(item_path):
                    extension = '│   ' if pointer == '├── ' else '    '
                    tree += self.generate_tree(item_path, prefix + extension)
        except Exception as e:
            tree += f"{prefix}[Error: {e}]\n"
        return tree

    def choose_folder(self, event):
        with wx.DirDialog(self, "Choose a folder", style=wx.DD_DEFAULT_STYLE) as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                folder_selected = dialog.GetPath()
                tree = os.path.basename(folder_selected) + "/\n" + self.generate_tree(folder_selected)
                self.text_area.SetValue(tree)
                self.btn_copy.Enable()

    def copy_to_clipboard(self, event):
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(wx.TextDataObject(self.text_area.GetValue()))
            wx.TheClipboard.Close()
            self.custom_messagebox("Success", "Directory tree copied to clipboard.")

    def custom_messagebox(self, title, message):
        dlg = wx.MessageDialog(self, message, title, wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()


# Run the application
if __name__ == "__main__":
    app = wx.App(False)  # Initialize wx.App before any other wxPython classes
    frame = ContentFolderApp(btn_choose_text="Browse", btn_copy_text="Export")
    frame.Show()
    app.MainLoop()
