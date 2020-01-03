﻿#Author: Ha Le
#The test verify pin icon tooltip display 

import Setup
def AdvOCR_Train_058(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel3.Panel.Panel.Panel.Panel2.Button.ClickButton()

  a = Aliases.javaw.FloatablePanel.SwingObject("JRootPane", "", 0).SwingObject("null.layeredPane").SwingObject("null.contentPane").SwingObject("JPanel", "", 0).SwingObject("JPanel", "", 0).SwingObject("JPanel", "", 1).SwingObject("JButton", "", 0).getToolTipText()
  if a == "Click to pin OCR Font Library.":
    Log.Checkpoint(a, "Passed")
  else:
    Log.Error(a, "Failed")


  Setup.Setup_closeVPM()



