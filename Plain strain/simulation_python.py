# Clear previously generated data
# Model.NamedSelections.Delete()
# Model.Mesh.Delete()
# Storing first body in a variable
Body=Model.Geometry.Children[0].Children[0]
# 2D Dimension setting
Body.Dimension = ShellBodyDimension.Two_D
# Plane Strain idealization
Body.Behavior = Model2DBehavior.PlaneStrain
# Material assignment
# DataTransferID can be obtained from material's XML file 
Body.Material = "bcf8abf3-38d5-4e0c-9390-6a6085f17aef"
Body.NonlinearEffects = True
Body.ThermalStrainEffects = False

# Named selections
# use ExtAPI.SelectionManager.CurrentSelection.Ids for ID
# Use Tree.GetPathToFirstActiveObject() for object ID
# Defining selector datatype for geometric scoping method
SlMn = ExtAPI.SelectionManager
SlMn.ClearSelection()
Sel = SlMn.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
# Base boundary
Sel.Ids=[22]
MyNS = Model.AddNamedSelection()
MyNS.Name = 'base'
MyNS.Location = Sel
# Right boundary
Sel.Ids=[23]
MyNS = Model.AddNamedSelection()
MyNS.Name = 'right-boundary'
MyNS.Location = Sel
# Left boundary
Sel.Ids=[21]
MyNS = Model.AddNamedSelection()
MyNS.Name = 'Left-symmetry'
MyNS.Location = Sel

# Meshing
# general settings
# Physical preference- Non-linear mechanical
Model.Mesh.PhysicsPreference = MeshPhysicsPreferenceType.NonlinearMechanical
# Global Element quality
Model.Mesh.ElementOrder = ElementOrder.Quadratic
# Global element size
Model.Mesh.ElementSize =  Quantity(0.5, "m")
# Disabling mesh defeaturing
Model.Mesh.AutomaticMeshBasedDefeaturing = 0
# Disabling curvature capture
Model.Mesh.CaptureCurvature = False


# Mesh: secondary settings
mesh=Model.Mesh.AddAutomaticMethod()
Sel.Ids=[19]
mesh.Location=Sel
#mesh.Name=''
# Method-Quad dominant
mesh.Method=MethodType.Automatic
# Element order- quadratic
mesh.ElementMidsideNodes=ElementMidsideNodesType.Kept
# Free face mesh type= All quad (2)
mesh.FreeFaceMeshType=2
# Mesh refinement along left and top edges
refine=Model.Mesh.AddRefinement()
Sel.Ids=[21, 25, 24]
refine.Location = Sel
refine.NumberOfRefinements = 2
# Generate mesh
Model.Mesh.GenerateMesh()

# Boundary conditions
# Base edge
disp=DataModel.AnalysisList[0].AddDisplacement()
disp.Location=Model.NamedSelections.Children[0]
disp.XComponent.Output.DefinitionType=VariableDefinitionType.Free
disp.YComponent.Output.DefinitionType=VariableDefinitionType.Discrete
#disp.ZComponent.Output.DefinitionType=VariableDefinitionType.Discrete
disp.Name='BC_BaseEdge'
# Right edge
disp=DataModel.AnalysisList[0].AddDisplacement()
disp.Location=Model.NamedSelections.Children[1]
disp.XComponent.Output.DefinitionType=VariableDefinitionType.Discrete
disp.YComponent.Output.DefinitionType=VariableDefinitionType.Free
#disp.ZComponent.Output.DefinitionType=VariableDefinitionType.Discrete
disp.Name='BC_RightEdge'
# Symmetric boundary condition
disp=DataModel.AnalysisList[0].AddDisplacement()
disp.Location=Model.NamedSelections.Children[2]
disp.XComponent.Output.DefinitionType=VariableDefinitionType.Discrete
disp.YComponent.Output.DefinitionType=VariableDefinitionType.Free
disp.ZComponent.Output.DefinitionType=VariableDefinitionType.Discrete
disp.Name='BC_SymmetricEdge'

# Displacement
disp=DataModel.AnalysisList[0].AddDisplacement()
Sel.Ids=[25]
disp.Location=Sel
disp.XComponent.Output.DefinitionType=VariableDefinitionType.Discrete
disp.YComponent.Output.DefinitionType=VariableDefinitionType.Discrete
#disp.ZComponent.Output.DefinitionType=VariableDefinitionType.Discrete
disp.DefineBy=LoadDefineBy.Components
disp.YComponent.Inputs[0].DiscreteValues=[Quantity('0 [sec]'),Quantity('0.1[sec]'),Quantity('0.2 [sec]'),Quantity('1[sec]')]
disp.YComponent.Output.DiscreteValues=[Quantity('0 [m]'),Quantity('-0.000001[m]'),Quantity('-0.00002 [m]'),Quantity('-0.1[m]')]

# Analysis setting
# Step controls
analysis_settings=Model.Analyses[0].AnalysisSettings
analysis_settings.NumberOfSteps=1
analysis_settings.CurrentStepNumber=1
analysis_settings.StepEndTime=Quantity('1 [sec]')
analysis_settings.AutomaticTimeStepping=AutomaticTimeStepping.Off
analysis_settings.DefineBy=TimeStepDefineByType.Time
analysis_settings.TimeStep=Quantity('0.1[sec]')

# Solver controls
analysis_settings.SolverType=SolverType.Iterative
analysis_settings.WeakSprings=WeakSpringsType.Off
#analysis_settings.InertiaRelief='Off'
analysis_settings.LargeDeflection='Off'
analysis_settings.NewtonRaphsonOption=NewtonRaphsonType.Full

# Adding post-processing results
solution=Model.Analyses[0].Solution
solution.AddTotalDeformation()
solution.AddEquivalentTotalStrain()
solution.AddEquivalentStress()
solution.AddEquivalentPlasticStrain()
reaction=solution.AddForceReaction()
reaction.LocationMethod=LocationDefinitionMethod.BoundaryCondition
reaction.BoundaryConditionSelection=Model.Analyses[0].Children[1]
solution.Solve()






