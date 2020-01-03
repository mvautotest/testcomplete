#Author: Ha Le
#The test verify the message appears after load db without trainning before

import Setup

def PST_CPM_031():
  Setup.Setup_PSTCheck()
  
  Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  #Setup.VPM_CameraCheck()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  aqTestCase.Begin("Start test ID: PST_CPM_31");
  Setup.Setup_LoadCPM()
  Setup.Setup_PSTCPMDragDropPatternDBToPanel()
  Setup.Setup_EnableRunMode()
  Setup.Setup_PSTCPMLoadDB("dbnottrain\\dbnottrain.pdb", "load")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.RetrainPrompt, "text", cmpEqual, "Retrain database to optimize 4 changes")
  Setup.Setup_PSTCPMRetrainAll("")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.RetrainPrompt, "text", cmpEqual, "")
  aqTestCase.End();
  
  #PST_CPM_032: Verify user can add image successfully
  aqTestCase.Begin("Start test ID: PST_CPM_32");
  Setup.Setup_PSTCPMAddImage(aqFileSystem.GetCurrentFolder() + "\\PST\\Image\\Image004.JPG", "add")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.RetrainPrompt, "text", cmpEqual, "Retrain database to optimize 1 change")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternValue, "text", cmpEqual, "<html>5</html>")
  aqTestCase.End();
  
  #PST_CPM_033: Verify duplicate dialog appear if user add the duplicate image
  aqTestCase.Begin("Start test ID: PST_CPM_33");
  Setup.Setup_PSTCPMAddImage("Image004.JPG", "add")
  aqObject.CheckProperty(Aliases.javaw.Dialog5, "WndCaption", cmpEqual, "Error")
  Aliases.javaw.Dialog5.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  aqTestCase.End();
  
  Setup.Setup_DisableRunMode()
  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()

  Setup.Setup_PSTDeleteFoder("PST\\test")
  Setup.Setup_PSTDeleteFoder("PST\\dbnottrain")
  

 