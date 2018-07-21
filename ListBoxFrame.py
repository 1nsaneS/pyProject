#!E:/anaconda env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-21 13:09:08
# @Author  : 1nsane SUN
# @Email   : 771499532@qq.com
# @Link    : pass
# @Version : $Id$

import wx

class ListBoxFrame(wx.Frame):
	"""docstring for ClassName"""
	def __init__(self):
		wx.Frame.__init__(self,None,-1,
			size=(250,200))
		panel = wx.Panel(self,-1)
		sampleList = ['1','2','3','4','5']
		listBox = wx.ListBox(panel,-1,(20,20),(80,120),sampleList,
			wx.LB_SINGLE)
		listBox.SetSelection(1)


if __name__ == '__main__':
	app = wx.PySimpleApp()
	ListBoxFrame().Show()
	app.MainLoop()
		
