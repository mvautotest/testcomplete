#Author: Ha Le
#The test verify the selected location is displayed on Database Root Directory in properties tab

import Setup
def PST_Train_017():
  #Setup.Setup_InnitializeCPM()
  
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTNewDB()

  Aliases.javaw.Dialog4.RootPane.null_layeredPane.null_contentPane.PatternSortingSetup1_SortingTrainPanel_1_1.ToolBar.ClickItem("Up")
  Aliases.javaw.Dialog4.RootPane.null_layeredPane.null_contentPane.PatternSortingSetup1_SortingTrainPanel_1_1.Panel.Panel.Panel.WindowsFileChooserUI_7.Keys("test[Enter]")

  Setup.Setup_VPMPropertiesTab()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[10, "E"], "stringValue_", cmpEqual, "C:\\Datalogic\\IMPACT\\Applications\\Emulator\\EmulatorRoot")
  

  Setup.Setup_PSTDeleteFoder("test")
  Setup.Setup_closeVPM()


