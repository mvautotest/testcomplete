#Author: Ha Le
#The test verify user can delete the label on the character box and move the highlighted back to the box on the left with backspace keyboard

import Setup
def AdvOCR_Train_040(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  Setup.Setup_OCRClicktoTrain()
  javaw = Aliases.javaw
  baseSetupPanel_1 = javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1
  displayCanvas = baseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas
 
  displayCanvas.Keys("[BS][BS][BS][BS][BS][BS][BS]")
  Regions.DisplayCanvas50.Check(Regions.CreateRegionInfo(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas, 51, 59, 488, 311, False), False, False, 1000)
 

  Setup.Setup_closeVPM()
  
