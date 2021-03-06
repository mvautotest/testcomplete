﻿#Author: Ha Le
#The test verify there is validation on number of scale level

import Setup
def PST_Train_047():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTNewDB()
  Setup.Setup_PSTNameDB("test12345[Enter]")
  Setup.Setup_PSTAddLabel("train", "test new")
  Setup.Setup_PSTAddInfo("train", "test new 1")
  Setup.Setup_PSTMode("Contour")
  #Setup.Setup_PSTAdvance("train")
  #Setup.Setup_PSTScaleLevel("[BS]5")
  Setup.Setup_PSTAdvanceSet("train", "Contour", None, "[BS]5", None, None, None, None, None, None, "ok")
  Setup.Setup_PSTAddButton()
  Setup.Setup_VPMPropertiesTab()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.ClickCell(21, "E")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.Panel.ExtendedTextField.Keys("[BS]15[Enter]")
  aqObject.CheckProperty(Aliases.javaw.Dialog7, "WndCaption", cmpEqual, "Error: Contour Algorithm Train Number of Scale Levels")
  Aliases.javaw.Dialog7.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()

  Setup.Setup_PSTDeleteFoder("PST\\test12345")
 

  Setup.Setup_closeVPM()
