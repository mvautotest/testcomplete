#Author: Ha Le
#The test verify export database dialog appears with default path in the first time when click on export icon

import Setup
def PST_Database_034():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTLoadDBSet("test", "load")
  Setup.Setup_PSTDBPanel()
  Setup.Setup_PSTExport("", None)
  aqObject.CheckProperty(Aliases.javaw.Dialog23.RootPane.null_layeredPane.null_contentPane.PatternSortDatabaseViewer_25.ToolBar.WindowsFileChooserUI_2, "wText", cmpEqual, "PST")
  Setup.Setup_PSTExport(None, "cancel")
  
  #Database_035: verify export database display a directory broswer to allow user to specify the directory
  Setup.Setup_PSTExport("test", None)
  Aliases.javaw.Dialog23.RootPane.null_layeredPane.null_contentPane.PatternSortDatabaseViewer_25.WindowsPlacesBar.CheckItem("Documents", True)
  Setup.Setup_PSTExport(None, "export")
  
  path = "C:\\Users\\" + Sys.UserName + "\\Documents"
  if aqFileSystem.FindFiles(path, "test.pdpkg") == None:
    Log.Error("fail")
  else:
    Log.Checkpoint("pass")
    
  #Database_036: Verify a prompting appears if user store the duplicate name at location
  Setup.Setup_PSTExport("test", "export")
  aqObject.CheckProperty(Aliases.javaw.Dialog22, "WndCaption", cmpEqual, "Warning")
  Aliases.javaw.Dialog22.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  aqFileSystem.DeleteFile("%Document%\\test.pdpkg")
  
  #Database_037: Verify export icon is disabled if no db is loaded
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTDBPanel()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.Button5, "Enabled", cmpEqual, False)
  
  Setup.Setup_closeVPM()

  

