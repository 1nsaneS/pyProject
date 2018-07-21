#!E:/anaconda env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-21 14:24:21
# @Author  : 1nsane SUN
# @Email   : 771499532@qq.com
# @Link    : pass
# @Version : $Id$

import wx

class ComBoxFrame(wx.Frame):
	"""docstring for ComBoxFrame"""
	def __init__(self):
		wx.Frame.__init__(self,None,-1,'ComBoxFrame',
			size=(350,300))
		panel = wx.Panel(self,-1)
		sampleList = ['1','2','3','4','5','6']
		wx.StaticText(panel,-1,'Select one:',(15,15))
		wx.ComboBox(panel,-1,'defaultvalue',(15,30),wx.DefaultSize,sampleList,wx.CB_DROPDOWN)
		wx.ComboBox(panel,-1,'defaultvalue',(150,30),wx.DefaultSize,sampleList,wx.CB_SIMPLE)

if __name__ == '__main__':
	app = wx.PySimpleApp()
	ComBoxFrame().Show()
	app.MainLoop()
		

