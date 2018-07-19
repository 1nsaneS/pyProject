import wx

class SpinnerFrame(wx.Frame):
	"""docstring for SpinnerFrame"""
	def __init__(self):
		wx.Frame.__init__(self,None,-1,'Spinner',
			size=(100,100))
		panel = wx.Panel(self,-1)
		sc = wx.SpinCtrl(panel,-1,'',(30,20),(80,-1))
		sc.SetRange(1,100)
		sc.SetValue(5)


if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = SpinnerFrame()
	frame.Show()
	app.MainLoop()