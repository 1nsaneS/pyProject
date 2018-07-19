import wx

class CheckBoxFrame(wx.Frame):
	"""docstring for CheckBoxFrame"""
	def __init__(self):
		wx.Frame.__init__(self,None,-1,'CheckBoxFrame',
			size=(150,200))
		panel = wx.Panel(self,-1)
		wx.CheckBox(panel,-1,'1',(35,40),(150,20))
		wx.CheckBox(panel,-1,'2',(35,60),(150,20))
		wx.CheckBox(panel,-1,'3',(35,80),(150,20))


if __name__ == '__main__':
	app = wx.PySimpleApp()
	CheckBoxFrame().Show()
	app.MainLoop()
		
		