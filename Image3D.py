#***************************************************
#**              Written By MQX                   **
#**               Hohai University                **
#**           06-Dec-2019 00:12:18                     **
#***************************************************
from abaqus import *
from abaqusConstants import *
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
Mdb()
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-1']
p.WirePolyLine(points=(((32.000000, 28.000000, 0.000000), (30.000000, 34.000000, 15.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((30.000000, 34.000000, 15.000000), (34.000000, 40.000000, 8.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((34.000000, 40.000000, 8.000000), (32.000000, 28.000000, 0.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((31.000000, 31.000000, 7.500000),),
((32.000000, 37.000000, 11.500000),),
((33.000000, 34.000000, 4.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((30.000000, 34.000000, 15.000000), (31.000000, 39.000000, 15.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((31.000000, 39.000000, 15.000000), (34.000000, 40.000000, 8.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((34.000000, 40.000000, 8.000000), (30.000000, 34.000000, 15.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((30.500000, 36.500000, 15.000000),),
((32.500000, 39.500000, 11.500000),),
((32.000000, 37.000000, 11.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((30.000000, 41.000000, 0.000000), (32.000000, 28.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((32.000000, 28.000000, 0.000000), (34.000000, 40.000000, 8.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((34.000000, 40.000000, 8.000000), (30.000000, 41.000000, 0.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((31.000000, 34.500000, 0.000000),),
((33.000000, 34.000000, 4.000000),),
((32.000000, 40.500000, 4.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((30.000000, 34.000000, 15.000000), (32.000000, 28.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((32.000000, 28.000000, 0.000000), (23.000000, 17.000000, 7.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((23.000000, 17.000000, 7.000000), (30.000000, 34.000000, 15.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((31.000000, 31.000000, 7.500000),),
((27.500000, 22.500000, 3.500000),),
((26.500000, 25.500000, 11.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((32.000000, 28.000000, 0.000000), (24.000000, 17.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 17.000000, 0.000000), (23.000000, 17.000000, 7.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((23.000000, 17.000000, 7.000000), (32.000000, 28.000000, 0.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((28.000000, 22.500000, 0.000000),),
((23.500000, 17.000000, 3.500000),),
((27.500000, 22.500000, 3.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((25.000000, 47.000000, 3.000000), (30.000000, 41.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((30.000000, 41.000000, 0.000000), (34.000000, 40.000000, 8.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((34.000000, 40.000000, 8.000000), (25.000000, 47.000000, 3.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((27.500000, 44.000000, 1.500000),),
((32.000000, 40.500000, 4.000000),),
((29.500000, 43.500000, 5.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((31.000000, 39.000000, 15.000000), (25.000000, 47.000000, 3.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((25.000000, 47.000000, 3.000000), (34.000000, 40.000000, 8.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((34.000000, 40.000000, 8.000000), (31.000000, 39.000000, 15.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((28.000000, 43.000000, 9.000000),),
((29.500000, 43.500000, 5.500000),),
((32.500000, 39.500000, 11.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((18.000000, 26.000000, 15.000000), (30.000000, 34.000000, 15.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((30.000000, 34.000000, 15.000000), (23.000000, 17.000000, 7.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((23.000000, 17.000000, 7.000000), (18.000000, 26.000000, 15.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((24.000000, 30.000000, 15.000000),),
((26.500000, 25.500000, 11.000000),),
((20.500000, 21.500000, 11.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((25.000000, 47.000000, 3.000000), (31.000000, 39.000000, 15.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((31.000000, 39.000000, 15.000000), (18.000000, 45.000000, 13.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((18.000000, 45.000000, 13.000000), (25.000000, 47.000000, 3.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((28.000000, 43.000000, 9.000000),),
((24.500000, 42.000000, 14.000000),),
((21.500000, 46.000000, 8.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((18.000000, 45.000000, 13.000000), (31.000000, 39.000000, 15.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((31.000000, 39.000000, 15.000000), (22.000000, 41.000000, 17.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((22.000000, 41.000000, 17.000000), (18.000000, 45.000000, 13.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((24.500000, 42.000000, 14.000000),),
((26.500000, 40.000000, 16.000000),),
((20.000000, 43.000000, 15.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((31.000000, 39.000000, 15.000000), (30.000000, 34.000000, 15.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((30.000000, 34.000000, 15.000000), (22.000000, 41.000000, 17.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((22.000000, 41.000000, 17.000000), (31.000000, 39.000000, 15.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((30.500000, 36.500000, 15.000000),),
((26.000000, 37.500000, 16.000000),),
((26.500000, 40.000000, 16.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((25.000000, 47.000000, 3.000000), (22.000000, 43.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((22.000000, 43.000000, 0.000000), (30.000000, 41.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((30.000000, 41.000000, 0.000000), (25.000000, 47.000000, 3.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((23.500000, 45.000000, 1.500000),),
((26.000000, 42.000000, 0.000000),),
((27.500000, 44.000000, 1.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((24.000000, 17.000000, 0.000000), (16.000000, 16.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((16.000000, 16.000000, 0.000000), (23.000000, 17.000000, 7.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((23.000000, 17.000000, 7.000000), (24.000000, 17.000000, 0.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((20.000000, 16.500000, 0.000000),),
((19.500000, 16.500000, 3.500000),),
((23.500000, 17.000000, 3.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((25.000000, 47.000000, 3.000000), (18.000000, 45.000000, 13.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((18.000000, 45.000000, 13.000000), (18.000000, 47.000000, 6.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((18.000000, 47.000000, 6.000000), (25.000000, 47.000000, 3.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((21.500000, 46.000000, 8.000000),),
((18.000000, 46.000000, 9.500000),),
((21.500000, 47.000000, 4.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((30.000000, 34.000000, 15.000000), (18.000000, 26.000000, 15.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((18.000000, 26.000000, 15.000000), (22.000000, 41.000000, 17.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((22.000000, 41.000000, 17.000000), (30.000000, 34.000000, 15.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((24.000000, 30.000000, 15.000000),),
((20.000000, 33.500000, 16.000000),),
((26.000000, 37.500000, 16.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((16.000000, 16.000000, 0.000000), (24.000000, 17.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 17.000000, 0.000000), (32.000000, 28.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((32.000000, 28.000000, 0.000000), (30.000000, 41.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((30.000000, 41.000000, 0.000000), (22.000000, 43.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((22.000000, 43.000000, 0.000000), (11.000000, 36.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((11.000000, 36.000000, 0.000000), (10.000000, 25.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((10.000000, 25.000000, 0.000000), (16.000000, 16.000000, 0.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((20.000000, 16.500000, 0.000000),),
((28.000000, 22.500000, 0.000000),),
((31.000000, 34.500000, 0.000000),),
((26.000000, 42.000000, 0.000000),),
((16.500000, 39.500000, 0.000000),),
((10.500000, 30.500000, 0.000000),),
((13.000000, 20.500000, 0.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((15.000000, 18.500000, 8.000000), (18.000000, 26.000000, 15.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((18.000000, 26.000000, 15.000000), (23.000000, 17.000000, 7.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((23.000000, 17.000000, 7.000000), (15.000000, 18.500000, 8.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((16.500000, 22.250000, 11.500000),),
((20.500000, 21.500000, 11.000000),),
((19.000000, 17.750000, 7.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((16.000000, 16.000000, 0.000000), (15.000000, 18.500000, 8.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((15.000000, 18.500000, 8.000000), (23.000000, 17.000000, 7.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((23.000000, 17.000000, 7.000000), (16.000000, 16.000000, 0.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((15.500000, 17.250000, 4.000000),),
((19.000000, 17.750000, 7.500000),),
((19.500000, 16.500000, 3.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((22.000000, 43.000000, 0.000000), (25.000000, 47.000000, 3.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((25.000000, 47.000000, 3.000000), (18.000000, 47.000000, 6.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((18.000000, 47.000000, 6.000000), (22.000000, 43.000000, 0.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((23.500000, 45.000000, 1.500000),),
((21.500000, 47.000000, 4.500000),),
((20.000000, 45.000000, 3.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((22.000000, 43.000000, 0.000000), (18.000000, 47.000000, 6.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((18.000000, 47.000000, 6.000000), (11.000000, 36.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((11.000000, 36.000000, 0.000000), (22.000000, 43.000000, 0.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((20.000000, 45.000000, 3.000000),),
((14.500000, 41.500000, 3.000000),),
((16.500000, 39.500000, 0.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((18.000000, 26.000000, 15.000000), (12.000000, 36.000000, 12.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((12.000000, 36.000000, 12.000000), (22.000000, 41.000000, 17.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((22.000000, 41.000000, 17.000000), (18.000000, 26.000000, 15.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((15.000000, 31.000000, 13.500000),),
((17.000000, 38.500000, 14.500000),),
((20.000000, 33.500000, 16.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((12.000000, 36.000000, 12.000000), (18.000000, 45.000000, 13.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((18.000000, 45.000000, 13.000000), (22.000000, 41.000000, 17.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((22.000000, 41.000000, 17.000000), (12.000000, 36.000000, 12.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((15.000000, 40.500000, 12.500000),),
((20.000000, 43.000000, 15.000000),),
((17.000000, 38.500000, 14.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((15.000000, 18.500000, 8.000000), (12.000000, 36.000000, 12.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((12.000000, 36.000000, 12.000000), (18.000000, 26.000000, 15.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((18.000000, 26.000000, 15.000000), (15.000000, 18.500000, 8.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((13.500000, 27.250000, 10.000000),),
((15.000000, 31.000000, 13.500000),),
((16.500000, 22.250000, 11.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((18.000000, 45.000000, 13.000000), (12.000000, 36.000000, 12.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((12.000000, 36.000000, 12.000000), (18.000000, 47.000000, 6.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((18.000000, 47.000000, 6.000000), (18.000000, 45.000000, 13.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((15.000000, 40.500000, 12.500000),),
((15.000000, 41.500000, 9.000000),),
((18.000000, 46.000000, 9.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((10.000000, 25.000000, 0.000000), (15.000000, 18.500000, 8.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((15.000000, 18.500000, 8.000000), (16.000000, 16.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((16.000000, 16.000000, 0.000000), (10.000000, 25.000000, 0.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((12.500000, 21.750000, 4.000000),),
((15.500000, 17.250000, 4.000000),),
((13.000000, 20.500000, 0.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((18.000000, 47.000000, 6.000000), (12.000000, 36.000000, 12.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((12.000000, 36.000000, 12.000000), (11.000000, 36.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((11.000000, 36.000000, 0.000000), (18.000000, 47.000000, 6.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((15.000000, 41.500000, 9.000000),),
((11.500000, 36.000000, 6.000000),),
((14.500000, 41.500000, 3.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((12.000000, 36.000000, 12.000000), (15.000000, 18.500000, 8.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((15.000000, 18.500000, 8.000000), (10.000000, 25.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((10.000000, 25.000000, 0.000000), (12.000000, 36.000000, 12.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((13.500000, 27.250000, 10.000000),),
((12.500000, 21.750000, 4.000000),),
((11.000000, 30.500000, 6.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((12.000000, 36.000000, 12.000000), (10.000000, 25.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((10.000000, 25.000000, 0.000000), (11.000000, 36.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((11.000000, 36.000000, 0.000000), (12.000000, 36.000000, 12.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((11.000000, 30.500000, 6.000000),),
((10.500000, 30.500000, 0.000000),),
((11.500000, 36.000000, 6.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((40.000000, 77.000000, 0.000000), (46.000000, 63.000000, 4.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((46.000000, 63.000000, 4.000000), (46.000000, 68.000000, 11.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((46.000000, 68.000000, 11.000000), (40.000000, 77.000000, 0.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((43.000000, 70.000000, 2.000000),),
((46.000000, 65.500000, 7.500000),),
((43.000000, 72.500000, 5.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((43.000000, 76.000000, 12.000000), (40.000000, 77.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((40.000000, 77.000000, 0.000000), (46.000000, 68.000000, 11.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((46.000000, 68.000000, 11.000000), (43.000000, 76.000000, 12.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((41.500000, 76.500000, 6.000000),),
((43.000000, 72.500000, 5.500000),),
((44.500000, 72.000000, 11.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((46.000000, 63.000000, 4.000000), (38.000000, 57.000000, 9.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((38.000000, 57.000000, 9.000000), (46.000000, 68.000000, 11.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((46.000000, 68.000000, 11.000000), (46.000000, 63.000000, 4.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((42.000000, 60.000000, 6.500000),),
((42.000000, 62.500000, 10.000000),),
((46.000000, 65.500000, 7.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((38.000000, 57.000000, 9.000000), (36.000000, 62.000000, 18.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((36.000000, 62.000000, 18.000000), (46.000000, 68.000000, 11.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((46.000000, 68.000000, 11.000000), (38.000000, 57.000000, 9.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((37.000000, 59.500000, 13.500000),),
((41.000000, 65.000000, 14.500000),),
((42.000000, 62.500000, 10.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((36.000000, 62.000000, 18.000000), (38.000000, 57.000000, 9.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((38.000000, 57.000000, 9.000000), (35.000000, 55.000000, 10.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((35.000000, 55.000000, 10.000000), (36.000000, 62.000000, 18.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((37.000000, 59.500000, 13.500000),),
((36.500000, 56.000000, 9.500000),),
((35.500000, 58.500000, 14.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((36.000000, 62.000000, 18.000000), (43.000000, 76.000000, 12.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((43.000000, 76.000000, 12.000000), (46.000000, 68.000000, 11.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((46.000000, 68.000000, 11.000000), (36.000000, 62.000000, 18.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((39.500000, 69.000000, 15.000000),),
((44.500000, 72.000000, 11.500000),),
((41.000000, 65.000000, 14.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((38.000000, 57.000000, 9.000000), (46.000000, 63.000000, 4.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((46.000000, 63.000000, 4.000000), (34.000000, 57.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((34.000000, 57.000000, 0.000000), (38.000000, 57.000000, 9.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((42.000000, 60.000000, 6.500000),),
((40.000000, 60.000000, 2.000000),),
((36.000000, 57.000000, 4.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((35.000000, 55.000000, 10.000000), (38.000000, 57.000000, 9.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((38.000000, 57.000000, 9.000000), (34.000000, 57.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((34.000000, 57.000000, 0.000000), (35.000000, 55.000000, 10.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((36.500000, 56.000000, 9.500000),),
((36.000000, 57.000000, 4.500000),),
((34.500000, 56.000000, 5.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((43.000000, 76.000000, 12.000000), (36.000000, 62.000000, 18.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((36.000000, 62.000000, 18.000000), (31.500000, 73.000000, 18.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((31.500000, 73.000000, 18.000000), (43.000000, 76.000000, 12.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((39.500000, 69.000000, 15.000000),),
((33.750000, 67.500000, 18.000000),),
((37.250000, 74.500000, 15.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((46.000000, 63.000000, 4.000000), (40.000000, 77.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((40.000000, 77.000000, 0.000000), (34.000000, 57.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((34.000000, 57.000000, 0.000000), (46.000000, 63.000000, 4.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((43.000000, 70.000000, 2.000000),),
((37.000000, 67.000000, 0.000000),),
((40.000000, 60.000000, 2.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((36.000000, 62.000000, 18.000000), (35.000000, 55.000000, 10.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((35.000000, 55.000000, 10.000000), (23.000000, 54.000000, 13.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((23.000000, 54.000000, 13.000000), (36.000000, 62.000000, 18.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((35.500000, 58.500000, 14.000000),),
((29.000000, 54.500000, 11.500000),),
((29.500000, 58.000000, 15.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((43.000000, 76.000000, 12.000000), (26.000000, 78.000000, 11.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((26.000000, 78.000000, 11.000000), (40.000000, 77.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((40.000000, 77.000000, 0.000000), (43.000000, 76.000000, 12.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((34.500000, 77.000000, 11.500000),),
((33.000000, 77.500000, 5.500000),),
((41.500000, 76.500000, 6.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((20.000000, 55.000000, 4.000000), (35.000000, 55.000000, 10.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((35.000000, 55.000000, 10.000000), (34.000000, 57.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((34.000000, 57.000000, 0.000000), (20.000000, 55.000000, 4.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((27.500000, 55.000000, 7.000000),),
((34.500000, 56.000000, 5.000000),),
((27.000000, 56.000000, 2.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((26.000000, 78.000000, 11.000000), (43.000000, 76.000000, 12.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((43.000000, 76.000000, 12.000000), (31.500000, 73.000000, 18.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((31.500000, 73.000000, 18.000000), (26.000000, 78.000000, 11.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((34.500000, 77.000000, 11.500000),),
((37.250000, 74.500000, 15.000000),),
((28.750000, 75.500000, 14.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((36.000000, 62.000000, 18.000000), (19.000000, 66.000000, 19.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((19.000000, 66.000000, 19.000000), (31.500000, 73.000000, 18.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((31.500000, 73.000000, 18.000000), (36.000000, 62.000000, 18.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((27.500000, 64.000000, 18.500000),),
((25.250000, 69.500000, 18.500000),),
((33.750000, 67.500000, 18.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((35.000000, 55.000000, 10.000000), (20.000000, 55.000000, 4.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((20.000000, 55.000000, 4.000000), (23.000000, 54.000000, 13.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((23.000000, 54.000000, 13.000000), (35.000000, 55.000000, 10.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((27.500000, 55.000000, 7.000000),),
((21.500000, 54.500000, 8.500000),),
((29.000000, 54.500000, 11.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((18.000000, 68.000000, 0.000000), (40.000000, 77.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((40.000000, 77.000000, 0.000000), (34.000000, 57.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((34.000000, 57.000000, 0.000000), (17.000000, 60.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((17.000000, 60.000000, 0.000000), (18.000000, 68.000000, 0.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((29.000000, 72.500000, 0.000000),),
((37.000000, 67.000000, 0.000000),),
((25.500000, 58.500000, 0.000000),),
((17.500000, 64.000000, 0.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((19.000000, 66.000000, 19.000000), (36.000000, 62.000000, 18.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((36.000000, 62.000000, 18.000000), (23.000000, 54.000000, 13.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((23.000000, 54.000000, 13.000000), (19.000000, 66.000000, 19.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((27.500000, 64.000000, 18.500000),),
((29.500000, 58.000000, 15.500000),),
((21.000000, 60.000000, 16.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((17.000000, 60.000000, 0.000000), (20.000000, 55.000000, 4.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((20.000000, 55.000000, 4.000000), (34.000000, 57.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((34.000000, 57.000000, 0.000000), (17.000000, 60.000000, 0.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((18.500000, 57.500000, 2.000000),),
((27.000000, 56.000000, 2.000000),),
((25.500000, 58.500000, 0.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((19.000000, 66.000000, 19.000000), (26.000000, 78.000000, 11.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((26.000000, 78.000000, 11.000000), (31.500000, 73.000000, 18.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((31.500000, 73.000000, 18.000000), (19.000000, 66.000000, 19.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((22.500000, 72.000000, 15.000000),),
((28.750000, 75.500000, 14.500000),),
((25.250000, 69.500000, 18.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((26.000000, 78.000000, 11.000000), (18.000000, 68.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((18.000000, 68.000000, 0.000000), (40.000000, 77.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((40.000000, 77.000000, 0.000000), (26.000000, 78.000000, 11.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((22.000000, 73.000000, 5.500000),),
((29.000000, 72.500000, 0.000000),),
((33.000000, 77.500000, 5.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((14.000000, 59.000000, 12.000000), (19.000000, 66.000000, 19.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((19.000000, 66.000000, 19.000000), (23.000000, 54.000000, 13.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((23.000000, 54.000000, 13.000000), (14.000000, 59.000000, 12.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((16.500000, 62.500000, 15.500000),),
((21.000000, 60.000000, 16.000000),),
((18.500000, 56.500000, 12.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((20.000000, 55.000000, 4.000000), (14.000000, 59.000000, 12.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((14.000000, 59.000000, 12.000000), (23.000000, 54.000000, 13.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((23.000000, 54.000000, 13.000000), (20.000000, 55.000000, 4.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((17.000000, 57.000000, 8.000000),),
((18.500000, 56.500000, 12.500000),),
((21.500000, 54.500000, 8.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((18.000000, 68.000000, 0.000000), (26.000000, 78.000000, 11.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((26.000000, 78.000000, 11.000000), (15.000000, 69.000000, 7.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((15.000000, 69.000000, 7.000000), (18.000000, 68.000000, 0.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((22.000000, 73.000000, 5.500000),),
((20.500000, 73.500000, 9.000000),),
((16.500000, 68.500000, 3.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((26.000000, 78.000000, 11.000000), (19.000000, 66.000000, 19.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((19.000000, 66.000000, 19.000000), (15.000000, 69.000000, 7.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((15.000000, 69.000000, 7.000000), (26.000000, 78.000000, 11.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((22.500000, 72.000000, 15.000000),),
((17.000000, 67.500000, 13.000000),),
((20.500000, 73.500000, 9.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((14.000000, 59.000000, 12.000000), (20.000000, 55.000000, 4.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((20.000000, 55.000000, 4.000000), (17.000000, 60.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((17.000000, 60.000000, 0.000000), (14.000000, 59.000000, 12.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((17.000000, 57.000000, 8.000000),),
((18.500000, 57.500000, 2.000000),),
((15.500000, 59.500000, 6.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((19.000000, 66.000000, 19.000000), (14.000000, 59.000000, 12.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((14.000000, 59.000000, 12.000000), (15.000000, 69.000000, 7.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((15.000000, 69.000000, 7.000000), (19.000000, 66.000000, 19.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((16.500000, 62.500000, 15.500000),),
((14.500000, 64.000000, 9.500000),),
((17.000000, 67.500000, 13.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((17.000000, 60.000000, 0.000000), (18.000000, 68.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((18.000000, 68.000000, 0.000000), (15.000000, 69.000000, 7.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((15.000000, 69.000000, 7.000000), (17.000000, 60.000000, 0.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((17.500000, 64.000000, 0.000000),),
((16.500000, 68.500000, 3.500000),),
((16.000000, 64.500000, 3.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((14.000000, 59.000000, 12.000000), (17.000000, 60.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((17.000000, 60.000000, 0.000000), (15.000000, 69.000000, 7.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((15.000000, 69.000000, 7.000000), (14.000000, 59.000000, 12.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((15.500000, 59.500000, 6.000000),),
((16.000000, 64.500000, 3.500000),),
((14.500000, 64.000000, 9.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((100.000000, 57.000000, 4.000000), (100.000000, 69.000000, 7.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 69.000000, 7.000000), (100.000000, 69.000000, 25.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 69.000000, 25.000000), (100.000000, 58.000000, 26.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 58.000000, 26.000000), (100.000000, 50.000000, 22.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 50.000000, 22.000000), (100.000000, 49.000000, 11.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 49.000000, 11.000000), (100.000000, 57.000000, 4.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((100.000000, 63.000000, 5.500000),),
((100.000000, 69.000000, 16.000000),),
((100.000000, 63.500000, 25.500000),),
((100.000000, 54.000000, 24.000000),),
((100.000000, 49.500000, 16.500000),),
((100.000000, 53.000000, 7.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((100.000000, 50.000000, 22.000000), (100.000000, 49.000000, 11.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 49.000000, 11.000000), (94.000000, 47.000000, 23.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((94.000000, 47.000000, 23.000000), (100.000000, 50.000000, 22.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((100.000000, 49.500000, 16.500000),),
((97.000000, 48.000000, 17.000000),),
((97.000000, 48.500000, 22.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((100.000000, 49.000000, 11.000000), (100.000000, 57.000000, 4.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 57.000000, 4.000000), (91.000000, 56.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((91.000000, 56.000000, 0.000000), (100.000000, 49.000000, 11.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((100.000000, 53.000000, 7.500000),),
((95.500000, 56.500000, 2.000000),),
((95.500000, 52.500000, 5.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((100.000000, 50.000000, 22.000000), (94.000000, 47.000000, 23.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((94.000000, 47.000000, 23.000000), (100.000000, 58.000000, 26.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 58.000000, 26.000000), (100.000000, 50.000000, 22.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((97.000000, 48.500000, 22.500000),),
((97.000000, 52.500000, 24.500000),),
((100.000000, 54.000000, 24.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((100.000000, 57.000000, 4.000000), (90.000000, 69.000000, 5.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((90.000000, 69.000000, 5.000000), (91.000000, 56.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((91.000000, 56.000000, 0.000000), (100.000000, 57.000000, 4.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((95.000000, 63.000000, 4.500000),),
((90.500000, 62.500000, 2.500000),),
((95.500000, 56.500000, 2.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((89.000000, 47.000000, 10.000000), (100.000000, 49.000000, 11.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 49.000000, 11.000000), (91.000000, 56.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((91.000000, 56.000000, 0.000000), (89.000000, 47.000000, 10.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((94.500000, 48.000000, 10.500000),),
((95.500000, 52.500000, 5.500000),),
((90.000000, 51.500000, 5.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((90.000000, 69.000000, 5.000000), (100.000000, 57.000000, 4.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 57.000000, 4.000000), (100.000000, 69.000000, 7.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 69.000000, 7.000000), (90.000000, 69.000000, 5.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((95.000000, 63.000000, 4.500000),),
((100.000000, 63.000000, 5.500000),),
((95.000000, 69.000000, 6.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((100.000000, 49.000000, 11.000000), (89.000000, 47.000000, 10.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((89.000000, 47.000000, 10.000000), (94.000000, 47.000000, 23.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((94.000000, 47.000000, 23.000000), (100.000000, 49.000000, 11.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((94.500000, 48.000000, 10.500000),),
((91.500000, 47.000000, 16.500000),),
((97.000000, 48.000000, 17.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((91.000000, 70.000000, 26.000000), (100.000000, 69.000000, 25.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 69.000000, 25.000000), (100.000000, 58.000000, 26.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 58.000000, 26.000000), (91.000000, 70.000000, 26.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((95.500000, 69.500000, 25.500000),),
((100.000000, 63.500000, 25.500000),),
((95.500000, 64.000000, 26.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((100.000000, 69.000000, 25.000000), (91.000000, 70.000000, 26.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((91.000000, 70.000000, 26.000000), (87.000000, 70.000000, 18.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((87.000000, 70.000000, 18.000000), (100.000000, 69.000000, 25.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((95.500000, 69.500000, 25.500000),),
((89.000000, 70.000000, 22.000000),),
((93.500000, 69.500000, 21.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((100.000000, 69.000000, 7.000000), (100.000000, 69.000000, 25.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 69.000000, 25.000000), (87.000000, 70.000000, 18.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((87.000000, 70.000000, 18.000000), (100.000000, 69.000000, 7.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((100.000000, 69.000000, 16.000000),),
((93.500000, 69.500000, 21.500000),),
((93.500000, 69.500000, 12.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((94.000000, 47.000000, 23.000000), (77.000000, 56.000000, 26.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((77.000000, 56.000000, 26.000000), (100.000000, 58.000000, 26.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 58.000000, 26.000000), (94.000000, 47.000000, 23.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((85.500000, 51.500000, 24.500000),),
((88.500000, 57.000000, 26.000000),),
((97.000000, 52.500000, 24.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((90.000000, 69.000000, 5.000000), (100.000000, 69.000000, 7.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 69.000000, 7.000000), (87.000000, 70.000000, 18.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((87.000000, 70.000000, 18.000000), (90.000000, 69.000000, 5.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((95.000000, 69.000000, 6.000000),),
((93.500000, 69.500000, 12.500000),),
((88.500000, 69.500000, 11.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((86.000000, 66.000000, 26.000000), (77.000000, 56.000000, 26.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((77.000000, 56.000000, 26.000000), (100.000000, 58.000000, 26.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 58.000000, 26.000000), (91.000000, 70.000000, 26.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((91.000000, 70.000000, 26.000000), (86.000000, 66.000000, 26.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((81.500000, 61.000000, 26.000000),),
((88.500000, 57.000000, 26.000000),),
((95.500000, 64.000000, 26.000000),),
((88.500000, 68.000000, 26.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((89.000000, 47.000000, 10.000000), (78.500000, 49.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((78.500000, 49.000000, 21.000000), (94.000000, 47.000000, 23.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((94.000000, 47.000000, 23.000000), (89.000000, 47.000000, 10.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((83.750000, 48.000000, 15.500000),),
((86.250000, 48.000000, 22.000000),),
((91.500000, 47.000000, 16.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((75.000000, 68.000000, 16.000000), (90.000000, 69.000000, 5.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((90.000000, 69.000000, 5.000000), (87.000000, 70.000000, 18.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((87.000000, 70.000000, 18.000000), (75.000000, 68.000000, 16.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((82.500000, 68.500000, 10.500000),),
((88.500000, 69.500000, 11.500000),),
((81.000000, 69.000000, 17.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((78.500000, 49.000000, 21.000000), (77.000000, 56.000000, 26.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((77.000000, 56.000000, 26.000000), (94.000000, 47.000000, 23.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((94.000000, 47.000000, 23.000000), (78.500000, 49.000000, 21.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((77.750000, 52.500000, 23.500000),),
((85.500000, 51.500000, 24.500000),),
((86.250000, 48.000000, 22.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((78.000000, 49.000000, 11.000000), (78.500000, 49.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((78.500000, 49.000000, 21.000000), (89.000000, 47.000000, 10.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((89.000000, 47.000000, 10.000000), (78.000000, 49.000000, 11.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((78.250000, 49.000000, 16.000000),),
((83.750000, 48.000000, 15.500000),),
((83.500000, 48.000000, 10.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((78.000000, 49.000000, 11.000000), (89.000000, 47.000000, 10.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((89.000000, 47.000000, 10.000000), (91.000000, 56.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((91.000000, 56.000000, 0.000000), (78.000000, 49.000000, 11.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((83.500000, 48.000000, 10.500000),),
((90.000000, 51.500000, 5.000000),),
((84.500000, 52.500000, 5.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((86.000000, 66.000000, 26.000000), (75.000000, 68.000000, 16.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((75.000000, 68.000000, 16.000000), (87.000000, 70.000000, 18.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((87.000000, 70.000000, 18.000000), (86.000000, 66.000000, 26.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((80.500000, 67.000000, 21.000000),),
((81.000000, 69.000000, 17.000000),),
((86.500000, 68.000000, 22.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((90.000000, 69.000000, 5.000000), (76.000000, 63.500000, 7.500000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((76.000000, 63.500000, 7.500000), (91.000000, 56.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((91.000000, 56.000000, 0.000000), (90.000000, 69.000000, 5.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((83.000000, 66.250000, 6.250000),),
((83.500000, 59.750000, 3.750000),),
((90.500000, 62.500000, 2.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((90.000000, 69.000000, 5.000000), (75.000000, 68.000000, 16.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((75.000000, 68.000000, 16.000000), (76.000000, 63.500000, 7.500000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((76.000000, 63.500000, 7.500000), (90.000000, 69.000000, 5.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((82.500000, 68.500000, 10.500000),),
((75.500000, 65.750000, 11.750000),),
((83.000000, 66.250000, 6.250000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((76.000000, 63.500000, 7.500000), (78.000000, 49.000000, 11.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((78.000000, 49.000000, 11.000000), (91.000000, 56.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((91.000000, 56.000000, 0.000000), (76.000000, 63.500000, 7.500000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((77.000000, 56.250000, 9.250000),),
((84.500000, 52.500000, 5.500000),),
((83.500000, 59.750000, 3.750000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((77.000000, 56.000000, 26.000000), (75.000000, 68.000000, 16.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((75.000000, 68.000000, 16.000000), (86.000000, 66.000000, 26.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((86.000000, 66.000000, 26.000000), (77.000000, 56.000000, 26.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((76.000000, 62.000000, 21.000000),),
((80.500000, 67.000000, 21.000000),),
((81.500000, 61.000000, 26.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((91.000000, 70.000000, 26.000000), (86.000000, 66.000000, 26.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((86.000000, 66.000000, 26.000000), (87.000000, 70.000000, 18.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((87.000000, 70.000000, 18.000000), (91.000000, 70.000000, 26.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((88.500000, 68.000000, 26.000000),),
((86.500000, 68.000000, 22.000000),),
((89.000000, 70.000000, 22.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((78.000000, 49.000000, 11.000000), (76.000000, 63.500000, 7.500000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((76.000000, 63.500000, 7.500000), (71.000000, 56.000000, 15.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((71.000000, 56.000000, 15.000000), (78.000000, 49.000000, 11.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((77.000000, 56.250000, 9.250000),),
((73.500000, 59.750000, 11.250000),),
((74.500000, 52.500000, 13.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((78.500000, 49.000000, 21.000000), (78.000000, 49.000000, 11.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((78.000000, 49.000000, 11.000000), (71.000000, 56.000000, 15.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((71.000000, 56.000000, 15.000000), (78.500000, 49.000000, 21.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((78.250000, 49.000000, 16.000000),),
((74.500000, 52.500000, 13.000000),),
((74.750000, 52.500000, 18.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((77.000000, 56.000000, 26.000000), (78.500000, 49.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((78.500000, 49.000000, 21.000000), (71.000000, 56.000000, 15.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((71.000000, 56.000000, 15.000000), (77.000000, 56.000000, 26.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((77.750000, 52.500000, 23.500000),),
((74.750000, 52.500000, 18.000000),),
((74.000000, 56.000000, 20.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((75.000000, 68.000000, 16.000000), (77.000000, 56.000000, 26.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((77.000000, 56.000000, 26.000000), (71.000000, 56.000000, 15.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((71.000000, 56.000000, 15.000000), (75.000000, 68.000000, 16.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((76.000000, 62.000000, 21.000000),),
((74.000000, 56.000000, 20.500000),),
((73.000000, 62.000000, 15.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((76.000000, 63.500000, 7.500000), (75.000000, 68.000000, 16.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((75.000000, 68.000000, 16.000000), (71.000000, 56.000000, 15.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((71.000000, 56.000000, 15.000000), (76.000000, 63.500000, 7.500000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((75.500000, 65.750000, 11.750000),),
((73.000000, 62.000000, 15.500000),),
((73.500000, 59.750000, 11.250000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((84.000000, 100.000000, 43.000000), (91.000000, 100.000000, 20.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((91.000000, 100.000000, 20.000000), (85.000000, 85.000000, 35.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((85.000000, 85.000000, 35.000000), (84.000000, 100.000000, 43.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((87.500000, 100.000000, 31.500000),),
((88.000000, 92.500000, 27.500000),),
((84.500000, 92.500000, 39.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((91.000000, 100.000000, 20.000000), (84.000000, 83.000000, 17.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((84.000000, 83.000000, 17.000000), (85.000000, 85.000000, 35.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((85.000000, 85.000000, 35.000000), (91.000000, 100.000000, 20.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((87.500000, 91.500000, 18.500000),),
((84.500000, 84.000000, 26.000000),),
((88.000000, 92.500000, 27.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((91.000000, 100.000000, 20.000000), (80.000000, 100.000000, 11.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((80.000000, 100.000000, 11.000000), (84.000000, 83.000000, 17.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((84.000000, 83.000000, 17.000000), (91.000000, 100.000000, 20.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((85.500000, 100.000000, 15.500000),),
((82.000000, 91.500000, 14.000000),),
((87.500000, 91.500000, 18.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((59.000000, 70.000000, 22.000000), (59.000000, 85.000000, 5.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((59.000000, 85.000000, 5.000000), (55.000000, 70.000000, 18.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((55.000000, 70.000000, 18.000000), (59.000000, 70.000000, 22.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((59.000000, 77.500000, 13.500000),),
((57.000000, 77.500000, 11.500000),),
((57.000000, 70.000000, 20.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((59.000000, 85.000000, 5.000000), (55.000000, 93.000000, 4.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((55.000000, 93.000000, 4.000000), (50.000000, 85.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((50.000000, 85.000000, 0.000000), (59.000000, 85.000000, 5.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((57.000000, 89.000000, 4.500000),),
((52.500000, 89.000000, 2.000000),),
((54.500000, 85.000000, 2.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((58.000000, 95.000000, 55.000000), (65.000000, 75.000000, 41.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((65.000000, 75.000000, 41.000000), (60.000000, 73.000000, 43.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((60.000000, 73.000000, 43.000000), (58.000000, 95.000000, 55.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((61.500000, 85.000000, 48.000000),),
((62.500000, 74.000000, 42.000000),),
((59.000000, 84.000000, 49.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((84.000000, 83.000000, 17.000000), (59.000000, 70.000000, 22.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((59.000000, 70.000000, 22.000000), (85.000000, 85.000000, 35.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((85.000000, 85.000000, 35.000000), (84.000000, 83.000000, 17.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((71.500000, 76.500000, 19.500000),),
((72.000000, 77.500000, 28.500000),),
((84.500000, 84.000000, 26.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((67.000000, 96.000000, 51.000000), (84.000000, 100.000000, 43.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((84.000000, 100.000000, 43.000000), (85.000000, 85.000000, 35.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((85.000000, 85.000000, 35.000000), (67.000000, 96.000000, 51.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((75.500000, 98.000000, 47.000000),),
((84.500000, 92.500000, 39.000000),),
((76.000000, 90.500000, 43.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((59.000000, 70.000000, 22.000000), (65.000000, 75.000000, 41.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((65.000000, 75.000000, 41.000000), (85.000000, 85.000000, 35.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((85.000000, 85.000000, 35.000000), (59.000000, 70.000000, 22.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((62.000000, 72.500000, 31.500000),),
((75.000000, 80.000000, 38.000000),),
((72.000000, 77.500000, 28.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((65.000000, 75.000000, 41.000000), (67.000000, 96.000000, 51.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((67.000000, 96.000000, 51.000000), (85.000000, 85.000000, 35.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((85.000000, 85.000000, 35.000000), (65.000000, 75.000000, 41.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((66.000000, 85.500000, 46.000000),),
((76.000000, 90.500000, 43.000000),),
((75.000000, 80.000000, 38.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((80.000000, 100.000000, 11.000000), (59.000000, 85.000000, 5.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((59.000000, 85.000000, 5.000000), (84.000000, 83.000000, 17.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((84.000000, 83.000000, 17.000000), (80.000000, 100.000000, 11.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((69.500000, 92.500000, 8.000000),),
((71.500000, 84.000000, 11.000000),),
((82.000000, 91.500000, 14.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((65.000000, 75.000000, 41.000000), (58.000000, 95.000000, 55.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((58.000000, 95.000000, 55.000000), (67.000000, 96.000000, 51.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((67.000000, 96.000000, 51.000000), (65.000000, 75.000000, 41.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((61.500000, 85.000000, 48.000000),),
((62.500000, 95.500000, 53.000000),),
((66.000000, 85.500000, 46.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((65.000000, 75.000000, 41.000000), (59.000000, 70.000000, 22.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((59.000000, 70.000000, 22.000000), (60.000000, 73.000000, 43.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((60.000000, 73.000000, 43.000000), (65.000000, 75.000000, 41.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((62.000000, 72.500000, 31.500000),),
((59.500000, 71.500000, 32.500000),),
((62.500000, 74.000000, 42.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((59.000000, 85.000000, 5.000000), (50.000000, 85.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((50.000000, 85.000000, 0.000000), (55.000000, 70.000000, 18.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((55.000000, 70.000000, 18.000000), (59.000000, 85.000000, 5.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((54.500000, 85.000000, 2.500000),),
((52.500000, 77.500000, 9.000000),),
((57.000000, 77.500000, 11.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((58.000000, 95.000000, 55.000000), (57.000000, 100.000000, 53.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((57.000000, 100.000000, 53.000000), (67.000000, 96.000000, 51.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((67.000000, 96.000000, 51.000000), (58.000000, 95.000000, 55.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((57.500000, 97.500000, 54.000000),),
((62.000000, 98.000000, 52.000000),),
((62.500000, 95.500000, 53.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((59.000000, 85.000000, 5.000000), (80.000000, 100.000000, 11.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((80.000000, 100.000000, 11.000000), (63.000000, 100.000000, 5.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((63.000000, 100.000000, 5.000000), (59.000000, 85.000000, 5.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((69.500000, 92.500000, 8.000000),),
((71.500000, 100.000000, 8.000000),),
((61.000000, 92.500000, 5.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((67.000000, 96.000000, 51.000000), (57.000000, 100.000000, 53.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((57.000000, 100.000000, 53.000000), (84.000000, 100.000000, 43.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((84.000000, 100.000000, 43.000000), (67.000000, 96.000000, 51.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((62.000000, 98.000000, 52.000000),),
((70.500000, 100.000000, 48.000000),),
((75.500000, 98.000000, 47.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((59.000000, 85.000000, 5.000000), (59.000000, 70.000000, 22.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((59.000000, 70.000000, 22.000000), (84.000000, 83.000000, 17.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((84.000000, 83.000000, 17.000000), (59.000000, 85.000000, 5.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((59.000000, 77.500000, 13.500000),),
((71.500000, 76.500000, 19.500000),),
((71.500000, 84.000000, 11.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((55.000000, 93.000000, 4.000000), (59.000000, 85.000000, 5.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((59.000000, 85.000000, 5.000000), (63.000000, 100.000000, 5.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((63.000000, 100.000000, 5.000000), (55.000000, 93.000000, 4.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((57.000000, 89.000000, 4.500000),),
((61.000000, 92.500000, 5.000000),),
((59.000000, 96.500000, 4.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((29.000000, 88.000000, 52.000000), (58.000000, 95.000000, 55.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((58.000000, 95.000000, 55.000000), (60.000000, 73.000000, 43.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((60.000000, 73.000000, 43.000000), (29.000000, 88.000000, 52.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((43.500000, 91.500000, 53.500000),),
((59.000000, 84.000000, 49.000000),),
((44.500000, 80.500000, 47.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((91.000000, 100.000000, 20.000000), (84.000000, 100.000000, 43.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((84.000000, 100.000000, 43.000000), (57.000000, 100.000000, 53.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((57.000000, 100.000000, 53.000000), (24.000000, 100.000000, 48.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 100.000000, 48.000000), (17.000000, 100.000000, 30.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((17.000000, 100.000000, 30.000000), (21.500000, 100.000000, 23.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((21.500000, 100.000000, 23.000000), (63.000000, 100.000000, 5.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((63.000000, 100.000000, 5.000000), (80.000000, 100.000000, 11.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((80.000000, 100.000000, 11.000000), (91.000000, 100.000000, 20.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((87.500000, 100.000000, 31.500000),),
((70.500000, 100.000000, 48.000000),),
((40.500000, 100.000000, 50.500000),),
((20.500000, 100.000000, 39.000000),),
((19.250000, 100.000000, 26.500000),),
((42.250000, 100.000000, 14.000000),),
((71.500000, 100.000000, 8.000000),),
((85.500000, 100.000000, 15.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((29.000000, 73.000000, 43.000000), (29.000000, 88.000000, 52.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((29.000000, 88.000000, 52.000000), (60.000000, 73.000000, 43.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((60.000000, 73.000000, 43.000000), (29.000000, 73.000000, 43.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((29.000000, 80.500000, 47.500000),),
((44.500000, 80.500000, 47.500000),),
((44.500000, 73.000000, 43.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((59.000000, 70.000000, 22.000000), (29.000000, 73.000000, 43.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((29.000000, 73.000000, 43.000000), (60.000000, 73.000000, 43.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((60.000000, 73.000000, 43.000000), (59.000000, 70.000000, 22.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((44.000000, 71.500000, 32.500000),),
((44.500000, 73.000000, 43.000000),),
((59.500000, 71.500000, 32.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((59.000000, 70.000000, 22.000000), (27.000000, 71.000000, 25.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((27.000000, 71.000000, 25.000000), (29.000000, 73.000000, 43.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((29.000000, 73.000000, 43.000000), (59.000000, 70.000000, 22.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((43.000000, 70.500000, 23.500000),),
((28.000000, 72.000000, 34.000000),),
((44.000000, 71.500000, 32.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((27.000000, 71.000000, 25.000000), (59.000000, 70.000000, 22.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((59.000000, 70.000000, 22.000000), (55.000000, 70.000000, 18.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((55.000000, 70.000000, 18.000000), (27.000000, 71.000000, 25.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((43.000000, 70.500000, 23.500000),),
((57.000000, 70.000000, 20.000000),),
((41.000000, 70.500000, 21.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((24.000000, 100.000000, 48.000000), (57.000000, 100.000000, 53.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((57.000000, 100.000000, 53.000000), (29.000000, 88.000000, 52.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((29.000000, 88.000000, 52.000000), (24.000000, 100.000000, 48.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((40.500000, 100.000000, 50.500000),),
((43.000000, 94.000000, 52.500000),),
((26.500000, 94.000000, 50.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((29.000000, 88.000000, 52.000000), (57.000000, 100.000000, 53.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((57.000000, 100.000000, 53.000000), (58.000000, 95.000000, 55.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((58.000000, 95.000000, 55.000000), (29.000000, 88.000000, 52.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((43.000000, 94.000000, 52.500000),),
((57.500000, 97.500000, 54.000000),),
((43.500000, 91.500000, 53.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((23.000000, 81.000000, 14.000000), (27.000000, 71.000000, 25.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((27.000000, 71.000000, 25.000000), (55.000000, 70.000000, 18.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((55.000000, 70.000000, 18.000000), (23.000000, 81.000000, 14.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((25.000000, 76.000000, 19.500000),),
((41.000000, 70.500000, 21.500000),),
((39.000000, 75.500000, 16.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((50.000000, 85.000000, 0.000000), (23.000000, 81.000000, 14.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((23.000000, 81.000000, 14.000000), (55.000000, 70.000000, 18.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((55.000000, 70.000000, 18.000000), (50.000000, 85.000000, 0.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((36.500000, 83.000000, 7.000000),),
((39.000000, 75.500000, 16.000000),),
((52.500000, 77.500000, 9.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((21.500000, 100.000000, 23.000000), (55.000000, 93.000000, 4.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((55.000000, 93.000000, 4.000000), (63.000000, 100.000000, 5.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((63.000000, 100.000000, 5.000000), (21.500000, 100.000000, 23.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((38.250000, 96.500000, 13.500000),),
((59.000000, 96.500000, 4.500000),),
((42.250000, 100.000000, 14.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((55.000000, 93.000000, 4.000000), (22.000000, 89.000000, 17.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((22.000000, 89.000000, 17.000000), (50.000000, 85.000000, 0.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((50.000000, 85.000000, 0.000000), (55.000000, 93.000000, 4.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((38.500000, 91.000000, 10.500000),),
((36.000000, 87.000000, 8.500000),),
((52.500000, 89.000000, 2.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((22.000000, 89.000000, 17.000000), (55.000000, 93.000000, 4.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((55.000000, 93.000000, 4.000000), (21.500000, 100.000000, 23.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((21.500000, 100.000000, 23.000000), (22.000000, 89.000000, 17.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((38.500000, 91.000000, 10.500000),),
((38.250000, 96.500000, 13.500000),),
((21.750000, 94.500000, 20.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((50.000000, 85.000000, 0.000000), (22.000000, 89.000000, 17.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((22.000000, 89.000000, 17.000000), (23.000000, 81.000000, 14.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((23.000000, 81.000000, 14.000000), (50.000000, 85.000000, 0.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((36.000000, 87.000000, 8.500000),),
((22.500000, 85.000000, 15.500000),),
((36.500000, 83.000000, 7.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((23.000000, 87.000000, 47.000000), (29.000000, 88.000000, 52.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((29.000000, 88.000000, 52.000000), (29.000000, 73.000000, 43.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((29.000000, 73.000000, 43.000000), (23.000000, 87.000000, 47.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((26.000000, 87.500000, 49.500000),),
((29.000000, 80.500000, 47.500000),),
((26.000000, 80.000000, 45.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((23.000000, 87.000000, 47.000000), (24.000000, 100.000000, 48.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 100.000000, 48.000000), (29.000000, 88.000000, 52.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((29.000000, 88.000000, 52.000000), (23.000000, 87.000000, 47.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((23.500000, 93.500000, 47.500000),),
((26.500000, 94.000000, 50.000000),),
((26.000000, 87.500000, 49.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((29.000000, 73.000000, 43.000000), (22.000000, 76.000000, 27.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((22.000000, 76.000000, 27.000000), (12.000000, 86.000000, 34.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((12.000000, 86.000000, 34.000000), (29.000000, 73.000000, 43.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((25.500000, 74.500000, 35.000000),),
((17.000000, 81.000000, 30.500000),),
((20.500000, 79.500000, 38.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((23.000000, 87.000000, 47.000000), (29.000000, 73.000000, 43.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((29.000000, 73.000000, 43.000000), (12.000000, 86.000000, 34.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((12.000000, 86.000000, 34.000000), (23.000000, 87.000000, 47.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((26.000000, 80.000000, 45.000000),),
((20.500000, 79.500000, 38.500000),),
((17.500000, 86.500000, 40.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((27.000000, 71.000000, 25.000000), (22.000000, 76.000000, 27.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((22.000000, 76.000000, 27.000000), (29.000000, 73.000000, 43.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((29.000000, 73.000000, 43.000000), (27.000000, 71.000000, 25.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((24.500000, 73.500000, 26.000000),),
((25.500000, 74.500000, 35.000000),),
((28.000000, 72.000000, 34.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((22.000000, 76.000000, 27.000000), (27.000000, 71.000000, 25.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((27.000000, 71.000000, 25.000000), (23.000000, 81.000000, 14.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((23.000000, 81.000000, 14.000000), (22.000000, 76.000000, 27.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((24.500000, 73.500000, 26.000000),),
((25.000000, 76.000000, 19.500000),),
((22.500000, 78.500000, 20.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((24.000000, 100.000000, 48.000000), (23.000000, 87.000000, 47.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((23.000000, 87.000000, 47.000000), (12.000000, 86.000000, 34.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((12.000000, 86.000000, 34.000000), (24.000000, 100.000000, 48.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((23.500000, 93.500000, 47.500000),),
((17.500000, 86.500000, 40.500000),),
((18.000000, 93.000000, 41.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((22.000000, 76.000000, 27.000000), (19.000000, 83.500000, 20.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((19.000000, 83.500000, 20.000000), (12.000000, 86.000000, 34.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((12.000000, 86.000000, 34.000000), (22.000000, 76.000000, 27.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((20.500000, 79.750000, 23.500000),),
((15.500000, 84.750000, 27.000000),),
((17.000000, 81.000000, 30.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((19.000000, 83.500000, 20.000000), (22.000000, 76.000000, 27.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((22.000000, 76.000000, 27.000000), (23.000000, 81.000000, 14.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((23.000000, 81.000000, 14.000000), (19.000000, 83.500000, 20.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((20.500000, 79.750000, 23.500000),),
((22.500000, 78.500000, 20.500000),),
((21.000000, 82.250000, 17.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((22.000000, 89.000000, 17.000000), (19.000000, 83.500000, 20.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((19.000000, 83.500000, 20.000000), (23.000000, 81.000000, 14.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((23.000000, 81.000000, 14.000000), (22.000000, 89.000000, 17.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((20.500000, 86.250000, 18.500000),),
((21.000000, 82.250000, 17.000000),),
((22.500000, 85.000000, 15.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((21.500000, 100.000000, 23.000000), (17.000000, 100.000000, 30.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((17.000000, 100.000000, 30.000000), (12.000000, 86.000000, 34.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((12.000000, 86.000000, 34.000000), (21.500000, 100.000000, 23.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((19.250000, 100.000000, 26.500000),),
((14.500000, 93.000000, 32.000000),),
((16.750000, 93.000000, 28.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((17.000000, 100.000000, 30.000000), (24.000000, 100.000000, 48.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 100.000000, 48.000000), (12.000000, 86.000000, 34.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((12.000000, 86.000000, 34.000000), (17.000000, 100.000000, 30.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((20.500000, 100.000000, 39.000000),),
((18.000000, 93.000000, 41.000000),),
((14.500000, 93.000000, 32.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((19.000000, 83.500000, 20.000000), (21.500000, 100.000000, 23.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((21.500000, 100.000000, 23.000000), (12.000000, 86.000000, 34.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((12.000000, 86.000000, 34.000000), (19.000000, 83.500000, 20.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((20.250000, 91.750000, 21.500000),),
((16.750000, 93.000000, 28.500000),),
((15.500000, 84.750000, 27.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((19.000000, 83.500000, 20.000000), (22.000000, 89.000000, 17.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((22.000000, 89.000000, 17.000000), (21.500000, 100.000000, 23.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((21.500000, 100.000000, 23.000000), (19.000000, 83.500000, 20.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((20.500000, 86.250000, 18.500000),),
((21.750000, 94.500000, 20.000000),),
((20.250000, 91.750000, 21.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((8.000000, 59.000000, 6.000000), (7.000000, 52.000000, 11.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((7.000000, 52.000000, 11.000000), (13.000000, 62.000000, 15.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((13.000000, 62.000000, 15.000000), (8.000000, 59.000000, 6.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((7.500000, 55.500000, 8.500000),),
((10.000000, 57.000000, 13.000000),),
((10.500000, 60.500000, 10.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((8.000000, 59.000000, 25.000000), (6.000000, 69.000000, 24.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((6.000000, 69.000000, 24.000000), (13.000000, 62.000000, 15.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((13.000000, 62.000000, 15.000000), (8.000000, 59.000000, 25.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((7.000000, 64.000000, 24.500000),),
((9.500000, 65.500000, 19.500000),),
((10.500000, 60.500000, 20.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((6.000000, 68.000000, 7.000000), (8.000000, 59.000000, 6.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((8.000000, 59.000000, 6.000000), (13.000000, 62.000000, 15.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((13.000000, 62.000000, 15.000000), (6.000000, 68.000000, 7.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((7.000000, 63.500000, 6.500000),),
((10.500000, 60.500000, 10.500000),),
((9.500000, 65.000000, 11.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((6.000000, 69.000000, 24.000000), (6.000000, 72.000000, 14.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((6.000000, 72.000000, 14.000000), (13.000000, 62.000000, 15.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((13.000000, 62.000000, 15.000000), (6.000000, 69.000000, 24.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((6.000000, 70.500000, 19.000000),),
((9.500000, 67.000000, 14.500000),),
((9.500000, 65.500000, 19.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((4.000000, 52.000000, 22.000000), (8.000000, 59.000000, 25.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((8.000000, 59.000000, 25.000000), (13.000000, 62.000000, 15.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((13.000000, 62.000000, 15.000000), (4.000000, 52.000000, 22.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((6.000000, 55.500000, 23.500000),),
((10.500000, 60.500000, 20.000000),),
((8.500000, 57.000000, 18.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((7.000000, 52.000000, 11.000000), (4.000000, 52.000000, 22.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((4.000000, 52.000000, 22.000000), (13.000000, 62.000000, 15.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((13.000000, 62.000000, 15.000000), (7.000000, 52.000000, 11.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((5.500000, 52.000000, 16.500000),),
((8.500000, 57.000000, 18.500000),),
((10.000000, 57.000000, 13.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((6.000000, 72.000000, 14.000000), (6.000000, 68.000000, 7.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((6.000000, 68.000000, 7.000000), (13.000000, 62.000000, 15.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((13.000000, 62.000000, 15.000000), (6.000000, 72.000000, 14.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((6.000000, 70.000000, 10.500000),),
((9.500000, 65.000000, 11.000000),),
((9.500000, 67.000000, 14.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 50.000000, 10.000000), (0.000000, 50.000000, 22.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 50.000000, 22.000000), (4.000000, 52.000000, 22.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((4.000000, 52.000000, 22.000000), (0.000000, 50.000000, 10.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((0.000000, 50.000000, 16.000000),),
((2.000000, 51.000000, 22.000000),),
((2.000000, 51.000000, 16.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((5.000000, 59.000000, 26.000000), (6.000000, 69.000000, 24.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((6.000000, 69.000000, 24.000000), (8.000000, 59.000000, 25.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((8.000000, 59.000000, 25.000000), (5.000000, 59.000000, 26.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((5.500000, 64.000000, 25.000000),),
((7.000000, 64.000000, 24.500000),),
((6.500000, 59.000000, 25.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 50.000000, 10.000000), (7.000000, 52.000000, 11.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((7.000000, 52.000000, 11.000000), (0.000000, 58.000000, 4.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 58.000000, 4.000000), (0.000000, 50.000000, 10.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((3.500000, 51.000000, 10.500000),),
((3.500000, 55.000000, 7.500000),),
((0.000000, 54.000000, 7.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((5.000000, 59.000000, 26.000000), (8.000000, 59.000000, 25.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((8.000000, 59.000000, 25.000000), (4.000000, 52.000000, 22.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((4.000000, 52.000000, 22.000000), (5.000000, 59.000000, 26.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((6.500000, 59.000000, 25.500000),),
((6.000000, 55.500000, 23.500000),),
((4.500000, 55.500000, 24.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((7.000000, 52.000000, 11.000000), (8.000000, 59.000000, 6.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((8.000000, 59.000000, 6.000000), (0.000000, 58.000000, 4.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 58.000000, 4.000000), (7.000000, 52.000000, 11.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((7.500000, 55.500000, 8.500000),),
((4.000000, 58.500000, 5.000000),),
((3.500000, 55.000000, 7.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((7.000000, 52.000000, 11.000000), (0.000000, 50.000000, 10.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 50.000000, 10.000000), (4.000000, 52.000000, 22.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((4.000000, 52.000000, 22.000000), (7.000000, 52.000000, 11.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((3.500000, 51.000000, 10.500000),),
((2.000000, 51.000000, 16.000000),),
((5.500000, 52.000000, 16.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 50.000000, 22.000000), (5.000000, 59.000000, 26.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((5.000000, 59.000000, 26.000000), (4.000000, 52.000000, 22.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((4.000000, 52.000000, 22.000000), (0.000000, 50.000000, 22.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((2.500000, 54.500000, 24.000000),),
((4.500000, 55.500000, 24.000000),),
((2.000000, 51.000000, 22.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((6.000000, 69.000000, 24.000000), (5.000000, 59.000000, 26.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((5.000000, 59.000000, 26.000000), (0.000000, 66.000000, 26.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 66.000000, 26.000000), (6.000000, 69.000000, 24.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((5.500000, 64.000000, 25.000000),),
((2.500000, 62.500000, 26.000000),),
((3.000000, 67.500000, 25.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((8.000000, 59.000000, 6.000000), (6.000000, 68.000000, 7.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((6.000000, 68.000000, 7.000000), (0.000000, 58.000000, 4.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 58.000000, 4.000000), (8.000000, 59.000000, 6.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((7.000000, 63.500000, 6.500000),),
((3.000000, 63.000000, 5.500000),),
((4.000000, 58.500000, 5.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((6.000000, 68.000000, 7.000000), (0.000000, 68.000000, 6.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 68.000000, 6.000000), (0.000000, 58.000000, 4.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 58.000000, 4.000000), (6.000000, 68.000000, 7.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((3.000000, 68.000000, 6.500000),),
((0.000000, 63.000000, 5.000000),),
((3.000000, 63.000000, 5.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((6.000000, 69.000000, 24.000000), (0.000000, 72.000000, 16.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 72.000000, 16.000000), (6.000000, 72.000000, 14.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((6.000000, 72.000000, 14.000000), (6.000000, 69.000000, 24.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((3.000000, 70.500000, 20.000000),),
((3.000000, 72.000000, 15.000000),),
((6.000000, 70.500000, 19.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 68.000000, 6.000000), (6.000000, 68.000000, 7.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((6.000000, 68.000000, 7.000000), (6.000000, 72.000000, 14.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((6.000000, 72.000000, 14.000000), (0.000000, 68.000000, 6.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((3.000000, 68.000000, 6.500000),),
((6.000000, 70.000000, 10.500000),),
((3.000000, 70.000000, 10.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 72.000000, 16.000000), (0.000000, 68.000000, 6.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 68.000000, 6.000000), (6.000000, 72.000000, 14.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((6.000000, 72.000000, 14.000000), (0.000000, 72.000000, 16.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((0.000000, 70.000000, 11.000000),),
((3.000000, 70.000000, 10.000000),),
((3.000000, 72.000000, 15.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 72.000000, 16.000000), (6.000000, 69.000000, 24.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((6.000000, 69.000000, 24.000000), (0.000000, 66.000000, 26.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 66.000000, 26.000000), (0.000000, 72.000000, 16.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((3.000000, 70.500000, 20.000000),),
((3.000000, 67.500000, 25.000000),),
((0.000000, 69.000000, 21.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((5.000000, 59.000000, 26.000000), (0.000000, 50.000000, 22.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 50.000000, 22.000000), (0.000000, 66.000000, 26.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 66.000000, 26.000000), (5.000000, 59.000000, 26.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((2.500000, 54.500000, 24.000000),),
((0.000000, 58.000000, 24.000000),),
((2.500000, 62.500000, 26.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 50.000000, 10.000000), (0.000000, 50.000000, 22.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 50.000000, 22.000000), (0.000000, 66.000000, 26.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 66.000000, 26.000000), (0.000000, 72.000000, 16.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 72.000000, 16.000000), (0.000000, 68.000000, 6.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 68.000000, 6.000000), (0.000000, 58.000000, 4.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 58.000000, 4.000000), (0.000000, 50.000000, 10.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((0.000000, 50.000000, 16.000000),),
((0.000000, 58.000000, 24.000000),),
((0.000000, 69.000000, 21.000000),),
((0.000000, 70.000000, 11.000000),),
((0.000000, 63.000000, 5.000000),),
((0.000000, 54.000000, 7.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((85.000000, 0.000000, 42.000000), (80.000000, 16.000000, 38.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((80.000000, 16.000000, 38.000000), (92.000000, 0.000000, 24.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((92.000000, 0.000000, 24.000000), (85.000000, 0.000000, 42.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((82.500000, 8.000000, 40.000000),),
((86.000000, 8.000000, 31.000000),),
((88.500000, 0.000000, 33.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((92.000000, 0.000000, 24.000000), (80.000000, 16.000000, 38.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((80.000000, 16.000000, 38.000000), (93.000000, 5.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((93.000000, 5.000000, 21.000000), (92.000000, 0.000000, 24.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((86.000000, 8.000000, 31.000000),),
((86.500000, 10.500000, 29.500000),),
((92.500000, 2.500000, 22.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((82.000000, 9.000000, 11.000000), (79.000000, 4.000000, 9.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((79.000000, 4.000000, 9.000000), (79.000000, 0.000000, 10.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((79.000000, 0.000000, 10.000000), (82.000000, 9.000000, 11.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((80.500000, 6.500000, 10.000000),),
((79.000000, 2.000000, 9.500000),),
((80.500000, 4.500000, 10.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((77.000000, 12.000000, 7.000000), (82.000000, 9.000000, 11.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((82.000000, 9.000000, 11.000000), (77.000000, 20.000000, 19.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((77.000000, 20.000000, 19.000000), (77.000000, 12.000000, 7.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((79.500000, 10.500000, 9.000000),),
((79.500000, 14.500000, 15.000000),),
((77.000000, 16.000000, 13.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((80.000000, 16.000000, 38.000000), (77.000000, 20.000000, 19.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((77.000000, 20.000000, 19.000000), (93.000000, 5.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((93.000000, 5.000000, 21.000000), (80.000000, 16.000000, 38.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((78.500000, 18.000000, 28.500000),),
((85.000000, 12.500000, 20.000000),),
((86.500000, 10.500000, 29.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((82.000000, 9.000000, 11.000000), (79.000000, 0.000000, 10.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((79.000000, 0.000000, 10.000000), (93.000000, 5.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((93.000000, 5.000000, 21.000000), (82.000000, 9.000000, 11.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((80.500000, 4.500000, 10.500000),),
((86.000000, 2.500000, 15.500000),),
((87.500000, 7.000000, 16.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((79.000000, 0.000000, 10.000000), (92.000000, 0.000000, 24.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((92.000000, 0.000000, 24.000000), (93.000000, 5.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((93.000000, 5.000000, 21.000000), (79.000000, 0.000000, 10.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((85.500000, 0.000000, 17.000000),),
((92.500000, 2.500000, 22.500000),),
((86.000000, 2.500000, 15.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((77.000000, 20.000000, 19.000000), (82.000000, 9.000000, 11.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((82.000000, 9.000000, 11.000000), (93.000000, 5.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((93.000000, 5.000000, 21.000000), (77.000000, 20.000000, 19.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((79.500000, 14.500000, 15.000000),),
((87.500000, 7.000000, 16.000000),),
((85.000000, 12.500000, 20.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((77.000000, 12.000000, 7.000000), (79.000000, 4.000000, 9.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((79.000000, 4.000000, 9.000000), (82.000000, 9.000000, 11.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((82.000000, 9.000000, 11.000000), (77.000000, 12.000000, 7.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((78.000000, 8.000000, 8.000000),),
((80.500000, 6.500000, 10.000000),),
((79.500000, 10.500000, 9.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((79.000000, 0.000000, 10.000000), (79.000000, 4.000000, 9.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((79.000000, 4.000000, 9.000000), (67.000000, 0.000000, 5.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((67.000000, 0.000000, 5.000000), (79.000000, 0.000000, 10.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((79.000000, 2.000000, 9.500000),),
((73.000000, 2.000000, 7.000000),),
((73.000000, 0.000000, 7.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((80.000000, 16.000000, 38.000000), (85.000000, 0.000000, 42.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((85.000000, 0.000000, 42.000000), (56.000000, 0.000000, 53.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((56.000000, 0.000000, 53.000000), (80.000000, 16.000000, 38.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((82.500000, 8.000000, 40.000000),),
((70.500000, 0.000000, 47.500000),),
((68.000000, 8.000000, 45.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((50.000000, 16.000000, 47.000000), (80.000000, 16.000000, 38.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((80.000000, 16.000000, 38.000000), (56.000000, 0.000000, 53.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((56.000000, 0.000000, 53.000000), (50.000000, 16.000000, 47.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((65.000000, 16.000000, 42.500000),),
((68.000000, 8.000000, 45.500000),),
((53.000000, 8.000000, 50.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((67.000000, 0.000000, 5.000000), (79.000000, 4.000000, 9.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((79.000000, 4.000000, 9.000000), (65.000000, 5.000000, 7.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((65.000000, 5.000000, 7.000000), (67.000000, 0.000000, 5.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((73.000000, 2.000000, 7.000000),),
((72.000000, 4.500000, 8.000000),),
((66.000000, 2.500000, 6.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((79.000000, 4.000000, 9.000000), (77.000000, 12.000000, 7.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((77.000000, 12.000000, 7.000000), (65.000000, 5.000000, 7.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((65.000000, 5.000000, 7.000000), (79.000000, 4.000000, 9.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((78.000000, 8.000000, 8.000000),),
((71.000000, 8.500000, 7.000000),),
((72.000000, 4.500000, 8.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((77.000000, 20.000000, 19.000000), (80.000000, 16.000000, 38.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((80.000000, 16.000000, 38.000000), (46.000000, 22.000000, 27.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((46.000000, 22.000000, 27.000000), (77.000000, 20.000000, 19.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((78.500000, 18.000000, 28.500000),),
((63.000000, 19.000000, 32.500000),),
((61.500000, 21.000000, 23.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((46.000000, 22.000000, 27.000000), (80.000000, 16.000000, 38.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((80.000000, 16.000000, 38.000000), (50.000000, 16.000000, 47.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((50.000000, 16.000000, 47.000000), (46.000000, 22.000000, 27.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((63.000000, 19.000000, 32.500000),),
((65.000000, 16.000000, 42.500000),),
((48.000000, 19.000000, 37.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((77.000000, 20.000000, 19.000000), (46.000000, 22.000000, 27.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((46.000000, 22.000000, 27.000000), (47.000000, 22.000000, 23.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((47.000000, 22.000000, 23.000000), (77.000000, 20.000000, 19.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((61.500000, 21.000000, 23.000000),),
((46.500000, 22.000000, 25.000000),),
((62.000000, 21.000000, 21.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((77.000000, 12.000000, 7.000000), (77.000000, 20.000000, 19.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((77.000000, 20.000000, 19.000000), (70.000000, 14.000000, 10.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((70.000000, 14.000000, 10.000000), (77.000000, 12.000000, 7.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((77.000000, 16.000000, 13.000000),),
((73.500000, 17.000000, 14.500000),),
((73.500000, 13.000000, 8.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((17.000000, 0.000000, 33.000000), (20.000000, 0.000000, 25.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((20.000000, 0.000000, 25.000000), (53.000000, 0.000000, 9.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((53.000000, 0.000000, 9.000000), (67.000000, 0.000000, 5.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((67.000000, 0.000000, 5.000000), (79.000000, 0.000000, 10.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((79.000000, 0.000000, 10.000000), (92.000000, 0.000000, 24.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((92.000000, 0.000000, 24.000000), (85.000000, 0.000000, 42.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((85.000000, 0.000000, 42.000000), (56.000000, 0.000000, 53.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((56.000000, 0.000000, 53.000000), (24.000000, 0.000000, 47.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 0.000000, 47.000000), (17.000000, 0.000000, 33.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((18.500000, 0.000000, 29.000000),),
((36.500000, 0.000000, 17.000000),),
((60.000000, 0.000000, 7.000000),),
((73.000000, 0.000000, 7.500000),),
((85.500000, 0.000000, 17.000000),),
((88.500000, 0.000000, 33.000000),),
((70.500000, 0.000000, 47.500000),),
((40.000000, 0.000000, 50.000000),),
((20.500000, 0.000000, 40.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((70.000000, 14.000000, 10.000000), (77.000000, 20.000000, 19.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((77.000000, 20.000000, 19.000000), (47.000000, 22.000000, 23.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((47.000000, 22.000000, 23.000000), (70.000000, 14.000000, 10.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((73.500000, 17.000000, 14.500000),),
((62.000000, 21.000000, 21.000000),),
((58.500000, 18.000000, 16.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((24.000000, 0.000000, 47.000000), (23.000000, 4.000000, 46.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((23.000000, 4.000000, 46.000000), (46.000000, 14.000000, 47.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((46.000000, 14.000000, 47.000000), (24.000000, 0.000000, 47.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((23.500000, 2.000000, 46.500000),),
((34.500000, 9.000000, 46.500000),),
((35.000000, 7.000000, 47.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((46.000000, 14.000000, 47.000000), (50.000000, 16.000000, 47.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((50.000000, 16.000000, 47.000000), (56.000000, 0.000000, 53.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((56.000000, 0.000000, 53.000000), (46.000000, 14.000000, 47.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((48.000000, 15.000000, 47.000000),),
((53.000000, 8.000000, 50.000000),),
((51.000000, 7.000000, 50.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((24.000000, 0.000000, 47.000000), (46.000000, 14.000000, 47.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((46.000000, 14.000000, 47.000000), (56.000000, 0.000000, 53.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((56.000000, 0.000000, 53.000000), (24.000000, 0.000000, 47.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((35.000000, 7.000000, 47.000000),),
((51.000000, 7.000000, 50.000000),),
((40.000000, 0.000000, 50.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((65.000000, 5.000000, 7.000000), (77.000000, 12.000000, 7.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((77.000000, 12.000000, 7.000000), (70.000000, 14.000000, 10.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((70.000000, 14.000000, 10.000000), (65.000000, 5.000000, 7.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((71.000000, 8.500000, 7.000000),),
((73.500000, 13.000000, 8.500000),),
((67.500000, 9.500000, 8.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((67.000000, 0.000000, 5.000000), (65.000000, 5.000000, 7.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((65.000000, 5.000000, 7.000000), (53.000000, 0.000000, 9.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((53.000000, 0.000000, 9.000000), (67.000000, 0.000000, 5.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((66.000000, 2.500000, 6.000000),),
((59.000000, 2.500000, 8.000000),),
((60.000000, 0.000000, 7.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((65.000000, 5.000000, 7.000000), (70.000000, 14.000000, 10.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((70.000000, 14.000000, 10.000000), (47.000000, 22.000000, 23.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((47.000000, 22.000000, 23.000000), (65.000000, 5.000000, 7.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((67.500000, 9.500000, 8.500000),),
((58.500000, 18.000000, 16.500000),),
((56.000000, 13.500000, 15.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((53.000000, 0.000000, 9.000000), (65.000000, 5.000000, 7.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((65.000000, 5.000000, 7.000000), (47.000000, 22.000000, 23.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((47.000000, 22.000000, 23.000000), (53.000000, 0.000000, 9.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((59.000000, 2.500000, 8.000000),),
((56.000000, 13.500000, 15.000000),),
((50.000000, 11.000000, 16.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((43.000000, 19.000000, 23.000000), (53.000000, 0.000000, 9.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((53.000000, 0.000000, 9.000000), (47.000000, 22.000000, 23.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((47.000000, 22.000000, 23.000000), (43.000000, 19.000000, 23.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((48.000000, 9.500000, 16.000000),),
((50.000000, 11.000000, 16.000000),),
((45.000000, 20.500000, 23.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((22.000000, 9.000000, 32.000000), (20.000000, 9.000000, 29.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((20.000000, 9.000000, 29.000000), (43.000000, 19.000000, 23.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((43.000000, 19.000000, 23.000000), (22.000000, 9.000000, 32.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((21.000000, 9.000000, 30.500000),),
((31.500000, 14.000000, 26.000000),),
((32.500000, 14.000000, 27.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((43.000000, 19.000000, 23.000000), (20.000000, 9.000000, 29.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((20.000000, 9.000000, 29.000000), (24.000000, 4.000000, 26.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 4.000000, 26.000000), (43.000000, 19.000000, 23.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((31.500000, 14.000000, 26.000000),),
((22.000000, 6.500000, 27.500000),),
((33.500000, 11.500000, 24.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((23.000000, 4.000000, 46.000000), (22.000000, 9.000000, 32.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((22.000000, 9.000000, 32.000000), (46.000000, 14.000000, 47.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((46.000000, 14.000000, 47.000000), (23.000000, 4.000000, 46.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((22.500000, 6.500000, 39.000000),),
((34.000000, 11.500000, 39.500000),),
((34.500000, 9.000000, 46.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((22.000000, 9.000000, 32.000000), (46.000000, 22.000000, 27.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((46.000000, 22.000000, 27.000000), (46.000000, 14.000000, 47.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((46.000000, 14.000000, 47.000000), (22.000000, 9.000000, 32.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((34.000000, 15.500000, 29.500000),),
((46.000000, 18.000000, 37.000000),),
((34.000000, 11.500000, 39.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((43.000000, 19.000000, 23.000000), (20.000000, 0.000000, 25.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((20.000000, 0.000000, 25.000000), (53.000000, 0.000000, 9.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((53.000000, 0.000000, 9.000000), (43.000000, 19.000000, 23.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((31.500000, 9.500000, 24.000000),),
((36.500000, 0.000000, 17.000000),),
((48.000000, 9.500000, 16.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((46.000000, 22.000000, 27.000000), (50.000000, 16.000000, 47.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((50.000000, 16.000000, 47.000000), (46.000000, 14.000000, 47.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((46.000000, 14.000000, 47.000000), (46.000000, 22.000000, 27.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((48.000000, 19.000000, 37.000000),),
((48.000000, 15.000000, 47.000000),),
((46.000000, 18.000000, 37.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((46.000000, 22.000000, 27.000000), (22.000000, 9.000000, 32.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((22.000000, 9.000000, 32.000000), (43.000000, 19.000000, 23.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((43.000000, 19.000000, 23.000000), (46.000000, 22.000000, 27.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((34.000000, 15.500000, 29.500000),),
((32.500000, 14.000000, 27.500000),),
((44.500000, 20.500000, 25.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((46.000000, 22.000000, 27.000000), (43.000000, 19.000000, 23.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((43.000000, 19.000000, 23.000000), (47.000000, 22.000000, 23.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((47.000000, 22.000000, 23.000000), (46.000000, 22.000000, 27.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((44.500000, 20.500000, 25.000000),),
((45.000000, 20.500000, 23.000000),),
((46.500000, 22.000000, 25.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((20.000000, 0.000000, 25.000000), (43.000000, 19.000000, 23.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((43.000000, 19.000000, 23.000000), (24.000000, 4.000000, 26.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 4.000000, 26.000000), (20.000000, 0.000000, 25.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((31.500000, 9.500000, 24.000000),),
((33.500000, 11.500000, 24.500000),),
((22.000000, 2.000000, 25.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((17.000000, 0.000000, 33.000000), (20.000000, 0.000000, 25.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((20.000000, 0.000000, 25.000000), (24.000000, 4.000000, 26.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 4.000000, 26.000000), (17.000000, 0.000000, 33.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((18.500000, 0.000000, 29.000000),),
((22.000000, 2.000000, 25.500000),),
((20.500000, 2.000000, 29.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((20.000000, 9.000000, 29.000000), (17.000000, 0.000000, 33.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((17.000000, 0.000000, 33.000000), (24.000000, 4.000000, 26.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 4.000000, 26.000000), (20.000000, 9.000000, 29.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((18.500000, 4.500000, 31.000000),),
((20.500000, 2.000000, 29.500000),),
((22.000000, 6.500000, 27.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((20.000000, 9.000000, 29.000000), (22.000000, 9.000000, 32.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((22.000000, 9.000000, 32.000000), (17.000000, 0.000000, 33.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((17.000000, 0.000000, 33.000000), (20.000000, 9.000000, 29.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((21.000000, 9.000000, 30.500000),),
((19.500000, 4.500000, 32.500000),),
((18.500000, 4.500000, 31.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((22.000000, 9.000000, 32.000000), (23.000000, 4.000000, 46.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((23.000000, 4.000000, 46.000000), (17.000000, 0.000000, 33.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((17.000000, 0.000000, 33.000000), (22.000000, 9.000000, 32.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((22.500000, 6.500000, 39.000000),),
((20.000000, 2.000000, 39.500000),),
((19.500000, 4.500000, 32.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((23.000000, 4.000000, 46.000000), (24.000000, 0.000000, 47.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 0.000000, 47.000000), (17.000000, 0.000000, 33.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((17.000000, 0.000000, 33.000000), (23.000000, 4.000000, 46.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((23.500000, 2.000000, 46.500000),),
((20.500000, 0.000000, 40.000000),),
((20.000000, 2.000000, 39.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((100.000000, 45.000000, 49.000000), (100.000000, 49.000000, 31.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 49.000000, 31.000000), (100.000000, 40.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 40.000000, 21.000000), (100.000000, 30.000000, 22.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 30.000000, 22.000000), (100.000000, 14.000000, 28.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 14.000000, 28.000000), (100.000000, 15.000000, 41.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 15.000000, 41.000000), (100.000000, 27.000000, 51.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 27.000000, 51.000000), (100.000000, 45.000000, 49.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((100.000000, 47.000000, 40.000000),),
((100.000000, 44.500000, 26.000000),),
((100.000000, 35.000000, 21.500000),),
((100.000000, 22.000000, 25.000000),),
((100.000000, 14.500000, 34.500000),),
((100.000000, 21.000000, 46.000000),),
((100.000000, 36.000000, 50.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((96.000000, 21.000000, 20.000000), (100.000000, 14.000000, 28.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 14.000000, 28.000000), (100.000000, 30.000000, 22.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 30.000000, 22.000000), (96.000000, 21.000000, 20.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((98.000000, 17.500000, 24.000000),),
((100.000000, 22.000000, 25.000000),),
((98.000000, 25.500000, 21.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((100.000000, 49.000000, 31.000000), (100.000000, 45.000000, 49.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 45.000000, 49.000000), (97.000000, 49.000000, 36.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((97.000000, 49.000000, 36.000000), (100.000000, 49.000000, 31.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((100.000000, 47.000000, 40.000000),),
((98.500000, 47.000000, 42.500000),),
((98.500000, 49.000000, 33.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((91.000000, 33.000000, 21.000000), (96.000000, 21.000000, 20.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((96.000000, 21.000000, 20.000000), (100.000000, 30.000000, 22.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 30.000000, 22.000000), (91.000000, 33.000000, 21.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((93.500000, 27.000000, 20.500000),),
((98.000000, 25.500000, 21.000000),),
((95.500000, 31.500000, 21.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((100.000000, 40.000000, 21.000000), (91.000000, 33.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((91.000000, 33.000000, 21.000000), (100.000000, 30.000000, 22.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 30.000000, 22.000000), (100.000000, 40.000000, 21.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((95.500000, 36.500000, 21.000000),),
((95.500000, 31.500000, 21.500000),),
((100.000000, 35.000000, 21.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((100.000000, 15.000000, 41.000000), (89.000000, 21.000000, 45.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((89.000000, 21.000000, 45.000000), (100.000000, 27.000000, 51.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 27.000000, 51.000000), (100.000000, 15.000000, 41.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((94.500000, 18.000000, 43.000000),),
((94.500000, 24.000000, 48.000000),),
((100.000000, 21.000000, 46.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((100.000000, 15.000000, 41.000000), (100.000000, 14.000000, 28.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 14.000000, 28.000000), (91.000000, 16.000000, 32.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((91.000000, 16.000000, 32.000000), (100.000000, 15.000000, 41.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((100.000000, 14.500000, 34.500000),),
((95.500000, 15.000000, 30.000000),),
((95.500000, 15.500000, 36.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((96.000000, 21.000000, 20.000000), (85.000000, 19.000000, 30.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((85.000000, 19.000000, 30.000000), (91.000000, 16.000000, 32.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((91.000000, 16.000000, 32.000000), (96.000000, 21.000000, 20.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((90.500000, 20.000000, 25.000000),),
((88.000000, 17.500000, 31.000000),),
((93.500000, 18.500000, 26.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((89.000000, 21.000000, 45.000000), (100.000000, 15.000000, 41.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 15.000000, 41.000000), (91.000000, 16.000000, 32.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((91.000000, 16.000000, 32.000000), (89.000000, 21.000000, 45.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((94.500000, 18.000000, 43.000000),),
((95.500000, 15.500000, 36.500000),),
((90.000000, 18.500000, 38.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((100.000000, 14.000000, 28.000000), (96.000000, 21.000000, 20.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((96.000000, 21.000000, 20.000000), (91.000000, 16.000000, 32.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((91.000000, 16.000000, 32.000000), (100.000000, 14.000000, 28.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((98.000000, 17.500000, 24.000000),),
((93.500000, 18.500000, 26.000000),),
((95.500000, 15.000000, 30.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((85.000000, 19.000000, 30.000000), (89.000000, 21.000000, 45.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((89.000000, 21.000000, 45.000000), (91.000000, 16.000000, 32.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((91.000000, 16.000000, 32.000000), (85.000000, 19.000000, 30.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((87.000000, 20.000000, 37.500000),),
((90.000000, 18.500000, 38.500000),),
((88.000000, 17.500000, 31.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((100.000000, 40.000000, 21.000000), (85.000000, 36.000000, 30.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((85.000000, 36.000000, 30.000000), (91.000000, 33.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((91.000000, 33.000000, 21.000000), (100.000000, 40.000000, 21.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((92.500000, 38.000000, 25.500000),),
((88.000000, 34.500000, 25.500000),),
((95.500000, 36.500000, 21.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((100.000000, 45.000000, 49.000000), (100.000000, 27.000000, 51.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 27.000000, 51.000000), (84.000000, 31.000000, 41.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((84.000000, 31.000000, 41.000000), (100.000000, 45.000000, 49.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((100.000000, 36.000000, 50.000000),),
((92.000000, 29.000000, 46.000000),),
((92.000000, 38.000000, 45.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((100.000000, 27.000000, 51.000000), (89.000000, 21.000000, 45.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((89.000000, 21.000000, 45.000000), (84.000000, 31.000000, 41.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((84.000000, 31.000000, 41.000000), (100.000000, 27.000000, 51.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((94.500000, 24.000000, 48.000000),),
((86.500000, 26.000000, 43.000000),),
((92.000000, 29.000000, 46.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((85.000000, 36.000000, 30.000000), (100.000000, 40.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 40.000000, 21.000000), (100.000000, 49.000000, 31.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 49.000000, 31.000000), (85.000000, 36.000000, 30.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((92.500000, 38.000000, 25.500000),),
((100.000000, 44.500000, 26.000000),),
((92.500000, 42.500000, 30.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((85.000000, 36.000000, 30.000000), (100.000000, 49.000000, 31.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 49.000000, 31.000000), (97.000000, 49.000000, 36.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((97.000000, 49.000000, 36.000000), (85.000000, 36.000000, 30.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((92.500000, 42.500000, 30.500000),),
((98.500000, 49.000000, 33.500000),),
((91.000000, 42.500000, 33.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((85.000000, 19.000000, 30.000000), (96.000000, 21.000000, 20.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((96.000000, 21.000000, 20.000000), (91.000000, 33.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((91.000000, 33.000000, 21.000000), (85.000000, 19.000000, 30.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((90.500000, 20.000000, 25.000000),),
((93.500000, 27.000000, 20.500000),),
((88.000000, 26.000000, 25.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((97.000000, 49.000000, 36.000000), (100.000000, 45.000000, 49.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 45.000000, 49.000000), (84.000000, 31.000000, 41.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((84.000000, 31.000000, 41.000000), (97.000000, 49.000000, 36.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((98.500000, 47.000000, 42.500000),),
((92.000000, 38.000000, 45.000000),),
((90.500000, 40.000000, 38.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((85.000000, 36.000000, 30.000000), (97.000000, 49.000000, 36.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((97.000000, 49.000000, 36.000000), (84.000000, 31.000000, 41.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((84.000000, 31.000000, 41.000000), (85.000000, 36.000000, 30.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((91.000000, 42.500000, 33.000000),),
((90.500000, 40.000000, 38.500000),),
((84.500000, 33.500000, 35.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((85.000000, 36.000000, 30.000000), (85.000000, 19.000000, 30.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((85.000000, 19.000000, 30.000000), (91.000000, 33.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((91.000000, 33.000000, 21.000000), (85.000000, 36.000000, 30.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((85.000000, 27.500000, 30.000000),),
((88.000000, 26.000000, 25.500000),),
((88.000000, 34.500000, 25.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((89.000000, 21.000000, 45.000000), (85.000000, 19.000000, 30.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((85.000000, 19.000000, 30.000000), (84.000000, 31.000000, 41.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((84.000000, 31.000000, 41.000000), (89.000000, 21.000000, 45.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((87.000000, 20.000000, 37.500000),),
((84.500000, 25.000000, 35.500000),),
((86.500000, 26.000000, 43.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((85.000000, 19.000000, 30.000000), (85.000000, 36.000000, 30.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((85.000000, 36.000000, 30.000000), (84.000000, 31.000000, 41.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((84.000000, 31.000000, 41.000000), (85.000000, 19.000000, 30.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((85.000000, 27.500000, 30.000000),),
((84.500000, 33.500000, 35.500000),),
((84.500000, 25.000000, 35.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((28.000000, 34.000000, 48.000000), (30.000000, 49.000000, 43.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((30.000000, 49.000000, 43.000000), (30.000000, 36.000000, 34.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((30.000000, 36.000000, 34.000000), (28.000000, 34.000000, 48.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((29.000000, 41.500000, 45.500000),),
((30.000000, 42.500000, 38.500000),),
((29.000000, 35.000000, 41.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((30.000000, 49.000000, 43.000000), (27.000000, 41.000000, 28.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((27.000000, 41.000000, 28.000000), (30.000000, 36.000000, 34.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((30.000000, 36.000000, 34.000000), (30.000000, 49.000000, 43.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((28.500000, 45.000000, 35.500000),),
((28.500000, 38.500000, 31.000000),),
((30.000000, 42.500000, 38.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((27.000000, 41.000000, 28.000000), (30.000000, 49.000000, 43.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((30.000000, 49.000000, 43.000000), (24.000000, 49.000000, 29.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 49.000000, 29.000000), (27.000000, 41.000000, 28.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((28.500000, 45.000000, 35.500000),),
((27.000000, 49.000000, 36.000000),),
((25.500000, 45.000000, 28.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((18.000000, 20.000000, 31.000000), (28.000000, 34.000000, 48.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((28.000000, 34.000000, 48.000000), (30.000000, 36.000000, 34.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((30.000000, 36.000000, 34.000000), (18.000000, 20.000000, 31.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((23.000000, 27.000000, 39.500000),),
((29.000000, 35.000000, 41.000000),),
((24.000000, 28.000000, 32.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((30.000000, 49.000000, 43.000000), (28.000000, 34.000000, 48.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((28.000000, 34.000000, 48.000000), (22.000000, 43.000000, 53.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((22.000000, 43.000000, 53.000000), (30.000000, 49.000000, 43.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((29.000000, 41.500000, 45.500000),),
((25.000000, 38.500000, 50.500000),),
((26.000000, 46.000000, 48.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((14.000000, 20.000000, 47.000000), (28.000000, 34.000000, 48.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((28.000000, 34.000000, 48.000000), (18.000000, 20.000000, 31.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((18.000000, 20.000000, 31.000000), (14.000000, 20.000000, 47.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((21.000000, 27.000000, 47.500000),),
((23.000000, 27.000000, 39.500000),),
((16.000000, 20.000000, 39.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((24.000000, 40.000000, 27.000000), (18.000000, 20.000000, 31.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((18.000000, 20.000000, 31.000000), (30.000000, 36.000000, 34.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((30.000000, 36.000000, 34.000000), (24.000000, 40.000000, 27.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((21.000000, 30.000000, 29.000000),),
((24.000000, 28.000000, 32.500000),),
((27.000000, 38.000000, 30.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((16.000000, 51.500000, 49.500000), (30.000000, 49.000000, 43.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((30.000000, 49.000000, 43.000000), (22.000000, 43.000000, 53.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((22.000000, 43.000000, 53.000000), (16.000000, 51.500000, 49.500000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((23.000000, 50.250000, 46.250000),),
((26.000000, 46.000000, 48.000000),),
((19.000000, 47.250000, 51.250000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((27.000000, 41.000000, 28.000000), (24.000000, 40.000000, 27.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 40.000000, 27.000000), (30.000000, 36.000000, 34.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((30.000000, 36.000000, 34.000000), (27.000000, 41.000000, 28.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((25.500000, 40.500000, 27.500000),),
((27.000000, 38.000000, 30.500000),),
((28.500000, 38.500000, 31.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((24.000000, 40.000000, 27.000000), (0.000000, 24.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 24.000000, 21.000000), (18.000000, 20.000000, 31.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((18.000000, 20.000000, 31.000000), (24.000000, 40.000000, 27.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((12.000000, 32.000000, 24.000000),),
((9.000000, 22.000000, 26.000000),),
((21.000000, 30.000000, 29.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((24.000000, 40.000000, 27.000000), (24.000000, 49.000000, 29.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 49.000000, 29.000000), (4.000000, 44.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((4.000000, 44.000000, 21.000000), (24.000000, 40.000000, 27.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((24.000000, 44.500000, 28.000000),),
((14.000000, 46.500000, 25.000000),),
((14.000000, 42.000000, 24.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 24.000000, 21.000000), (0.000000, 15.000000, 28.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 15.000000, 28.000000), (18.000000, 20.000000, 31.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((18.000000, 20.000000, 31.000000), (0.000000, 24.000000, 21.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((0.000000, 19.500000, 24.500000),),
((9.000000, 17.500000, 29.500000),),
((9.000000, 22.000000, 26.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 24.000000, 21.000000), (24.000000, 40.000000, 27.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 40.000000, 27.000000), (4.000000, 44.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((4.000000, 44.000000, 21.000000), (0.000000, 24.000000, 21.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((12.000000, 32.000000, 24.000000),),
((14.000000, 42.000000, 24.000000),),
((2.000000, 34.000000, 21.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((22.000000, 43.000000, 53.000000), (28.000000, 34.000000, 48.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((28.000000, 34.000000, 48.000000), (14.000000, 20.000000, 47.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((14.000000, 20.000000, 47.000000), (22.000000, 43.000000, 53.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((25.000000, 38.500000, 50.500000),),
((21.000000, 27.000000, 47.500000),),
((18.000000, 31.500000, 50.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 15.000000, 28.000000), (0.000000, 16.000000, 42.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 16.000000, 42.000000), (18.000000, 20.000000, 31.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((18.000000, 20.000000, 31.000000), (0.000000, 15.000000, 28.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((0.000000, 15.500000, 35.000000),),
((9.000000, 18.000000, 36.500000),),
((9.000000, 17.500000, 29.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 16.000000, 42.000000), (14.000000, 20.000000, 47.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((14.000000, 20.000000, 47.000000), (18.000000, 20.000000, 31.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((18.000000, 20.000000, 31.000000), (0.000000, 16.000000, 42.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((7.000000, 18.000000, 44.500000),),
((16.000000, 20.000000, 39.000000),),
((9.000000, 18.000000, 36.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((24.000000, 40.000000, 27.000000), (27.000000, 41.000000, 28.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((27.000000, 41.000000, 28.000000), (24.000000, 49.000000, 29.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 49.000000, 29.000000), (24.000000, 40.000000, 27.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((25.500000, 40.500000, 27.500000),),
((25.500000, 45.000000, 28.500000),),
((24.000000, 44.500000, 28.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 28.000000, 52.000000), (22.000000, 43.000000, 53.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((22.000000, 43.000000, 53.000000), (14.000000, 20.000000, 47.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((14.000000, 20.000000, 47.000000), (0.000000, 28.000000, 52.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((11.000000, 35.500000, 52.500000),),
((18.000000, 31.500000, 50.000000),),
((7.000000, 24.000000, 49.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((30.000000, 49.000000, 43.000000), (16.000000, 51.500000, 49.500000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((16.000000, 51.500000, 49.500000), (24.000000, 49.000000, 29.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 49.000000, 29.000000), (30.000000, 49.000000, 43.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((23.000000, 50.250000, 46.250000),),
((20.000000, 50.250000, 39.250000),),
((27.000000, 49.000000, 36.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((16.000000, 51.500000, 49.500000), (0.000000, 50.000000, 32.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 50.000000, 32.000000), (24.000000, 49.000000, 29.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 49.000000, 29.000000), (16.000000, 51.500000, 49.500000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((8.000000, 50.750000, 40.750000),),
((12.000000, 49.500000, 30.500000),),
((20.000000, 50.250000, 39.250000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 40.000000, 21.000000), (0.000000, 24.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 24.000000, 21.000000), (4.000000, 44.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((4.000000, 44.000000, 21.000000), (0.000000, 40.000000, 21.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((0.000000, 32.000000, 21.000000),),
((2.000000, 34.000000, 21.000000),),
((2.000000, 42.000000, 21.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((24.000000, 49.000000, 29.000000), (0.000000, 50.000000, 32.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 50.000000, 32.000000), (4.000000, 44.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((4.000000, 44.000000, 21.000000), (24.000000, 49.000000, 29.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((12.000000, 49.500000, 30.500000),),
((2.000000, 47.000000, 26.500000),),
((14.000000, 46.500000, 25.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 16.000000, 42.000000), (0.000000, 28.000000, 52.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 28.000000, 52.000000), (14.000000, 20.000000, 47.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((14.000000, 20.000000, 47.000000), (0.000000, 16.000000, 42.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((0.000000, 22.000000, 47.000000),),
((7.000000, 24.000000, 49.500000),),
((7.000000, 18.000000, 44.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((16.000000, 51.500000, 49.500000), (22.000000, 43.000000, 53.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((22.000000, 43.000000, 53.000000), (0.000000, 45.000000, 49.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 45.000000, 49.000000), (16.000000, 51.500000, 49.500000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((19.000000, 47.250000, 51.250000),),
((11.000000, 44.000000, 51.000000),),
((8.000000, 48.250000, 49.250000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((22.000000, 43.000000, 53.000000), (0.000000, 28.000000, 52.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 28.000000, 52.000000), (0.000000, 45.000000, 49.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 45.000000, 49.000000), (22.000000, 43.000000, 53.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((11.000000, 35.500000, 52.500000),),
((0.000000, 36.500000, 50.500000),),
((11.000000, 44.000000, 51.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 50.000000, 32.000000), (16.000000, 51.500000, 49.500000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((16.000000, 51.500000, 49.500000), (0.000000, 45.000000, 49.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 45.000000, 49.000000), (0.000000, 50.000000, 32.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((8.000000, 50.750000, 40.750000),),
((8.000000, 48.250000, 49.250000),),
((0.000000, 47.500000, 40.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 50.000000, 32.000000), (0.000000, 40.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 40.000000, 21.000000), (4.000000, 44.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((4.000000, 44.000000, 21.000000), (0.000000, 50.000000, 32.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((0.000000, 45.000000, 26.500000),),
((2.000000, 42.000000, 21.000000),),
((2.000000, 47.000000, 26.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 15.000000, 28.000000), (0.000000, 24.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 24.000000, 21.000000), (0.000000, 40.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 40.000000, 21.000000), (0.000000, 50.000000, 32.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 50.000000, 32.000000), (0.000000, 45.000000, 49.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 45.000000, 49.000000), (0.000000, 28.000000, 52.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 28.000000, 52.000000), (0.000000, 16.000000, 42.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 16.000000, 42.000000), (0.000000, 15.000000, 28.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((0.000000, 19.500000, 24.500000),),
((0.000000, 32.000000, 21.000000),),
((0.000000, 45.000000, 26.500000),),
((0.000000, 47.500000, 40.500000),),
((0.000000, 36.500000, 50.500000),),
((0.000000, 22.000000, 47.000000),),
((0.000000, 15.500000, 35.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((71.000000, 54.000000, 29.000000), (76.000000, 47.000000, 29.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((76.000000, 47.000000, 29.000000), (78.000000, 43.000000, 34.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((78.000000, 43.000000, 34.000000), (71.000000, 54.000000, 29.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((73.500000, 50.500000, 29.000000),),
((77.000000, 45.000000, 31.500000),),
((74.500000, 48.500000, 31.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((66.000000, 55.000000, 43.000000), (71.000000, 54.000000, 29.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((71.000000, 54.000000, 29.000000), (78.000000, 43.000000, 34.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((78.000000, 43.000000, 34.000000), (66.000000, 55.000000, 43.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((68.500000, 54.500000, 36.000000),),
((74.500000, 48.500000, 31.500000),),
((72.000000, 49.000000, 38.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((76.000000, 47.000000, 29.000000), (66.000000, 35.000000, 22.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((66.000000, 35.000000, 22.000000), (78.000000, 43.000000, 34.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((78.000000, 43.000000, 34.000000), (76.000000, 47.000000, 29.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((71.000000, 41.000000, 25.500000),),
((72.000000, 39.000000, 28.000000),),
((77.000000, 45.000000, 31.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((65.000000, 30.000000, 44.000000), (75.000000, 43.000000, 45.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((75.000000, 43.000000, 45.000000), (78.000000, 43.000000, 34.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((78.000000, 43.000000, 34.000000), (65.000000, 30.000000, 44.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((70.000000, 36.500000, 44.500000),),
((76.500000, 43.000000, 39.500000),),
((71.500000, 36.500000, 39.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((75.000000, 43.000000, 45.000000), (66.000000, 55.000000, 43.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((66.000000, 55.000000, 43.000000), (78.000000, 43.000000, 34.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((78.000000, 43.000000, 34.000000), (75.000000, 43.000000, 45.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((70.500000, 49.000000, 44.000000),),
((72.000000, 49.000000, 38.500000),),
((76.500000, 43.000000, 39.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((66.000000, 35.000000, 22.000000), (65.000000, 30.000000, 44.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((65.000000, 30.000000, 44.000000), (78.000000, 43.000000, 34.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((78.000000, 43.000000, 34.000000), (66.000000, 35.000000, 22.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((65.500000, 32.500000, 33.000000),),
((71.500000, 36.500000, 39.000000),),
((72.000000, 39.000000, 28.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((71.000000, 54.000000, 29.000000), (66.000000, 55.000000, 43.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((66.000000, 55.000000, 43.000000), (65.000000, 57.000000, 35.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((65.000000, 57.000000, 35.000000), (71.000000, 54.000000, 29.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((68.500000, 54.500000, 36.000000),),
((65.500000, 56.000000, 39.000000),),
((68.000000, 55.500000, 32.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((53.000000, 24.000000, 35.000000), (65.000000, 30.000000, 44.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((65.000000, 30.000000, 44.000000), (66.000000, 35.000000, 22.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((66.000000, 35.000000, 22.000000), (53.000000, 24.000000, 35.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((59.000000, 27.000000, 39.500000),),
((65.500000, 32.500000, 33.000000),),
((59.500000, 29.500000, 28.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((53.000000, 24.000000, 35.000000), (66.000000, 35.000000, 22.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((66.000000, 35.000000, 22.000000), (53.000000, 28.000000, 22.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((53.000000, 28.000000, 22.000000), (53.000000, 24.000000, 35.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((59.500000, 29.500000, 28.500000),),
((59.500000, 31.500000, 22.000000),),
((53.000000, 26.000000, 28.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((66.000000, 35.000000, 22.000000), (76.000000, 47.000000, 29.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((76.000000, 47.000000, 29.000000), (59.000000, 47.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((59.000000, 47.000000, 21.000000), (66.000000, 35.000000, 22.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((71.000000, 41.000000, 25.500000),),
((67.500000, 47.000000, 25.000000),),
((62.500000, 41.000000, 21.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((76.000000, 47.000000, 29.000000), (71.000000, 54.000000, 29.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((71.000000, 54.000000, 29.000000), (59.000000, 47.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((59.000000, 47.000000, 21.000000), (76.000000, 47.000000, 29.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((73.500000, 50.500000, 29.000000),),
((65.000000, 50.500000, 25.000000),),
((67.500000, 47.000000, 25.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((75.000000, 43.000000, 45.000000), (65.000000, 30.000000, 44.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((65.000000, 30.000000, 44.000000), (56.000000, 38.000000, 48.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((56.000000, 38.000000, 48.000000), (75.000000, 43.000000, 45.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((70.000000, 36.500000, 44.500000),),
((60.500000, 34.000000, 46.000000),),
((65.500000, 40.500000, 46.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((66.000000, 55.000000, 43.000000), (75.000000, 43.000000, 45.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((75.000000, 43.000000, 45.000000), (56.000000, 38.000000, 48.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((56.000000, 38.000000, 48.000000), (66.000000, 55.000000, 43.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((70.500000, 49.000000, 44.000000),),
((65.500000, 40.500000, 46.500000),),
((61.000000, 46.500000, 45.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((53.000000, 28.000000, 22.000000), (66.000000, 35.000000, 22.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((66.000000, 35.000000, 22.000000), (59.000000, 47.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((59.000000, 47.000000, 21.000000), (53.000000, 28.000000, 22.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((59.500000, 31.500000, 22.000000),),
((62.500000, 41.000000, 21.500000),),
((56.000000, 37.500000, 21.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((53.000000, 24.000000, 35.000000), (49.000000, 27.000000, 39.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((49.000000, 27.000000, 39.000000), (65.000000, 30.000000, 44.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((65.000000, 30.000000, 44.000000), (53.000000, 24.000000, 35.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((51.000000, 25.500000, 37.000000),),
((57.000000, 28.500000, 41.500000),),
((59.000000, 27.000000, 39.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((59.000000, 47.000000, 21.000000), (71.000000, 54.000000, 29.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((71.000000, 54.000000, 29.000000), (65.000000, 57.000000, 35.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((65.000000, 57.000000, 35.000000), (59.000000, 47.000000, 21.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((65.000000, 50.500000, 25.000000),),
((68.000000, 55.500000, 32.000000),),
((62.000000, 52.000000, 28.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((52.000000, 51.000000, 29.000000), (59.000000, 47.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((59.000000, 47.000000, 21.000000), (65.000000, 57.000000, 35.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((65.000000, 57.000000, 35.000000), (52.000000, 51.000000, 29.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((55.500000, 49.000000, 25.000000),),
((62.000000, 52.000000, 28.000000),),
((58.500000, 54.000000, 32.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((65.000000, 30.000000, 44.000000), (49.000000, 27.000000, 39.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((49.000000, 27.000000, 39.000000), (56.000000, 38.000000, 48.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((56.000000, 38.000000, 48.000000), (65.000000, 30.000000, 44.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((57.000000, 28.500000, 41.500000),),
((52.500000, 32.500000, 43.500000),),
((60.500000, 34.000000, 46.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((45.000000, 37.000000, 24.000000), (53.000000, 28.000000, 22.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((53.000000, 28.000000, 22.000000), (59.000000, 47.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((59.000000, 47.000000, 21.000000), (45.000000, 37.000000, 24.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((49.000000, 32.500000, 23.000000),),
((56.000000, 37.500000, 21.500000),),
((52.000000, 42.000000, 22.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((52.000000, 49.000000, 42.000000), (66.000000, 55.000000, 43.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((66.000000, 55.000000, 43.000000), (56.000000, 38.000000, 48.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((56.000000, 38.000000, 48.000000), (52.000000, 49.000000, 42.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((59.000000, 52.000000, 42.500000),),
((61.000000, 46.500000, 45.500000),),
((54.000000, 43.500000, 45.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((66.000000, 55.000000, 43.000000), (52.000000, 49.000000, 42.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((52.000000, 49.000000, 42.000000), (65.000000, 57.000000, 35.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((65.000000, 57.000000, 35.000000), (66.000000, 55.000000, 43.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((59.000000, 52.000000, 42.500000),),
((58.500000, 53.000000, 38.500000),),
((65.500000, 56.000000, 39.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((52.000000, 49.000000, 42.000000), (52.000000, 51.000000, 29.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((52.000000, 51.000000, 29.000000), (65.000000, 57.000000, 35.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((65.000000, 57.000000, 35.000000), (52.000000, 49.000000, 42.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((52.000000, 50.000000, 35.500000),),
((58.500000, 54.000000, 32.000000),),
((58.500000, 53.000000, 38.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((52.000000, 51.000000, 29.000000), (45.000000, 37.000000, 24.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((45.000000, 37.000000, 24.000000), (59.000000, 47.000000, 21.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((59.000000, 47.000000, 21.000000), (52.000000, 51.000000, 29.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((48.500000, 44.000000, 26.500000),),
((52.000000, 42.000000, 22.500000),),
((55.500000, 49.000000, 25.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((56.000000, 38.000000, 48.000000), (49.000000, 27.000000, 39.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((49.000000, 27.000000, 39.000000), (42.000000, 37.000000, 35.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((42.000000, 37.000000, 35.000000), (56.000000, 38.000000, 48.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((52.500000, 32.500000, 43.500000),),
((45.500000, 32.000000, 37.000000),),
((49.000000, 37.500000, 41.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((52.000000, 49.000000, 42.000000), (56.000000, 38.000000, 48.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((56.000000, 38.000000, 48.000000), (42.000000, 37.000000, 35.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((42.000000, 37.000000, 35.000000), (52.000000, 49.000000, 42.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((54.000000, 43.500000, 45.000000),),
((49.000000, 37.500000, 41.500000),),
((47.000000, 43.000000, 38.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((49.000000, 27.000000, 39.000000), (53.000000, 24.000000, 35.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((53.000000, 24.000000, 35.000000), (45.000000, 37.000000, 24.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((45.000000, 37.000000, 24.000000), (49.000000, 27.000000, 39.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((51.000000, 25.500000, 37.000000),),
((49.000000, 30.500000, 29.500000),),
((47.000000, 32.000000, 31.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((45.000000, 37.000000, 24.000000), (53.000000, 24.000000, 35.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((53.000000, 24.000000, 35.000000), (53.000000, 28.000000, 22.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((53.000000, 28.000000, 22.000000), (45.000000, 37.000000, 24.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((49.000000, 30.500000, 29.500000),),
((53.000000, 26.000000, 28.500000),),
((49.000000, 32.500000, 23.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((49.000000, 27.000000, 39.000000), (45.000000, 37.000000, 24.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((45.000000, 37.000000, 24.000000), (42.000000, 37.000000, 35.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((42.000000, 37.000000, 35.000000), (49.000000, 27.000000, 39.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((47.000000, 32.000000, 31.500000),),
((43.500000, 37.000000, 29.500000),),
((45.500000, 32.000000, 37.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((52.000000, 51.000000, 29.000000), (52.000000, 49.000000, 42.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((52.000000, 49.000000, 42.000000), (42.000000, 37.000000, 35.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((42.000000, 37.000000, 35.000000), (52.000000, 51.000000, 29.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((52.000000, 50.000000, 35.500000),),
((47.000000, 43.000000, 38.500000),),
((47.000000, 44.000000, 32.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((45.000000, 37.000000, 24.000000), (52.000000, 51.000000, 29.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((52.000000, 51.000000, 29.000000), (42.000000, 37.000000, 35.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((42.000000, 37.000000, 35.000000), (45.000000, 37.000000, 24.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((48.500000, 44.000000, 26.500000),),
((47.000000, 44.000000, 32.000000),),
((43.500000, 37.000000, 29.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((100.000000, 67.000000, 54.000000), (100.000000, 86.000000, 50.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 86.000000, 50.000000), (100.000000, 90.000000, 42.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 90.000000, 42.000000), (100.000000, 83.000000, 31.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 83.000000, 31.000000), (100.000000, 59.000000, 34.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 59.000000, 34.000000), (100.000000, 53.000000, 37.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 53.000000, 37.000000), (100.000000, 54.000000, 46.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 54.000000, 46.000000), (100.000000, 67.000000, 54.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((100.000000, 76.500000, 52.000000),),
((100.000000, 88.000000, 46.000000),),
((100.000000, 86.500000, 36.500000),),
((100.000000, 71.000000, 32.500000),),
((100.000000, 56.000000, 35.500000),),
((100.000000, 53.500000, 41.500000),),
((100.000000, 60.500000, 50.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((100.000000, 59.000000, 34.000000), (100.000000, 83.000000, 31.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 83.000000, 31.000000), (96.000000, 75.000000, 28.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((96.000000, 75.000000, 28.000000), (100.000000, 59.000000, 34.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((100.000000, 71.000000, 32.500000),),
((98.000000, 79.000000, 29.500000),),
((98.000000, 67.000000, 31.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((100.000000, 54.000000, 46.000000), (93.000000, 57.000000, 49.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((93.000000, 57.000000, 49.000000), (100.000000, 67.000000, 54.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 67.000000, 54.000000), (100.000000, 54.000000, 46.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((96.500000, 55.500000, 47.500000),),
((96.500000, 62.000000, 51.500000),),
((100.000000, 60.500000, 50.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((100.000000, 54.000000, 46.000000), (100.000000, 53.000000, 37.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 53.000000, 37.000000), (92.000000, 52.000000, 38.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((92.000000, 52.000000, 38.000000), (100.000000, 54.000000, 46.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((100.000000, 53.500000, 41.500000),),
((96.000000, 52.500000, 37.500000),),
((96.000000, 53.000000, 42.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((92.000000, 52.000000, 38.000000), (100.000000, 53.000000, 37.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 53.000000, 37.000000), (100.000000, 59.000000, 34.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 59.000000, 34.000000), (92.000000, 52.000000, 38.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((96.000000, 52.500000, 37.500000),),
((100.000000, 56.000000, 35.500000),),
((96.000000, 55.500000, 36.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((100.000000, 54.000000, 46.000000), (92.000000, 52.000000, 38.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((92.000000, 52.000000, 38.000000), (93.000000, 57.000000, 49.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((93.000000, 57.000000, 49.000000), (100.000000, 54.000000, 46.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((96.000000, 53.000000, 42.000000),),
((92.500000, 54.500000, 43.500000),),
((96.500000, 55.500000, 47.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((92.000000, 52.000000, 38.000000), (100.000000, 59.000000, 34.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 59.000000, 34.000000), (86.000000, 61.000000, 37.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((86.000000, 61.000000, 37.000000), (92.000000, 52.000000, 38.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((96.000000, 55.500000, 36.000000),),
((93.000000, 60.000000, 35.500000),),
((89.000000, 56.500000, 37.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((100.000000, 59.000000, 34.000000), (96.000000, 75.000000, 28.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((96.000000, 75.000000, 28.000000), (86.000000, 61.000000, 37.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((86.000000, 61.000000, 37.000000), (100.000000, 59.000000, 34.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((98.000000, 67.000000, 31.000000),),
((91.000000, 68.000000, 32.500000),),
((93.000000, 60.000000, 35.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((90.000000, 73.000000, 50.000000), (100.000000, 86.000000, 50.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 86.000000, 50.000000), (100.000000, 67.000000, 54.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 67.000000, 54.000000), (90.000000, 73.000000, 50.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((95.000000, 79.500000, 50.000000),),
((100.000000, 76.500000, 52.000000),),
((95.000000, 70.000000, 52.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((93.000000, 57.000000, 49.000000), (90.000000, 73.000000, 50.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((90.000000, 73.000000, 50.000000), (100.000000, 67.000000, 54.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 67.000000, 54.000000), (93.000000, 57.000000, 49.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((91.500000, 65.000000, 49.500000),),
((95.000000, 70.000000, 52.000000),),
((96.500000, 62.000000, 51.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((100.000000, 83.000000, 31.000000), (93.000000, 76.000000, 31.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((93.000000, 76.000000, 31.000000), (96.000000, 75.000000, 28.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((96.000000, 75.000000, 28.000000), (100.000000, 83.000000, 31.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((96.500000, 79.500000, 31.000000),),
((94.500000, 75.500000, 29.500000),),
((98.000000, 79.000000, 29.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((89.000000, 79.000000, 38.000000), (100.000000, 83.000000, 31.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 83.000000, 31.000000), (100.000000, 90.000000, 42.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 90.000000, 42.000000), (89.000000, 79.000000, 38.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((94.500000, 81.000000, 34.500000),),
((100.000000, 86.500000, 36.500000),),
((94.500000, 84.500000, 40.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((89.000000, 79.000000, 38.000000), (93.000000, 76.000000, 31.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((93.000000, 76.000000, 31.000000), (100.000000, 83.000000, 31.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 83.000000, 31.000000), (89.000000, 79.000000, 38.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((91.000000, 77.500000, 34.500000),),
((96.500000, 79.500000, 31.000000),),
((94.500000, 81.000000, 34.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((93.000000, 57.000000, 49.000000), (87.000000, 60.000000, 45.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((87.000000, 60.000000, 45.000000), (90.000000, 73.000000, 50.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((90.000000, 73.000000, 50.000000), (93.000000, 57.000000, 49.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((90.000000, 58.500000, 47.000000),),
((88.500000, 66.500000, 47.500000),),
((91.500000, 65.000000, 49.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((92.000000, 52.000000, 38.000000), (87.000000, 60.000000, 45.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((87.000000, 60.000000, 45.000000), (93.000000, 57.000000, 49.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((93.000000, 57.000000, 49.000000), (92.000000, 52.000000, 38.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((89.500000, 56.000000, 41.500000),),
((90.000000, 58.500000, 47.000000),),
((92.500000, 54.500000, 43.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((96.000000, 75.000000, 28.000000), (93.000000, 76.000000, 31.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((93.000000, 76.000000, 31.000000), (86.000000, 61.000000, 37.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((86.000000, 61.000000, 37.000000), (96.000000, 75.000000, 28.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((94.500000, 75.500000, 29.500000),),
((89.500000, 68.500000, 34.000000),),
((91.000000, 68.000000, 32.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((100.000000, 86.000000, 50.000000), (89.000000, 79.000000, 38.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((89.000000, 79.000000, 38.000000), (100.000000, 90.000000, 42.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 90.000000, 42.000000), (100.000000, 86.000000, 50.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((94.500000, 82.500000, 44.000000),),
((94.500000, 84.500000, 40.000000),),
((100.000000, 88.000000, 46.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((89.000000, 79.000000, 38.000000), (100.000000, 86.000000, 50.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((100.000000, 86.000000, 50.000000), (90.000000, 73.000000, 50.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((90.000000, 73.000000, 50.000000), (89.000000, 79.000000, 38.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((94.500000, 82.500000, 44.000000),),
((95.000000, 79.500000, 50.000000),),
((89.500000, 76.000000, 44.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((93.000000, 76.000000, 31.000000), (89.000000, 79.000000, 38.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((89.000000, 79.000000, 38.000000), (86.000000, 61.000000, 37.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((86.000000, 61.000000, 37.000000), (93.000000, 76.000000, 31.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((91.000000, 77.500000, 34.500000),),
((87.500000, 70.000000, 37.500000),),
((89.500000, 68.500000, 34.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((87.000000, 60.000000, 45.000000), (92.000000, 52.000000, 38.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((92.000000, 52.000000, 38.000000), (86.000000, 61.000000, 37.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((86.000000, 61.000000, 37.000000), (87.000000, 60.000000, 45.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((89.500000, 56.000000, 41.500000),),
((89.000000, 56.500000, 37.500000),),
((86.500000, 60.500000, 41.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((90.000000, 73.000000, 50.000000), (87.000000, 60.000000, 45.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((87.000000, 60.000000, 45.000000), (86.000000, 61.000000, 37.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((86.000000, 61.000000, 37.000000), (90.000000, 73.000000, 50.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((88.500000, 66.500000, 47.500000),),
((86.500000, 60.500000, 41.000000),),
((88.000000, 67.000000, 43.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((89.000000, 79.000000, 38.000000), (90.000000, 73.000000, 50.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((90.000000, 73.000000, 50.000000), (86.000000, 61.000000, 37.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((86.000000, 61.000000, 37.000000), (89.000000, 79.000000, 38.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((89.500000, 76.000000, 44.000000),),
((88.000000, 67.000000, 43.500000),),
((87.500000, 70.000000, 37.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((14.000000, 66.000000, 36.000000), (15.000000, 82.000000, 48.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((15.000000, 82.000000, 48.000000), (15.000000, 83.000000, 38.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((15.000000, 83.000000, 38.000000), (14.000000, 66.000000, 36.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((14.500000, 74.000000, 42.000000),),
((15.000000, 82.500000, 43.000000),),
((14.500000, 74.500000, 37.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((15.000000, 82.000000, 48.000000), (14.000000, 66.000000, 36.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((14.000000, 66.000000, 36.000000), (12.000000, 66.000000, 49.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((12.000000, 66.000000, 49.000000), (15.000000, 82.000000, 48.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((14.500000, 74.000000, 42.000000),),
((13.000000, 66.000000, 42.500000),),
((13.500000, 74.000000, 48.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((12.000000, 66.000000, 49.000000), (14.000000, 66.000000, 36.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((14.000000, 66.000000, 36.000000), (4.000000, 54.000000, 36.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((4.000000, 54.000000, 36.000000), (12.000000, 66.000000, 49.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((13.000000, 66.000000, 42.500000),),
((9.000000, 60.000000, 36.000000),),
((8.000000, 60.000000, 42.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 54.000000, 46.000000), (12.000000, 66.000000, 49.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((12.000000, 66.000000, 49.000000), (4.000000, 54.000000, 36.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((4.000000, 54.000000, 36.000000), (0.000000, 54.000000, 46.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((6.000000, 60.000000, 47.500000),),
((8.000000, 60.000000, 42.500000),),
((2.000000, 54.000000, 41.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((15.000000, 82.000000, 48.000000), (12.000000, 66.000000, 49.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((12.000000, 66.000000, 49.000000), (7.000000, 83.000000, 53.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((7.000000, 83.000000, 53.000000), (15.000000, 82.000000, 48.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((13.500000, 74.000000, 48.500000),),
((9.500000, 74.500000, 51.000000),),
((11.000000, 82.500000, 50.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((3.000000, 72.000000, 31.000000), (14.000000, 66.000000, 36.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((14.000000, 66.000000, 36.000000), (15.000000, 83.000000, 38.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((15.000000, 83.000000, 38.000000), (3.000000, 72.000000, 31.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((8.500000, 69.000000, 33.500000),),
((14.500000, 74.500000, 37.000000),),
((9.000000, 77.500000, 34.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((12.000000, 66.000000, 49.000000), (0.000000, 69.000000, 55.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 69.000000, 55.000000), (7.000000, 83.000000, 53.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((7.000000, 83.000000, 53.000000), (12.000000, 66.000000, 49.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((6.000000, 67.500000, 52.000000),),
((3.500000, 76.000000, 54.000000),),
((9.500000, 74.500000, 51.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((15.000000, 82.000000, 48.000000), (3.000000, 89.000000, 34.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((3.000000, 89.000000, 34.000000), (15.000000, 83.000000, 38.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((15.000000, 83.000000, 38.000000), (15.000000, 82.000000, 48.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((9.000000, 85.500000, 41.000000),),
((9.000000, 86.000000, 36.000000),),
((15.000000, 82.500000, 43.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((3.000000, 89.000000, 34.000000), (3.000000, 72.000000, 31.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((3.000000, 72.000000, 31.000000), (15.000000, 83.000000, 38.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((15.000000, 83.000000, 38.000000), (3.000000, 89.000000, 34.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((3.000000, 80.500000, 32.500000),),
((9.000000, 77.500000, 34.500000),),
((9.000000, 86.000000, 36.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 87.000000, 50.000000), (15.000000, 82.000000, 48.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((15.000000, 82.000000, 48.000000), (7.000000, 83.000000, 53.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((7.000000, 83.000000, 53.000000), (0.000000, 87.000000, 50.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((7.500000, 84.500000, 49.000000),),
((11.000000, 82.500000, 50.500000),),
((3.500000, 85.000000, 51.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((15.000000, 82.000000, 48.000000), (0.000000, 87.000000, 50.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 87.000000, 50.000000), (3.000000, 89.000000, 34.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((3.000000, 89.000000, 34.000000), (15.000000, 82.000000, 48.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((7.500000, 84.500000, 49.000000),),
((1.500000, 88.000000, 42.000000),),
((9.000000, 85.500000, 41.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 54.000000, 46.000000), (0.000000, 69.000000, 55.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 69.000000, 55.000000), (12.000000, 66.000000, 49.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((12.000000, 66.000000, 49.000000), (0.000000, 54.000000, 46.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((0.000000, 61.500000, 50.500000),),
((6.000000, 67.500000, 52.000000),),
((6.000000, 60.000000, 47.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 61.000000, 33.000000), (14.000000, 66.000000, 36.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((14.000000, 66.000000, 36.000000), (3.000000, 72.000000, 31.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((3.000000, 72.000000, 31.000000), (0.000000, 61.000000, 33.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((7.000000, 63.500000, 34.500000),),
((8.500000, 69.000000, 33.500000),),
((1.500000, 66.500000, 32.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((14.000000, 66.000000, 36.000000), (0.000000, 61.000000, 33.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 61.000000, 33.000000), (4.000000, 54.000000, 36.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((4.000000, 54.000000, 36.000000), (14.000000, 66.000000, 36.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((7.000000, 63.500000, 34.500000),),
((2.000000, 57.500000, 34.500000),),
((9.000000, 60.000000, 36.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((3.000000, 72.000000, 31.000000), (3.000000, 89.000000, 34.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((3.000000, 89.000000, 34.000000), (0.000000, 85.000000, 33.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 85.000000, 33.000000), (3.000000, 72.000000, 31.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((3.000000, 80.500000, 32.500000),),
((1.500000, 87.000000, 33.500000),),
((1.500000, 78.500000, 32.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 61.000000, 33.000000), (0.000000, 54.000000, 36.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 54.000000, 36.000000), (4.000000, 54.000000, 36.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((4.000000, 54.000000, 36.000000), (0.000000, 61.000000, 33.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((0.000000, 57.500000, 34.500000),),
((2.000000, 54.000000, 36.000000),),
((2.000000, 57.500000, 34.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 54.000000, 36.000000), (0.000000, 54.000000, 46.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 54.000000, 46.000000), (4.000000, 54.000000, 36.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((4.000000, 54.000000, 36.000000), (0.000000, 54.000000, 36.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((0.000000, 54.000000, 41.000000),),
((2.000000, 54.000000, 41.000000),),
((2.000000, 54.000000, 36.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 69.000000, 55.000000), (0.000000, 87.000000, 50.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 87.000000, 50.000000), (7.000000, 83.000000, 53.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((7.000000, 83.000000, 53.000000), (0.000000, 69.000000, 55.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((0.000000, 78.000000, 52.500000),),
((3.500000, 85.000000, 51.500000),),
((3.500000, 76.000000, 54.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 61.000000, 33.000000), (3.000000, 72.000000, 31.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((3.000000, 72.000000, 31.000000), (0.000000, 85.000000, 33.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 85.000000, 33.000000), (0.000000, 61.000000, 33.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((1.500000, 66.500000, 32.000000),),
((1.500000, 78.500000, 32.000000),),
((0.000000, 73.000000, 33.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((3.000000, 89.000000, 34.000000), (0.000000, 87.000000, 50.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 87.000000, 50.000000), (0.000000, 85.000000, 33.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 85.000000, 33.000000), (3.000000, 89.000000, 34.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((1.500000, 88.000000, 42.000000),),
((0.000000, 86.000000, 41.500000),),
((1.500000, 87.000000, 33.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 54.000000, 46.000000), (0.000000, 69.000000, 55.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 69.000000, 55.000000), (0.000000, 87.000000, 50.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 87.000000, 50.000000), (0.000000, 85.000000, 33.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 85.000000, 33.000000), (0.000000, 61.000000, 33.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 61.000000, 33.000000), (0.000000, 54.000000, 36.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 54.000000, 36.000000), (0.000000, 54.000000, 46.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((0.000000, 61.500000, 50.500000),),
((0.000000, 78.000000, 52.500000),),
((0.000000, 86.000000, 41.500000),),
((0.000000, 73.000000, 33.000000),),
((0.000000, 57.500000, 34.500000),),
((0.000000, 54.000000, 41.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((79.000000, 54.000000, 48.000000), (80.000000, 52.000000, 58.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((80.000000, 52.000000, 58.000000), (78.000000, 64.000000, 46.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((78.000000, 64.000000, 46.000000), (79.000000, 54.000000, 48.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((79.500000, 53.000000, 53.000000),),
((79.000000, 58.000000, 52.000000),),
((78.500000, 59.000000, 47.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((78.000000, 64.000000, 46.000000), (80.000000, 52.000000, 58.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((80.000000, 52.000000, 58.000000), (90.000000, 69.000000, 73.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((90.000000, 69.000000, 73.000000), (78.000000, 64.000000, 46.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((79.000000, 58.000000, 52.000000),),
((85.000000, 60.500000, 65.500000),),
((84.000000, 66.500000, 59.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((80.000000, 52.000000, 58.000000), (80.000000, 50.000000, 68.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((80.000000, 50.000000, 68.000000), (90.000000, 69.000000, 73.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((90.000000, 69.000000, 73.000000), (80.000000, 52.000000, 58.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((80.000000, 51.000000, 63.000000),),
((85.000000, 59.500000, 70.500000),),
((85.000000, 60.500000, 65.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((80.000000, 50.000000, 68.000000), (85.000000, 59.000000, 80.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((85.000000, 59.000000, 80.000000), (90.000000, 69.000000, 73.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((90.000000, 69.000000, 73.000000), (80.000000, 50.000000, 68.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((82.500000, 54.500000, 74.000000),),
((87.500000, 64.000000, 76.500000),),
((85.000000, 59.500000, 70.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((88.000000, 74.000000, 71.000000), (78.000000, 64.000000, 46.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((78.000000, 64.000000, 46.000000), (90.000000, 69.000000, 73.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((90.000000, 69.000000, 73.000000), (88.000000, 74.000000, 71.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((83.000000, 69.000000, 58.500000),),
((84.000000, 66.500000, 59.500000),),
((89.000000, 71.500000, 72.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((85.000000, 59.000000, 80.000000), (84.000000, 71.000000, 83.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((84.000000, 71.000000, 83.000000), (90.000000, 69.000000, 73.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((90.000000, 69.000000, 73.000000), (85.000000, 59.000000, 80.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((84.500000, 65.000000, 81.500000),),
((87.000000, 70.000000, 78.000000),),
((87.500000, 64.000000, 76.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((84.000000, 71.000000, 83.000000), (88.000000, 74.000000, 71.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((88.000000, 74.000000, 71.000000), (90.000000, 69.000000, 73.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((90.000000, 69.000000, 73.000000), (84.000000, 71.000000, 83.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((86.000000, 72.500000, 77.000000),),
((89.000000, 71.500000, 72.000000),),
((87.000000, 70.000000, 78.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((88.000000, 74.000000, 71.000000), (78.000000, 77.000000, 59.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((78.000000, 77.000000, 59.000000), (78.000000, 64.000000, 46.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((78.000000, 64.000000, 46.000000), (88.000000, 74.000000, 71.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((83.000000, 75.500000, 65.000000),),
((78.000000, 70.500000, 52.500000),),
((83.000000, 69.000000, 58.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((80.000000, 52.000000, 58.000000), (79.000000, 54.000000, 48.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((79.000000, 54.000000, 48.000000), (70.000000, 49.000000, 53.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((70.000000, 49.000000, 53.000000), (80.000000, 52.000000, 58.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((79.500000, 53.000000, 53.000000),),
((74.500000, 51.500000, 50.500000),),
((75.000000, 50.500000, 55.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((80.000000, 52.000000, 58.000000), (70.000000, 49.000000, 53.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((70.000000, 49.000000, 53.000000), (80.000000, 50.000000, 68.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((80.000000, 50.000000, 68.000000), (80.000000, 52.000000, 58.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((75.000000, 50.500000, 55.500000),),
((75.000000, 49.500000, 60.500000),),
((80.000000, 51.000000, 63.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((74.000000, 55.000000, 46.000000), (79.000000, 54.000000, 48.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((79.000000, 54.000000, 48.000000), (78.000000, 64.000000, 46.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((78.000000, 64.000000, 46.000000), (74.000000, 55.000000, 46.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((76.500000, 54.500000, 47.000000),),
((78.500000, 59.000000, 47.000000),),
((76.000000, 59.500000, 46.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((78.000000, 77.000000, 59.000000), (69.000000, 68.000000, 46.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((69.000000, 68.000000, 46.000000), (78.000000, 64.000000, 46.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((78.000000, 64.000000, 46.000000), (78.000000, 77.000000, 59.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((73.500000, 72.500000, 52.500000),),
((73.500000, 66.000000, 46.000000),),
((78.000000, 70.500000, 52.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((84.000000, 71.000000, 83.000000), (85.000000, 59.000000, 80.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((85.000000, 59.000000, 80.000000), (75.500000, 60.000000, 82.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((75.500000, 60.000000, 82.000000), (84.000000, 71.000000, 83.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((84.500000, 65.000000, 81.500000),),
((80.250000, 59.500000, 81.000000),),
((79.750000, 65.500000, 82.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((66.000000, 56.000000, 45.000000), (74.000000, 55.000000, 46.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((74.000000, 55.000000, 46.000000), (69.000000, 68.000000, 46.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((69.000000, 68.000000, 46.000000), (66.000000, 56.000000, 45.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((70.000000, 55.500000, 45.500000),),
((71.500000, 61.500000, 46.000000),),
((67.500000, 62.000000, 45.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((79.000000, 54.000000, 48.000000), (74.000000, 55.000000, 46.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((74.000000, 55.000000, 46.000000), (70.000000, 49.000000, 53.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((70.000000, 49.000000, 53.000000), (79.000000, 54.000000, 48.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((76.500000, 54.500000, 47.000000),),
((72.000000, 52.000000, 49.500000),),
((74.500000, 51.500000, 50.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((75.500000, 60.000000, 82.000000), (85.000000, 59.000000, 80.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((85.000000, 59.000000, 80.000000), (80.000000, 50.000000, 68.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((80.000000, 50.000000, 68.000000), (75.500000, 60.000000, 82.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((80.250000, 59.500000, 81.000000),),
((82.500000, 54.500000, 74.000000),),
((77.750000, 55.000000, 75.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((69.000000, 68.000000, 46.000000), (74.000000, 55.000000, 46.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((74.000000, 55.000000, 46.000000), (78.000000, 64.000000, 46.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((78.000000, 64.000000, 46.000000), (69.000000, 68.000000, 46.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((71.500000, 61.500000, 46.000000),),
((76.000000, 59.500000, 46.000000),),
((73.500000, 66.000000, 46.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((68.000000, 53.000000, 72.000000), (75.500000, 60.000000, 82.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((75.500000, 60.000000, 82.000000), (80.000000, 50.000000, 68.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((80.000000, 50.000000, 68.000000), (68.000000, 53.000000, 72.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((71.750000, 56.500000, 77.000000),),
((77.750000, 55.000000, 75.000000),),
((74.000000, 51.500000, 70.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((74.000000, 55.000000, 46.000000), (66.000000, 56.000000, 45.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((66.000000, 56.000000, 45.000000), (70.000000, 49.000000, 53.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((70.000000, 49.000000, 53.000000), (74.000000, 55.000000, 46.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((70.000000, 55.500000, 45.500000),),
((68.000000, 52.500000, 49.000000),),
((72.000000, 52.000000, 49.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((84.000000, 71.000000, 83.000000), (65.000000, 75.000000, 64.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((65.000000, 75.000000, 64.000000), (88.000000, 74.000000, 71.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((88.000000, 74.000000, 71.000000), (84.000000, 71.000000, 83.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((74.500000, 73.000000, 73.500000),),
((76.500000, 74.500000, 67.500000),),
((86.000000, 72.500000, 77.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((88.000000, 74.000000, 71.000000), (65.000000, 75.000000, 64.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((65.000000, 75.000000, 64.000000), (78.000000, 77.000000, 59.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((78.000000, 77.000000, 59.000000), (88.000000, 74.000000, 71.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((76.500000, 74.500000, 67.500000),),
((71.500000, 76.000000, 61.500000),),
((83.000000, 75.500000, 65.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((70.000000, 49.000000, 53.000000), (68.000000, 53.000000, 72.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((68.000000, 53.000000, 72.000000), (80.000000, 50.000000, 68.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((80.000000, 50.000000, 68.000000), (70.000000, 49.000000, 53.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((69.000000, 51.000000, 62.500000),),
((74.000000, 51.500000, 70.000000),),
((75.000000, 49.500000, 60.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((63.500000, 51.500000, 56.000000), (68.000000, 53.000000, 72.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((68.000000, 53.000000, 72.000000), (70.000000, 49.000000, 53.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((70.000000, 49.000000, 53.000000), (63.500000, 51.500000, 56.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((65.750000, 52.250000, 64.000000),),
((69.000000, 51.000000, 62.500000),),
((66.750000, 50.250000, 54.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((65.000000, 75.000000, 64.000000), (69.000000, 68.000000, 46.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((69.000000, 68.000000, 46.000000), (78.000000, 77.000000, 59.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((78.000000, 77.000000, 59.000000), (65.000000, 75.000000, 64.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((67.000000, 71.500000, 55.000000),),
((73.500000, 72.500000, 52.500000),),
((71.500000, 76.000000, 61.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((69.000000, 68.000000, 46.000000), (65.000000, 75.000000, 64.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((65.000000, 75.000000, 64.000000), (62.000000, 67.000000, 51.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((62.000000, 67.000000, 51.000000), (69.000000, 68.000000, 46.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((67.000000, 71.500000, 55.000000),),
((63.500000, 71.000000, 57.500000),),
((65.500000, 67.500000, 48.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((66.000000, 56.000000, 45.000000), (63.500000, 51.500000, 56.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((63.500000, 51.500000, 56.000000), (70.000000, 49.000000, 53.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((70.000000, 49.000000, 53.000000), (66.000000, 56.000000, 45.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((64.750000, 53.750000, 50.500000),),
((66.750000, 50.250000, 54.500000),),
((68.000000, 52.500000, 49.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((65.000000, 75.000000, 64.000000), (84.000000, 71.000000, 83.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((84.000000, 71.000000, 83.000000), (62.000000, 64.000000, 71.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((62.000000, 64.000000, 71.000000), (65.000000, 75.000000, 64.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((74.500000, 73.000000, 73.500000),),
((73.000000, 67.500000, 77.000000),),
((63.500000, 69.500000, 67.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((62.000000, 64.000000, 71.000000), (84.000000, 71.000000, 83.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((84.000000, 71.000000, 83.000000), (75.500000, 60.000000, 82.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((75.500000, 60.000000, 82.000000), (62.000000, 64.000000, 71.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((73.000000, 67.500000, 77.000000),),
((79.750000, 65.500000, 82.500000),),
((68.750000, 62.000000, 76.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((62.000000, 64.000000, 50.000000), (66.000000, 56.000000, 45.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((66.000000, 56.000000, 45.000000), (69.000000, 68.000000, 46.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((69.000000, 68.000000, 46.000000), (62.000000, 64.000000, 50.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((64.000000, 60.000000, 47.500000),),
((67.500000, 62.000000, 45.500000),),
((65.500000, 66.000000, 48.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((62.000000, 64.000000, 50.000000), (69.000000, 68.000000, 46.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((69.000000, 68.000000, 46.000000), (62.000000, 67.000000, 51.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((62.000000, 67.000000, 51.000000), (62.000000, 64.000000, 50.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((65.500000, 66.000000, 48.000000),),
((65.500000, 67.500000, 48.500000),),
((62.000000, 65.500000, 50.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((68.000000, 53.000000, 72.000000), (62.000000, 64.000000, 71.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((62.000000, 64.000000, 71.000000), (75.500000, 60.000000, 82.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((75.500000, 60.000000, 82.000000), (68.000000, 53.000000, 72.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((65.000000, 58.500000, 71.500000),),
((68.750000, 62.000000, 76.500000),),
((71.750000, 56.500000, 77.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((68.000000, 53.000000, 72.000000), (63.500000, 51.500000, 56.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((63.500000, 51.500000, 56.000000), (60.000000, 60.000000, 61.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((60.000000, 60.000000, 61.000000), (68.000000, 53.000000, 72.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((65.750000, 52.250000, 64.000000),),
((61.750000, 55.750000, 58.500000),),
((64.000000, 56.500000, 66.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((62.000000, 64.000000, 71.000000), (68.000000, 53.000000, 72.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((68.000000, 53.000000, 72.000000), (60.000000, 60.000000, 61.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((60.000000, 60.000000, 61.000000), (62.000000, 64.000000, 71.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((65.000000, 58.500000, 71.500000),),
((64.000000, 56.500000, 66.500000),),
((61.000000, 62.000000, 66.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((66.000000, 56.000000, 45.000000), (62.000000, 64.000000, 50.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((62.000000, 64.000000, 50.000000), (63.500000, 51.500000, 56.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((63.500000, 51.500000, 56.000000), (66.000000, 56.000000, 45.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((64.000000, 60.000000, 47.500000),),
((62.750000, 57.750000, 53.000000),),
((64.750000, 53.750000, 50.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((63.500000, 51.500000, 56.000000), (62.000000, 64.000000, 50.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((62.000000, 64.000000, 50.000000), (60.000000, 60.000000, 61.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((60.000000, 60.000000, 61.000000), (63.500000, 51.500000, 56.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((62.750000, 57.750000, 53.000000),),
((61.000000, 62.000000, 55.500000),),
((61.750000, 55.750000, 58.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((62.000000, 67.000000, 51.000000), (65.000000, 75.000000, 64.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((65.000000, 75.000000, 64.000000), (60.000000, 60.000000, 61.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((60.000000, 60.000000, 61.000000), (62.000000, 67.000000, 51.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((63.500000, 71.000000, 57.500000),),
((62.500000, 67.500000, 62.500000),),
((61.000000, 63.500000, 56.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((65.000000, 75.000000, 64.000000), (62.000000, 64.000000, 71.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((62.000000, 64.000000, 71.000000), (60.000000, 60.000000, 61.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((60.000000, 60.000000, 61.000000), (65.000000, 75.000000, 64.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((63.500000, 69.500000, 67.500000),),
((61.000000, 62.000000, 66.000000),),
((62.500000, 67.500000, 62.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((62.000000, 64.000000, 50.000000), (62.000000, 67.000000, 51.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((62.000000, 67.000000, 51.000000), (60.000000, 60.000000, 61.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((60.000000, 60.000000, 61.000000), (62.000000, 64.000000, 50.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((62.000000, 65.500000, 50.500000),),
((61.000000, 63.500000, 56.000000),),
((61.000000, 62.000000, 55.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((85.000000, 35.000000, 77.000000), (86.000000, 31.000000, 87.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((86.000000, 31.000000, 87.000000), (86.000000, 34.000000, 86.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((86.000000, 34.000000, 86.000000), (85.000000, 35.000000, 77.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((85.500000, 33.000000, 82.000000),),
((86.000000, 32.500000, 86.500000),),
((85.500000, 34.500000, 81.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((94.000000, 16.000000, 62.000000), (92.000000, 0.000000, 67.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((92.000000, 0.000000, 67.000000), (96.000000, 12.000000, 78.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((96.000000, 12.000000, 78.000000), (94.000000, 16.000000, 62.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((93.000000, 8.000000, 64.500000),),
((94.000000, 6.000000, 72.500000),),
((95.000000, 14.000000, 70.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((85.000000, 35.000000, 77.000000), (94.000000, 16.000000, 62.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((94.000000, 16.000000, 62.000000), (96.000000, 12.000000, 78.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((96.000000, 12.000000, 78.000000), (85.000000, 35.000000, 77.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((89.500000, 25.500000, 69.500000),),
((95.000000, 14.000000, 70.000000),),
((90.500000, 23.500000, 77.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((86.000000, 31.000000, 87.000000), (85.000000, 35.000000, 77.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((85.000000, 35.000000, 77.000000), (96.000000, 12.000000, 78.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((96.000000, 12.000000, 78.000000), (86.000000, 31.000000, 87.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((85.500000, 33.000000, 82.000000),),
((90.500000, 23.500000, 77.500000),),
((91.000000, 21.500000, 82.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((89.000000, 0.000000, 81.000000), (90.000000, 3.000000, 85.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((90.000000, 3.000000, 85.000000), (96.000000, 12.000000, 78.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((96.000000, 12.000000, 78.000000), (89.000000, 0.000000, 81.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((89.500000, 1.500000, 83.000000),),
((93.000000, 7.500000, 81.500000),),
((92.500000, 6.000000, 79.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((92.000000, 0.000000, 67.000000), (89.000000, 0.000000, 81.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((89.000000, 0.000000, 81.000000), (96.000000, 12.000000, 78.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((96.000000, 12.000000, 78.000000), (92.000000, 0.000000, 67.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((90.500000, 0.000000, 74.000000),),
((92.500000, 6.000000, 79.500000),),
((94.000000, 6.000000, 72.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((94.000000, 16.000000, 62.000000), (85.000000, 35.000000, 77.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((85.000000, 35.000000, 77.000000), (81.500000, 38.000000, 65.500000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((81.500000, 38.000000, 65.500000), (94.000000, 16.000000, 62.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((89.500000, 25.500000, 69.500000),),
((83.250000, 36.500000, 71.250000),),
((87.750000, 27.000000, 63.750000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((86.000000, 31.000000, 87.000000), (90.000000, 3.000000, 85.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((90.000000, 3.000000, 85.000000), (76.000000, 19.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((76.000000, 19.000000, 100.000000), (86.000000, 31.000000, 87.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((88.000000, 17.000000, 86.000000),),
((83.000000, 11.000000, 92.500000),),
((81.000000, 25.000000, 93.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((94.000000, 16.000000, 62.000000), (87.000000, 6.000000, 58.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((87.000000, 6.000000, 58.000000), (92.000000, 0.000000, 67.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((92.000000, 0.000000, 67.000000), (94.000000, 16.000000, 62.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((90.500000, 11.000000, 60.000000),),
((89.500000, 3.000000, 62.500000),),
((93.000000, 8.000000, 64.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((90.000000, 3.000000, 85.000000), (86.000000, 31.000000, 87.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((86.000000, 31.000000, 87.000000), (96.000000, 12.000000, 78.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((96.000000, 12.000000, 78.000000), (90.000000, 3.000000, 85.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((88.000000, 17.000000, 86.000000),),
((91.000000, 21.500000, 82.500000),),
((93.000000, 7.500000, 81.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((87.000000, 6.000000, 58.000000), (94.000000, 16.000000, 62.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((94.000000, 16.000000, 62.000000), (84.000000, 9.000000, 54.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((84.000000, 9.000000, 54.000000), (87.000000, 6.000000, 58.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((90.500000, 11.000000, 60.000000),),
((89.000000, 12.500000, 58.000000),),
((85.500000, 7.500000, 56.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((81.500000, 38.000000, 65.500000), (85.000000, 35.000000, 77.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((85.000000, 35.000000, 77.000000), (63.000000, 51.000000, 75.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((63.000000, 51.000000, 75.000000), (81.500000, 38.000000, 65.500000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((83.250000, 36.500000, 71.250000),),
((74.000000, 43.000000, 76.000000),),
((72.250000, 44.500000, 70.250000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((85.000000, 35.000000, 77.000000), (66.000000, 48.000000, 90.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((66.000000, 48.000000, 90.000000), (63.000000, 51.000000, 75.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((63.000000, 51.000000, 75.000000), (85.000000, 35.000000, 77.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((75.500000, 41.500000, 83.500000),),
((64.500000, 49.500000, 82.500000),),
((74.000000, 43.000000, 76.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((66.000000, 48.000000, 90.000000), (85.000000, 35.000000, 77.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((85.000000, 35.000000, 77.000000), (86.000000, 34.000000, 86.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((86.000000, 34.000000, 86.000000), (66.000000, 48.000000, 90.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((75.500000, 41.500000, 83.500000),),
((85.500000, 34.500000, 81.500000),),
((76.000000, 41.000000, 88.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((59.000000, 39.000000, 100.000000), (86.000000, 31.000000, 87.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((86.000000, 31.000000, 87.000000), (76.000000, 19.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((76.000000, 19.000000, 100.000000), (59.000000, 39.000000, 100.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((72.500000, 35.000000, 93.500000),),
((81.000000, 25.000000, 93.500000),),
((67.500000, 29.000000, 100.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((86.000000, 34.000000, 86.000000), (86.000000, 31.000000, 87.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((86.000000, 31.000000, 87.000000), (59.000000, 39.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((59.000000, 39.000000, 100.000000), (86.000000, 34.000000, 86.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((86.000000, 32.500000, 86.500000),),
((72.500000, 35.000000, 93.500000),),
((72.500000, 36.500000, 93.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((66.000000, 48.000000, 90.000000), (86.000000, 34.000000, 86.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((86.000000, 34.000000, 86.000000), (59.000000, 39.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((59.000000, 39.000000, 100.000000), (66.000000, 48.000000, 90.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((76.000000, 41.000000, 88.000000),),
((72.500000, 36.500000, 93.000000),),
((62.500000, 43.500000, 95.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((94.000000, 16.000000, 62.000000), (81.500000, 38.000000, 65.500000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((81.500000, 38.000000, 65.500000), (67.000000, 30.000000, 54.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((67.000000, 30.000000, 54.000000), (94.000000, 16.000000, 62.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((87.750000, 27.000000, 63.750000),),
((74.250000, 34.000000, 59.750000),),
((80.500000, 23.000000, 58.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((84.000000, 9.000000, 54.000000), (94.000000, 16.000000, 62.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((94.000000, 16.000000, 62.000000), (67.000000, 30.000000, 54.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((67.000000, 30.000000, 54.000000), (84.000000, 9.000000, 54.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((89.000000, 12.500000, 58.000000),),
((80.500000, 23.000000, 58.000000),),
((75.500000, 19.500000, 54.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((87.000000, 6.000000, 58.000000), (73.000000, 0.000000, 57.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((73.000000, 0.000000, 57.000000), (92.000000, 0.000000, 67.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((92.000000, 0.000000, 67.000000), (87.000000, 6.000000, 58.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((80.000000, 3.000000, 57.500000),),
((82.500000, 0.000000, 62.000000),),
((89.500000, 3.000000, 62.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((73.000000, 0.000000, 57.000000), (87.000000, 6.000000, 58.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((87.000000, 6.000000, 58.000000), (84.000000, 9.000000, 54.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((84.000000, 9.000000, 54.000000), (73.000000, 0.000000, 57.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((80.000000, 3.000000, 57.500000),),
((85.500000, 7.500000, 56.000000),),
((78.500000, 4.500000, 55.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((90.000000, 3.000000, 85.000000), (70.000000, 7.000000, 92.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((70.000000, 7.000000, 92.000000), (76.000000, 19.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((76.000000, 19.000000, 100.000000), (90.000000, 3.000000, 85.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((80.000000, 5.000000, 88.500000),),
((73.000000, 13.000000, 96.000000),),
((83.000000, 11.000000, 92.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((67.000000, 30.000000, 54.000000), (81.500000, 38.000000, 65.500000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((81.500000, 38.000000, 65.500000), (63.000000, 51.000000, 75.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((63.000000, 51.000000, 75.000000), (67.000000, 30.000000, 54.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((74.250000, 34.000000, 59.750000),),
((72.250000, 44.500000, 70.250000),),
((65.000000, 40.500000, 64.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((51.000000, 45.000000, 67.000000), (67.000000, 30.000000, 54.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((67.000000, 30.000000, 54.000000), (63.000000, 51.000000, 75.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((63.000000, 51.000000, 75.000000), (51.000000, 45.000000, 67.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((59.000000, 37.500000, 60.500000),),
((65.000000, 40.500000, 64.500000),),
((57.000000, 48.000000, 71.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((70.000000, 7.000000, 92.000000), (60.000000, 8.000000, 94.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((60.000000, 8.000000, 94.000000), (76.000000, 19.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((76.000000, 19.000000, 100.000000), (70.000000, 7.000000, 92.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((65.000000, 7.500000, 93.000000),),
((68.000000, 13.500000, 97.000000),),
((73.000000, 13.000000, 96.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((89.000000, 0.000000, 81.000000), (65.000000, 0.000000, 83.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((65.000000, 0.000000, 83.000000), (70.000000, 7.000000, 92.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((70.000000, 7.000000, 92.000000), (89.000000, 0.000000, 81.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((77.000000, 0.000000, 82.000000),),
((67.500000, 3.500000, 87.500000),),
((79.500000, 3.500000, 86.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((90.000000, 3.000000, 85.000000), (89.000000, 0.000000, 81.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((89.000000, 0.000000, 81.000000), (70.000000, 7.000000, 92.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((70.000000, 7.000000, 92.000000), (90.000000, 3.000000, 85.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((89.500000, 1.500000, 83.000000),),
((79.500000, 3.500000, 86.500000),),
((80.000000, 5.000000, 88.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((65.000000, 0.000000, 83.000000), (60.000000, 8.000000, 94.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((60.000000, 8.000000, 94.000000), (70.000000, 7.000000, 92.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((70.000000, 7.000000, 92.000000), (65.000000, 0.000000, 83.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((62.500000, 4.000000, 88.500000),),
((65.000000, 7.500000, 93.000000),),
((67.500000, 3.500000, 87.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((92.000000, 0.000000, 67.000000), (73.000000, 0.000000, 57.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((73.000000, 0.000000, 57.000000), (60.000000, 0.000000, 73.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((60.000000, 0.000000, 73.000000), (65.000000, 0.000000, 83.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((65.000000, 0.000000, 83.000000), (89.000000, 0.000000, 81.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((89.000000, 0.000000, 81.000000), (92.000000, 0.000000, 67.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((82.500000, 0.000000, 62.000000),),
((66.500000, 0.000000, 65.000000),),
((62.500000, 0.000000, 78.000000),),
((77.000000, 0.000000, 82.000000),),
((90.500000, 0.000000, 74.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((66.000000, 48.000000, 90.000000), (46.000000, 48.000000, 86.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((46.000000, 48.000000, 86.000000), (63.000000, 51.000000, 75.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((63.000000, 51.000000, 75.000000), (66.000000, 48.000000, 90.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((56.000000, 48.000000, 88.000000),),
((54.500000, 49.500000, 80.500000),),
((64.500000, 49.500000, 82.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((66.000000, 48.000000, 90.000000), (54.000000, 41.000000, 96.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((54.000000, 41.000000, 96.000000), (46.000000, 48.000000, 86.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((46.000000, 48.000000, 86.000000), (66.000000, 48.000000, 90.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((60.000000, 44.500000, 93.000000),),
((50.000000, 44.500000, 91.000000),),
((56.000000, 48.000000, 88.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((54.000000, 41.000000, 96.000000), (66.000000, 48.000000, 90.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((66.000000, 48.000000, 90.000000), (59.000000, 39.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((59.000000, 39.000000, 100.000000), (54.000000, 41.000000, 96.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((60.000000, 44.500000, 93.000000),),
((62.500000, 43.500000, 95.000000),),
((56.500000, 40.000000, 98.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((73.000000, 0.000000, 57.000000), (84.000000, 9.000000, 54.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((84.000000, 9.000000, 54.000000), (67.000000, 30.000000, 54.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((67.000000, 30.000000, 54.000000), (73.000000, 0.000000, 57.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((78.500000, 4.500000, 55.500000),),
((75.500000, 19.500000, 54.000000),),
((70.000000, 15.000000, 55.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((53.500000, 16.000000, 58.500000), (73.000000, 0.000000, 57.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((73.000000, 0.000000, 57.000000), (67.000000, 30.000000, 54.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((67.000000, 30.000000, 54.000000), (53.500000, 16.000000, 58.500000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((63.250000, 8.000000, 57.750000),),
((70.000000, 15.000000, 55.500000),),
((60.250000, 23.000000, 56.250000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((47.000000, 29.000000, 96.000000), (59.000000, 39.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((59.000000, 39.000000, 100.000000), (76.000000, 19.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((76.000000, 19.000000, 100.000000), (47.000000, 29.000000, 96.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((53.000000, 34.000000, 98.000000),),
((67.500000, 29.000000, 100.000000),),
((61.500000, 24.000000, 98.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((60.000000, 8.000000, 94.000000), (47.000000, 29.000000, 96.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((47.000000, 29.000000, 96.000000), (76.000000, 19.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((76.000000, 19.000000, 100.000000), (60.000000, 8.000000, 94.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((53.500000, 18.500000, 95.000000),),
((61.500000, 24.000000, 98.000000),),
((68.000000, 13.500000, 97.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((50.000000, 46.000000, 72.000000), (51.000000, 45.000000, 67.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((51.000000, 45.000000, 67.000000), (63.000000, 51.000000, 75.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((63.000000, 51.000000, 75.000000), (50.000000, 46.000000, 72.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((50.500000, 45.500000, 69.500000),),
((57.000000, 48.000000, 71.000000),),
((56.500000, 48.500000, 73.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((46.000000, 48.000000, 86.000000), (50.000000, 46.000000, 72.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((50.000000, 46.000000, 72.000000), (63.000000, 51.000000, 75.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((63.000000, 51.000000, 75.000000), (46.000000, 48.000000, 86.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((48.000000, 47.000000, 79.000000),),
((56.500000, 48.500000, 73.500000),),
((54.500000, 49.500000, 80.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((60.000000, 8.000000, 94.000000), (65.000000, 0.000000, 83.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((65.000000, 0.000000, 83.000000), (57.000000, 7.000000, 88.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((57.000000, 7.000000, 88.000000), (60.000000, 8.000000, 94.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((62.500000, 4.000000, 88.500000),),
((61.000000, 3.500000, 85.500000),),
((58.500000, 7.500000, 91.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((51.000000, 45.000000, 67.000000), (42.000000, 36.000000, 70.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((42.000000, 36.000000, 70.000000), (67.000000, 30.000000, 54.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((67.000000, 30.000000, 54.000000), (51.000000, 45.000000, 67.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((46.500000, 40.500000, 68.500000),),
((54.500000, 33.000000, 62.000000),),
((59.000000, 37.500000, 60.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((42.000000, 36.000000, 70.000000), (53.500000, 16.000000, 58.500000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((53.500000, 16.000000, 58.500000), (67.000000, 30.000000, 54.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((67.000000, 30.000000, 54.000000), (42.000000, 36.000000, 70.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((47.750000, 26.000000, 64.250000),),
((60.250000, 23.000000, 56.250000),),
((54.500000, 33.000000, 62.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((50.000000, 7.000000, 75.000000), (57.000000, 7.000000, 88.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((57.000000, 7.000000, 88.000000), (60.000000, 0.000000, 73.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((60.000000, 0.000000, 73.000000), (50.000000, 7.000000, 75.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((53.500000, 7.000000, 81.500000),),
((58.500000, 3.500000, 80.500000),),
((55.000000, 3.500000, 74.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((47.000000, 29.000000, 96.000000), (54.000000, 41.000000, 96.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((54.000000, 41.000000, 96.000000), (59.000000, 39.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((59.000000, 39.000000, 100.000000), (47.000000, 29.000000, 96.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((50.500000, 35.000000, 96.000000),),
((56.500000, 40.000000, 98.000000),),
((53.000000, 34.000000, 98.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((57.000000, 7.000000, 88.000000), (65.000000, 0.000000, 83.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((65.000000, 0.000000, 83.000000), (60.000000, 0.000000, 73.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((60.000000, 0.000000, 73.000000), (57.000000, 7.000000, 88.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((61.000000, 3.500000, 85.500000),),
((62.500000, 0.000000, 78.000000),),
((58.500000, 3.500000, 80.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((53.500000, 16.000000, 58.500000), (50.000000, 7.000000, 75.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((50.000000, 7.000000, 75.000000), (60.000000, 0.000000, 73.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((60.000000, 0.000000, 73.000000), (53.500000, 16.000000, 58.500000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((51.750000, 11.500000, 66.750000),),
((55.000000, 3.500000, 74.000000),),
((56.750000, 8.000000, 65.750000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((73.000000, 0.000000, 57.000000), (53.500000, 16.000000, 58.500000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((53.500000, 16.000000, 58.500000), (60.000000, 0.000000, 73.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((60.000000, 0.000000, 73.000000), (73.000000, 0.000000, 57.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((63.250000, 8.000000, 57.750000),),
((56.750000, 8.000000, 65.750000),),
((66.500000, 0.000000, 65.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((54.000000, 41.000000, 96.000000), (41.000000, 34.000000, 85.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((41.000000, 34.000000, 85.000000), (46.000000, 48.000000, 86.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((46.000000, 48.000000, 86.000000), (54.000000, 41.000000, 96.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((47.500000, 37.500000, 90.500000),),
((43.500000, 41.000000, 85.500000),),
((50.000000, 44.500000, 91.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((41.000000, 34.000000, 85.000000), (54.000000, 41.000000, 96.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((54.000000, 41.000000, 96.000000), (47.000000, 29.000000, 96.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((47.000000, 29.000000, 96.000000), (41.000000, 34.000000, 85.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((47.500000, 37.500000, 90.500000),),
((50.500000, 35.000000, 96.000000),),
((44.000000, 31.500000, 90.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((42.000000, 36.000000, 70.000000), (50.000000, 46.000000, 72.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((50.000000, 46.000000, 72.000000), (46.000000, 48.000000, 86.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((46.000000, 48.000000, 86.000000), (42.000000, 36.000000, 70.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((46.000000, 41.000000, 71.000000),),
((48.000000, 47.000000, 79.000000),),
((44.000000, 42.000000, 78.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((50.000000, 46.000000, 72.000000), (42.000000, 36.000000, 70.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((42.000000, 36.000000, 70.000000), (51.000000, 45.000000, 67.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((51.000000, 45.000000, 67.000000), (50.000000, 46.000000, 72.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((46.000000, 41.000000, 71.000000),),
((46.500000, 40.500000, 68.500000),),
((50.500000, 45.500000, 69.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((47.000000, 29.000000, 96.000000), (57.000000, 7.000000, 88.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((57.000000, 7.000000, 88.000000), (40.000000, 27.000000, 83.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((40.000000, 27.000000, 83.000000), (47.000000, 29.000000, 96.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((52.000000, 18.000000, 92.000000),),
((48.500000, 17.000000, 85.500000),),
((43.500000, 28.000000, 89.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((60.000000, 8.000000, 94.000000), (57.000000, 7.000000, 88.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((57.000000, 7.000000, 88.000000), (47.000000, 29.000000, 96.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((47.000000, 29.000000, 96.000000), (60.000000, 8.000000, 94.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((58.500000, 7.500000, 91.000000),),
((52.000000, 18.000000, 92.000000),),
((53.500000, 18.500000, 95.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((57.000000, 7.000000, 88.000000), (50.000000, 7.000000, 75.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((50.000000, 7.000000, 75.000000), (40.000000, 27.000000, 83.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((40.000000, 27.000000, 83.000000), (57.000000, 7.000000, 88.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((53.500000, 7.000000, 81.500000),),
((45.000000, 17.000000, 79.000000),),
((48.500000, 17.000000, 85.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((41.000000, 34.000000, 85.000000), (47.000000, 29.000000, 96.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((47.000000, 29.000000, 96.000000), (40.000000, 27.000000, 83.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((40.000000, 27.000000, 83.000000), (41.000000, 34.000000, 85.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((44.000000, 31.500000, 90.500000),),
((43.500000, 28.000000, 89.500000),),
((40.500000, 30.500000, 84.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((53.500000, 16.000000, 58.500000), (42.000000, 36.000000, 70.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((42.000000, 36.000000, 70.000000), (40.000000, 27.000000, 83.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((40.000000, 27.000000, 83.000000), (53.500000, 16.000000, 58.500000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((47.750000, 26.000000, 64.250000),),
((41.000000, 31.500000, 76.500000),),
((46.750000, 21.500000, 70.750000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((50.000000, 7.000000, 75.000000), (53.500000, 16.000000, 58.500000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((53.500000, 16.000000, 58.500000), (40.000000, 27.000000, 83.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((40.000000, 27.000000, 83.000000), (50.000000, 7.000000, 75.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((51.750000, 11.500000, 66.750000),),
((46.750000, 21.500000, 70.750000),),
((45.000000, 17.000000, 79.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((41.000000, 34.000000, 85.000000), (42.000000, 36.000000, 70.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((42.000000, 36.000000, 70.000000), (46.000000, 48.000000, 86.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((46.000000, 48.000000, 86.000000), (41.000000, 34.000000, 85.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((41.500000, 35.000000, 77.500000),),
((44.000000, 42.000000, 78.000000),),
((43.500000, 41.000000, 85.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((42.000000, 36.000000, 70.000000), (41.000000, 34.000000, 85.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((41.000000, 34.000000, 85.000000), (40.000000, 27.000000, 83.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((40.000000, 27.000000, 83.000000), (42.000000, 36.000000, 70.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((41.500000, 35.000000, 77.500000),),
((40.500000, 30.500000, 84.000000),),
((41.000000, 31.500000, 76.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((43.000000, 58.000000, 83.000000), (44.000000, 64.000000, 72.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((44.000000, 64.000000, 72.000000), (45.000000, 56.000000, 71.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((45.000000, 56.000000, 71.000000), (43.000000, 58.000000, 83.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((43.500000, 61.000000, 77.500000),),
((44.500000, 60.000000, 71.500000),),
((44.000000, 57.000000, 77.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((44.000000, 64.000000, 72.000000), (40.000000, 63.000000, 62.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((40.000000, 63.000000, 62.000000), (45.000000, 56.000000, 71.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((45.000000, 56.000000, 71.000000), (44.000000, 64.000000, 72.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((42.000000, 63.500000, 67.000000),),
((42.500000, 59.500000, 66.500000),),
((44.500000, 60.000000, 71.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((34.500000, 42.500000, 86.500000), (43.000000, 58.000000, 83.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((43.000000, 58.000000, 83.000000), (45.000000, 56.000000, 71.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((45.000000, 56.000000, 71.000000), (34.500000, 42.500000, 86.500000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((38.750000, 50.250000, 84.750000),),
((44.000000, 57.000000, 77.000000),),
((39.750000, 49.250000, 78.750000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((37.000000, 40.000000, 70.000000), (34.500000, 42.500000, 86.500000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((34.500000, 42.500000, 86.500000), (45.000000, 56.000000, 71.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((45.000000, 56.000000, 71.000000), (37.000000, 40.000000, 70.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((35.750000, 41.250000, 78.250000),),
((39.750000, 49.250000, 78.750000),),
((41.000000, 48.000000, 70.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((44.000000, 64.000000, 72.000000), (37.000000, 69.000000, 84.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((37.000000, 69.000000, 84.000000), (40.000000, 73.000000, 73.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((40.000000, 73.000000, 73.000000), (44.000000, 64.000000, 72.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((40.500000, 66.500000, 78.000000),),
((38.500000, 71.000000, 78.500000),),
((42.000000, 68.500000, 72.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((37.000000, 69.000000, 84.000000), (44.000000, 64.000000, 72.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((44.000000, 64.000000, 72.000000), (43.000000, 58.000000, 83.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((43.000000, 58.000000, 83.000000), (37.000000, 69.000000, 84.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((40.500000, 66.500000, 78.000000),),
((43.500000, 61.000000, 77.500000),),
((40.000000, 63.500000, 83.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((44.000000, 64.000000, 72.000000), (40.000000, 73.000000, 73.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((40.000000, 73.000000, 73.000000), (40.000000, 63.000000, 62.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((40.000000, 63.000000, 62.000000), (44.000000, 64.000000, 72.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((42.000000, 68.500000, 72.500000),),
((40.000000, 68.000000, 67.500000),),
((42.000000, 63.500000, 67.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((37.000000, 69.000000, 84.000000), (43.000000, 58.000000, 83.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((43.000000, 58.000000, 83.000000), (36.000000, 67.000000, 87.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((36.000000, 67.000000, 87.000000), (37.000000, 69.000000, 84.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((40.000000, 63.500000, 83.500000),),
((39.500000, 62.500000, 85.000000),),
((36.500000, 68.000000, 85.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((40.000000, 63.000000, 62.000000), (28.500000, 45.000000, 58.500000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((28.500000, 45.000000, 58.500000), (45.000000, 56.000000, 71.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((45.000000, 56.000000, 71.000000), (40.000000, 63.000000, 62.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((34.250000, 54.000000, 60.250000),),
((36.750000, 50.500000, 64.750000),),
((42.500000, 59.500000, 66.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((28.500000, 45.000000, 58.500000), (37.000000, 40.000000, 70.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((37.000000, 40.000000, 70.000000), (45.000000, 56.000000, 71.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((45.000000, 56.000000, 71.000000), (28.500000, 45.000000, 58.500000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((32.750000, 42.500000, 64.250000),),
((41.000000, 48.000000, 70.500000),),
((36.750000, 50.500000, 64.750000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((37.000000, 40.000000, 70.000000), (21.000000, 28.000000, 73.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((21.000000, 28.000000, 73.000000), (34.500000, 42.500000, 86.500000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((34.500000, 42.500000, 86.500000), (37.000000, 40.000000, 70.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((29.000000, 34.000000, 71.500000),),
((27.750000, 35.250000, 79.750000),),
((35.750000, 41.250000, 78.250000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((34.500000, 42.500000, 86.500000), (21.000000, 28.000000, 73.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((21.000000, 28.000000, 73.000000), (19.000000, 30.000000, 84.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((19.000000, 30.000000, 84.000000), (34.500000, 42.500000, 86.500000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((27.750000, 35.250000, 79.750000),),
((20.000000, 29.000000, 78.500000),),
((26.750000, 36.250000, 85.250000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((43.000000, 58.000000, 83.000000), (34.500000, 42.500000, 86.500000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((34.500000, 42.500000, 86.500000), (24.000000, 52.000000, 93.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 52.000000, 93.000000), (43.000000, 58.000000, 83.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((38.750000, 50.250000, 84.750000),),
((29.250000, 47.250000, 89.750000),),
((33.500000, 55.000000, 88.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((36.000000, 67.000000, 87.000000), (43.000000, 58.000000, 83.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((43.000000, 58.000000, 83.000000), (24.000000, 52.000000, 93.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 52.000000, 93.000000), (36.000000, 67.000000, 87.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((39.500000, 62.500000, 85.000000),),
((33.500000, 55.000000, 88.000000),),
((30.000000, 59.500000, 90.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((21.000000, 28.000000, 73.000000), (37.000000, 40.000000, 70.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((37.000000, 40.000000, 70.000000), (16.000000, 32.000000, 64.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((16.000000, 32.000000, 64.000000), (21.000000, 28.000000, 73.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((29.000000, 34.000000, 71.500000),),
((26.500000, 36.000000, 67.000000),),
((18.500000, 30.000000, 68.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((16.000000, 32.000000, 64.000000), (37.000000, 40.000000, 70.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((37.000000, 40.000000, 70.000000), (28.500000, 45.000000, 58.500000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((28.500000, 45.000000, 58.500000), (16.000000, 32.000000, 64.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((26.500000, 36.000000, 67.000000),),
((32.750000, 42.500000, 64.250000),),
((22.250000, 38.500000, 61.250000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((40.000000, 73.000000, 73.000000), (29.000000, 68.000000, 61.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((29.000000, 68.000000, 61.000000), (40.000000, 63.000000, 62.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((40.000000, 63.000000, 62.000000), (40.000000, 73.000000, 73.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((34.500000, 70.500000, 67.000000),),
((34.500000, 65.500000, 61.500000),),
((40.000000, 68.000000, 67.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((37.000000, 69.000000, 84.000000), (27.000000, 73.000000, 82.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((27.000000, 73.000000, 82.000000), (40.000000, 73.000000, 73.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((40.000000, 73.000000, 73.000000), (37.000000, 69.000000, 84.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((32.000000, 71.000000, 83.000000),),
((33.500000, 73.000000, 77.500000),),
((38.500000, 71.000000, 78.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((29.000000, 68.000000, 61.000000), (40.000000, 73.000000, 73.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((40.000000, 73.000000, 73.000000), (26.000000, 74.000000, 69.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((26.000000, 74.000000, 69.000000), (29.000000, 68.000000, 61.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((34.500000, 70.500000, 67.000000),),
((33.000000, 73.500000, 71.000000),),
((27.500000, 71.000000, 65.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((27.000000, 73.000000, 82.000000), (37.000000, 69.000000, 84.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((37.000000, 69.000000, 84.000000), (36.000000, 67.000000, 87.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((36.000000, 67.000000, 87.000000), (27.000000, 73.000000, 82.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((32.000000, 71.000000, 83.000000),),
((36.500000, 68.000000, 85.500000),),
((31.500000, 70.000000, 84.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((34.500000, 42.500000, 86.500000), (19.000000, 30.000000, 84.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((19.000000, 30.000000, 84.000000), (24.000000, 52.000000, 93.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 52.000000, 93.000000), (34.500000, 42.500000, 86.500000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((26.750000, 36.250000, 85.250000),),
((21.500000, 41.000000, 88.500000),),
((29.250000, 47.250000, 89.750000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((40.000000, 63.000000, 62.000000), (29.000000, 68.000000, 61.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((29.000000, 68.000000, 61.000000), (28.500000, 45.000000, 58.500000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((28.500000, 45.000000, 58.500000), (40.000000, 63.000000, 62.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((34.500000, 65.500000, 61.500000),),
((28.750000, 56.500000, 59.750000),),
((34.250000, 54.000000, 60.250000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((29.000000, 68.000000, 61.000000), (16.000000, 55.000000, 58.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((16.000000, 55.000000, 58.000000), (28.500000, 45.000000, 58.500000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((28.500000, 45.000000, 58.500000), (29.000000, 68.000000, 61.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((22.500000, 61.500000, 59.500000),),
((22.250000, 50.000000, 58.250000),),
((28.750000, 56.500000, 59.750000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((40.000000, 73.000000, 73.000000), (27.000000, 73.000000, 82.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((27.000000, 73.000000, 82.000000), (26.000000, 74.000000, 69.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((26.000000, 74.000000, 69.000000), (40.000000, 73.000000, 73.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((33.500000, 73.000000, 77.500000),),
((26.500000, 73.500000, 75.500000),),
((33.000000, 73.500000, 71.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((19.000000, 30.000000, 84.000000), (10.000000, 40.000000, 88.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((10.000000, 40.000000, 88.000000), (24.000000, 52.000000, 93.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 52.000000, 93.000000), (19.000000, 30.000000, 84.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((14.500000, 35.000000, 86.000000),),
((17.000000, 46.000000, 90.500000),),
((21.500000, 41.000000, 88.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((21.000000, 28.000000, 73.000000), (6.000000, 30.000000, 77.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((6.000000, 30.000000, 77.000000), (19.000000, 30.000000, 84.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((19.000000, 30.000000, 84.000000), (21.000000, 28.000000, 73.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((13.500000, 29.000000, 75.000000),),
((12.500000, 30.000000, 80.500000),),
((20.000000, 29.000000, 78.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((15.000000, 64.000000, 85.000000), (36.000000, 67.000000, 87.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((36.000000, 67.000000, 87.000000), (24.000000, 52.000000, 93.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 52.000000, 93.000000), (15.000000, 64.000000, 85.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((25.500000, 65.500000, 86.000000),),
((30.000000, 59.500000, 90.000000),),
((19.500000, 58.000000, 89.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((15.000000, 64.000000, 85.000000), (27.000000, 73.000000, 82.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((27.000000, 73.000000, 82.000000), (36.000000, 67.000000, 87.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((36.000000, 67.000000, 87.000000), (15.000000, 64.000000, 85.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((21.000000, 68.500000, 83.500000),),
((31.500000, 70.000000, 84.500000),),
((25.500000, 65.500000, 86.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((16.000000, 55.000000, 58.000000), (16.000000, 32.000000, 64.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((16.000000, 32.000000, 64.000000), (28.500000, 45.000000, 58.500000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((28.500000, 45.000000, 58.500000), (16.000000, 55.000000, 58.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((16.000000, 43.500000, 61.000000),),
((22.250000, 38.500000, 61.250000),),
((22.250000, 50.000000, 58.250000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((12.000000, 61.000000, 86.000000), (15.000000, 64.000000, 85.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((15.000000, 64.000000, 85.000000), (24.000000, 52.000000, 93.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 52.000000, 93.000000), (12.000000, 61.000000, 86.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((13.500000, 62.500000, 85.500000),),
((19.500000, 58.000000, 89.000000),),
((18.000000, 56.500000, 89.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((6.000000, 39.000000, 64.000000), (16.000000, 32.000000, 64.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((16.000000, 32.000000, 64.000000), (16.000000, 55.000000, 58.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((16.000000, 55.000000, 58.000000), (6.000000, 39.000000, 64.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((11.000000, 35.500000, 64.000000),),
((16.000000, 43.500000, 61.000000),),
((11.000000, 47.000000, 61.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((6.000000, 30.000000, 77.000000), (21.000000, 28.000000, 73.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((21.000000, 28.000000, 73.000000), (16.000000, 32.000000, 64.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((16.000000, 32.000000, 64.000000), (6.000000, 30.000000, 77.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((13.500000, 29.000000, 75.000000),),
((18.500000, 30.000000, 68.500000),),
((11.000000, 31.000000, 70.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((6.000000, 30.000000, 77.000000), (10.000000, 40.000000, 88.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((10.000000, 40.000000, 88.000000), (19.000000, 30.000000, 84.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((19.000000, 30.000000, 84.000000), (6.000000, 30.000000, 77.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((8.000000, 35.000000, 82.500000),),
((14.500000, 35.000000, 86.000000),),
((12.500000, 30.000000, 80.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((6.000000, 39.000000, 64.000000), (6.000000, 36.000000, 67.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((6.000000, 36.000000, 67.000000), (16.000000, 32.000000, 64.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((16.000000, 32.000000, 64.000000), (6.000000, 39.000000, 64.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((6.000000, 37.500000, 65.500000),),
((11.000000, 34.000000, 65.500000),),
((11.000000, 35.500000, 64.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((6.000000, 36.000000, 67.000000), (6.000000, 30.000000, 77.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((6.000000, 30.000000, 77.000000), (16.000000, 32.000000, 64.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((16.000000, 32.000000, 64.000000), (6.000000, 36.000000, 67.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((6.000000, 33.000000, 72.000000),),
((11.000000, 31.000000, 70.500000),),
((11.000000, 34.000000, 65.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((10.500000, 63.500000, 69.500000), (29.000000, 68.000000, 61.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((29.000000, 68.000000, 61.000000), (26.000000, 74.000000, 69.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((26.000000, 74.000000, 69.000000), (10.500000, 63.500000, 69.500000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((19.750000, 65.750000, 65.250000),),
((27.500000, 71.000000, 65.000000),),
((18.250000, 68.750000, 69.250000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((29.000000, 68.000000, 61.000000), (10.500000, 63.500000, 69.500000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((10.500000, 63.500000, 69.500000), (16.000000, 55.000000, 58.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((16.000000, 55.000000, 58.000000), (29.000000, 68.000000, 61.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((19.750000, 65.750000, 65.250000),),
((13.250000, 59.250000, 63.750000),),
((22.500000, 61.500000, 59.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((10.000000, 40.000000, 88.000000), (9.000000, 56.000000, 83.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((9.000000, 56.000000, 83.000000), (24.000000, 52.000000, 93.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 52.000000, 93.000000), (10.000000, 40.000000, 88.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((9.500000, 48.000000, 85.500000),),
((16.500000, 54.000000, 88.000000),),
((17.000000, 46.000000, 90.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((27.000000, 73.000000, 82.000000), (13.000000, 64.000000, 79.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((13.000000, 64.000000, 79.000000), (26.000000, 74.000000, 69.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((26.000000, 74.000000, 69.000000), (27.000000, 73.000000, 82.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((20.000000, 68.500000, 80.500000),),
((19.500000, 69.000000, 74.000000),),
((26.500000, 73.500000, 75.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((13.000000, 64.000000, 79.000000), (10.500000, 63.500000, 69.500000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((10.500000, 63.500000, 69.500000), (26.000000, 74.000000, 69.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((26.000000, 74.000000, 69.000000), (13.000000, 64.000000, 79.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((11.750000, 63.750000, 74.250000),),
((18.250000, 68.750000, 69.250000),),
((19.500000, 69.000000, 74.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((27.000000, 73.000000, 82.000000), (15.000000, 64.000000, 85.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((15.000000, 64.000000, 85.000000), (13.000000, 64.000000, 79.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((13.000000, 64.000000, 79.000000), (27.000000, 73.000000, 82.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((21.000000, 68.500000, 83.500000),),
((14.000000, 64.000000, 82.000000),),
((20.000000, 68.500000, 80.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((9.000000, 56.000000, 83.000000), (12.000000, 61.000000, 86.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((12.000000, 61.000000, 86.000000), (24.000000, 52.000000, 93.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 52.000000, 93.000000), (9.000000, 56.000000, 83.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((10.500000, 58.500000, 84.500000),),
((18.000000, 56.500000, 89.500000),),
((16.500000, 54.000000, 88.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((15.000000, 64.000000, 85.000000), (12.000000, 61.000000, 86.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((12.000000, 61.000000, 86.000000), (13.000000, 64.000000, 79.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((13.000000, 64.000000, 79.000000), (15.000000, 64.000000, 85.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((13.500000, 62.500000, 85.500000),),
((12.500000, 62.500000, 82.500000),),
((14.000000, 64.000000, 82.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((6.000000, 39.000000, 64.000000), (16.000000, 55.000000, 58.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((16.000000, 55.000000, 58.000000), (0.000000, 45.000000, 72.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 45.000000, 72.000000), (6.000000, 39.000000, 64.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((11.000000, 47.000000, 61.000000),),
((8.000000, 50.000000, 65.000000),),
((3.000000, 42.000000, 68.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((16.000000, 55.000000, 58.000000), (10.500000, 63.500000, 69.500000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((10.500000, 63.500000, 69.500000), (0.000000, 45.000000, 72.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 45.000000, 72.000000), (16.000000, 55.000000, 58.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((13.250000, 59.250000, 63.750000),),
((5.250000, 54.250000, 70.750000),),
((8.000000, 50.000000, 65.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((9.000000, 56.000000, 83.000000), (10.000000, 40.000000, 88.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((10.000000, 40.000000, 88.000000), (0.000000, 45.000000, 72.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 45.000000, 72.000000), (9.000000, 56.000000, 83.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((9.500000, 48.000000, 85.500000),),
((5.000000, 42.500000, 80.000000),),
((4.500000, 50.500000, 77.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((9.000000, 56.000000, 83.000000), (10.500000, 63.500000, 69.500000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((10.500000, 63.500000, 69.500000), (13.000000, 64.000000, 79.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((13.000000, 64.000000, 79.000000), (9.000000, 56.000000, 83.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((9.750000, 59.750000, 76.250000),),
((11.750000, 63.750000, 74.250000),),
((11.000000, 60.000000, 81.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((10.500000, 63.500000, 69.500000), (9.000000, 56.000000, 83.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((9.000000, 56.000000, 83.000000), (0.000000, 45.000000, 72.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 45.000000, 72.000000), (10.500000, 63.500000, 69.500000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((9.750000, 59.750000, 76.250000),),
((4.500000, 50.500000, 77.500000),),
((5.250000, 54.250000, 70.750000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((6.000000, 36.000000, 67.000000), (6.000000, 39.000000, 64.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((6.000000, 39.000000, 64.000000), (0.000000, 45.000000, 72.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 45.000000, 72.000000), (6.000000, 36.000000, 67.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((6.000000, 37.500000, 65.500000),),
((3.000000, 42.000000, 68.000000),),
((3.000000, 40.500000, 69.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((10.000000, 40.000000, 88.000000), (6.000000, 30.000000, 77.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((6.000000, 30.000000, 77.000000), (0.000000, 45.000000, 72.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 45.000000, 72.000000), (10.000000, 40.000000, 88.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((8.000000, 35.000000, 82.500000),),
((3.000000, 37.500000, 74.500000),),
((5.000000, 42.500000, 80.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((6.000000, 30.000000, 77.000000), (6.000000, 36.000000, 67.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((6.000000, 36.000000, 67.000000), (0.000000, 45.000000, 72.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 45.000000, 72.000000), (6.000000, 30.000000, 77.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((6.000000, 33.000000, 72.000000),),
((3.000000, 40.500000, 69.500000),),
((3.000000, 37.500000, 74.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((12.000000, 61.000000, 86.000000), (9.000000, 56.000000, 83.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((9.000000, 56.000000, 83.000000), (13.000000, 64.000000, 79.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((13.000000, 64.000000, 79.000000), (12.000000, 61.000000, 86.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((10.500000, 58.500000, 84.500000),),
((11.000000, 60.000000, 81.000000),),
((12.500000, 62.500000, 82.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((21.000000, 87.000000, 69.000000), (21.000000, 85.000000, 65.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((21.000000, 85.000000, 65.000000), (24.000000, 80.000000, 72.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 80.000000, 72.000000), (21.000000, 87.000000, 69.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((21.000000, 86.000000, 67.000000),),
((22.500000, 82.500000, 68.500000),),
((22.500000, 83.500000, 70.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((21.000000, 85.000000, 65.000000), (20.000000, 75.000000, 65.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((20.000000, 75.000000, 65.000000), (24.000000, 80.000000, 72.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 80.000000, 72.000000), (21.000000, 85.000000, 65.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((20.500000, 80.000000, 65.000000),),
((22.000000, 77.500000, 68.500000),),
((22.500000, 82.500000, 68.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((21.000000, 85.000000, 65.000000), (21.000000, 87.000000, 69.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((21.000000, 87.000000, 69.000000), (19.000000, 89.000000, 68.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((19.000000, 89.000000, 68.000000), (21.000000, 85.000000, 65.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((21.000000, 86.000000, 67.000000),),
((20.000000, 88.000000, 68.500000),),
((20.000000, 87.000000, 66.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((20.000000, 75.000000, 65.000000), (19.000000, 75.000000, 77.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((19.000000, 75.000000, 77.000000), (24.000000, 80.000000, 72.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 80.000000, 72.000000), (20.000000, 75.000000, 65.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((19.500000, 75.000000, 71.000000),),
((21.500000, 77.500000, 74.500000),),
((22.000000, 77.500000, 68.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((20.000000, 75.000000, 65.000000), (21.000000, 85.000000, 65.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((21.000000, 85.000000, 65.000000), (16.000000, 81.000000, 61.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((16.000000, 81.000000, 61.000000), (20.000000, 75.000000, 65.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((20.500000, 80.000000, 65.000000),),
((18.500000, 83.000000, 63.000000),),
((18.000000, 78.000000, 63.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((9.000000, 84.000000, 58.000000), (16.000000, 81.000000, 61.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((16.000000, 81.000000, 61.000000), (11.000000, 91.000000, 65.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((11.000000, 91.000000, 65.000000), (9.000000, 84.000000, 58.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((12.500000, 82.500000, 59.500000),),
((13.500000, 86.000000, 63.000000),),
((10.000000, 87.500000, 61.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((19.000000, 75.000000, 77.000000), (8.000000, 83.000000, 80.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((8.000000, 83.000000, 80.000000), (24.000000, 80.000000, 72.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 80.000000, 72.000000), (19.000000, 75.000000, 77.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((13.500000, 79.000000, 78.500000),),
((16.000000, 81.500000, 76.000000),),
((21.500000, 77.500000, 74.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((8.000000, 83.000000, 80.000000), (21.000000, 87.000000, 69.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((21.000000, 87.000000, 69.000000), (24.000000, 80.000000, 72.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 80.000000, 72.000000), (8.000000, 83.000000, 80.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((14.500000, 85.000000, 74.500000),),
((22.500000, 83.500000, 70.500000),),
((16.000000, 81.500000, 76.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((7.000000, 91.000000, 75.000000), (21.000000, 87.000000, 69.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((21.000000, 87.000000, 69.000000), (8.000000, 83.000000, 80.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((8.000000, 83.000000, 80.000000), (7.000000, 91.000000, 75.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((14.000000, 89.000000, 72.000000),),
((14.500000, 85.000000, 74.500000),),
((7.500000, 87.000000, 77.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((10.000000, 74.000000, 60.000000), (20.000000, 75.000000, 65.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((20.000000, 75.000000, 65.000000), (16.000000, 81.000000, 61.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((16.000000, 81.000000, 61.000000), (10.000000, 74.000000, 60.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((15.000000, 74.500000, 62.500000),),
((18.000000, 78.000000, 63.000000),),
((13.000000, 77.500000, 60.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((21.000000, 87.000000, 69.000000), (7.000000, 91.000000, 75.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((7.000000, 91.000000, 75.000000), (19.000000, 89.000000, 68.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((19.000000, 89.000000, 68.000000), (21.000000, 87.000000, 69.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((14.000000, 89.000000, 72.000000),),
((13.000000, 90.000000, 71.500000),),
((20.000000, 88.000000, 68.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((19.000000, 75.000000, 77.000000), (20.000000, 75.000000, 65.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((20.000000, 75.000000, 65.000000), (7.000000, 69.000000, 69.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((7.000000, 69.000000, 69.000000), (19.000000, 75.000000, 77.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((19.500000, 75.000000, 71.000000),),
((13.500000, 72.000000, 67.000000),),
((13.000000, 72.000000, 73.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((21.000000, 85.000000, 65.000000), (19.000000, 89.000000, 68.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((19.000000, 89.000000, 68.000000), (11.000000, 91.000000, 65.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((11.000000, 91.000000, 65.000000), (21.000000, 85.000000, 65.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((20.000000, 87.000000, 66.500000),),
((15.000000, 90.000000, 66.500000),),
((16.000000, 88.000000, 65.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((9.000000, 84.000000, 58.000000), (10.000000, 74.000000, 60.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((10.000000, 74.000000, 60.000000), (16.000000, 81.000000, 61.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((16.000000, 81.000000, 61.000000), (9.000000, 84.000000, 58.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((9.500000, 79.000000, 59.000000),),
((13.000000, 77.500000, 60.500000),),
((12.500000, 82.500000, 59.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((16.000000, 81.000000, 61.000000), (21.000000, 85.000000, 65.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((21.000000, 85.000000, 65.000000), (11.000000, 91.000000, 65.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((11.000000, 91.000000, 65.000000), (16.000000, 81.000000, 61.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((18.500000, 83.000000, 63.000000),),
((16.000000, 88.000000, 65.000000),),
((13.500000, 86.000000, 63.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((20.000000, 75.000000, 65.000000), (10.000000, 74.000000, 60.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((10.000000, 74.000000, 60.000000), (7.000000, 69.000000, 69.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((7.000000, 69.000000, 69.000000), (20.000000, 75.000000, 65.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((15.000000, 74.500000, 62.500000),),
((8.500000, 71.500000, 64.500000),),
((13.500000, 72.000000, 67.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((19.000000, 89.000000, 68.000000), (7.000000, 91.000000, 75.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((7.000000, 91.000000, 75.000000), (11.000000, 91.000000, 65.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((11.000000, 91.000000, 65.000000), (19.000000, 89.000000, 68.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((13.000000, 90.000000, 71.500000),),
((9.000000, 91.000000, 70.000000),),
((15.000000, 90.000000, 66.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((6.000000, 73.000000, 78.000000), (19.000000, 75.000000, 77.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((19.000000, 75.000000, 77.000000), (7.000000, 69.000000, 69.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((7.000000, 69.000000, 69.000000), (6.000000, 73.000000, 78.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((12.500000, 74.000000, 77.500000),),
((13.000000, 72.000000, 73.000000),),
((6.500000, 71.000000, 73.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((19.000000, 75.000000, 77.000000), (6.000000, 73.000000, 78.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((6.000000, 73.000000, 78.000000), (8.000000, 83.000000, 80.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((8.000000, 83.000000, 80.000000), (19.000000, 75.000000, 77.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((12.500000, 74.000000, 77.500000),),
((7.000000, 78.000000, 79.000000),),
((13.500000, 79.000000, 78.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 90.000000, 64.000000), (9.000000, 84.000000, 58.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((9.000000, 84.000000, 58.000000), (11.000000, 91.000000, 65.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((11.000000, 91.000000, 65.000000), (0.000000, 90.000000, 64.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((4.500000, 87.000000, 61.000000),),
((10.000000, 87.500000, 61.500000),),
((5.500000, 90.500000, 64.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((10.000000, 74.000000, 60.000000), (9.000000, 84.000000, 58.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((9.000000, 84.000000, 58.000000), (0.000000, 76.000000, 60.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 76.000000, 60.000000), (10.000000, 74.000000, 60.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((9.500000, 79.000000, 59.000000),),
((4.500000, 80.000000, 59.000000),),
((5.000000, 75.000000, 60.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 90.000000, 73.000000), (0.000000, 90.000000, 64.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 90.000000, 64.000000), (11.000000, 91.000000, 65.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((11.000000, 91.000000, 65.000000), (0.000000, 90.000000, 73.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((0.000000, 90.000000, 68.500000),),
((5.500000, 90.500000, 64.500000),),
((5.500000, 90.500000, 69.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 76.000000, 60.000000), (9.000000, 84.000000, 58.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((9.000000, 84.000000, 58.000000), (0.000000, 83.000000, 59.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 83.000000, 59.000000), (0.000000, 76.000000, 60.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((4.500000, 80.000000, 59.000000),),
((4.500000, 83.500000, 58.500000),),
((0.000000, 79.500000, 59.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 83.000000, 79.000000), (7.000000, 91.000000, 75.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((7.000000, 91.000000, 75.000000), (8.000000, 83.000000, 80.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((8.000000, 83.000000, 80.000000), (0.000000, 83.000000, 79.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((3.500000, 87.000000, 77.000000),),
((7.500000, 87.000000, 77.500000),),
((4.000000, 83.000000, 79.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((6.000000, 73.000000, 78.000000), (0.000000, 83.000000, 79.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 83.000000, 79.000000), (8.000000, 83.000000, 80.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((8.000000, 83.000000, 80.000000), (6.000000, 73.000000, 78.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((3.000000, 78.000000, 78.500000),),
((4.000000, 83.000000, 79.500000),),
((7.000000, 78.000000, 79.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((7.000000, 91.000000, 75.000000), (0.000000, 90.000000, 73.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 90.000000, 73.000000), (11.000000, 91.000000, 65.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((11.000000, 91.000000, 65.000000), (7.000000, 91.000000, 75.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((3.500000, 90.500000, 74.000000),),
((5.500000, 90.500000, 69.000000),),
((9.000000, 91.000000, 70.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 73.000000, 76.000000), (6.000000, 73.000000, 78.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((6.000000, 73.000000, 78.000000), (7.000000, 69.000000, 69.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((7.000000, 69.000000, 69.000000), (0.000000, 73.000000, 76.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((3.000000, 73.000000, 77.000000),),
((6.500000, 71.000000, 73.500000),),
((3.500000, 71.000000, 72.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((9.000000, 84.000000, 58.000000), (0.000000, 90.000000, 64.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 90.000000, 64.000000), (0.000000, 83.000000, 59.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 83.000000, 59.000000), (9.000000, 84.000000, 58.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((4.500000, 87.000000, 61.000000),),
((0.000000, 86.500000, 61.500000),),
((4.500000, 83.500000, 58.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((10.000000, 74.000000, 60.000000), (0.000000, 76.000000, 60.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 76.000000, 60.000000), (7.000000, 69.000000, 69.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((7.000000, 69.000000, 69.000000), (10.000000, 74.000000, 60.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((5.000000, 75.000000, 60.000000),),
((3.500000, 72.500000, 64.500000),),
((8.500000, 71.500000, 64.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 76.000000, 60.000000), (0.000000, 71.000000, 69.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 71.000000, 69.000000), (7.000000, 69.000000, 69.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((7.000000, 69.000000, 69.000000), (0.000000, 76.000000, 60.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((0.000000, 73.500000, 64.500000),),
((3.500000, 70.000000, 69.000000),),
((3.500000, 72.500000, 64.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 71.000000, 69.000000), (0.000000, 73.000000, 76.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 73.000000, 76.000000), (7.000000, 69.000000, 69.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((7.000000, 69.000000, 69.000000), (0.000000, 71.000000, 69.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((0.000000, 72.000000, 72.500000),),
((3.500000, 71.000000, 72.500000),),
((3.500000, 70.000000, 69.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((7.000000, 91.000000, 75.000000), (0.000000, 83.000000, 79.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 83.000000, 79.000000), (0.000000, 90.000000, 73.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 90.000000, 73.000000), (7.000000, 91.000000, 75.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((3.500000, 87.000000, 77.000000),),
((0.000000, 86.500000, 76.000000),),
((3.500000, 90.500000, 74.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 83.000000, 79.000000), (6.000000, 73.000000, 78.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((6.000000, 73.000000, 78.000000), (0.000000, 73.000000, 76.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 73.000000, 76.000000), (0.000000, 83.000000, 79.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((3.000000, 78.000000, 78.500000),),
((3.000000, 73.000000, 77.000000),),
((0.000000, 78.000000, 77.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((0.000000, 83.000000, 59.000000), (0.000000, 90.000000, 64.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 90.000000, 64.000000), (0.000000, 90.000000, 73.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 90.000000, 73.000000), (0.000000, 83.000000, 79.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 83.000000, 79.000000), (0.000000, 73.000000, 76.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 73.000000, 76.000000), (0.000000, 71.000000, 69.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 71.000000, 69.000000), (0.000000, 76.000000, 60.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((0.000000, 76.000000, 60.000000), (0.000000, 83.000000, 59.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((0.000000, 86.500000, 61.500000),),
((0.000000, 90.000000, 68.500000),),
((0.000000, 86.500000, 76.000000),),
((0.000000, 78.000000, 77.500000),),
((0.000000, 72.000000, 72.500000),),
((0.000000, 73.500000, 64.500000),),
((0.000000, 79.500000, 59.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((41.000000, 4.000000, 72.000000), (40.000000, 0.000000, 70.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((40.000000, 0.000000, 70.000000), (45.000000, 6.000000, 81.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((45.000000, 6.000000, 81.000000), (41.000000, 4.000000, 72.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((40.500000, 2.000000, 71.000000),),
((42.500000, 3.000000, 75.500000),),
((43.000000, 5.000000, 76.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((40.000000, 0.000000, 70.000000), (44.000000, 0.000000, 90.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((44.000000, 0.000000, 90.000000), (45.000000, 6.000000, 81.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((45.000000, 6.000000, 81.000000), (40.000000, 0.000000, 70.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((42.000000, 0.000000, 80.000000),),
((44.500000, 3.000000, 85.500000),),
((42.500000, 3.000000, 75.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((44.000000, 0.000000, 90.000000), (40.000000, 11.000000, 83.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((40.000000, 11.000000, 83.000000), (45.000000, 6.000000, 81.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((45.000000, 6.000000, 81.000000), (44.000000, 0.000000, 90.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((42.000000, 5.500000, 86.500000),),
((42.500000, 8.500000, 82.000000),),
((44.500000, 3.000000, 85.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((40.000000, 11.000000, 83.000000), (44.000000, 0.000000, 90.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((44.000000, 0.000000, 90.000000), (30.000000, 11.000000, 97.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((30.000000, 11.000000, 97.000000), (40.000000, 11.000000, 83.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((42.000000, 5.500000, 86.500000),),
((37.000000, 5.500000, 93.500000),),
((35.000000, 11.000000, 90.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((40.000000, 11.000000, 83.000000), (41.000000, 4.000000, 72.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((41.000000, 4.000000, 72.000000), (45.000000, 6.000000, 81.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((45.000000, 6.000000, 81.000000), (40.000000, 11.000000, 83.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((40.500000, 7.500000, 77.500000),),
((43.000000, 5.000000, 76.500000),),
((42.500000, 8.500000, 82.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((30.000000, 11.000000, 97.000000), (44.000000, 0.000000, 90.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((44.000000, 0.000000, 90.000000), (28.000000, 0.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((28.000000, 0.000000, 100.000000), (30.000000, 11.000000, 97.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((37.000000, 5.500000, 93.500000),),
((36.000000, 0.000000, 95.000000),),
((29.000000, 5.500000, 98.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((40.000000, 11.000000, 83.000000), (30.000000, 11.000000, 97.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((30.000000, 11.000000, 97.000000), (24.000000, 20.000000, 87.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 20.000000, 87.000000), (40.000000, 11.000000, 83.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((35.000000, 11.000000, 90.000000),),
((27.000000, 15.500000, 92.000000),),
((32.000000, 15.500000, 85.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((41.000000, 4.000000, 72.000000), (40.000000, 11.000000, 83.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((40.000000, 11.000000, 83.000000), (24.000000, 20.000000, 87.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 20.000000, 87.000000), (41.000000, 4.000000, 72.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((40.500000, 7.500000, 77.500000),),
((32.000000, 15.500000, 85.000000),),
((32.500000, 12.000000, 79.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((13.000000, 19.000000, 78.000000), (41.000000, 4.000000, 72.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((41.000000, 4.000000, 72.000000), (24.000000, 20.000000, 87.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 20.000000, 87.000000), (13.000000, 19.000000, 78.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((27.000000, 11.500000, 75.000000),),
((32.500000, 12.000000, 79.500000),),
((18.500000, 19.500000, 82.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((30.000000, 11.000000, 97.000000), (13.000000, 21.000000, 89.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((13.000000, 21.000000, 89.000000), (24.000000, 20.000000, 87.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 20.000000, 87.000000), (30.000000, 11.000000, 97.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((21.500000, 16.000000, 93.000000),),
((18.500000, 20.500000, 88.000000),),
((27.000000, 15.500000, 92.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((40.000000, 0.000000, 70.000000), (41.000000, 4.000000, 72.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((41.000000, 4.000000, 72.000000), (19.000000, 0.000000, 67.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((19.000000, 0.000000, 67.000000), (40.000000, 0.000000, 70.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((40.500000, 2.000000, 71.000000),),
((30.000000, 2.000000, 69.500000),),
((29.500000, 0.000000, 68.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((30.000000, 11.000000, 97.000000), (16.000000, 0.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((16.000000, 0.000000, 100.000000), (8.000000, 6.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((8.000000, 6.000000, 100.000000), (30.000000, 11.000000, 97.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((23.000000, 5.500000, 98.500000),),
((12.000000, 3.000000, 100.000000),),
((19.000000, 8.500000, 98.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((41.000000, 4.000000, 72.000000), (13.000000, 19.000000, 78.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((13.000000, 19.000000, 78.000000), (19.000000, 0.000000, 67.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((19.000000, 0.000000, 67.000000), (41.000000, 4.000000, 72.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((27.000000, 11.500000, 75.000000),),
((16.000000, 9.500000, 72.500000),),
((30.000000, 2.000000, 69.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((13.000000, 21.000000, 89.000000), (13.000000, 19.000000, 78.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((13.000000, 19.000000, 78.000000), (24.000000, 20.000000, 87.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((24.000000, 20.000000, 87.000000), (13.000000, 21.000000, 89.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((13.000000, 20.000000, 83.500000),),
((18.500000, 19.500000, 82.500000),),
((18.500000, 20.500000, 88.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((16.000000, 0.000000, 100.000000), (30.000000, 11.000000, 97.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((30.000000, 11.000000, 97.000000), (28.000000, 0.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((28.000000, 0.000000, 100.000000), (16.000000, 0.000000, 100.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((23.000000, 5.500000, 98.500000),),
((29.000000, 5.500000, 98.500000),),
((22.000000, 0.000000, 100.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((44.000000, 0.000000, 90.000000), (40.000000, 0.000000, 70.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((40.000000, 0.000000, 70.000000), (19.000000, 0.000000, 67.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((19.000000, 0.000000, 67.000000), (5.000000, 0.000000, 79.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((5.000000, 0.000000, 79.000000), (3.000000, 0.000000, 88.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((3.000000, 0.000000, 88.000000), (16.000000, 0.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((16.000000, 0.000000, 100.000000), (28.000000, 0.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((28.000000, 0.000000, 100.000000), (44.000000, 0.000000, 90.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((42.000000, 0.000000, 80.000000),),
((29.500000, 0.000000, 68.500000),),
((12.000000, 0.000000, 73.000000),),
((4.000000, 0.000000, 83.500000),),
((9.500000, 0.000000, 94.000000),),
((22.000000, 0.000000, 100.000000),),
((36.000000, 0.000000, 95.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((13.000000, 21.000000, 89.000000), (30.000000, 11.000000, 97.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((30.000000, 11.000000, 97.000000), (8.000000, 6.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((8.000000, 6.000000, 100.000000), (13.000000, 21.000000, 89.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((21.500000, 16.000000, 93.000000),),
((19.000000, 8.500000, 98.500000),),
((10.500000, 13.500000, 94.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((13.000000, 19.000000, 78.000000), (5.000000, 11.000000, 75.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((5.000000, 11.000000, 75.000000), (19.000000, 0.000000, 67.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((19.000000, 0.000000, 67.000000), (13.000000, 19.000000, 78.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((9.000000, 15.000000, 76.500000),),
((12.000000, 5.500000, 71.000000),),
((16.000000, 9.500000, 72.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((8.000000, 6.000000, 100.000000), (16.000000, 0.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((16.000000, 0.000000, 100.000000), (3.000000, 0.000000, 88.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((3.000000, 0.000000, 88.000000), (8.000000, 6.000000, 100.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((12.000000, 3.000000, 100.000000),),
((9.500000, 0.000000, 94.000000),),
((5.500000, 3.000000, 94.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((5.000000, 11.000000, 75.000000), (5.000000, 0.000000, 79.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((5.000000, 0.000000, 79.000000), (19.000000, 0.000000, 67.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((19.000000, 0.000000, 67.000000), (5.000000, 11.000000, 75.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((5.000000, 5.500000, 77.000000),),
((12.000000, 0.000000, 73.000000),),
((12.000000, 5.500000, 71.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((13.000000, 21.000000, 89.000000), (5.000000, 11.000000, 75.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((5.000000, 11.000000, 75.000000), (13.000000, 19.000000, 78.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((13.000000, 19.000000, 78.000000), (13.000000, 21.000000, 89.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((9.000000, 16.000000, 82.000000),),
((9.000000, 15.000000, 76.500000),),
((13.000000, 20.000000, 83.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((5.000000, 11.000000, 75.000000), (13.000000, 21.000000, 89.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((13.000000, 21.000000, 89.000000), (3.000000, 0.000000, 88.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((3.000000, 0.000000, 88.000000), (5.000000, 11.000000, 75.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((9.000000, 16.000000, 82.000000),),
((8.000000, 10.500000, 88.500000),),
((4.000000, 5.500000, 81.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((13.000000, 21.000000, 89.000000), (8.000000, 6.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((8.000000, 6.000000, 100.000000), (3.000000, 0.000000, 88.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((3.000000, 0.000000, 88.000000), (13.000000, 21.000000, 89.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((10.500000, 13.500000, 94.500000),),
((5.500000, 3.000000, 94.000000),),
((8.000000, 10.500000, 88.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((5.000000, 0.000000, 79.000000), (5.000000, 11.000000, 75.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((5.000000, 11.000000, 75.000000), (3.000000, 0.000000, 88.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((3.000000, 0.000000, 88.000000), (5.000000, 0.000000, 79.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((5.000000, 5.500000, 77.000000),),
((4.000000, 5.500000, 81.500000),),
((4.000000, 0.000000, 83.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((39.000000, 100.000000, 70.000000), (40.000000, 91.000000, 91.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((40.000000, 91.000000, 91.000000), (42.000000, 100.000000, 91.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((42.000000, 100.000000, 91.000000), (39.000000, 100.000000, 70.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((39.500000, 95.500000, 80.500000),),
((41.000000, 95.500000, 91.000000),),
((40.500000, 100.000000, 80.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((39.000000, 100.000000, 70.000000), (34.000000, 87.000000, 73.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((34.000000, 87.000000, 73.000000), (35.000000, 85.000000, 84.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((35.000000, 85.000000, 84.000000), (39.000000, 100.000000, 70.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((36.500000, 93.500000, 71.500000),),
((34.500000, 86.000000, 78.500000),),
((37.000000, 92.500000, 77.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((40.000000, 91.000000, 91.000000), (39.000000, 100.000000, 70.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((39.000000, 100.000000, 70.000000), (35.000000, 85.000000, 84.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((35.000000, 85.000000, 84.000000), (40.000000, 91.000000, 91.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((39.500000, 95.500000, 80.500000),),
((37.000000, 92.500000, 77.000000),),
((37.500000, 88.000000, 87.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((28.000000, 100.000000, 68.000000), (32.000000, 96.000000, 68.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((32.000000, 96.000000, 68.000000), (31.000000, 100.000000, 70.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((31.000000, 100.000000, 70.000000), (28.000000, 100.000000, 68.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((30.000000, 98.000000, 68.000000),),
((31.500000, 98.000000, 69.000000),),
((29.500000, 100.000000, 69.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((32.000000, 96.000000, 68.000000), (34.000000, 87.000000, 73.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((34.000000, 87.000000, 73.000000), (39.000000, 100.000000, 70.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((39.000000, 100.000000, 70.000000), (32.000000, 96.000000, 68.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((33.000000, 91.500000, 70.500000),),
((36.500000, 93.500000, 71.500000),),
((35.500000, 98.000000, 69.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((40.000000, 91.000000, 91.000000), (20.000000, 100.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((20.000000, 100.000000, 100.000000), (42.000000, 100.000000, 91.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((42.000000, 100.000000, 91.000000), (40.000000, 91.000000, 91.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((30.000000, 95.500000, 95.500000),),
((31.000000, 100.000000, 95.500000),),
((41.000000, 95.500000, 91.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((18.000000, 89.000000, 90.000000), (40.000000, 91.000000, 91.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((40.000000, 91.000000, 91.000000), (35.000000, 85.000000, 84.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((35.000000, 85.000000, 84.000000), (18.000000, 89.000000, 90.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((29.000000, 90.000000, 90.500000),),
((37.500000, 88.000000, 87.500000),),
((26.500000, 87.000000, 87.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((40.000000, 91.000000, 91.000000), (18.000000, 89.000000, 90.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((18.000000, 89.000000, 90.000000), (20.000000, 100.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((20.000000, 100.000000, 100.000000), (40.000000, 91.000000, 91.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((29.000000, 90.000000, 90.500000),),
((19.000000, 94.500000, 95.000000),),
((30.000000, 95.500000, 95.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((5.000000, 100.000000, 91.000000), (20.000000, 100.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((20.000000, 100.000000, 100.000000), (42.000000, 100.000000, 91.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((42.000000, 100.000000, 91.000000), (39.000000, 100.000000, 70.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((39.000000, 100.000000, 70.000000), (31.000000, 100.000000, 70.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((31.000000, 100.000000, 70.000000), (28.000000, 100.000000, 68.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((28.000000, 100.000000, 68.000000), (18.000000, 100.000000, 69.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((18.000000, 100.000000, 69.000000), (9.000000, 100.000000, 76.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((9.000000, 100.000000, 76.000000), (7.000000, 100.000000, 78.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((7.000000, 100.000000, 78.000000), (5.000000, 100.000000, 91.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((12.500000, 100.000000, 95.500000),),
((31.000000, 100.000000, 95.500000),),
((40.500000, 100.000000, 80.500000),),
((35.000000, 100.000000, 70.000000),),
((29.500000, 100.000000, 69.000000),),
((23.000000, 100.000000, 68.500000),),
((13.500000, 100.000000, 72.500000),),
((8.000000, 100.000000, 77.000000),),
((6.000000, 100.000000, 84.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((32.000000, 96.000000, 68.000000), (39.000000, 100.000000, 70.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((39.000000, 100.000000, 70.000000), (31.000000, 100.000000, 70.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((31.000000, 100.000000, 70.000000), (32.000000, 96.000000, 68.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((35.500000, 98.000000, 69.000000),),
((35.000000, 100.000000, 70.000000),),
((31.500000, 98.000000, 69.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((28.000000, 100.000000, 68.000000), (18.000000, 100.000000, 69.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((18.000000, 100.000000, 69.000000), (19.000000, 90.000000, 74.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((19.000000, 90.000000, 74.000000), (28.000000, 100.000000, 68.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((23.000000, 100.000000, 68.500000),),
((18.500000, 95.000000, 71.500000),),
((23.500000, 95.000000, 71.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((34.000000, 87.000000, 73.000000), (32.000000, 96.000000, 68.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((32.000000, 96.000000, 68.000000), (19.000000, 90.000000, 74.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((19.000000, 90.000000, 74.000000), (34.000000, 87.000000, 73.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((33.000000, 91.500000, 70.500000),),
((25.500000, 93.000000, 71.000000),),
((26.500000, 88.500000, 73.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((34.000000, 87.000000, 73.000000), (19.000000, 90.000000, 74.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((19.000000, 90.000000, 74.000000), (35.000000, 85.000000, 84.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((35.000000, 85.000000, 84.000000), (34.000000, 87.000000, 73.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((26.500000, 88.500000, 73.500000),),
((27.000000, 87.500000, 79.000000),),
((34.500000, 86.000000, 78.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((19.000000, 90.000000, 74.000000), (18.000000, 89.000000, 90.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((18.000000, 89.000000, 90.000000), (35.000000, 85.000000, 84.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((35.000000, 85.000000, 84.000000), (19.000000, 90.000000, 74.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((18.500000, 89.500000, 82.000000),),
((26.500000, 87.000000, 87.000000),),
((27.000000, 87.500000, 79.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((32.000000, 96.000000, 68.000000), (28.000000, 100.000000, 68.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((28.000000, 100.000000, 68.000000), (19.000000, 90.000000, 74.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((19.000000, 90.000000, 74.000000), (32.000000, 96.000000, 68.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((30.000000, 98.000000, 68.000000),),
((23.500000, 95.000000, 71.000000),),
((25.500000, 93.000000, 71.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((18.000000, 89.000000, 90.000000), (5.000000, 100.000000, 91.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((5.000000, 100.000000, 91.000000), (20.000000, 100.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((20.000000, 100.000000, 100.000000), (18.000000, 89.000000, 90.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((11.500000, 94.500000, 90.500000),),
((12.500000, 100.000000, 95.500000),),
((19.000000, 94.500000, 95.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((18.000000, 100.000000, 69.000000), (9.000000, 100.000000, 76.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((9.000000, 100.000000, 76.000000), (19.000000, 90.000000, 74.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((19.000000, 90.000000, 74.000000), (18.000000, 100.000000, 69.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((13.500000, 100.000000, 72.500000),),
((14.000000, 95.000000, 75.000000),),
((18.500000, 95.000000, 71.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((19.000000, 90.000000, 74.000000), (9.000000, 100.000000, 76.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((9.000000, 100.000000, 76.000000), (7.000000, 100.000000, 78.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((7.000000, 100.000000, 78.000000), (19.000000, 90.000000, 74.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((14.000000, 95.000000, 75.000000),),
((8.000000, 100.000000, 77.000000),),
((13.000000, 95.000000, 76.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((5.000000, 100.000000, 91.000000), (18.000000, 89.000000, 90.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((18.000000, 89.000000, 90.000000), (7.000000, 100.000000, 78.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((7.000000, 100.000000, 78.000000), (5.000000, 100.000000, 91.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((11.500000, 94.500000, 90.500000),),
((12.500000, 94.500000, 84.000000),),
((6.000000, 100.000000, 84.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((18.000000, 89.000000, 90.000000), (19.000000, 90.000000, 74.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((19.000000, 90.000000, 74.000000), (7.000000, 100.000000, 78.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((7.000000, 100.000000, 78.000000), (18.000000, 89.000000, 90.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((18.500000, 89.500000, 82.000000),),
((13.000000, 95.000000, 76.000000),),
((12.500000, 94.500000, 84.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((75.000000, 69.000000, 91.000000), (73.000000, 62.000000, 88.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((73.000000, 62.000000, 88.000000), (76.000000, 67.000000, 96.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((76.000000, 67.000000, 96.000000), (75.000000, 69.000000, 91.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((74.000000, 65.500000, 89.500000),),
((74.500000, 64.500000, 92.000000),),
((75.500000, 68.000000, 93.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((73.000000, 62.000000, 88.000000), (73.500000, 58.000000, 96.500000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((73.500000, 58.000000, 96.500000), (76.000000, 67.000000, 96.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((76.000000, 67.000000, 96.000000), (73.000000, 62.000000, 88.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((73.250000, 60.000000, 92.250000),),
((74.750000, 62.500000, 96.250000),),
((74.500000, 64.500000, 92.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((77.000000, 73.000000, 94.000000), (75.000000, 69.000000, 91.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((75.000000, 69.000000, 91.000000), (76.000000, 67.000000, 96.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((76.000000, 67.000000, 96.000000), (77.000000, 73.000000, 94.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((76.000000, 71.000000, 92.500000),),
((75.500000, 68.000000, 93.500000),),
((76.500000, 70.000000, 95.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((74.000000, 78.000000, 100.000000), (77.000000, 73.000000, 94.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((77.000000, 73.000000, 94.000000), (76.000000, 67.000000, 96.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((76.000000, 67.000000, 96.000000), (74.000000, 78.000000, 100.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((75.500000, 75.500000, 97.000000),),
((76.500000, 70.000000, 95.000000),),
((75.000000, 72.500000, 98.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((73.500000, 58.000000, 96.500000), (70.000000, 58.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((70.000000, 58.000000, 100.000000), (76.000000, 67.000000, 96.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((76.000000, 67.000000, 96.000000), (73.500000, 58.000000, 96.500000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((71.750000, 58.000000, 98.250000),),
((73.000000, 62.500000, 98.000000),),
((74.750000, 62.500000, 96.250000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((73.500000, 58.000000, 96.500000), (73.000000, 62.000000, 88.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((73.000000, 62.000000, 88.000000), (64.000000, 50.000000, 92.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((64.000000, 50.000000, 92.000000), (73.500000, 58.000000, 96.500000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((73.250000, 60.000000, 92.250000),),
((68.500000, 56.000000, 90.000000),),
((68.750000, 54.000000, 94.250000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((70.000000, 58.000000, 100.000000), (74.000000, 78.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((74.000000, 78.000000, 100.000000), (76.000000, 67.000000, 96.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((76.000000, 67.000000, 96.000000), (70.000000, 58.000000, 100.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((72.000000, 68.000000, 100.000000),),
((75.000000, 72.500000, 98.000000),),
((73.000000, 62.500000, 98.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((73.000000, 62.000000, 88.000000), (63.000000, 53.000000, 86.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((63.000000, 53.000000, 86.000000), (64.000000, 50.000000, 92.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((64.000000, 50.000000, 92.000000), (73.000000, 62.000000, 88.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((68.000000, 57.500000, 87.000000),),
((63.500000, 51.500000, 89.000000),),
((68.500000, 56.000000, 90.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((73.000000, 62.000000, 88.000000), (75.000000, 69.000000, 91.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((75.000000, 69.000000, 91.000000), (66.000000, 70.000000, 85.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((66.000000, 70.000000, 85.000000), (73.000000, 62.000000, 88.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((74.000000, 65.500000, 89.500000),),
((70.500000, 69.500000, 88.000000),),
((69.500000, 66.000000, 86.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((75.000000, 69.000000, 91.000000), (77.000000, 73.000000, 94.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((77.000000, 73.000000, 94.000000), (66.000000, 70.000000, 85.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((66.000000, 70.000000, 85.000000), (75.000000, 69.000000, 91.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((76.000000, 71.000000, 92.500000),),
((71.500000, 71.500000, 89.500000),),
((70.500000, 69.500000, 88.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((58.000000, 51.000000, 100.000000), (70.000000, 58.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((70.000000, 58.000000, 100.000000), (64.000000, 50.000000, 92.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((64.000000, 50.000000, 92.000000), (58.000000, 51.000000, 100.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((64.000000, 54.500000, 100.000000),),
((67.000000, 54.000000, 96.000000),),
((61.000000, 50.500000, 96.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((70.000000, 58.000000, 100.000000), (73.500000, 58.000000, 96.500000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((73.500000, 58.000000, 96.500000), (64.000000, 50.000000, 92.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((64.000000, 50.000000, 92.000000), (70.000000, 58.000000, 100.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((71.750000, 58.000000, 98.250000),),
((68.750000, 54.000000, 94.250000),),
((67.000000, 54.000000, 96.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((77.000000, 73.000000, 94.000000), (74.000000, 78.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((74.000000, 78.000000, 100.000000), (65.000000, 80.000000, 95.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((65.000000, 80.000000, 95.000000), (77.000000, 73.000000, 94.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((75.500000, 75.500000, 97.000000),),
((69.500000, 79.000000, 97.500000),),
((71.000000, 76.500000, 94.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((77.000000, 73.000000, 94.000000), (65.000000, 80.000000, 95.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((65.000000, 80.000000, 95.000000), (66.000000, 70.000000, 85.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((66.000000, 70.000000, 85.000000), (77.000000, 73.000000, 94.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((71.000000, 76.500000, 94.500000),),
((65.500000, 75.000000, 90.000000),),
((71.500000, 71.500000, 89.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((63.000000, 53.000000, 86.000000), (73.000000, 62.000000, 88.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((73.000000, 62.000000, 88.000000), (66.000000, 70.000000, 85.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((66.000000, 70.000000, 85.000000), (63.000000, 53.000000, 86.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((68.000000, 57.500000, 87.000000),),
((69.500000, 66.000000, 86.500000),),
((64.500000, 61.500000, 85.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((57.000000, 57.000000, 84.000000), (63.000000, 53.000000, 86.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((63.000000, 53.000000, 86.000000), (66.000000, 70.000000, 85.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((66.000000, 70.000000, 85.000000), (57.000000, 57.000000, 84.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((60.000000, 55.000000, 85.000000),),
((64.500000, 61.500000, 85.500000),),
((61.500000, 63.500000, 84.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((74.000000, 78.000000, 100.000000), (62.000000, 78.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((62.000000, 78.000000, 100.000000), (65.000000, 80.000000, 95.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((65.000000, 80.000000, 95.000000), (74.000000, 78.000000, 100.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((68.000000, 78.000000, 100.000000),),
((63.500000, 79.000000, 97.500000),),
((69.500000, 79.000000, 97.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((65.000000, 80.000000, 95.000000), (63.000000, 78.000000, 93.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((63.000000, 78.000000, 93.000000), (66.000000, 70.000000, 85.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((66.000000, 70.000000, 85.000000), (65.000000, 80.000000, 95.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((64.000000, 79.000000, 94.000000),),
((64.500000, 74.000000, 89.000000),),
((65.500000, 75.000000, 90.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((74.000000, 78.000000, 100.000000), (70.000000, 58.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((70.000000, 58.000000, 100.000000), (58.000000, 51.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((58.000000, 51.000000, 100.000000), (53.000000, 59.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((53.000000, 59.000000, 100.000000), (62.000000, 78.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((62.000000, 78.000000, 100.000000), (74.000000, 78.000000, 100.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((72.000000, 68.000000, 100.000000),),
((64.000000, 54.500000, 100.000000),),
((55.500000, 55.000000, 100.000000),),
((57.500000, 68.500000, 100.000000),),
((68.000000, 78.000000, 100.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((63.000000, 53.000000, 86.000000), (54.000000, 51.000000, 90.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((54.000000, 51.000000, 90.000000), (64.000000, 50.000000, 92.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((64.000000, 50.000000, 92.000000), (63.000000, 53.000000, 86.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((58.500000, 52.000000, 88.000000),),
((59.000000, 50.500000, 91.000000),),
((63.500000, 51.500000, 89.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((63.000000, 78.000000, 93.000000), (57.000000, 73.000000, 89.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((57.000000, 73.000000, 89.000000), (66.000000, 70.000000, 85.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((66.000000, 70.000000, 85.000000), (63.000000, 78.000000, 93.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((60.000000, 75.500000, 91.000000),),
((61.500000, 71.500000, 87.000000),),
((64.500000, 74.000000, 89.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((54.000000, 51.000000, 90.000000), (58.000000, 51.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((58.000000, 51.000000, 100.000000), (64.000000, 50.000000, 92.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((64.000000, 50.000000, 92.000000), (54.000000, 51.000000, 90.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((56.000000, 51.000000, 95.000000),),
((61.000000, 50.500000, 96.000000),),
((59.000000, 50.500000, 91.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((54.000000, 51.000000, 90.000000), (63.000000, 53.000000, 86.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((63.000000, 53.000000, 86.000000), (57.000000, 57.000000, 84.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((57.000000, 57.000000, 84.000000), (54.000000, 51.000000, 90.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((58.500000, 52.000000, 88.000000),),
((60.000000, 55.000000, 85.000000),),
((55.500000, 54.000000, 87.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((57.000000, 73.000000, 89.000000), (57.000000, 57.000000, 84.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((57.000000, 57.000000, 84.000000), (66.000000, 70.000000, 85.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((66.000000, 70.000000, 85.000000), (57.000000, 73.000000, 89.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((57.000000, 65.000000, 86.500000),),
((61.500000, 63.500000, 84.500000),),
((61.500000, 71.500000, 87.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((63.000000, 78.000000, 93.000000), (62.000000, 78.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((62.000000, 78.000000, 100.000000), (57.000000, 73.000000, 89.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((57.000000, 73.000000, 89.000000), (63.000000, 78.000000, 93.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((62.500000, 78.000000, 96.500000),),
((59.500000, 75.500000, 94.500000),),
((60.000000, 75.500000, 91.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((62.000000, 78.000000, 100.000000), (63.000000, 78.000000, 93.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((63.000000, 78.000000, 93.000000), (65.000000, 80.000000, 95.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((65.000000, 80.000000, 95.000000), (62.000000, 78.000000, 100.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((62.500000, 78.000000, 96.500000),),
((64.000000, 79.000000, 94.000000),),
((63.500000, 79.000000, 97.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((57.000000, 57.000000, 84.000000), (57.000000, 73.000000, 89.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((57.000000, 73.000000, 89.000000), (50.000000, 60.000000, 94.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((50.000000, 60.000000, 94.000000), (57.000000, 57.000000, 84.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((57.000000, 65.000000, 86.500000),),
((53.500000, 66.500000, 91.500000),),
((53.500000, 58.500000, 89.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((62.000000, 78.000000, 100.000000), (53.000000, 59.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((53.000000, 59.000000, 100.000000), (50.000000, 60.000000, 94.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((50.000000, 60.000000, 94.000000), (62.000000, 78.000000, 100.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((57.500000, 68.500000, 100.000000),),
((51.500000, 59.500000, 97.000000),),
((56.000000, 69.000000, 97.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((54.000000, 51.000000, 90.000000), (53.000000, 59.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((53.000000, 59.000000, 100.000000), (58.000000, 51.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((58.000000, 51.000000, 100.000000), (54.000000, 51.000000, 90.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((53.500000, 55.000000, 95.000000),),
((55.500000, 55.000000, 100.000000),),
((56.000000, 51.000000, 95.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((53.000000, 59.000000, 100.000000), (54.000000, 51.000000, 90.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((54.000000, 51.000000, 90.000000), (50.000000, 60.000000, 94.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((50.000000, 60.000000, 94.000000), (53.000000, 59.000000, 100.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((53.500000, 55.000000, 95.000000),),
((52.000000, 55.500000, 92.000000),),
((51.500000, 59.500000, 97.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((54.000000, 51.000000, 90.000000), (57.000000, 57.000000, 84.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((57.000000, 57.000000, 84.000000), (50.000000, 60.000000, 94.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((50.000000, 60.000000, 94.000000), (54.000000, 51.000000, 90.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((55.500000, 54.000000, 87.000000),),
((53.500000, 58.500000, 89.000000),),
((52.000000, 55.500000, 92.000000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
p.WirePolyLine(points=(((57.000000, 73.000000, 89.000000), (62.000000, 78.000000, 100.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((62.000000, 78.000000, 100.000000), (50.000000, 60.000000, 94.000000)), ), mergeType=IMPRINT)
p.WirePolyLine(points=(((50.000000, 60.000000, 94.000000), (57.000000, 73.000000, 89.000000)), ), mergeType=IMPRINT)
e = p.edges
e1 = e.findAt(
((59.500000, 75.500000, 94.500000),),
((56.000000, 69.000000, 97.000000),),
((53.500000, 66.500000, 91.500000),),
)
p.CoverEdges(edgeList = e1, tryAnalytical=True)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.rectangle(point1=(0.000000, 0.000000), point2=(100.000000, 100.000000))
p = mdb.models['Model-1'].Part(name='Part-2', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-2']
p.BaseSolidExtrude(sketch=s, depth=100.000000)
a = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Part-1']
a.Instance(name='Part-1-1', part=p, dependent=ON)
p = mdb.models['Model-1'].parts['Part-2']
a.Instance(name='Part-2-1', part=p, dependent=ON)
a = mdb.models['Model-1'].rootAssembly
a.InstanceFromBooleanMerge(name='Part-3', instances=(
    a.instances['Part-1-1'],
    a.instances['Part-2-1'],
    ), keepIntersections=ON,originalInstances=DELETE, domain=GEOMETRY)
v=mdb.models['Model-1'].rootAssembly.instances['Part-3-1'].cells
for i in range(len(v)):
  mdb.models['Model-1'].rootAssembly.Set(name = 'Set'+str(i+1) , cells=v[i:i+1])
