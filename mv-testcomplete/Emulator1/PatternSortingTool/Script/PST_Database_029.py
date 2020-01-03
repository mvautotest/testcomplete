#Author: Ha Le
#The test verify a prompting appear if user select the same name as the importing database at the location

import Setup
def PST_Database_0029():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTLoadDBSet("test", "load")
  Delay(500)
  Setup.Setup_PSTDBPanel()
 
  
  aqFileSystem.CopyFile(aqFileSystem.GetCurrentFolder() + "\\PST\\test123\\test123.pdpkg", aqFileSystem.GetCurrentFolder())
  Setup.Setup_PSTImport("\\test123.pdpkg[Enter]", "ok")
  #Setup.Setup_PSTImport(aqFileSystem.GetCurrentFolder() + "\\test123.pdpkg[Enter]", "")
  aqObject.CheckProperty(Aliases.javaw.Dialog22, "WndCaption", cmpEqual, "Warning")
  Aliases.javaw.Dialog22.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()

  Delay(500)
  aqFileSystem.DeleteFile(aqFileSystem.GetCurrentFolder()+ "\\test123.pdpkg")

  Setup.Setup_closeVPM()

  

