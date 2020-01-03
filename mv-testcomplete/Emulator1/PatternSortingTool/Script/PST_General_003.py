#Author: Ha Le
#The test verify that Origin displays linked value correctly

import Setup
def PST_General_003():
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_VPMOrigin()

  Setup.Setup_PSTOriginSetting()

  
  Setup.Setup_DragPatternSortToTaskTree()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.General.Panel.Panel2.Panel.TextField, "wText", cmpEqual, "[Inspection.Image In Task.Origin:Output Origin Relative To RWC]")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.General.Panel.Panel2.Panel2.Label, "text", cmpEqual, "-90°")


  Setup.Setup_closeVPM()

