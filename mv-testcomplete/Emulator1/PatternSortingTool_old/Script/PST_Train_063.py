#Author: Ha Le
#The test verify there is validation on "Max Dip"

import Setup
def PST_Train_063():
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

  Setup.Setup_PSTAdvanceSet("train", "Texture", None, None, None, None, "[BS]7", None, None, None, "ok")
  Setup.Setup_PSTAddButton()
  Setup.Setup_VPMPropertiesTab()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.ClickCell(27, "E")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.Panel.ExtendedTextField.Keys("[BS]101[Enter]")
  aqObject.CheckProperty(Aliases.javaw.Dialog11, "WndCaption", cmpEqual, "Error: Texture Algorithm Train Max Dip")
  Aliases.javaw.Dialog11.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.Panel.ExtendedTextField.Keys("[BS][BS][BS][BS]0.01[Enter]")
  aqObject.CheckProperty(Aliases.javaw.Dialog11, "WndCaption", cmpEqual, "Error: Texture Algorithm Train Max Dip")
  Aliases.javaw.Dialog11.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.Panel.ExtendedTextField.Keys("[BS][BS][BS][BS]t@>?[Enter]")
  aqObject.CheckProperty(Aliases.javaw.Dialog11, "WndCaption", cmpEqual, "Error: Texture Algorithm Train Max Dip")
  Aliases.javaw.Dialog11.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()

  Setup.Setup_VPMAdvSetupTab()
  Setup.Setup_PSTDBPanel()
  Setup.Setup_PSTDeletePattern()

  Setup.Setup_PSTRetrainAll("db", None)

  Setup.Setup_closeVPM()
