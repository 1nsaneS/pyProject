#!E:/anaconda env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-21 14:07:48
# @Author  : 1nsane SUN
# @Email   : 771499532@qq.com
# @Link    : pass
# @Version : $Id$

import wx

class CheckListBoxFrame(wx.Frame):
	"""docstring for CheckListBoxFrame"""
	def __init__(self):
		wx.Frame.__init__(self,None,-1,'Choice Example',
			size=(250,200))
		panel = wx.Panel(self,-1)
		sampleList = ['1','2','3','4','5']
		wx.StaticText(panel,-1,'Select one:',(15,20))
		wx.Choice(panel,-1,(85,18),choices=sampleList)

if __name__ == '__main__':
	app = wx.PySimpleApp()
	CheckListBoxFrame().Show()
	app.MainLoop()
