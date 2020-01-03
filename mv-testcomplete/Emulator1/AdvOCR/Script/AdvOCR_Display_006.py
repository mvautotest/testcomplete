#Author: Ha Le
#The test verify all selected options and settings are saved and work correctly when loading

import Setup
def AdvOCR_Display_006(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  Setup.Setup_VPMVerificationPanel()

  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGVerifyPanel.Panel.Panel.Panel.Panel.RadioButton.Click(True)

  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGVerifyPanel.Panel.Panel.Panel.Panel.TextField2.Click()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGVerifyPanel.Panel.Panel.Panel.Panel.TextField2.Keys("3aN2aN")

  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGVerifyPanel.Panel.Panel2.Panel.Panel.Panel.PatchableRealTextField.Click(True)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGVerifyPanel.Panel.Panel2.Panel.Panel.Panel.PatchableRealTextField.Keys("[BS][BS][BS][BS][BS]70")
  Setup.Setup_VPMDisplayPanel()
  #Enable OCR font library
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGDisplayPanel.Panel.Panel.ScrollPane.Viewport.BaseDisplayPane_DisplayTable.wValue[0, "A"]
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGDisplayPanel.Panel.Panel.ScrollPane.Viewport.BaseDisplayPane_DisplayTable.ClickCell(0, "A")
  #Enbale Train Segment
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGDisplayPanel.Panel.Panel.ScrollPane.Viewport.BaseDisplayPane_DisplayTable.wValue[8, "A"]
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGDisplayPanel.Panel.Panel.ScrollPane.Viewport.BaseDisplayPane_DisplayTable.ClickCell(8, "A")
  #Enable minimum Score
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGDisplayPanel.Panel.Panel.ScrollPane.Viewport.BaseDisplayPane_DisplayTable.wValue[14, "A"]
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGDisplayPanel.Panel.Panel.ScrollPane.Viewport.BaseDisplayPane_DisplayTable.ClickCell(14, "A")
  
  Setup.Setup_VPMSaveAsButton()
  Aliases.javaw.ToolBar_SaveProgramAsAction_SaveAsDialog.RootPane.null_layeredPane.null_contentPane.Panel.Panel.VisionProgramsPanel.Panel.TextField.Keys("new[Enter]")
  if Aliases.javaw.Dialog.Exists:
    
    Aliases.javaw.Dialog.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button2.ClickButton()
  else:
    Log.Message("do nothing")
  
  Setup.Setup_VPMUnloadProgram()

  Setup.Setup_VPMDisconectReconectDevice()

  javaw = Aliases.javaw
  vpm = javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM
  vpm.Panel.Main_Toolbar.LoadProgramButton.ClickButton()
  panel = javaw.ToolBar_LoadProgramAction_LoadProgramDialog.RootPane.null_layeredPane.null_contentPane.Panel
  a = Aliases.javaw.ToolBar_LoadProgramAction_LoadProgramDialog.RootPane.null_layeredPane.null_contentPane.Panel.Panel.VisionProgramsPanel.ScrollPane.Viewport.Table.wRowCount
  Aliases.javaw.ToolBar_LoadProgramAction_LoadProgramDialog.RootPane.null_layeredPane.null_contentPane.Panel.Panel.VisionProgramsPanel.ScrollPane.Viewport.Table.wValue[a-1, "File Name"]
  Aliases.javaw.ToolBar_LoadProgramAction_LoadProgramDialog.RootPane.null_layeredPane.null_contentPane.Panel.Panel.VisionProgramsPanel.ScrollPane.Viewport.Table.ClickCell(a-1, "File Name")
  #panel.Panel.VisionProgramsPanel.ScrollPane.Viewport.Table.ClickCell(94, "File Name")
  panel.Panel2.Button.ClickButton()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.Panel.TaskToolbar.TaskAdvanceButton.ClickButton()
  scrollPane = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane
  #crollPane.HScroll.Pos = 0
  scrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.ClickItem("Root|Image In Task|Advanced OCR 1")
  Setup.Setup_VPMVerificationPanel()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGVerifyPanel.Panel.Panel.Panel.Panel.TextField2, "wText", cmpEqual, "3aN2aN")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGVerifyPanel.Panel.Panel2.Panel.Panel.Panel.PatchableRealTextField, "wText", cmpEqual, "70.00")
  Setup.Setup_VPMRunModeEnable()
  Regions.DisplayPanel_RuntimeTable.Check(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane2.DisplayPanel.SplitPane.DisplayPanel_DisplayPanelLeftPanel_.DisplayPanel_TablePane.ScrollPane.Viewport.DisplayPanel_RuntimeTable)
  Setup.Setup_VPMRunModeDisable()

  Setup.Setup_closeVPM()




 


