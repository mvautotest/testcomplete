#Author: Ha Le
#The test verify user can save and load cp file without error


import Setup
def AdvOCR_CPM_023(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  Setup.Setup_LoadCPM()
  Setup.Setup_DragOCRFontLibraryToCpFile()
  Setup.Setup_CPMSaveAs("new[Enter]")
  Delay(7000)
  a = aqFileSystem.FindFiles("C:\\Datalogic\\IMPACT\\Applications\\Root\\Control Panels", "new.cp")
  if a != None:
    Log.Checkpoint("test pass")
  else:
    Log.Error("test fail")
  Setup.Setup_CPMLoadFile("new.cp[Enter]")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame10.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.CPMPatchPanel.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.TasksTabbedPane_TaskTree_, "Enabled", cmpEqual, True)
  Setup.Setup_DeleteFile("C:\\Datalogic\\IMPACT\\Applications\\Root\\Control Panels\\new.cp")
 

  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()
