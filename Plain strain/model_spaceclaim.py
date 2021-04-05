
# Set Sketch Plane
sectionPlane = Plane.PlaneXY
result = ViewHelper.SetSketchPlane(sectionPlane, Info15)
# EndBlock

# Sketch Line
start = Point2D.Create(M(0), M(0))
end = Point2D.Create(M(10), M(0))
result = SketchLine.Create(start, end)
# EndBlock

# Sketch Line
start = Point2D.Create(M(10), M(0))
end = Point2D.Create(M(10), M(10))
result = SketchLine.Create(start, end)
# EndBlock

# Sketch Line
start = Point2D.Create(M(10), M(10))
end = Point2D.Create(M(1), M(10))
result = SketchLine.Create(start, end)
# EndBlock

# Sketch Line
start = Point2D.Create(M(1), M(10))
end = Point2D.Create(M(0), M(10))
result = SketchLine.Create(start, end)
# EndBlock

# Sketch Line
start = Point2D.Create(M(0), M(10))
end = Point2D.Create(M(0), M(0))
result = SketchLine.Create(start, end)
# EndBlock

# Solidify Sketch
mode = InteractionMode.Solid
result = ViewHelper.SetViewMode(mode, Info13)
# EndBlock

# Split Edge
selection = Edge1
referencePoint = EdgePoint1
result = SplitEdge.ByProportion(selection, referencePoint, PERCENT(10))
# EndBlock