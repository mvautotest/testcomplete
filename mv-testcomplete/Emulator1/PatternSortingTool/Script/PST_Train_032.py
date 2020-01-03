#Author: Ha Le
#The test verify tooltip displays correctly on ROI on the image

import Setup
def PST_Train_032():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  #ImageRepository.DrawROI.ROI1.HoverMouse()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.PatternSortingSetup1_PatternSortingSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.roiList_.elementData_2.Items[3].toolTipText_, "OleValue", cmpEqual, "Size and position Primary Train ROI over the area that defines a pattern.")
  
  #Train_033: verify tooltip displays correctly on Load button
  a = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel.Button2.getToolTipText()
  if a == "Click to create a new pattern database. ":
    Log.Checkpoint("Pass", a)
  else:
    Log.Error("Fail", a)
  
  # Train_034:verify tooltip displays correctly on Load Button
  b = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel.Button.getToolTipText()
  if b == "Click to load an existing pattern database.":
    Log.Checkpoint("Pass", b)
  else:
    Log.Error("Fail", b)
  
  #Train_035: verify tooltip displays correctly on Name
  Setup.Setup_PSTLoadDB("test")
 

  c =  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel.PatchableStringTextField.getToolTipText()
  if c == "test":
    Log.Checkpoint("Pass", c)
  else:
    Log.Error("Fail", c)
  
  #Train_036: tooltip displays correctly on Pattern
  d =  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel.IntegerLabel.getToolTipText()
  if d == "The number of patterns in the currently loaded database.":
    Log.Checkpoint("Pass", d)
  else:
    Log.Error("Fail", d)
    
  #Train_037:verify tooltip displays correctly on Mode used button
  e =  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel.Button3.getToolTipText()
  if e == "Press to view all pattern modes used in loaded database.":
    Log.Checkpoint("Pass", e)
  else:
    Log.Error("Fail", e)
  
  #train_038: verify tooltip displays correctly on Add button
  f =  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel2.Panel.Panel.Button.getToolTipText()
  if f == "Add pattern to current database.":
    Log.Checkpoint("Pass", f)
  else:
    Log.Error("Fail", f)
  
  #Train_039: verify tooltip displays correctly on Advance button
  g =  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel2.Panel.Panel.Button2.getToolTipText()
  if g == "Click to enter advanced training parameters.":
    Log.Checkpoint("Pass", g)
  else:
    Log.Error("Fail", g)
    
  #Train_040: verify tooltip displays correctly on Retrain All button
  h =  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel3.Panel.Button.getToolTipText()
  if h == "Retrain all patterns in the current database.":
    Log.Checkpoint("Pass", h)
  else:
    Log.Error("Fail", h)
  
  #Train_041: verify tooltip displays correctly on label button
  i =  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel2.Panel.PatternSortModelDropdown.BasicComboBoxEditor_BorderlessTextField.getToolTipText()
  if i == "Enter a unique label for new pattern.":
    Log.Checkpoint("Pass", i)
  else:
    Log.Error("Fail", i)
  #train_042: verify tooltip displays correctly on info button
  j =  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel2.Panel.PatternSortModelDropdown2.BasicComboBoxEditor_BorderlessTextField.getToolTipText()
  if j == "Enter information text for new pattern.":
    Log.Checkpoint("Pass", j)
  else:
    Log.Error("Fail", j)
  
  #Train_043: verify tooltip displays correctly on mode button
  l =  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel2.Panel.PatchableComboBox.getToolTipText()
  if l == "Method used to train the pattern.":
    Log.Checkpoint("Pass", l)
  else:
    Log.Error("Fail", l)
  
  Setup.Setup_closeVPM()
