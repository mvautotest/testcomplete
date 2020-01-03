#Author: Ha Le
#The test verify there is validation when input [1, 10] on Sampling Resolution

import Setup
def PST_Train_089():
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
  Setup.Setup_PSTAddLabel("train", "testhale")
  Setup.Setup_PSTAddInfo("train", "test[Enter]")

  Setup.Setup_PSTAdvanceSet("train", "Edge Match", "[BS][BS]8", None, None, None, None, None, None, None, "ok")
  Setup.Setup_PSTRetrainAll("train", None)
  Setup.Setup_VPMPropertiesTab()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.ClickCell(19, "E")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.Panel.ExtendedTextField.Keys("[BS]21[Enter]")
  aqObject.CheckProperty(Aliases.javaw.Dialog19, "WndCaption", cmpEqual, "Error: Edge Match Algorithm Sampling Resolution")
  Aliases.javaw.Dialog19.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.Panel.ExtendedTextField.Keys("[BS][BS]0[Enter]")
  aqObject.CheckProperty(Aliases.javaw.Dialog19, "WndCaption", cmpEqual, "Error: Edge Match Algorithm Sampling Resolution")
  Aliases.javaw.Dialog19.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.Panel.ExtendedTextField.Keys("[BS]T@est?[Enter]")
  aqObject.CheckProperty(Aliases.javaw.Dialog19, "WndCaption", cmpEqual, "Error: Edge Match Algorithm Sampling Resolution")
  Aliases.javaw.Dialog19.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  

  Setup.Setup_closeVPM()
 


  
