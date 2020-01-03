#Author: Ha Le
#The test verify import database browse to currently loaded database's parent directory

import Setup
def PST_Database_0027():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()

  Setup.Setup_PSTDBPanel()
 
  
  aqFileSystem.CopyFile(aqFileSystem.GetCurrentFolder() + "\\PST\\test123\\test123.pdpkg", aqFileSystem.GetCurrentFolder())
  Setup.Setup_PSTImport(aqFileSystem.GetCurrentFolder() + "\\test123.pdpkg[Enter]", "ok")
  Aliases.javaw.Dialog22.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.Keys("[Enter]")
  Delay(500)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ScrollPane.Viewport.PatternSortDatabaseViewer_DatabasePanel_, "ChildCount", cmpEqual, 42)
  
 
  
  aqFileSystem.DeleteFile(aqFileSystem.GetCurrentFolder()+ "\\test123.pdpkg")
 


  Setup.Setup_closeVPM()

  

