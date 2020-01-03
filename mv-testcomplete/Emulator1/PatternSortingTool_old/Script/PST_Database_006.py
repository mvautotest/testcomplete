#Author: Ha Le
#The test verify tooltip appear on train ROI

import Setup
def PST_Database_006():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTLoadDBSet("test", "load")
  Setup.Setup_PSTResizeROI()
  Setup.Setup_PSTAddButton()
  Setup.Setup_PSTRetrainAll("train", "ok")
  Setup.Setup_PSTDBPanel()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.PatternSortingSetup1_SortingDatabasePanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.activeListROI_, "toolTipText_", cmpEqual, "Size and position Primary Train ROI over the area that defines a pattern.")
  a = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.SwingObject("JButton", "", 0).getToolTipText()
  if a == "Browse and import specified database. ":
    Log.Checkpoint("pass", a)
  else:
    Log.Error("Fail", a)
    
  b = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.SwingObject("JButton", "", 1).getToolTipText()
  if b == "Browse and export database to specified location.":
    Log.Checkpoint("pass", b)
  else:
    Log.Error("Fail", b)
  c = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.Button2.getToolTipText()
  if c == "Browse and add pattern images to database.":  
    Log.Checkpoint("pass", c)
  else:
    Log.Error("Fail", c) 
    
  d =  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.Button.getToolTipText()
  if d == "Delete selected patterns. ":  
    Log.Checkpoint("pass", d)
  else:
    Log.Error("Fail", d) 
    
  e =  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.SwingObject("JButton", "", 5).getToolTipText()
  if e == "Delete all patterns.":  
    Log.Checkpoint("pass", e)
  else:
    Log.Error("Fail", e)
    
  f =  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.SwingObject("JToggleButton", "", 0).getToolTipText()
  if f == "Select to display pattern custom info text.":  
    Log.Checkpoint("pass", f)
  else:
    Log.Error("Fail", f)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.ToggleButton2.ClickButton(True)
  
  g = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.SwingObject("JButton", "", 9).getToolTipText()
  if g == "Zoom all patterns to 100%.":  
    Log.Checkpoint("pass", g)
  else:
    Log.Error("Fail", g) 
  h0 = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.SwingObject("JButton", "", 6).getToolTipText()
  if h0 == "Sort patterns either alphabetically or by creation date.":  
    Log.Checkpoint("pass", h0)
  else:
    Log.Error("Fail", h0)
  
  i = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.Panel.Panel.Panel.PatternSortModelDropdown2.BasicComboBoxEditor_BorderlessTextField.getToolTipText()
  if i == "Enter a unique label for new pattern.":  
    Log.Checkpoint("pass", i)
  else:
    Log.Error("Fail", i)  
  j = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.Panel.Panel.Panel.PatternSortModelDropdown.BasicComboBoxEditor_BorderlessTextField.getToolTipText()
  if j == "Enter information text for the current pattern.":  
    Log.Checkpoint("pass", j)
  else:
    Log.Error("Fail", j)  
    
  k = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.ToggleButton2.getToolTipText()
  if k == "Select to display pattern label text.":  
    Log.Checkpoint("pass", k)
  else:
    Log.Error("Fail", k)
  
 
  
  l = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.ToggleButton.getToolTipText()
  if l == "Display training model points on selected pattern.":  
    Log.Checkpoint("pass", l)
  else:
    Log.Error("Fail", l)
    
 
  
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.ToggleButton.ClickButton(True)

  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.PatternSortingSetup1_SortingDatabasePanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.HoverMouse(155, 378)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.PatternSortingSetup1_SortingDatabasePanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.roiList_.elementData_2.Items[2], "dynamicToolTipText_", cmpEqual, "Points used to train this pattern.")
  m = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.SwingObject("JButton", "", 7).getToolTipText()
  if m == "Zoom in all patterns.":  
    Log.Checkpoint("pass", m)
  else:
    Log.Error("Fail", m)
  n = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.SwingObject("JButton", "", 8).getToolTipText()
  if n == "Zoom out all patterns.":  
    Log.Checkpoint("pass", n)
  else:
    Log.Error("Fail", n)
 
  o = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.Panel.Panel2.Button.getToolTipText()
  if o == "Retrain all patterns in the current database.":  
    Log.Checkpoint("pass", o)
  else:
    Log.Error("Fail", o)   
    
    
  p = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.Panel.Panel2.SwingObject("LinkPanel", "", 0).SwingObject("JToggleButton", "Link", 0).getToolTipText()
  if p == "Link this Pattern Database from another tool's Pattern Database port.":  
    Log.Checkpoint("pass", p)
  else:
    Log.Error("Fail", p)  
    
        
  q = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.SwingObject("JPanel", "", 1).SwingObject("JTextField", "", 0).getToolTipText()
  if q == "Enter search string to locate corresponding patterns in the list.":  
    Log.Checkpoint("pass", q)
  else:
    Log.Error("Fail", q)
    
  r = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.Panel.Panel2.SwingObject("LinkPanel", "", 0).SwingObject("JButton", "", 0).getToolTipText()
  if r == "Unlink the Pattern Database.":  
    Log.Checkpoint("pass", r)
  else:
    Log.Error("Fail", r)
    
  w = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.SwingObject("JPanel", "", 1).SwingObject("JTextField", "", 0).getToolTipText()
  if w == "Enter search string to locate corresponding patterns in the list.":  
    Log.Checkpoint("pass", w)
  else:
    Log.Error("Fail", w)  
    
    
 
  Setup.Setup_PSTDeletePattern()
  Setup.Setup_PSTRetrainAll("db", "ok")
  Setup.Setup_closeVPM()


