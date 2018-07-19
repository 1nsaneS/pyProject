import wx

class RadioBoxFrame(wx.Frame):
	"""docstring for RadioBoxFrame"""
	def __init__(self):
		wx.Frame.__init__(self,None,-1,'RadioBoxFrame',
			size=(350,200))
		panel = wx.Panel(self,-1)
		samplist = ('1','2','3','4','5')
		wx.RadioBox(panel,-1,'33333',(10,10),wx.DefaultSize,
			samplist,3,wx.RA_SPECIFY_COLS)

if __name__ == '__main__':
	app = wx.PySimpleApp()
	RadioBoxFrame().Show()
	app.MainLoop()
		
