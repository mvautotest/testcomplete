#Author: Ha Le
#The test verify a dropdown list (E) train adge detection sensivity appears


import Setup
def PST_Train_082():
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
  Setup.Setup_PSTAddLabel("train", "test")
  Setup.Setup_PSTAddInfo("train", "test")
  Setup.Setup_PSTAddButton()
  Setup.Setup_VPMPropertiesTab()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.ClickCell(23, "E")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.Panel.ComboPopup_popup.ComboBox_scrollPane.Viewport.ComboBox_list, "wItemCount", cmpEqual, 6)

  Setup.Setup_VPMAdvSetupTab()
  Setup.Setup_PSTDBPanel()
  Setup.Setup_PSTDeletePattern()
  Setup.Setup_PSTRetrainAll("db", "ok")
 
  Setup.Setup_closeVPM()

 


  
