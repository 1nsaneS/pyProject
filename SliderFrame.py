import wx

class SliderFrame(wx.Frame):
	"""docstring for SliderFrame"""
	def __init__(self):
		wx.Frame.__init__(self,None,-1,'Slider Frame',
			size=(300,350))
		panel = wx.Panel(self,-1)
		#self.count = 0
		slider = wx.Slider(panel,100,25,1,100,pos=(10,10),
			size=(250,-1),
			style=wx.SL_HORIZONTAL|wx.SL_AUTOTICKS|wx.SL_LABELS)
		slider.SetTickFreq(5)


if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = SliderFrame()
	frame.Show()
	app.MainLoop()
		