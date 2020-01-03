#Author: Ha Le
#The test verify a blue message dispaly if OCRSet is empty

import Setup
def AdvOCR_CPM_013():
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM()  
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCREmpty()
  Setup.Setup_AdvNotTrain()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel2.Label, "Enabled", cmpEqual, True)
  
  Setup.Setup_LoadCPM()
  Setup.Setup_DragOCRFontLibraryToCpFile()
  aqObject.CheckProperty(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCR_Font_Library2.Train_Prompt.Control_GlassPane, "Enabled", cmpEqual, True)
  
  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()