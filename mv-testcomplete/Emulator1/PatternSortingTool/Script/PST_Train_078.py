#Author: Ha Le
#The test verify input range in [0, 100] at fixed train edge threshold


import Setup
def PST_Train_078():
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
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.ClickCell(24, "E")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.Panel.ExtendedTextField.Keys("[BS][BS]101[Enter]")
  aqObject.CheckProperty(Aliases.javaw.Dialog17, "WndCaption", cmpEqual, "Error: Edge Match Algorithm Fixed Train Edge Threshold")
  Aliases.javaw.Dialog17.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.Panel.ExtendedTextField.Keys("20[Enter]")
  Setup.Setup_VPMAdvSetupTab()
  Setup.Setup_PSTDBPanel()
  Delay(500)
  Setup.Setup_PSTAdvanceSet("db", "Edge Match", None, None, None, None, None, None, None, None, None)
  aqObject.CheckProperty(Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane3.Panel.Panel.Panel.Panel.Panel.PatchableRealSlider, "wPosition", cmpEqual, 200)
  Setup.Setup_PSTAdvanceSet(None, "Edge Match", None, None, None, None, None, None, None, None, "ok")
  Delay(500)
  Setup.Setup_PSTDeletePattern()
  Setup.Setup_PSTRetrainAll("db", "ok")
 
  Setup.Setup_closeVPM()

 


  
