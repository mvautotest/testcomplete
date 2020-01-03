#Author: Ha Le
#The test verify time is  detected correctly after clicked "Retrainall" button

import Setup
def PST_Train_074():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTLoadDB("test")

  Setup.Setup_PSTMode("Texture")
  Setup.Setup_PSTAddLabel("train", "testhale")
  Setup.Setup_PSTAddInfo("train", "test[Enter]")
  Setup.Setup_PSTResizeROI()
  for i in range(0, 3):
    Setup.Setup_VPMtriggerOne()
  
  Setup.Setup_PSTAddButton()
  Setup.Setup_PSTRetrainAll("train", None)
  a = aqDateTime.Now()
  Setup.Setup_VPMPropertiesTab()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.ClickCell(7, "A")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.ClickCell(23, "A")
  
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[24, "E"], "stringValue_", cmpEqual, str(a))
  Setup.Setup_VPMAdvSetupTab()
  Setup.Setup_PSTDBPanel()
  Setup.Setup_PSTDeletePattern()
  Delay(700)
  Setup.Setup_PSTRetrainAll("db", None)

  Setup.Setup_closeVPM()
