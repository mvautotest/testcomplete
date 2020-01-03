#Author: Ha Le
#The test verify add image to database dialog appears when clicking on add image icon

import Setup
def PST_Database_038():
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
  Setup.Setup_PSTAddImage("", None)
  aqObject.CheckProperty(Aliases.javaw.Dialog20, "WndCaption", cmpEqual, "Add Images to Database")
  Setup.Setup_PSTAddImage(None, "cancel")
  
  #Database_039: Verify user can add one or multi images
  Setup.Setup_PSTAddImage("\\Image\\Image004.JPG", "add")
  Setup.Setup_PSTDeletePattern()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.Button2.ClickButton()

  #Setup.Setup_PSTAddImage("Image005.BMP", "add")
  Aliases.javaw.Dialog20.RootPane.null_layeredPane.null_contentPane.FileChooser.Panel.Panel.Panel.WindowsFileChooserUI_7.Keys('"Image004.BMP" "Image005.BMP"'+"[Enter]")
  #Aliases.javaw.Dialog20.RootPane.null_layeredPane.null_contentPane.FileChooser.Panel.FilePane.Panel.ScrollPane.Viewport.FilePane_4.ClickItemXY("Image005.BMP", 58, 13)
  #Aliases.javaw.Dialog20.RootPane.null_layeredPane.null_contentPane.FileChooser.Panel.Panel.Panel2.WindowsFileChooserUI_9.ClickButton()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ScrollPane.Viewport.PatternSortDatabaseViewer_DatabasePanel_, "ChildCount", cmpEqual, 6)
  
  #database_51: Verify train processing display during train patterns
  Setup.Setup_PSTModeDB("Texture")
  Setup.Setup_PSTAdvanceSet("db", "Texture","[BS]2", "[BS]3", "[BS]2","[BS]4", None, None, None, None, "ok")
  Setup.Setup_PSTRetrainAll("db", "ok")
  aqObject.CheckProperty(Aliases.javaw.Dialog2.RootPane.null_layeredPane.null_contentPane.Panel, "Enabled", cmpEqual, True)
  
  #Database_040: verify duplicate pattern dialog appears if user add duplicate image to db
  Setup.Setup_PSTAddImage("Image004.JPG", "add")
  aqObject.CheckProperty(Aliases.javaw.Dialog6, "WndCaption", cmpEqual, "Setup Error")
  Aliases.javaw.Dialog6.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()

  #Database_052: verify user can delete selected pattern
  Setup.Setup_PSTDeletePattern()
  
  scrollPane = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ScrollPane
  scrollPane.VScroll.Pos = 5
  scrollPane.Viewport.PatternSortDatabaseViewer_DatabasePanel_.PatternSortDatabaseViewer_PatternModelPanel_4.Label.Click(30, 39)
  Setup.Setup_PSTDeletePattern()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ScrollPane.Viewport.PatternSortDatabaseViewer_DatabasePanel_, "ChildCount", cmpEqual, 4)
  
  Setup.Setup_PSTDeleteAllPatten()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ScrollPane.Viewport.PatternSortDatabaseViewer_DatabasePanel_, "ChildCount", cmpEqual, 0)
  
  #Database_058: Verify meesage "database needs to be trained" appear after delete all pattern
  Setup.Setup_VPMPropertiesTab()
  Setup.Setup_PSTRunpropertytab()
  aqObject.CheckProperty(Aliases.javaw.Dialog5, "WndCaption", cmpEqual, "Error")
  Sys.Process("javaw").SwingObject("JDialog", "Error", -1, 1).SwingObject("JRootPane", "", 0).SwingObject("null.layeredPane").SwingObject("null.contentPane").SwingObject("JOptionPane", "", 0).SwingObject("OptionPane.buttonArea").SwingObject("OptionPane.button").ClickButton()

  
  Setup.Setup_PSTDeleteFoder("PST\\test")
  Setup.Setup_VPMUnloadProgram()
  Aliases.javaw.Dialog14.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()

  
 



 
  

