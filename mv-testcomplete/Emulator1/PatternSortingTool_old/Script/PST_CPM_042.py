#Author: Ha Le
#The test verify user can export db

import Setup

def PST_CPM_042():
  Setup.Setup_PSTCheck()
  
  Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  #Setup.VPM_CameraCheck()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()

  Setup.Setup_LoadCPM()
  Setup.Setup_PSTCPMDragDropPatternDBToPanel()
  Setup.Setup_EnableRunMode()
  aqFileSystem.CopyFile(aqFileSystem.GetCurrentFolder() + "\\PST\\test123\\test123.pdpkg", aqFileSystem.GetCurrentFolder())
  Setup.Setup_PSTCPMImportDb(aqFileSystem.GetCurrentFolder() + "\\test123.pdpkg[Enter]", "ok")
  
  Aliases.javaw.Dialog22.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.Keys("[Enter]")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.LoadDatabaseValue, "wText", cmpEqual, "test123")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternValue, "text", cmpEqual, "<html>42</html>")
  
  Setup.Setup_DisableRunMode()
  aqFileSystem.DeleteFile(aqFileSystem.GetCurrentFolder()+ "\\test123.pdpkg")
  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()

 
