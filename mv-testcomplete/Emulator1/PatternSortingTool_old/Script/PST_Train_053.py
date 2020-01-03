#Author: Ha Le
#The test verify message "Database needs to be trained" still displays if user cancel during training
 
import Setup
def PST_Train_053():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTLoadDB("test")


  Setup.Setup_PSTMode("Contour")
  Setup.Setup_PSTAddLabel("train", "testhale")
  Setup.Setup_PSTAddInfo("train", "test")
  Setup.Setup_PSTAddButton()
  Delay(500)
  Setup.Setup_PSTRetrainAll("train", "cancel")
  
  aqObject.CheckProperty(Aliases.javaw.Dialog6, "WndCaption", cmpEqual, "Setup Error")
 
  Aliases.javaw.Dialog6.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel2.Panel.Panel.TextField, "wText", cmpEqual, "Database needs to be retrained")
  Setup.Setup_PSTDBPanel()
  Setup.Setup_PSTDeletePattern()
  Setup.Setup_PSTRetrainAll("db", None)

  Setup.Setup_closeVPM()
  

