#Author: Ha Le
#The test verify there are some validation appear when input "Max Number of Keypoints"
#Need Check again for this case because no validation on Nax Number of Keypoint, other fileds still have
#update: Invalid TC
import Setup
def PST_Train_045():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTNewDB()
  Setup.Setup_PSTNameDB("test12345[Enter]")
  Setup.Setup_PSTAddLabel("train", "test new")
  Setup.Setup_PSTAddInfo("train", "test new 1")
  Setup.Setup_PSTAdvance("train")
  Setup.Setup_PSTMaxNumberOfKeypoint("10") 
  Setup.Setup_PSTAddButton()
  Setup.Setup_VPMPropertiesTab()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.ClickCell(20, "E")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.Panel.ExtendedTextField.Keys("[BS]15[Enter]")

  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.ClickCell(21, "E")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.Panel.ExtendedTextField.Keys("[BS]15[Enter]")
  aqObject.CheckProperty(Aliases.javaw.Dialog7, "WndCaption", cmpEqual, "Error: Contour Algorithm Train Number of Scale Levels")
  Aliases.javaw.Dialog7.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.ClickCell(22, "E")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.Panel.ExtendedTextField.Keys("[BS]10[Enter]")
  aqObject.CheckProperty(Aliases.javaw.Dialog9, "WndCaption", cmpEqual, "Error: Contour Algorithm Train Number of Clusters Per Keypoint")
  Aliases.javaw.Dialog9.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()

  Setup.Setup_PSTDeleteFoder("PST\\test12345")

  Setup.Setup_closeVPM()
