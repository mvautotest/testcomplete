#Author: Ha Le
#The test verify default value = 40 at fixed train edge threshold
#Document was wrong and not update yet.

import Setup
def PST_Train_077():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTLoadDB("test")

  Setup.Setup_PSTMode("Edge Match")
  Setup.Setup_PSTAdvanceSet("train", "Edge Match", None, None, None, None, None, None, None, None, None)
  aqObject.CheckProperty(Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane3.Panel.Panel.Panel.Panel.Panel.PatchableRealSlider, "wPosition", cmpEqual, 400)
  Setup.Setup_PSTAdvanceSet(None, "Edge Match", None, None, None, None, None, None, None, None, "ok")

  Setup.Setup_PSTRetrainAll("train", "ok")
  Setup.Setup_VPMPropertiesTab()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[24, "E"], "value_", cmpEqual, 40)

  Setup.Setup_closeVPM()

 


  
