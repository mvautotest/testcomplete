#Author: Ha Le
#The test verify user can cancel during train

import Setup

def PST_CPM_026():
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
  
  Setup.Setup_PSTCPMLoadDB("acb\\acb.pdb", "load")
  
  #PST_CPM_030: Verify BD name and number of patterns display correctly when load a db
  aqTestCase.Begin("Start test ID: PST_CPM_30");
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.LoadDatabaseValue, "wText", cmpEqual, "acb")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternValue, "text", cmpEqual, "<html>3</html>")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternFrame.ModeValue, "wText", cmpEqual, "Edge Match")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternFrame.LabelValue.BasicComboBoxEditor_BorderlessTextField, "wText", cmpEqual, "a")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternFrame.InfoValue.BasicComboBoxEditor_BorderlessTextField, "wText", cmpEqual, "a")
  aqTestCase.End();
  aqTestCase.Begin("Start test ID: PST_CPM_26");
  Setup.Setup_PSTCPMAddLabelInfo(True, "test", "test", "Edge Match", "add")
  #Delay(300)
  Setup.Setup_PSTCPMRetrainAll("cancel")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.RetrainPrompt, "text", cmpEqual, "Retrain database to optimize 1 change")
  Setup.Setup_PSTCPMDeletePattern()
  Setup.Setup_PSTCPMRetrainAll("")
  aqTestCase.End();
  
  #PST_CPM_027: Verify selected pattern info displays when user click on
  aqTestCase.Begin("Start test ID: PST_CPM_27");
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternFrame.LabelValue.BasicComboBoxEditor_BorderlessTextField, "wText", cmpEqual, "a")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternFrame.InfoValue.BasicComboBoxEditor_BorderlessTextField, "wText", cmpEqual, "a")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternFrame.ModeValue, "wText", cmpEqual, "Edge Match")
  aqTestCase.End();
  
  #PST_CPM_028: Verify user can modify label, info, algorithm and parameters successfully
  aqTestCase.Begin("Start test ID: PST_CPM_28");
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternFrame.LabelValue.BasicComboBoxEditor_BorderlessTextField.Keys("[BS]test[Enter]")
  Delay(300)
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternFrame.InfoValue.BasicComboBoxEditor_BorderlessTextField.Keys("[BS]testinfo[Enter]")
  Setup.Setup_PSTCPMUpdateMode("Texture")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternFrame.LabelValue.BasicComboBoxEditor_BorderlessTextField, "wText", cmpEqual, "test")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternFrame.InfoValue.BasicComboBoxEditor_BorderlessTextField, "wText", cmpEqual, "testinfo")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternFrame.ModeValue, "wText", cmpEqual, "Texture")
  aqTestCase.End();
  
  #PST_CPM_029: Verify the warning message disappears after trained the update infomation
  aqTestCase.Begin("Start test ID: PST_CPM_29");
  Setup.Setup_PSTCPMRetrainAll("")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.RetrainPrompt, "text", cmpEqual, "")
  aqTestCase.End();
  
  Setup.Setup_DisableRunMode()
  Setup.Setup_PSTDeleteFoder("PST\\test")
  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()

 
