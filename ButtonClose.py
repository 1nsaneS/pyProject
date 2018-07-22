#!E:/anaconda env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-21 15:00:38
# @Author  : 1nsane SUN
# @Email   : 771499532@qq.com
# @Link    : pass
# @Version : $Id$

import wx

class SubclassFrame(wx.Frame):
	"""docstring for SubclassFrame"""
	def __init__(self):
		wx.Frame.__init__(self,None,-1,'SubclassFrame',
			size=(300,100))
		panel = wx.Panel(self,-1)
		button = wx.Button(panel,-1,'Close Me',pos=(15,15))
		self.Bind(wx.EVT_BUTTON,self.OnClose,button)
		self.Bind(wx.EVT_CLOSE,self.OnCloseWindow)

	def OnClose(self,event):
		self.Close(True)

	def OnCloseWindow(self,event):
		self.Destroy()


if __name__ == '__main__':
	app = wx.PySimpleApp()
	SubclassFrame().Show()
	app.MainLoop()