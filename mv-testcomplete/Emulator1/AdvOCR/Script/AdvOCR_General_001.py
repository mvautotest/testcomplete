#Author: Ha Le
#The test verify Image link from another tool

import Setup
def AdvOCR_General_001(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  #Setup.Setup_AdvOCR()
  Setup.Setup_AdvOCREmpty()
  Setup.Setup_GeneralPanel()
  Setup.Setup_LinkButtonGeneralPanel()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.ClickItem("Root|Image In Task|Advanced OCR 1")

 
  Aliases.javaw.VpmFrame.SwingPopupMenu.Click("Search Image")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.General.Panel.Panel.Panel.TextField, "wText", cmpEqual, "[Inspection.Image In Task.Advanced OCR 1:Search Image]")
  Setup.Setup_closeVPM()


