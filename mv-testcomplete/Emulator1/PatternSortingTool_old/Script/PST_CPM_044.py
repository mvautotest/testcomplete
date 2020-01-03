#Author: Ha Le
#The test verify user can import db

import Setup

def PST_CPM_044():
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
  Setup.Setup_PSTCPMLoadDB("test123\\test123.pdb", "load")
  Delay(5000)
  Setup.Setup_PSTCPMExportDb("test123[Enter]", "ok")
  if aqFileSystem.Exists("C:\\Datalogic\\IMPACT\\Applications\\Emulator\\EmulatorRoot\\PST"):
  
    if aqFileSystem.FindFiles("C:\\Datalogic\\IMPACT\\Applications\\Emulator\\EmulatorRoot\\PST", "test123.pdpkg") == None:
      Log.Error("fail")
    else:
      Log.Checkpoint("pass")
  else:
    if aqFileSystem.FindFiles("C:\\Datalogic\\IMPACT\\Applications\\Device\\DeviceRoot\\PST", "test123.pdpkg") == None:
      Log.Error("fail")
    else:
      Log.Checkpoint("pass")
  

  Setup.Setup_DisableRunMode()
  aqFileSystem.DeleteFile(aqFileSystem.GetCurrentFolder()+ "\\PST\\test123.pdpkg")
  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()

 
