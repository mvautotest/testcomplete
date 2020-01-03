#Author: Ha Le
#The test verify user can delete the label on the character box and its label by clicking on delete keyboard or x icon

import Setup
def AdvOCR_Train_042(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  Setup.Setup_OCRClicktoTrain()
  panel = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_2.ROIEditor.Panel
  #panel.Panel.ScrollPane.Viewport.DisplayCanvas.Click(293, 141)
  ROIToolBar_4 = panel.ROIToolBar.Panel.ROIToolBar_4
  ROIToolBar_4.ClickButton()
  ROIToolBar_4.ClickButton()
  ROIToolBar_4.ClickButton()
  ROIToolBar_4.ClickButton()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.Keys("[Del][Del][Del]")

#  ROIToolBar_4.ClickButton()
#  ROIToolBar_4.ClickButton()
  Regions.DisplayCanvas33.Check(Regions.CreateRegionInfo(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas, 51, 59, 488, 311, False), False, False, 1000)

  Setup.Setup_closeVPM()
  
