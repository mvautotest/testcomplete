#Author: Ha Le
#The test verify user can drag and drop Pattern database to cp file without error

import Setup

def PST_CPM_001():
  Setup.Setup_PSTCheck()
  
  Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  #Setup.VPM_CameraCheck()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Delay(500)
  Setup.Setup_LoadCPM()
  Setup.Setup_PSTCPMDragDropPatternDBToPanel()
  
  aqTestCase.Begin("Start test ID: PST_CPM_001");
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.Pattern_Database2, "AWTComponentName", cmpEqual, "Pattern Database2")
  Setup.Setup_EnableRunMode()
  aqTestCase.End();
  
  #PST_CPM_002: Verify default directory displays when user create db at the first time
  aqTestCase.Begin("Start test ID: PST_CPM_002");
  Setup.Setup_PSTCPMNewDb("", None)
  aqObject.CheckProperty(Aliases.javaw.Dialog4, "WndCaption", cmpEqual, "Create New Pattern Database Folder")
  aqObject.CheckProperty(Aliases.javaw.Dialog4.RootPane.null_layeredPane.null_contentPane.PatternSortDatabase_15.ToolBar.WindowsFileChooserUI_2, "wText", cmpEqual, "PST")
  Setup.Setup_PSTCPMNewDb(None, "cancel")
  Delay(500)
  aqTestCase.End();
  
  #PST_CPM_003: Verify user can create a db by clicking new button
  aqTestCase.Begin("Start test ID: PST_CPM_003");
  Setup.Setup_PSTCPMNewDb("testcpm1", "create")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.LoadDatabaseValue, "wText", cmpEqual, "testcpm1")
  aqTestCase.End();
  #PST_CPM_004: Verify user can add pattern successfully
  
  #PST_CPM_006:The test verify the number of patterns is increased 1 unit after add a pattern
  aqTestCase.Begin("Start test ID: PST_CPM_006");
  #Setup.Setup_PSTCPMLoadDB("test123\\test123.pdb", "load")
  Setup.Setup_PSTCPMAddLabelInfo(True, "test", "test", None, "add")
  Delay(500)
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternSortDatabaseDisplay.PatternSortDatabaseViewer.Panel.ScrollPane.Viewport.PatternSortDatabaseViewer_DatabasePanel_, "ChildCount", cmpEqual, 1)
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.RetrainPrompt, "text", cmpEqual, "Retrain database to optimize 1 change")
  aqTestCase.End();
  #Aliases.javaw.PatternSortDatabase_AddPatternDialog.RootPane.null_layeredPane.null_contentPane.Panel.Panel2.Button.ClickButton()
  Setup.Setup_PSTCPMDeletePattern()
  
  #PST_CPM_005: Verify validation on label and info field
  aqTestCase.Begin("Start test ID: PST_CPM_005");
  Setup.Setup_PSTCPMAddLabelInfo(True, "t@st?", "test?", None, "add")
  aqObject.CheckProperty(Aliases.javaw.Dialog5, "WndCaption", cmpEqual, "Error")
  Aliases.javaw.Dialog5.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  Setup.Setup_DisableRunMode()
  aqTestCase.End();
  
  
  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()
  Setup.Setup_PSTDeleteFoder("PST\\testcpm1")
  
