import wx;
import sys;


class main_window(wx.Frame):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        screenSize = wx.DisplaySize()
        """Constructor"""
        wx.Frame.__init__(self, parent=None, title="A Simple Grid", size=screenSize)
        self.panel = wx.Panel(self)

        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Apps
        self.open_file_button();
        self.panel.SetSizer(self.sizer);
        

    def open_file_button(self):
        btn_open_file = wx.Button(self.panel, wx.ID_CLOSE, "Open File")
        btn_open_file.Bind(wx.EVT_BUTTON, self.open_file)
        self.sizer.Add(btn_open_file, 0, wx.ALL, 10)

    def open_file(self):
        print "open file";

def create_main_window():
    app = wx.App()
    main = main_window()
    main.Show()
    app.MainLoop()
