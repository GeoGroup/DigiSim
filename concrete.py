from abaqus import *
from abaqusConstants import *
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=10.0)
s.rectangle(point1=(0.000000, 0.000000), point2=(75.000000, 52.500000))
p = mdb.models['Model-1'].Part(name='Part-1',dimensionality=TWO_D_PLANAR,type=DEFORMABLE_BODY) 
p.BaseShell(sketch=s)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(6.450000, 52.500000), point2=(7.950000, 49.650000))
s0.Line(point1=(7.950000, 49.650000), point2=(7.500000, 48.900000))
s0.Line(point1=(7.500000, 48.900000), point2=(7.650000, 46.650000))
s0.Line(point1=(7.650000, 46.650000), point2=(6.600000, 45.750000))
s0.Line(point1=(6.600000, 45.750000), point2=(6.300000, 44.700000))
s0.Line(point1=(6.300000, 44.700000), point2=(3.900000, 42.900000))
s0.Line(point1=(3.900000, 42.900000), point2=(1.800000, 42.900000))
s0.Line(point1=(1.800000, 42.900000), point2=(0.750000, 43.500000))
s0.Line(point1=(0.750000, 43.500000), point2=(0.000000, 43.350000))
s0.Line(point1=(0.000000, 43.350000), point2=(0.000000, 52.500000))
s0.Line(point1=(0.000000, 52.500000), point2=(6.450000, 52.500000))
s0.Line(point1=(6.538492, 52.500000), point2=(8.124241, 49.645125))
s0.Line(point1=(8.124241, 49.645125), point2=(7.685528, 48.855202))
s0.Line(point1=(7.685528, 48.855202), point2=(7.814858, 46.580726))
s0.Line(point1=(7.814858, 46.580726), point2=(6.761232, 45.646602))
s0.Line(point1=(6.761232, 45.646602), point2=(6.456152, 44.592528))
s0.Line(point1=(6.456152, 44.592528), point2=(3.960000, 42.720000))
s0.Line(point1=(3.960000, 42.720000), point2=(1.750386, 42.713176))
s0.Line(point1=(1.750386, 42.713176), point2=(0.719998, 43.315118))
s0.Line(point1=(0.719998, 43.315118), point2=(0.000000, 43.251942))
s0.Line(point1=(0.000000, 43.251942), point2=(0.000000, 52.500000))
s0.Line(point1=(0.000000, 52.500000), point2=(6.538492, 52.500000))
s0.Line(point1=(6.361508, 52.500000), point2=(7.775759, 49.654875))
s0.Line(point1=(7.775759, 49.654875), point2=(7.314472, 48.944798))
s0.Line(point1=(7.314472, 48.944798), point2=(7.485142, 46.719274))
s0.Line(point1=(7.485142, 46.719274), point2=(6.438768, 45.853398))
s0.Line(point1=(6.438768, 45.853398), point2=(6.143848, 44.807472))
s0.Line(point1=(6.143848, 44.807472), point2=(3.840000, 43.080000))
s0.Line(point1=(3.840000, 43.080000), point2=(1.849614, 43.086824))
s0.Line(point1=(1.849614, 43.086824), point2=(0.780002, 43.684882))
s0.Line(point1=(0.780002, 43.684882), point2=(0.000000, 43.448058))
s0.Line(point1=(0.000000, 43.448058), point2=(0.000000, 52.500000))
s0.Line(point1=(0.000000, 52.500000), point2=(6.361508, 52.500000))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(0.000000, 36.150000), point2=(0.900000, 35.700000))
s0.Line(point1=(0.900000, 35.700000), point2=(0.900000, 34.950000))
s0.Line(point1=(0.900000, 34.950000), point2=(1.650000, 34.350000))
s0.Line(point1=(1.650000, 34.350000), point2=(1.800000, 33.600000))
s0.Line(point1=(1.800000, 33.600000), point2=(2.400000, 33.000000))
s0.Line(point1=(2.400000, 33.000000), point2=(1.800000, 31.500000))
s0.Line(point1=(1.800000, 31.500000), point2=(0.450000, 30.750000))
s0.Line(point1=(0.450000, 30.750000), point2=(0.000000, 30.750000))
s0.Line(point1=(0.000000, 30.750000), point2=(0.000000, 36.150000))
s0.Line(point1=(0.000000, 36.239443), point2=(1.044721, 35.789443))
s0.Line(point1=(1.044721, 35.789443), point2=(1.062470, 35.028087))
s0.Line(point1=(1.062470, 35.028087), point2=(1.810528, 34.447698))
s0.Line(point1=(1.810528, 34.447698), point2=(1.968769, 33.690322))
s0.Line(point1=(1.968769, 33.690322), point2=(2.563558, 33.033572))
s0.Line(point1=(2.563558, 33.033572), point2=(1.941412, 31.375445))
s0.Line(point1=(1.941412, 31.375445), point2=(0.498564, 30.562584))
s0.Line(point1=(0.498564, 30.562584), point2=(0.000000, 30.650000))
s0.Line(point1=(0.000000, 30.650000), point2=(0.000000, 36.239443))
s0.Line(point1=(0.000000, 36.060557), point2=(0.755279, 35.610557))
s0.Line(point1=(0.755279, 35.610557), point2=(0.737530, 34.871913))
s0.Line(point1=(0.737530, 34.871913), point2=(1.489472, 34.252302))
s0.Line(point1=(1.489472, 34.252302), point2=(1.631231, 33.509678))
s0.Line(point1=(1.631231, 33.509678), point2=(2.236442, 32.966428))
s0.Line(point1=(2.236442, 32.966428), point2=(1.658588, 31.624555))
s0.Line(point1=(1.658588, 31.624555), point2=(0.401436, 30.937416))
s0.Line(point1=(0.401436, 30.937416), point2=(0.000000, 30.850000))
s0.Line(point1=(0.000000, 30.850000), point2=(0.000000, 36.060557))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(0.000000, 28.800000), point2=(1.050000, 28.350000))
s0.Line(point1=(1.050000, 28.350000), point2=(1.200000, 27.900000))
s0.Line(point1=(1.200000, 27.900000), point2=(2.250000, 27.750000))
s0.Line(point1=(2.250000, 27.750000), point2=(2.550000, 27.300000))
s0.Line(point1=(2.550000, 27.300000), point2=(2.550000, 26.700000))
s0.Line(point1=(2.550000, 26.700000), point2=(1.800000, 26.250000))
s0.Line(point1=(1.800000, 26.250000), point2=(1.500000, 25.350000))
s0.Line(point1=(1.500000, 25.350000), point2=(0.900000, 25.350000))
s0.Line(point1=(0.900000, 25.350000), point2=(0.000000, 26.700000))
s0.Line(point1=(0.000000, 26.700000), point2=(0.000000, 28.800000))
s0.Line(point1=(0.000000, 28.891915), point2=(1.184260, 28.473537))
s0.Line(point1=(1.184260, 28.473537), point2=(1.309010, 28.030618))
s0.Line(point1=(1.309010, 28.030618), point2=(2.347347, 27.904465))
s0.Line(point1=(2.347347, 27.904465), point2=(2.733205, 27.355470))
s0.Line(point1=(2.733205, 27.355470), point2=(2.701450, 26.614251))
s0.Line(point1=(2.701450, 26.614251), point2=(1.946318, 26.132628))
s0.Line(point1=(1.946318, 26.132628), point2=(1.594868, 25.218377))
s0.Line(point1=(1.594868, 25.218377), point2=(0.816795, 25.194530))
s0.Line(point1=(0.816795, 25.194530), point2=(0.000000, 26.644530))
s0.Line(point1=(0.000000, 26.644530), point2=(0.000000, 28.891915))
s0.Line(point1=(0.000000, 28.708085), point2=(0.915740, 28.226463))
s0.Line(point1=(0.915740, 28.226463), point2=(1.090990, 27.769382))
s0.Line(point1=(1.090990, 27.769382), point2=(2.152653, 27.595535))
s0.Line(point1=(2.152653, 27.595535), point2=(2.366795, 27.244530))
s0.Line(point1=(2.366795, 27.244530), point2=(2.398550, 26.785749))
s0.Line(point1=(2.398550, 26.785749), point2=(1.653682, 26.367372))
s0.Line(point1=(1.653682, 26.367372), point2=(1.405132, 25.481623))
s0.Line(point1=(1.405132, 25.481623), point2=(0.983205, 25.505470))
s0.Line(point1=(0.983205, 25.505470), point2=(0.000000, 26.755470))
s0.Line(point1=(0.000000, 26.755470), point2=(0.000000, 28.708085))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(0.000000, 10.800000), point2=(1.350000, 11.700000))
s0.Line(point1=(1.350000, 11.700000), point2=(1.800000, 12.600000))
s0.Line(point1=(1.800000, 12.600000), point2=(3.900000, 13.050000))
s0.Line(point1=(3.900000, 13.050000), point2=(4.650000, 13.650000))
s0.Line(point1=(4.650000, 13.650000), point2=(6.450000, 11.700000))
s0.Line(point1=(6.450000, 11.700000), point2=(7.950000, 8.550000))
s0.Line(point1=(7.950000, 8.550000), point2=(10.050000, 6.450000))
s0.Line(point1=(10.050000, 6.450000), point2=(10.050000, 3.750000))
s0.Line(point1=(10.050000, 3.750000), point2=(9.750000, 3.450000))
s0.Line(point1=(9.750000, 3.450000), point2=(8.250000, 3.750000))
s0.Line(point1=(8.250000, 3.750000), point2=(5.550000, 2.700000))
s0.Line(point1=(5.550000, 2.700000), point2=(4.650000, 1.950000))
s0.Line(point1=(4.650000, 1.950000), point2=(3.300000, 1.800000))
s0.Line(point1=(3.300000, 1.800000), point2=(2.250000, 3.000000))
s0.Line(point1=(2.250000, 3.000000), point2=(0.450000, 6.600000))
s0.Line(point1=(0.450000, 6.600000), point2=(0.000000, 6.750000))
s0.Line(point1=(0.000000, 6.750000), point2=(0.000000, 10.800000))
s0.Line(point1=(0.000000, 10.883205), point2=(1.205087, 11.827926))
s0.Line(point1=(1.205087, 11.827926), point2=(1.689604, 12.742502))
s0.Line(point1=(1.689604, 12.742502), point2=(3.816578, 13.225867))
s0.Line(point1=(3.816578, 13.225867), point2=(4.661011, 13.795915))
s0.Line(point1=(4.661011, 13.795915), point2=(6.613766, 11.810821))
s0.Line(point1=(6.613766, 11.810821), point2=(8.110997, 8.663704))
s0.Line(point1=(8.110997, 8.663704), point2=(10.220711, 6.520711))
s0.Line(point1=(10.220711, 6.520711), point2=(10.220711, 3.679289))
s0.Line(point1=(10.220711, 3.679289), point2=(9.801099, 3.281231))
s0.Line(point1=(9.801099, 3.281231), point2=(8.266633, 3.558741))
s0.Line(point1=(8.266633, 3.558741), point2=(5.650263, 2.529977))
s0.Line(point1=(5.650263, 2.529977), point2=(4.725062, 1.773789))
s0.Line(point1=(4.725062, 1.773789), point2=(3.235785, 1.634761))
s0.Line(point1=(3.235785, 1.634761), point2=(2.085300, 2.889428))
s0.Line(point1=(2.085300, 2.889428), point2=(0.328935, 6.460410))
s0.Line(point1=(0.328935, 6.460410), point2=(0.000000, 6.655132))
s0.Line(point1=(0.000000, 6.655132), point2=(0.000000, 10.883205))
s0.Line(point1=(0.000000, 10.716795), point2=(1.494913, 11.572074))
s0.Line(point1=(1.494913, 11.572074), point2=(1.910396, 12.457498))
s0.Line(point1=(1.910396, 12.457498), point2=(3.983422, 12.874133))
s0.Line(point1=(3.983422, 12.874133), point2=(4.638989, 13.504085))
s0.Line(point1=(4.638989, 13.504085), point2=(6.286234, 11.589179))
s0.Line(point1=(6.286234, 11.589179), point2=(7.789003, 8.436296))
s0.Line(point1=(7.789003, 8.436296), point2=(9.879289, 6.379289))
s0.Line(point1=(9.879289, 6.379289), point2=(9.879289, 3.820711))
s0.Line(point1=(9.879289, 3.820711), point2=(9.698901, 3.618769))
s0.Line(point1=(9.698901, 3.618769), point2=(8.233367, 3.941259))
s0.Line(point1=(8.233367, 3.941259), point2=(5.449737, 2.870023))
s0.Line(point1=(5.449737, 2.870023), point2=(4.574938, 2.126211))
s0.Line(point1=(4.574938, 2.126211), point2=(3.364215, 1.965239))
s0.Line(point1=(3.364215, 1.965239), point2=(2.414700, 3.110572))
s0.Line(point1=(2.414700, 3.110572), point2=(0.571065, 6.739590))
s0.Line(point1=(0.571065, 6.739590), point2=(0.000000, 6.844868))
s0.Line(point1=(0.000000, 6.844868), point2=(0.000000, 10.716795))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(0.000000, 1.650000), point2=(1.200000, 1.500000))
s0.Line(point1=(1.200000, 1.500000), point2=(2.550000, 0.000000))
s0.Line(point1=(2.550000, 0.000000), point2=(0.000000, 0.000000))
s0.Line(point1=(0.000000, 0.000000), point2=(0.000000, 1.650000))
s0.Line(point1=(0.000000, 1.749228), point2=(1.286733, 1.666124))
s0.Line(point1=(1.286733, 1.666124), point2=(2.624329, 0.000000))
s0.Line(point1=(2.624329, 0.000000), point2=(0.000000, 0.000000))
s0.Line(point1=(0.000000, 0.000000), point2=(0.000000, 1.749228))
s0.Line(point1=(0.000000, 1.550772), point2=(1.113267, 1.333876))
s0.Line(point1=(1.113267, 1.333876), point2=(2.475671, 0.000000))
s0.Line(point1=(2.475671, 0.000000), point2=(0.000000, 0.000000))
s0.Line(point1=(0.000000, 0.000000), point2=(0.000000, 1.550772))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(0.600000, 39.300000), point2=(1.350000, 39.300000))
s0.Line(point1=(1.350000, 39.300000), point2=(2.400000, 37.950000))
s0.Line(point1=(2.400000, 37.950000), point2=(3.600000, 37.650000))
s0.Line(point1=(3.600000, 37.650000), point2=(3.900000, 37.200000))
s0.Line(point1=(3.900000, 37.200000), point2=(3.750000, 35.850000))
s0.Line(point1=(3.750000, 35.850000), point2=(1.050000, 36.150000))
s0.Line(point1=(1.050000, 36.150000), point2=(0.300000, 37.500000))
s0.Line(point1=(0.300000, 37.500000), point2=(0.600000, 39.300000))
s0.Line(point1=(0.501361, 39.416440), point2=(1.428935, 39.461394))
s0.Line(point1=(1.428935, 39.461394), point2=(2.503189, 38.108408))
s0.Line(point1=(2.503189, 38.108408), point2=(3.707459, 37.802484))
s0.Line(point1=(3.707459, 37.802484), point2=(4.082593, 37.244427))
s0.Line(point1=(4.082593, 37.244427), point2=(3.838345, 35.739568))
s0.Line(point1=(3.838345, 35.739568), point2=(0.951541, 36.002047))
s0.Line(point1=(0.951541, 36.002047), point2=(0.000000, 37.467876))
s0.Line(point1=(0.000000, 37.467876), point2=(0.501361, 39.416440))
s0.Line(point1=(0.698639, 39.183560), point2=(1.271065, 39.138606))
s0.Line(point1=(1.271065, 39.138606), point2=(2.296811, 37.791592))
s0.Line(point1=(2.296811, 37.791592), point2=(3.492541, 37.497516))
s0.Line(point1=(3.492541, 37.497516), point2=(3.717407, 37.155573))
s0.Line(point1=(3.717407, 37.155573), point2=(3.661655, 35.960432))
s0.Line(point1=(3.661655, 35.960432), point2=(1.148459, 36.297953))
s0.Line(point1=(1.148459, 36.297953), point2=(0.486055, 37.532124))
s0.Line(point1=(0.486055, 37.532124), point2=(0.698639, 39.183560))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(0.900000, 17.700000), point2=(1.350000, 17.700000))
s0.Line(point1=(1.350000, 17.700000), point2=(2.850000, 16.350000))
s0.Line(point1=(2.850000, 16.350000), point2=(3.000000, 15.450000))
s0.Line(point1=(3.000000, 15.450000), point2=(3.900000, 14.550000))
s0.Line(point1=(3.900000, 14.550000), point2=(3.900000, 13.500000))
s0.Line(point1=(3.900000, 13.500000), point2=(1.650000, 14.100000))
s0.Line(point1=(1.650000, 14.100000), point2=(0.900000, 15.900000))
s0.Line(point1=(0.900000, 15.900000), point2=(0.900000, 17.700000))
s0.Line(point1=(0.800000, 17.800000), point2=(1.416896, 17.874329))
s0.Line(point1=(1.416896, 17.874329), point2=(3.015536, 16.440769))
s0.Line(point1=(3.015536, 16.440769), point2=(3.169350, 15.537151))
s0.Line(point1=(3.169350, 15.537151), point2=(4.070711, 14.620711))
s0.Line(point1=(4.070711, 14.620711), point2=(3.974234, 13.403377))
s0.Line(point1=(3.974234, 13.403377), point2=(1.531926, 13.964915))
s0.Line(point1=(1.531926, 13.964915), point2=(0.707692, 15.861538))
s0.Line(point1=(0.707692, 15.861538), point2=(0.800000, 17.800000))
s0.Line(point1=(1.000000, 17.600000), point2=(1.283104, 17.525671))
s0.Line(point1=(1.283104, 17.525671), point2=(2.684464, 16.259231))
s0.Line(point1=(2.684464, 16.259231), point2=(2.830650, 15.362849))
s0.Line(point1=(2.830650, 15.362849), point2=(3.729289, 14.479289))
s0.Line(point1=(3.729289, 14.479289), point2=(3.825766, 13.596623))
s0.Line(point1=(3.825766, 13.596623), point2=(1.768074, 14.235085))
s0.Line(point1=(1.768074, 14.235085), point2=(1.092308, 15.938462))
s0.Line(point1=(1.092308, 15.938462), point2=(1.000000, 17.600000))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(1.950000, 42.000000), point2=(1.650000, 40.350000))
s0.Line(point1=(1.650000, 40.350000), point2=(1.050000, 40.200000))
s0.Line(point1=(1.050000, 40.200000), point2=(1.050000, 42.000000))
s0.Line(point1=(1.050000, 42.000000), point2=(1.950000, 42.000000))
s0.Line(point1=(2.048387, 42.082111), point2=(1.772641, 40.235097))
s0.Line(point1=(1.772641, 40.235097), point2=(0.974254, 40.102986))
s0.Line(point1=(0.974254, 40.102986), point2=(0.950000, 42.100000))
s0.Line(point1=(0.950000, 42.100000), point2=(2.048387, 42.082111))
s0.Line(point1=(1.851613, 41.917889), point2=(1.527359, 40.464903))
s0.Line(point1=(1.527359, 40.464903), point2=(1.125746, 40.297014))
s0.Line(point1=(1.125746, 40.297014), point2=(1.150000, 41.900000))
s0.Line(point1=(1.150000, 41.900000), point2=(1.851613, 41.917889))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(1.200000, 22.650000), point2=(2.250000, 22.500000))
s0.Line(point1=(2.250000, 22.500000), point2=(2.850000, 21.900000))
s0.Line(point1=(2.850000, 21.900000), point2=(3.000000, 20.550000))
s0.Line(point1=(3.000000, 20.550000), point2=(2.550000, 19.350000))
s0.Line(point1=(2.550000, 19.350000), point2=(2.100000, 19.350000))
s0.Line(point1=(2.100000, 19.350000), point2=(2.100000, 19.050000))
s0.Line(point1=(2.100000, 19.050000), point2=(1.350000, 19.050000))
s0.Line(point1=(1.350000, 19.050000), point2=(1.200000, 22.650000))
s0.Line(point1=(1.114229, 22.744832), point2=(2.334853, 22.669706))
s0.Line(point1=(2.334853, 22.669706), point2=(3.020099, 21.981754))
s0.Line(point1=(3.020099, 21.981754), point2=(3.193021, 20.525931))
s0.Line(point1=(3.193021, 20.525931), point2=(2.643633, 19.214888))
s0.Line(point1=(2.643633, 19.214888), point2=(2.200000, 19.250000))
s0.Line(point1=(2.200000, 19.250000), point2=(2.200000, 18.950000))
s0.Line(point1=(2.200000, 18.950000), point2=(1.250087, 18.945837))
s0.Line(point1=(1.250087, 18.945837), point2=(1.114229, 22.744832))
s0.Line(point1=(1.285771, 22.555168), point2=(2.165147, 22.330294))
s0.Line(point1=(2.165147, 22.330294), point2=(2.679901, 21.818246))
s0.Line(point1=(2.679901, 21.818246), point2=(2.806979, 20.574069))
s0.Line(point1=(2.806979, 20.574069), point2=(2.456367, 19.485112))
s0.Line(point1=(2.456367, 19.485112), point2=(2.000000, 19.450000))
s0.Line(point1=(2.000000, 19.450000), point2=(2.000000, 19.150000))
s0.Line(point1=(2.000000, 19.150000), point2=(1.449913, 19.154163))
s0.Line(point1=(1.449913, 19.154163), point2=(1.285771, 22.555168))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(2.250000, 24.450000), point2=(4.200000, 24.750000))
s0.Line(point1=(4.200000, 24.750000), point2=(5.400000, 24.150000))
s0.Line(point1=(5.400000, 24.150000), point2=(5.400000, 23.250000))
s0.Line(point1=(5.400000, 23.250000), point2=(4.500000, 21.900000))
s0.Line(point1=(4.500000, 21.900000), point2=(3.600000, 22.050000))
s0.Line(point1=(3.600000, 22.050000), point2=(2.700000, 22.950000))
s0.Line(point1=(2.700000, 22.950000), point2=(2.250000, 23.700000))
s0.Line(point1=(2.250000, 23.700000), point2=(2.250000, 24.450000))
s0.Line(point1=(2.134794, 24.548837), point2=(4.229516, 24.938280))
s0.Line(point1=(4.229516, 24.938280), point2=(5.544721, 24.239443))
s0.Line(point1=(5.544721, 24.239443), point2=(5.583205, 23.194530))
s0.Line(point1=(5.583205, 23.194530), point2=(4.566765, 21.745891))
s0.Line(point1=(4.566765, 21.745891), point2=(3.512849, 21.880650))
s0.Line(point1=(3.512849, 21.880650), point2=(2.543540, 22.827840))
s0.Line(point1=(2.543540, 22.827840), point2=(2.064251, 23.648550))
s0.Line(point1=(2.064251, 23.648550), point2=(2.134794, 24.548837))
s0.Line(point1=(2.365206, 24.351163), point2=(4.170484, 24.561720))
s0.Line(point1=(4.170484, 24.561720), point2=(5.255279, 24.060557))
s0.Line(point1=(5.255279, 24.060557), point2=(5.216795, 23.305470))
s0.Line(point1=(5.216795, 23.305470), point2=(4.433235, 22.054109))
s0.Line(point1=(4.433235, 22.054109), point2=(3.687151, 22.219350))
s0.Line(point1=(3.687151, 22.219350), point2=(2.856460, 23.072160))
s0.Line(point1=(2.856460, 23.072160), point2=(2.435749, 23.751450))
s0.Line(point1=(2.435749, 23.751450), point2=(2.365206, 24.351163))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(3.150000, 42.000000), point2=(4.050000, 41.700000))
s0.Line(point1=(4.050000, 41.700000), point2=(5.550000, 40.350000))
s0.Line(point1=(5.550000, 40.350000), point2=(5.550000, 39.450000))
s0.Line(point1=(5.550000, 39.450000), point2=(5.250000, 39.150000))
s0.Line(point1=(5.250000, 39.150000), point2=(3.600000, 39.300000))
s0.Line(point1=(3.600000, 39.300000), point2=(2.700000, 40.050000))
s0.Line(point1=(2.700000, 40.050000), point2=(3.150000, 42.000000))
s0.Line(point1=(3.084184, 42.117354), point2=(4.148519, 41.869198))
s0.Line(point1=(4.148519, 41.869198), point2=(5.716896, 40.424329))
s0.Line(point1=(5.716896, 40.424329), point2=(5.720711, 39.379289))
s0.Line(point1=(5.720711, 39.379289), point2=(5.311657, 38.979700))
s0.Line(point1=(5.311657, 38.979700), point2=(3.526928, 39.123589))
s0.Line(point1=(3.526928, 39.123589), point2=(2.538542, 39.995664))
s0.Line(point1=(2.538542, 39.995664), point2=(3.084184, 42.117354))
s0.Line(point1=(3.215816, 41.882646), point2=(3.951481, 41.530802))
s0.Line(point1=(3.951481, 41.530802), point2=(5.383104, 40.275671))
s0.Line(point1=(5.383104, 40.275671), point2=(5.379289, 39.520711))
s0.Line(point1=(5.379289, 39.520711), point2=(5.188343, 39.320300))
s0.Line(point1=(5.188343, 39.320300), point2=(3.673072, 39.476411))
s0.Line(point1=(3.673072, 39.476411), point2=(2.861458, 40.104336))
s0.Line(point1=(2.861458, 40.104336), point2=(3.215816, 41.882646))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(4.350000, 31.200000), point2=(4.650000, 30.600000))
s0.Line(point1=(4.650000, 30.600000), point2=(4.200000, 30.600000))
s0.Line(point1=(4.200000, 30.600000), point2=(3.900000, 29.550000))
s0.Line(point1=(3.900000, 29.550000), point2=(3.150000, 29.250000))
s0.Line(point1=(3.150000, 29.250000), point2=(3.000000, 30.300000))
s0.Line(point1=(3.000000, 30.300000), point2=(3.450000, 31.050000))
s0.Line(point1=(3.450000, 31.050000), point2=(3.900000, 31.350000))
s0.Line(point1=(3.900000, 31.350000), point2=(4.350000, 31.200000))
s0.Line(point1=(4.471065, 31.339590), point2=(4.739443, 30.544721))
s0.Line(point1=(4.739443, 30.544721), point2=(4.296152, 30.472528))
s0.Line(point1=(4.296152, 30.472528), point2=(4.033291, 29.429680))
s0.Line(point1=(4.033291, 29.429680), point2=(3.088144, 29.143010))
s0.Line(point1=(3.088144, 29.143010), point2=(2.815256, 30.337307))
s0.Line(point1=(2.815256, 30.337307), point2=(3.308781, 31.184655))
s0.Line(point1=(3.308781, 31.184655), point2=(3.876153, 31.528073))
s0.Line(point1=(3.876153, 31.528073), point2=(4.471065, 31.339590))
s0.Line(point1=(4.228935, 31.060410), point2=(4.560557, 30.655279))
s0.Line(point1=(4.560557, 30.655279), point2=(4.103848, 30.727472))
s0.Line(point1=(4.103848, 30.727472), point2=(3.766709, 29.670320))
s0.Line(point1=(3.766709, 29.670320), point2=(3.211856, 29.356990))
s0.Line(point1=(3.211856, 29.356990), point2=(3.184744, 30.262693))
s0.Line(point1=(3.184744, 30.262693), point2=(3.591219, 30.915345))
s0.Line(point1=(3.591219, 30.915345), point2=(3.923847, 31.171927))
s0.Line(point1=(3.923847, 31.171927), point2=(4.228935, 31.060410))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(3.300000, 20.400000), point2=(4.650000, 20.400000))
s0.Line(point1=(4.650000, 20.400000), point2=(5.850000, 18.900000))
s0.Line(point1=(5.850000, 18.900000), point2=(6.150000, 18.000000))
s0.Line(point1=(6.150000, 18.000000), point2=(3.900000, 17.550000))
s0.Line(point1=(3.900000, 17.550000), point2=(4.050000, 18.150000))
s0.Line(point1=(4.050000, 18.150000), point2=(3.300000, 20.400000))
s0.Line(point1=(3.205132, 20.468377), point2=(4.728087, 20.562470))
s0.Line(point1=(4.728087, 20.562470), point2=(6.022955, 18.994092))
s0.Line(point1=(6.022955, 18.994092), point2=(6.264480, 17.933565))
s0.Line(point1=(6.264480, 17.933565), point2=(3.822597, 17.476195))
s0.Line(point1=(3.822597, 17.476195), point2=(3.858117, 18.142631))
s0.Line(point1=(3.858117, 18.142631), point2=(3.205132, 20.468377))
s0.Line(point1=(3.394868, 20.331623), point2=(4.571913, 20.237530))
s0.Line(point1=(4.571913, 20.237530), point2=(5.677045, 18.805908))
s0.Line(point1=(5.677045, 18.805908), point2=(6.035520, 18.066435))
s0.Line(point1=(6.035520, 18.066435), point2=(3.977403, 17.623805))
s0.Line(point1=(3.977403, 17.623805), point2=(4.241883, 18.157369))
s0.Line(point1=(4.241883, 18.157369), point2=(3.394868, 20.331623))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(8.700000, 2.550000), point2=(8.850000, 1.500000))
s0.Line(point1=(8.850000, 1.500000), point2=(7.950000, 1.050000))
s0.Line(point1=(7.950000, 1.050000), point2=(7.350000, 0.000000))
s0.Line(point1=(7.350000, 0.000000), point2=(3.900000, 0.000000))
s0.Line(point1=(3.900000, 0.000000), point2=(4.650000, 0.300000))
s0.Line(point1=(4.650000, 0.300000), point2=(5.250000, 1.200000))
s0.Line(point1=(5.250000, 1.200000), point2=(7.950000, 1.950000))
s0.Line(point1=(7.950000, 1.950000), point2=(8.250000, 2.550000))
s0.Line(point1=(8.250000, 2.550000), point2=(8.700000, 2.550000))
s0.Line(point1=(8.798995, 2.664142), point2=(8.993716, 1.424699))
s0.Line(point1=(8.993716, 1.424699), point2=(8.081546, 0.910943))
s0.Line(point1=(8.081546, 0.910943), point2=(7.436824, 0.000000))
s0.Line(point1=(7.436824, 0.000000), point2=(3.862861, 0.000000))
s0.Line(point1=(3.862861, 0.000000), point2=(4.529656, 0.448318))
s0.Line(point1=(4.529656, 0.448318), point2=(5.140031, 1.351822))
s0.Line(point1=(5.140031, 1.351822), point2=(7.833793, 2.091073))
s0.Line(point1=(7.833793, 2.091073), point2=(8.160557, 2.694721))
s0.Line(point1=(8.160557, 2.694721), point2=(8.798995, 2.664142))
s0.Line(point1=(8.601005, 2.435858), point2=(8.706284, 1.575301))
s0.Line(point1=(8.706284, 1.575301), point2=(7.818454, 1.189057))
s0.Line(point1=(7.818454, 1.189057), point2=(7.263176, 0.000000))
s0.Line(point1=(7.263176, 0.000000), point2=(3.937139, 0.000000))
s0.Line(point1=(3.937139, 0.000000), point2=(4.770344, 0.000000))
s0.Line(point1=(4.770344, 0.000000), point2=(5.359969, 1.048178))
s0.Line(point1=(5.359969, 1.048178), point2=(8.066207, 1.808927))
s0.Line(point1=(8.066207, 1.808927), point2=(8.339443, 2.405279))
s0.Line(point1=(8.339443, 2.405279), point2=(8.601005, 2.435858))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(4.500000, 35.100000), point2=(7.200000, 32.850000))
s0.Line(point1=(7.200000, 32.850000), point2=(10.500000, 30.750000))
s0.Line(point1=(10.500000, 30.750000), point2=(11.400000, 29.400000))
s0.Line(point1=(11.400000, 29.400000), point2=(11.400000, 28.050000))
s0.Line(point1=(11.400000, 28.050000), point2=(10.800000, 26.850000))
s0.Line(point1=(10.800000, 26.850000), point2=(9.450000, 25.350000))
s0.Line(point1=(9.450000, 25.350000), point2=(7.650000, 24.300000))
s0.Line(point1=(7.650000, 24.300000), point2=(6.600000, 25.050000))
s0.Line(point1=(6.600000, 25.050000), point2=(5.400000, 26.850000))
s0.Line(point1=(5.400000, 26.850000), point2=(5.550000, 28.350000))
s0.Line(point1=(5.550000, 28.350000), point2=(4.650000, 30.750000))
s0.Line(point1=(4.650000, 30.750000), point2=(4.500000, 35.100000))
s0.Line(point1=(4.464078, 35.173376), point2=(7.317706, 33.011188))
s0.Line(point1=(7.317706, 33.011188), point2=(10.636893, 30.889836))
s0.Line(point1=(10.636893, 30.889836), point2=(11.583205, 29.455470))
s0.Line(point1=(11.583205, 29.455470), point2=(11.589443, 28.005279))
s0.Line(point1=(11.589443, 28.005279), point2=(10.963772, 26.738382))
s0.Line(point1=(10.963772, 26.738382), point2=(9.574717, 25.196726))
s0.Line(point1=(9.574717, 25.196726), point2=(7.642263, 24.132249))
s0.Line(point1=(7.642263, 24.132249), point2=(6.458671, 24.913157))
s0.Line(point1=(6.458671, 24.913157), point2=(5.217291, 26.804480))
s0.Line(point1=(5.217291, 26.804480), point2=(5.356863, 28.324838))
s0.Line(point1=(5.356863, 28.324838), point2=(4.456426, 30.711441))
s0.Line(point1=(4.456426, 30.711441), point2=(4.464078, 35.173376))
s0.Line(point1=(4.535922, 35.026624), point2=(7.082294, 32.688812))
s0.Line(point1=(7.082294, 32.688812), point2=(10.363107, 30.610164))
s0.Line(point1=(10.363107, 30.610164), point2=(11.216795, 29.344530))
s0.Line(point1=(11.216795, 29.344530), point2=(11.210557, 28.094721))
s0.Line(point1=(11.210557, 28.094721), point2=(10.636228, 26.961618))
s0.Line(point1=(10.636228, 26.961618), point2=(9.325283, 25.503274))
s0.Line(point1=(9.325283, 25.503274), point2=(7.657737, 24.467751))
s0.Line(point1=(7.657737, 24.467751), point2=(6.741329, 25.186843))
s0.Line(point1=(6.741329, 25.186843), point2=(5.582709, 26.895520))
s0.Line(point1=(5.582709, 26.895520), point2=(5.743137, 28.375162))
s0.Line(point1=(5.743137, 28.375162), point2=(4.843574, 30.788559))
s0.Line(point1=(4.843574, 30.788559), point2=(4.535922, 35.026624))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(4.950000, 43.050000), point2=(6.300000, 42.900000))
s0.Line(point1=(6.300000, 42.900000), point2=(7.050000, 40.200000))
s0.Line(point1=(7.050000, 40.200000), point2=(5.850000, 40.650000))
s0.Line(point1=(5.850000, 40.650000), point2=(4.950000, 42.300000))
s0.Line(point1=(4.950000, 42.300000), point2=(4.950000, 43.050000))
s0.Line(point1=(4.861043, 43.149388), point2=(6.407395, 43.026153))
s0.Line(point1=(6.407395, 43.026153), point2=(7.111239, 40.133131))
s0.Line(point1=(7.111239, 40.133131), point2=(5.727098, 40.508482))
s0.Line(point1=(5.727098, 40.508482), point2=(4.762210, 42.252115))
s0.Line(point1=(4.762210, 42.252115), point2=(4.861043, 43.149388))
s0.Line(point1=(5.038957, 42.950612), point2=(6.192605, 42.773847))
s0.Line(point1=(6.192605, 42.773847), point2=(6.988761, 40.266869))
s0.Line(point1=(6.988761, 40.266869), point2=(5.972902, 40.791518))
s0.Line(point1=(5.972902, 40.791518), point2=(5.137790, 42.347885))
s0.Line(point1=(5.137790, 42.347885), point2=(5.038957, 42.950612))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(7.200000, 38.100000), point2=(7.200000, 37.350000))
s0.Line(point1=(7.200000, 37.350000), point2=(6.600000, 36.300000))
s0.Line(point1=(6.600000, 36.300000), point2=(5.400000, 36.450000))
s0.Line(point1=(5.400000, 36.450000), point2=(5.550000, 37.500000))
s0.Line(point1=(5.550000, 37.500000), point2=(7.200000, 38.100000))
s0.Line(point1=(7.265826, 38.193979), point2=(7.386824, 37.300386))
s0.Line(point1=(7.386824, 37.300386), point2=(6.674421, 36.151158))
s0.Line(point1=(6.674421, 36.151158), point2=(5.288602, 36.364914))
s0.Line(point1=(5.288602, 36.364914), point2=(5.416831, 37.608121))
s0.Line(point1=(5.416831, 37.608121), point2=(7.265826, 38.193979))
s0.Line(point1=(7.134174, 38.006021), point2=(7.013176, 37.399614))
s0.Line(point1=(7.013176, 37.399614), point2=(6.525579, 36.448842))
s0.Line(point1=(6.525579, 36.448842), point2=(5.511398, 36.535086))
s0.Line(point1=(5.511398, 36.535086), point2=(5.683169, 37.391879))
s0.Line(point1=(5.683169, 37.391879), point2=(7.134174, 38.006021))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(5.850000, 22.050000), point2=(6.600000, 22.350000))
s0.Line(point1=(6.600000, 22.350000), point2=(9.900000, 22.350000))
s0.Line(point1=(9.900000, 22.350000), point2=(9.900000, 21.750000))
s0.Line(point1=(9.900000, 21.750000), point2=(10.800000, 21.450000))
s0.Line(point1=(10.800000, 21.450000), point2=(10.800000, 20.250000))
s0.Line(point1=(10.800000, 20.250000), point2=(8.700000, 20.100000))
s0.Line(point1=(8.700000, 20.100000), point2=(7.350000, 20.400000))
s0.Line(point1=(7.350000, 20.400000), point2=(5.850000, 21.300000))
s0.Line(point1=(5.850000, 21.300000), point2=(5.850000, 22.050000))
s0.Line(point1=(5.712861, 22.142848), point2=(6.562861, 22.542848))
s0.Line(point1=(6.562861, 22.542848), point2=(10.000000, 22.450000))
s0.Line(point1=(10.000000, 22.450000), point2=(10.031623, 21.844868))
s0.Line(point1=(10.031623, 21.844868), point2=(10.931623, 21.544868))
s0.Line(point1=(10.931623, 21.544868), point2=(10.907125, 20.150254))
s0.Line(point1=(10.907125, 20.150254), point2=(8.685432, 19.902635))
s0.Line(point1=(8.685432, 19.902635), point2=(7.276857, 20.216632))
s0.Line(point1=(7.276857, 20.216632), point2=(5.698550, 21.214251))
s0.Line(point1=(5.698550, 21.214251), point2=(5.712861, 22.142848))
s0.Line(point1=(5.987139, 21.957152), point2=(6.637139, 22.157152))
s0.Line(point1=(6.637139, 22.157152), point2=(9.800000, 22.250000))
s0.Line(point1=(9.800000, 22.250000), point2=(9.768377, 21.655132))
s0.Line(point1=(9.768377, 21.655132), point2=(10.668377, 21.355132))
s0.Line(point1=(10.668377, 21.355132), point2=(10.692875, 20.349746))
s0.Line(point1=(10.692875, 20.349746), point2=(8.714568, 20.297365))
s0.Line(point1=(8.714568, 20.297365), point2=(7.423143, 20.583368))
s0.Line(point1=(7.423143, 20.583368), point2=(6.001450, 21.385749))
s0.Line(point1=(6.001450, 21.385749), point2=(5.987139, 21.957152))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(6.450000, 35.850000), point2=(8.100000, 36.000000))
s0.Line(point1=(8.100000, 36.000000), point2=(9.300000, 35.700000))
s0.Line(point1=(9.300000, 35.700000), point2=(9.900000, 34.350000))
s0.Line(point1=(9.900000, 34.350000), point2=(9.750000, 33.000000))
s0.Line(point1=(9.750000, 33.000000), point2=(8.550000, 32.850000))
s0.Line(point1=(8.550000, 32.850000), point2=(6.750000, 34.200000))
s0.Line(point1=(6.750000, 34.200000), point2=(6.450000, 35.850000))
s0.Line(point1=(6.342559, 35.931701), point2=(8.115200, 36.196604))
s0.Line(point1=(8.115200, 36.196604), point2=(9.415635, 35.837628))
s0.Line(point1=(9.415635, 35.837628), point2=(10.090770, 34.379571))
s0.Line(point1=(10.090770, 34.379571), point2=(9.861792, 32.889729))
s0.Line(point1=(9.861792, 32.889729), point2=(8.502403, 32.670772))
s0.Line(point1=(8.502403, 32.670772), point2=(6.591613, 34.102111))
s0.Line(point1=(6.591613, 34.102111), point2=(6.342559, 35.931701))
s0.Line(point1=(6.557441, 35.768299), point2=(8.084800, 35.803396))
s0.Line(point1=(8.084800, 35.803396), point2=(9.184365, 35.562372))
s0.Line(point1=(9.184365, 35.562372), point2=(9.709230, 34.320429))
s0.Line(point1=(9.709230, 34.320429), point2=(9.638208, 33.110271))
s0.Line(point1=(9.638208, 33.110271), point2=(8.597597, 33.029228))
s0.Line(point1=(8.597597, 33.029228), point2=(6.908387, 34.297889))
s0.Line(point1=(6.908387, 34.297889), point2=(6.557441, 35.768299))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
print 20
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(6.600000, 16.950000), point2=(7.350000, 16.650000))
s0.Line(point1=(7.350000, 16.650000), point2=(9.300000, 13.950000))
s0.Line(point1=(9.300000, 13.950000), point2=(9.300000, 12.750000))
s0.Line(point1=(9.300000, 12.750000), point2=(8.700000, 12.600000))
s0.Line(point1=(8.700000, 12.600000), point2=(8.700000, 12.300000))
s0.Line(point1=(8.700000, 12.300000), point2=(8.100000, 12.300000))
s0.Line(point1=(8.100000, 12.300000), point2=(7.500000, 13.500000))
s0.Line(point1=(7.500000, 13.500000), point2=(7.050000, 15.450000))
s0.Line(point1=(7.050000, 15.450000), point2=(6.600000, 16.050000))
s0.Line(point1=(6.600000, 16.050000), point2=(6.600000, 16.950000))
s0.Line(point1=(6.537139, 17.042848), point2=(7.468207, 16.801397))
s0.Line(point1=(7.468207, 16.801397), point2=(9.481068, 14.008549))
s0.Line(point1=(9.481068, 14.008549), point2=(9.424254, 12.652986))
s0.Line(point1=(9.424254, 12.652986), point2=(8.824254, 12.502986))
s0.Line(point1=(8.824254, 12.502986), point2=(8.800000, 12.200000))
s0.Line(point1=(8.800000, 12.200000), point2=(8.010557, 12.155279))
s0.Line(point1=(8.010557, 12.155279), point2=(7.313118, 13.432793))
s0.Line(point1=(7.313118, 13.432793), point2=(6.872561, 15.367514))
s0.Line(point1=(6.872561, 15.367514), point2=(6.420000, 15.990000))
s0.Line(point1=(6.420000, 15.990000), point2=(6.537139, 17.042848))
s0.Line(point1=(6.662861, 16.857152), point2=(7.231793, 16.498603))
s0.Line(point1=(7.231793, 16.498603), point2=(9.118932, 13.891451))
s0.Line(point1=(9.118932, 13.891451), point2=(9.175746, 12.847014))
s0.Line(point1=(9.175746, 12.847014), point2=(8.575746, 12.697014))
s0.Line(point1=(8.575746, 12.697014), point2=(8.600000, 12.400000))
s0.Line(point1=(8.600000, 12.400000), point2=(8.189443, 12.444721))
s0.Line(point1=(8.189443, 12.444721), point2=(7.686882, 13.567207))
s0.Line(point1=(7.686882, 13.567207), point2=(7.227439, 15.532486))
s0.Line(point1=(7.227439, 15.532486), point2=(6.780000, 16.110000))
s0.Line(point1=(6.780000, 16.110000), point2=(6.662861, 16.857152))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(7.500000, 19.350000), point2=(8.100000, 19.350000))
s0.Line(point1=(8.100000, 19.350000), point2=(7.950000, 17.700000))
s0.Line(point1=(7.950000, 17.700000), point2=(8.100000, 17.100000))
s0.Line(point1=(8.100000, 17.100000), point2=(8.400000, 17.100000))
s0.Line(point1=(8.400000, 17.100000), point2=(8.400000, 16.500000))
s0.Line(point1=(8.400000, 16.500000), point2=(7.650000, 16.650000))
s0.Line(point1=(7.650000, 16.650000), point2=(7.050000, 17.550000))
s0.Line(point1=(7.050000, 17.550000), point2=(7.050000, 18.900000))
s0.Line(point1=(7.050000, 18.900000), point2=(7.500000, 19.350000))
s0.Line(point1=(7.429289, 19.520711), point2=(8.199589, 19.440946))
s0.Line(point1=(8.199589, 19.440946), point2=(8.146604, 17.715200))
s0.Line(point1=(8.146604, 17.715200), point2=(8.197014, 17.224254))
s0.Line(point1=(8.197014, 17.224254), point2=(8.500000, 17.200000))
s0.Line(point1=(8.500000, 17.200000), point2=(8.480388, 16.401942))
s0.Line(point1=(8.480388, 16.401942), point2=(7.547183, 16.496472))
s0.Line(point1=(7.547183, 16.496472), point2=(6.866795, 17.494530))
s0.Line(point1=(6.866795, 17.494530), point2=(6.879289, 18.970711))
s0.Line(point1=(6.879289, 18.970711), point2=(7.429289, 19.520711))
s0.Line(point1=(7.570711, 19.179289), point2=(8.000411, 19.259054))
s0.Line(point1=(8.000411, 19.259054), point2=(7.753396, 17.684800))
s0.Line(point1=(7.753396, 17.684800), point2=(8.002986, 16.975746))
s0.Line(point1=(8.002986, 16.975746), point2=(8.300000, 17.000000))
s0.Line(point1=(8.300000, 17.000000), point2=(8.319612, 16.598058))
s0.Line(point1=(8.319612, 16.598058), point2=(7.752817, 16.803528))
s0.Line(point1=(7.752817, 16.803528), point2=(7.233205, 17.605470))
s0.Line(point1=(7.233205, 17.605470), point2=(7.220711, 18.829289))
s0.Line(point1=(7.220711, 18.829289), point2=(7.570711, 19.179289))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(12.000000, 46.050000), point2=(12.000000, 45.600000))
s0.Line(point1=(12.000000, 45.600000), point2=(10.950000, 45.150000))
s0.Line(point1=(10.950000, 45.150000), point2=(10.650000, 44.400000))
s0.Line(point1=(10.650000, 44.400000), point2=(8.850000, 42.900000))
s0.Line(point1=(8.850000, 42.900000), point2=(8.400000, 39.750000))
s0.Line(point1=(8.400000, 39.750000), point2=(8.100000, 39.000000))
s0.Line(point1=(8.100000, 39.000000), point2=(7.650000, 39.000000))
s0.Line(point1=(7.650000, 39.000000), point2=(7.650000, 41.850000))
s0.Line(point1=(7.650000, 41.850000), point2=(7.350000, 42.450000))
s0.Line(point1=(7.350000, 42.450000), point2=(7.350000, 43.500000))
s0.Line(point1=(7.350000, 43.500000), point2=(7.650000, 43.650000))
s0.Line(point1=(7.650000, 43.650000), point2=(7.500000, 44.850000))
s0.Line(point1=(7.500000, 44.850000), point2=(9.450000, 45.450000))
s0.Line(point1=(9.450000, 45.450000), point2=(10.200000, 46.350000))
s0.Line(point1=(10.200000, 46.350000), point2=(12.000000, 46.050000))
s0.Line(point1=(12.116440, 46.148639), point2=(12.139392, 45.508085))
s0.Line(point1=(12.139392, 45.508085), point2=(11.082240, 45.020946))
s0.Line(point1=(11.082240, 45.020946), point2=(10.806866, 44.286039))
s0.Line(point1=(10.806866, 44.286039), point2=(9.013013, 42.809036))
s0.Line(point1=(9.013013, 42.809036), point2=(8.591843, 39.698719))
s0.Line(point1=(8.591843, 39.698719), point2=(8.192848, 38.862861))
s0.Line(point1=(8.192848, 38.862861), point2=(7.550000, 38.900000))
s0.Line(point1=(7.550000, 38.900000), point2=(7.460557, 41.805279))
s0.Line(point1=(7.460557, 41.805279), point2=(7.160557, 42.405279))
s0.Line(point1=(7.160557, 42.405279), point2=(7.205279, 43.589443))
s0.Line(point1=(7.205279, 43.589443), point2=(7.506051, 43.727039))
s0.Line(point1=(7.506051, 43.727039), point2=(7.371364, 44.933174))
s0.Line(point1=(7.371364, 44.933174), point2=(9.343769, 45.609596))
s0.Line(point1=(9.343769, 45.609596), point2=(10.139618, 46.512658))
s0.Line(point1=(10.139618, 46.512658), point2=(12.116440, 46.148639))
s0.Line(point1=(11.883560, 45.951361), point2=(11.860608, 45.691915))
s0.Line(point1=(11.860608, 45.691915), point2=(10.817760, 45.279054))
s0.Line(point1=(10.817760, 45.279054), point2=(10.493134, 44.513961))
s0.Line(point1=(10.493134, 44.513961), point2=(8.686987, 42.990964))
s0.Line(point1=(8.686987, 42.990964), point2=(8.208157, 39.801281))
s0.Line(point1=(8.208157, 39.801281), point2=(8.007152, 39.137139))
s0.Line(point1=(8.007152, 39.137139), point2=(7.750000, 39.100000))
s0.Line(point1=(7.750000, 39.100000), point2=(7.839443, 41.894721))
s0.Line(point1=(7.839443, 41.894721), point2=(7.539443, 42.494721))
s0.Line(point1=(7.539443, 42.494721), point2=(7.494721, 43.410557))
s0.Line(point1=(7.494721, 43.410557), point2=(7.793949, 43.572961))
s0.Line(point1=(7.793949, 43.572961), point2=(7.628636, 44.766826))
s0.Line(point1=(7.628636, 44.766826), point2=(9.556231, 45.290404))
s0.Line(point1=(9.556231, 45.290404), point2=(10.260382, 46.187342))
s0.Line(point1=(10.260382, 46.187342), point2=(11.883560, 45.951361))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(8.100000, 49.500000), point2=(9.000000, 50.100000))
s0.Line(point1=(9.000000, 50.100000), point2=(10.200000, 50.100000))
s0.Line(point1=(10.200000, 50.100000), point2=(10.950000, 49.200000))
s0.Line(point1=(10.950000, 49.200000), point2=(10.500000, 48.450000))
s0.Line(point1=(10.500000, 48.450000), point2=(9.000000, 48.150000))
s0.Line(point1=(9.000000, 48.150000), point2=(8.100000, 49.500000))
s0.Line(point1=(7.961325, 49.527735), point2=(8.944530, 50.283205))
s0.Line(point1=(8.944530, 50.283205), point2=(10.276822, 50.264018))
s0.Line(point1=(10.276822, 50.264018), point2=(11.112571, 49.212569))
s0.Line(point1=(11.112571, 49.212569), point2=(10.605361, 48.300492))
s0.Line(point1=(10.605361, 48.300492), point2=(8.936407, 47.996472))
s0.Line(point1=(8.936407, 47.996472), point2=(7.961325, 49.527735))
s0.Line(point1=(8.238675, 49.472265), point2=(9.055470, 49.916795))
s0.Line(point1=(9.055470, 49.916795), point2=(10.123178, 49.935982))
s0.Line(point1=(10.123178, 49.935982), point2=(10.787429, 49.187431))
s0.Line(point1=(10.787429, 49.187431), point2=(10.394639, 48.599508))
s0.Line(point1=(10.394639, 48.599508), point2=(9.063593, 48.303528))
s0.Line(point1=(9.063593, 48.303528), point2=(8.238675, 49.472265))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(8.250000, 37.650000), point2=(9.300000, 38.400000))
s0.Line(point1=(9.300000, 38.400000), point2=(9.750000, 38.250000))
s0.Line(point1=(9.750000, 38.250000), point2=(10.800000, 36.750000))
s0.Line(point1=(10.800000, 36.750000), point2=(10.800000, 36.150000))
s0.Line(point1=(10.800000, 36.150000), point2=(10.200000, 36.000000))
s0.Line(point1=(10.200000, 36.000000), point2=(8.250000, 37.650000))
s0.Line(point1=(8.127282, 37.655035), point2=(9.273499, 38.576242))
s0.Line(point1=(9.273499, 38.576242), point2=(9.863546, 38.402215))
s0.Line(point1=(9.863546, 38.402215), point2=(10.981923, 36.807346))
s0.Line(point1=(10.981923, 36.807346), point2=(10.924254, 36.052986))
s0.Line(point1=(10.924254, 36.052986), point2=(10.159659, 35.826647))
s0.Line(point1=(10.159659, 35.826647), point2=(8.127282, 37.655035))
s0.Line(point1=(8.372718, 37.644965), point2=(9.326501, 38.223758))
s0.Line(point1=(9.326501, 38.223758), point2=(9.636454, 38.097785))
s0.Line(point1=(9.636454, 38.097785), point2=(10.618077, 36.692654))
s0.Line(point1=(10.618077, 36.692654), point2=(10.675746, 36.247014))
s0.Line(point1=(10.675746, 36.247014), point2=(10.240341, 36.173353))
s0.Line(point1=(10.240341, 36.173353), point2=(8.372718, 37.644965))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(8.550000, 18.750000), point2=(9.750000, 19.650000))
s0.Line(point1=(9.750000, 19.650000), point2=(11.100000, 19.800000))
s0.Line(point1=(11.100000, 19.800000), point2=(11.550000, 18.300000))
s0.Line(point1=(11.550000, 18.300000), point2=(10.950000, 17.700000))
s0.Line(point1=(10.950000, 17.700000), point2=(10.050000, 17.550000))
s0.Line(point1=(10.050000, 17.550000), point2=(9.000000, 17.850000))
s0.Line(point1=(9.000000, 17.850000), point2=(8.550000, 18.750000))
s0.Line(point1=(8.400557, 18.785279), point2=(9.678957, 19.829388))
s0.Line(point1=(9.678957, 19.829388), point2=(11.184739, 19.928123))
s0.Line(point1=(11.184739, 19.928123), point2=(11.716493, 18.258024))
s0.Line(point1=(11.716493, 18.258024), point2=(11.037151, 17.530650))
s0.Line(point1=(11.037151, 17.530650), point2=(10.038968, 17.355208))
s0.Line(point1=(10.038968, 17.355208), point2=(8.883085, 17.709126))
s0.Line(point1=(8.883085, 17.709126), point2=(8.400557, 18.785279))
s0.Line(point1=(8.699443, 18.714721), point2=(9.821043, 19.470612))
s0.Line(point1=(9.821043, 19.470612), point2=(11.015261, 19.671877))
s0.Line(point1=(11.015261, 19.671877), point2=(11.383507, 18.341976))
s0.Line(point1=(11.383507, 18.341976), point2=(10.862849, 17.869350))
s0.Line(point1=(10.862849, 17.869350), point2=(10.061032, 17.744792))
s0.Line(point1=(10.061032, 17.744792), point2=(9.116915, 17.990874))
s0.Line(point1=(9.116915, 17.990874), point2=(8.699443, 18.714721))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(10.500000, 43.950000), point2=(11.100000, 44.100000))
s0.Line(point1=(11.100000, 44.100000), point2=(11.850000, 42.900000))
s0.Line(point1=(11.850000, 42.900000), point2=(12.450000, 42.600000))
s0.Line(point1=(12.450000, 42.600000), point2=(13.050000, 41.550000))
s0.Line(point1=(13.050000, 41.550000), point2=(13.200000, 40.350000))
s0.Line(point1=(13.200000, 40.350000), point2=(11.700000, 40.800000))
s0.Line(point1=(11.700000, 40.800000), point2=(10.050000, 42.150000))
s0.Line(point1=(10.050000, 42.150000), point2=(9.900000, 42.900000))
s0.Line(point1=(9.900000, 42.900000), point2=(10.500000, 43.950000))
s0.Line(point1=(10.388922, 44.096628), point2=(11.160546, 44.250014))
s0.Line(point1=(11.160546, 44.250014), point2=(11.979521, 43.042443))
s0.Line(point1=(11.979521, 43.042443), point2=(12.581546, 42.739057))
s0.Line(point1=(12.581546, 42.739057), point2=(13.236052, 41.612017))
s0.Line(point1=(13.236052, 41.612017), point2=(13.270493, 40.266621))
s0.Line(point1=(13.270493, 40.266621), point2=(11.607941, 40.626822))
s0.Line(point1=(11.607941, 40.626822), point2=(9.888618, 42.052993))
s0.Line(point1=(9.888618, 42.052993), point2=(9.715118, 42.930002))
s0.Line(point1=(9.715118, 42.930002), point2=(10.388922, 44.096628))
s0.Line(point1=(10.611078, 43.803372), point2=(11.039454, 43.949986))
s0.Line(point1=(11.039454, 43.949986), point2=(11.720479, 42.757557))
s0.Line(point1=(11.720479, 42.757557), point2=(12.318454, 42.460943))
s0.Line(point1=(12.318454, 42.460943), point2=(12.863948, 41.487983))
s0.Line(point1=(12.863948, 41.487983), point2=(13.129507, 40.433379))
s0.Line(point1=(13.129507, 40.433379), point2=(11.792059, 40.973178))
s0.Line(point1=(11.792059, 40.973178), point2=(10.211382, 42.247007))
s0.Line(point1=(10.211382, 42.247007), point2=(10.084882, 42.869998))
s0.Line(point1=(10.084882, 42.869998), point2=(10.611078, 43.803372))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(10.200000, 24.750000), point2=(10.950000, 25.350000))
s0.Line(point1=(10.950000, 25.350000), point2=(11.850000, 25.350000))
s0.Line(point1=(11.850000, 25.350000), point2=(13.500000, 24.750000))
s0.Line(point1=(13.500000, 24.750000), point2=(15.450000, 23.400000))
s0.Line(point1=(15.450000, 23.400000), point2=(15.900000, 22.200000))
s0.Line(point1=(15.900000, 22.200000), point2=(15.750000, 21.450000))
s0.Line(point1=(15.750000, 21.450000), point2=(15.300000, 21.000000))
s0.Line(point1=(15.300000, 21.000000), point2=(13.500000, 21.000000))
s0.Line(point1=(13.500000, 21.000000), point2=(12.300000, 21.900000))
s0.Line(point1=(12.300000, 21.900000), point2=(12.300000, 22.200000))
s0.Line(point1=(12.300000, 22.200000), point2=(10.500000, 23.250000))
s0.Line(point1=(10.500000, 23.250000), point2=(10.200000, 24.750000))
s0.Line(point1=(10.039472, 24.808475), point2=(10.887530, 25.528087))
s0.Line(point1=(10.887530, 25.528087), point2=(11.884174, 25.543979))
s0.Line(point1=(11.884174, 25.543979), point2=(13.591095, 24.926199))
s0.Line(point1=(13.591095, 24.926199), point2=(15.600554, 23.517332))
s0.Line(point1=(15.600554, 23.517332), point2=(16.091691, 22.215501))
s0.Line(point1=(16.091691, 22.215501), point2=(15.918769, 21.359678))
s0.Line(point1=(15.918769, 21.359678), point2=(15.370711, 20.829289))
s0.Line(point1=(15.370711, 20.829289), point2=(13.440000, 20.820000))
s0.Line(point1=(13.440000, 20.820000), point2=(12.140000, 21.820000))
s0.Line(point1=(12.140000, 21.820000), point2=(12.149613, 22.113622))
s0.Line(point1=(12.149613, 22.113622), point2=(10.351555, 23.144010))
s0.Line(point1=(10.351555, 23.144010), point2=(10.039472, 24.808475))
s0.Line(point1=(10.360528, 24.691525), point2=(11.012470, 25.171913))
s0.Line(point1=(11.012470, 25.171913), point2=(11.815826, 25.156021))
s0.Line(point1=(11.815826, 25.156021), point2=(13.408905, 24.573801))
s0.Line(point1=(13.408905, 24.573801), point2=(15.299446, 23.282668))
s0.Line(point1=(15.299446, 23.282668), point2=(15.708309, 22.184499))
s0.Line(point1=(15.708309, 22.184499), point2=(15.581231, 21.540322))
s0.Line(point1=(15.581231, 21.540322), point2=(15.229289, 21.170711))
s0.Line(point1=(15.229289, 21.170711), point2=(13.560000, 21.180000))
s0.Line(point1=(13.560000, 21.180000), point2=(12.460000, 21.980000))
s0.Line(point1=(12.460000, 21.980000), point2=(12.450387, 22.286378))
s0.Line(point1=(12.450387, 22.286378), point2=(10.648445, 23.355990))
s0.Line(point1=(10.648445, 23.355990), point2=(10.360528, 24.691525))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(10.350000, 16.500000), point2=(10.950000, 16.500000))
s0.Line(point1=(10.950000, 16.500000), point2=(11.550000, 15.150000))
s0.Line(point1=(11.550000, 15.150000), point2=(12.000000, 15.150000))
s0.Line(point1=(12.000000, 15.150000), point2=(11.700000, 10.200000))
s0.Line(point1=(11.700000, 10.200000), point2=(10.800000, 10.350000))
s0.Line(point1=(10.800000, 10.350000), point2=(10.200000, 11.250000))
s0.Line(point1=(10.200000, 11.250000), point2=(10.200000, 12.600000))
s0.Line(point1=(10.200000, 12.600000), point2=(10.650000, 13.050000))
s0.Line(point1=(10.650000, 13.050000), point2=(10.200000, 15.000000))
s0.Line(point1=(10.200000, 15.000000), point2=(10.350000, 16.500000))
s0.Line(point1=(10.250496, 16.609950), point2=(11.041381, 16.640614))
s0.Line(point1=(11.041381, 16.640614), point2=(11.641381, 15.290614))
s0.Line(point1=(11.641381, 15.290614), point2=(12.099817, 15.243950))
s0.Line(point1=(12.099817, 15.243950), point2=(11.783377, 10.095311))
s0.Line(point1=(11.783377, 10.095311), point2=(10.700355, 10.195891))
s0.Line(point1=(10.700355, 10.195891), point2=(10.016795, 11.194530))
s0.Line(point1=(10.016795, 11.194530), point2=(10.029289, 12.670711))
s0.Line(point1=(10.029289, 12.670711), point2=(10.481850, 13.098225))
s0.Line(point1=(10.481850, 13.098225), point2=(10.003057, 14.987464))
s0.Line(point1=(10.003057, 14.987464), point2=(10.250496, 16.609950))
s0.Line(point1=(10.449504, 16.390050), point2=(10.858619, 16.359386))
s0.Line(point1=(10.858619, 16.359386), point2=(11.458619, 15.009386))
s0.Line(point1=(11.458619, 15.009386), point2=(11.900183, 15.056050))
s0.Line(point1=(11.900183, 15.056050), point2=(11.616623, 10.304689))
s0.Line(point1=(11.616623, 10.304689), point2=(10.899645, 10.504109))
s0.Line(point1=(10.899645, 10.504109), point2=(10.383205, 11.305470))
s0.Line(point1=(10.383205, 11.305470), point2=(10.370711, 12.529289))
s0.Line(point1=(10.370711, 12.529289), point2=(10.818150, 13.001775))
s0.Line(point1=(10.818150, 13.001775), point2=(10.396943, 15.012536))
s0.Line(point1=(10.396943, 15.012536), point2=(10.449504, 16.390050))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(10.200000, 8.700000), point2=(10.800000, 9.450000))
s0.Line(point1=(10.800000, 9.450000), point2=(11.400000, 9.600000))
s0.Line(point1=(11.400000, 9.600000), point2=(12.150000, 9.000000))
s0.Line(point1=(12.150000, 9.000000), point2=(12.150000, 8.100000))
s0.Line(point1=(12.150000, 8.100000), point2=(10.950000, 7.800000))
s0.Line(point1=(10.950000, 7.800000), point2=(10.350000, 8.100000))
s0.Line(point1=(10.350000, 8.100000), point2=(10.200000, 8.700000))
s0.Line(point1=(10.024899, 8.738216), point2=(10.697660, 9.609484))
s0.Line(point1=(10.697660, 9.609484), point2=(11.438216, 9.775101))
s0.Line(point1=(11.438216, 9.775101), point2=(12.312470, 9.078087))
s0.Line(point1=(12.312470, 9.078087), point2=(12.274254, 8.002986))
s0.Line(point1=(12.274254, 8.002986), point2=(10.929532, 7.613543))
s0.Line(point1=(10.929532, 7.613543), point2=(10.208264, 7.986304))
s0.Line(point1=(10.208264, 7.986304), point2=(10.024899, 8.738216))
s0.Line(point1=(10.375101, 8.661784), point2=(10.902340, 9.290516))
s0.Line(point1=(10.902340, 9.290516), point2=(11.361784, 9.424899))
s0.Line(point1=(11.361784, 9.424899), point2=(11.987530, 8.921913))
s0.Line(point1=(11.987530, 8.921913), point2=(12.025746, 8.197014))
s0.Line(point1=(12.025746, 8.197014), point2=(10.970468, 7.986457))
s0.Line(point1=(10.970468, 7.986457), point2=(10.491736, 8.213696))
s0.Line(point1=(10.491736, 8.213696), point2=(10.375101, 8.661784))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(10.500000, 51.600000), point2=(11.250000, 51.750000))
s0.Line(point1=(11.250000, 51.750000), point2=(11.700000, 51.300000))
s0.Line(point1=(11.700000, 51.300000), point2=(11.550000, 50.100000))
s0.Line(point1=(11.550000, 50.100000), point2=(10.500000, 50.550000))
s0.Line(point1=(10.500000, 50.550000), point2=(10.500000, 51.600000))
s0.Line(point1=(10.380388, 51.698058), point2=(11.301099, 51.918769))
s0.Line(point1=(11.301099, 51.918769), point2=(11.869938, 51.358307))
s0.Line(point1=(11.869938, 51.358307), point2=(11.609836, 49.995682))
s0.Line(point1=(11.609836, 49.995682), point2=(10.360608, 50.458085))
s0.Line(point1=(10.360608, 50.458085), point2=(10.380388, 51.698058))
s0.Line(point1=(10.619612, 51.501942), point2=(11.198901, 51.581231))
s0.Line(point1=(11.198901, 51.581231), point2=(11.530062, 51.241693))
s0.Line(point1=(11.530062, 51.241693), point2=(11.490164, 50.204318))
s0.Line(point1=(11.490164, 50.204318), point2=(10.639392, 50.641915))
s0.Line(point1=(10.639392, 50.641915), point2=(10.619612, 51.501942))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(13.350000, 49.800000), point2=(13.350000, 49.200000))
s0.Line(point1=(13.350000, 49.200000), point2=(12.900000, 49.200000))
s0.Line(point1=(12.900000, 49.200000), point2=(12.600000, 48.750000))
s0.Line(point1=(12.600000, 48.750000), point2=(11.250000, 48.900000))
s0.Line(point1=(11.250000, 48.900000), point2=(12.450000, 50.100000))
s0.Line(point1=(12.450000, 50.100000), point2=(13.350000, 49.800000))
s0.Line(point1=(13.481623, 49.894868), point2=(13.450000, 49.100000))
s0.Line(point1=(13.450000, 49.100000), point2=(12.983205, 49.044530))
s0.Line(point1=(12.983205, 49.044530), point2=(12.672162, 48.595142))
s0.Line(point1=(12.672162, 48.595142), point2=(11.168246, 48.871322))
s0.Line(point1=(11.168246, 48.871322), point2=(12.410912, 50.265579))
s0.Line(point1=(12.410912, 50.265579), point2=(13.481623, 49.894868))
s0.Line(point1=(13.218377, 49.705132), point2=(13.250000, 49.300000))
s0.Line(point1=(13.250000, 49.300000), point2=(12.816795, 49.355470))
s0.Line(point1=(12.816795, 49.355470), point2=(12.527838, 48.904858))
s0.Line(point1=(12.527838, 48.904858), point2=(11.331754, 48.928678))
s0.Line(point1=(11.331754, 48.928678), point2=(12.489088, 49.934421))
s0.Line(point1=(12.489088, 49.934421), point2=(13.218377, 49.705132))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(11.550000, 38.100000), point2=(12.750000, 37.950000))
s0.Line(point1=(12.750000, 37.950000), point2=(13.200000, 37.500000))
s0.Line(point1=(13.200000, 37.500000), point2=(13.200000, 36.600000))
s0.Line(point1=(13.200000, 36.600000), point2=(11.700000, 36.450000))
s0.Line(point1=(11.700000, 36.450000), point2=(11.250000, 37.050000))
s0.Line(point1=(11.250000, 37.050000), point2=(11.550000, 38.100000))
s0.Line(point1=(11.466251, 38.226700), point2=(12.833114, 38.119938))
s0.Line(point1=(12.833114, 38.119938), point2=(13.370711, 37.570711))
s0.Line(point1=(13.370711, 37.570711), point2=(13.309950, 36.500496))
s0.Line(point1=(13.309950, 36.500496), point2=(11.629950, 36.290496))
s0.Line(point1=(11.629950, 36.290496), point2=(11.073848, 37.017472))
s0.Line(point1=(11.073848, 37.017472), point2=(11.466251, 38.226700))
s0.Line(point1=(11.633749, 37.973300), point2=(12.666886, 37.780062))
s0.Line(point1=(12.666886, 37.780062), point2=(13.029289, 37.429289))
s0.Line(point1=(13.029289, 37.429289), point2=(13.090050, 36.699504))
s0.Line(point1=(13.090050, 36.699504), point2=(11.770050, 36.609504))
s0.Line(point1=(11.770050, 36.609504), point2=(11.426152, 37.082528))
s0.Line(point1=(11.426152, 37.082528), point2=(11.633749, 37.973300))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(15.300000, 0.750000), point2=(15.300000, 0.000000))
s0.Line(point1=(15.300000, 0.000000), point2=(11.250000, 0.000000))
s0.Line(point1=(11.250000, 0.000000), point2=(11.400000, 0.750000))
s0.Line(point1=(11.400000, 0.750000), point2=(13.050000, 2.100000))
s0.Line(point1=(13.050000, 2.100000), point2=(14.250000, 2.250000))
s0.Line(point1=(14.250000, 2.250000), point2=(15.300000, 0.750000))
s0.Line(point1=(15.481923, 0.807346), point2=(15.400000, 0.000000))
s0.Line(point1=(15.400000, 0.000000), point2=(11.151942, 0.000000))
s0.Line(point1=(11.151942, 0.000000), point2=(11.238618, 0.847007))
s0.Line(point1=(11.238618, 0.847007), point2=(12.974273, 2.276624))
s0.Line(point1=(12.974273, 2.276624), point2=(14.319520, 2.406574))
s0.Line(point1=(14.319520, 2.406574), point2=(15.481923, 0.807346))
s0.Line(point1=(15.118077, 0.692654), point2=(15.200000, 0.000000))
s0.Line(point1=(15.200000, 0.000000), point2=(11.348058, 0.000000))
s0.Line(point1=(11.348058, 0.000000), point2=(11.561382, 0.652993))
s0.Line(point1=(11.561382, 0.652993), point2=(13.125727, 1.923376))
s0.Line(point1=(13.125727, 1.923376), point2=(14.180480, 2.093426))
s0.Line(point1=(14.180480, 2.093426), point2=(15.118077, 0.692654))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(11.400000, 33.750000), point2=(14.100000, 35.550000))
s0.Line(point1=(14.100000, 35.550000), point2=(14.700000, 35.400000))
s0.Line(point1=(14.700000, 35.400000), point2=(16.200000, 34.350000))
s0.Line(point1=(16.200000, 34.350000), point2=(17.700000, 34.050000))
s0.Line(point1=(17.700000, 34.050000), point2=(18.600000, 33.300000))
s0.Line(point1=(18.600000, 33.300000), point2=(18.600000, 32.550000))
s0.Line(point1=(18.600000, 32.550000), point2=(19.350000, 31.650000))
s0.Line(point1=(19.350000, 31.650000), point2=(19.350000, 30.450000))
s0.Line(point1=(19.350000, 30.450000), point2=(18.600000, 29.550000))
s0.Line(point1=(18.600000, 29.550000), point2=(16.500000, 28.650000))
s0.Line(point1=(16.500000, 28.650000), point2=(16.200000, 28.050000))
s0.Line(point1=(16.200000, 28.050000), point2=(15.000000, 28.200000))
s0.Line(point1=(15.000000, 28.200000), point2=(13.800000, 29.400000))
s0.Line(point1=(13.800000, 29.400000), point2=(13.800000, 30.750000))
s0.Line(point1=(13.800000, 30.750000), point2=(13.050000, 32.100000))
s0.Line(point1=(13.050000, 32.100000), point2=(11.700000, 33.000000))
s0.Line(point1=(11.700000, 33.000000), point2=(11.400000, 33.750000))
s0.Line(point1=(11.251682, 33.796066), point2=(14.068784, 35.730219))
s0.Line(point1=(14.068784, 35.730219), point2=(14.781600, 35.578937))
s0.Line(point1=(14.781600, 35.578937), point2=(16.276958, 34.529981))
s0.Line(point1=(16.276958, 34.529981), point2=(17.783630, 34.224880))
s0.Line(point1=(17.783630, 34.224880), point2=(18.764018, 33.376822))
s0.Line(point1=(18.764018, 33.376822), point2=(18.776822, 32.614018))
s0.Line(point1=(18.776822, 32.614018), point2=(19.526822, 31.714018))
s0.Line(point1=(19.526822, 31.714018), point2=(19.526822, 30.385982))
s0.Line(point1=(19.526822, 30.385982), point2=(18.716214, 29.394067))
s0.Line(point1=(18.716214, 29.394067), point2=(16.628835, 28.513364))
s0.Line(point1=(16.628835, 28.513364), point2=(16.277039, 27.906051))
s0.Line(point1=(16.277039, 27.906051), point2=(14.916886, 28.030062))
s0.Line(point1=(14.916886, 28.030062), point2=(13.629289, 29.329289))
s0.Line(point1=(13.629289, 29.329289), point2=(13.612584, 30.701436))
s0.Line(point1=(13.612584, 30.701436), point2=(12.907114, 31.968231))
s0.Line(point1=(12.907114, 31.968231), point2=(11.551682, 32.879656))
s0.Line(point1=(11.551682, 32.879656), point2=(11.251682, 33.796066))
s0.Line(point1=(11.548318, 33.703934), point2=(14.131216, 35.369781))
s0.Line(point1=(14.131216, 35.369781), point2=(14.618400, 35.221063))
s0.Line(point1=(14.618400, 35.221063), point2=(16.123042, 34.170019))
s0.Line(point1=(16.123042, 34.170019), point2=(17.616370, 33.875120))
s0.Line(point1=(17.616370, 33.875120), point2=(18.435982, 33.223178))
s0.Line(point1=(18.435982, 33.223178), point2=(18.423178, 32.485982))
s0.Line(point1=(18.423178, 32.485982), point2=(19.173178, 31.585982))
s0.Line(point1=(19.173178, 31.585982), point2=(19.173178, 30.514018))
s0.Line(point1=(19.173178, 30.514018), point2=(18.483786, 29.705933))
s0.Line(point1=(18.483786, 29.705933), point2=(16.371165, 28.786636))
s0.Line(point1=(16.371165, 28.786636), point2=(16.122961, 28.193949))
s0.Line(point1=(16.122961, 28.193949), point2=(15.083114, 28.369938))
s0.Line(point1=(15.083114, 28.369938), point2=(13.970711, 29.470711))
s0.Line(point1=(13.970711, 29.470711), point2=(13.987416, 30.798564))
s0.Line(point1=(13.987416, 30.798564), point2=(13.192886, 32.231769))
s0.Line(point1=(13.192886, 32.231769), point2=(11.848318, 33.120344))
s0.Line(point1=(11.848318, 33.120344), point2=(11.548318, 33.703934))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(15.150000, 6.150000), point2=(15.150000, 4.800000))
s0.Line(point1=(15.150000, 4.800000), point2=(14.400000, 4.200000))
s0.Line(point1=(14.400000, 4.200000), point2=(14.250000, 3.000000))
s0.Line(point1=(14.250000, 3.000000), point2=(13.350000, 2.700000))
s0.Line(point1=(13.350000, 2.700000), point2=(11.550000, 3.300000))
s0.Line(point1=(11.550000, 3.300000), point2=(11.550000, 4.350000))
s0.Line(point1=(11.550000, 4.350000), point2=(12.150000, 5.100000))
s0.Line(point1=(12.150000, 5.100000), point2=(13.800000, 5.550000))
s0.Line(point1=(13.800000, 5.550000), point2=(13.950000, 6.000000))
s0.Line(point1=(13.950000, 6.000000), point2=(15.150000, 6.150000))
s0.Line(point1=(15.237597, 6.249228), point2=(15.312470, 4.721913))
s0.Line(point1=(15.312470, 4.721913), point2=(14.561697, 4.109510))
s0.Line(point1=(14.561697, 4.109510), point2=(14.380851, 2.892728))
s0.Line(point1=(14.380851, 2.892728), point2=(13.350000, 2.510263))
s0.Line(point1=(13.350000, 2.510263), point2=(11.418377, 3.205132))
s0.Line(point1=(11.418377, 3.205132), point2=(11.371913, 4.412470))
s0.Line(point1=(11.371913, 4.412470), point2=(12.045601, 5.258946))
s0.Line(point1=(12.045601, 5.258946), point2=(13.678820, 5.678099))
s0.Line(point1=(13.678820, 5.678099), point2=(13.842728, 6.130851))
s0.Line(point1=(13.842728, 6.130851), point2=(15.237597, 6.249228))
s0.Line(point1=(15.062403, 6.050772), point2=(14.987530, 4.878087))
s0.Line(point1=(14.987530, 4.878087), point2=(14.238303, 4.290490))
s0.Line(point1=(14.238303, 4.290490), point2=(14.119149, 3.107272))
s0.Line(point1=(14.119149, 3.107272), point2=(13.350000, 2.889737))
s0.Line(point1=(13.350000, 2.889737), point2=(11.681623, 3.394868))
s0.Line(point1=(11.681623, 3.394868), point2=(11.728087, 4.287530))
s0.Line(point1=(11.728087, 4.287530), point2=(12.254399, 4.941054))
s0.Line(point1=(12.254399, 4.941054), point2=(13.921180, 5.421901))
s0.Line(point1=(13.921180, 5.421901), point2=(14.057272, 5.869149))
s0.Line(point1=(14.057272, 5.869149), point2=(15.062403, 6.050772))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(17.700000, 20.400000), point2=(17.700000, 19.800000))
s0.Line(point1=(17.700000, 19.800000), point2=(16.200000, 19.050000))
s0.Line(point1=(16.200000, 19.050000), point2=(14.400000, 16.800000))
s0.Line(point1=(14.400000, 16.800000), point2=(12.900000, 16.650000))
s0.Line(point1=(12.900000, 16.650000), point2=(12.900000, 17.250000))
s0.Line(point1=(12.900000, 17.250000), point2=(11.850000, 17.250000))
s0.Line(point1=(11.850000, 17.250000), point2=(12.000000, 18.000000))
s0.Line(point1=(12.000000, 18.000000), point2=(13.800000, 18.750000))
s0.Line(point1=(13.800000, 18.750000), point2=(14.550000, 19.200000))
s0.Line(point1=(14.550000, 19.200000), point2=(14.550000, 19.500000))
s0.Line(point1=(14.550000, 19.500000), point2=(15.450000, 19.650000))
s0.Line(point1=(15.450000, 19.650000), point2=(16.350000, 20.550000))
s0.Line(point1=(16.350000, 20.550000), point2=(17.700000, 20.400000))
s0.Line(point1=(17.811043, 20.499388), point2=(17.844721, 19.710557))
s0.Line(point1=(17.844721, 19.710557), point2=(16.322808, 18.898088))
s0.Line(point1=(16.322808, 18.898088), point2=(14.488037, 16.638027))
s0.Line(point1=(14.488037, 16.638027), point2=(12.809950, 16.550496))
s0.Line(point1=(12.809950, 16.550496), point2=(12.800000, 17.150000))
s0.Line(point1=(12.800000, 17.150000), point2=(11.751942, 17.169612))
s0.Line(point1=(11.751942, 17.169612), point2=(11.863480, 18.111919))
s0.Line(point1=(11.863480, 18.111919), point2=(13.710089, 18.928057))
s0.Line(point1=(13.710089, 18.928057), point2=(14.398550, 19.285749))
s0.Line(point1=(14.398550, 19.285749), point2=(14.433560, 19.598639))
s0.Line(point1=(14.433560, 19.598639), point2=(15.362849, 19.819350))
s0.Line(point1=(15.362849, 19.819350), point2=(16.290332, 20.720099))
s0.Line(point1=(16.290332, 20.720099), point2=(17.811043, 20.499388))
s0.Line(point1=(17.588957, 20.300612), point2=(17.555279, 19.889443))
s0.Line(point1=(17.555279, 19.889443), point2=(16.077192, 19.201912))
s0.Line(point1=(16.077192, 19.201912), point2=(14.311963, 16.961973))
s0.Line(point1=(14.311963, 16.961973), point2=(12.990050, 16.749504))
s0.Line(point1=(12.990050, 16.749504), point2=(13.000000, 17.350000))
s0.Line(point1=(13.000000, 17.350000), point2=(11.948058, 17.330388))
s0.Line(point1=(11.948058, 17.330388), point2=(12.136520, 17.888081))
s0.Line(point1=(12.136520, 17.888081), point2=(13.889911, 18.571943))
s0.Line(point1=(13.889911, 18.571943), point2=(14.701450, 19.114251))
s0.Line(point1=(14.701450, 19.114251), point2=(14.666440, 19.401361))
s0.Line(point1=(14.666440, 19.401361), point2=(15.537151, 19.480650))
s0.Line(point1=(15.537151, 19.480650), point2=(16.409668, 20.379901))
s0.Line(point1=(16.409668, 20.379901), point2=(17.588957, 20.300612))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(12.300000, 30.000000), point2=(12.750000, 30.000000))
s0.Line(point1=(12.750000, 30.000000), point2=(13.200000, 28.950000))
s0.Line(point1=(13.200000, 28.950000), point2=(14.250000, 28.050000))
s0.Line(point1=(14.250000, 28.050000), point2=(14.250000, 25.350000))
s0.Line(point1=(14.250000, 25.350000), point2=(13.950000, 25.050000))
s0.Line(point1=(13.950000, 25.050000), point2=(13.500000, 25.200000))
s0.Line(point1=(13.500000, 25.200000), point2=(12.600000, 26.850000))
s0.Line(point1=(12.600000, 26.850000), point2=(12.000000, 26.850000))
s0.Line(point1=(12.000000, 26.850000), point2=(12.300000, 30.000000))
s0.Line(point1=(12.200450, 30.109481), point2=(12.841915, 30.139392))
s0.Line(point1=(12.841915, 30.139392), point2=(13.356994, 29.065318))
s0.Line(point1=(13.356994, 29.065318), point2=(14.415079, 28.125926))
s0.Line(point1=(14.415079, 28.125926), point2=(14.420711, 25.279289))
s0.Line(point1=(14.420711, 25.279289), point2=(13.989088, 24.884421))
s0.Line(point1=(13.989088, 24.884421), point2=(13.380588, 25.057246))
s0.Line(point1=(13.380588, 25.057246), point2=(12.512210, 26.702115))
s0.Line(point1=(12.512210, 26.702115), point2=(11.900450, 26.759481))
s0.Line(point1=(11.900450, 26.759481), point2=(12.200450, 30.109481))
s0.Line(point1=(12.399550, 29.890519), point2=(12.658085, 29.860608))
s0.Line(point1=(12.658085, 29.860608), point2=(13.043006, 28.834682))
s0.Line(point1=(13.043006, 28.834682), point2=(14.084921, 27.974074))
s0.Line(point1=(14.084921, 27.974074), point2=(14.079289, 25.420711))
s0.Line(point1=(14.079289, 25.420711), point2=(13.910912, 25.215579))
s0.Line(point1=(13.910912, 25.215579), point2=(13.619412, 25.342754))
s0.Line(point1=(13.619412, 25.342754), point2=(12.687790, 26.997885))
s0.Line(point1=(12.687790, 26.997885), point2=(12.099550, 26.940519))
s0.Line(point1=(12.099550, 26.940519), point2=(12.399550, 29.890519))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(15.150000, 40.950000), point2=(14.550000, 39.000000))
s0.Line(point1=(14.550000, 39.000000), point2=(12.450000, 39.150000))
s0.Line(point1=(12.450000, 39.150000), point2=(12.900000, 40.050000))
s0.Line(point1=(12.900000, 40.050000), point2=(14.250000, 40.350000))
s0.Line(point1=(14.250000, 40.350000), point2=(14.250000, 40.650000))
s0.Line(point1=(14.250000, 40.650000), point2=(15.150000, 40.950000))
s0.Line(point1=(15.213955, 41.015460), point2=(14.638453, 38.870846))
s0.Line(point1=(14.638453, 38.870846), point2=(12.353433, 39.094975))
s0.Line(point1=(12.353433, 39.094975), point2=(12.788864, 40.192340))
s0.Line(point1=(12.788864, 40.192340), point2=(14.128307, 40.447619))
s0.Line(point1=(14.128307, 40.447619), point2=(14.118377, 40.744868))
s0.Line(point1=(14.118377, 40.744868), point2=(15.213955, 41.015460))
s0.Line(point1=(15.086045, 40.884540), point2=(14.461547, 39.129154))
s0.Line(point1=(14.461547, 39.129154), point2=(12.546567, 39.205025))
s0.Line(point1=(12.546567, 39.205025), point2=(13.011136, 39.907660))
s0.Line(point1=(13.011136, 39.907660), point2=(14.371693, 40.252381))
s0.Line(point1=(14.371693, 40.252381), point2=(14.381623, 40.555132))
s0.Line(point1=(14.381623, 40.555132), point2=(15.086045, 40.884540))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(12.750000, 14.250000), point2=(15.150000, 13.350000))
s0.Line(point1=(15.150000, 13.350000), point2=(16.800000, 11.700000))
s0.Line(point1=(16.800000, 11.700000), point2=(16.800000, 10.650000))
s0.Line(point1=(16.800000, 10.650000), point2=(15.150000, 8.850000))
s0.Line(point1=(15.150000, 8.850000), point2=(13.500000, 6.000000))
s0.Line(point1=(13.500000, 6.000000), point2=(12.900000, 6.900000))
s0.Line(point1=(12.900000, 6.900000), point2=(13.200000, 13.200000))
s0.Line(point1=(13.200000, 13.200000), point2=(12.900000, 13.350000))
s0.Line(point1=(12.900000, 13.350000), point2=(12.750000, 14.250000))
s0.Line(point1=(12.686473, 14.327193), point2=(15.255823, 13.514344))
s0.Line(point1=(15.255823, 13.514344), point2=(16.970711, 11.770711))
s0.Line(point1=(16.970711, 11.770711), point2=(16.973715, 10.582428))
s0.Line(point1=(16.973715, 10.582428), point2=(15.310258, 8.732324))
s0.Line(point1=(15.310258, 8.732324), point2=(13.503338, 5.894426))
s0.Line(point1=(13.503338, 5.894426), point2=(12.716908, 6.849286))
s0.Line(point1=(12.716908, 6.849286), point2=(13.055392, 13.115314))
s0.Line(point1=(13.055392, 13.115314), point2=(12.756639, 13.244117))
s0.Line(point1=(12.756639, 13.244117), point2=(12.686473, 14.327193))
s0.Line(point1=(12.813527, 14.172807), point2=(15.044177, 13.185656))
s0.Line(point1=(15.044177, 13.185656), point2=(16.629289, 11.629289))
s0.Line(point1=(16.629289, 11.629289), point2=(16.626285, 10.717572))
s0.Line(point1=(16.626285, 10.717572), point2=(14.989742, 8.967676))
s0.Line(point1=(14.989742, 8.967676), point2=(13.496662, 6.105574))
s0.Line(point1=(13.496662, 6.105574), point2=(13.083092, 6.950714))
s0.Line(point1=(13.083092, 6.950714), point2=(13.344608, 13.284686))
s0.Line(point1=(13.344608, 13.284686), point2=(13.043361, 13.455883))
s0.Line(point1=(13.043361, 13.455883), point2=(12.813527, 14.172807))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
print 40
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(13.650000, 47.250000), point2=(14.250000, 47.100000))
s0.Line(point1=(14.250000, 47.100000), point2=(14.550000, 44.250000))
s0.Line(point1=(14.550000, 44.250000), point2=(15.000000, 43.500000))
s0.Line(point1=(15.000000, 43.500000), point2=(15.000000, 42.450000))
s0.Line(point1=(15.000000, 42.450000), point2=(14.250000, 41.550000))
s0.Line(point1=(14.250000, 41.550000), point2=(13.800000, 41.550000))
s0.Line(point1=(13.800000, 41.550000), point2=(13.800000, 42.300000))
s0.Line(point1=(13.800000, 42.300000), point2=(12.900000, 43.650000))
s0.Line(point1=(12.900000, 43.650000), point2=(12.900000, 44.100000))
s0.Line(point1=(12.900000, 44.100000), point2=(13.200000, 44.100000))
s0.Line(point1=(13.200000, 44.100000), point2=(12.900000, 44.400000))
s0.Line(point1=(12.900000, 44.400000), point2=(13.200000, 46.800000))
s0.Line(point1=(13.200000, 46.800000), point2=(13.650000, 46.950000))
s0.Line(point1=(13.650000, 46.950000), point2=(13.650000, 47.250000))
s0.Line(point1=(13.574254, 47.347014), point2=(14.373704, 47.207483))
s0.Line(point1=(14.373704, 47.207483), point2=(14.735200, 44.311918))
s0.Line(point1=(14.735200, 44.311918), point2=(15.185749, 43.551450))
s0.Line(point1=(15.185749, 43.551450), point2=(15.176822, 42.385982))
s0.Line(point1=(15.176822, 42.385982), point2=(14.326822, 41.385982))
s0.Line(point1=(14.326822, 41.385982), point2=(13.700000, 41.450000))
s0.Line(point1=(13.700000, 41.450000), point2=(13.616795, 42.244530))
s0.Line(point1=(13.616795, 42.244530), point2=(12.716795, 43.594530))
s0.Line(point1=(12.716795, 43.594530), point2=(12.800000, 44.200000))
s0.Line(point1=(12.800000, 44.200000), point2=(13.129289, 44.129289))
s0.Line(point1=(13.129289, 44.129289), point2=(12.730062, 44.341693))
s0.Line(point1=(12.730062, 44.341693), point2=(13.069149, 46.907272))
s0.Line(point1=(13.069149, 46.907272), point2=(13.518377, 47.044868))
s0.Line(point1=(13.518377, 47.044868), point2=(13.574254, 47.347014))
s0.Line(point1=(13.725746, 47.152986), point2=(14.126296, 46.992517))
s0.Line(point1=(14.126296, 46.992517), point2=(14.364800, 44.188082))
s0.Line(point1=(14.364800, 44.188082), point2=(14.814251, 43.448550))
s0.Line(point1=(14.814251, 43.448550), point2=(14.823178, 42.514018))
s0.Line(point1=(14.823178, 42.514018), point2=(14.173178, 41.714018))
s0.Line(point1=(14.173178, 41.714018), point2=(13.900000, 41.650000))
s0.Line(point1=(13.900000, 41.650000), point2=(13.983205, 42.355470))
s0.Line(point1=(13.983205, 42.355470), point2=(13.083205, 43.705470))
s0.Line(point1=(13.083205, 43.705470), point2=(13.000000, 44.000000))
s0.Line(point1=(13.000000, 44.000000), point2=(13.270711, 44.070711))
s0.Line(point1=(13.270711, 44.070711), point2=(13.069938, 44.458307))
s0.Line(point1=(13.069938, 44.458307), point2=(13.330851, 46.692728))
s0.Line(point1=(13.330851, 46.692728), point2=(13.781623, 46.855132))
s0.Line(point1=(13.781623, 46.855132), point2=(13.725746, 47.152986))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(16.950000, 50.850000), point2=(16.950000, 50.400000))
s0.Line(point1=(16.950000, 50.400000), point2=(16.050000, 49.650000))
s0.Line(point1=(16.050000, 49.650000), point2=(14.400000, 50.250000))
s0.Line(point1=(14.400000, 50.250000), point2=(14.850000, 51.900000))
s0.Line(point1=(14.850000, 51.900000), point2=(16.050000, 51.900000))
s0.Line(point1=(16.050000, 51.900000), point2=(16.950000, 50.850000))
s0.Line(point1=(17.125926, 50.915079), point2=(17.114018, 50.323178))
s0.Line(point1=(17.114018, 50.323178), point2=(16.079844, 49.479199))
s0.Line(point1=(16.079844, 49.479199), point2=(14.269349, 50.182332))
s0.Line(point1=(14.269349, 50.182332), point2=(14.753524, 52.026312))
s0.Line(point1=(14.753524, 52.026312), point2=(16.125926, 52.065079))
s0.Line(point1=(16.125926, 52.065079), point2=(17.125926, 50.915079))
s0.Line(point1=(16.774074, 50.784921), point2=(16.785982, 50.476822))
s0.Line(point1=(16.785982, 50.476822), point2=(16.020156, 49.820801))
s0.Line(point1=(16.020156, 49.820801), point2=(14.530651, 50.317668))
s0.Line(point1=(14.530651, 50.317668), point2=(14.946476, 51.773688))
s0.Line(point1=(14.946476, 51.773688), point2=(15.974074, 51.734921))
s0.Line(point1=(15.974074, 51.734921), point2=(16.774074, 50.784921))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(16.800000, 27.450000), point2=(16.800000, 26.250000))
s0.Line(point1=(16.800000, 26.250000), point2=(15.750000, 25.200000))
s0.Line(point1=(15.750000, 25.200000), point2=(14.550000, 25.500000))
s0.Line(point1=(14.550000, 25.500000), point2=(14.700000, 27.300000))
s0.Line(point1=(14.700000, 27.300000), point2=(15.000000, 27.600000))
s0.Line(point1=(15.000000, 27.600000), point2=(16.350000, 27.750000))
s0.Line(point1=(16.350000, 27.750000), point2=(16.800000, 27.450000))
s0.Line(point1=(16.955470, 27.533205), point2=(16.970711, 26.179289))
s0.Line(point1=(16.970711, 26.179289), point2=(15.796457, 25.032275))
s0.Line(point1=(15.796457, 25.032275), point2=(14.426092, 25.411290))
s0.Line(point1=(14.426092, 25.411290), point2=(14.529635, 27.379015))
s0.Line(point1=(14.529635, 27.379015), point2=(14.918246, 27.770099))
s0.Line(point1=(14.918246, 27.770099), point2=(16.394427, 27.932593))
s0.Line(point1=(16.394427, 27.932593), point2=(16.955470, 27.533205))
s0.Line(point1=(16.644530, 27.366795), point2=(16.629289, 26.320711))
s0.Line(point1=(16.629289, 26.320711), point2=(15.703543, 25.367725))
s0.Line(point1=(15.703543, 25.367725), point2=(14.673908, 25.588710))
s0.Line(point1=(14.673908, 25.588710), point2=(14.870365, 27.220985))
s0.Line(point1=(14.870365, 27.220985), point2=(15.081754, 27.429901))
s0.Line(point1=(15.081754, 27.429901), point2=(16.305573, 27.567407))
s0.Line(point1=(16.305573, 27.567407), point2=(16.644530, 27.366795))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(14.850000, 16.800000), point2=(15.600000, 17.550000))
s0.Line(point1=(15.600000, 17.550000), point2=(16.200000, 17.250000))
s0.Line(point1=(16.200000, 17.250000), point2=(16.500000, 16.500000))
s0.Line(point1=(16.500000, 16.500000), point2=(16.050000, 16.200000))
s0.Line(point1=(16.050000, 16.200000), point2=(14.850000, 16.500000))
s0.Line(point1=(14.850000, 16.500000), point2=(14.850000, 16.800000))
s0.Line(point1=(14.679289, 16.870711), point2=(15.574011, 17.710153))
s0.Line(point1=(15.574011, 17.710153), point2=(16.337569, 17.376582))
s0.Line(point1=(16.337569, 17.376582), point2=(16.648318, 16.453934))
s0.Line(point1=(16.648318, 16.453934), point2=(16.081216, 16.019781))
s0.Line(point1=(16.081216, 16.019781), point2=(14.725746, 16.402986))
s0.Line(point1=(14.725746, 16.402986), point2=(14.679289, 16.870711))
s0.Line(point1=(15.020711, 16.729289), point2=(15.625989, 17.389847))
s0.Line(point1=(15.625989, 17.389847), point2=(16.062431, 17.123418))
s0.Line(point1=(16.062431, 17.123418), point2=(16.351682, 16.546066))
s0.Line(point1=(16.351682, 16.546066), point2=(16.018784, 16.380219))
s0.Line(point1=(16.018784, 16.380219), point2=(14.974254, 16.597014))
s0.Line(point1=(14.974254, 16.597014), point2=(15.020711, 16.729289))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(15.150000, 39.450000), point2=(16.350000, 39.600000))
s0.Line(point1=(16.350000, 39.600000), point2=(17.700000, 38.550000))
s0.Line(point1=(17.700000, 38.550000), point2=(18.300000, 37.200000))
s0.Line(point1=(18.300000, 37.200000), point2=(18.300000, 35.700000))
s0.Line(point1=(18.300000, 35.700000), point2=(17.700000, 34.950000))
s0.Line(point1=(17.700000, 34.950000), point2=(16.950000, 34.950000))
s0.Line(point1=(16.950000, 34.950000), point2=(16.050000, 36.450000))
s0.Line(point1=(16.050000, 36.450000), point2=(15.750000, 36.450000))
s0.Line(point1=(15.750000, 36.450000), point2=(15.000000, 38.250000))
s0.Line(point1=(15.000000, 38.250000), point2=(15.150000, 39.450000))
s0.Line(point1=(15.038369, 39.561631), point2=(16.398991, 39.778163))
s0.Line(point1=(16.398991, 39.778163), point2=(17.852775, 38.669549))
s0.Line(point1=(17.852775, 38.669549), point2=(18.491381, 37.240614))
s0.Line(point1=(18.491381, 37.240614), point2=(18.478087, 35.637530))
s0.Line(point1=(18.478087, 35.637530), point2=(17.778087, 34.787530))
s0.Line(point1=(17.778087, 34.787530), point2=(16.864251, 34.798550))
s0.Line(point1=(16.864251, 34.798550), point2=(15.964251, 36.298550))
s0.Line(point1=(15.964251, 36.298550), point2=(15.657692, 36.311538))
s0.Line(point1=(15.657692, 36.311538), point2=(14.808465, 38.223942))
s0.Line(point1=(14.808465, 38.223942), point2=(15.038369, 39.561631))
s0.Line(point1=(15.261631, 39.338369), point2=(16.301009, 39.421837))
s0.Line(point1=(16.301009, 39.421837), point2=(17.547225, 38.430451))
s0.Line(point1=(17.547225, 38.430451), point2=(18.108619, 37.159386))
s0.Line(point1=(18.108619, 37.159386), point2=(18.121913, 35.762470))
s0.Line(point1=(18.121913, 35.762470), point2=(17.621913, 35.112470))
s0.Line(point1=(17.621913, 35.112470), point2=(17.035749, 35.101450))
s0.Line(point1=(17.035749, 35.101450), point2=(16.135749, 36.601450))
s0.Line(point1=(16.135749, 36.601450), point2=(15.842308, 36.588462))
s0.Line(point1=(15.842308, 36.588462), point2=(15.191535, 38.276058))
s0.Line(point1=(15.191535, 38.276058), point2=(15.261631, 39.338369))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(16.350000, 14.850000), point2=(16.500000, 14.250000))
s0.Line(point1=(16.500000, 14.250000), point2=(16.200000, 13.800000))
s0.Line(point1=(16.200000, 13.800000), point2=(15.600000, 13.650000))
s0.Line(point1=(15.600000, 13.650000), point2=(15.150000, 13.950000))
s0.Line(point1=(15.150000, 13.950000), point2=(15.450000, 14.550000))
s0.Line(point1=(15.450000, 14.550000), point2=(16.350000, 14.850000))
s0.Line(point1=(16.415391, 14.969122), point2=(16.680219, 14.218784))
s0.Line(point1=(16.680219, 14.218784), point2=(16.307459, 13.647516))
s0.Line(point1=(16.307459, 13.647516), point2=(15.568784, 13.469781))
s0.Line(point1=(15.568784, 13.469781), point2=(15.005087, 13.911516))
s0.Line(point1=(15.005087, 13.911516), point2=(15.328935, 14.689590))
s0.Line(point1=(15.328935, 14.689590), point2=(16.415391, 14.969122))
s0.Line(point1=(16.284609, 14.730878), point2=(16.319781, 14.281216))
s0.Line(point1=(16.319781, 14.281216), point2=(16.092541, 13.952484))
s0.Line(point1=(16.092541, 13.952484), point2=(15.631216, 13.830219))
s0.Line(point1=(15.631216, 13.830219), point2=(15.294913, 13.988484))
s0.Line(point1=(15.294913, 13.988484), point2=(15.571065, 14.410410))
s0.Line(point1=(15.571065, 14.410410), point2=(16.284609, 14.730878))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(17.850000, 50.250000), point2=(18.300000, 49.050000))
s0.Line(point1=(18.300000, 49.050000), point2=(19.500000, 48.000000))
s0.Line(point1=(19.500000, 48.000000), point2=(19.650000, 47.100000))
s0.Line(point1=(19.650000, 47.100000), point2=(18.300000, 46.200000))
s0.Line(point1=(18.300000, 46.200000), point2=(16.950000, 45.900000))
s0.Line(point1=(16.950000, 45.900000), point2=(16.350000, 44.700000))
s0.Line(point1=(16.350000, 44.700000), point2=(15.300000, 44.850000))
s0.Line(point1=(15.300000, 44.850000), point2=(15.300000, 46.200000))
s0.Line(point1=(15.300000, 46.200000), point2=(15.900000, 46.650000))
s0.Line(point1=(15.900000, 46.650000), point2=(16.050000, 49.200000))
s0.Line(point1=(16.050000, 49.200000), point2=(17.100000, 50.250000))
s0.Line(point1=(17.100000, 50.250000), point2=(17.850000, 50.250000))
s0.Line(point1=(17.943633, 50.385112), point2=(18.459483, 49.160370))
s0.Line(point1=(18.459483, 49.160370), point2=(19.664490, 48.091698))
s0.Line(point1=(19.664490, 48.091698), point2=(19.804109, 47.033235))
s0.Line(point1=(19.804109, 47.033235), point2=(18.377163, 46.019176))
s0.Line(point1=(18.377163, 46.019176), point2=(17.061136, 45.757660))
s0.Line(point1=(17.061136, 45.757660), point2=(16.425301, 44.556284))
s0.Line(point1=(16.425301, 44.556284), point2=(15.185858, 44.751005))
s0.Line(point1=(15.185858, 44.751005), point2=(15.140000, 46.280000))
s0.Line(point1=(15.140000, 46.280000), point2=(15.740173, 46.735872))
s0.Line(point1=(15.740173, 46.735872), point2=(15.879462, 49.276583))
s0.Line(point1=(15.879462, 49.276583), point2=(17.029289, 50.420711))
s0.Line(point1=(17.029289, 50.420711), point2=(17.943633, 50.385112))
s0.Line(point1=(17.756367, 50.114888), point2=(18.140517, 48.939630))
s0.Line(point1=(18.140517, 48.939630), point2=(19.335510, 47.908302))
s0.Line(point1=(19.335510, 47.908302), point2=(19.495891, 47.166765))
s0.Line(point1=(19.495891, 47.166765), point2=(18.222837, 46.380824))
s0.Line(point1=(18.222837, 46.380824), point2=(16.838864, 46.042340))
s0.Line(point1=(16.838864, 46.042340), point2=(16.274699, 44.843716))
s0.Line(point1=(16.274699, 44.843716), point2=(15.414142, 44.948995))
s0.Line(point1=(15.414142, 44.948995), point2=(15.460000, 46.120000))
s0.Line(point1=(15.460000, 46.120000), point2=(16.059827, 46.564128))
s0.Line(point1=(16.059827, 46.564128), point2=(16.220538, 49.123417))
s0.Line(point1=(16.220538, 49.123417), point2=(17.170711, 50.079289))
s0.Line(point1=(17.170711, 50.079289), point2=(17.756367, 50.114888))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(16.650000, 6.750000), point2=(17.550000, 6.750000))
s0.Line(point1=(17.550000, 6.750000), point2=(17.850000, 6.300000))
s0.Line(point1=(17.850000, 6.300000), point2=(18.300000, 4.950000))
s0.Line(point1=(18.300000, 4.950000), point2=(18.450000, 2.550000))
s0.Line(point1=(18.450000, 2.550000), point2=(16.650000, 3.000000))
s0.Line(point1=(16.650000, 3.000000), point2=(16.650000, 4.200000))
s0.Line(point1=(16.650000, 4.200000), point2=(16.350000, 4.800000))
s0.Line(point1=(16.350000, 4.800000), point2=(15.900000, 4.800000))
s0.Line(point1=(15.900000, 4.800000), point2=(15.900000, 5.700000))
s0.Line(point1=(15.900000, 5.700000), point2=(16.650000, 6.750000))
s0.Line(point1=(16.568627, 6.908124), point2=(17.633205, 6.905470))
s0.Line(point1=(17.633205, 6.905470), point2=(18.028073, 6.387093))
s0.Line(point1=(18.028073, 6.387093), point2=(18.494674, 4.987861))
s0.Line(point1=(18.494674, 4.987861), point2=(18.525552, 2.459224))
s0.Line(point1=(18.525552, 2.459224), point2=(16.525746, 2.902986))
s0.Line(point1=(16.525746, 2.902986), point2=(16.460557, 4.155279))
s0.Line(point1=(16.460557, 4.155279), point2=(16.260557, 4.655279))
s0.Line(point1=(16.260557, 4.655279), point2=(15.800000, 4.700000))
s0.Line(point1=(15.800000, 4.700000), point2=(15.718627, 5.758124))
s0.Line(point1=(15.718627, 5.758124), point2=(16.568627, 6.908124))
s0.Line(point1=(16.731373, 6.591876), point2=(17.466795, 6.594530))
s0.Line(point1=(17.466795, 6.594530), point2=(17.671927, 6.212907))
s0.Line(point1=(17.671927, 6.212907), point2=(18.105326, 4.912139))
s0.Line(point1=(18.105326, 4.912139), point2=(18.374448, 2.640776))
s0.Line(point1=(18.374448, 2.640776), point2=(16.774254, 3.097014))
s0.Line(point1=(16.774254, 3.097014), point2=(16.839443, 4.244721))
s0.Line(point1=(16.839443, 4.244721), point2=(16.439443, 4.944721))
s0.Line(point1=(16.439443, 4.944721), point2=(16.000000, 4.900000))
s0.Line(point1=(16.000000, 4.900000), point2=(16.081373, 5.641876))
s0.Line(point1=(16.081373, 5.641876), point2=(16.731373, 6.591876))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(18.300000, 43.500000), point2=(18.450000, 42.450000))
s0.Line(point1=(18.450000, 42.450000), point2=(16.200000, 40.650000))
s0.Line(point1=(16.200000, 40.650000), point2=(16.050000, 43.500000))
s0.Line(point1=(16.050000, 43.500000), point2=(17.100000, 43.950000))
s0.Line(point1=(17.100000, 43.950000), point2=(18.300000, 43.500000))
s0.Line(point1=(18.434107, 43.607775), point2=(18.611464, 42.386055))
s0.Line(point1=(18.611464, 42.386055), point2=(16.162608, 40.566657))
s0.Line(point1=(16.162608, 40.566657), point2=(15.910746, 43.586659))
s0.Line(point1=(15.910746, 43.586659), point2=(17.095720, 44.135547))
s0.Line(point1=(17.095720, 44.135547), point2=(18.434107, 43.607775))
s0.Line(point1=(18.165893, 43.392225), point2=(18.288536, 42.513945))
s0.Line(point1=(18.288536, 42.513945), point2=(16.237392, 40.733343))
s0.Line(point1=(16.237392, 40.733343), point2=(16.189254, 43.413341))
s0.Line(point1=(16.189254, 43.413341), point2=(17.104280, 43.764453))
s0.Line(point1=(17.104280, 43.764453), point2=(18.165893, 43.392225))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(16.800000, 24.450000), point2=(18.750000, 26.250000))
s0.Line(point1=(18.750000, 26.250000), point2=(20.850000, 24.600000))
s0.Line(point1=(20.850000, 24.600000), point2=(21.150000, 23.700000))
s0.Line(point1=(21.150000, 23.700000), point2=(20.250000, 22.650000))
s0.Line(point1=(20.250000, 22.650000), point2=(19.200000, 22.800000))
s0.Line(point1=(19.200000, 22.800000), point2=(16.950000, 24.000000))
s0.Line(point1=(16.950000, 24.000000), point2=(16.800000, 24.450000))
s0.Line(point1=(16.637304, 24.491858), point2=(18.743954, 26.402112))
s0.Line(point1=(18.743954, 26.402112), point2=(21.006650, 24.710255))
s0.Line(point1=(21.006650, 24.710255), point2=(21.320794, 23.666544))
s0.Line(point1=(21.320794, 23.666544), point2=(20.311784, 22.485926))
s0.Line(point1=(20.311784, 22.485926), point2=(19.138799, 22.612770))
s0.Line(point1=(19.138799, 22.612770), point2=(16.808073, 23.880142))
s0.Line(point1=(16.808073, 23.880142), point2=(16.637304, 24.491858))
s0.Line(point1=(16.962696, 24.408142), point2=(18.756046, 26.097888))
s0.Line(point1=(18.756046, 26.097888), point2=(20.693350, 24.489745))
s0.Line(point1=(20.693350, 24.489745), point2=(20.979206, 23.733456))
s0.Line(point1=(20.979206, 23.733456), point2=(20.188216, 22.814074))
s0.Line(point1=(20.188216, 22.814074), point2=(19.261201, 22.987230))
s0.Line(point1=(19.261201, 22.987230), point2=(17.091927, 24.119858))
s0.Line(point1=(17.091927, 24.119858), point2=(16.962696, 24.408142))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(23.850000, 20.100000), point2=(26.100000, 18.150000))
s0.Line(point1=(26.100000, 18.150000), point2=(25.500000, 16.500000))
s0.Line(point1=(25.500000, 16.500000), point2=(25.500000, 15.300000))
s0.Line(point1=(25.500000, 15.300000), point2=(23.400000, 10.200000))
s0.Line(point1=(23.400000, 10.200000), point2=(22.200000, 9.000000))
s0.Line(point1=(22.200000, 9.000000), point2=(21.900000, 7.950000))
s0.Line(point1=(21.900000, 7.950000), point2=(19.950000, 7.350000))
s0.Line(point1=(19.950000, 7.350000), point2=(18.750000, 7.950000))
s0.Line(point1=(18.750000, 7.950000), point2=(18.300000, 9.000000))
s0.Line(point1=(18.300000, 9.000000), point2=(17.400000, 13.200000))
s0.Line(point1=(17.400000, 13.200000), point2=(17.400000, 15.000000))
s0.Line(point1=(17.400000, 15.000000), point2=(19.500000, 17.250000))
s0.Line(point1=(19.500000, 17.250000), point2=(19.950000, 18.150000))
s0.Line(point1=(19.950000, 18.150000), point2=(22.200000, 19.350000))
s0.Line(point1=(22.200000, 19.350000), point2=(22.650000, 19.950000))
s0.Line(point1=(22.650000, 19.950000), point2=(23.850000, 20.100000))
s0.Line(point1=(23.903090, 20.274797), point2=(26.259472, 18.191395))
s0.Line(point1=(26.259472, 18.191395), point2=(25.693979, 16.465826))
s0.Line(point1=(25.693979, 16.465826), point2=(25.692468, 15.261925))
s0.Line(point1=(25.692468, 15.261925), point2=(23.563178, 10.091214))
s0.Line(point1=(23.563178, 10.091214), point2=(22.366863, 8.901817))
s0.Line(point1=(22.366863, 8.901817), point2=(22.025561, 7.826950))
s0.Line(point1=(22.025561, 7.826950), point2=(19.934687, 7.164979))
s0.Line(point1=(19.934687, 7.164979), point2=(18.613364, 7.821165))
s0.Line(point1=(18.613364, 7.821165), point2=(18.110305, 8.939655))
s0.Line(point1=(18.110305, 8.939655), point2=(17.202220, 13.179047))
s0.Line(point1=(17.202220, 13.179047), point2=(17.226894, 15.068232))
s0.Line(point1=(17.226894, 15.068232), point2=(19.337452, 17.362953))
s0.Line(point1=(19.337452, 17.362953), point2=(19.813498, 18.282957))
s0.Line(point1=(19.813498, 18.282957), point2=(22.072941, 19.498235))
s0.Line(point1=(22.072941, 19.498235), point2=(22.557597, 20.109228))
s0.Line(point1=(22.557597, 20.109228), point2=(23.903090, 20.274797))
s0.Line(point1=(23.796910, 19.925203), point2=(25.940528, 18.108605))
s0.Line(point1=(25.940528, 18.108605), point2=(25.306021, 16.534174))
s0.Line(point1=(25.306021, 16.534174), point2=(25.307532, 15.338075))
s0.Line(point1=(25.307532, 15.338075), point2=(23.236822, 10.308786))
s0.Line(point1=(23.236822, 10.308786), point2=(22.033137, 9.098183))
s0.Line(point1=(22.033137, 9.098183), point2=(21.774439, 8.073050))
s0.Line(point1=(21.774439, 8.073050), point2=(19.965313, 7.535021))
s0.Line(point1=(19.965313, 7.535021), point2=(18.886636, 8.078835))
s0.Line(point1=(18.886636, 8.078835), point2=(18.489695, 9.060345))
s0.Line(point1=(18.489695, 9.060345), point2=(17.597780, 13.220953))
s0.Line(point1=(17.597780, 13.220953), point2=(17.573106, 14.931768))
s0.Line(point1=(17.573106, 14.931768), point2=(19.662548, 17.137047))
s0.Line(point1=(19.662548, 17.137047), point2=(20.086502, 18.017043))
s0.Line(point1=(20.086502, 18.017043), point2=(22.327059, 19.201765))
s0.Line(point1=(22.327059, 19.201765), point2=(22.742403, 19.790772))
s0.Line(point1=(22.742403, 19.790772), point2=(23.796910, 19.925203))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(23.100000, 42.750000), point2=(23.250000, 41.400000))
s0.Line(point1=(23.250000, 41.400000), point2=(17.400000, 40.350000))
s0.Line(point1=(17.400000, 40.350000), point2=(17.400000, 40.950000))
s0.Line(point1=(17.400000, 40.950000), point2=(18.750000, 41.400000))
s0.Line(point1=(18.750000, 41.400000), point2=(18.750000, 41.850000))
s0.Line(point1=(18.750000, 41.850000), point2=(20.100000, 42.000000))
s0.Line(point1=(20.100000, 42.000000), point2=(22.200000, 43.050000))
s0.Line(point1=(22.200000, 43.050000), point2=(23.100000, 42.750000))
s0.Line(point1=(23.231011, 42.855911), point2=(23.367055, 41.312616))
s0.Line(point1=(23.367055, 41.312616), point2=(17.317666, 40.251573))
s0.Line(point1=(17.317666, 40.251573), point2=(17.268377, 41.044868))
s0.Line(point1=(17.268377, 41.044868), point2=(18.618377, 41.494868))
s0.Line(point1=(18.618377, 41.494868), point2=(18.638957, 41.949388))
s0.Line(point1=(18.638957, 41.949388), point2=(20.044235, 42.188831))
s0.Line(point1=(20.044235, 42.188831), point2=(22.186901, 43.234311))
s0.Line(point1=(22.186901, 43.234311), point2=(23.231011, 42.855911))
s0.Line(point1=(22.968989, 42.644089), point2=(23.132945, 41.487384))
s0.Line(point1=(23.132945, 41.487384), point2=(17.482334, 40.448427))
s0.Line(point1=(17.482334, 40.448427), point2=(17.531623, 40.855132))
s0.Line(point1=(17.531623, 40.855132), point2=(18.881623, 41.305132))
s0.Line(point1=(18.881623, 41.305132), point2=(18.861043, 41.750612))
s0.Line(point1=(18.861043, 41.750612), point2=(20.155765, 41.811169))
s0.Line(point1=(20.155765, 41.811169), point2=(22.213099, 42.865689))
s0.Line(point1=(22.213099, 42.865689), point2=(22.968989, 42.644089))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(18.900000, 19.950000), point2=(19.650000, 18.900000))
s0.Line(point1=(19.650000, 18.900000), point2=(19.650000, 18.300000))
s0.Line(point1=(19.650000, 18.300000), point2=(18.900000, 18.300000))
s0.Line(point1=(18.900000, 18.300000), point2=(18.750000, 17.400000))
s0.Line(point1=(18.750000, 17.400000), point2=(17.550000, 17.400000))
s0.Line(point1=(17.550000, 17.400000), point2=(17.550000, 18.300000))
s0.Line(point1=(17.550000, 18.300000), point2=(18.000000, 18.600000))
s0.Line(point1=(18.000000, 18.600000), point2=(18.000000, 19.800000))
s0.Line(point1=(18.000000, 19.800000), point2=(18.900000, 19.950000))
s0.Line(point1=(18.964933, 20.106763), point2=(19.831373, 18.958124))
s0.Line(point1=(19.831373, 18.958124), point2=(19.750000, 18.200000))
s0.Line(point1=(19.750000, 18.200000), point2=(18.998639, 18.183560))
s0.Line(point1=(18.998639, 18.183560), point2=(18.848639, 17.283560))
s0.Line(point1=(18.848639, 17.283560), point2=(17.450000, 17.300000))
s0.Line(point1=(17.450000, 17.300000), point2=(17.394530, 18.383205))
s0.Line(point1=(17.394530, 18.383205), point2=(17.844530, 18.683205))
s0.Line(point1=(17.844530, 18.683205), point2=(17.883560, 19.898639))
s0.Line(point1=(17.883560, 19.898639), point2=(18.964933, 20.106763))
s0.Line(point1=(18.835067, 19.793237), point2=(19.468627, 18.841876))
s0.Line(point1=(19.468627, 18.841876), point2=(19.550000, 18.400000))
s0.Line(point1=(19.550000, 18.400000), point2=(18.801361, 18.416440))
s0.Line(point1=(18.801361, 18.416440), point2=(18.651361, 17.516440))
s0.Line(point1=(18.651361, 17.516440), point2=(17.650000, 17.500000))
s0.Line(point1=(17.650000, 17.500000), point2=(17.705470, 18.216795))
s0.Line(point1=(17.705470, 18.216795), point2=(18.155470, 18.516795))
s0.Line(point1=(18.155470, 18.516795), point2=(18.116440, 19.701361))
s0.Line(point1=(18.116440, 19.701361), point2=(18.835067, 19.793237))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(17.850000, 52.500000), point2=(20.400000, 52.500000))
s0.Line(point1=(20.400000, 52.500000), point2=(21.000000, 51.150000))
s0.Line(point1=(21.000000, 51.150000), point2=(22.200000, 50.550000))
s0.Line(point1=(22.200000, 50.550000), point2=(23.250000, 49.350000))
s0.Line(point1=(23.250000, 49.350000), point2=(23.100000, 48.300000))
s0.Line(point1=(23.100000, 48.300000), point2=(22.050000, 48.450000))
s0.Line(point1=(22.050000, 48.450000), point2=(21.300000, 47.550000))
s0.Line(point1=(21.300000, 47.550000), point2=(20.850000, 47.550000))
s0.Line(point1=(20.850000, 47.550000), point2=(20.850000, 49.050000))
s0.Line(point1=(20.850000, 49.050000), point2=(17.850000, 52.500000))
s0.Line(point1=(17.774539, 52.500000), point2=(20.491381, 52.500000))
s0.Line(point1=(20.491381, 52.500000), point2=(21.136103, 51.280057))
s0.Line(point1=(21.136103, 51.280057), point2=(22.319979, 50.705293))
s0.Line(point1=(22.319979, 50.705293), point2=(23.424253, 49.401708))
s0.Line(point1=(23.424253, 49.401708), point2=(23.184853, 48.186863))
s0.Line(point1=(23.184853, 48.186863), point2=(22.112680, 48.286987))
s0.Line(point1=(22.112680, 48.286987), point2=(21.376822, 47.385982))
s0.Line(point1=(21.376822, 47.385982), point2=(20.750000, 47.450000))
s0.Line(point1=(20.750000, 47.450000), point2=(20.674539, 48.984382))
s0.Line(point1=(20.674539, 48.984382), point2=(17.774539, 52.500000))
s0.Line(point1=(17.925461, 52.500000), point2=(20.308619, 52.500000))
s0.Line(point1=(20.308619, 52.500000), point2=(20.863897, 51.019943))
s0.Line(point1=(20.863897, 51.019943), point2=(22.080021, 50.394707))
s0.Line(point1=(22.080021, 50.394707), point2=(23.075747, 49.298292))
s0.Line(point1=(23.075747, 49.298292), point2=(23.015147, 48.413137))
s0.Line(point1=(23.015147, 48.413137), point2=(21.987320, 48.613013))
s0.Line(point1=(21.987320, 48.613013), point2=(21.223178, 47.714018))
s0.Line(point1=(21.223178, 47.714018), point2=(20.950000, 47.650000))
s0.Line(point1=(20.950000, 47.650000), point2=(21.025461, 49.115618))
s0.Line(point1=(21.025461, 49.115618), point2=(17.925461, 52.500000))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(19.500000, 28.500000), point2=(19.350000, 26.700000))
s0.Line(point1=(19.350000, 26.700000), point2=(18.150000, 26.700000))
s0.Line(point1=(18.150000, 26.700000), point2=(17.850000, 27.300000))
s0.Line(point1=(17.850000, 27.300000), point2=(18.600000, 28.200000))
s0.Line(point1=(18.600000, 28.200000), point2=(19.500000, 28.500000))
s0.Line(point1=(19.568032, 28.586564), point2=(19.449655, 26.591695))
s0.Line(point1=(19.449655, 26.591695), point2=(18.060557, 26.555279))
s0.Line(point1=(18.060557, 26.555279), point2=(17.683735, 27.319297))
s0.Line(point1=(17.683735, 27.319297), point2=(18.491555, 28.358887))
s0.Line(point1=(18.491555, 28.358887), point2=(19.568032, 28.586564))
s0.Line(point1=(19.431968, 28.413436), point2=(19.250345, 26.808305))
s0.Line(point1=(19.250345, 26.808305), point2=(18.239443, 26.844721))
s0.Line(point1=(18.239443, 26.844721), point2=(18.016265, 27.280703))
s0.Line(point1=(18.016265, 27.280703), point2=(18.708445, 28.041113))
s0.Line(point1=(18.708445, 28.041113), point2=(19.431968, 28.413436))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(21.750000, 22.500000), point2=(21.750000, 22.050000))
s0.Line(point1=(21.750000, 22.050000), point2=(20.850000, 21.450000))
s0.Line(point1=(20.850000, 21.450000), point2=(19.350000, 21.150000))
s0.Line(point1=(19.350000, 21.150000), point2=(18.000000, 21.300000))
s0.Line(point1=(18.000000, 21.300000), point2=(18.000000, 22.050000))
s0.Line(point1=(18.000000, 22.050000), point2=(20.550000, 22.050000))
s0.Line(point1=(20.550000, 22.050000), point2=(21.150000, 22.500000))
s0.Line(point1=(21.150000, 22.500000), point2=(21.750000, 22.500000))
s0.Line(point1=(21.850000, 22.600000), point2=(21.905470, 21.966795))
s0.Line(point1=(21.905470, 21.966795), point2=(20.925082, 21.268737))
s0.Line(point1=(20.925082, 21.268737), point2=(19.358568, 20.952554))
s0.Line(point1=(19.358568, 20.952554), point2=(17.888957, 21.200612))
s0.Line(point1=(17.888957, 21.200612), point2=(17.900000, 22.150000))
s0.Line(point1=(17.900000, 22.150000), point2=(20.490000, 22.230000))
s0.Line(point1=(20.490000, 22.230000), point2=(21.090000, 22.680000))
s0.Line(point1=(21.090000, 22.680000), point2=(21.850000, 22.600000))
s0.Line(point1=(21.650000, 22.400000), point2=(21.594530, 22.133205))
s0.Line(point1=(21.594530, 22.133205), point2=(20.774918, 21.631263))
s0.Line(point1=(20.774918, 21.631263), point2=(19.341432, 21.347446))
s0.Line(point1=(19.341432, 21.347446), point2=(18.111043, 21.399388))
s0.Line(point1=(18.111043, 21.399388), point2=(18.100000, 21.950000))
s0.Line(point1=(18.100000, 21.950000), point2=(20.610000, 21.870000))
s0.Line(point1=(20.610000, 21.870000), point2=(21.210000, 22.320000))
s0.Line(point1=(21.210000, 22.320000), point2=(21.650000, 22.400000))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(19.050000, 38.850000), point2=(19.950000, 38.850000))
s0.Line(point1=(19.950000, 38.850000), point2=(20.250000, 38.550000))
s0.Line(point1=(20.250000, 38.550000), point2=(20.550000, 37.050000))
s0.Line(point1=(20.550000, 37.050000), point2=(19.950000, 36.300000))
s0.Line(point1=(19.950000, 36.300000), point2=(19.350000, 36.300000))
s0.Line(point1=(19.350000, 36.300000), point2=(18.750000, 37.200000))
s0.Line(point1=(18.750000, 37.200000), point2=(18.750000, 38.400000))
s0.Line(point1=(18.750000, 38.400000), point2=(19.050000, 38.850000))
s0.Line(point1=(18.966795, 39.005470), point2=(20.020711, 39.020711))
s0.Line(point1=(20.020711, 39.020711), point2=(20.418769, 38.640322))
s0.Line(point1=(20.418769, 38.640322), point2=(20.726145, 37.007142))
s0.Line(point1=(20.726145, 37.007142), point2=(20.028087, 36.137530))
s0.Line(point1=(20.028087, 36.137530), point2=(19.266795, 36.144530))
s0.Line(point1=(19.266795, 36.144530), point2=(18.566795, 37.144530))
s0.Line(point1=(18.566795, 37.144530), point2=(18.566795, 38.455470))
s0.Line(point1=(18.566795, 38.455470), point2=(18.966795, 39.005470))
s0.Line(point1=(19.133205, 38.694530), point2=(19.879289, 38.679289))
s0.Line(point1=(19.879289, 38.679289), point2=(20.081231, 38.459678))
s0.Line(point1=(20.081231, 38.459678), point2=(20.373855, 37.092858))
s0.Line(point1=(20.373855, 37.092858), point2=(19.871913, 36.462470))
s0.Line(point1=(19.871913, 36.462470), point2=(19.433205, 36.455470))
s0.Line(point1=(19.433205, 36.455470), point2=(18.933205, 37.255470))
s0.Line(point1=(18.933205, 37.255470), point2=(18.933205, 38.344530))
s0.Line(point1=(18.933205, 38.344530), point2=(19.133205, 38.694530))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(19.050000, 5.550000), point2=(19.650000, 5.550000))
s0.Line(point1=(19.650000, 5.550000), point2=(20.100000, 4.500000))
s0.Line(point1=(20.100000, 4.500000), point2=(21.000000, 3.900000))
s0.Line(point1=(21.000000, 3.900000), point2=(21.000000, 3.000000))
s0.Line(point1=(21.000000, 3.000000), point2=(20.250000, 2.850000))
s0.Line(point1=(20.250000, 2.850000), point2=(19.800000, 3.300000))
s0.Line(point1=(19.800000, 3.300000), point2=(19.050000, 5.550000))
s0.Line(point1=(18.955132, 5.618377), point2=(19.741915, 5.689392))
s0.Line(point1=(19.741915, 5.689392), point2=(20.247385, 4.622597))
s0.Line(point1=(20.247385, 4.622597), point2=(21.155470, 3.983205))
s0.Line(point1=(21.155470, 3.983205), point2=(21.119612, 2.901942))
s0.Line(point1=(21.119612, 2.901942), point2=(20.198901, 2.681231))
s0.Line(point1=(20.198901, 2.681231), point2=(19.634421, 3.197667))
s0.Line(point1=(19.634421, 3.197667), point2=(18.955132, 5.618377))
s0.Line(point1=(19.144868, 5.481623), point2=(19.558085, 5.410608))
s0.Line(point1=(19.558085, 5.410608), point2=(19.952615, 4.377403))
s0.Line(point1=(19.952615, 4.377403), point2=(20.844530, 3.816795))
s0.Line(point1=(20.844530, 3.816795), point2=(20.880388, 3.098058))
s0.Line(point1=(20.880388, 3.098058), point2=(20.301099, 3.018769))
s0.Line(point1=(20.301099, 3.018769), point2=(19.965579, 3.402333))
s0.Line(point1=(19.965579, 3.402333), point2=(19.144868, 5.481623))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(19.800000, 46.050000), point2=(20.850000, 46.500000))
s0.Line(point1=(20.850000, 46.500000), point2=(22.050000, 46.050000))
s0.Line(point1=(22.050000, 46.050000), point2=(22.650000, 45.150000))
s0.Line(point1=(22.650000, 45.150000), point2=(22.500000, 44.250000))
s0.Line(point1=(22.500000, 44.250000), point2=(19.950000, 44.850000))
s0.Line(point1=(19.950000, 44.850000), point2=(19.650000, 45.300000))
s0.Line(point1=(19.650000, 45.300000), point2=(19.800000, 46.050000))
s0.Line(point1=(19.662550, 46.161526), point2=(20.845720, 46.685547))
s0.Line(point1=(20.845720, 46.685547), point2=(22.168317, 46.199103))
s0.Line(point1=(22.168317, 46.199103), point2=(22.831844, 45.189030))
s0.Line(point1=(22.831844, 45.189030), point2=(22.575735, 44.136218))
s0.Line(point1=(22.575735, 44.136218), point2=(19.843891, 44.697188))
s0.Line(point1=(19.843891, 44.697188), point2=(19.468737, 45.264142))
s0.Line(point1=(19.468737, 45.264142), point2=(19.662550, 46.161526))
s0.Line(point1=(19.937450, 45.938474), point2=(20.854280, 46.314453))
s0.Line(point1=(20.854280, 46.314453), point2=(21.931683, 45.900897))
s0.Line(point1=(21.931683, 45.900897), point2=(22.468156, 45.110970))
s0.Line(point1=(22.468156, 45.110970), point2=(22.424265, 44.363782))
s0.Line(point1=(22.424265, 44.363782), point2=(20.056109, 45.002812))
s0.Line(point1=(20.056109, 45.002812), point2=(19.831263, 45.335858))
s0.Line(point1=(19.831263, 45.335858), point2=(19.937450, 45.938474))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(19.800000, 1.800000), point2=(20.250000, 1.800000))
s0.Line(point1=(20.250000, 1.800000), point2=(21.000000, 2.700000))
s0.Line(point1=(21.000000, 2.700000), point2=(21.900000, 2.550000))
s0.Line(point1=(21.900000, 2.550000), point2=(21.750000, 1.500000))
s0.Line(point1=(21.750000, 1.500000), point2=(22.650000, 0.000000))
s0.Line(point1=(22.650000, 0.000000), point2=(19.950000, 0.000000))
s0.Line(point1=(19.950000, 0.000000), point2=(19.800000, 1.800000))
s0.Line(point1=(19.700345, 1.891695), point2=(20.173178, 1.964018))
s0.Line(point1=(20.173178, 1.964018), point2=(20.939618, 2.862658))
s0.Line(point1=(20.939618, 2.862658), point2=(22.015435, 2.634497))
s0.Line(point1=(22.015435, 2.634497), point2=(21.934744, 1.537307))
s0.Line(point1=(21.934744, 1.537307), point2=(22.735749, 0.000000))
s0.Line(point1=(22.735749, 0.000000), point2=(19.850345, 0.000000))
s0.Line(point1=(19.850345, 0.000000), point2=(19.700345, 1.891695))
s0.Line(point1=(19.899655, 1.708305), point2=(20.326822, 1.635982))
s0.Line(point1=(20.326822, 1.635982), point2=(21.060382, 2.537342))
s0.Line(point1=(21.060382, 2.537342), point2=(21.784565, 2.465503))
s0.Line(point1=(21.784565, 2.465503), point2=(21.565256, 1.462693))
s0.Line(point1=(21.565256, 1.462693), point2=(22.564251, 0.000000))
s0.Line(point1=(22.564251, 0.000000), point2=(20.049655, 0.000000))
s0.Line(point1=(20.049655, 0.000000), point2=(19.899655, 1.708305))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
print 60
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(19.950000, 35.850000), point2=(22.200000, 36.300000))
s0.Line(point1=(22.200000, 36.300000), point2=(22.050000, 35.700000))
s0.Line(point1=(22.050000, 35.700000), point2=(22.500000, 35.250000))
s0.Line(point1=(22.500000, 35.250000), point2=(22.500000, 34.650000))
s0.Line(point1=(22.500000, 34.650000), point2=(19.950000, 35.250000))
s0.Line(point1=(19.950000, 35.250000), point2=(19.950000, 35.850000))
s0.Line(point1=(19.830388, 35.948058), point2=(22.277403, 36.373805))
s0.Line(point1=(22.277403, 36.373805), point2=(22.217725, 35.746457))
s0.Line(point1=(22.217725, 35.746457), point2=(22.670711, 35.320711))
s0.Line(point1=(22.670711, 35.320711), point2=(22.577096, 34.552658))
s0.Line(point1=(22.577096, 34.552658), point2=(19.827096, 35.152658))
s0.Line(point1=(19.827096, 35.152658), point2=(19.830388, 35.948058))
s0.Line(point1=(20.069612, 35.751942), point2=(22.122597, 36.226195))
s0.Line(point1=(22.122597, 36.226195), point2=(21.882275, 35.653543))
s0.Line(point1=(21.882275, 35.653543), point2=(22.329289, 35.179289))
s0.Line(point1=(22.329289, 35.179289), point2=(22.422904, 34.747342))
s0.Line(point1=(22.422904, 34.747342), point2=(20.072904, 35.347342))
s0.Line(point1=(20.072904, 35.347342), point2=(20.069612, 35.751942))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(19.950000, 20.700000), point2=(20.850000, 21.000000))
s0.Line(point1=(20.850000, 21.000000), point2=(21.600000, 20.400000))
s0.Line(point1=(21.600000, 20.400000), point2=(21.750000, 19.500000))
s0.Line(point1=(21.750000, 19.500000), point2=(20.250000, 19.650000))
s0.Line(point1=(20.250000, 19.650000), point2=(19.950000, 20.700000))
s0.Line(point1=(19.822225, 20.767396), point2=(20.880847, 21.172955))
s0.Line(point1=(20.880847, 21.172955), point2=(21.761109, 20.494527))
s0.Line(point1=(21.761109, 20.494527), point2=(21.838689, 19.416936))
s0.Line(point1=(21.838689, 19.416936), point2=(20.143897, 19.523024))
s0.Line(point1=(20.143897, 19.523024), point2=(19.822225, 20.767396))
s0.Line(point1=(20.077775, 20.632604), point2=(20.819153, 20.827045))
s0.Line(point1=(20.819153, 20.827045), point2=(21.438891, 20.305473))
s0.Line(point1=(21.438891, 20.305473), point2=(21.661311, 19.583064))
s0.Line(point1=(21.661311, 19.583064), point2=(20.356103, 19.776976))
s0.Line(point1=(20.356103, 19.776976), point2=(20.077775, 20.632604))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(20.700000, 34.500000), point2=(21.600000, 34.350000))
s0.Line(point1=(21.600000, 34.350000), point2=(22.200000, 31.950000))
s0.Line(point1=(22.200000, 31.950000), point2=(22.950000, 31.050000))
s0.Line(point1=(22.950000, 31.050000), point2=(23.550000, 29.400000))
s0.Line(point1=(23.550000, 29.400000), point2=(23.250000, 28.350000))
s0.Line(point1=(23.250000, 28.350000), point2=(22.650000, 27.750000))
s0.Line(point1=(22.650000, 27.750000), point2=(22.050000, 27.750000))
s0.Line(point1=(22.050000, 27.750000), point2=(20.850000, 31.050000))
s0.Line(point1=(20.850000, 31.050000), point2=(20.400000, 33.000000))
s0.Line(point1=(20.400000, 33.000000), point2=(20.400000, 34.350000))
s0.Line(point1=(20.400000, 34.350000), point2=(20.700000, 34.500000))
s0.Line(point1=(20.671719, 34.688082), point2=(21.713454, 34.472893))
s0.Line(point1=(21.713454, 34.472893), point2=(22.373836, 32.038272))
s0.Line(point1=(22.373836, 32.038272), point2=(23.120801, 31.148193))
s0.Line(point1=(23.120801, 31.148193), point2=(23.740132, 29.406702))
s0.Line(point1=(23.740132, 29.406702), point2=(23.416863, 28.251817))
s0.Line(point1=(23.416863, 28.251817), point2=(22.720711, 27.579289))
s0.Line(point1=(22.720711, 27.579289), point2=(21.956021, 27.615826))
s0.Line(point1=(21.956021, 27.615826), point2=(20.658582, 30.993340))
s0.Line(point1=(20.658582, 30.993340), point2=(20.202561, 32.977514))
s0.Line(point1=(20.202561, 32.977514), point2=(20.255279, 34.439443))
s0.Line(point1=(20.255279, 34.439443), point2=(20.671719, 34.688082))
s0.Line(point1=(20.728281, 34.311918), point2=(21.486546, 34.227107))
s0.Line(point1=(21.486546, 34.227107), point2=(22.026164, 31.861728))
s0.Line(point1=(22.026164, 31.861728), point2=(22.779199, 30.951807))
s0.Line(point1=(22.779199, 30.951807), point2=(23.359868, 29.393298))
s0.Line(point1=(23.359868, 29.393298), point2=(23.083137, 28.448183))
s0.Line(point1=(23.083137, 28.448183), point2=(22.579289, 27.920711))
s0.Line(point1=(22.579289, 27.920711), point2=(22.143979, 27.884174))
s0.Line(point1=(22.143979, 27.884174), point2=(21.041418, 31.106660))
s0.Line(point1=(21.041418, 31.106660), point2=(20.597439, 33.022486))
s0.Line(point1=(20.597439, 33.022486), point2=(20.544721, 34.260557))
s0.Line(point1=(20.544721, 34.260557), point2=(20.728281, 34.311918))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(24.150000, 27.300000), point2=(23.850000, 26.400000))
s0.Line(point1=(23.850000, 26.400000), point2=(24.150000, 25.200000))
s0.Line(point1=(24.150000, 25.200000), point2=(21.150000, 25.650000))
s0.Line(point1=(21.150000, 25.650000), point2=(21.150000, 26.400000))
s0.Line(point1=(21.150000, 26.400000), point2=(22.500000, 26.550000))
s0.Line(point1=(22.500000, 26.550000), point2=(24.150000, 27.300000))
s0.Line(point1=(24.203488, 27.359414), point2=(24.041883, 26.392631))
s0.Line(point1=(24.041883, 26.392631), point2=(24.232180, 25.125360))
s0.Line(point1=(24.232180, 25.125360), point2=(21.035166, 25.551106))
s0.Line(point1=(21.035166, 25.551106), point2=(21.038957, 26.499388))
s0.Line(point1=(21.038957, 26.499388), point2=(22.447577, 26.740425))
s0.Line(point1=(22.447577, 26.740425), point2=(24.203488, 27.359414))
s0.Line(point1=(24.096512, 27.240586), point2=(23.658117, 26.407369))
s0.Line(point1=(23.658117, 26.407369), point2=(24.067820, 25.274640))
s0.Line(point1=(24.067820, 25.274640), point2=(21.264834, 25.748894))
s0.Line(point1=(21.264834, 25.748894), point2=(21.261043, 26.300612))
s0.Line(point1=(21.261043, 26.300612), point2=(22.552423, 26.359575))
s0.Line(point1=(22.552423, 26.359575), point2=(24.096512, 27.240586))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(21.600000, 40.050000), point2=(22.200000, 40.050000))
s0.Line(point1=(22.200000, 40.050000), point2=(22.800000, 39.600000))
s0.Line(point1=(22.800000, 39.600000), point2=(22.800000, 37.200000))
s0.Line(point1=(22.800000, 37.200000), point2=(22.050000, 37.350000))
s0.Line(point1=(22.050000, 37.350000), point2=(21.600000, 38.400000))
s0.Line(point1=(21.600000, 38.400000), point2=(21.600000, 40.050000))
s0.Line(point1=(21.500000, 40.150000), point2=(22.260000, 40.230000))
s0.Line(point1=(22.260000, 40.230000), point2=(22.960000, 39.680000))
s0.Line(point1=(22.960000, 39.680000), point2=(22.880388, 37.101942))
s0.Line(point1=(22.880388, 37.101942), point2=(21.938474, 37.212550))
s0.Line(point1=(21.938474, 37.212550), point2=(21.408085, 38.360608))
s0.Line(point1=(21.408085, 38.360608), point2=(21.500000, 40.150000))
s0.Line(point1=(21.700000, 39.950000), point2=(22.140000, 39.870000))
s0.Line(point1=(22.140000, 39.870000), point2=(22.640000, 39.520000))
s0.Line(point1=(22.640000, 39.520000), point2=(22.719612, 37.298058))
s0.Line(point1=(22.719612, 37.298058), point2=(22.161526, 37.487450))
s0.Line(point1=(22.161526, 37.487450), point2=(21.791915, 38.439392))
s0.Line(point1=(21.791915, 38.439392), point2=(21.700000, 39.950000))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(23.850000, 8.550000), point2=(23.700000, 7.500000))
s0.Line(point1=(23.700000, 7.500000), point2=(21.900000, 7.200000))
s0.Line(point1=(21.900000, 7.200000), point2=(22.650000, 8.700000))
s0.Line(point1=(22.650000, 8.700000), point2=(23.850000, 8.550000))
s0.Line(point1=(23.961398, 8.635086), point2=(23.815435, 7.387218))
s0.Line(point1=(23.815435, 7.387218), point2=(21.826997, 7.146082))
s0.Line(point1=(21.826997, 7.146082), point2=(22.572961, 8.843949))
s0.Line(point1=(22.572961, 8.843949), point2=(23.961398, 8.635086))
s0.Line(point1=(23.738602, 8.464914), point2=(23.584565, 7.612782))
s0.Line(point1=(23.584565, 7.612782), point2=(21.973003, 7.253918))
s0.Line(point1=(21.973003, 7.253918), point2=(22.727039, 8.556051))
s0.Line(point1=(22.727039, 8.556051), point2=(23.738602, 8.464914))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(22.350000, 6.900000), point2=(25.500000, 6.900000))
s0.Line(point1=(25.500000, 6.900000), point2=(25.500000, 6.450000))
s0.Line(point1=(25.500000, 6.450000), point2=(26.550000, 5.850000))
s0.Line(point1=(26.550000, 5.850000), point2=(27.300000, 4.800000))
s0.Line(point1=(27.300000, 4.800000), point2=(27.300000, 3.900000))
s0.Line(point1=(27.300000, 3.900000), point2=(22.050000, 4.500000))
s0.Line(point1=(22.050000, 4.500000), point2=(21.900000, 5.850000))
s0.Line(point1=(21.900000, 5.850000), point2=(22.350000, 6.300000))
s0.Line(point1=(22.350000, 6.300000), point2=(22.350000, 6.900000))
s0.Line(point1=(22.250000, 7.000000), point2=(25.600000, 7.000000))
s0.Line(point1=(25.600000, 7.000000), point2=(25.649614, 6.536824))
s0.Line(point1=(25.649614, 6.536824), point2=(26.680987, 5.994948))
s0.Line(point1=(26.680987, 5.994948), point2=(27.481373, 4.858124))
s0.Line(point1=(27.481373, 4.858124), point2=(27.388645, 3.800647))
s0.Line(point1=(27.388645, 3.800647), point2=(21.939257, 4.389604))
s0.Line(point1=(21.939257, 4.389604), point2=(21.729901, 5.909668))
s0.Line(point1=(21.729901, 5.909668), point2=(22.179289, 6.370711))
s0.Line(point1=(22.179289, 6.370711), point2=(22.250000, 7.000000))
s0.Line(point1=(22.450000, 6.800000), point2=(25.400000, 6.800000))
s0.Line(point1=(25.400000, 6.800000), point2=(25.350386, 6.363176))
s0.Line(point1=(25.350386, 6.363176), point2=(26.419013, 5.705052))
s0.Line(point1=(26.419013, 5.705052), point2=(27.118627, 4.741876))
s0.Line(point1=(27.118627, 4.741876), point2=(27.211355, 3.999353))
s0.Line(point1=(27.211355, 3.999353), point2=(22.160743, 4.610396))
s0.Line(point1=(22.160743, 4.610396), point2=(22.070099, 5.790332))
s0.Line(point1=(22.070099, 5.790332), point2=(22.520711, 6.229289))
s0.Line(point1=(22.520711, 6.229289), point2=(22.450000, 6.800000))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(22.800000, 24.750000), point2=(23.850000, 24.000000))
s0.Line(point1=(23.850000, 24.000000), point2=(24.000000, 22.650000))
s0.Line(point1=(24.000000, 22.650000), point2=(23.550000, 22.050000))
s0.Line(point1=(23.550000, 22.050000), point2=(22.800000, 23.250000))
s0.Line(point1=(22.800000, 23.250000), point2=(22.800000, 24.750000))
s0.Line(point1=(22.758124, 24.831373), point2=(24.007512, 24.092416))
s0.Line(point1=(24.007512, 24.092416), point2=(24.179388, 22.601043))
s0.Line(point1=(24.179388, 22.601043), point2=(23.545200, 21.937000))
s0.Line(point1=(23.545200, 21.937000), point2=(22.615200, 23.197000))
s0.Line(point1=(22.615200, 23.197000), point2=(22.758124, 24.831373))
s0.Line(point1=(22.841876, 24.668627), point2=(23.692488, 23.907584))
s0.Line(point1=(23.692488, 23.907584), point2=(23.820612, 22.698957))
s0.Line(point1=(23.820612, 22.698957), point2=(23.554800, 22.163000))
s0.Line(point1=(23.554800, 22.163000), point2=(22.984800, 23.303000))
s0.Line(point1=(22.984800, 23.303000), point2=(22.841876, 24.668627))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(26.250000, 48.900000), point2=(25.950000, 48.000000))
s0.Line(point1=(25.950000, 48.000000), point2=(26.100000, 47.250000))
s0.Line(point1=(26.100000, 47.250000), point2=(25.500000, 46.500000))
s0.Line(point1=(25.500000, 46.500000), point2=(25.500000, 44.250000))
s0.Line(point1=(25.500000, 44.250000), point2=(24.750000, 43.500000))
s0.Line(point1=(24.750000, 43.500000), point2=(23.700000, 43.350000))
s0.Line(point1=(23.700000, 43.350000), point2=(24.000000, 46.800000))
s0.Line(point1=(24.000000, 46.800000), point2=(23.100000, 47.100000))
s0.Line(point1=(23.100000, 47.100000), point2=(23.100000, 47.700000))
s0.Line(point1=(23.100000, 47.700000), point2=(25.650000, 48.900000))
s0.Line(point1=(25.650000, 48.900000), point2=(26.250000, 48.900000))
s0.Line(point1=(26.344868, 48.968377), point2=(26.142926, 47.987989))
s0.Line(point1=(26.142926, 47.987989), point2=(26.276145, 47.207142))
s0.Line(point1=(26.276145, 47.207142), point2=(25.678087, 46.437530))
s0.Line(point1=(25.678087, 46.437530), point2=(25.670711, 44.179289))
s0.Line(point1=(25.670711, 44.179289), point2=(24.834853, 43.330294))
s0.Line(point1=(24.834853, 43.330294), point2=(23.614518, 43.259668))
s0.Line(point1=(23.614518, 43.259668), point2=(23.868753, 46.713795))
s0.Line(point1=(23.868753, 46.713795), point2=(22.968377, 47.005132))
s0.Line(point1=(22.968377, 47.005132), point2=(22.957420, 47.790482))
s0.Line(point1=(22.957420, 47.790482), point2=(25.607420, 49.090482))
s0.Line(point1=(25.607420, 49.090482), point2=(26.344868, 48.968377))
s0.Line(point1=(26.155132, 48.831623), point2=(25.757074, 48.012011))
s0.Line(point1=(25.757074, 48.012011), point2=(25.923855, 47.292858))
s0.Line(point1=(25.923855, 47.292858), point2=(25.321913, 46.562470))
s0.Line(point1=(25.321913, 46.562470), point2=(25.329289, 44.320711))
s0.Line(point1=(25.329289, 44.320711), point2=(24.665147, 43.669706))
s0.Line(point1=(24.665147, 43.669706), point2=(23.785482, 43.440332))
s0.Line(point1=(23.785482, 43.440332), point2=(24.131247, 46.886205))
s0.Line(point1=(24.131247, 46.886205), point2=(23.231623, 47.194868))
s0.Line(point1=(23.231623, 47.194868), point2=(23.242580, 47.609518))
s0.Line(point1=(23.242580, 47.609518), point2=(25.692580, 48.709518))
s0.Line(point1=(25.692580, 48.709518), point2=(26.155132, 48.831623))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(23.250000, 37.950000), point2=(24.150000, 37.800000))
s0.Line(point1=(24.150000, 37.800000), point2=(24.450000, 37.050000))
s0.Line(point1=(24.450000, 37.050000), point2=(25.350000, 36.450000))
s0.Line(point1=(25.350000, 36.450000), point2=(25.050000, 35.550000))
s0.Line(point1=(25.050000, 35.550000), point2=(23.400000, 35.850000))
s0.Line(point1=(23.400000, 35.850000), point2=(23.250000, 37.950000))
s0.Line(point1=(23.166694, 38.041515), point2=(24.259288, 37.935778))
s0.Line(point1=(24.259288, 37.935778), point2=(24.598318, 37.170344))
s0.Line(point1=(24.598318, 37.170344), point2=(25.500338, 36.501582))
s0.Line(point1=(25.500338, 36.501582), point2=(25.126980, 35.419990))
s0.Line(point1=(25.126980, 35.419990), point2=(23.282366, 35.744488))
s0.Line(point1=(23.282366, 35.744488), point2=(23.166694, 38.041515))
s0.Line(point1=(23.333306, 37.858485), point2=(24.040712, 37.664222))
s0.Line(point1=(24.040712, 37.664222), point2=(24.301682, 36.929656))
s0.Line(point1=(24.301682, 36.929656), point2=(25.199662, 36.398418))
s0.Line(point1=(25.199662, 36.398418), point2=(24.973020, 35.680010))
s0.Line(point1=(24.973020, 35.680010), point2=(23.517634, 35.955512))
s0.Line(point1=(23.517634, 35.955512), point2=(23.333306, 37.858485))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(23.850000, 50.850000), point2=(24.300000, 50.850000))
s0.Line(point1=(24.300000, 50.850000), point2=(24.900000, 50.250000))
s0.Line(point1=(24.900000, 50.250000), point2=(24.900000, 48.900000))
s0.Line(point1=(24.900000, 48.900000), point2=(23.550000, 49.650000))
s0.Line(point1=(23.550000, 49.650000), point2=(23.400000, 50.100000))
s0.Line(point1=(23.400000, 50.100000), point2=(23.850000, 50.850000))
s0.Line(point1=(23.764251, 51.001450), point2=(24.370711, 51.020711))
s0.Line(point1=(24.370711, 51.020711), point2=(25.070711, 50.320711))
s0.Line(point1=(25.070711, 50.320711), point2=(24.951436, 48.812584))
s0.Line(point1=(24.951436, 48.812584), point2=(23.406567, 49.530961))
s0.Line(point1=(23.406567, 49.530961), point2=(23.219382, 50.119827))
s0.Line(point1=(23.219382, 50.119827), point2=(23.764251, 51.001450))
s0.Line(point1=(23.935749, 50.698550), point2=(24.229289, 50.679289))
s0.Line(point1=(24.229289, 50.679289), point2=(24.729289, 50.179289))
s0.Line(point1=(24.729289, 50.179289), point2=(24.848564, 48.987416))
s0.Line(point1=(24.848564, 48.987416), point2=(23.693433, 49.769039))
s0.Line(point1=(23.693433, 49.769039), point2=(23.580618, 50.080173))
s0.Line(point1=(23.580618, 50.080173), point2=(23.935749, 50.698550))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(23.550000, 34.500000), point2=(24.300000, 34.950000))
s0.Line(point1=(24.300000, 34.950000), point2=(27.150000, 34.500000))
s0.Line(point1=(27.150000, 34.500000), point2=(28.050000, 32.550000))
s0.Line(point1=(28.050000, 32.550000), point2=(27.750000, 31.050000))
s0.Line(point1=(27.750000, 31.050000), point2=(26.400000, 30.150000))
s0.Line(point1=(26.400000, 30.150000), point2=(24.450000, 30.450000))
s0.Line(point1=(24.450000, 30.450000), point2=(23.550000, 31.650000))
s0.Line(point1=(23.550000, 31.650000), point2=(23.850000, 32.550000))
s0.Line(point1=(23.850000, 32.550000), point2=(23.550000, 34.500000))
s0.Line(point1=(23.399713, 34.570544), point2=(24.264147, 35.134526))
s0.Line(point1=(24.264147, 35.134526), point2=(27.256392, 34.640682))
s0.Line(point1=(27.256392, 34.640682), point2=(28.238854, 32.572294))
s0.Line(point1=(28.238854, 32.572294), point2=(27.903528, 30.947183))
s0.Line(point1=(27.903528, 30.947183), point2=(26.440264, 29.967958))
s0.Line(point1=(26.440264, 29.967958), point2=(24.354794, 30.291163))
s0.Line(point1=(24.354794, 30.291163), point2=(23.375132, 31.621623))
s0.Line(point1=(23.375132, 31.621623), point2=(23.656295, 32.566417))
s0.Line(point1=(23.656295, 32.566417), point2=(23.399713, 34.570544))
s0.Line(point1=(23.700287, 34.429456), point2=(24.335853, 34.765474))
s0.Line(point1=(24.335853, 34.765474), point2=(27.043608, 34.359318))
s0.Line(point1=(27.043608, 34.359318), point2=(27.861146, 32.527706))
s0.Line(point1=(27.861146, 32.527706), point2=(27.596472, 31.152817))
s0.Line(point1=(27.596472, 31.152817), point2=(26.359736, 30.332042))
s0.Line(point1=(26.359736, 30.332042), point2=(24.545206, 30.608837))
s0.Line(point1=(24.545206, 30.608837), point2=(23.724868, 31.678377))
s0.Line(point1=(23.724868, 31.678377), point2=(24.043705, 32.533583))
s0.Line(point1=(24.043705, 32.533583), point2=(23.700287, 34.429456))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(25.800000, 42.750000), point2=(26.400000, 42.300000))
s0.Line(point1=(26.400000, 42.300000), point2=(26.850000, 41.100000))
s0.Line(point1=(26.850000, 41.100000), point2=(26.400000, 37.350000))
s0.Line(point1=(26.400000, 37.350000), point2=(24.900000, 37.950000))
s0.Line(point1=(24.900000, 37.950000), point2=(23.850000, 39.150000))
s0.Line(point1=(23.850000, 39.150000), point2=(24.000000, 40.800000))
s0.Line(point1=(24.000000, 40.800000), point2=(24.600000, 41.250000))
s0.Line(point1=(24.600000, 41.250000), point2=(24.600000, 41.850000))
s0.Line(point1=(24.600000, 41.850000), point2=(25.800000, 42.750000))
s0.Line(point1=(25.800000, 42.910000), point2=(26.553633, 42.415112))
s0.Line(point1=(26.553633, 42.415112), point2=(27.042921, 41.123198))
s0.Line(point1=(27.042921, 41.123198), point2=(26.462149, 37.245238))
s0.Line(point1=(26.462149, 37.245238), point2=(24.787603, 37.791302))
s0.Line(point1=(24.787603, 37.791302), point2=(23.675153, 39.093203))
s0.Line(point1=(23.675153, 39.093203), point2=(23.840411, 40.889054))
s0.Line(point1=(23.840411, 40.889054), point2=(24.440000, 41.330000))
s0.Line(point1=(24.440000, 41.330000), point2=(24.440000, 41.930000))
s0.Line(point1=(24.440000, 41.930000), point2=(25.800000, 42.910000))
s0.Line(point1=(25.800000, 42.590000), point2=(26.246367, 42.184888))
s0.Line(point1=(26.246367, 42.184888), point2=(26.657079, 41.076802))
s0.Line(point1=(26.657079, 41.076802), point2=(26.337851, 37.454762))
s0.Line(point1=(26.337851, 37.454762), point2=(25.012397, 38.108698))
s0.Line(point1=(25.012397, 38.108698), point2=(24.024847, 39.206797))
s0.Line(point1=(24.024847, 39.206797), point2=(24.159589, 40.710946))
s0.Line(point1=(24.159589, 40.710946), point2=(24.760000, 41.170000))
s0.Line(point1=(24.760000, 41.170000), point2=(24.760000, 41.770000))
s0.Line(point1=(24.760000, 41.770000), point2=(25.800000, 42.590000))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(25.050000, 11.850000), point2=(25.350000, 10.950000))
s0.Line(point1=(25.350000, 10.950000), point2=(24.750000, 9.900000))
s0.Line(point1=(24.750000, 9.900000), point2=(24.150000, 9.750000))
s0.Line(point1=(24.150000, 9.750000), point2=(23.850000, 10.800000))
s0.Line(point1=(23.850000, 10.800000), point2=(24.600000, 11.850000))
s0.Line(point1=(24.600000, 11.850000), point2=(25.050000, 11.850000))
s0.Line(point1=(25.144868, 11.981623), point2=(25.531693, 10.932009))
s0.Line(point1=(25.531693, 10.932009), point2=(24.861078, 9.753372))
s0.Line(point1=(24.861078, 9.753372), point2=(24.078101, 9.625514))
s0.Line(point1=(24.078101, 9.625514), point2=(23.672474, 10.830652))
s0.Line(point1=(23.672474, 10.830652), point2=(24.518627, 12.008124))
s0.Line(point1=(24.518627, 12.008124), point2=(25.144868, 11.981623))
s0.Line(point1=(24.955132, 11.718377), point2=(25.168307, 10.967991))
s0.Line(point1=(25.168307, 10.967991), point2=(24.638922, 10.046628))
s0.Line(point1=(24.638922, 10.046628), point2=(24.221899, 9.874486))
s0.Line(point1=(24.221899, 9.874486), point2=(24.027526, 10.769348))
s0.Line(point1=(24.027526, 10.769348), point2=(24.681373, 11.691876))
s0.Line(point1=(24.681373, 11.691876), point2=(24.955132, 11.718377))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(25.800000, 24.450000), point2=(27.600000, 23.250000))
s0.Line(point1=(27.600000, 23.250000), point2=(27.450000, 20.550000))
s0.Line(point1=(27.450000, 20.550000), point2=(27.000000, 19.650000))
s0.Line(point1=(27.000000, 19.650000), point2=(25.050000, 20.250000))
s0.Line(point1=(25.050000, 20.250000), point2=(24.000000, 21.450000))
s0.Line(point1=(24.000000, 21.450000), point2=(24.150000, 22.350000))
s0.Line(point1=(24.150000, 22.350000), point2=(25.350000, 23.250000))
s0.Line(point1=(25.350000, 23.250000), point2=(25.800000, 24.450000))
s0.Line(point1=(25.761837, 24.568317), point2=(27.755316, 23.327658))
s0.Line(point1=(27.755316, 23.327658), point2=(27.639289, 20.499732))
s0.Line(point1=(27.639289, 20.499732), point2=(27.060034, 19.509701))
s0.Line(point1=(27.060034, 19.509701), point2=(24.945334, 20.088572))
s0.Line(point1=(24.945334, 20.088572), point2=(23.826103, 21.400589))
s0.Line(point1=(23.826103, 21.400589), point2=(23.991361, 22.446440))
s0.Line(point1=(23.991361, 22.446440), point2=(25.196367, 23.365112))
s0.Line(point1=(25.196367, 23.365112), point2=(25.761837, 24.568317))
s0.Line(point1=(25.838163, 24.331683), point2=(27.444684, 23.172342))
s0.Line(point1=(27.444684, 23.172342), point2=(27.260711, 20.600268))
s0.Line(point1=(27.260711, 20.600268), point2=(26.939966, 19.790299))
s0.Line(point1=(26.939966, 19.790299), point2=(25.154666, 20.411428))
s0.Line(point1=(25.154666, 20.411428), point2=(24.173897, 21.499411))
s0.Line(point1=(24.173897, 21.499411), point2=(24.308639, 22.253560))
s0.Line(point1=(24.308639, 22.253560), point2=(25.503633, 23.134888))
s0.Line(point1=(25.503633, 23.134888), point2=(25.838163, 24.331683))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(24.750000, 3.300000), point2=(25.650000, 3.450000))
s0.Line(point1=(25.650000, 3.450000), point2=(25.950000, 3.150000))
s0.Line(point1=(25.950000, 3.150000), point2=(25.800000, 1.650000))
s0.Line(point1=(25.800000, 1.650000), point2=(25.050000, 2.100000))
s0.Line(point1=(25.050000, 2.100000), point2=(24.600000, 3.000000))
s0.Line(point1=(24.600000, 3.000000), point2=(24.750000, 3.300000))
s0.Line(point1=(24.644117, 3.443361), point2=(25.704271, 3.619350))
s0.Line(point1=(25.704271, 3.619350), point2=(26.120214, 3.210760))
s0.Line(point1=(26.120214, 3.210760), point2=(25.848054, 1.554300))
s0.Line(point1=(25.848054, 1.554300), point2=(24.909108, 1.969529))
s0.Line(point1=(24.909108, 1.969529), point2=(24.421115, 3.000000))
s0.Line(point1=(24.421115, 3.000000), point2=(24.644117, 3.443361))
s0.Line(point1=(24.855883, 3.156639), point2=(25.595729, 3.280650))
s0.Line(point1=(25.595729, 3.280650), point2=(25.779786, 3.089240))
s0.Line(point1=(25.779786, 3.089240), point2=(25.751946, 1.745700))
s0.Line(point1=(25.751946, 1.745700), point2=(25.190892, 2.230471))
s0.Line(point1=(25.190892, 2.230471), point2=(24.778885, 3.000000))
s0.Line(point1=(24.778885, 3.000000), point2=(24.855883, 3.156639))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(35.250000, 30.150000), point2=(34.950000, 24.600000))
s0.Line(point1=(34.950000, 24.600000), point2=(34.650000, 24.150000))
s0.Line(point1=(34.650000, 24.150000), point2=(33.150000, 24.150000))
s0.Line(point1=(33.150000, 24.150000), point2=(28.500000, 25.350000))
s0.Line(point1=(28.500000, 25.350000), point2=(26.100000, 25.200000))
s0.Line(point1=(26.100000, 25.200000), point2=(25.350000, 25.800000))
s0.Line(point1=(25.350000, 25.800000), point2=(24.750000, 27.000000))
s0.Line(point1=(24.750000, 27.000000), point2=(24.900000, 27.750000))
s0.Line(point1=(24.900000, 27.750000), point2=(25.500000, 28.350000))
s0.Line(point1=(25.500000, 28.350000), point2=(28.500000, 29.700000))
s0.Line(point1=(28.500000, 29.700000), point2=(28.800000, 30.600000))
s0.Line(point1=(28.800000, 30.600000), point2=(28.500000, 31.800000))
s0.Line(point1=(28.500000, 31.800000), point2=(29.100000, 32.250000))
s0.Line(point1=(29.100000, 32.250000), point2=(32.700000, 30.900000))
s0.Line(point1=(32.700000, 30.900000), point2=(33.450000, 30.900000))
s0.Line(point1=(33.450000, 30.900000), point2=(34.200000, 31.350000))
s0.Line(point1=(34.200000, 31.350000), point2=(35.250000, 30.150000))
s0.Line(point1=(35.425112, 30.210453), point2=(35.133059, 24.539132))
s0.Line(point1=(35.133059, 24.539132), point2=(34.733205, 23.994530))
s0.Line(point1=(34.733205, 23.994530), point2=(33.125012, 23.953172))
s0.Line(point1=(33.125012, 23.953172), point2=(28.481250, 25.153367))
s0.Line(point1=(28.481250, 25.153367), point2=(26.043768, 25.022108))
s0.Line(point1=(26.043768, 25.022108), point2=(25.198088, 25.677192))
s0.Line(point1=(25.198088, 25.677192), point2=(24.562499, 26.974890))
s0.Line(point1=(24.562499, 26.974890), point2=(24.731231, 27.840322))
s0.Line(point1=(24.731231, 27.840322), point2=(25.388253, 28.511903))
s0.Line(point1=(25.388253, 28.511903), point2=(28.364095, 29.822815))
s0.Line(point1=(28.364095, 29.822815), point2=(28.608117, 30.607369))
s0.Line(point1=(28.608117, 30.607369), point2=(28.342986, 31.855746))
s0.Line(point1=(28.342986, 31.855746), point2=(29.075112, 32.423633))
s0.Line(point1=(29.075112, 32.423633), point2=(32.735112, 31.093633))
s0.Line(point1=(32.735112, 31.093633), point2=(33.398550, 31.085749))
s0.Line(point1=(33.398550, 31.085749), point2=(34.223808, 31.501600))
s0.Line(point1=(34.223808, 31.501600), point2=(35.425112, 30.210453))
s0.Line(point1=(35.074888, 30.089547), point2=(34.766941, 24.660868))
s0.Line(point1=(34.766941, 24.660868), point2=(34.566795, 24.305470))
s0.Line(point1=(34.566795, 24.305470), point2=(33.174988, 24.346828))
s0.Line(point1=(33.174988, 24.346828), point2=(28.518750, 25.546633))
s0.Line(point1=(28.518750, 25.546633), point2=(26.156232, 25.377892))
s0.Line(point1=(26.156232, 25.377892), point2=(25.501912, 25.922808))
s0.Line(point1=(25.501912, 25.922808), point2=(24.937501, 27.025110))
s0.Line(point1=(24.937501, 27.025110), point2=(25.068769, 27.659678))
s0.Line(point1=(25.068769, 27.659678), point2=(25.611747, 28.188097))
s0.Line(point1=(25.611747, 28.188097), point2=(28.635905, 29.577185))
s0.Line(point1=(28.635905, 29.577185), point2=(28.991883, 30.592631))
s0.Line(point1=(28.991883, 30.592631), point2=(28.657014, 31.744254))
s0.Line(point1=(28.657014, 31.744254), point2=(29.124888, 32.076367))
s0.Line(point1=(29.124888, 32.076367), point2=(32.664888, 30.706367))
s0.Line(point1=(32.664888, 30.706367), point2=(33.501450, 30.714251))
s0.Line(point1=(33.501450, 30.714251), point2=(34.176192, 31.198400))
s0.Line(point1=(34.176192, 31.198400), point2=(35.074888, 30.089547))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(27.150000, 18.150000), point2=(27.450000, 13.800000))
s0.Line(point1=(27.450000, 13.800000), point2=(25.800000, 13.200000))
s0.Line(point1=(25.800000, 13.200000), point2=(26.100000, 14.400000))
s0.Line(point1=(26.100000, 14.400000), point2=(25.350000, 14.250000))
s0.Line(point1=(25.350000, 14.250000), point2=(25.350000, 14.700000))
s0.Line(point1=(25.350000, 14.700000), point2=(26.700000, 16.950000))
s0.Line(point1=(26.700000, 16.950000), point2=(26.700000, 18.150000))
s0.Line(point1=(26.700000, 18.150000), point2=(27.150000, 18.150000))
s0.Line(point1=(27.249763, 18.256880), point2=(27.583937, 13.712901))
s0.Line(point1=(27.583937, 13.712901), point2=(25.737160, 13.130274))
s0.Line(point1=(25.737160, 13.130274), point2=(26.022597, 14.326195))
s0.Line(point1=(26.022597, 14.326195), point2=(25.269612, 14.151942))
s0.Line(point1=(25.269612, 14.151942), point2=(25.164251, 14.751450))
s0.Line(point1=(25.164251, 14.751450), point2=(26.514251, 17.001450))
s0.Line(point1=(26.514251, 17.001450), point2=(26.600000, 18.250000))
s0.Line(point1=(26.600000, 18.250000), point2=(27.249763, 18.256880))
s0.Line(point1=(27.050237, 18.043120), point2=(27.316063, 13.887099))
s0.Line(point1=(27.316063, 13.887099), point2=(25.862840, 13.269726))
s0.Line(point1=(25.862840, 13.269726), point2=(26.177403, 14.473805))
s0.Line(point1=(26.177403, 14.473805), point2=(25.430388, 14.348058))
s0.Line(point1=(25.430388, 14.348058), point2=(25.535749, 14.648550))
s0.Line(point1=(25.535749, 14.648550), point2=(26.885749, 16.898550))
s0.Line(point1=(26.885749, 16.898550), point2=(26.800000, 18.050000))
s0.Line(point1=(26.800000, 18.050000), point2=(27.050237, 18.043120))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(31.350000, 11.100000), point2=(31.350000, 10.200000))
s0.Line(point1=(31.350000, 10.200000), point2=(30.600000, 10.050000))
s0.Line(point1=(30.600000, 10.050000), point2=(29.850000, 9.150000))
s0.Line(point1=(29.850000, 9.150000), point2=(28.200000, 8.700000))
s0.Line(point1=(28.200000, 8.700000), point2=(27.900000, 7.650000))
s0.Line(point1=(27.900000, 7.650000), point2=(27.000000, 7.650000))
s0.Line(point1=(27.000000, 7.650000), point2=(25.350000, 8.700000))
s0.Line(point1=(25.350000, 8.700000), point2=(25.800000, 10.500000))
s0.Line(point1=(25.800000, 10.500000), point2=(25.650000, 12.000000))
s0.Line(point1=(25.650000, 12.000000), point2=(26.400000, 12.600000))
s0.Line(point1=(26.400000, 12.600000), point2=(27.900000, 12.900000))
s0.Line(point1=(27.900000, 12.900000), point2=(28.500000, 13.350000))
s0.Line(point1=(28.500000, 13.350000), point2=(31.350000, 11.100000))
s0.Line(point1=(31.511964, 11.178488), point2=(31.469612, 10.101942))
s0.Line(point1=(31.469612, 10.101942), point2=(30.696434, 9.887923))
s0.Line(point1=(30.696434, 9.887923), point2=(29.953134, 8.989505))
s0.Line(point1=(29.953134, 8.989505), point2=(28.322464, 8.576052))
s0.Line(point1=(28.322464, 8.576052), point2=(27.996152, 7.522528))
s0.Line(point1=(27.996152, 7.522528), point2=(26.946312, 7.465634))
s0.Line(point1=(26.946312, 7.465634), point2=(25.199298, 8.639887))
s0.Line(point1=(25.199298, 8.639887), point2=(25.603482, 10.514303))
s0.Line(point1=(25.603482, 10.514303), point2=(25.488027, 12.068137))
s0.Line(point1=(25.488027, 12.068137), point2=(26.317919, 12.776145))
s0.Line(point1=(26.317919, 12.776145), point2=(27.820388, 13.078058))
s0.Line(point1=(27.820388, 13.078058), point2=(28.501964, 13.508488))
s0.Line(point1=(28.501964, 13.508488), point2=(31.511964, 11.178488))
s0.Line(point1=(31.188036, 11.021512), point2=(31.230388, 10.298058))
s0.Line(point1=(31.230388, 10.298058), point2=(30.503566, 10.212077))
s0.Line(point1=(30.503566, 10.212077), point2=(29.746866, 9.310495))
s0.Line(point1=(29.746866, 9.310495), point2=(28.077536, 8.823948))
s0.Line(point1=(28.077536, 8.823948), point2=(27.803848, 7.777472))
s0.Line(point1=(27.803848, 7.777472), point2=(27.053688, 7.834366))
s0.Line(point1=(27.053688, 7.834366), point2=(25.500702, 8.760113))
s0.Line(point1=(25.500702, 8.760113), point2=(25.996518, 10.485697))
s0.Line(point1=(25.996518, 10.485697), point2=(25.811973, 11.931863))
s0.Line(point1=(25.811973, 11.931863), point2=(26.482081, 12.423855))
s0.Line(point1=(26.482081, 12.423855), point2=(27.979612, 12.721942))
s0.Line(point1=(27.979612, 12.721942), point2=(28.498036, 13.191512))
s0.Line(point1=(28.498036, 13.191512), point2=(31.188036, 11.021512))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(27.900000, 48.150000), point2=(28.650000, 47.250000))
s0.Line(point1=(28.650000, 47.250000), point2=(29.400000, 45.300000))
s0.Line(point1=(29.400000, 45.300000), point2=(28.050000, 45.150000))
s0.Line(point1=(28.050000, 45.150000), point2=(26.850000, 44.550000))
s0.Line(point1=(26.850000, 44.550000), point2=(26.250000, 45.300000))
s0.Line(point1=(26.250000, 45.300000), point2=(26.400000, 46.050000))
s0.Line(point1=(26.400000, 46.050000), point2=(27.450000, 48.000000))
s0.Line(point1=(27.450000, 48.000000), point2=(27.900000, 48.150000))
s0.Line(point1=(27.945199, 48.308887), point2=(28.820157, 47.349916))
s0.Line(point1=(28.820157, 47.349916), point2=(29.504378, 45.236510))
s0.Line(point1=(29.504378, 45.236510), point2=(28.105765, 44.961169))
s0.Line(point1=(28.105765, 44.961169), point2=(26.816634, 44.398088))
s0.Line(point1=(26.816634, 44.398088), point2=(26.073855, 45.257142))
s0.Line(point1=(26.073855, 45.257142), point2=(26.213895, 46.117022))
s0.Line(point1=(26.213895, 46.117022), point2=(27.330330, 48.142278))
s0.Line(point1=(27.330330, 48.142278), point2=(27.945199, 48.308887))
s0.Line(point1=(27.854801, 47.991113), point2=(28.479843, 47.150084))
s0.Line(point1=(28.479843, 47.150084), point2=(29.295622, 45.363490))
s0.Line(point1=(29.295622, 45.363490), point2=(27.994235, 45.338831))
s0.Line(point1=(27.994235, 45.338831), point2=(26.883366, 44.701912))
s0.Line(point1=(26.883366, 44.701912), point2=(26.426145, 45.342858))
s0.Line(point1=(26.426145, 45.342858), point2=(26.586105, 45.982978))
s0.Line(point1=(26.586105, 45.982978), point2=(27.569670, 47.857722))
s0.Line(point1=(27.569670, 47.857722), point2=(27.854801, 47.991113))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
print 80
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(26.400000, 52.500000), point2=(30.900000, 52.500000))
s0.Line(point1=(30.900000, 52.500000), point2=(31.950000, 50.400000))
s0.Line(point1=(31.950000, 50.400000), point2=(32.400000, 48.300000))
s0.Line(point1=(32.400000, 48.300000), point2=(31.500000, 47.700000))
s0.Line(point1=(31.500000, 47.700000), point2=(30.900000, 47.700000))
s0.Line(point1=(30.900000, 47.700000), point2=(27.150000, 48.750000))
s0.Line(point1=(27.150000, 48.750000), point2=(26.550000, 49.650000))
s0.Line(point1=(26.550000, 49.650000), point2=(26.400000, 52.500000))
s0.Line(point1=(26.300138, 52.500000), point2=(30.989443, 52.500000))
s0.Line(point1=(30.989443, 52.500000), point2=(32.137223, 50.465674))
s0.Line(point1=(32.137223, 50.465674), point2=(32.553250, 48.237748))
s0.Line(point1=(32.553250, 48.237748), point2=(31.555470, 47.516795))
s0.Line(point1=(31.555470, 47.516795), point2=(30.873037, 47.503704))
s0.Line(point1=(30.873037, 47.503704), point2=(27.039832, 48.598234))
s0.Line(point1=(27.039832, 48.598234), point2=(26.366933, 49.589274))
s0.Line(point1=(26.366933, 49.589274), point2=(26.300138, 52.500000))
s0.Line(point1=(26.499862, 52.500000), point2=(30.810557, 52.500000))
s0.Line(point1=(30.810557, 52.500000), point2=(31.762777, 50.334326))
s0.Line(point1=(31.762777, 50.334326), point2=(32.246750, 48.362252))
s0.Line(point1=(32.246750, 48.362252), point2=(31.444530, 47.883205))
s0.Line(point1=(31.444530, 47.883205), point2=(30.926963, 47.896296))
s0.Line(point1=(30.926963, 47.896296), point2=(27.260168, 48.901766))
s0.Line(point1=(27.260168, 48.901766), point2=(26.733067, 49.710726))
s0.Line(point1=(26.733067, 49.710726), point2=(26.499862, 52.500000))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(28.350000, 1.050000), point2=(28.050000, 0.000000))
s0.Line(point1=(28.050000, 0.000000), point2=(26.400000, 0.000000))
s0.Line(point1=(26.400000, 0.000000), point2=(26.400000, 0.600000))
s0.Line(point1=(26.400000, 0.600000), point2=(27.000000, 1.500000))
s0.Line(point1=(27.000000, 1.500000), point2=(28.350000, 1.050000))
s0.Line(point1=(28.477775, 1.117396), point2=(28.146152, 0.000000))
s0.Line(point1=(28.146152, 0.000000), point2=(26.300000, 0.000000))
s0.Line(point1=(26.300000, 0.000000), point2=(26.216795, 0.655470))
s0.Line(point1=(26.216795, 0.655470), point2=(26.948418, 1.650338))
s0.Line(point1=(26.948418, 1.650338), point2=(28.477775, 1.117396))
s0.Line(point1=(28.222225, 0.982604), point2=(27.953848, 0.000000))
s0.Line(point1=(27.953848, 0.000000), point2=(26.500000, 0.000000))
s0.Line(point1=(26.500000, 0.000000), point2=(26.583205, 0.544530))
s0.Line(point1=(26.583205, 0.544530), point2=(27.051582, 1.349662))
s0.Line(point1=(27.051582, 1.349662), point2=(28.222225, 0.982604))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(27.300000, 38.400000), point2=(28.350000, 38.400000))
s0.Line(point1=(28.350000, 38.400000), point2=(28.650000, 37.800000))
s0.Line(point1=(28.650000, 37.800000), point2=(28.350000, 36.150000))
s0.Line(point1=(28.350000, 36.150000), point2=(27.750000, 36.150000))
s0.Line(point1=(27.750000, 36.150000), point2=(27.150000, 36.900000))
s0.Line(point1=(27.150000, 36.900000), point2=(27.300000, 38.400000))
s0.Line(point1=(27.200496, 38.509950), point2=(28.439443, 38.544721))
s0.Line(point1=(28.439443, 38.544721), point2=(28.837830, 37.826833))
s0.Line(point1=(28.837830, 37.826833), point2=(28.448387, 36.032111))
s0.Line(point1=(28.448387, 36.032111), point2=(27.671913, 35.987530))
s0.Line(point1=(27.671913, 35.987530), point2=(26.972409, 36.847481))
s0.Line(point1=(26.972409, 36.847481), point2=(27.200496, 38.509950))
s0.Line(point1=(27.399504, 38.290050), point2=(28.260557, 38.255279))
s0.Line(point1=(28.260557, 38.255279), point2=(28.462170, 37.773167))
s0.Line(point1=(28.462170, 37.773167), point2=(28.251613, 36.267889))
s0.Line(point1=(28.251613, 36.267889), point2=(27.828087, 36.312470))
s0.Line(point1=(27.828087, 36.312470), point2=(27.327591, 36.952519))
s0.Line(point1=(27.327591, 36.952519), point2=(27.399504, 38.290050))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(28.050000, 35.250000), point2=(28.800000, 35.250000))
s0.Line(point1=(28.800000, 35.250000), point2=(29.250000, 34.800000))
s0.Line(point1=(29.250000, 34.800000), point2=(29.100000, 33.450000))
s0.Line(point1=(29.100000, 33.450000), point2=(28.500000, 33.450000))
s0.Line(point1=(28.500000, 33.450000), point2=(28.350000, 34.050000))
s0.Line(point1=(28.350000, 34.050000), point2=(27.900000, 34.200000))
s0.Line(point1=(27.900000, 34.200000), point2=(28.050000, 35.250000))
s0.Line(point1=(27.951005, 35.364142), point2=(28.870711, 35.420711))
s0.Line(point1=(28.870711, 35.420711), point2=(29.420099, 34.859668))
s0.Line(point1=(29.420099, 34.859668), point2=(29.199388, 33.338957))
s0.Line(point1=(29.199388, 33.338957), point2=(28.402986, 33.325746))
s0.Line(point1=(28.402986, 33.325746), point2=(28.221363, 33.930878))
s0.Line(point1=(28.221363, 33.930878), point2=(27.769382, 34.119274))
s0.Line(point1=(27.769382, 34.119274), point2=(27.951005, 35.364142))
s0.Line(point1=(28.148995, 35.135858), point2=(28.729289, 35.079289))
s0.Line(point1=(28.729289, 35.079289), point2=(29.079901, 34.740332))
s0.Line(point1=(29.079901, 34.740332), point2=(29.000612, 33.561043))
s0.Line(point1=(29.000612, 33.561043), point2=(28.597014, 33.574254))
s0.Line(point1=(28.597014, 33.574254), point2=(28.478637, 34.169122))
s0.Line(point1=(28.478637, 34.169122), point2=(28.030618, 34.280726))
s0.Line(point1=(28.030618, 34.280726), point2=(28.148995, 35.135858))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(27.900000, 17.250000), point2=(28.650000, 17.550000))
s0.Line(point1=(28.650000, 17.550000), point2=(30.300000, 16.950000))
s0.Line(point1=(30.300000, 16.950000), point2=(30.450000, 16.500000))
s0.Line(point1=(30.450000, 16.500000), point2=(30.000000, 16.050000))
s0.Line(point1=(30.000000, 16.050000), point2=(28.650000, 16.050000))
s0.Line(point1=(28.650000, 16.050000), point2=(28.050000, 16.350000))
s0.Line(point1=(28.050000, 16.350000), point2=(27.900000, 17.250000))
s0.Line(point1=(27.764222, 17.326408), point2=(28.647035, 17.736827))
s0.Line(point1=(28.647035, 17.736827), point2=(30.429043, 17.075602))
s0.Line(point1=(30.429043, 17.075602), point2=(30.615579, 16.460912))
s0.Line(point1=(30.615579, 16.460912), point2=(30.070711, 15.879289))
s0.Line(point1=(30.070711, 15.879289), point2=(28.605279, 15.860557))
s0.Line(point1=(28.605279, 15.860557), point2=(27.906639, 16.244117))
s0.Line(point1=(27.906639, 16.244117), point2=(27.764222, 17.326408))
s0.Line(point1=(28.035778, 17.173592), point2=(28.652965, 17.363173))
s0.Line(point1=(28.652965, 17.363173), point2=(30.170957, 16.824398))
s0.Line(point1=(30.170957, 16.824398), point2=(30.284421, 16.539088))
s0.Line(point1=(30.284421, 16.539088), point2=(29.929289, 16.220711))
s0.Line(point1=(29.929289, 16.220711), point2=(28.694721, 16.239443))
s0.Line(point1=(28.694721, 16.239443), point2=(28.193361, 16.455883))
s0.Line(point1=(28.193361, 16.455883), point2=(28.035778, 17.173592))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(28.350000, 22.350000), point2=(30.000000, 23.250000))
s0.Line(point1=(30.000000, 23.250000), point2=(30.750000, 22.950000))
s0.Line(point1=(30.750000, 22.950000), point2=(30.900000, 21.900000))
s0.Line(point1=(30.900000, 21.900000), point2=(30.600000, 20.850000))
s0.Line(point1=(30.600000, 20.850000), point2=(29.250000, 20.700000))
s0.Line(point1=(29.250000, 20.700000), point2=(28.650000, 21.300000))
s0.Line(point1=(28.650000, 21.300000), point2=(28.350000, 22.350000))
s0.Line(point1=(28.205962, 22.410317), point2=(29.989254, 23.430637))
s0.Line(point1=(29.989254, 23.430637), point2=(30.886134, 23.056990))
s0.Line(point1=(30.886134, 23.056990), point2=(31.095147, 21.886670))
s0.Line(point1=(31.095147, 21.886670), point2=(30.707196, 20.723140))
s0.Line(point1=(30.707196, 20.723140), point2=(29.190332, 20.529901))
s0.Line(point1=(29.190332, 20.529901), point2=(28.483137, 21.201817))
s0.Line(point1=(28.483137, 21.201817), point2=(28.205962, 22.410317))
s0.Line(point1=(28.494038, 22.289683), point2=(30.010746, 23.069363))
s0.Line(point1=(30.010746, 23.069363), point2=(30.613866, 22.843010))
s0.Line(point1=(30.613866, 22.843010), point2=(30.704853, 21.913330))
s0.Line(point1=(30.704853, 21.913330), point2=(30.492804, 20.976860))
s0.Line(point1=(30.492804, 20.976860), point2=(29.309668, 20.870099))
s0.Line(point1=(29.309668, 20.870099), point2=(28.816863, 21.398183))
s0.Line(point1=(28.816863, 21.398183), point2=(28.494038, 22.289683))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(28.350000, 15.450000), point2=(29.400000, 15.150000))
s0.Line(point1=(29.400000, 15.150000), point2=(29.400000, 15.450000))
s0.Line(point1=(29.400000, 15.450000), point2=(30.450000, 15.300000))
s0.Line(point1=(30.450000, 15.300000), point2=(31.350000, 15.750000))
s0.Line(point1=(31.350000, 15.750000), point2=(31.350000, 15.000000))
s0.Line(point1=(31.350000, 15.000000), point2=(30.900000, 14.400000))
s0.Line(point1=(30.900000, 14.400000), point2=(31.200000, 12.450000))
s0.Line(point1=(31.200000, 12.450000), point2=(30.600000, 12.450000))
s0.Line(point1=(30.600000, 12.450000), point2=(28.950000, 14.400000))
s0.Line(point1=(28.950000, 14.400000), point2=(28.500000, 14.550000))
s0.Line(point1=(28.500000, 14.550000), point2=(28.350000, 15.450000))
s0.Line(point1=(28.278833, 15.529712), point2=(29.327472, 15.246152))
s0.Line(point1=(29.327472, 15.246152), point2=(29.314142, 15.548995))
s0.Line(point1=(29.314142, 15.548995), point2=(30.419421, 15.488438))
s0.Line(point1=(30.419421, 15.488438), point2=(31.405279, 15.839443))
s0.Line(point1=(31.405279, 15.839443), point2=(31.530000, 14.940000))
s0.Line(point1=(31.530000, 14.940000), point2=(31.078837, 14.355206))
s0.Line(point1=(31.078837, 14.355206), point2=(31.298837, 12.365206))
s0.Line(point1=(31.298837, 12.365206), point2=(30.523661, 12.285406))
s0.Line(point1=(30.523661, 12.285406), point2=(28.842039, 14.240537))
s0.Line(point1=(28.842039, 14.240537), point2=(28.369738, 14.438692))
s0.Line(point1=(28.369738, 14.438692), point2=(28.278833, 15.529712))
s0.Line(point1=(28.421167, 15.370288), point2=(29.472528, 15.053848))
s0.Line(point1=(29.472528, 15.053848), point2=(29.485858, 15.351005))
s0.Line(point1=(29.485858, 15.351005), point2=(30.480579, 15.111562))
s0.Line(point1=(30.480579, 15.111562), point2=(31.294721, 15.660557))
s0.Line(point1=(31.294721, 15.660557), point2=(31.170000, 15.060000))
s0.Line(point1=(31.170000, 15.060000), point2=(30.721163, 14.444794))
s0.Line(point1=(30.721163, 14.444794), point2=(31.101163, 12.534794))
s0.Line(point1=(31.101163, 12.534794), point2=(30.676339, 12.614594))
s0.Line(point1=(30.676339, 12.614594), point2=(29.057961, 14.559463))
s0.Line(point1=(29.057961, 14.559463), point2=(28.630262, 14.661308))
s0.Line(point1=(28.630262, 14.661308), point2=(28.421167, 15.370288))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(30.750000, 40.650000), point2=(30.750000, 40.050000))
s0.Line(point1=(30.750000, 40.050000), point2=(29.850000, 39.450000))
s0.Line(point1=(29.850000, 39.450000), point2=(28.500000, 39.600000))
s0.Line(point1=(28.500000, 39.600000), point2=(28.500000, 40.200000))
s0.Line(point1=(28.500000, 40.200000), point2=(29.400000, 40.500000))
s0.Line(point1=(29.400000, 40.500000), point2=(29.400000, 40.800000))
s0.Line(point1=(29.400000, 40.800000), point2=(30.750000, 40.650000))
s0.Line(point1=(30.861043, 40.749388), point2=(30.905470, 39.966795))
s0.Line(point1=(30.905470, 39.966795), point2=(29.894427, 39.267407))
s0.Line(point1=(29.894427, 39.267407), point2=(28.388957, 39.500612))
s0.Line(point1=(28.388957, 39.500612), point2=(28.368377, 40.294868))
s0.Line(point1=(28.368377, 40.294868), point2=(29.268377, 40.594868))
s0.Line(point1=(29.268377, 40.594868), point2=(29.311043, 40.899388))
s0.Line(point1=(29.311043, 40.899388), point2=(30.861043, 40.749388))
s0.Line(point1=(30.638957, 40.550612), point2=(30.594530, 40.133205))
s0.Line(point1=(30.594530, 40.133205), point2=(29.805573, 39.632593))
s0.Line(point1=(29.805573, 39.632593), point2=(28.611043, 39.699388))
s0.Line(point1=(28.611043, 39.699388), point2=(28.631623, 40.105132))
s0.Line(point1=(28.631623, 40.105132), point2=(29.531623, 40.405132))
s0.Line(point1=(29.531623, 40.405132), point2=(29.488957, 40.700612))
s0.Line(point1=(29.488957, 40.700612), point2=(30.638957, 40.550612))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(31.800000, 1.950000), point2=(31.650000, 1.350000))
s0.Line(point1=(31.650000, 1.350000), point2=(31.050000, 1.350000))
s0.Line(point1=(31.050000, 1.350000), point2=(31.050000, 1.050000))
s0.Line(point1=(31.050000, 1.050000), point2=(30.000000, 0.900000))
s0.Line(point1=(30.000000, 0.900000), point2=(29.850000, 0.600000))
s0.Line(point1=(29.850000, 0.600000), point2=(29.100000, 0.600000))
s0.Line(point1=(29.100000, 0.600000), point2=(28.950000, 1.050000))
s0.Line(point1=(28.950000, 1.050000), point2=(28.500000, 1.200000))
s0.Line(point1=(28.500000, 1.200000), point2=(29.100000, 2.850000))
s0.Line(point1=(29.100000, 2.850000), point2=(29.700000, 2.850000))
s0.Line(point1=(29.700000, 2.850000), point2=(30.150000, 2.250000))
s0.Line(point1=(30.150000, 2.250000), point2=(30.900000, 1.950000))
s0.Line(point1=(30.900000, 1.950000), point2=(31.800000, 1.950000))
s0.Line(point1=(31.897014, 2.025746), point2=(31.747014, 1.225746))
s0.Line(point1=(31.747014, 1.225746), point2=(31.150000, 1.250000))
s0.Line(point1=(31.150000, 1.250000), point2=(31.164142, 0.951005))
s0.Line(point1=(31.164142, 0.951005), point2=(30.103585, 0.756284))
s0.Line(point1=(30.103585, 0.756284), point2=(29.939443, 0.455279))
s0.Line(point1=(29.939443, 0.455279), point2=(29.005132, 0.468377))
s0.Line(point1=(29.005132, 0.468377), point2=(28.823509, 0.923509))
s0.Line(point1=(28.823509, 0.923509), point2=(28.374398, 1.139306))
s0.Line(point1=(28.374398, 1.139306), point2=(29.006021, 2.984174))
s0.Line(point1=(29.006021, 2.984174), point2=(29.780000, 3.010000))
s0.Line(point1=(29.780000, 3.010000), point2=(30.267139, 2.402848))
s0.Line(point1=(30.267139, 2.402848), point2=(30.937139, 2.142848))
s0.Line(point1=(30.937139, 2.142848), point2=(31.897014, 2.025746))
s0.Line(point1=(31.702986, 1.874254), point2=(31.552986, 1.474254))
s0.Line(point1=(31.552986, 1.474254), point2=(30.950000, 1.450000))
s0.Line(point1=(30.950000, 1.450000), point2=(30.935858, 1.148995))
s0.Line(point1=(30.935858, 1.148995), point2=(29.896415, 1.043716))
s0.Line(point1=(29.896415, 1.043716), point2=(29.760557, 0.744721))
s0.Line(point1=(29.760557, 0.744721), point2=(29.194868, 0.731623))
s0.Line(point1=(29.194868, 0.731623), point2=(29.076491, 1.176491))
s0.Line(point1=(29.076491, 1.176491), point2=(28.625602, 1.260694))
s0.Line(point1=(28.625602, 1.260694), point2=(29.193979, 2.715826))
s0.Line(point1=(29.193979, 2.715826), point2=(29.620000, 2.690000))
s0.Line(point1=(29.620000, 2.690000), point2=(30.032861, 2.097152))
s0.Line(point1=(30.032861, 2.097152), point2=(30.862861, 1.757152))
s0.Line(point1=(30.862861, 1.757152), point2=(31.702986, 1.874254))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(33.300000, 43.800000), point2=(33.300000, 43.200000))
s0.Line(point1=(33.300000, 43.200000), point2=(28.800000, 40.950000))
s0.Line(point1=(28.800000, 40.950000), point2=(29.250000, 43.650000))
s0.Line(point1=(29.250000, 43.650000), point2=(29.700000, 44.400000))
s0.Line(point1=(29.700000, 44.400000), point2=(31.350000, 44.400000))
s0.Line(point1=(31.350000, 44.400000), point2=(33.300000, 43.800000))
s0.Line(point1=(33.429409, 43.895578), point2=(33.444721, 43.110557))
s0.Line(point1=(33.444721, 43.110557), point2=(28.746082, 40.876997))
s0.Line(point1=(28.746082, 40.876997), point2=(29.065611, 43.717889))
s0.Line(point1=(29.065611, 43.717889), point2=(29.614251, 44.551450))
s0.Line(point1=(29.614251, 44.551450), point2=(31.379409, 44.595578))
s0.Line(point1=(31.379409, 44.595578), point2=(33.429409, 43.895578))
s0.Line(point1=(33.170591, 43.704422), point2=(33.155279, 43.289443))
s0.Line(point1=(33.155279, 43.289443), point2=(28.853918, 41.023003))
s0.Line(point1=(28.853918, 41.023003), point2=(29.434389, 43.582111))
s0.Line(point1=(29.434389, 43.582111), point2=(29.785749, 44.248550))
s0.Line(point1=(29.785749, 44.248550), point2=(31.320591, 44.204422))
s0.Line(point1=(31.320591, 44.204422), point2=(33.170591, 43.704422))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(32.250000, 39.600000), point2=(33.150000, 37.650000))
s0.Line(point1=(33.150000, 37.650000), point2=(34.950000, 35.700000))
s0.Line(point1=(34.950000, 35.700000), point2=(35.100000, 34.650000))
s0.Line(point1=(35.100000, 34.650000), point2=(34.650000, 34.050000))
s0.Line(point1=(34.650000, 34.050000), point2=(32.700000, 34.050000))
s0.Line(point1=(32.700000, 34.050000), point2=(32.550000, 33.450000))
s0.Line(point1=(32.550000, 33.450000), point2=(30.900000, 32.100000))
s0.Line(point1=(30.900000, 32.100000), point2=(30.150000, 33.450000))
s0.Line(point1=(30.150000, 33.450000), point2=(29.100000, 37.200000))
s0.Line(point1=(29.100000, 37.200000), point2=(31.350000, 38.850000))
s0.Line(point1=(31.350000, 38.850000), point2=(31.500000, 39.600000))
s0.Line(point1=(31.500000, 39.600000), point2=(32.250000, 39.600000))
s0.Line(point1=(32.340796, 39.741906), point2=(33.314276, 37.759734))
s0.Line(point1=(33.314276, 37.759734), point2=(35.122475, 35.781970))
s0.Line(point1=(35.122475, 35.781970), point2=(35.278995, 34.604142))
s0.Line(point1=(35.278995, 34.604142), point2=(34.730000, 33.890000))
s0.Line(point1=(34.730000, 33.890000), point2=(32.797014, 33.925746))
s0.Line(point1=(32.797014, 33.925746), point2=(32.710338, 33.348351))
s0.Line(point1=(32.710338, 33.348351), point2=(30.875908, 31.974040))
s0.Line(point1=(30.875908, 31.974040), point2=(29.966288, 33.374473))
s0.Line(point1=(29.966288, 33.374473), point2=(28.944567, 37.253678))
s0.Line(point1=(28.944567, 37.253678), point2=(31.192806, 38.950252))
s0.Line(point1=(31.192806, 38.950252), point2=(31.401942, 39.719612))
s0.Line(point1=(31.401942, 39.719612), point2=(32.340796, 39.741906))
s0.Line(point1=(32.159204, 39.458094), point2=(32.985724, 37.540266))
s0.Line(point1=(32.985724, 37.540266), point2=(34.777525, 35.618030))
s0.Line(point1=(34.777525, 35.618030), point2=(34.921005, 34.695858))
s0.Line(point1=(34.921005, 34.695858), point2=(34.570000, 34.210000))
s0.Line(point1=(34.570000, 34.210000), point2=(32.602986, 34.174254))
s0.Line(point1=(32.602986, 34.174254), point2=(32.389662, 33.551649))
s0.Line(point1=(32.389662, 33.551649), point2=(30.924092, 32.225960))
s0.Line(point1=(30.924092, 32.225960), point2=(30.333712, 33.525527))
s0.Line(point1=(30.333712, 33.525527), point2=(29.255433, 37.146322))
s0.Line(point1=(29.255433, 37.146322), point2=(31.507194, 38.749748))
s0.Line(point1=(31.507194, 38.749748), point2=(31.598058, 39.480388))
s0.Line(point1=(31.598058, 39.480388), point2=(32.159204, 39.458094))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(29.100000, 19.500000), point2=(30.150000, 19.350000))
s0.Line(point1=(30.150000, 19.350000), point2=(30.150000, 17.250000))
s0.Line(point1=(30.150000, 17.250000), point2=(29.700000, 17.400000))
s0.Line(point1=(29.700000, 17.400000), point2=(29.400000, 18.000000))
s0.Line(point1=(29.400000, 18.000000), point2=(29.100000, 19.500000))
s0.Line(point1=(29.016084, 19.579383), point2=(30.264142, 19.448995))
s0.Line(point1=(30.264142, 19.448995), point2=(30.218377, 17.155132))
s0.Line(point1=(30.218377, 17.155132), point2=(29.578935, 17.260410))
s0.Line(point1=(29.578935, 17.260410), point2=(29.212499, 17.935667))
s0.Line(point1=(29.212499, 17.935667), point2=(29.016084, 19.579383))
s0.Line(point1=(29.183916, 19.420617), point2=(30.035858, 19.251005))
s0.Line(point1=(30.035858, 19.251005), point2=(30.081623, 17.344868))
s0.Line(point1=(30.081623, 17.344868), point2=(29.821065, 17.539590))
s0.Line(point1=(29.821065, 17.539590), point2=(29.587501, 18.064333))
s0.Line(point1=(29.587501, 18.064333), point2=(29.183916, 19.420617))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(29.400000, 5.100000), point2=(29.850000, 5.700000))
s0.Line(point1=(29.850000, 5.700000), point2=(31.950000, 5.700000))
s0.Line(point1=(31.950000, 5.700000), point2=(32.400000, 4.200000))
s0.Line(point1=(32.400000, 4.200000), point2=(31.650000, 3.450000))
s0.Line(point1=(31.650000, 3.450000), point2=(30.300000, 3.150000))
s0.Line(point1=(30.300000, 3.150000), point2=(29.550000, 4.050000))
s0.Line(point1=(29.550000, 4.050000), point2=(29.400000, 5.100000))
s0.Line(point1=(29.221005, 5.145858), point2=(29.770000, 5.860000))
s0.Line(point1=(29.770000, 5.860000), point2=(32.045783, 5.828735))
s0.Line(point1=(32.045783, 5.828735), point2=(32.566493, 4.158024))
s0.Line(point1=(32.566493, 4.158024), point2=(31.742404, 3.281671))
s0.Line(point1=(31.742404, 3.281671), point2=(30.244871, 2.988363))
s0.Line(point1=(30.244871, 2.988363), point2=(29.374183, 3.971839))
s0.Line(point1=(29.374183, 3.971839), point2=(29.221005, 5.145858))
s0.Line(point1=(29.578995, 5.054142), point2=(29.930000, 5.540000))
s0.Line(point1=(29.930000, 5.540000), point2=(31.854217, 5.571265))
s0.Line(point1=(31.854217, 5.571265), point2=(32.233507, 4.241976))
s0.Line(point1=(32.233507, 4.241976), point2=(31.557596, 3.618329))
s0.Line(point1=(31.557596, 3.618329), point2=(30.355129, 3.311637))
s0.Line(point1=(30.355129, 3.311637), point2=(29.725817, 4.128161))
s0.Line(point1=(29.725817, 4.128161), point2=(29.578995, 5.054142))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(30.150000, 47.100000), point2=(31.800000, 46.800000))
s0.Line(point1=(31.800000, 46.800000), point2=(32.850000, 45.450000))
s0.Line(point1=(32.850000, 45.450000), point2=(32.850000, 44.700000))
s0.Line(point1=(32.850000, 44.700000), point2=(31.650000, 44.850000))
s0.Line(point1=(31.650000, 44.850000), point2=(30.900000, 45.450000))
s0.Line(point1=(30.900000, 45.450000), point2=(30.150000, 47.100000))
s0.Line(point1=(30.076852, 47.157007), point2=(31.896824, 46.959781))
s0.Line(point1=(31.896824, 46.959781), point2=(33.028935, 45.511394))
s0.Line(point1=(33.028935, 45.511394), point2=(32.937597, 44.600772))
s0.Line(point1=(32.937597, 44.600772), point2=(31.575127, 44.672685))
s0.Line(point1=(31.575127, 44.672685), point2=(30.746494, 45.330533))
s0.Line(point1=(30.746494, 45.330533), point2=(30.076852, 47.157007))
s0.Line(point1=(30.223148, 47.042993), point2=(31.703176, 46.640219))
s0.Line(point1=(31.703176, 46.640219), point2=(32.671065, 45.388606))
s0.Line(point1=(32.671065, 45.388606), point2=(32.762403, 44.799228))
s0.Line(point1=(32.762403, 44.799228), point2=(31.724873, 45.027315))
s0.Line(point1=(31.724873, 45.027315), point2=(31.053506, 45.569467))
s0.Line(point1=(31.053506, 45.569467), point2=(30.223148, 47.042993))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(31.950000, 19.200000), point2=(31.950000, 18.600000))
s0.Line(point1=(31.950000, 18.600000), point2=(31.350000, 18.150000))
s0.Line(point1=(31.350000, 18.150000), point2=(30.600000, 18.600000))
s0.Line(point1=(30.600000, 18.600000), point2=(31.050000, 19.500000))
s0.Line(point1=(31.050000, 19.500000), point2=(31.950000, 19.200000))
s0.Line(point1=(32.081623, 19.294868), point2=(32.110000, 18.520000))
s0.Line(point1=(32.110000, 18.520000), point2=(31.358550, 17.984251))
s0.Line(point1=(31.358550, 17.984251), point2=(30.459108, 18.558972))
s0.Line(point1=(30.459108, 18.558972), point2=(30.992180, 19.639590))
s0.Line(point1=(30.992180, 19.639590), point2=(32.081623, 19.294868))
s0.Line(point1=(31.818377, 19.105132), point2=(31.790000, 18.680000))
s0.Line(point1=(31.790000, 18.680000), point2=(31.341450, 18.315749))
s0.Line(point1=(31.341450, 18.315749), point2=(30.740892, 18.641028))
s0.Line(point1=(30.740892, 18.641028), point2=(31.107820, 19.360410))
s0.Line(point1=(31.107820, 19.360410), point2=(31.818377, 19.105132))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(36.450000, 5.100000), point2=(36.450000, 3.450000))
s0.Line(point1=(36.450000, 3.450000), point2=(36.000000, 3.450000))
s0.Line(point1=(36.000000, 3.450000), point2=(35.700000, 2.700000))
s0.Line(point1=(35.700000, 2.700000), point2=(35.250000, 1.350000))
s0.Line(point1=(35.250000, 1.350000), point2=(35.250000, 0.000000))
s0.Line(point1=(35.250000, 0.000000), point2=(31.350000, 0.000000))
s0.Line(point1=(31.350000, 0.000000), point2=(31.650000, 0.900000))
s0.Line(point1=(31.650000, 0.900000), point2=(33.750000, 2.100000))
s0.Line(point1=(33.750000, 2.100000), point2=(34.800000, 3.900000))
s0.Line(point1=(34.800000, 3.900000), point2=(35.250000, 4.050000))
s0.Line(point1=(35.250000, 4.050000), point2=(36.000000, 5.100000))
s0.Line(point1=(36.000000, 5.100000), point2=(36.450000, 5.100000))
s0.Line(point1=(36.550000, 5.200000), point2=(36.550000, 3.350000))
s0.Line(point1=(36.550000, 3.350000), point2=(36.092848, 3.312861))
s0.Line(point1=(36.092848, 3.312861), point2=(35.887716, 2.631238))
s0.Line(point1=(35.887716, 2.631238), point2=(35.444868, 1.318377))
s0.Line(point1=(35.444868, 1.318377), point2=(35.350000, 0.000000))
s0.Line(point1=(35.350000, 0.000000), point2=(31.255132, 0.000000))
s0.Line(point1=(31.255132, 0.000000), point2=(31.505518, 1.018447))
s0.Line(point1=(31.505518, 1.018447), point2=(33.614008, 2.237211))
s0.Line(point1=(33.614008, 2.237211), point2=(34.681999, 4.045255))
s0.Line(point1=(34.681999, 4.045255), point2=(35.137004, 4.202992))
s0.Line(point1=(35.137004, 4.202992), point2=(35.918627, 5.258124))
s0.Line(point1=(35.918627, 5.258124), point2=(36.550000, 5.200000))
s0.Line(point1=(36.350000, 5.000000), point2=(36.350000, 3.550000))
s0.Line(point1=(36.350000, 3.550000), point2=(35.907152, 3.587139))
s0.Line(point1=(35.907152, 3.587139), point2=(35.512284, 2.768762))
s0.Line(point1=(35.512284, 2.768762), point2=(35.055132, 1.381623))
s0.Line(point1=(35.055132, 1.381623), point2=(35.150000, 0.000000))
s0.Line(point1=(35.150000, 0.000000), point2=(31.444868, 0.000000))
s0.Line(point1=(31.444868, 0.000000), point2=(31.794482, 0.781553))
s0.Line(point1=(31.794482, 0.781553), point2=(33.885992, 1.962789))
s0.Line(point1=(33.885992, 1.962789), point2=(34.918001, 3.754745))
s0.Line(point1=(34.918001, 3.754745), point2=(35.362996, 3.897008))
s0.Line(point1=(35.362996, 3.897008), point2=(36.081373, 4.941876))
s0.Line(point1=(36.081373, 4.941876), point2=(36.350000, 5.000000))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(31.800000, 22.650000), point2=(32.550000, 22.500000))
s0.Line(point1=(32.550000, 22.500000), point2=(34.050000, 19.800000))
s0.Line(point1=(34.050000, 19.800000), point2=(34.350000, 18.600000))
s0.Line(point1=(34.350000, 18.600000), point2=(33.150000, 18.600000))
s0.Line(point1=(33.150000, 18.600000), point2=(32.400000, 19.500000))
s0.Line(point1=(32.400000, 19.500000), point2=(31.800000, 21.150000))
s0.Line(point1=(31.800000, 21.150000), point2=(31.800000, 22.650000))
s0.Line(point1=(31.719612, 22.748058), point2=(32.657027, 22.646622))
s0.Line(point1=(32.657027, 22.646622), point2=(34.234430, 19.872818))
s0.Line(point1=(34.234430, 19.872818), point2=(34.447014, 18.524254))
s0.Line(point1=(34.447014, 18.524254), point2=(33.073178, 18.435982))
s0.Line(point1=(33.073178, 18.435982), point2=(32.229199, 19.401807))
s0.Line(point1=(32.229199, 19.401807), point2=(31.606021, 21.115826))
s0.Line(point1=(31.606021, 21.115826), point2=(31.719612, 22.748058))
s0.Line(point1=(31.880388, 22.551942), point2=(32.442973, 22.353378))
s0.Line(point1=(32.442973, 22.353378), point2=(33.865570, 19.727182))
s0.Line(point1=(33.865570, 19.727182), point2=(34.252986, 18.675746))
s0.Line(point1=(34.252986, 18.675746), point2=(33.226822, 18.764018))
s0.Line(point1=(33.226822, 18.764018), point2=(32.570801, 19.598193))
s0.Line(point1=(32.570801, 19.598193), point2=(31.993979, 21.184174))
s0.Line(point1=(31.993979, 21.184174), point2=(31.880388, 22.551942))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(33.900000, 16.650000), point2=(33.150000, 15.450000))
s0.Line(point1=(33.150000, 15.450000), point2=(32.400000, 15.450000))
s0.Line(point1=(32.400000, 15.450000), point2=(31.950000, 15.900000))
s0.Line(point1=(31.950000, 15.900000), point2=(31.950000, 16.350000))
s0.Line(point1=(31.950000, 16.350000), point2=(32.400000, 16.650000))
s0.Line(point1=(32.400000, 16.650000), point2=(33.900000, 16.650000))
s0.Line(point1=(33.984800, 16.697000), point2=(33.234800, 15.297000))
s0.Line(point1=(33.234800, 15.297000), point2=(32.329289, 15.279289))
s0.Line(point1=(32.329289, 15.279289), point2=(31.779289, 15.829289))
s0.Line(point1=(31.779289, 15.829289), point2=(31.794530, 16.433205))
s0.Line(point1=(31.794530, 16.433205), point2=(32.344530, 16.833205))
s0.Line(point1=(32.344530, 16.833205), point2=(33.984800, 16.697000))
s0.Line(point1=(33.815200, 16.603000), point2=(33.065200, 15.603000))
s0.Line(point1=(33.065200, 15.603000), point2=(32.470711, 15.620711))
s0.Line(point1=(32.470711, 15.620711), point2=(32.120711, 15.970711))
s0.Line(point1=(32.120711, 15.970711), point2=(32.105470, 16.266795))
s0.Line(point1=(32.105470, 16.266795), point2=(32.455470, 16.466795))
s0.Line(point1=(32.455470, 16.466795), point2=(33.815200, 16.603000))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(34.950000, 9.600000), point2=(35.100000, 8.100000))
s0.Line(point1=(35.100000, 8.100000), point2=(34.500000, 7.350000))
s0.Line(point1=(34.500000, 7.350000), point2=(34.350000, 5.400000))
s0.Line(point1=(34.350000, 5.400000), point2=(33.900000, 4.200000))
s0.Line(point1=(33.900000, 4.200000), point2=(33.450000, 4.200000))
s0.Line(point1=(33.450000, 4.200000), point2=(33.450000, 6.150000))
s0.Line(point1=(33.450000, 6.150000), point2=(33.000000, 6.150000))
s0.Line(point1=(33.000000, 6.150000), point2=(32.850000, 6.750000))
s0.Line(point1=(32.850000, 6.750000), point2=(31.950000, 7.350000))
s0.Line(point1=(31.950000, 7.350000), point2=(31.950000, 8.100000))
s0.Line(point1=(31.950000, 8.100000), point2=(34.950000, 9.600000))
s0.Line(point1=(35.004782, 9.699393), point2=(35.277591, 8.047481))
s0.Line(point1=(35.277591, 8.047481), point2=(34.677792, 7.279861))
s0.Line(point1=(34.677792, 7.279861), point2=(34.543338, 5.357218))
s0.Line(point1=(34.543338, 5.357218), point2=(33.993633, 4.064888))
s0.Line(point1=(33.993633, 4.064888), point2=(33.350000, 4.100000))
s0.Line(point1=(33.350000, 4.100000), point2=(33.350000, 6.050000))
s0.Line(point1=(33.350000, 6.050000), point2=(32.902986, 6.025746))
s0.Line(point1=(32.902986, 6.025746), point2=(32.697516, 6.642541))
s0.Line(point1=(32.697516, 6.642541), point2=(31.794530, 7.266795))
s0.Line(point1=(31.794530, 7.266795), point2=(31.805279, 8.189443))
s0.Line(point1=(31.805279, 8.189443), point2=(35.004782, 9.699393))
s0.Line(point1=(34.895218, 9.500607), point2=(34.922409, 8.152519))
s0.Line(point1=(34.922409, 8.152519), point2=(34.322208, 7.420139))
s0.Line(point1=(34.322208, 7.420139), point2=(34.156662, 5.442782))
s0.Line(point1=(34.156662, 5.442782), point2=(33.806367, 4.335112))
s0.Line(point1=(33.806367, 4.335112), point2=(33.550000, 4.300000))
s0.Line(point1=(33.550000, 4.300000), point2=(33.550000, 6.250000))
s0.Line(point1=(33.550000, 6.250000), point2=(33.097014, 6.274254))
s0.Line(point1=(33.097014, 6.274254), point2=(33.002484, 6.857459))
s0.Line(point1=(33.002484, 6.857459), point2=(32.105470, 7.433205))
s0.Line(point1=(32.105470, 7.433205), point2=(32.094721, 8.010557))
s0.Line(point1=(32.094721, 8.010557), point2=(34.895218, 9.500607))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(32.250000, 52.050000), point2=(32.850000, 51.750000))
s0.Line(point1=(32.850000, 51.750000), point2=(33.450000, 52.050000))
s0.Line(point1=(33.450000, 52.050000), point2=(33.900000, 51.150000))
s0.Line(point1=(33.900000, 51.150000), point2=(34.800000, 50.700000))
s0.Line(point1=(34.800000, 50.700000), point2=(36.000000, 48.600000))
s0.Line(point1=(36.000000, 48.600000), point2=(35.250000, 48.750000))
s0.Line(point1=(35.250000, 48.750000), point2=(33.900000, 49.500000))
s0.Line(point1=(33.900000, 49.500000), point2=(33.450000, 50.250000))
s0.Line(point1=(33.450000, 50.250000), point2=(33.000000, 50.250000))
s0.Line(point1=(33.000000, 50.250000), point2=(32.850000, 50.700000))
s0.Line(point1=(32.850000, 50.700000), point2=(32.100000, 51.150000))
s0.Line(point1=(32.100000, 51.150000), point2=(32.250000, 52.050000))
s0.Line(point1=(32.196082, 52.155883), point2=(32.850000, 51.928885))
s0.Line(point1=(32.850000, 51.928885), point2=(33.494721, 52.184164))
s0.Line(point1=(33.494721, 52.184164), point2=(34.034164, 51.284164))
s0.Line(point1=(34.034164, 51.284164), point2=(34.931546, 50.839057))
s0.Line(point1=(34.931546, 50.839057), point2=(36.067213, 48.551556))
s0.Line(point1=(36.067213, 48.551556), point2=(35.181824, 48.564526))
s0.Line(point1=(35.181824, 48.564526), point2=(33.765686, 49.361135))
s0.Line(point1=(33.765686, 49.361135), point2=(33.364251, 50.098550))
s0.Line(point1=(33.364251, 50.098550), point2=(32.905132, 50.118377))
s0.Line(point1=(32.905132, 50.118377), point2=(32.703682, 50.582628))
s0.Line(point1=(32.703682, 50.582628), point2=(31.949911, 51.080691))
s0.Line(point1=(31.949911, 51.080691), point2=(32.196082, 52.155883))
s0.Line(point1=(32.303918, 51.944117), point2=(32.850000, 51.571115))
s0.Line(point1=(32.850000, 51.571115), point2=(33.405279, 51.915836))
s0.Line(point1=(33.405279, 51.915836), point2=(33.765836, 51.015836))
s0.Line(point1=(33.765836, 51.015836), point2=(34.668454, 50.560943))
s0.Line(point1=(34.668454, 50.560943), point2=(35.932787, 48.648444))
s0.Line(point1=(35.932787, 48.648444), point2=(35.318176, 48.935474))
s0.Line(point1=(35.318176, 48.935474), point2=(34.034314, 49.638865))
s0.Line(point1=(34.034314, 49.638865), point2=(33.535749, 50.401450))
s0.Line(point1=(33.535749, 50.401450), point2=(33.094868, 50.381623))
s0.Line(point1=(33.094868, 50.381623), point2=(32.996318, 50.817372))
s0.Line(point1=(32.996318, 50.817372), point2=(32.250089, 51.219309))
s0.Line(point1=(32.250089, 51.219309), point2=(32.303918, 51.944117))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
print 100
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(33.300000, 14.700000), point2=(34.500000, 13.950000))
s0.Line(point1=(34.500000, 13.950000), point2=(34.350000, 12.600000))
s0.Line(point1=(34.350000, 12.600000), point2=(33.900000, 12.150000))
s0.Line(point1=(33.900000, 12.150000), point2=(33.300000, 12.150000))
s0.Line(point1=(33.300000, 12.150000), point2=(32.400000, 12.750000))
s0.Line(point1=(32.400000, 12.750000), point2=(33.300000, 14.700000))
s0.Line(point1=(33.262204, 14.826706), point2=(34.652388, 14.023757))
s0.Line(point1=(34.652388, 14.023757), point2=(34.520099, 12.518246))
s0.Line(point1=(34.520099, 12.518246), point2=(33.970711, 11.979289))
s0.Line(point1=(33.970711, 11.979289), point2=(33.244530, 11.966795))
s0.Line(point1=(33.244530, 11.966795), point2=(32.253734, 12.708701))
s0.Line(point1=(32.253734, 12.708701), point2=(33.262204, 14.826706))
s0.Line(point1=(33.337796, 14.573294), point2=(34.347612, 13.876243))
s0.Line(point1=(34.347612, 13.876243), point2=(34.179901, 12.681754))
s0.Line(point1=(34.179901, 12.681754), point2=(33.829289, 12.320711))
s0.Line(point1=(33.829289, 12.320711), point2=(33.355470, 12.333205))
s0.Line(point1=(33.355470, 12.333205), point2=(32.546266, 12.791299))
s0.Line(point1=(32.546266, 12.791299), point2=(33.337796, 14.573294))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(35.100000, 15.000000), point2=(36.000000, 15.000000))
s0.Line(point1=(36.000000, 15.000000), point2=(36.150000, 14.700000))
s0.Line(point1=(36.150000, 14.700000), point2=(36.300000, 12.450000))
s0.Line(point1=(36.300000, 12.450000), point2=(37.200000, 10.350000))
s0.Line(point1=(37.200000, 10.350000), point2=(37.200000, 9.600000))
s0.Line(point1=(37.200000, 9.600000), point2=(35.550000, 9.450000))
s0.Line(point1=(35.550000, 9.450000), point2=(35.100000, 9.900000))
s0.Line(point1=(35.100000, 9.900000), point2=(33.900000, 10.050000))
s0.Line(point1=(33.900000, 10.050000), point2=(33.900000, 10.350000))
s0.Line(point1=(33.900000, 10.350000), point2=(32.550000, 10.350000))
s0.Line(point1=(32.550000, 10.350000), point2=(32.550000, 10.800000))
s0.Line(point1=(32.550000, 10.800000), point2=(34.050000, 11.250000))
s0.Line(point1=(34.050000, 11.250000), point2=(33.900000, 12.000000))
s0.Line(point1=(33.900000, 12.000000), point2=(34.350000, 12.150000))
s0.Line(point1=(34.350000, 12.150000), point2=(34.500000, 13.050000))
s0.Line(point1=(34.500000, 13.050000), point2=(35.100000, 13.800000))
s0.Line(point1=(35.100000, 13.800000), point2=(35.100000, 15.000000))
s0.Line(point1=(35.000000, 15.100000), point2=(36.089443, 15.144721))
s0.Line(point1=(36.089443, 15.144721), point2=(36.339221, 14.751373))
s0.Line(point1=(36.339221, 14.751373), point2=(36.491693, 12.496044))
s0.Line(point1=(36.491693, 12.496044), point2=(37.391915, 10.389392))
s0.Line(point1=(37.391915, 10.389392), point2=(37.309054, 9.500411))
s0.Line(point1=(37.309054, 9.500411), point2=(35.488343, 9.279700))
s0.Line(point1=(35.488343, 9.279700), point2=(35.016886, 9.730062))
s0.Line(point1=(35.016886, 9.730062), point2=(33.787597, 9.950772))
s0.Line(point1=(33.787597, 9.950772), point2=(33.800000, 10.250000))
s0.Line(point1=(33.800000, 10.250000), point2=(32.450000, 10.250000))
s0.Line(point1=(32.450000, 10.250000), point2=(32.421265, 10.895783))
s0.Line(point1=(32.421265, 10.895783), point2=(33.923207, 11.326171))
s0.Line(point1=(33.923207, 11.326171), point2=(33.770319, 12.075257))
s0.Line(point1=(33.770319, 12.075257), point2=(34.219738, 12.261308))
s0.Line(point1=(34.219738, 12.261308), point2=(34.323274, 13.128909))
s0.Line(point1=(34.323274, 13.128909), point2=(34.921913, 13.862470))
s0.Line(point1=(34.921913, 13.862470), point2=(35.000000, 15.100000))
s0.Line(point1=(35.200000, 14.900000), point2=(35.910557, 14.855279))
s0.Line(point1=(35.910557, 14.855279), point2=(35.960779, 14.648627))
s0.Line(point1=(35.960779, 14.648627), point2=(36.108307, 12.403956))
s0.Line(point1=(36.108307, 12.403956), point2=(37.008085, 10.310608))
s0.Line(point1=(37.008085, 10.310608), point2=(37.090946, 9.699589))
s0.Line(point1=(37.090946, 9.699589), point2=(35.611657, 9.620300))
s0.Line(point1=(35.611657, 9.620300), point2=(35.183114, 10.069938))
s0.Line(point1=(35.183114, 10.069938), point2=(34.012403, 10.149228))
s0.Line(point1=(34.012403, 10.149228), point2=(34.000000, 10.450000))
s0.Line(point1=(34.000000, 10.450000), point2=(32.650000, 10.450000))
s0.Line(point1=(32.650000, 10.450000), point2=(32.678735, 10.704217))
s0.Line(point1=(32.678735, 10.704217), point2=(34.176793, 11.173829))
s0.Line(point1=(34.176793, 11.173829), point2=(34.029681, 11.924743))
s0.Line(point1=(34.029681, 11.924743), point2=(34.480262, 12.038692))
s0.Line(point1=(34.480262, 12.038692), point2=(34.676726, 12.971091))
s0.Line(point1=(34.676726, 12.971091), point2=(35.278087, 13.737530))
s0.Line(point1=(35.278087, 13.737530), point2=(35.200000, 14.900000))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(33.300000, 47.700000), point2=(33.750000, 47.700000))
s0.Line(point1=(33.750000, 47.700000), point2=(34.200000, 46.800000))
s0.Line(point1=(34.200000, 46.800000), point2=(34.200000, 46.050000))
s0.Line(point1=(34.200000, 46.050000), point2=(33.750000, 45.750000))
s0.Line(point1=(33.750000, 45.750000), point2=(33.150000, 46.500000))
s0.Line(point1=(33.150000, 46.500000), point2=(33.300000, 47.700000))
s0.Line(point1=(33.200772, 47.812403), point2=(33.839443, 47.844721))
s0.Line(point1=(33.839443, 47.844721), point2=(34.389443, 46.844721))
s0.Line(point1=(34.389443, 46.844721), point2=(34.355470, 45.966795))
s0.Line(point1=(34.355470, 45.966795), point2=(33.727383, 45.604325))
s0.Line(point1=(33.727383, 45.604325), point2=(32.972685, 46.449934))
s0.Line(point1=(32.972685, 46.449934), point2=(33.200772, 47.812403))
s0.Line(point1=(33.399228, 47.587597), point2=(33.660557, 47.555279))
s0.Line(point1=(33.660557, 47.555279), point2=(34.010557, 46.755279))
s0.Line(point1=(34.010557, 46.755279), point2=(34.044530, 46.133205))
s0.Line(point1=(34.044530, 46.133205), point2=(33.772617, 45.895675))
s0.Line(point1=(33.772617, 45.895675), point2=(33.327315, 46.550066))
s0.Line(point1=(33.327315, 46.550066), point2=(33.399228, 47.587597))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(33.600000, 41.100000), point2=(34.650000, 41.100000))
s0.Line(point1=(34.650000, 41.100000), point2=(36.750000, 40.050000))
s0.Line(point1=(36.750000, 40.050000), point2=(37.050000, 40.200000))
s0.Line(point1=(37.050000, 40.200000), point2=(37.050000, 40.800000))
s0.Line(point1=(37.050000, 40.800000), point2=(37.650000, 40.950000))
s0.Line(point1=(37.650000, 40.950000), point2=(37.800000, 40.350000))
s0.Line(point1=(37.800000, 40.350000), point2=(38.250000, 40.200000))
s0.Line(point1=(38.250000, 40.200000), point2=(37.800000, 37.950000))
s0.Line(point1=(37.800000, 37.950000), point2=(37.200000, 37.950000))
s0.Line(point1=(37.200000, 37.950000), point2=(35.100000, 39.750000))
s0.Line(point1=(35.100000, 39.750000), point2=(33.300000, 39.750000))
s0.Line(point1=(33.300000, 39.750000), point2=(33.600000, 41.100000))
s0.Line(point1=(33.502381, 41.221693), point2=(34.694721, 41.289443))
s0.Line(point1=(34.694721, 41.289443), point2=(36.750000, 40.228885))
s0.Line(point1=(36.750000, 40.228885), point2=(36.905279, 40.289443))
s0.Line(point1=(36.905279, 40.289443), point2=(36.925746, 40.897014))
s0.Line(point1=(36.925746, 40.897014), point2=(37.722761, 41.071268))
s0.Line(point1=(37.722761, 41.071268), point2=(37.928637, 40.469122))
s0.Line(point1=(37.928637, 40.469122), point2=(38.379681, 40.275257))
s0.Line(point1=(38.379681, 40.275257), point2=(37.898058, 37.830388))
s0.Line(point1=(37.898058, 37.830388), point2=(37.134921, 37.774074))
s0.Line(point1=(37.134921, 37.774074), point2=(35.034921, 39.574074))
s0.Line(point1=(35.034921, 39.574074), point2=(33.202381, 39.671693))
s0.Line(point1=(33.202381, 39.671693), point2=(33.502381, 41.221693))
s0.Line(point1=(33.697619, 40.978307), point2=(34.605279, 40.910557))
s0.Line(point1=(34.605279, 40.910557), point2=(36.750000, 39.871115))
s0.Line(point1=(36.750000, 39.871115), point2=(37.194721, 40.110557))
s0.Line(point1=(37.194721, 40.110557), point2=(37.174254, 40.702986))
s0.Line(point1=(37.174254, 40.702986), point2=(37.577239, 40.828732))
s0.Line(point1=(37.577239, 40.828732), point2=(37.671363, 40.230878))
s0.Line(point1=(37.671363, 40.230878), point2=(38.120319, 40.124743))
s0.Line(point1=(38.120319, 40.124743), point2=(37.701942, 38.069612))
s0.Line(point1=(37.701942, 38.069612), point2=(37.265079, 38.125926))
s0.Line(point1=(37.265079, 38.125926), point2=(35.165079, 39.925926))
s0.Line(point1=(35.165079, 39.925926), point2=(33.397619, 39.828307))
s0.Line(point1=(33.397619, 39.828307), point2=(33.697619, 40.978307))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(33.450000, 43.350000), point2=(34.500000, 43.950000))
s0.Line(point1=(34.500000, 43.950000), point2=(35.100000, 43.050000))
s0.Line(point1=(35.100000, 43.050000), point2=(34.350000, 42.750000))
s0.Line(point1=(34.350000, 42.750000), point2=(33.450000, 43.350000))
s0.Line(point1=(33.344916, 43.353619), point2=(34.533591, 44.092294))
s0.Line(point1=(34.533591, 44.092294), point2=(35.220344, 43.012622))
s0.Line(point1=(35.220344, 43.012622), point2=(34.331669, 42.573947))
s0.Line(point1=(34.331669, 42.573947), point2=(33.344916, 43.353619))
s0.Line(point1=(33.555084, 43.346381), point2=(34.466409, 43.807706))
s0.Line(point1=(34.466409, 43.807706), point2=(34.979656, 43.087378))
s0.Line(point1=(34.979656, 43.087378), point2=(34.368331, 42.926053))
s0.Line(point1=(34.368331, 42.926053), point2=(33.555084, 43.346381))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(34.950000, 38.400000), point2=(36.150000, 38.100000))
s0.Line(point1=(36.150000, 38.100000), point2=(36.450000, 37.500000))
s0.Line(point1=(36.450000, 37.500000), point2=(36.450000, 36.450000))
s0.Line(point1=(36.450000, 36.450000), point2=(35.700000, 35.550000))
s0.Line(point1=(35.700000, 35.550000), point2=(35.100000, 35.550000))
s0.Line(point1=(35.100000, 35.550000), point2=(34.200000, 37.650000))
s0.Line(point1=(34.200000, 37.650000), point2=(34.350000, 38.100000))
s0.Line(point1=(34.350000, 38.100000), point2=(34.950000, 38.400000))
s0.Line(point1=(34.929532, 38.586457), point2=(36.263696, 38.241736))
s0.Line(point1=(36.263696, 38.241736), point2=(36.639443, 37.544721))
s0.Line(point1=(36.639443, 37.544721), point2=(36.626822, 36.385982))
s0.Line(point1=(36.626822, 36.385982), point2=(35.776822, 35.385982))
s0.Line(point1=(35.776822, 35.385982), point2=(35.008085, 35.410608))
s0.Line(point1=(35.008085, 35.410608), point2=(34.013217, 37.642231))
s0.Line(point1=(34.013217, 37.642231), point2=(34.210410, 38.221065))
s0.Line(point1=(34.210410, 38.221065), point2=(34.929532, 38.586457))
s0.Line(point1=(34.970468, 38.213543), point2=(36.036304, 37.958264))
s0.Line(point1=(36.036304, 37.958264), point2=(36.260557, 37.455279))
s0.Line(point1=(36.260557, 37.455279), point2=(36.273178, 36.514018))
s0.Line(point1=(36.273178, 36.514018), point2=(35.623178, 35.714018))
s0.Line(point1=(35.623178, 35.714018), point2=(35.191915, 35.689392))
s0.Line(point1=(35.191915, 35.689392), point2=(34.386783, 37.657769))
s0.Line(point1=(34.386783, 37.657769), point2=(34.489590, 37.978935))
s0.Line(point1=(34.489590, 37.978935), point2=(34.970468, 38.213543))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(37.350000, 23.700000), point2=(37.950000, 22.950000))
s0.Line(point1=(37.950000, 22.950000), point2=(37.800000, 21.150000))
s0.Line(point1=(37.800000, 21.150000), point2=(37.050000, 20.550000))
s0.Line(point1=(37.050000, 20.550000), point2=(36.600000, 19.650000))
s0.Line(point1=(36.600000, 19.650000), point2=(35.400000, 19.500000))
s0.Line(point1=(35.400000, 19.500000), point2=(34.500000, 20.850000))
s0.Line(point1=(34.500000, 20.850000), point2=(34.500000, 22.350000))
s0.Line(point1=(34.500000, 22.350000), point2=(35.250000, 23.250000))
s0.Line(point1=(35.250000, 23.250000), point2=(36.300000, 23.850000))
s0.Line(point1=(36.300000, 23.850000), point2=(37.350000, 23.700000))
s0.Line(point1=(37.442229, 23.861464), point2=(38.127741, 23.004165))
s0.Line(point1=(38.127741, 23.004165), point2=(37.962124, 21.063609))
s0.Line(point1=(37.962124, 21.063609), point2=(37.201912, 20.427192))
s0.Line(point1=(37.201912, 20.427192), point2=(36.701846, 19.506051))
s0.Line(point1=(36.701846, 19.506051), point2=(35.329198, 19.345302))
s0.Line(point1=(35.329198, 19.345302), point2=(34.316795, 20.794530))
s0.Line(point1=(34.316795, 20.794530), point2=(34.323178, 22.414018))
s0.Line(point1=(34.323178, 22.414018), point2=(35.123564, 23.400843))
s0.Line(point1=(35.123564, 23.400843), point2=(36.264528, 24.035819))
s0.Line(point1=(36.264528, 24.035819), point2=(37.442229, 23.861464))
s0.Line(point1=(37.257771, 23.538536), point2=(37.772259, 22.895835))
s0.Line(point1=(37.772259, 22.895835), point2=(37.637876, 21.236391))
s0.Line(point1=(37.637876, 21.236391), point2=(36.898088, 20.672808))
s0.Line(point1=(36.898088, 20.672808), point2=(36.498154, 19.793949))
s0.Line(point1=(36.498154, 19.793949), point2=(35.470802, 19.654698))
s0.Line(point1=(35.470802, 19.654698), point2=(34.683205, 20.905470))
s0.Line(point1=(34.683205, 20.905470), point2=(34.676822, 22.285982))
s0.Line(point1=(34.676822, 22.285982), point2=(35.376436, 23.099157))
s0.Line(point1=(35.376436, 23.099157), point2=(36.335472, 23.664181))
s0.Line(point1=(36.335472, 23.664181), point2=(37.257771, 23.538536))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(34.800000, 33.450000), point2=(36.300000, 33.900000))
s0.Line(point1=(36.300000, 33.900000), point2=(36.600000, 32.550000))
s0.Line(point1=(36.600000, 32.550000), point2=(34.950000, 32.550000))
s0.Line(point1=(34.950000, 32.550000), point2=(34.800000, 33.450000))
s0.Line(point1=(34.672626, 33.529343), point2=(36.368884, 34.017476))
s0.Line(point1=(36.368884, 34.017476), point2=(36.697619, 32.471693))
s0.Line(point1=(36.697619, 32.471693), point2=(34.851361, 32.433560))
s0.Line(point1=(34.851361, 32.433560), point2=(34.672626, 33.529343))
s0.Line(point1=(34.927374, 33.370657), point2=(36.231116, 33.782524))
s0.Line(point1=(36.231116, 33.782524), point2=(36.502381, 32.628307))
s0.Line(point1=(36.502381, 32.628307), point2=(35.048639, 32.666440))
s0.Line(point1=(35.048639, 32.666440), point2=(34.927374, 33.370657))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(35.250000, 46.650000), point2=(37.050000, 46.800000))
s0.Line(point1=(37.050000, 46.800000), point2=(38.550000, 45.750000))
s0.Line(point1=(38.550000, 45.750000), point2=(39.450000, 45.750000))
s0.Line(point1=(39.450000, 45.750000), point2=(39.750000, 45.150000))
s0.Line(point1=(39.750000, 45.150000), point2=(39.600000, 43.800000))
s0.Line(point1=(39.600000, 43.800000), point2=(39.000000, 43.800000))
s0.Line(point1=(39.000000, 43.800000), point2=(38.400000, 44.550000))
s0.Line(point1=(38.400000, 44.550000), point2=(36.900000, 45.450000))
s0.Line(point1=(36.900000, 45.450000), point2=(35.250000, 45.900000))
s0.Line(point1=(35.250000, 45.900000), point2=(35.250000, 46.650000))
s0.Line(point1=(35.141695, 46.749655), point2=(37.099042, 46.981578))
s0.Line(point1=(37.099042, 46.981578), point2=(38.607346, 45.931923))
s0.Line(point1=(38.607346, 45.931923), point2=(39.539443, 45.894721))
s0.Line(point1=(39.539443, 45.894721), point2=(39.938831, 45.183678))
s0.Line(point1=(39.938831, 45.183678), point2=(39.699388, 43.688957))
s0.Line(point1=(39.699388, 43.688957), point2=(38.921913, 43.637530))
s0.Line(point1=(38.921913, 43.637530), point2=(38.270464, 44.401781))
s0.Line(point1=(38.270464, 44.401781), point2=(36.822239, 45.267774))
s0.Line(point1=(36.822239, 45.267774), point2=(35.123688, 45.803524))
s0.Line(point1=(35.123688, 45.803524), point2=(35.141695, 46.749655))
s0.Line(point1=(35.358305, 46.550345), point2=(37.000958, 46.618422))
s0.Line(point1=(37.000958, 46.618422), point2=(38.492654, 45.568077))
s0.Line(point1=(38.492654, 45.568077), point2=(39.360557, 45.605279))
s0.Line(point1=(39.360557, 45.605279), point2=(39.561169, 45.116322))
s0.Line(point1=(39.561169, 45.116322), point2=(39.500612, 43.911043))
s0.Line(point1=(39.500612, 43.911043), point2=(39.078087, 43.962470))
s0.Line(point1=(39.078087, 43.962470), point2=(38.529536, 44.698219))
s0.Line(point1=(38.529536, 44.698219), point2=(36.977761, 45.632226))
s0.Line(point1=(36.977761, 45.632226), point2=(35.376312, 45.996476))
s0.Line(point1=(35.376312, 45.996476), point2=(35.358305, 46.550345))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(38.700000, 43.800000), point2=(38.550000, 43.050000))
s0.Line(point1=(38.550000, 43.050000), point2=(37.800000, 42.900000))
s0.Line(point1=(37.800000, 42.900000), point2=(37.200000, 42.300000))
s0.Line(point1=(37.200000, 42.300000), point2=(35.250000, 42.750000))
s0.Line(point1=(35.250000, 42.750000), point2=(35.250000, 43.200000))
s0.Line(point1=(35.250000, 43.200000), point2=(36.600000, 44.250000))
s0.Line(point1=(36.600000, 44.250000), point2=(37.800000, 44.250000))
s0.Line(point1=(37.800000, 44.250000), point2=(38.700000, 43.800000))
s0.Line(point1=(38.842779, 43.869831), point2=(38.667670, 42.932330))
s0.Line(point1=(38.667670, 42.932330), point2=(37.890322, 42.731231))
s0.Line(point1=(37.890322, 42.731231), point2=(37.248225, 42.131850))
s0.Line(point1=(37.248225, 42.131850), point2=(35.127514, 42.652561))
s0.Line(point1=(35.127514, 42.652561), point2=(35.088606, 43.278935))
s0.Line(point1=(35.088606, 43.278935), point2=(36.538606, 44.428935))
s0.Line(point1=(36.538606, 44.428935), point2=(37.844721, 44.439443))
s0.Line(point1=(37.844721, 44.439443), point2=(38.842779, 43.869831))
s0.Line(point1=(38.557221, 43.730169), point2=(38.432330, 43.167670))
s0.Line(point1=(38.432330, 43.167670), point2=(37.709678, 43.068769))
s0.Line(point1=(37.709678, 43.068769), point2=(37.151775, 42.468150))
s0.Line(point1=(37.151775, 42.468150), point2=(35.372486, 42.847439))
s0.Line(point1=(35.372486, 42.847439), point2=(35.411394, 43.121065))
s0.Line(point1=(35.411394, 43.121065), point2=(36.661394, 44.071065))
s0.Line(point1=(36.661394, 44.071065), point2=(37.755279, 44.060557))
s0.Line(point1=(37.755279, 44.060557), point2=(38.557221, 43.730169))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(35.250000, 17.700000), point2=(37.650000, 18.000000))
s0.Line(point1=(37.650000, 18.000000), point2=(38.100000, 18.900000))
s0.Line(point1=(38.100000, 18.900000), point2=(38.550000, 18.900000))
s0.Line(point1=(38.550000, 18.900000), point2=(39.450000, 18.000000))
s0.Line(point1=(39.450000, 18.000000), point2=(42.000000, 16.500000))
s0.Line(point1=(42.000000, 16.500000), point2=(42.150000, 14.700000))
s0.Line(point1=(42.150000, 14.700000), point2=(40.050000, 14.700000))
s0.Line(point1=(40.050000, 14.700000), point2=(35.550000, 15.900000))
s0.Line(point1=(35.550000, 15.900000), point2=(35.250000, 16.200000))
s0.Line(point1=(35.250000, 16.200000), point2=(35.250000, 17.700000))
s0.Line(point1=(35.137597, 17.799228), point2=(37.548154, 18.143949))
s0.Line(point1=(37.548154, 18.143949), point2=(38.010557, 19.044721))
s0.Line(point1=(38.010557, 19.044721), point2=(38.620711, 19.070711))
s0.Line(point1=(38.620711, 19.070711), point2=(39.571413, 18.156904))
s0.Line(point1=(39.571413, 18.156904), point2=(42.150357, 16.594498))
s0.Line(point1=(42.150357, 16.594498), point2=(42.249655, 14.608305))
s0.Line(point1=(42.249655, 14.608305), point2=(40.024234, 14.503377))
s0.Line(point1=(40.024234, 14.503377), point2=(35.453523, 15.732666))
s0.Line(point1=(35.453523, 15.732666), point2=(35.079289, 16.129289))
s0.Line(point1=(35.079289, 16.129289), point2=(35.137597, 17.799228))
s0.Line(point1=(35.362403, 17.600772), point2=(37.751846, 17.856051))
s0.Line(point1=(37.751846, 17.856051), point2=(38.189443, 18.755279))
s0.Line(point1=(38.189443, 18.755279), point2=(38.479289, 18.729289))
s0.Line(point1=(38.479289, 18.729289), point2=(39.328587, 17.843096))
s0.Line(point1=(39.328587, 17.843096), point2=(41.849643, 16.405502))
s0.Line(point1=(41.849643, 16.405502), point2=(42.050345, 14.791695))
s0.Line(point1=(42.050345, 14.791695), point2=(40.075766, 14.896623))
s0.Line(point1=(40.075766, 14.896623), point2=(35.646477, 16.067334))
s0.Line(point1=(35.646477, 16.067334), point2=(35.420711, 16.270711))
s0.Line(point1=(35.420711, 16.270711), point2=(35.362403, 17.600772))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(37.650000, 25.950000), point2=(37.650000, 24.900000))
s0.Line(point1=(37.650000, 24.900000), point2=(35.850000, 24.600000))
s0.Line(point1=(35.850000, 24.600000), point2=(35.850000, 25.350000))
s0.Line(point1=(35.850000, 25.350000), point2=(36.450000, 26.100000))
s0.Line(point1=(36.450000, 26.100000), point2=(37.650000, 25.950000))
s0.Line(point1=(37.762403, 26.049228), point2=(37.766440, 24.801361))
s0.Line(point1=(37.766440, 24.801361), point2=(35.766440, 24.501361))
s0.Line(point1=(35.766440, 24.501361), point2=(35.671913, 25.412470))
s0.Line(point1=(35.671913, 25.412470), point2=(36.384317, 26.261697))
s0.Line(point1=(36.384317, 26.261697), point2=(37.762403, 26.049228))
s0.Line(point1=(37.537597, 25.850772), point2=(37.533560, 24.998639))
s0.Line(point1=(37.533560, 24.998639), point2=(35.933560, 24.698639))
s0.Line(point1=(35.933560, 24.698639), point2=(36.028087, 25.287530))
s0.Line(point1=(36.028087, 25.287530), point2=(36.515683, 25.938303))
s0.Line(point1=(36.515683, 25.938303), point2=(37.537597, 25.850772))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(36.000000, 51.150000), point2=(36.600000, 51.450000))
s0.Line(point1=(36.600000, 51.450000), point2=(37.200000, 50.700000))
s0.Line(point1=(37.200000, 50.700000), point2=(36.300000, 50.550000))
s0.Line(point1=(36.300000, 50.550000), point2=(36.000000, 51.150000))
s0.Line(point1=(35.865836, 51.194721), point2=(36.633366, 51.601912))
s0.Line(point1=(36.633366, 51.601912), point2=(37.294527, 50.663830))
s0.Line(point1=(37.294527, 50.663830), point2=(36.226997, 50.406639))
s0.Line(point1=(36.226997, 50.406639), point2=(35.865836, 51.194721))
s0.Line(point1=(36.134164, 51.105279), point2=(36.566634, 51.298088))
s0.Line(point1=(36.566634, 51.298088), point2=(37.105473, 50.736170))
s0.Line(point1=(37.105473, 50.736170), point2=(36.373003, 50.693361))
s0.Line(point1=(36.373003, 50.693361), point2=(36.134164, 51.105279))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(36.450000, 31.950000), point2=(37.350000, 31.650000))
s0.Line(point1=(37.350000, 31.650000), point2=(37.500000, 30.750000))
s0.Line(point1=(37.500000, 30.750000), point2=(37.200000, 30.450000))
s0.Line(point1=(37.200000, 30.450000), point2=(36.300000, 30.600000))
s0.Line(point1=(36.300000, 30.600000), point2=(36.450000, 31.950000))
s0.Line(point1=(36.382234, 32.055911), point2=(37.480262, 31.761308))
s0.Line(point1=(37.480262, 31.761308), point2=(37.669350, 30.695729))
s0.Line(point1=(37.669350, 30.695729), point2=(37.254271, 30.280650))
s0.Line(point1=(37.254271, 30.280650), point2=(36.184172, 30.512404))
s0.Line(point1=(36.184172, 30.512404), point2=(36.382234, 32.055911))
s0.Line(point1=(36.517766, 31.844089), point2=(37.219738, 31.538692))
s0.Line(point1=(37.219738, 31.538692), point2=(37.330650, 30.804271))
s0.Line(point1=(37.330650, 30.804271), point2=(37.145729, 30.619350))
s0.Line(point1=(37.145729, 30.619350), point2=(36.415828, 30.687596))
s0.Line(point1=(36.415828, 30.687596), point2=(36.517766, 31.844089))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(40.800000, 29.700000), point2=(40.800000, 28.950000))
s0.Line(point1=(40.800000, 28.950000), point2=(38.400000, 27.000000))
s0.Line(point1=(38.400000, 27.000000), point2=(36.300000, 27.000000))
s0.Line(point1=(36.300000, 27.000000), point2=(36.300000, 27.750000))
s0.Line(point1=(36.300000, 27.750000), point2=(38.700000, 29.550000))
s0.Line(point1=(38.700000, 29.550000), point2=(40.800000, 29.700000))
s0.Line(point1=(40.892875, 29.799746), point2=(40.963059, 28.872389))
s0.Line(point1=(40.963059, 28.872389), point2=(38.463059, 26.822389))
s0.Line(point1=(38.463059, 26.822389), point2=(36.200000, 26.900000))
s0.Line(point1=(36.200000, 26.900000), point2=(36.140000, 27.830000))
s0.Line(point1=(36.140000, 27.830000), point2=(38.632875, 29.729746))
s0.Line(point1=(38.632875, 29.729746), point2=(40.892875, 29.799746))
s0.Line(point1=(40.707125, 29.600254), point2=(40.636941, 29.027611))
s0.Line(point1=(40.636941, 29.027611), point2=(38.336941, 27.177611))
s0.Line(point1=(38.336941, 27.177611), point2=(36.400000, 27.100000))
s0.Line(point1=(36.400000, 27.100000), point2=(36.460000, 27.670000))
s0.Line(point1=(36.460000, 27.670000), point2=(38.767125, 29.370254))
s0.Line(point1=(38.767125, 29.370254), point2=(40.707125, 29.600254))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(37.950000, 8.700000), point2=(39.600000, 8.700000))
s0.Line(point1=(39.600000, 8.700000), point2=(40.200000, 7.500000))
s0.Line(point1=(40.200000, 7.500000), point2=(40.500000, 5.700000))
s0.Line(point1=(40.500000, 5.700000), point2=(39.750000, 4.500000))
s0.Line(point1=(39.750000, 4.500000), point2=(38.850000, 4.350000))
s0.Line(point1=(38.850000, 4.350000), point2=(37.200000, 5.100000))
s0.Line(point1=(37.200000, 5.100000), point2=(37.050000, 6.150000))
s0.Line(point1=(37.050000, 6.150000), point2=(37.950000, 8.700000))
s0.Line(point1=(37.855701, 8.833282), point2=(39.689443, 8.844721))
s0.Line(point1=(39.689443, 8.844721), point2=(40.388082, 7.561161))
s0.Line(point1=(40.388082, 7.561161), point2=(40.683439, 5.663440))
s0.Line(point1=(40.683439, 5.663440), point2=(39.851240, 4.348361))
s0.Line(point1=(39.851240, 4.348361), point2=(38.825060, 4.160324))
s0.Line(point1=(38.825060, 4.160324), point2=(37.059625, 4.994821))
s0.Line(point1=(37.059625, 4.994821), point2=(36.856706, 6.169140))
s0.Line(point1=(36.856706, 6.169140), point2=(37.855701, 8.833282))
s0.Line(point1=(38.044299, 8.566718), point2=(39.510557, 8.555279))
s0.Line(point1=(39.510557, 8.555279), point2=(40.011918, 7.438839))
s0.Line(point1=(40.011918, 7.438839), point2=(40.316561, 5.736560))
s0.Line(point1=(40.316561, 5.736560), point2=(39.648760, 4.651639))
s0.Line(point1=(39.648760, 4.651639), point2=(38.874940, 4.539676))
s0.Line(point1=(38.874940, 4.539676), point2=(37.340375, 5.205179))
s0.Line(point1=(37.340375, 5.205179), point2=(37.243294, 6.130860))
s0.Line(point1=(37.243294, 6.130860), point2=(38.044299, 8.566718))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(37.050000, 0.900000), point2=(38.250000, 1.800000))
s0.Line(point1=(38.250000, 1.800000), point2=(40.200000, 2.400000))
s0.Line(point1=(40.200000, 2.400000), point2=(41.400000, 4.050000))
s0.Line(point1=(41.400000, 4.050000), point2=(41.850000, 6.450000))
s0.Line(point1=(41.850000, 6.450000), point2=(43.200000, 6.600000))
s0.Line(point1=(43.200000, 6.600000), point2=(45.150000, 4.950000))
s0.Line(point1=(45.150000, 4.950000), point2=(46.200000, 3.300000))
s0.Line(point1=(46.200000, 3.300000), point2=(49.050000, 1.350000))
s0.Line(point1=(49.050000, 1.350000), point2=(49.350000, 0.000000))
s0.Line(point1=(49.350000, 0.000000), point2=(37.200000, 0.000000))
s0.Line(point1=(37.200000, 0.000000), point2=(37.050000, 0.900000))
s0.Line(point1=(36.891361, 0.963560), point2=(38.160591, 1.975578))
s0.Line(point1=(38.160591, 1.975578), point2=(40.089718, 2.554395))
s0.Line(point1=(40.089718, 2.554395), point2=(41.220839, 4.127246))
s0.Line(point1=(41.220839, 4.127246), point2=(41.740670, 6.567817))
s0.Line(point1=(41.740670, 6.567817), point2=(43.253551, 6.775727))
s0.Line(point1=(43.253551, 6.775727), point2=(45.298960, 5.080026))
s0.Line(point1=(45.298960, 5.080026), point2=(46.340835, 3.436218))
s0.Line(point1=(46.340835, 3.436218), point2=(49.204087, 1.454224))
s0.Line(point1=(49.204087, 1.454224), point2=(49.447619, 0.000000))
s0.Line(point1=(49.447619, 0.000000), point2=(37.101361, 0.000000))
s0.Line(point1=(37.101361, 0.000000), point2=(36.891361, 0.963560))
s0.Line(point1=(37.208639, 0.836440), point2=(38.339409, 1.624422))
s0.Line(point1=(38.339409, 1.624422), point2=(40.310282, 2.245605))
s0.Line(point1=(40.310282, 2.245605), point2=(41.579161, 3.972754))
s0.Line(point1=(41.579161, 3.972754), point2=(41.959330, 6.332183))
s0.Line(point1=(41.959330, 6.332183), point2=(43.146449, 6.424273))
s0.Line(point1=(43.146449, 6.424273), point2=(45.001040, 4.819974))
s0.Line(point1=(45.001040, 4.819974), point2=(46.059165, 3.163782))
s0.Line(point1=(46.059165, 3.163782), point2=(48.895913, 1.245776))
s0.Line(point1=(48.895913, 1.245776), point2=(49.252381, 0.000000))
s0.Line(point1=(49.252381, 0.000000), point2=(37.298639, 0.000000))
s0.Line(point1=(37.298639, 0.000000), point2=(37.208639, 0.836440))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(37.800000, 49.800000), point2=(38.700000, 49.650000))
s0.Line(point1=(38.700000, 49.650000), point2=(40.050000, 48.300000))
s0.Line(point1=(40.050000, 48.300000), point2=(40.050000, 46.800000))
s0.Line(point1=(40.050000, 46.800000), point2=(39.000000, 46.650000))
s0.Line(point1=(39.000000, 46.650000), point2=(37.950000, 46.950000))
s0.Line(point1=(37.950000, 46.950000), point2=(37.350000, 48.600000))
s0.Line(point1=(37.350000, 48.600000), point2=(37.800000, 49.800000))
s0.Line(point1=(37.722807, 49.933752), point2=(38.787151, 49.819350))
s0.Line(point1=(38.787151, 49.819350), point2=(40.220711, 48.370711))
s0.Line(point1=(40.220711, 48.370711), point2=(40.164142, 46.701005))
s0.Line(point1=(40.164142, 46.701005), point2=(38.986670, 46.454853))
s0.Line(point1=(38.986670, 46.454853), point2=(37.828549, 46.819673))
s0.Line(point1=(37.828549, 46.819673), point2=(37.162388, 48.600938))
s0.Line(point1=(37.162388, 48.600938), point2=(37.722807, 49.933752))
s0.Line(point1=(37.877193, 49.666248), point2=(38.612849, 49.480650))
s0.Line(point1=(38.612849, 49.480650), point2=(39.879289, 48.229289))
s0.Line(point1=(39.879289, 48.229289), point2=(39.935858, 46.898995))
s0.Line(point1=(39.935858, 46.898995), point2=(39.013330, 46.845147))
s0.Line(point1=(39.013330, 46.845147), point2=(38.071451, 47.080327))
s0.Line(point1=(38.071451, 47.080327), point2=(37.537612, 48.599062))
s0.Line(point1=(37.537612, 48.599062), point2=(37.877193, 49.666248))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(42.900000, 36.750000), point2=(42.450000, 35.400000))
s0.Line(point1=(42.450000, 35.400000), point2=(40.350000, 33.900000))
s0.Line(point1=(40.350000, 33.900000), point2=(38.850000, 33.900000))
s0.Line(point1=(38.850000, 33.900000), point2=(37.350000, 34.950000))
s0.Line(point1=(37.350000, 34.950000), point2=(37.350000, 35.400000))
s0.Line(point1=(37.350000, 35.400000), point2=(40.200000, 36.750000))
s0.Line(point1=(40.200000, 36.750000), point2=(42.900000, 36.750000))
s0.Line(point1=(42.994868, 36.818377), point2=(42.602992, 35.287004))
s0.Line(point1=(42.602992, 35.287004), point2=(40.408124, 33.718627))
s0.Line(point1=(40.408124, 33.718627), point2=(38.792654, 33.718077))
s0.Line(point1=(38.792654, 33.718077), point2=(37.192654, 34.868077))
s0.Line(point1=(37.192654, 34.868077), point2=(37.207191, 35.490374))
s0.Line(point1=(37.207191, 35.490374), point2=(40.157191, 36.940374))
s0.Line(point1=(40.157191, 36.940374), point2=(42.994868, 36.818377))
s0.Line(point1=(42.805132, 36.681623), point2=(42.297008, 35.512996))
s0.Line(point1=(42.297008, 35.512996), point2=(40.291876, 34.081373))
s0.Line(point1=(40.291876, 34.081373), point2=(38.907346, 34.081923))
s0.Line(point1=(38.907346, 34.081923), point2=(37.507346, 35.031923))
s0.Line(point1=(37.507346, 35.031923), point2=(37.492809, 35.309626))
s0.Line(point1=(37.492809, 35.309626), point2=(40.242809, 36.559626))
s0.Line(point1=(40.242809, 36.559626), point2=(42.805132, 36.681623))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(37.350000, 13.050000), point2=(38.250000, 13.050000))
s0.Line(point1=(38.250000, 13.050000), point2=(38.850000, 13.650000))
s0.Line(point1=(38.850000, 13.650000), point2=(39.300000, 13.650000))
s0.Line(point1=(39.300000, 13.650000), point2=(40.500000, 12.450000))
s0.Line(point1=(40.500000, 12.450000), point2=(40.650000, 11.400000))
s0.Line(point1=(40.650000, 11.400000), point2=(39.600000, 10.800000))
s0.Line(point1=(39.600000, 10.800000), point2=(38.400000, 10.800000))
s0.Line(point1=(38.400000, 10.800000), point2=(37.350000, 13.050000))
s0.Line(point1=(37.259382, 13.107711), point2=(38.179289, 13.220711))
s0.Line(point1=(38.179289, 13.220711), point2=(38.779289, 13.820711))
s0.Line(point1=(38.779289, 13.820711), point2=(39.370711, 13.820711))
s0.Line(point1=(39.370711, 13.820711), point2=(40.669706, 12.534853))
s0.Line(point1=(40.669706, 12.534853), point2=(40.798609, 11.327318))
s0.Line(point1=(40.798609, 11.327318), point2=(39.649614, 10.613176))
s0.Line(point1=(39.649614, 10.613176), point2=(38.309382, 10.657711))
s0.Line(point1=(38.309382, 10.657711), point2=(37.259382, 13.107711))
s0.Line(point1=(37.440618, 12.992289), point2=(38.320711, 12.879289))
s0.Line(point1=(38.320711, 12.879289), point2=(38.920711, 13.479289))
s0.Line(point1=(38.920711, 13.479289), point2=(39.229289, 13.479289))
s0.Line(point1=(39.229289, 13.479289), point2=(40.330294, 12.365147))
s0.Line(point1=(40.330294, 12.365147), point2=(40.501391, 11.472682))
s0.Line(point1=(40.501391, 11.472682), point2=(39.550386, 10.986824))
s0.Line(point1=(39.550386, 10.986824), point2=(38.490618, 10.942289))
s0.Line(point1=(38.490618, 10.942289), point2=(37.440618, 12.992289))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
print 120
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(38.100000, 42.300000), point2=(38.700000, 42.600000))
s0.Line(point1=(38.700000, 42.600000), point2=(39.750000, 42.150000))
s0.Line(point1=(39.750000, 42.150000), point2=(40.200000, 40.950000))
s0.Line(point1=(40.200000, 40.950000), point2=(39.750000, 40.650000))
s0.Line(point1=(39.750000, 40.650000), point2=(38.700000, 41.100000))
s0.Line(point1=(38.700000, 41.100000), point2=(38.100000, 42.300000))
s0.Line(point1=(37.965836, 42.344721), point2=(38.694671, 42.781357))
s0.Line(point1=(38.694671, 42.781357), point2=(39.883025, 42.277027))
s0.Line(point1=(39.883025, 42.277027), point2=(40.349103, 40.901907))
s0.Line(point1=(40.349103, 40.901907), point2=(39.766078, 40.474880))
s0.Line(point1=(39.766078, 40.474880), point2=(38.571165, 40.963364))
s0.Line(point1=(38.571165, 40.963364), point2=(37.965836, 42.344721))
s0.Line(point1=(38.234164, 42.255279), point2=(38.705329, 42.418643))
s0.Line(point1=(38.705329, 42.418643), point2=(39.616975, 42.022973))
s0.Line(point1=(39.616975, 42.022973), point2=(40.050897, 40.998093))
s0.Line(point1=(40.050897, 40.998093), point2=(39.733922, 40.825120))
s0.Line(point1=(39.733922, 40.825120), point2=(38.828835, 41.236636))
s0.Line(point1=(38.828835, 41.236636), point2=(38.234164, 42.255279))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(41.400000, 33.000000), point2=(41.400000, 32.400000))
s0.Line(point1=(41.400000, 32.400000), point2=(40.650000, 31.800000))
s0.Line(point1=(40.650000, 31.800000), point2=(40.650000, 30.750000))
s0.Line(point1=(40.650000, 30.750000), point2=(39.600000, 31.050000))
s0.Line(point1=(39.600000, 31.050000), point2=(38.250000, 32.400000))
s0.Line(point1=(38.250000, 32.400000), point2=(38.400000, 33.000000))
s0.Line(point1=(38.400000, 33.000000), point2=(41.400000, 33.000000))
s0.Line(point1=(41.500000, 33.100000), point2=(41.562470, 32.321913))
s0.Line(point1=(41.562470, 32.321913), point2=(40.812470, 31.721913))
s0.Line(point1=(40.812470, 31.721913), point2=(40.722528, 30.653848))
s0.Line(point1=(40.722528, 30.653848), point2=(39.501817, 30.883137))
s0.Line(point1=(39.501817, 30.883137), point2=(38.082275, 32.353543))
s0.Line(point1=(38.082275, 32.353543), point2=(38.302986, 33.124254))
s0.Line(point1=(38.302986, 33.124254), point2=(41.500000, 33.100000))
s0.Line(point1=(41.300000, 32.900000), point2=(41.237530, 32.478087))
s0.Line(point1=(41.237530, 32.478087), point2=(40.487530, 31.878087))
s0.Line(point1=(40.487530, 31.878087), point2=(40.577472, 30.846152))
s0.Line(point1=(40.577472, 30.846152), point2=(39.698183, 31.216863))
s0.Line(point1=(39.698183, 31.216863), point2=(38.417725, 32.446457))
s0.Line(point1=(38.417725, 32.446457), point2=(38.497014, 32.875746))
s0.Line(point1=(38.497014, 32.875746), point2=(41.300000, 32.900000))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(38.550000, 22.800000), point2=(39.900000, 22.650000))
s0.Line(point1=(39.900000, 22.650000), point2=(40.200000, 22.350000))
s0.Line(point1=(40.200000, 22.350000), point2=(41.700000, 19.350000))
s0.Line(point1=(41.700000, 19.350000), point2=(41.700000, 18.750000))
s0.Line(point1=(41.700000, 18.750000), point2=(41.100000, 18.750000))
s0.Line(point1=(41.100000, 18.750000), point2=(40.800000, 19.350000))
s0.Line(point1=(40.800000, 19.350000), point2=(40.200000, 19.500000))
s0.Line(point1=(40.200000, 19.500000), point2=(39.300000, 19.350000))
s0.Line(point1=(39.300000, 19.350000), point2=(39.150000, 21.300000))
s0.Line(point1=(39.150000, 21.300000), point2=(38.550000, 22.200000))
s0.Line(point1=(38.550000, 22.200000), point2=(38.550000, 22.800000))
s0.Line(point1=(38.461043, 22.899388), point2=(39.981754, 22.820099))
s0.Line(point1=(39.981754, 22.820099), point2=(40.360153, 22.465432))
s0.Line(point1=(40.360153, 22.465432), point2=(41.889443, 19.394721))
s0.Line(point1=(41.889443, 19.394721), point2=(41.800000, 18.650000))
s0.Line(point1=(41.800000, 18.650000), point2=(41.010557, 18.605279))
s0.Line(point1=(41.010557, 18.605279), point2=(40.686304, 19.208264))
s0.Line(point1=(40.686304, 19.208264), point2=(40.192186, 19.304346))
s0.Line(point1=(40.192186, 19.304346), point2=(39.216734, 19.243691))
s0.Line(point1=(39.216734, 19.243691), point2=(38.967090, 21.236860))
s0.Line(point1=(38.967090, 21.236860), point2=(38.366795, 22.144530))
s0.Line(point1=(38.366795, 22.144530), point2=(38.461043, 22.899388))
s0.Line(point1=(38.638957, 22.700612), point2=(39.818246, 22.479901))
s0.Line(point1=(39.818246, 22.479901), point2=(40.039847, 22.234568))
s0.Line(point1=(40.039847, 22.234568), point2=(41.510557, 19.305279))
s0.Line(point1=(41.510557, 19.305279), point2=(41.600000, 18.850000))
s0.Line(point1=(41.600000, 18.850000), point2=(41.189443, 18.894721))
s0.Line(point1=(41.189443, 18.894721), point2=(40.913696, 19.491736))
s0.Line(point1=(40.913696, 19.491736), point2=(40.207814, 19.695654))
s0.Line(point1=(40.207814, 19.695654), point2=(39.383266, 19.456309))
s0.Line(point1=(39.383266, 19.456309), point2=(39.332910, 21.363140))
s0.Line(point1=(39.332910, 21.363140), point2=(38.733205, 22.255470))
s0.Line(point1=(38.733205, 22.255470), point2=(38.638957, 22.700612))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(42.150000, 27.000000), point2=(42.150000, 25.950000))
s0.Line(point1=(42.150000, 25.950000), point2=(41.400000, 25.650000))
s0.Line(point1=(41.400000, 25.650000), point2=(40.800000, 24.750000))
s0.Line(point1=(40.800000, 24.750000), point2=(40.050000, 24.300000))
s0.Line(point1=(40.050000, 24.300000), point2=(39.150000, 24.450000))
s0.Line(point1=(39.150000, 24.450000), point2=(38.850000, 25.200000))
s0.Line(point1=(38.850000, 25.200000), point2=(40.800000, 27.300000))
s0.Line(point1=(40.800000, 27.300000), point2=(41.400000, 27.450000))
s0.Line(point1=(41.400000, 27.450000), point2=(42.150000, 27.000000))
s0.Line(point1=(42.301450, 27.085749), point2=(42.287139, 25.857152))
s0.Line(point1=(42.287139, 25.857152), point2=(41.520344, 25.501682))
s0.Line(point1=(41.520344, 25.501682), point2=(40.934655, 24.608781))
s0.Line(point1=(40.934655, 24.608781), point2=(40.085010, 24.115611))
s0.Line(point1=(40.085010, 24.115611), point2=(39.040712, 24.314222))
s0.Line(point1=(39.040712, 24.314222), point2=(38.683873, 25.230906))
s0.Line(point1=(38.683873, 25.230906), point2=(40.702467, 27.465059))
s0.Line(point1=(40.702467, 27.465059), point2=(41.427196, 27.632764))
s0.Line(point1=(41.427196, 27.632764), point2=(42.301450, 27.085749))
s0.Line(point1=(41.998550, 26.914251), point2=(42.012861, 26.042848))
s0.Line(point1=(42.012861, 26.042848), point2=(41.279656, 25.798318))
s0.Line(point1=(41.279656, 25.798318), point2=(40.665345, 24.891219))
s0.Line(point1=(40.665345, 24.891219), point2=(40.014990, 24.484389))
s0.Line(point1=(40.014990, 24.484389), point2=(39.259288, 24.585778))
s0.Line(point1=(39.259288, 24.585778), point2=(39.016127, 25.169094))
s0.Line(point1=(39.016127, 25.169094), point2=(40.897533, 27.134941))
s0.Line(point1=(40.897533, 27.134941), point2=(41.372804, 27.267236))
s0.Line(point1=(41.372804, 27.267236), point2=(41.998550, 26.914251))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(39.450000, 52.500000), point2=(41.100000, 52.500000))
s0.Line(point1=(41.100000, 52.500000), point2=(42.000000, 51.150000))
s0.Line(point1=(42.000000, 51.150000), point2=(42.000000, 50.550000))
s0.Line(point1=(42.000000, 50.550000), point2=(41.400000, 50.550000))
s0.Line(point1=(41.400000, 50.550000), point2=(41.250000, 49.350000))
s0.Line(point1=(41.250000, 49.350000), point2=(40.800000, 49.350000))
s0.Line(point1=(40.800000, 49.350000), point2=(40.050000, 50.400000))
s0.Line(point1=(40.050000, 50.400000), point2=(39.450000, 51.450000))
s0.Line(point1=(39.450000, 51.450000), point2=(39.450000, 52.500000))
s0.Line(point1=(39.350000, 52.500000), point2=(41.183205, 52.500000))
s0.Line(point1=(41.183205, 52.500000), point2=(42.183205, 51.205470))
s0.Line(point1=(42.183205, 51.205470), point2=(42.100000, 50.450000))
s0.Line(point1=(42.100000, 50.450000), point2=(41.499228, 50.437597))
s0.Line(point1=(41.499228, 50.437597), point2=(41.349228, 49.237597))
s0.Line(point1=(41.349228, 49.237597), point2=(40.718627, 49.191876))
s0.Line(point1=(40.718627, 49.191876), point2=(39.881802, 50.292262))
s0.Line(point1=(39.881802, 50.292262), point2=(39.263176, 51.400386))
s0.Line(point1=(39.263176, 51.400386), point2=(39.350000, 52.500000))
s0.Line(point1=(39.550000, 52.500000), point2=(41.016795, 52.500000))
s0.Line(point1=(41.016795, 52.500000), point2=(41.816795, 51.094530))
s0.Line(point1=(41.816795, 51.094530), point2=(41.900000, 50.650000))
s0.Line(point1=(41.900000, 50.650000), point2=(41.300772, 50.662403))
s0.Line(point1=(41.300772, 50.662403), point2=(41.150772, 49.462403))
s0.Line(point1=(41.150772, 49.462403), point2=(40.881373, 49.508124))
s0.Line(point1=(40.881373, 49.508124), point2=(40.218198, 50.507738))
s0.Line(point1=(40.218198, 50.507738), point2=(39.636824, 51.499614))
s0.Line(point1=(39.636824, 51.499614), point2=(39.550000, 52.500000))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(39.450000, 39.450000), point2=(40.800000, 39.900000))
s0.Line(point1=(40.800000, 39.900000), point2=(41.550000, 39.600000))
s0.Line(point1=(41.550000, 39.600000), point2=(41.700000, 39.000000))
s0.Line(point1=(41.700000, 39.000000), point2=(41.250000, 38.400000))
s0.Line(point1=(41.250000, 38.400000), point2=(40.350000, 38.400000))
s0.Line(point1=(40.350000, 38.400000), point2=(39.450000, 39.000000))
s0.Line(point1=(39.450000, 39.000000), point2=(39.450000, 39.450000))
s0.Line(point1=(39.318377, 39.544868), point2=(40.805516, 40.087716))
s0.Line(point1=(40.805516, 40.087716), point2=(41.684153, 39.717101))
s0.Line(point1=(41.684153, 39.717101), point2=(41.877014, 38.964254))
s0.Line(point1=(41.877014, 38.964254), point2=(41.330000, 38.240000))
s0.Line(point1=(41.330000, 38.240000), point2=(40.294530, 38.216795))
s0.Line(point1=(40.294530, 38.216795), point2=(39.294530, 38.916795))
s0.Line(point1=(39.294530, 38.916795), point2=(39.318377, 39.544868))
s0.Line(point1=(39.581623, 39.355132), point2=(40.794484, 39.712284))
s0.Line(point1=(40.794484, 39.712284), point2=(41.415847, 39.482899))
s0.Line(point1=(41.415847, 39.482899), point2=(41.522986, 39.035746))
s0.Line(point1=(41.522986, 39.035746), point2=(41.170000, 38.560000))
s0.Line(point1=(41.170000, 38.560000), point2=(40.405470, 38.583205))
s0.Line(point1=(40.405470, 38.583205), point2=(39.605470, 39.083205))
s0.Line(point1=(39.605470, 39.083205), point2=(39.581623, 39.355132))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(40.050000, 43.200000), point2=(40.650000, 43.500000))
s0.Line(point1=(40.650000, 43.500000), point2=(41.550000, 43.350000))
s0.Line(point1=(41.550000, 43.350000), point2=(42.300000, 42.450000))
s0.Line(point1=(42.300000, 42.450000), point2=(42.300000, 41.850000))
s0.Line(point1=(42.300000, 41.850000), point2=(41.700000, 41.850000))
s0.Line(point1=(41.700000, 41.850000), point2=(40.800000, 42.600000))
s0.Line(point1=(40.800000, 42.600000), point2=(40.050000, 42.600000))
s0.Line(point1=(40.050000, 42.600000), point2=(40.050000, 43.200000))
s0.Line(point1=(39.905279, 43.289443), point2=(40.621719, 43.688082))
s0.Line(point1=(40.621719, 43.688082), point2=(41.643262, 43.512658))
s0.Line(point1=(41.643262, 43.512658), point2=(42.476822, 42.514018))
s0.Line(point1=(42.476822, 42.514018), point2=(42.400000, 41.750000))
s0.Line(point1=(42.400000, 41.750000), point2=(41.635982, 41.673178))
s0.Line(point1=(41.635982, 41.673178), point2=(40.735982, 42.423178))
s0.Line(point1=(40.735982, 42.423178), point2=(39.950000, 42.500000))
s0.Line(point1=(39.950000, 42.500000), point2=(39.905279, 43.289443))
s0.Line(point1=(40.194721, 43.110557), point2=(40.678281, 43.311918))
s0.Line(point1=(40.678281, 43.311918), point2=(41.456738, 43.187342))
s0.Line(point1=(41.456738, 43.187342), point2=(42.123178, 42.385982))
s0.Line(point1=(42.123178, 42.385982), point2=(42.200000, 41.950000))
s0.Line(point1=(42.200000, 41.950000), point2=(41.764018, 42.026822))
s0.Line(point1=(41.764018, 42.026822), point2=(40.864018, 42.776822))
s0.Line(point1=(40.864018, 42.776822), point2=(40.150000, 42.700000))
s0.Line(point1=(40.150000, 42.700000), point2=(40.194721, 43.110557))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(41.550000, 41.550000), point2=(41.550000, 40.500000))
s0.Line(point1=(41.550000, 40.500000), point2=(40.500000, 40.200000))
s0.Line(point1=(40.500000, 40.200000), point2=(40.350000, 40.800000))
s0.Line(point1=(40.350000, 40.800000), point2=(40.800000, 41.700000))
s0.Line(point1=(40.800000, 41.700000), point2=(41.550000, 41.550000))
s0.Line(point1=(41.669612, 41.648058), point2=(41.677472, 40.403848))
s0.Line(point1=(41.677472, 40.403848), point2=(40.430458, 40.079594))
s0.Line(point1=(40.430458, 40.079594), point2=(40.163543, 40.820468))
s0.Line(point1=(40.163543, 40.820468), point2=(40.730169, 41.842779))
s0.Line(point1=(40.730169, 41.842779), point2=(41.669612, 41.648058))
s0.Line(point1=(41.430388, 41.451942), point2=(41.422528, 40.596152))
s0.Line(point1=(41.422528, 40.596152), point2=(40.569542, 40.320406))
s0.Line(point1=(40.569542, 40.320406), point2=(40.536457, 40.779532))
s0.Line(point1=(40.536457, 40.779532), point2=(40.869831, 41.557221))
s0.Line(point1=(40.869831, 41.557221), point2=(41.430388, 41.451942))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(42.450000, 47.250000), point2=(44.100000, 46.800000))
s0.Line(point1=(44.100000, 46.800000), point2=(45.450000, 45.600000))
s0.Line(point1=(45.450000, 45.600000), point2=(45.450000, 44.700000))
s0.Line(point1=(45.450000, 44.700000), point2=(44.100000, 42.300000))
s0.Line(point1=(44.100000, 42.300000), point2=(43.050000, 42.600000))
s0.Line(point1=(43.050000, 42.600000), point2=(41.850000, 43.500000))
s0.Line(point1=(41.850000, 43.500000), point2=(41.100000, 44.700000))
s0.Line(point1=(41.100000, 44.700000), point2=(41.700000, 46.650000))
s0.Line(point1=(41.700000, 46.650000), point2=(42.450000, 46.950000))
s0.Line(point1=(42.450000, 46.950000), point2=(42.450000, 47.250000))
s0.Line(point1=(42.376312, 47.346476), point2=(44.192748, 46.971217))
s0.Line(point1=(44.192748, 46.971217), point2=(45.616436, 45.674741))
s0.Line(point1=(45.616436, 45.674741), point2=(45.637158, 44.650974))
s0.Line(point1=(45.637158, 44.650974), point2=(44.159685, 42.154821))
s0.Line(point1=(44.159685, 42.154821), point2=(42.962528, 42.423848))
s0.Line(point1=(42.962528, 42.423848), point2=(41.705200, 43.367000))
s0.Line(point1=(41.705200, 43.367000), point2=(40.919622, 44.676409))
s0.Line(point1=(40.919622, 44.676409), point2=(41.567283, 46.772256))
s0.Line(point1=(41.567283, 46.772256), point2=(42.312861, 47.042848))
s0.Line(point1=(42.312861, 47.042848), point2=(42.376312, 47.346476))
s0.Line(point1=(42.523688, 47.153524), point2=(44.007252, 46.628783))
s0.Line(point1=(44.007252, 46.628783), point2=(45.283564, 45.525259))
s0.Line(point1=(45.283564, 45.525259), point2=(45.262842, 44.749026))
s0.Line(point1=(45.262842, 44.749026), point2=(44.040315, 42.445179))
s0.Line(point1=(44.040315, 42.445179), point2=(43.137472, 42.776152))
s0.Line(point1=(43.137472, 42.776152), point2=(41.994800, 43.633000))
s0.Line(point1=(41.994800, 43.633000), point2=(41.280378, 44.723591))
s0.Line(point1=(41.280378, 44.723591), point2=(41.832717, 46.527744))
s0.Line(point1=(41.832717, 46.527744), point2=(42.587139, 46.857152))
s0.Line(point1=(42.587139, 46.857152), point2=(42.523688, 47.153524))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(41.400000, 22.200000), point2=(42.450000, 22.050000))
s0.Line(point1=(42.450000, 22.050000), point2=(43.200000, 21.450000))
s0.Line(point1=(43.200000, 21.450000), point2=(43.650000, 20.250000))
s0.Line(point1=(43.650000, 20.250000), point2=(43.500000, 19.500000))
s0.Line(point1=(43.500000, 19.500000), point2=(42.900000, 19.350000))
s0.Line(point1=(42.900000, 19.350000), point2=(42.600000, 20.100000))
s0.Line(point1=(42.600000, 20.100000), point2=(41.550000, 20.850000))
s0.Line(point1=(41.550000, 20.850000), point2=(41.400000, 22.200000))
s0.Line(point1=(41.314754, 22.287952), point2=(42.526612, 22.227082))
s0.Line(point1=(42.526612, 22.227082), point2=(43.356102, 21.563199))
s0.Line(point1=(43.356102, 21.563199), point2=(43.841691, 20.265501))
s0.Line(point1=(43.841691, 20.265501), point2=(43.622312, 19.383374))
s0.Line(point1=(43.622312, 19.383374), point2=(42.831406, 19.215847))
s0.Line(point1=(42.831406, 19.215847), point2=(42.449029, 19.981488))
s0.Line(point1=(42.449029, 19.981488), point2=(41.392488, 20.757584))
s0.Line(point1=(41.392488, 20.757584), point2=(41.314754, 22.287952))
s0.Line(point1=(41.485246, 22.112048), point2=(42.373388, 21.872918))
s0.Line(point1=(42.373388, 21.872918), point2=(43.043898, 21.336801))
s0.Line(point1=(43.043898, 21.336801), point2=(43.458309, 20.234499))
s0.Line(point1=(43.458309, 20.234499), point2=(43.377688, 19.616626))
s0.Line(point1=(43.377688, 19.616626), point2=(42.968594, 19.484153))
s0.Line(point1=(42.968594, 19.484153), point2=(42.750971, 20.218512))
s0.Line(point1=(42.750971, 20.218512), point2=(41.707512, 20.942416))
s0.Line(point1=(41.707512, 20.942416), point2=(41.485246, 22.112048))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(45.600000, 24.300000), point2=(45.150000, 21.600000))
s0.Line(point1=(45.150000, 21.600000), point2=(44.700000, 21.600000))
s0.Line(point1=(44.700000, 21.600000), point2=(44.100000, 22.350000))
s0.Line(point1=(44.100000, 22.350000), point2=(43.350000, 22.350000))
s0.Line(point1=(43.350000, 22.350000), point2=(42.900000, 23.250000))
s0.Line(point1=(42.900000, 23.250000), point2=(41.550000, 23.250000))
s0.Line(point1=(41.550000, 23.250000), point2=(41.550000, 23.700000))
s0.Line(point1=(41.550000, 23.700000), point2=(42.750000, 24.750000))
s0.Line(point1=(42.750000, 24.750000), point2=(45.600000, 24.300000))
s0.Line(point1=(45.714236, 24.382336), point2=(45.248639, 21.483560))
s0.Line(point1=(45.248639, 21.483560), point2=(44.621913, 21.437530))
s0.Line(point1=(44.621913, 21.437530), point2=(44.021913, 22.187530))
s0.Line(point1=(44.021913, 22.187530), point2=(43.260557, 22.205279))
s0.Line(point1=(43.260557, 22.205279), point2=(42.810557, 23.105279))
s0.Line(point1=(42.810557, 23.105279), point2=(41.450000, 23.150000))
s0.Line(point1=(41.450000, 23.150000), point2=(41.384150, 23.775258))
s0.Line(point1=(41.384150, 23.775258), point2=(42.699746, 24.924034))
s0.Line(point1=(42.699746, 24.924034), point2=(45.714236, 24.382336))
s0.Line(point1=(45.485764, 24.217664), point2=(45.051361, 21.716440))
s0.Line(point1=(45.051361, 21.716440), point2=(44.778087, 21.762470))
s0.Line(point1=(44.778087, 21.762470), point2=(44.178087, 22.512470))
s0.Line(point1=(44.178087, 22.512470), point2=(43.439443, 22.494721))
s0.Line(point1=(43.439443, 22.494721), point2=(42.989443, 23.394721))
s0.Line(point1=(42.989443, 23.394721), point2=(41.650000, 23.350000))
s0.Line(point1=(41.650000, 23.350000), point2=(41.715850, 23.624742))
s0.Line(point1=(41.715850, 23.624742), point2=(42.800254, 24.575966))
s0.Line(point1=(42.800254, 24.575966), point2=(45.485764, 24.217664))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(41.550000, 11.550000), point2=(44.550000, 11.700000))
s0.Line(point1=(44.550000, 11.700000), point2=(46.500000, 11.100000))
s0.Line(point1=(46.500000, 11.100000), point2=(48.450000, 11.100000))
s0.Line(point1=(48.450000, 11.100000), point2=(51.900000, 9.750000))
s0.Line(point1=(51.900000, 9.750000), point2=(51.900000, 8.700000))
s0.Line(point1=(51.900000, 8.700000), point2=(49.650000, 5.100000))
s0.Line(point1=(49.650000, 5.100000), point2=(48.300000, 4.050000))
s0.Line(point1=(48.300000, 4.050000), point2=(47.100000, 4.950000))
s0.Line(point1=(47.100000, 4.950000), point2=(46.200000, 6.150000))
s0.Line(point1=(46.200000, 6.150000), point2=(43.950000, 7.200000))
s0.Line(point1=(43.950000, 7.200000), point2=(42.900000, 8.250000))
s0.Line(point1=(42.900000, 8.250000), point2=(41.700000, 9.750000))
s0.Line(point1=(41.700000, 9.750000), point2=(41.550000, 11.550000))
s0.Line(point1=(41.445352, 11.641571), point2=(44.574415, 11.895453))
s0.Line(point1=(44.574415, 11.895453), point2=(46.529409, 11.295578))
s0.Line(point1=(46.529409, 11.295578), point2=(48.486440, 11.293124))
s0.Line(point1=(48.486440, 11.293124), point2=(52.036440, 9.843124))
s0.Line(point1=(52.036440, 9.843124), point2=(52.084800, 8.647000))
s0.Line(point1=(52.084800, 8.647000), point2=(49.796194, 4.968065))
s0.Line(point1=(49.796194, 4.968065), point2=(48.301394, 3.891065))
s0.Line(point1=(48.301394, 3.891065), point2=(46.960000, 4.810000))
s0.Line(point1=(46.960000, 4.810000), point2=(46.077711, 5.999382))
s0.Line(point1=(46.077711, 5.999382), point2=(43.837001, 7.038671))
s0.Line(point1=(43.837001, 7.038671), point2=(42.751202, 8.116820))
s0.Line(point1=(42.751202, 8.116820), point2=(41.522259, 9.679226))
s0.Line(point1=(41.522259, 9.679226), point2=(41.445352, 11.641571))
s0.Line(point1=(41.654648, 11.458429), point2=(44.525585, 11.504547))
s0.Line(point1=(44.525585, 11.504547), point2=(46.470591, 10.904422))
s0.Line(point1=(46.470591, 10.904422), point2=(48.413560, 10.906876))
s0.Line(point1=(48.413560, 10.906876), point2=(51.763560, 9.656876))
s0.Line(point1=(51.763560, 9.656876), point2=(51.715200, 8.753000))
s0.Line(point1=(51.715200, 8.753000), point2=(49.503806, 5.231935))
s0.Line(point1=(49.503806, 5.231935), point2=(48.298606, 4.208935))
s0.Line(point1=(48.298606, 4.208935), point2=(47.240000, 5.090000))
s0.Line(point1=(47.240000, 5.090000), point2=(46.322289, 6.300618))
s0.Line(point1=(46.322289, 6.300618), point2=(44.062999, 7.361329))
s0.Line(point1=(44.062999, 7.361329), point2=(43.048798, 8.383180))
s0.Line(point1=(43.048798, 8.383180), point2=(41.877741, 9.820774))
s0.Line(point1=(41.877741, 9.820774), point2=(41.654648, 11.458429))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(42.600000, 50.700000), point2=(43.350000, 50.700000))
s0.Line(point1=(43.350000, 50.700000), point2=(43.650000, 50.100000))
s0.Line(point1=(43.650000, 50.100000), point2=(43.350000, 49.350000))
s0.Line(point1=(43.350000, 49.350000), point2=(44.100000, 48.150000))
s0.Line(point1=(44.100000, 48.150000), point2=(44.100000, 47.550000))
s0.Line(point1=(44.100000, 47.550000), point2=(43.500000, 47.550000))
s0.Line(point1=(43.500000, 47.550000), point2=(41.700000, 48.450000))
s0.Line(point1=(41.700000, 48.450000), point2=(42.600000, 50.700000))
s0.Line(point1=(42.507152, 50.837139), point2=(43.439443, 50.844721))
s0.Line(point1=(43.439443, 50.844721), point2=(43.832290, 50.107582))
s0.Line(point1=(43.832290, 50.107582), point2=(43.527647, 49.365861))
s0.Line(point1=(43.527647, 49.365861), point2=(44.284800, 48.203000))
s0.Line(point1=(44.284800, 48.203000), point2=(44.200000, 47.450000))
s0.Line(point1=(44.200000, 47.450000), point2=(43.455279, 47.360557))
s0.Line(point1=(43.455279, 47.360557), point2=(41.562431, 48.397696))
s0.Line(point1=(41.562431, 48.397696), point2=(42.507152, 50.837139))
s0.Line(point1=(42.692848, 50.562861), point2=(43.260557, 50.555279))
s0.Line(point1=(43.260557, 50.555279), point2=(43.467710, 50.092418))
s0.Line(point1=(43.467710, 50.092418), point2=(43.172353, 49.334139))
s0.Line(point1=(43.172353, 49.334139), point2=(43.915200, 48.097000))
s0.Line(point1=(43.915200, 48.097000), point2=(44.000000, 47.650000))
s0.Line(point1=(44.000000, 47.650000), point2=(43.544721, 47.739443))
s0.Line(point1=(43.544721, 47.739443), point2=(41.837569, 48.502304))
s0.Line(point1=(41.837569, 48.502304), point2=(42.692848, 50.562861))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(42.000000, 13.350000), point2=(42.450000, 13.800000))
s0.Line(point1=(42.450000, 13.800000), point2=(43.650000, 13.950000))
s0.Line(point1=(43.650000, 13.950000), point2=(43.950000, 13.650000))
s0.Line(point1=(43.950000, 13.650000), point2=(43.800000, 13.200000))
s0.Line(point1=(43.800000, 13.200000), point2=(44.400000, 12.750000))
s0.Line(point1=(44.400000, 12.750000), point2=(44.400000, 12.150000))
s0.Line(point1=(44.400000, 12.150000), point2=(42.000000, 12.900000))
s0.Line(point1=(42.000000, 12.900000), point2=(42.000000, 13.350000))
s0.Line(point1=(41.829289, 13.420711), point2=(42.366886, 13.969938))
s0.Line(point1=(42.366886, 13.969938), point2=(43.708307, 14.119938))
s0.Line(point1=(43.708307, 14.119938), point2=(44.115579, 13.689088))
s0.Line(point1=(44.115579, 13.689088), point2=(43.954868, 13.248377))
s0.Line(point1=(43.954868, 13.248377), point2=(44.560000, 12.830000))
s0.Line(point1=(44.560000, 12.830000), point2=(44.470173, 12.054552))
s0.Line(point1=(44.470173, 12.054552), point2=(41.870173, 12.804552))
s0.Line(point1=(41.870173, 12.804552), point2=(41.829289, 13.420711))
s0.Line(point1=(42.170711, 13.279289), point2=(42.533114, 13.630062))
s0.Line(point1=(42.533114, 13.630062), point2=(43.591693, 13.780062))
s0.Line(point1=(43.591693, 13.780062), point2=(43.784421, 13.610912))
s0.Line(point1=(43.784421, 13.610912), point2=(43.645132, 13.151623))
s0.Line(point1=(43.645132, 13.151623), point2=(44.240000, 12.670000))
s0.Line(point1=(44.240000, 12.670000), point2=(44.329827, 12.245448))
s0.Line(point1=(44.329827, 12.245448), point2=(42.129827, 12.995448))
s0.Line(point1=(42.129827, 12.995448), point2=(42.170711, 13.279289))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(44.400000, 33.450000), point2=(44.400000, 32.550000))
s0.Line(point1=(44.400000, 32.550000), point2=(43.500000, 31.650000))
s0.Line(point1=(43.500000, 31.650000), point2=(42.450000, 31.350000))
s0.Line(point1=(42.450000, 31.350000), point2=(42.150000, 32.250000))
s0.Line(point1=(42.150000, 32.250000), point2=(42.750000, 33.150000))
s0.Line(point1=(42.750000, 33.150000), point2=(43.800000, 33.600000))
s0.Line(point1=(43.800000, 33.600000), point2=(44.400000, 33.450000))
s0.Line(point1=(44.524254, 33.547014), point2=(44.570711, 32.479289))
s0.Line(point1=(44.570711, 32.479289), point2=(43.598183, 31.483137))
s0.Line(point1=(43.598183, 31.483137), point2=(42.382604, 31.222225))
s0.Line(point1=(42.382604, 31.222225), point2=(41.971927, 32.273847))
s0.Line(point1=(41.971927, 32.273847), point2=(42.627403, 33.297385))
s0.Line(point1=(42.627403, 33.297385), point2=(43.784862, 33.788929))
s0.Line(point1=(43.784862, 33.788929), point2=(44.524254, 33.547014))
s0.Line(point1=(44.275746, 33.352986), point2=(44.229289, 32.620711))
s0.Line(point1=(44.229289, 32.620711), point2=(43.401817, 31.816863))
s0.Line(point1=(43.401817, 31.816863), point2=(42.517396, 31.477775))
s0.Line(point1=(42.517396, 31.477775), point2=(42.328073, 32.226153))
s0.Line(point1=(42.328073, 32.226153), point2=(42.872597, 33.002615))
s0.Line(point1=(42.872597, 33.002615), point2=(43.815138, 33.411071))
s0.Line(point1=(43.815138, 33.411071), point2=(44.275746, 33.352986))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(42.300000, 18.450000), point2=(42.900000, 18.450000))
s0.Line(point1=(42.900000, 18.450000), point2=(43.800000, 17.250000))
s0.Line(point1=(43.800000, 17.250000), point2=(43.500000, 16.050000))
s0.Line(point1=(43.500000, 16.050000), point2=(42.900000, 16.050000))
s0.Line(point1=(42.900000, 16.050000), point2=(42.300000, 17.400000))
s0.Line(point1=(42.300000, 17.400000), point2=(42.300000, 18.450000))
s0.Line(point1=(42.200000, 18.550000), point2=(42.980000, 18.610000))
s0.Line(point1=(42.980000, 18.610000), point2=(43.977014, 17.285746))
s0.Line(point1=(43.977014, 17.285746), point2=(43.597014, 15.925746))
s0.Line(point1=(43.597014, 15.925746), point2=(42.808619, 15.909386))
s0.Line(point1=(42.808619, 15.909386), point2=(42.108619, 17.359386))
s0.Line(point1=(42.108619, 17.359386), point2=(42.200000, 18.550000))
s0.Line(point1=(42.400000, 18.350000), point2=(42.820000, 18.290000))
s0.Line(point1=(42.820000, 18.290000), point2=(43.622986, 17.214254))
s0.Line(point1=(43.622986, 17.214254), point2=(43.402986, 16.174254))
s0.Line(point1=(43.402986, 16.174254), point2=(42.991381, 16.190614))
s0.Line(point1=(42.991381, 16.190614), point2=(42.491381, 17.440614))
s0.Line(point1=(42.491381, 17.440614), point2=(42.400000, 18.350000))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(45.000000, 41.850000), point2=(45.000000, 41.250000))
s0.Line(point1=(45.000000, 41.250000), point2=(44.400000, 41.100000))
s0.Line(point1=(44.400000, 41.100000), point2=(44.250000, 40.500000))
s0.Line(point1=(44.250000, 40.500000), point2=(43.050000, 40.350000))
s0.Line(point1=(43.050000, 40.350000), point2=(42.600000, 40.650000))
s0.Line(point1=(42.600000, 40.650000), point2=(42.750000, 41.400000))
s0.Line(point1=(42.750000, 41.400000), point2=(45.000000, 41.850000))
s0.Line(point1=(45.080388, 41.948058), point2=(45.124254, 41.152986))
s0.Line(point1=(45.124254, 41.152986), point2=(44.521268, 40.978732))
s0.Line(point1=(44.521268, 40.978732), point2=(44.359418, 40.376519))
s0.Line(point1=(44.359418, 40.376519), point2=(43.006933, 40.167567))
s0.Line(point1=(43.006933, 40.167567), point2=(42.446472, 40.586407))
s0.Line(point1=(42.446472, 40.586407), point2=(42.632330, 41.517670))
s0.Line(point1=(42.632330, 41.517670), point2=(45.080388, 41.948058))
s0.Line(point1=(44.919612, 41.751942), point2=(44.875746, 41.347014))
s0.Line(point1=(44.875746, 41.347014), point2=(44.278732, 41.221268))
s0.Line(point1=(44.278732, 41.221268), point2=(44.140582, 40.623481))
s0.Line(point1=(44.140582, 40.623481), point2=(43.093067, 40.532433))
s0.Line(point1=(43.093067, 40.532433), point2=(42.753528, 40.713593))
s0.Line(point1=(42.753528, 40.713593), point2=(42.867670, 41.282330))
s0.Line(point1=(42.867670, 41.282330), point2=(44.919612, 41.751942))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(42.750000, 39.300000), point2=(43.950000, 39.150000))
s0.Line(point1=(43.950000, 39.150000), point2=(44.400000, 38.400000))
s0.Line(point1=(44.400000, 38.400000), point2=(44.700000, 38.400000))
s0.Line(point1=(44.700000, 38.400000), point2=(45.450000, 37.050000))
s0.Line(point1=(45.450000, 37.050000), point2=(45.450000, 36.450000))
s0.Line(point1=(45.450000, 36.450000), point2=(44.850000, 36.450000))
s0.Line(point1=(44.850000, 36.450000), point2=(43.200000, 37.950000))
s0.Line(point1=(43.200000, 37.950000), point2=(42.750000, 39.300000))
s0.Line(point1=(42.667535, 39.367605), point2=(44.048153, 39.300677))
s0.Line(point1=(44.048153, 39.300677), point2=(44.485749, 38.551450))
s0.Line(point1=(44.485749, 38.551450), point2=(44.787416, 38.548564))
s0.Line(point1=(44.787416, 38.548564), point2=(45.637416, 37.098564))
s0.Line(point1=(45.637416, 37.098564), point2=(45.550000, 36.350000))
s0.Line(point1=(45.550000, 36.350000), point2=(44.782733, 36.276006))
s0.Line(point1=(44.782733, 36.276006), point2=(43.037864, 37.844383))
s0.Line(point1=(43.037864, 37.844383), point2=(42.667535, 39.367605))
s0.Line(point1=(42.832465, 39.232395), point2=(43.851847, 38.999323))
s0.Line(point1=(43.851847, 38.999323), point2=(44.314251, 38.248550))
s0.Line(point1=(44.314251, 38.248550), point2=(44.612584, 38.251436))
s0.Line(point1=(44.612584, 38.251436), point2=(45.262584, 37.001436))
s0.Line(point1=(45.262584, 37.001436), point2=(45.350000, 36.550000))
s0.Line(point1=(45.350000, 36.550000), point2=(44.917267, 36.623994))
s0.Line(point1=(44.917267, 36.623994), point2=(43.362136, 38.055617))
s0.Line(point1=(43.362136, 38.055617), point2=(42.832465, 39.232395))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(43.950000, 30.450000), point2=(44.850000, 29.700000))
s0.Line(point1=(44.850000, 29.700000), point2=(44.850000, 29.250000))
s0.Line(point1=(44.850000, 29.250000), point2=(43.950000, 27.900000))
s0.Line(point1=(43.950000, 27.900000), point2=(43.200000, 27.900000))
s0.Line(point1=(43.200000, 27.900000), point2=(42.900000, 28.200000))
s0.Line(point1=(42.900000, 28.200000), point2=(42.900000, 29.100000))
s0.Line(point1=(42.900000, 29.100000), point2=(43.950000, 30.450000))
s0.Line(point1=(43.935083, 30.588216), point2=(45.014018, 29.776822))
s0.Line(point1=(45.014018, 29.776822), point2=(45.033205, 29.194530))
s0.Line(point1=(45.033205, 29.194530), point2=(44.033205, 27.744530))
s0.Line(point1=(44.033205, 27.744530), point2=(43.129289, 27.729289))
s0.Line(point1=(43.129289, 27.729289), point2=(42.729289, 28.129289))
s0.Line(point1=(42.729289, 28.129289), point2=(42.721065, 29.161394))
s0.Line(point1=(42.721065, 29.161394), point2=(43.935083, 30.588216))
s0.Line(point1=(43.964917, 30.311784), point2=(44.685982, 29.623178))
s0.Line(point1=(44.685982, 29.623178), point2=(44.666795, 29.305470))
s0.Line(point1=(44.666795, 29.305470), point2=(43.866795, 28.055470))
s0.Line(point1=(43.866795, 28.055470), point2=(43.270711, 28.070711))
s0.Line(point1=(43.270711, 28.070711), point2=(43.070711, 28.270711))
s0.Line(point1=(43.070711, 28.270711), point2=(43.078935, 29.038606))
s0.Line(point1=(43.078935, 29.038606), point2=(43.964917, 30.311784))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(43.950000, 27.150000), point2=(44.700000, 27.300000))
s0.Line(point1=(44.700000, 27.300000), point2=(44.700000, 26.850000))
s0.Line(point1=(44.700000, 26.850000), point2=(45.750000, 25.650000))
s0.Line(point1=(45.750000, 25.650000), point2=(45.600000, 25.050000))
s0.Line(point1=(45.600000, 25.050000), point2=(44.550000, 25.350000))
s0.Line(point1=(44.550000, 25.350000), point2=(43.950000, 25.950000))
s0.Line(point1=(43.950000, 25.950000), point2=(43.950000, 27.150000))
s0.Line(point1=(43.830388, 27.248058), point2=(44.780388, 27.398058))
s0.Line(point1=(44.780388, 27.398058), point2=(44.875258, 26.915850))
s0.Line(point1=(44.875258, 26.915850), point2=(45.922272, 25.691597))
s0.Line(point1=(45.922272, 25.691597), point2=(45.669542, 24.929594))
s0.Line(point1=(45.669542, 24.929594), point2=(44.451817, 25.183137))
s0.Line(point1=(44.451817, 25.183137), point2=(43.779289, 25.879289))
s0.Line(point1=(43.779289, 25.879289), point2=(43.830388, 27.248058))
s0.Line(point1=(44.069612, 27.051942), point2=(44.619612, 27.201942))
s0.Line(point1=(44.619612, 27.201942), point2=(44.524742, 26.784150))
s0.Line(point1=(44.524742, 26.784150), point2=(45.577728, 25.608403))
s0.Line(point1=(45.577728, 25.608403), point2=(45.530458, 25.170406))
s0.Line(point1=(45.530458, 25.170406), point2=(44.648183, 25.516863))
s0.Line(point1=(44.648183, 25.516863), point2=(44.120711, 26.020711))
s0.Line(point1=(44.120711, 26.020711), point2=(44.069612, 27.051942))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
print 140
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(44.250000, 36.000000), point2=(45.450000, 35.700000))
s0.Line(point1=(45.450000, 35.700000), point2=(45.600000, 34.650000))
s0.Line(point1=(45.600000, 34.650000), point2=(45.300000, 34.350000))
s0.Line(point1=(45.300000, 34.350000), point2=(44.700000, 34.350000))
s0.Line(point1=(44.700000, 34.350000), point2=(44.250000, 34.800000))
s0.Line(point1=(44.250000, 34.800000), point2=(44.250000, 36.000000))
s0.Line(point1=(44.174254, 36.097014), point2=(45.573249, 35.811156))
s0.Line(point1=(45.573249, 35.811156), point2=(45.769706, 34.593431))
s0.Line(point1=(45.769706, 34.593431), point2=(45.370711, 34.179289))
s0.Line(point1=(45.370711, 34.179289), point2=(44.629289, 34.179289))
s0.Line(point1=(44.629289, 34.179289), point2=(44.079289, 34.729289))
s0.Line(point1=(44.079289, 34.729289), point2=(44.174254, 36.097014))
s0.Line(point1=(44.325746, 35.902986), point2=(45.326751, 35.588844))
s0.Line(point1=(45.326751, 35.588844), point2=(45.430294, 34.706569))
s0.Line(point1=(45.430294, 34.706569), point2=(45.229289, 34.520711))
s0.Line(point1=(45.229289, 34.520711), point2=(44.770711, 34.520711))
s0.Line(point1=(44.770711, 34.520711), point2=(44.420711, 34.870711))
s0.Line(point1=(44.420711, 34.870711), point2=(44.325746, 35.902986))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(48.450000, 52.500000), point2=(49.050000, 50.250000))
s0.Line(point1=(49.050000, 50.250000), point2=(49.050000, 49.350000))
s0.Line(point1=(49.050000, 49.350000), point2=(48.750000, 49.050000))
s0.Line(point1=(48.750000, 49.050000), point2=(47.400000, 48.900000))
s0.Line(point1=(47.400000, 48.900000), point2=(46.050000, 48.150000))
s0.Line(point1=(46.050000, 48.150000), point2=(44.250000, 48.750000))
s0.Line(point1=(44.250000, 48.750000), point2=(44.850000, 50.550000))
s0.Line(point1=(44.850000, 50.550000), point2=(44.850000, 52.500000))
s0.Line(point1=(44.850000, 52.500000), point2=(48.450000, 52.500000))
s0.Line(point1=(48.546623, 52.500000), point2=(49.246623, 50.275766))
s0.Line(point1=(49.246623, 50.275766), point2=(49.220711, 49.279289))
s0.Line(point1=(49.220711, 49.279289), point2=(48.831754, 48.879901))
s0.Line(point1=(48.831754, 48.879901), point2=(47.459607, 48.713196))
s0.Line(point1=(47.459607, 48.713196), point2=(46.066942, 47.967716))
s0.Line(point1=(46.066942, 47.967716), point2=(44.123509, 48.686754))
s0.Line(point1=(44.123509, 48.686754), point2=(44.655132, 50.581623))
s0.Line(point1=(44.655132, 50.581623), point2=(44.750000, 52.500000))
s0.Line(point1=(44.750000, 52.500000), point2=(48.546623, 52.500000))
s0.Line(point1=(48.353377, 52.500000), point2=(48.853377, 50.224234))
s0.Line(point1=(48.853377, 50.224234), point2=(48.879289, 49.420711))
s0.Line(point1=(48.879289, 49.420711), point2=(48.668246, 49.220099))
s0.Line(point1=(48.668246, 49.220099), point2=(47.340393, 49.086804))
s0.Line(point1=(47.340393, 49.086804), point2=(46.033058, 48.332284))
s0.Line(point1=(46.033058, 48.332284), point2=(44.376491, 48.813246))
s0.Line(point1=(44.376491, 48.813246), point2=(45.044868, 50.518377))
s0.Line(point1=(45.044868, 50.518377), point2=(44.950000, 52.500000))
s0.Line(point1=(44.950000, 52.500000), point2=(48.353377, 52.500000))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(44.400000, 32.400000), point2=(46.500000, 32.550000))
s0.Line(point1=(46.500000, 32.550000), point2=(47.700000, 31.650000))
s0.Line(point1=(47.700000, 31.650000), point2=(49.050000, 29.700000))
s0.Line(point1=(49.050000, 29.700000), point2=(49.050000, 28.800000))
s0.Line(point1=(49.050000, 28.800000), point2=(48.450000, 28.800000))
s0.Line(point1=(48.450000, 28.800000), point2=(47.400000, 29.850000))
s0.Line(point1=(47.400000, 29.850000), point2=(45.750000, 30.750000))
s0.Line(point1=(45.750000, 30.750000), point2=(44.550000, 30.750000))
s0.Line(point1=(44.550000, 30.750000), point2=(44.250000, 31.050000))
s0.Line(point1=(44.250000, 31.050000), point2=(44.400000, 32.400000))
s0.Line(point1=(44.293487, 32.510789), point2=(46.552875, 32.729746))
s0.Line(point1=(46.552875, 32.729746), point2=(47.842219, 31.786921))
s0.Line(point1=(47.842219, 31.786921), point2=(49.232219, 29.756921))
s0.Line(point1=(49.232219, 29.756921), point2=(49.150000, 28.700000))
s0.Line(point1=(49.150000, 28.700000), point2=(48.379289, 28.629289))
s0.Line(point1=(48.379289, 28.629289), point2=(47.281404, 29.691500))
s0.Line(point1=(47.281404, 29.691500), point2=(45.702115, 30.562210))
s0.Line(point1=(45.702115, 30.562210), point2=(44.479289, 30.579289))
s0.Line(point1=(44.479289, 30.579289), point2=(44.079901, 30.990332))
s0.Line(point1=(44.079901, 30.990332), point2=(44.293487, 32.510789))
s0.Line(point1=(44.506513, 32.289211), point2=(46.447125, 32.370254))
s0.Line(point1=(46.447125, 32.370254), point2=(47.557781, 31.513079))
s0.Line(point1=(47.557781, 31.513079), point2=(48.867781, 29.643079))
s0.Line(point1=(48.867781, 29.643079), point2=(48.950000, 28.900000))
s0.Line(point1=(48.950000, 28.900000), point2=(48.520711, 28.970711))
s0.Line(point1=(48.520711, 28.970711), point2=(47.518596, 30.008500))
s0.Line(point1=(47.518596, 30.008500), point2=(45.797885, 30.937790))
s0.Line(point1=(45.797885, 30.937790), point2=(44.620711, 30.920711))
s0.Line(point1=(44.620711, 30.920711), point2=(44.420099, 31.109668))
s0.Line(point1=(44.420099, 31.109668), point2=(44.506513, 32.289211))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(44.400000, 19.350000), point2=(46.950000, 18.150000))
s0.Line(point1=(46.950000, 18.150000), point2=(46.500000, 15.450000))
s0.Line(point1=(46.500000, 15.450000), point2=(45.900000, 14.700000))
s0.Line(point1=(45.900000, 14.700000), point2=(45.150000, 14.700000))
s0.Line(point1=(45.150000, 14.700000), point2=(44.850000, 15.150000))
s0.Line(point1=(44.850000, 15.150000), point2=(44.250000, 18.750000))
s0.Line(point1=(44.250000, 18.750000), point2=(44.400000, 19.350000))
s0.Line(point1=(44.345565, 19.464735), point2=(47.091219, 18.224042))
s0.Line(point1=(47.091219, 18.224042), point2=(46.676726, 15.371091))
s0.Line(point1=(46.676726, 15.371091), point2=(45.978087, 14.537530))
s0.Line(point1=(45.978087, 14.537530), point2=(45.066795, 14.544530))
s0.Line(point1=(45.066795, 14.544530), point2=(44.668156, 15.078090))
s0.Line(point1=(44.668156, 15.078090), point2=(44.054346, 18.757814))
s0.Line(point1=(44.054346, 18.757814), point2=(44.345565, 19.464735))
s0.Line(point1=(44.454435, 19.235265), point2=(46.808781, 18.075958))
s0.Line(point1=(46.808781, 18.075958), point2=(46.323274, 15.528909))
s0.Line(point1=(46.323274, 15.528909), point2=(45.821913, 14.862470))
s0.Line(point1=(45.821913, 14.862470), point2=(45.233205, 14.855470))
s0.Line(point1=(45.233205, 14.855470), point2=(45.031844, 15.221910))
s0.Line(point1=(45.031844, 15.221910), point2=(44.445654, 18.742186))
s0.Line(point1=(44.445654, 18.742186), point2=(44.454435, 19.235265))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(49.500000, 45.000000), point2=(49.500000, 44.100000))
s0.Line(point1=(49.500000, 44.100000), point2=(48.900000, 43.500000))
s0.Line(point1=(48.900000, 43.500000), point2=(48.300000, 42.000000))
s0.Line(point1=(48.300000, 42.000000), point2=(47.250000, 41.100000))
s0.Line(point1=(47.250000, 41.100000), point2=(46.950000, 39.750000))
s0.Line(point1=(46.950000, 39.750000), point2=(46.200000, 39.300000))
s0.Line(point1=(46.200000, 39.300000), point2=(46.200000, 38.850000))
s0.Line(point1=(46.200000, 38.850000), point2=(45.000000, 38.850000))
s0.Line(point1=(45.000000, 38.850000), point2=(45.150000, 40.200000))
s0.Line(point1=(45.150000, 40.200000), point2=(46.050000, 41.700000))
s0.Line(point1=(46.050000, 41.700000), point2=(47.250000, 42.600000))
s0.Line(point1=(47.250000, 42.600000), point2=(47.850000, 43.950000))
s0.Line(point1=(47.850000, 43.950000), point2=(48.900000, 45.000000))
s0.Line(point1=(48.900000, 45.000000), point2=(49.500000, 45.000000))
s0.Line(point1=(49.600000, 45.100000), point2=(49.670711, 44.029289))
s0.Line(point1=(49.670711, 44.029289), point2=(49.063558, 43.392150))
s0.Line(point1=(49.063558, 43.392150), point2=(48.457927, 41.886935))
s0.Line(point1=(48.457927, 41.886935), point2=(47.412698, 41.002381))
s0.Line(point1=(47.412698, 41.002381), point2=(47.099068, 39.642558))
s0.Line(point1=(47.099068, 39.642558), point2=(46.351450, 39.214251))
s0.Line(point1=(46.351450, 39.214251), point2=(46.300000, 38.750000))
s0.Line(point1=(46.300000, 38.750000), point2=(44.900612, 38.761043))
s0.Line(point1=(44.900612, 38.761043), point2=(44.964862, 40.262493))
s0.Line(point1=(44.964862, 40.262493), point2=(45.904251, 41.831450))
s0.Line(point1=(45.904251, 41.831450), point2=(47.098619, 42.720614))
s0.Line(point1=(47.098619, 42.720614), point2=(47.687908, 44.061325))
s0.Line(point1=(47.687908, 44.061325), point2=(48.829289, 45.170711))
s0.Line(point1=(48.829289, 45.170711), point2=(49.600000, 45.100000))
s0.Line(point1=(49.400000, 44.900000), point2=(49.329289, 44.170711))
s0.Line(point1=(49.329289, 44.170711), point2=(48.736442, 43.607850))
s0.Line(point1=(48.736442, 43.607850), point2=(48.142073, 42.113065))
s0.Line(point1=(48.142073, 42.113065), point2=(47.087302, 41.197619))
s0.Line(point1=(47.087302, 41.197619), point2=(46.800932, 39.857442))
s0.Line(point1=(46.800932, 39.857442), point2=(46.048550, 39.385749))
s0.Line(point1=(46.048550, 39.385749), point2=(46.100000, 38.950000))
s0.Line(point1=(46.100000, 38.950000), point2=(45.099388, 38.938957))
s0.Line(point1=(45.099388, 38.938957), point2=(45.335138, 40.137507))
s0.Line(point1=(45.335138, 40.137507), point2=(46.195749, 41.568550))
s0.Line(point1=(46.195749, 41.568550), point2=(47.401381, 42.479386))
s0.Line(point1=(47.401381, 42.479386), point2=(48.012092, 43.838675))
s0.Line(point1=(48.012092, 43.838675), point2=(48.970711, 44.829289))
s0.Line(point1=(48.970711, 44.829289), point2=(49.400000, 44.900000))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(46.650000, 34.500000), point2=(46.350000, 33.450000))
s0.Line(point1=(46.350000, 33.450000), point2=(45.300000, 32.850000))
s0.Line(point1=(45.300000, 32.850000), point2=(45.150000, 33.750000))
s0.Line(point1=(45.150000, 33.750000), point2=(45.750000, 34.650000))
s0.Line(point1=(45.750000, 34.650000), point2=(46.650000, 34.500000))
s0.Line(point1=(46.762592, 34.571167), point2=(46.495766, 33.335704))
s0.Line(point1=(46.495766, 33.335704), point2=(45.250975, 32.746736))
s0.Line(point1=(45.250975, 32.746736), point2=(44.968156, 33.789030))
s0.Line(point1=(44.968156, 33.789030), point2=(45.683235, 34.804109))
s0.Line(point1=(45.683235, 34.804109), point2=(46.762592, 34.571167))
s0.Line(point1=(46.537408, 34.428833), point2=(46.204234, 33.564296))
s0.Line(point1=(46.204234, 33.564296), point2=(45.349025, 32.953264))
s0.Line(point1=(45.349025, 32.953264), point2=(45.331844, 33.710970))
s0.Line(point1=(45.331844, 33.710970), point2=(45.816765, 34.495891))
s0.Line(point1=(45.816765, 34.495891), point2=(46.537408, 34.428833))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(45.300000, 29.400000), point2=(46.350000, 29.700000))
s0.Line(point1=(46.350000, 29.700000), point2=(47.700000, 28.200000))
s0.Line(point1=(47.700000, 28.200000), point2=(46.800000, 27.900000))
s0.Line(point1=(46.800000, 27.900000), point2=(45.300000, 29.400000))
s0.Line(point1=(45.201817, 29.425442), point2=(46.396857, 29.863049))
s0.Line(point1=(46.396857, 29.863049), point2=(47.805952, 28.172028))
s0.Line(point1=(47.805952, 28.172028), point2=(46.760912, 27.734421))
s0.Line(point1=(46.760912, 27.734421), point2=(45.201817, 29.425442))
s0.Line(point1=(45.398183, 29.374558), point2=(46.303143, 29.536951))
s0.Line(point1=(46.303143, 29.536951), point2=(47.594048, 28.227972))
s0.Line(point1=(47.594048, 28.227972), point2=(46.839088, 28.065579))
s0.Line(point1=(46.839088, 28.065579), point2=(45.398183, 29.374558))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(47.700000, 14.700000), point2=(47.850000, 14.400000))
s0.Line(point1=(47.850000, 14.400000), point2=(47.400000, 13.500000))
s0.Line(point1=(47.400000, 13.500000), point2=(45.900000, 12.150000))
s0.Line(point1=(45.900000, 12.150000), point2=(45.600000, 13.050000))
s0.Line(point1=(45.600000, 13.050000), point2=(45.900000, 14.400000))
s0.Line(point1=(45.900000, 14.400000), point2=(46.950000, 15.000000))
s0.Line(point1=(46.950000, 15.000000), point2=(47.700000, 14.700000))
s0.Line(point1=(47.826582, 14.837569), point2=(48.028885, 14.400000))
s0.Line(point1=(48.028885, 14.400000), point2=(47.556339, 13.380949))
s0.Line(point1=(47.556339, 13.380949), point2=(45.872028, 12.044048))
s0.Line(point1=(45.872028, 12.044048), point2=(45.407513, 13.040070))
s0.Line(point1=(45.407513, 13.040070), point2=(45.752767, 14.508517))
s0.Line(point1=(45.752767, 14.508517), point2=(46.937525, 15.179672))
s0.Line(point1=(46.937525, 15.179672), point2=(47.826582, 14.837569))
s0.Line(point1=(47.573418, 14.562431), point2=(47.671115, 14.400000))
s0.Line(point1=(47.671115, 14.400000), point2=(47.243661, 13.619051))
s0.Line(point1=(47.243661, 13.619051), point2=(45.927972, 12.255952))
s0.Line(point1=(45.927972, 12.255952), point2=(45.792487, 13.059930))
s0.Line(point1=(45.792487, 13.059930), point2=(46.047233, 14.291483))
s0.Line(point1=(46.047233, 14.291483), point2=(46.962475, 14.820328))
s0.Line(point1=(46.962475, 14.820328), point2=(47.573418, 14.562431))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(48.150000, 48.000000), point2=(48.450000, 46.200000))
s0.Line(point1=(48.450000, 46.200000), point2=(47.850000, 46.050000))
s0.Line(point1=(47.850000, 46.050000), point2=(47.850000, 45.150000))
s0.Line(point1=(47.850000, 45.150000), point2=(46.200000, 45.450000))
s0.Line(point1=(46.200000, 45.450000), point2=(45.900000, 45.750000))
s0.Line(point1=(45.900000, 45.750000), point2=(45.900000, 46.650000))
s0.Line(point1=(45.900000, 46.650000), point2=(46.350000, 47.250000))
s0.Line(point1=(46.350000, 47.250000), point2=(47.400000, 47.400000))
s0.Line(point1=(47.400000, 47.400000), point2=(47.550000, 48.000000))
s0.Line(point1=(47.550000, 48.000000), point2=(48.150000, 48.000000))
s0.Line(point1=(48.248639, 48.116440), point2=(48.572893, 46.119426))
s0.Line(point1=(48.572893, 46.119426), point2=(47.974254, 45.952986))
s0.Line(point1=(47.974254, 45.952986), point2=(47.932111, 45.051613))
s0.Line(point1=(47.932111, 45.051613), point2=(46.111401, 45.280902))
s0.Line(point1=(46.111401, 45.280902), point2=(45.729289, 45.679289))
s0.Line(point1=(45.729289, 45.679289), point2=(45.720000, 46.710000))
s0.Line(point1=(45.720000, 46.710000), point2=(46.255858, 47.408995))
s0.Line(point1=(46.255858, 47.408995), point2=(47.288844, 47.523249))
s0.Line(point1=(47.288844, 47.523249), point2=(47.452986, 48.124254))
s0.Line(point1=(47.452986, 48.124254), point2=(48.248639, 48.116440))
s0.Line(point1=(48.051361, 47.883560), point2=(48.327107, 46.280574))
s0.Line(point1=(48.327107, 46.280574), point2=(47.725746, 46.147014))
s0.Line(point1=(47.725746, 46.147014), point2=(47.767889, 45.248387))
s0.Line(point1=(47.767889, 45.248387), point2=(46.288599, 45.619098))
s0.Line(point1=(46.288599, 45.619098), point2=(46.070711, 45.820711))
s0.Line(point1=(46.070711, 45.820711), point2=(46.080000, 46.590000))
s0.Line(point1=(46.080000, 46.590000), point2=(46.444142, 47.091005))
s0.Line(point1=(46.444142, 47.091005), point2=(47.511156, 47.276751))
s0.Line(point1=(47.511156, 47.276751), point2=(47.647014, 47.875746))
s0.Line(point1=(47.647014, 47.875746), point2=(48.051361, 47.883560))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(50.850000, 29.850000), point2=(50.550000, 25.800000))
s0.Line(point1=(50.550000, 25.800000), point2=(49.950000, 25.200000))
s0.Line(point1=(49.950000, 25.200000), point2=(49.350000, 23.700000))
s0.Line(point1=(49.350000, 23.700000), point2=(48.000000, 22.350000))
s0.Line(point1=(48.000000, 22.350000), point2=(46.050000, 22.200000))
s0.Line(point1=(46.050000, 22.200000), point2=(46.650000, 24.300000))
s0.Line(point1=(46.650000, 24.300000), point2=(48.900000, 27.150000))
s0.Line(point1=(48.900000, 27.150000), point2=(49.200000, 28.350000))
s0.Line(point1=(49.200000, 28.350000), point2=(49.800000, 28.650000))
s0.Line(point1=(49.800000, 28.650000), point2=(50.400000, 29.850000))
s0.Line(point1=(50.400000, 29.850000), point2=(50.850000, 29.850000))
s0.Line(point1=(50.949727, 29.942613), point2=(50.720437, 25.721902))
s0.Line(point1=(50.720437, 25.721902), point2=(50.113558, 25.092150))
s0.Line(point1=(50.113558, 25.092150), point2=(49.513558, 23.592150))
s0.Line(point1=(49.513558, 23.592150), point2=(48.078380, 22.179584))
s0.Line(point1=(48.078380, 22.179584), point2=(45.961517, 22.127767))
s0.Line(point1=(45.961517, 22.127767), point2=(46.475359, 24.389437))
s0.Line(point1=(46.475359, 24.389437), point2=(48.724497, 27.236218))
s0.Line(point1=(48.724497, 27.236218), point2=(49.058264, 28.463696))
s0.Line(point1=(49.058264, 28.463696), point2=(49.665836, 28.784164))
s0.Line(point1=(49.665836, 28.784164), point2=(50.310557, 29.994721))
s0.Line(point1=(50.310557, 29.994721), point2=(50.949727, 29.942613))
s0.Line(point1=(50.750273, 29.757387), point2=(50.379563, 25.878098))
s0.Line(point1=(50.379563, 25.878098), point2=(49.786442, 25.307850))
s0.Line(point1=(49.786442, 25.307850), point2=(49.186442, 23.807850))
s0.Line(point1=(49.186442, 23.807850), point2=(47.921620, 22.520416))
s0.Line(point1=(47.921620, 22.520416), point2=(46.138483, 22.272233))
s0.Line(point1=(46.138483, 22.272233), point2=(46.824641, 24.210563))
s0.Line(point1=(46.824641, 24.210563), point2=(49.075503, 27.063782))
s0.Line(point1=(49.075503, 27.063782), point2=(49.341736, 28.236304))
s0.Line(point1=(49.341736, 28.236304), point2=(49.934164, 28.515836))
s0.Line(point1=(49.934164, 28.515836), point2=(50.489443, 29.705279))
s0.Line(point1=(50.489443, 29.705279), point2=(50.750273, 29.757387))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(46.200000, 20.850000), point2=(47.250000, 20.850000))
s0.Line(point1=(47.250000, 20.850000), point2=(47.700000, 21.300000))
s0.Line(point1=(47.700000, 21.300000), point2=(48.300000, 21.300000))
s0.Line(point1=(48.300000, 21.300000), point2=(48.150000, 20.400000))
s0.Line(point1=(48.150000, 20.400000), point2=(48.450000, 20.400000))
s0.Line(point1=(48.450000, 20.400000), point2=(48.900000, 19.500000))
s0.Line(point1=(48.900000, 19.500000), point2=(48.900000, 18.600000))
s0.Line(point1=(48.900000, 18.600000), point2=(48.000000, 18.450000))
s0.Line(point1=(48.000000, 18.450000), point2=(48.000000, 18.900000))
s0.Line(point1=(48.000000, 18.900000), point2=(47.100000, 19.800000))
s0.Line(point1=(47.100000, 19.800000), point2=(46.350000, 20.100000))
s0.Line(point1=(46.350000, 20.100000), point2=(46.200000, 20.850000))
s0.Line(point1=(46.101942, 20.930388), point2=(47.179289, 21.020711))
s0.Line(point1=(47.179289, 21.020711), point2=(47.629289, 21.470711))
s0.Line(point1=(47.629289, 21.470711), point2=(48.398639, 21.383560))
s0.Line(point1=(48.398639, 21.383560), point2=(48.248639, 20.483560))
s0.Line(point1=(48.248639, 20.483560), point2=(48.539443, 20.544721))
s0.Line(point1=(48.539443, 20.544721), point2=(49.089443, 19.544721))
s0.Line(point1=(49.089443, 19.544721), point2=(49.016440, 18.501361))
s0.Line(point1=(49.016440, 18.501361), point2=(47.916440, 18.351361))
s0.Line(point1=(47.916440, 18.351361), point2=(47.829289, 18.829289))
s0.Line(point1=(47.829289, 18.829289), point2=(46.992150, 19.636442))
s0.Line(point1=(46.992150, 19.636442), point2=(46.214803, 19.987541))
s0.Line(point1=(46.214803, 19.987541), point2=(46.101942, 20.930388))
s0.Line(point1=(46.298058, 20.769612), point2=(47.320711, 20.679289))
s0.Line(point1=(47.320711, 20.679289), point2=(47.770711, 21.129289))
s0.Line(point1=(47.770711, 21.129289), point2=(48.201361, 21.216440))
s0.Line(point1=(48.201361, 21.216440), point2=(48.051361, 20.316440))
s0.Line(point1=(48.051361, 20.316440), point2=(48.360557, 20.255279))
s0.Line(point1=(48.360557, 20.255279), point2=(48.710557, 19.455279))
s0.Line(point1=(48.710557, 19.455279), point2=(48.783560, 18.698639))
s0.Line(point1=(48.783560, 18.698639), point2=(48.083560, 18.548639))
s0.Line(point1=(48.083560, 18.548639), point2=(48.170711, 18.970711))
s0.Line(point1=(48.170711, 18.970711), point2=(47.207850, 19.963558))
s0.Line(point1=(47.207850, 19.963558), point2=(46.485197, 20.212459))
s0.Line(point1=(46.485197, 20.212459), point2=(46.298058, 20.769612))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(48.900000, 40.050000), point2=(49.200000, 39.450000))
s0.Line(point1=(49.200000, 39.450000), point2=(49.350000, 36.600000))
s0.Line(point1=(49.350000, 36.600000), point2=(48.900000, 36.600000))
s0.Line(point1=(48.900000, 36.600000), point2=(48.600000, 37.200000))
s0.Line(point1=(48.600000, 37.200000), point2=(48.150000, 37.050000))
s0.Line(point1=(48.150000, 37.050000), point2=(48.000000, 36.600000))
s0.Line(point1=(48.000000, 36.600000), point2=(47.100000, 36.600000))
s0.Line(point1=(47.100000, 36.600000), point2=(46.950000, 37.950000))
s0.Line(point1=(46.950000, 37.950000), point2=(47.550000, 38.400000))
s0.Line(point1=(47.550000, 38.400000), point2=(47.850000, 39.600000))
s0.Line(point1=(47.850000, 39.600000), point2=(48.900000, 40.050000))
s0.Line(point1=(48.950051, 40.186636), point2=(49.389305, 39.499977))
s0.Line(point1=(49.389305, 39.499977), point2=(49.449862, 36.505256))
s0.Line(point1=(49.449862, 36.505256), point2=(48.810557, 36.455279))
s0.Line(point1=(48.810557, 36.455279), point2=(48.542180, 37.060410))
s0.Line(point1=(48.542180, 37.060410), point2=(48.276491, 36.923509))
s0.Line(point1=(48.276491, 36.923509), point2=(48.094868, 36.468377))
s0.Line(point1=(48.094868, 36.468377), point2=(47.000612, 36.488957))
s0.Line(point1=(47.000612, 36.488957), point2=(46.790612, 38.018957))
s0.Line(point1=(46.790612, 38.018957), point2=(47.392986, 38.504254))
s0.Line(point1=(47.392986, 38.504254), point2=(47.713594, 39.716168))
s0.Line(point1=(47.713594, 39.716168), point2=(48.950051, 40.186636))
s0.Line(point1=(48.849949, 39.913364), point2=(49.010695, 39.400023))
s0.Line(point1=(49.010695, 39.400023), point2=(49.250138, 36.694744))
s0.Line(point1=(49.250138, 36.694744), point2=(48.989443, 36.744721))
s0.Line(point1=(48.989443, 36.744721), point2=(48.657820, 37.339590))
s0.Line(point1=(48.657820, 37.339590), point2=(48.023509, 37.176491))
s0.Line(point1=(48.023509, 37.176491), point2=(47.905132, 36.731623))
s0.Line(point1=(47.905132, 36.731623), point2=(47.199388, 36.711043))
s0.Line(point1=(47.199388, 36.711043), point2=(47.109388, 37.881043))
s0.Line(point1=(47.109388, 37.881043), point2=(47.707014, 38.295746))
s0.Line(point1=(47.707014, 38.295746), point2=(47.986406, 39.483832))
s0.Line(point1=(47.986406, 39.483832), point2=(48.849949, 39.913364))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(48.300000, 34.050000), point2=(49.500000, 34.050000))
s0.Line(point1=(49.500000, 34.050000), point2=(50.850000, 32.850000))
s0.Line(point1=(50.850000, 32.850000), point2=(50.400000, 32.400000))
s0.Line(point1=(50.400000, 32.400000), point2=(50.400000, 31.500000))
s0.Line(point1=(50.400000, 31.500000), point2=(49.950000, 31.200000))
s0.Line(point1=(49.950000, 31.200000), point2=(48.750000, 31.350000))
s0.Line(point1=(48.750000, 31.350000), point2=(48.000000, 32.550000))
s0.Line(point1=(48.000000, 32.550000), point2=(48.000000, 33.750000))
s0.Line(point1=(48.000000, 33.750000), point2=(48.300000, 34.050000))
s0.Line(point1=(48.229289, 34.220711), point2=(49.566436, 34.224741))
s0.Line(point1=(49.566436, 34.224741), point2=(50.987147, 32.854030))
s0.Line(point1=(50.987147, 32.854030), point2=(50.570711, 32.329289))
s0.Line(point1=(50.570711, 32.329289), point2=(50.555470, 31.416795))
s0.Line(point1=(50.555470, 31.416795), point2=(49.993067, 31.017567))
s0.Line(point1=(49.993067, 31.017567), point2=(48.652797, 31.197772))
s0.Line(point1=(48.652797, 31.197772), point2=(47.815200, 32.497000))
s0.Line(point1=(47.815200, 32.497000), point2=(47.829289, 33.820711))
s0.Line(point1=(47.829289, 33.820711), point2=(48.229289, 34.220711))
s0.Line(point1=(48.370711, 33.879289), point2=(49.433564, 33.875259))
s0.Line(point1=(49.433564, 33.875259), point2=(50.712853, 32.845970))
s0.Line(point1=(50.712853, 32.845970), point2=(50.229289, 32.470711))
s0.Line(point1=(50.229289, 32.470711), point2=(50.244530, 31.583205))
s0.Line(point1=(50.244530, 31.583205), point2=(49.906933, 31.382433))
s0.Line(point1=(49.906933, 31.382433), point2=(48.847203, 31.502228))
s0.Line(point1=(48.847203, 31.502228), point2=(48.184800, 32.603000))
s0.Line(point1=(48.184800, 32.603000), point2=(48.170711, 33.679289))
s0.Line(point1=(48.170711, 33.679289), point2=(48.370711, 33.879289))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(48.000000, 17.100000), point2=(49.650000, 17.100000))
s0.Line(point1=(49.650000, 17.100000), point2=(49.950000, 16.800000))
s0.Line(point1=(49.950000, 16.800000), point2=(50.100000, 15.900000))
s0.Line(point1=(50.100000, 15.900000), point2=(49.800000, 15.750000))
s0.Line(point1=(49.800000, 15.750000), point2=(50.100000, 15.600000))
s0.Line(point1=(50.100000, 15.600000), point2=(50.100000, 15.000000))
s0.Line(point1=(50.100000, 15.000000), point2=(51.150000, 14.700000))
s0.Line(point1=(51.150000, 14.700000), point2=(51.600000, 13.200000))
s0.Line(point1=(51.600000, 13.200000), point2=(52.050000, 13.050000))
s0.Line(point1=(52.050000, 13.050000), point2=(53.250000, 11.250000))
s0.Line(point1=(53.250000, 11.250000), point2=(52.950000, 10.200000))
s0.Line(point1=(52.950000, 10.200000), point2=(52.050000, 10.200000))
s0.Line(point1=(52.050000, 10.200000), point2=(51.600000, 10.950000))
s0.Line(point1=(51.600000, 10.950000), point2=(51.300000, 10.950000))
s0.Line(point1=(51.300000, 10.950000), point2=(50.850000, 12.150000))
s0.Line(point1=(50.850000, 12.150000), point2=(49.350000, 13.950000))
s0.Line(point1=(49.350000, 13.950000), point2=(48.750000, 15.600000))
s0.Line(point1=(48.750000, 15.600000), point2=(48.000000, 16.350000))
s0.Line(point1=(48.000000, 16.350000), point2=(48.000000, 17.100000))
s0.Line(point1=(47.900000, 17.200000), point2=(49.720711, 17.270711))
s0.Line(point1=(49.720711, 17.270711), point2=(50.119350, 16.887151))
s0.Line(point1=(50.119350, 16.887151), point2=(50.243361, 15.826997))
s0.Line(point1=(50.243361, 15.826997), point2=(49.889443, 15.750000))
s0.Line(point1=(49.889443, 15.750000), point2=(50.244721, 15.689443))
s0.Line(point1=(50.244721, 15.689443), point2=(50.227472, 15.096152))
s0.Line(point1=(50.227472, 15.096152), point2=(51.273255, 14.824887))
s0.Line(point1=(51.273255, 14.824887), point2=(51.727405, 13.323603))
s0.Line(point1=(51.727405, 13.323603), point2=(52.164828, 13.200338))
s0.Line(point1=(52.164828, 13.200338), point2=(53.429357, 11.277998))
s0.Line(point1=(53.429357, 11.277998), point2=(53.046152, 10.072528))
s0.Line(point1=(53.046152, 10.072528), point2=(51.964251, 10.048550))
s0.Line(point1=(51.964251, 10.048550), point2=(51.514251, 10.798550))
s0.Line(point1=(51.514251, 10.798550), point2=(51.206367, 10.814888))
s0.Line(point1=(51.206367, 10.814888), point2=(50.679545, 12.050869))
s0.Line(point1=(50.679545, 12.050869), point2=(49.179199, 13.851807))
s0.Line(point1=(49.179199, 13.851807), point2=(48.585310, 15.495115))
s0.Line(point1=(48.585310, 15.495115), point2=(47.829289, 16.279289))
s0.Line(point1=(47.829289, 16.279289), point2=(47.900000, 17.200000))
s0.Line(point1=(48.100000, 17.000000), point2=(49.579289, 16.929289))
s0.Line(point1=(49.579289, 16.929289), point2=(49.780650, 16.712849))
s0.Line(point1=(49.780650, 16.712849), point2=(49.956639, 15.973003))
s0.Line(point1=(49.956639, 15.973003), point2=(49.710557, 15.750000))
s0.Line(point1=(49.710557, 15.750000), point2=(49.955279, 15.510557))
s0.Line(point1=(49.955279, 15.510557), point2=(49.972528, 14.903848))
s0.Line(point1=(49.972528, 14.903848), point2=(51.026745, 14.575113))
s0.Line(point1=(51.026745, 14.575113), point2=(51.472595, 13.076397))
s0.Line(point1=(51.472595, 13.076397), point2=(51.935172, 12.899662))
s0.Line(point1=(51.935172, 12.899662), point2=(53.070643, 11.222002))
s0.Line(point1=(53.070643, 11.222002), point2=(52.853848, 10.327472))
s0.Line(point1=(52.853848, 10.327472), point2=(52.135749, 10.351450))
s0.Line(point1=(52.135749, 10.351450), point2=(51.685749, 11.101450))
s0.Line(point1=(51.685749, 11.101450), point2=(51.393633, 11.085112))
s0.Line(point1=(51.393633, 11.085112), point2=(51.020455, 12.249131))
s0.Line(point1=(51.020455, 12.249131), point2=(49.520801, 14.048193))
s0.Line(point1=(49.520801, 14.048193), point2=(48.914690, 15.704885))
s0.Line(point1=(48.914690, 15.704885), point2=(48.170711, 16.420711))
s0.Line(point1=(48.170711, 16.420711), point2=(48.100000, 17.000000))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(51.750000, 22.200000), point2=(51.150000, 21.000000))
s0.Line(point1=(51.150000, 21.000000), point2=(51.150000, 20.250000))
s0.Line(point1=(51.150000, 20.250000), point2=(50.550000, 19.800000))
s0.Line(point1=(50.550000, 19.800000), point2=(49.650000, 19.950000))
s0.Line(point1=(49.650000, 19.950000), point2=(48.900000, 21.150000))
s0.Line(point1=(48.900000, 21.150000), point2=(49.050000, 22.050000))
s0.Line(point1=(49.050000, 22.050000), point2=(49.500000, 22.500000))
s0.Line(point1=(49.500000, 22.500000), point2=(51.750000, 22.200000))
s0.Line(point1=(51.852659, 22.254401), point2=(51.339443, 20.955279))
s0.Line(point1=(51.339443, 20.955279), point2=(51.310000, 20.170000))
s0.Line(point1=(51.310000, 20.170000), point2=(50.593560, 19.621361))
s0.Line(point1=(50.593560, 19.621361), point2=(49.548760, 19.798361))
s0.Line(point1=(49.548760, 19.798361), point2=(48.716561, 21.113440))
s0.Line(point1=(48.716561, 21.113440), point2=(48.880650, 22.137151))
s0.Line(point1=(48.880650, 22.137151), point2=(49.442506, 22.669833))
s0.Line(point1=(49.442506, 22.669833), point2=(51.852659, 22.254401))
s0.Line(point1=(51.647341, 22.145599), point2=(50.960557, 21.044721))
s0.Line(point1=(50.960557, 21.044721), point2=(50.990000, 20.330000))
s0.Line(point1=(50.990000, 20.330000), point2=(50.506440, 19.978639))
s0.Line(point1=(50.506440, 19.978639), point2=(49.751240, 20.101639))
s0.Line(point1=(49.751240, 20.101639), point2=(49.083439, 21.186560))
s0.Line(point1=(49.083439, 21.186560), point2=(49.219350, 21.962849))
s0.Line(point1=(49.219350, 21.962849), point2=(49.557494, 22.330167))
s0.Line(point1=(49.557494, 22.330167), point2=(51.647341, 22.145599))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(50.850000, 47.700000), point2=(50.400000, 46.800000))
s0.Line(point1=(50.400000, 46.800000), point2=(49.200000, 46.800000))
s0.Line(point1=(49.200000, 46.800000), point2=(49.200000, 47.100000))
s0.Line(point1=(49.200000, 47.100000), point2=(49.950000, 47.250000))
s0.Line(point1=(49.950000, 47.250000), point2=(50.400000, 47.850000))
s0.Line(point1=(50.400000, 47.850000), point2=(50.850000, 47.700000))
s0.Line(point1=(50.971065, 47.750147), point2=(50.489443, 46.655279))
s0.Line(point1=(50.489443, 46.655279), point2=(49.100000, 46.700000))
s0.Line(point1=(49.100000, 46.700000), point2=(49.080388, 47.198058))
s0.Line(point1=(49.080388, 47.198058), point2=(49.850388, 47.408058))
s0.Line(point1=(49.850388, 47.408058), point2=(50.351623, 48.004868))
s0.Line(point1=(50.351623, 48.004868), point2=(50.971065, 47.750147))
s0.Line(point1=(50.728935, 47.649853), point2=(50.310557, 46.944721))
s0.Line(point1=(50.310557, 46.944721), point2=(49.300000, 46.900000))
s0.Line(point1=(49.300000, 46.900000), point2=(49.319612, 47.001942))
s0.Line(point1=(49.319612, 47.001942), point2=(50.049612, 47.091942))
s0.Line(point1=(50.049612, 47.091942), point2=(50.448377, 47.695132))
s0.Line(point1=(50.448377, 47.695132), point2=(50.728935, 47.649853))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(51.450000, 46.800000), point2=(50.400000, 45.450000))
s0.Line(point1=(50.400000, 45.450000), point2=(49.500000, 45.600000))
s0.Line(point1=(49.500000, 45.600000), point2=(51.000000, 46.950000))
s0.Line(point1=(51.000000, 46.950000), point2=(51.450000, 46.800000))
s0.Line(point1=(51.560558, 46.833474), point2=(50.462495, 45.289967))
s0.Line(point1=(50.462495, 45.289967), point2=(49.416664, 45.575690))
s0.Line(point1=(49.416664, 45.575690), point2=(50.964726, 47.119198))
s0.Line(point1=(50.964726, 47.119198), point2=(51.560558, 46.833474))
s0.Line(point1=(51.339442, 46.766526), point2=(50.337505, 45.610033))
s0.Line(point1=(50.337505, 45.610033), point2=(49.583336, 45.624310))
s0.Line(point1=(49.583336, 45.624310), point2=(51.035274, 46.780802))
s0.Line(point1=(51.035274, 46.780802), point2=(51.339442, 46.766526))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(49.800000, 42.300000), point2=(50.400000, 42.150000))
s0.Line(point1=(50.400000, 42.150000), point2=(50.850000, 40.950000))
s0.Line(point1=(50.850000, 40.950000), point2=(50.700000, 39.150000))
s0.Line(point1=(50.700000, 39.150000), point2=(50.250000, 39.150000))
s0.Line(point1=(50.250000, 39.150000), point2=(49.800000, 40.050000))
s0.Line(point1=(49.800000, 40.050000), point2=(49.800000, 42.300000))
s0.Line(point1=(49.724254, 42.397014), point2=(50.517886, 42.282127))
s0.Line(point1=(50.517886, 42.282127), point2=(51.043287, 40.976808))
s0.Line(point1=(51.043287, 40.976808), point2=(50.799655, 39.041695))
s0.Line(point1=(50.799655, 39.041695), point2=(50.160557, 39.005279))
s0.Line(point1=(50.160557, 39.005279), point2=(49.610557, 40.005279))
s0.Line(point1=(49.610557, 40.005279), point2=(49.724254, 42.397014))
s0.Line(point1=(49.875746, 42.202986), point2=(50.282114, 42.017873))
s0.Line(point1=(50.282114, 42.017873), point2=(50.656713, 40.923192))
s0.Line(point1=(50.656713, 40.923192), point2=(50.600345, 39.258305))
s0.Line(point1=(50.600345, 39.258305), point2=(50.339443, 39.294721))
s0.Line(point1=(50.339443, 39.294721), point2=(49.989443, 40.094721))
s0.Line(point1=(49.989443, 40.094721), point2=(49.875746, 42.202986))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(50.100000, 37.050000), point2=(51.000000, 37.950000))
s0.Line(point1=(51.000000, 37.950000), point2=(51.150000, 38.700000))
s0.Line(point1=(51.150000, 38.700000), point2=(51.750000, 38.700000))
s0.Line(point1=(51.750000, 38.700000), point2=(53.700000, 37.200000))
s0.Line(point1=(53.700000, 37.200000), point2=(53.850000, 35.850000))
s0.Line(point1=(53.850000, 35.850000), point2=(52.350000, 35.700000))
s0.Line(point1=(52.350000, 35.700000), point2=(50.250000, 36.450000))
s0.Line(point1=(50.250000, 36.450000), point2=(50.100000, 37.050000))
s0.Line(point1=(49.932275, 37.096457), point2=(50.831231, 38.040322))
s0.Line(point1=(50.831231, 38.040322), point2=(51.051942, 38.819612))
s0.Line(point1=(51.051942, 38.819612), point2=(51.810971, 38.879262))
s0.Line(point1=(51.810971, 38.879262), point2=(53.860359, 37.290306))
s0.Line(point1=(53.860359, 37.290306), point2=(53.959339, 35.761539))
s0.Line(point1=(53.959339, 35.761539), point2=(52.326317, 35.506322))
s0.Line(point1=(52.326317, 35.506322), point2=(50.119352, 36.331572))
s0.Line(point1=(50.119352, 36.331572), point2=(49.932275, 37.096457))
s0.Line(point1=(50.267725, 37.003543), point2=(51.168769, 37.859678))
s0.Line(point1=(51.168769, 37.859678), point2=(51.248058, 38.580388))
s0.Line(point1=(51.248058, 38.580388), point2=(51.689029, 38.520738))
s0.Line(point1=(51.689029, 38.520738), point2=(53.539641, 37.109694))
s0.Line(point1=(53.539641, 37.109694), point2=(53.740661, 35.938461))
s0.Line(point1=(53.740661, 35.938461), point2=(52.373683, 35.893678))
s0.Line(point1=(52.373683, 35.893678), point2=(50.380648, 36.568428))
s0.Line(point1=(50.380648, 36.568428), point2=(50.267725, 37.003543))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(52.950000, 18.600000), point2=(52.950000, 18.000000))
s0.Line(point1=(52.950000, 18.000000), point2=(52.350000, 17.550000))
s0.Line(point1=(52.350000, 17.550000), point2=(50.550000, 17.550000))
s0.Line(point1=(50.550000, 17.550000), point2=(50.100000, 18.000000))
s0.Line(point1=(50.100000, 18.000000), point2=(50.700000, 19.200000))
s0.Line(point1=(50.700000, 19.200000), point2=(51.900000, 19.350000))
s0.Line(point1=(51.900000, 19.350000), point2=(52.950000, 18.600000))
s0.Line(point1=(53.108124, 18.681373), point2=(53.110000, 17.920000))
s0.Line(point1=(53.110000, 17.920000), point2=(52.410000, 17.370000))
s0.Line(point1=(52.410000, 17.370000), point2=(50.479289, 17.379289))
s0.Line(point1=(50.479289, 17.379289), point2=(49.939847, 17.974011))
s0.Line(point1=(49.939847, 17.974011), point2=(50.598154, 19.343949))
s0.Line(point1=(50.598154, 19.343949), point2=(51.945720, 19.530601))
s0.Line(point1=(51.945720, 19.530601), point2=(53.108124, 18.681373))
s0.Line(point1=(52.791876, 18.518627), point2=(52.790000, 18.080000))
s0.Line(point1=(52.790000, 18.080000), point2=(52.290000, 17.730000))
s0.Line(point1=(52.290000, 17.730000), point2=(50.620711, 17.720711))
s0.Line(point1=(50.620711, 17.720711), point2=(50.260153, 18.025989))
s0.Line(point1=(50.260153, 18.025989), point2=(50.801846, 19.056051))
s0.Line(point1=(50.801846, 19.056051), point2=(51.854280, 19.169399))
s0.Line(point1=(51.854280, 19.169399), point2=(52.791876, 18.518627))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
print 160
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(51.600000, 4.050000), point2=(52.050000, 4.050000))
s0.Line(point1=(52.050000, 4.050000), point2=(52.950000, 3.150000))
s0.Line(point1=(52.950000, 3.150000), point2=(53.100000, 1.200000))
s0.Line(point1=(53.100000, 1.200000), point2=(53.700000, 0.750000))
s0.Line(point1=(53.700000, 0.750000), point2=(54.000000, 0.000000))
s0.Line(point1=(54.000000, 0.000000), point2=(50.700000, 0.000000))
s0.Line(point1=(50.700000, 0.000000), point2=(50.700000, 0.600000))
s0.Line(point1=(50.700000, 0.600000), point2=(51.450000, 1.050000))
s0.Line(point1=(51.450000, 1.050000), point2=(51.600000, 4.050000))
s0.Line(point1=(51.500125, 4.154994), point2=(52.120711, 4.220711))
s0.Line(point1=(52.120711, 4.220711), point2=(53.120416, 3.228380))
s0.Line(point1=(53.120416, 3.228380), point2=(53.259705, 1.287670))
s0.Line(point1=(53.259705, 1.287670), point2=(53.852848, 0.867139))
s0.Line(point1=(53.852848, 0.867139), point2=(54.092848, 0.000000))
s0.Line(point1=(54.092848, 0.000000), point2=(50.600000, 0.000000))
s0.Line(point1=(50.600000, 0.000000), point2=(50.548550, 0.685749))
s0.Line(point1=(50.548550, 0.685749), point2=(51.298675, 1.140743))
s0.Line(point1=(51.298675, 1.140743), point2=(51.500125, 4.154994))
s0.Line(point1=(51.699875, 3.945006), point2=(51.979289, 3.879289))
s0.Line(point1=(51.979289, 3.879289), point2=(52.779584, 3.071620))
s0.Line(point1=(52.779584, 3.071620), point2=(52.940295, 1.112330))
s0.Line(point1=(52.940295, 1.112330), point2=(53.547152, 0.632861))
s0.Line(point1=(53.547152, 0.632861), point2=(53.907152, 0.000000))
s0.Line(point1=(53.907152, 0.000000), point2=(50.800000, 0.000000))
s0.Line(point1=(50.800000, 0.000000), point2=(50.851450, 0.514251))
s0.Line(point1=(50.851450, 0.514251), point2=(51.601325, 0.959257))
s0.Line(point1=(51.601325, 0.959257), point2=(51.699875, 3.945006))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(50.850000, 52.050000), point2=(53.400000, 52.050000))
s0.Line(point1=(53.400000, 52.050000), point2=(54.000000, 51.600000))
s0.Line(point1=(54.000000, 51.600000), point2=(54.000000, 51.150000))
s0.Line(point1=(54.000000, 51.150000), point2=(52.950000, 50.250000))
s0.Line(point1=(52.950000, 50.250000), point2=(52.500000, 50.250000))
s0.Line(point1=(52.500000, 50.250000), point2=(51.000000, 51.150000))
s0.Line(point1=(51.000000, 51.150000), point2=(50.850000, 52.050000))
s0.Line(point1=(50.751361, 52.133560), point2=(53.460000, 52.230000))
s0.Line(point1=(53.460000, 52.230000), point2=(54.160000, 51.680000))
s0.Line(point1=(54.160000, 51.680000), point2=(54.165079, 51.074074))
s0.Line(point1=(54.165079, 51.074074), point2=(53.015079, 50.074074))
s0.Line(point1=(53.015079, 50.074074), point2=(52.448550, 50.064251))
s0.Line(point1=(52.448550, 50.064251), point2=(50.849911, 51.047811))
s0.Line(point1=(50.849911, 51.047811), point2=(50.751361, 52.133560))
s0.Line(point1=(50.948639, 51.966440), point2=(53.340000, 51.870000))
s0.Line(point1=(53.340000, 51.870000), point2=(53.840000, 51.520000))
s0.Line(point1=(53.840000, 51.520000), point2=(53.834921, 51.225926))
s0.Line(point1=(53.834921, 51.225926), point2=(52.884921, 50.425926))
s0.Line(point1=(52.884921, 50.425926), point2=(52.551450, 50.435749))
s0.Line(point1=(52.551450, 50.435749), point2=(51.150089, 51.252189))
s0.Line(point1=(51.150089, 51.252189), point2=(50.948639, 51.966440))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(51.000000, 44.400000), point2=(53.250000, 44.400000))
s0.Line(point1=(53.250000, 44.400000), point2=(54.450000, 43.350000))
s0.Line(point1=(54.450000, 43.350000), point2=(54.450000, 42.450000))
s0.Line(point1=(54.450000, 42.450000), point2=(51.450000, 43.350000))
s0.Line(point1=(51.450000, 43.350000), point2=(51.000000, 43.650000))
s0.Line(point1=(51.000000, 43.650000), point2=(51.000000, 44.400000))
s0.Line(point1=(50.900000, 44.500000), point2=(53.315850, 44.575258))
s0.Line(point1=(53.315850, 44.575258), point2=(54.615850, 43.425258))
s0.Line(point1=(54.615850, 43.425258), point2=(54.521265, 42.354217))
s0.Line(point1=(54.521265, 42.354217), point2=(51.365795, 43.171012))
s0.Line(point1=(51.365795, 43.171012), point2=(50.844530, 43.566795))
s0.Line(point1=(50.844530, 43.566795), point2=(50.900000, 44.500000))
s0.Line(point1=(51.100000, 44.300000), point2=(53.184150, 44.224742))
s0.Line(point1=(53.184150, 44.224742), point2=(54.284150, 43.274742))
s0.Line(point1=(54.284150, 43.274742), point2=(54.378735, 42.545783))
s0.Line(point1=(54.378735, 42.545783), point2=(51.534205, 43.528988))
s0.Line(point1=(51.534205, 43.528988), point2=(51.155470, 43.733205))
s0.Line(point1=(51.155470, 43.733205), point2=(51.100000, 44.300000))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(51.300000, 50.250000), point2=(52.950000, 49.050000))
s0.Line(point1=(52.950000, 49.050000), point2=(53.250000, 48.450000))
s0.Line(point1=(53.250000, 48.450000), point2=(53.100000, 48.000000))
s0.Line(point1=(53.100000, 48.000000), point2=(52.650000, 48.000000))
s0.Line(point1=(52.650000, 48.000000), point2=(51.450000, 49.050000))
s0.Line(point1=(51.450000, 49.050000), point2=(51.300000, 50.250000))
s0.Line(point1=(51.259589, 50.318470), point2=(53.098260, 49.175595))
s0.Line(point1=(53.098260, 49.175595), point2=(53.434311, 48.463099))
s0.Line(point1=(53.434311, 48.463099), point2=(53.194868, 47.868377))
s0.Line(point1=(53.194868, 47.868377), point2=(52.584150, 47.824742))
s0.Line(point1=(52.584150, 47.824742), point2=(51.284922, 48.962339))
s0.Line(point1=(51.284922, 48.962339), point2=(51.259589, 50.318470))
s0.Line(point1=(51.340411, 50.181530), point2=(52.801740, 48.924405))
s0.Line(point1=(52.801740, 48.924405), point2=(53.065689, 48.436901))
s0.Line(point1=(53.065689, 48.436901), point2=(53.005132, 48.131623))
s0.Line(point1=(53.005132, 48.131623), point2=(52.715850, 48.175258))
s0.Line(point1=(52.715850, 48.175258), point2=(51.615078, 49.137661))
s0.Line(point1=(51.615078, 49.137661), point2=(51.340411, 50.181530))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(53.700000, 41.700000), point2=(52.800000, 40.650000))
s0.Line(point1=(52.800000, 40.650000), point2=(51.300000, 40.800000))
s0.Line(point1=(51.300000, 40.800000), point2=(52.500000, 42.150000))
s0.Line(point1=(52.500000, 42.150000), point2=(53.100000, 42.150000))
s0.Line(point1=(53.100000, 42.150000), point2=(53.700000, 41.700000))
s0.Line(point1=(53.835926, 41.714921), point2=(52.865975, 40.485417))
s0.Line(point1=(52.865975, 40.485417), point2=(51.215309, 40.766933))
s0.Line(point1=(51.215309, 40.766933), point2=(52.425259, 42.316436))
s0.Line(point1=(52.425259, 42.316436), point2=(53.160000, 42.330000))
s0.Line(point1=(53.160000, 42.330000), point2=(53.835926, 41.714921))
s0.Line(point1=(53.564074, 41.685079), point2=(52.734025, 40.814583))
s0.Line(point1=(52.734025, 40.814583), point2=(51.384691, 40.833067))
s0.Line(point1=(51.384691, 40.833067), point2=(52.574741, 41.983564))
s0.Line(point1=(52.574741, 41.983564), point2=(53.040000, 41.970000))
s0.Line(point1=(53.040000, 41.970000), point2=(53.564074, 41.685079))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(53.250000, 34.650000), point2=(52.800000, 33.600000))
s0.Line(point1=(52.800000, 33.600000), point2=(53.100000, 30.150000))
s0.Line(point1=(53.100000, 30.150000), point2=(52.950000, 29.850000))
s0.Line(point1=(52.950000, 29.850000), point2=(52.350000, 29.850000))
s0.Line(point1=(52.350000, 29.850000), point2=(51.300000, 31.050000))
s0.Line(point1=(51.300000, 31.050000), point2=(51.300000, 32.550000))
s0.Line(point1=(51.300000, 32.550000), point2=(52.200000, 34.350000))
s0.Line(point1=(52.200000, 34.350000), point2=(53.250000, 34.650000))
s0.Line(point1=(53.314442, 34.706760), point2=(52.991539, 33.569271))
s0.Line(point1=(52.991539, 33.569271), point2=(53.289067, 30.113942))
s0.Line(point1=(53.289067, 30.113942), point2=(53.039443, 29.705279))
s0.Line(point1=(53.039443, 29.705279), point2=(52.274742, 29.684150))
s0.Line(point1=(52.274742, 29.684150), point2=(51.124742, 30.984150))
s0.Line(point1=(51.124742, 30.984150), point2=(51.110557, 32.594721))
s0.Line(point1=(51.110557, 32.594721), point2=(52.083085, 34.490874))
s0.Line(point1=(52.083085, 34.490874), point2=(53.314442, 34.706760))
s0.Line(point1=(53.185558, 34.593240), point2=(52.608461, 33.630729))
s0.Line(point1=(52.608461, 33.630729), point2=(52.910933, 30.186058))
s0.Line(point1=(52.910933, 30.186058), point2=(52.860557, 29.994721))
s0.Line(point1=(52.860557, 29.994721), point2=(52.425258, 30.015850))
s0.Line(point1=(52.425258, 30.015850), point2=(51.475258, 31.115850))
s0.Line(point1=(51.475258, 31.115850), point2=(51.489443, 32.505279))
s0.Line(point1=(51.489443, 32.505279), point2=(52.316915, 34.209126))
s0.Line(point1=(52.316915, 34.209126), point2=(53.185558, 34.593240))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(51.450000, 27.600000), point2=(52.800000, 26.400000))
s0.Line(point1=(52.800000, 26.400000), point2=(52.800000, 25.350000))
s0.Line(point1=(52.800000, 25.350000), point2=(52.200000, 25.200000))
s0.Line(point1=(52.200000, 25.200000), point2=(51.450000, 26.100000))
s0.Line(point1=(51.450000, 26.100000), point2=(51.450000, 27.600000))
s0.Line(point1=(51.416436, 27.674741), point2=(52.966436, 26.474741))
s0.Line(point1=(52.966436, 26.474741), point2=(52.924254, 25.252986))
s0.Line(point1=(52.924254, 25.252986), point2=(52.147431, 25.038967))
s0.Line(point1=(52.147431, 25.038967), point2=(51.273178, 26.035982))
s0.Line(point1=(51.273178, 26.035982), point2=(51.416436, 27.674741))
s0.Line(point1=(51.483564, 27.525259), point2=(52.633564, 26.325259))
s0.Line(point1=(52.633564, 26.325259), point2=(52.675746, 25.447014))
s0.Line(point1=(52.675746, 25.447014), point2=(52.252569, 25.361033))
s0.Line(point1=(52.252569, 25.361033), point2=(51.626822, 26.164018))
s0.Line(point1=(51.626822, 26.164018), point2=(51.483564, 27.525259))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(52.800000, 47.400000), point2=(52.200000, 46.500000))
s0.Line(point1=(52.200000, 46.500000), point2=(51.750000, 46.800000))
s0.Line(point1=(51.750000, 46.800000), point2=(51.750000, 47.550000))
s0.Line(point1=(51.750000, 47.550000), point2=(52.800000, 47.400000))
s0.Line(point1=(52.897347, 47.443525), point2=(52.227735, 46.361325))
s0.Line(point1=(52.227735, 46.361325), point2=(51.594530, 46.716795))
s0.Line(point1=(51.594530, 46.716795), point2=(51.664142, 47.648995))
s0.Line(point1=(51.664142, 47.648995), point2=(52.897347, 47.443525))
s0.Line(point1=(52.702653, 47.356475), point2=(52.172265, 46.638675))
s0.Line(point1=(52.172265, 46.638675), point2=(51.905470, 46.883205))
s0.Line(point1=(51.905470, 46.883205), point2=(51.835858, 47.451005))
s0.Line(point1=(51.835858, 47.451005), point2=(52.702653, 47.356475))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(56.100000, 11.250000), point2=(56.100000, 10.650000))
s0.Line(point1=(56.100000, 10.650000), point2=(56.850000, 9.750000))
s0.Line(point1=(56.850000, 9.750000), point2=(56.850000, 7.350000))
s0.Line(point1=(56.850000, 7.350000), point2=(56.400000, 6.600000))
s0.Line(point1=(56.400000, 6.600000), point2=(55.950000, 6.000000))
s0.Line(point1=(55.950000, 6.000000), point2=(54.750000, 5.400000))
s0.Line(point1=(54.750000, 5.400000), point2=(53.250000, 5.400000))
s0.Line(point1=(53.250000, 5.400000), point2=(52.650000, 4.950000))
s0.Line(point1=(52.650000, 4.950000), point2=(52.500000, 5.400000))
s0.Line(point1=(52.500000, 5.400000), point2=(51.750000, 5.400000))
s0.Line(point1=(51.750000, 5.400000), point2=(51.750000, 6.600000))
s0.Line(point1=(51.750000, 6.600000), point2=(52.650000, 7.350000))
s0.Line(point1=(52.650000, 7.350000), point2=(53.250000, 7.350000))
s0.Line(point1=(53.250000, 7.350000), point2=(53.850000, 8.250000))
s0.Line(point1=(53.850000, 8.250000), point2=(54.300000, 10.650000))
s0.Line(point1=(54.300000, 10.650000), point2=(54.900000, 11.100000))
s0.Line(point1=(54.900000, 11.100000), point2=(56.100000, 11.250000))
s0.Line(point1=(56.187597, 11.349228), point2=(56.276822, 10.714018))
s0.Line(point1=(56.276822, 10.714018), point2=(57.026822, 9.814018))
s0.Line(point1=(57.026822, 9.814018), point2=(57.035749, 7.298550))
s0.Line(point1=(57.035749, 7.298550), point2=(56.565749, 6.488550))
s0.Line(point1=(56.565749, 6.488550), point2=(56.074721, 5.850557))
s0.Line(point1=(56.074721, 5.850557), point2=(54.794721, 5.210557))
s0.Line(point1=(54.794721, 5.210557), point2=(53.310000, 5.220000))
s0.Line(point1=(53.310000, 5.220000), point2=(52.615132, 4.838377))
s0.Line(point1=(52.615132, 4.838377), point2=(52.405132, 5.268377))
s0.Line(point1=(52.405132, 5.268377), point2=(51.650000, 5.300000))
s0.Line(point1=(51.650000, 5.300000), point2=(51.585982, 6.676822))
s0.Line(point1=(51.585982, 6.676822), point2=(52.585982, 7.526822))
s0.Line(point1=(52.585982, 7.526822), point2=(53.166795, 7.505470))
s0.Line(point1=(53.166795, 7.505470), point2=(53.668508, 8.323899))
s0.Line(point1=(53.668508, 8.323899), point2=(54.141713, 10.748429))
s0.Line(point1=(54.141713, 10.748429), point2=(54.827597, 11.279228))
s0.Line(point1=(54.827597, 11.279228), point2=(56.187597, 11.349228))
s0.Line(point1=(56.012403, 11.150772), point2=(55.923178, 10.585982))
s0.Line(point1=(55.923178, 10.585982), point2=(56.673178, 9.685982))
s0.Line(point1=(56.673178, 9.685982), point2=(56.664251, 7.401450))
s0.Line(point1=(56.664251, 7.401450), point2=(56.234251, 6.711450))
s0.Line(point1=(56.234251, 6.711450), point2=(55.825279, 6.149443))
s0.Line(point1=(55.825279, 6.149443), point2=(54.705279, 5.589443))
s0.Line(point1=(54.705279, 5.589443), point2=(53.190000, 5.580000))
s0.Line(point1=(53.190000, 5.580000), point2=(52.684868, 5.061623))
s0.Line(point1=(52.684868, 5.061623), point2=(52.594868, 5.531623))
s0.Line(point1=(52.594868, 5.531623), point2=(51.850000, 5.500000))
s0.Line(point1=(51.850000, 5.500000), point2=(51.914018, 6.523178))
s0.Line(point1=(51.914018, 6.523178), point2=(52.714018, 7.173178))
s0.Line(point1=(52.714018, 7.173178), point2=(53.333205, 7.194530))
s0.Line(point1=(53.333205, 7.194530), point2=(54.031492, 8.176101))
s0.Line(point1=(54.031492, 8.176101), point2=(54.458287, 10.551571))
s0.Line(point1=(54.458287, 10.551571), point2=(54.972403, 10.920772))
s0.Line(point1=(54.972403, 10.920772), point2=(56.012403, 11.150772))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(52.200000, 15.000000), point2=(52.650000, 16.350000))
s0.Line(point1=(52.650000, 16.350000), point2=(53.400000, 17.100000))
s0.Line(point1=(53.400000, 17.100000), point2=(54.000000, 17.100000))
s0.Line(point1=(54.000000, 17.100000), point2=(55.050000, 16.350000))
s0.Line(point1=(55.050000, 16.350000), point2=(55.950000, 16.350000))
s0.Line(point1=(55.950000, 16.350000), point2=(59.400000, 15.000000))
s0.Line(point1=(59.400000, 15.000000), point2=(59.400000, 14.100000))
s0.Line(point1=(59.400000, 14.100000), point2=(58.650000, 13.500000))
s0.Line(point1=(58.650000, 13.500000), point2=(57.750000, 12.000000))
s0.Line(point1=(57.750000, 12.000000), point2=(56.700000, 12.000000))
s0.Line(point1=(56.700000, 12.000000), point2=(55.200000, 12.600000))
s0.Line(point1=(55.200000, 12.600000), point2=(53.550000, 12.600000))
s0.Line(point1=(53.550000, 12.600000), point2=(52.950000, 13.200000))
s0.Line(point1=(52.950000, 13.200000), point2=(52.200000, 15.000000))
s0.Line(point1=(52.012824, 14.993161), point2=(52.484421, 16.452333))
s0.Line(point1=(52.484421, 16.452333), point2=(53.329289, 17.270711))
s0.Line(point1=(53.329289, 17.270711), point2=(54.058124, 17.281373))
s0.Line(point1=(54.058124, 17.281373), point2=(55.108124, 16.531373))
s0.Line(point1=(55.108124, 16.531373), point2=(55.986440, 16.543124))
s0.Line(point1=(55.986440, 16.543124), point2=(59.536440, 15.093124))
s0.Line(point1=(59.536440, 15.093124), point2=(59.562470, 14.021913))
s0.Line(point1=(59.562470, 14.021913), point2=(58.798219, 13.370464))
s0.Line(point1=(58.798219, 13.370464), point2=(57.835749, 11.848550))
s0.Line(point1=(57.835749, 11.848550), point2=(56.662861, 11.807152))
s0.Line(point1=(56.662861, 11.807152), point2=(55.162861, 12.407152))
s0.Line(point1=(55.162861, 12.407152), point2=(53.479289, 12.429289))
s0.Line(point1=(53.479289, 12.429289), point2=(52.786982, 13.090828))
s0.Line(point1=(52.786982, 13.090828), point2=(52.012824, 14.993161))
s0.Line(point1=(52.387176, 15.006839), point2=(52.815579, 16.247667))
s0.Line(point1=(52.815579, 16.247667), point2=(53.470711, 16.929289))
s0.Line(point1=(53.470711, 16.929289), point2=(53.941876, 16.918627))
s0.Line(point1=(53.941876, 16.918627), point2=(54.991876, 16.168627))
s0.Line(point1=(54.991876, 16.168627), point2=(55.913560, 16.156876))
s0.Line(point1=(55.913560, 16.156876), point2=(59.263560, 14.906876))
s0.Line(point1=(59.263560, 14.906876), point2=(59.237530, 14.178087))
s0.Line(point1=(59.237530, 14.178087), point2=(58.501781, 13.629536))
s0.Line(point1=(58.501781, 13.629536), point2=(57.664251, 12.151450))
s0.Line(point1=(57.664251, 12.151450), point2=(56.737139, 12.192848))
s0.Line(point1=(56.737139, 12.192848), point2=(55.237139, 12.792848))
s0.Line(point1=(55.237139, 12.792848), point2=(53.620711, 12.770711))
s0.Line(point1=(53.620711, 12.770711), point2=(53.113018, 13.309172))
s0.Line(point1=(53.113018, 13.309172), point2=(52.387176, 15.006839))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(54.000000, 26.400000), point2=(54.900000, 25.650000))
s0.Line(point1=(54.900000, 25.650000), point2=(54.900000, 25.200000))
s0.Line(point1=(54.900000, 25.200000), point2=(54.600000, 24.750000))
s0.Line(point1=(54.600000, 24.750000), point2=(53.850000, 24.750000))
s0.Line(point1=(53.850000, 24.750000), point2=(53.100000, 24.150000))
s0.Line(point1=(53.100000, 24.150000), point2=(53.250000, 26.550000))
s0.Line(point1=(53.250000, 26.550000), point2=(54.000000, 26.400000))
s0.Line(point1=(54.083630, 26.574880), point2=(55.064018, 25.726822))
s0.Line(point1=(55.064018, 25.726822), point2=(55.083205, 25.144530))
s0.Line(point1=(55.083205, 25.144530), point2=(54.683205, 24.594530))
s0.Line(point1=(54.683205, 24.594530), point2=(53.912470, 24.571913))
s0.Line(point1=(53.912470, 24.571913), point2=(53.062664, 24.078151))
s0.Line(point1=(53.062664, 24.078151), point2=(53.169806, 26.654296))
s0.Line(point1=(53.169806, 26.654296), point2=(54.083630, 26.574880))
s0.Line(point1=(53.916370, 26.225120), point2=(54.735982, 25.573178))
s0.Line(point1=(54.735982, 25.573178), point2=(54.716795, 25.255470))
s0.Line(point1=(54.716795, 25.255470), point2=(54.516795, 24.905470))
s0.Line(point1=(54.516795, 24.905470), point2=(53.787530, 24.928087))
s0.Line(point1=(53.787530, 24.928087), point2=(53.137336, 24.221849))
s0.Line(point1=(53.137336, 24.221849), point2=(53.330194, 26.445704))
s0.Line(point1=(53.330194, 26.445704), point2=(53.916370, 26.225120))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(52.950000, 21.600000), point2=(54.300000, 21.750000))
s0.Line(point1=(54.300000, 21.750000), point2=(54.600000, 21.450000))
s0.Line(point1=(54.600000, 21.450000), point2=(54.450000, 20.700000))
s0.Line(point1=(54.450000, 20.700000), point2=(53.850000, 20.400000))
s0.Line(point1=(53.850000, 20.400000), point2=(53.250000, 20.700000))
s0.Line(point1=(53.250000, 20.700000), point2=(52.950000, 21.600000))
s0.Line(point1=(52.844089, 21.667766), point2=(54.359668, 21.920099))
s0.Line(point1=(54.359668, 21.920099), point2=(54.768769, 21.501099))
s0.Line(point1=(54.768769, 21.501099), point2=(54.592779, 20.590946))
s0.Line(point1=(54.592779, 20.590946), point2=(53.850000, 20.221115))
s0.Line(point1=(53.850000, 20.221115), point2=(53.110410, 20.578935))
s0.Line(point1=(53.110410, 20.578935), point2=(52.844089, 21.667766))
s0.Line(point1=(53.055911, 21.532234), point2=(54.240332, 21.579901))
s0.Line(point1=(54.240332, 21.579901), point2=(54.431231, 21.398901))
s0.Line(point1=(54.431231, 21.398901), point2=(54.307221, 20.809054))
s0.Line(point1=(54.307221, 20.809054), point2=(53.850000, 20.578885))
s0.Line(point1=(53.850000, 20.578885), point2=(53.389590, 20.821065))
s0.Line(point1=(53.389590, 20.821065), point2=(53.055911, 21.532234))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(55.950000, 3.750000), point2=(55.950000, 3.150000))
s0.Line(point1=(55.950000, 3.150000), point2=(54.900000, 2.250000))
s0.Line(point1=(54.900000, 2.250000), point2=(53.850000, 2.100000))
s0.Line(point1=(53.850000, 2.100000), point2=(53.400000, 2.700000))
s0.Line(point1=(53.400000, 2.700000), point2=(53.550000, 3.750000))
s0.Line(point1=(53.550000, 3.750000), point2=(55.950000, 3.750000))
s0.Line(point1=(56.050000, 3.850000), point2=(56.115079, 3.074074))
s0.Line(point1=(56.115079, 3.074074), point2=(54.979221, 2.075079))
s0.Line(point1=(54.979221, 2.075079), point2=(53.784142, 1.941005))
s0.Line(point1=(53.784142, 1.941005), point2=(53.221005, 2.654142))
s0.Line(point1=(53.221005, 2.654142), point2=(53.451005, 3.864142))
s0.Line(point1=(53.451005, 3.864142), point2=(56.050000, 3.850000))
s0.Line(point1=(55.850000, 3.650000), point2=(55.784921, 3.225926))
s0.Line(point1=(55.784921, 3.225926), point2=(54.820779, 2.424921))
s0.Line(point1=(54.820779, 2.424921), point2=(53.915858, 2.258995))
s0.Line(point1=(53.915858, 2.258995), point2=(53.578995, 2.745858))
s0.Line(point1=(53.578995, 2.745858), point2=(53.648995, 3.635858))
s0.Line(point1=(53.648995, 3.635858), point2=(55.850000, 3.650000))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(56.100000, 50.400000), point2=(56.700000, 49.650000))
s0.Line(point1=(56.700000, 49.650000), point2=(56.400000, 47.700000))
s0.Line(point1=(56.400000, 47.700000), point2=(53.550000, 45.900000))
s0.Line(point1=(53.550000, 45.900000), point2=(54.300000, 50.250000))
s0.Line(point1=(54.300000, 50.250000), point2=(54.750000, 50.700000))
s0.Line(point1=(54.750000, 50.700000), point2=(56.100000, 50.400000))
s0.Line(point1=(56.199780, 50.560088), point2=(56.876924, 49.697264))
s0.Line(point1=(56.876924, 49.697264), point2=(56.552236, 47.600245))
s0.Line(point1=(56.552236, 47.600245), point2=(53.504853, 45.832442))
s0.Line(point1=(53.504853, 45.832442), point2=(54.130743, 50.337701))
s0.Line(point1=(54.130743, 50.337701), point2=(54.700982, 50.868329))
s0.Line(point1=(54.700982, 50.868329), point2=(56.199780, 50.560088))
s0.Line(point1=(56.000220, 50.239912), point2=(56.523076, 49.602736))
s0.Line(point1=(56.523076, 49.602736), point2=(56.247764, 47.799755))
s0.Line(point1=(56.247764, 47.799755), point2=(53.595147, 45.967558))
s0.Line(point1=(53.595147, 45.967558), point2=(54.469257, 50.162299))
s0.Line(point1=(54.469257, 50.162299), point2=(54.799018, 50.531671))
s0.Line(point1=(54.799018, 50.531671), point2=(56.000220, 50.239912))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(56.400000, 42.750000), point2=(56.550000, 41.700000))
s0.Line(point1=(56.550000, 41.700000), point2=(56.100000, 40.650000))
s0.Line(point1=(56.100000, 40.650000), point2=(53.550000, 39.450000))
s0.Line(point1=(53.550000, 39.450000), point2=(53.550000, 40.200000))
s0.Line(point1=(53.550000, 40.200000), point2=(54.150000, 40.650000))
s0.Line(point1=(54.150000, 40.650000), point2=(54.150000, 41.400000))
s0.Line(point1=(54.150000, 41.400000), point2=(54.600000, 42.000000))
s0.Line(point1=(54.600000, 42.000000), point2=(55.800000, 42.750000))
s0.Line(point1=(55.800000, 42.750000), point2=(56.400000, 42.750000))
s0.Line(point1=(56.498995, 42.864142), point2=(56.740909, 41.674750))
s0.Line(point1=(56.740909, 41.674750), point2=(56.234494, 40.520126))
s0.Line(point1=(56.234494, 40.520126), point2=(53.492580, 39.359518))
s0.Line(point1=(53.492580, 39.359518), point2=(53.390000, 40.280000))
s0.Line(point1=(53.390000, 40.280000), point2=(53.990000, 40.730000))
s0.Line(point1=(53.990000, 40.730000), point2=(53.970000, 41.460000))
s0.Line(point1=(53.970000, 41.460000), point2=(54.467000, 42.144800))
s0.Line(point1=(54.467000, 42.144800), point2=(55.747000, 42.934800))
s0.Line(point1=(55.747000, 42.934800), point2=(56.498995, 42.864142))
s0.Line(point1=(56.301005, 42.635858), point2=(56.359091, 41.725250))
s0.Line(point1=(56.359091, 41.725250), point2=(55.965506, 40.779874))
s0.Line(point1=(55.965506, 40.779874), point2=(53.607420, 39.540482))
s0.Line(point1=(53.607420, 39.540482), point2=(53.710000, 40.120000))
s0.Line(point1=(53.710000, 40.120000), point2=(54.310000, 40.570000))
s0.Line(point1=(54.310000, 40.570000), point2=(54.330000, 41.340000))
s0.Line(point1=(54.330000, 41.340000), point2=(54.733000, 41.855200))
s0.Line(point1=(54.733000, 41.855200), point2=(55.853000, 42.565200))
s0.Line(point1=(55.853000, 42.565200), point2=(56.301005, 42.635858))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(56.400000, 34.350000), point2=(56.850000, 33.900000))
s0.Line(point1=(56.850000, 33.900000), point2=(57.000000, 30.900000))
s0.Line(point1=(57.000000, 30.900000), point2=(55.800000, 29.100000))
s0.Line(point1=(55.800000, 29.100000), point2=(54.300000, 28.950000))
s0.Line(point1=(54.300000, 28.950000), point2=(54.000000, 29.250000))
s0.Line(point1=(54.000000, 29.250000), point2=(54.000000, 31.650000))
s0.Line(point1=(54.000000, 31.650000), point2=(54.300000, 32.700000))
s0.Line(point1=(54.300000, 32.700000), point2=(55.050000, 34.050000))
s0.Line(point1=(55.050000, 34.050000), point2=(56.400000, 34.350000))
s0.Line(point1=(56.449018, 34.518329), point2=(57.020586, 33.975704))
s0.Line(point1=(57.020586, 33.975704), point2=(57.183080, 30.849524))
s0.Line(point1=(57.183080, 30.849524), point2=(55.893155, 28.945026))
s0.Line(point1=(55.893155, 28.945026), point2=(54.239240, 28.779786))
s0.Line(point1=(54.239240, 28.779786), point2=(53.829289, 29.179289))
s0.Line(point1=(53.829289, 29.179289), point2=(53.803848, 31.677472))
s0.Line(point1=(53.803848, 31.677472), point2=(54.116432, 32.776036))
s0.Line(point1=(54.116432, 32.776036), point2=(54.940891, 34.196183))
s0.Line(point1=(54.940891, 34.196183), point2=(56.449018, 34.518329))
s0.Line(point1=(56.350982, 34.181671), point2=(56.679414, 33.824296))
s0.Line(point1=(56.679414, 33.824296), point2=(56.816920, 30.950476))
s0.Line(point1=(56.816920, 30.950476), point2=(55.706845, 29.254974))
s0.Line(point1=(55.706845, 29.254974), point2=(54.360760, 29.120214))
s0.Line(point1=(54.360760, 29.120214), point2=(54.170711, 29.320711))
s0.Line(point1=(54.170711, 29.320711), point2=(54.196152, 31.622528))
s0.Line(point1=(54.196152, 31.622528), point2=(54.483568, 32.623964))
s0.Line(point1=(54.483568, 32.623964), point2=(55.159109, 33.903817))
s0.Line(point1=(55.159109, 33.903817), point2=(56.350982, 34.181671))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(58.350000, 18.750000), point2=(58.200000, 18.300000))
s0.Line(point1=(58.200000, 18.300000), point2=(56.400000, 17.700000))
s0.Line(point1=(56.400000, 17.700000), point2=(55.200000, 17.700000))
s0.Line(point1=(55.200000, 17.700000), point2=(54.450000, 18.300000))
s0.Line(point1=(54.450000, 18.300000), point2=(54.600000, 19.050000))
s0.Line(point1=(54.600000, 19.050000), point2=(56.550000, 20.250000))
s0.Line(point1=(56.550000, 20.250000), point2=(58.350000, 18.750000))
s0.Line(point1=(58.508887, 18.795199), point2=(58.326491, 18.173509))
s0.Line(point1=(58.326491, 18.173509), point2=(56.431623, 17.505132))
s0.Line(point1=(56.431623, 17.505132), point2=(55.137530, 17.521913))
s0.Line(point1=(55.137530, 17.521913), point2=(54.289472, 18.241525))
s0.Line(point1=(54.289472, 18.241525), point2=(54.449532, 19.154777))
s0.Line(point1=(54.449532, 19.154777), point2=(56.561609, 20.411988))
s0.Line(point1=(56.561609, 20.411988), point2=(58.508887, 18.795199))
s0.Line(point1=(58.191113, 18.704801), point2=(58.073509, 18.426491))
s0.Line(point1=(58.073509, 18.426491), point2=(56.368377, 17.894868))
s0.Line(point1=(56.368377, 17.894868), point2=(55.262470, 17.878087))
s0.Line(point1=(55.262470, 17.878087), point2=(54.610528, 18.358475))
s0.Line(point1=(54.610528, 18.358475), point2=(54.750468, 18.945223))
s0.Line(point1=(54.750468, 18.945223), point2=(56.538391, 20.088012))
s0.Line(point1=(56.538391, 20.088012), point2=(58.191113, 18.704801))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(54.600000, 38.100000), point2=(55.050000, 38.100000))
s0.Line(point1=(55.050000, 38.100000), point2=(55.500000, 37.200000))
s0.Line(point1=(55.500000, 37.200000), point2=(56.100000, 36.900000))
s0.Line(point1=(56.100000, 36.900000), point2=(56.250000, 35.850000))
s0.Line(point1=(56.250000, 35.850000), point2=(56.850000, 35.100000))
s0.Line(point1=(56.850000, 35.100000), point2=(56.700000, 34.800000))
s0.Line(point1=(56.700000, 34.800000), point2=(55.050000, 35.400000))
s0.Line(point1=(55.050000, 35.400000), point2=(54.600000, 36.750000))
s0.Line(point1=(54.600000, 36.750000), point2=(54.600000, 38.100000))
s0.Line(point1=(54.500000, 38.200000), point2=(55.139443, 38.244721))
s0.Line(point1=(55.139443, 38.244721), point2=(55.634164, 37.334164))
s0.Line(point1=(55.634164, 37.334164), point2=(56.243716, 37.003585))
s0.Line(point1=(56.243716, 37.003585), point2=(56.427082, 35.926612))
s0.Line(point1=(56.427082, 35.926612), point2=(57.017530, 35.117748))
s0.Line(point1=(57.017530, 35.117748), point2=(56.755268, 34.661299))
s0.Line(point1=(56.755268, 34.661299), point2=(54.920957, 35.274398))
s0.Line(point1=(54.920957, 35.274398), point2=(54.405132, 36.718377))
s0.Line(point1=(54.405132, 36.718377), point2=(54.500000, 38.200000))
s0.Line(point1=(54.700000, 38.000000), point2=(54.960557, 37.955279))
s0.Line(point1=(54.960557, 37.955279), point2=(55.365836, 37.065836))
s0.Line(point1=(55.365836, 37.065836), point2=(55.956284, 36.796415))
s0.Line(point1=(55.956284, 36.796415), point2=(56.072918, 35.773388))
s0.Line(point1=(56.072918, 35.773388), point2=(56.682470, 35.082252))
s0.Line(point1=(56.682470, 35.082252), point2=(56.644732, 34.938701))
s0.Line(point1=(56.644732, 34.938701), point2=(55.179043, 35.525602))
s0.Line(point1=(55.179043, 35.525602), point2=(54.794868, 36.781623))
s0.Line(point1=(54.794868, 36.781623), point2=(54.700000, 38.000000))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(55.050000, 21.450000), point2=(55.500000, 21.900000))
s0.Line(point1=(55.500000, 21.900000), point2=(56.400000, 21.600000))
s0.Line(point1=(56.400000, 21.600000), point2=(56.700000, 20.550000))
s0.Line(point1=(56.700000, 20.550000), point2=(55.500000, 20.250000))
s0.Line(point1=(55.500000, 20.250000), point2=(55.050000, 20.850000))
s0.Line(point1=(55.050000, 20.850000), point2=(55.050000, 21.450000))
s0.Line(point1=(54.879289, 21.520711), point2=(55.460912, 22.065579))
s0.Line(point1=(55.460912, 22.065579), point2=(56.527775, 21.722340))
s0.Line(point1=(56.527775, 21.722340), point2=(56.820406, 20.480458))
s0.Line(point1=(56.820406, 20.480458), point2=(55.444254, 20.092986))
s0.Line(point1=(55.444254, 20.092986), point2=(54.870000, 20.790000))
s0.Line(point1=(54.870000, 20.790000), point2=(54.879289, 21.520711))
s0.Line(point1=(55.220711, 21.379289), point2=(55.539088, 21.734421))
s0.Line(point1=(55.539088, 21.734421), point2=(56.272225, 21.477660))
s0.Line(point1=(56.272225, 21.477660), point2=(56.579594, 20.619542))
s0.Line(point1=(56.579594, 20.619542), point2=(55.555746, 20.407014))
s0.Line(point1=(55.555746, 20.407014), point2=(55.230000, 20.910000))
s0.Line(point1=(55.230000, 20.910000), point2=(55.220711, 21.379289))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(55.200000, 39.900000), point2=(56.550000, 39.900000))
s0.Line(point1=(56.550000, 39.900000), point2=(57.450000, 38.700000))
s0.Line(point1=(57.450000, 38.700000), point2=(57.750000, 38.700000))
s0.Line(point1=(57.750000, 38.700000), point2=(57.900000, 38.100000))
s0.Line(point1=(57.900000, 38.100000), point2=(58.350000, 37.950000))
s0.Line(point1=(58.350000, 37.950000), point2=(58.650000, 37.050000))
s0.Line(point1=(58.650000, 37.050000), point2=(58.350000, 35.250000))
s0.Line(point1=(58.350000, 35.250000), point2=(57.900000, 35.250000))
s0.Line(point1=(57.900000, 35.250000), point2=(56.850000, 37.200000))
s0.Line(point1=(56.850000, 37.200000), point2=(55.800000, 38.100000))
s0.Line(point1=(55.800000, 38.100000), point2=(55.200000, 39.900000))
s0.Line(point1=(55.105132, 39.968377), point2=(56.630000, 40.060000))
s0.Line(point1=(56.630000, 40.060000), point2=(57.530000, 38.860000))
s0.Line(point1=(57.530000, 38.860000), point2=(57.847014, 38.824254))
s0.Line(point1=(57.847014, 38.824254), point2=(58.028637, 38.219122))
s0.Line(point1=(58.028637, 38.219122), point2=(58.476491, 38.076491))
s0.Line(point1=(58.476491, 38.076491), point2=(58.843508, 37.065183))
s0.Line(point1=(58.843508, 37.065183), point2=(58.448639, 35.133560))
s0.Line(point1=(58.448639, 35.133560), point2=(57.811953, 35.102590))
s0.Line(point1=(57.811953, 35.102590), point2=(56.696874, 37.076664))
s0.Line(point1=(56.696874, 37.076664), point2=(55.640053, 37.992452))
s0.Line(point1=(55.640053, 37.992452), point2=(55.105132, 39.968377))
s0.Line(point1=(55.294868, 39.831623), point2=(56.470000, 39.740000))
s0.Line(point1=(56.470000, 39.740000), point2=(57.370000, 38.540000))
s0.Line(point1=(57.370000, 38.540000), point2=(57.652986, 38.575746))
s0.Line(point1=(57.652986, 38.575746), point2=(57.771363, 37.980878))
s0.Line(point1=(57.771363, 37.980878), point2=(58.223509, 37.823509))
s0.Line(point1=(58.223509, 37.823509), point2=(58.456492, 37.034817))
s0.Line(point1=(58.456492, 37.034817), point2=(58.251361, 35.366440))
s0.Line(point1=(58.251361, 35.366440), point2=(57.988047, 35.397410))
s0.Line(point1=(57.988047, 35.397410), point2=(57.003126, 37.323336))
s0.Line(point1=(57.003126, 37.323336), point2=(55.959947, 38.207548))
s0.Line(point1=(55.959947, 38.207548), point2=(55.294868, 39.831623))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
print 180
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(55.200000, 27.900000), point2=(55.800000, 28.200000))
s0.Line(point1=(55.800000, 28.200000), point2=(55.800000, 28.650000))
s0.Line(point1=(55.800000, 28.650000), point2=(61.650000, 28.200000))
s0.Line(point1=(61.650000, 28.200000), point2=(61.650000, 26.250000))
s0.Line(point1=(61.650000, 26.250000), point2=(57.600000, 26.850000))
s0.Line(point1=(57.600000, 26.850000), point2=(55.950000, 26.700000))
s0.Line(point1=(55.950000, 26.700000), point2=(55.200000, 27.150000))
s0.Line(point1=(55.200000, 27.150000), point2=(55.200000, 27.900000))
s0.Line(point1=(55.055279, 27.989443), point2=(55.655279, 28.289443))
s0.Line(point1=(55.655279, 28.289443), point2=(55.707670, 28.749705))
s0.Line(point1=(55.707670, 28.749705), point2=(61.757670, 28.299705))
s0.Line(point1=(61.757670, 28.299705), point2=(61.735345, 26.151080))
s0.Line(point1=(61.735345, 26.151080), point2=(57.594399, 26.651490))
s0.Line(point1=(57.594399, 26.651490), point2=(55.907604, 26.514661))
s0.Line(point1=(55.907604, 26.514661), point2=(55.048550, 27.064251))
s0.Line(point1=(55.048550, 27.064251), point2=(55.055279, 27.989443))
s0.Line(point1=(55.344721, 27.810557), point2=(55.944721, 28.110557))
s0.Line(point1=(55.944721, 28.110557), point2=(55.892330, 28.550295))
s0.Line(point1=(55.892330, 28.550295), point2=(61.542330, 28.100295))
s0.Line(point1=(61.542330, 28.100295), point2=(61.564655, 26.348920))
s0.Line(point1=(61.564655, 26.348920), point2=(57.605601, 27.048510))
s0.Line(point1=(57.605601, 27.048510), point2=(55.992396, 26.885339))
s0.Line(point1=(55.992396, 26.885339), point2=(55.351450, 27.235749))
s0.Line(point1=(55.351450, 27.235749), point2=(55.344721, 27.810557))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(55.500000, 44.400000), point2=(56.250000, 44.700000))
s0.Line(point1=(56.250000, 44.700000), point2=(60.150000, 44.550000))
s0.Line(point1=(60.150000, 44.550000), point2=(60.000000, 43.950000))
s0.Line(point1=(60.000000, 43.950000), point2=(61.050000, 43.650000))
s0.Line(point1=(61.050000, 43.650000), point2=(61.050000, 42.900000))
s0.Line(point1=(61.050000, 42.900000), point2=(59.400000, 42.750000))
s0.Line(point1=(59.400000, 42.750000), point2=(57.900000, 43.050000))
s0.Line(point1=(57.900000, 43.050000), point2=(55.500000, 43.800000))
s0.Line(point1=(55.500000, 43.800000), point2=(55.500000, 44.400000))
s0.Line(point1=(55.362861, 44.492848), point2=(56.216704, 44.892774))
s0.Line(point1=(56.216704, 44.892774), point2=(60.250858, 44.625673))
s0.Line(point1=(60.250858, 44.625673), point2=(60.124486, 44.021899))
s0.Line(point1=(60.124486, 44.021899), point2=(61.177472, 43.746152))
s0.Line(point1=(61.177472, 43.746152), point2=(61.159054, 42.800411))
s0.Line(point1=(61.159054, 42.800411), point2=(59.389442, 42.552353))
s0.Line(point1=(59.389442, 42.552353), point2=(57.850561, 42.856494))
s0.Line(point1=(57.850561, 42.856494), point2=(55.370173, 43.704552))
s0.Line(point1=(55.370173, 43.704552), point2=(55.362861, 44.492848))
s0.Line(point1=(55.637139, 44.307152), point2=(56.283296, 44.507226))
s0.Line(point1=(56.283296, 44.507226), point2=(60.049142, 44.474327))
s0.Line(point1=(60.049142, 44.474327), point2=(59.875514, 43.878101))
s0.Line(point1=(59.875514, 43.878101), point2=(60.922528, 43.553848))
s0.Line(point1=(60.922528, 43.553848), point2=(60.940946, 42.999589))
s0.Line(point1=(60.940946, 42.999589), point2=(59.410558, 42.947647))
s0.Line(point1=(59.410558, 42.947647), point2=(57.949439, 43.243506))
s0.Line(point1=(57.949439, 43.243506), point2=(55.629827, 43.895448))
s0.Line(point1=(55.629827, 43.895448), point2=(55.637139, 44.307152))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(55.650000, 52.500000), point2=(58.500000, 52.500000))
s0.Line(point1=(58.500000, 52.500000), point2=(58.950000, 51.750000))
s0.Line(point1=(58.950000, 51.750000), point2=(58.950000, 50.700000))
s0.Line(point1=(58.950000, 50.700000), point2=(58.350000, 50.550000))
s0.Line(point1=(58.350000, 50.550000), point2=(57.600000, 50.850000))
s0.Line(point1=(57.600000, 50.850000), point2=(55.650000, 52.500000))
s0.Line(point1=(55.585406, 52.500000), point2=(58.585749, 52.500000))
s0.Line(point1=(58.585749, 52.500000), point2=(59.135749, 51.801450))
s0.Line(point1=(59.135749, 51.801450), point2=(59.074254, 50.602986))
s0.Line(point1=(59.074254, 50.602986), point2=(58.337114, 50.360138))
s0.Line(point1=(58.337114, 50.360138), point2=(57.498267, 50.680814))
s0.Line(point1=(57.498267, 50.680814), point2=(55.585406, 52.500000))
s0.Line(point1=(55.714594, 52.500000), point2=(58.414251, 52.500000))
s0.Line(point1=(58.414251, 52.500000), point2=(58.764251, 51.698550))
s0.Line(point1=(58.764251, 51.698550), point2=(58.825746, 50.797014))
s0.Line(point1=(58.825746, 50.797014), point2=(58.362886, 50.739862))
s0.Line(point1=(58.362886, 50.739862), point2=(57.701733, 51.019186))
s0.Line(point1=(57.701733, 51.019186), point2=(55.714594, 52.500000))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(56.400000, 2.550000), point2=(57.000000, 2.550000))
s0.Line(point1=(57.000000, 2.550000), point2=(57.300000, 1.950000))
s0.Line(point1=(57.300000, 1.950000), point2=(57.600000, 1.950000))
s0.Line(point1=(57.600000, 1.950000), point2=(57.600000, 1.500000))
s0.Line(point1=(57.600000, 1.500000), point2=(58.350000, 1.050000))
s0.Line(point1=(58.350000, 1.050000), point2=(58.350000, 0.000000))
s0.Line(point1=(58.350000, 0.000000), point2=(56.250000, 0.000000))
s0.Line(point1=(56.250000, 0.000000), point2=(55.950000, 1.950000))
s0.Line(point1=(55.950000, 1.950000), point2=(56.400000, 1.950000))
s0.Line(point1=(56.400000, 1.950000), point2=(56.400000, 2.550000))
s0.Line(point1=(56.300000, 2.650000), point2=(57.089443, 2.694721))
s0.Line(point1=(57.089443, 2.694721), point2=(57.389443, 2.094721))
s0.Line(point1=(57.389443, 2.094721), point2=(57.700000, 2.050000))
s0.Line(point1=(57.700000, 2.050000), point2=(57.751450, 1.585749))
s0.Line(point1=(57.751450, 1.585749), point2=(58.501450, 1.135749))
s0.Line(point1=(58.501450, 1.135749), point2=(58.450000, 0.000000))
s0.Line(point1=(58.450000, 0.000000), point2=(56.151163, 0.000000))
s0.Line(point1=(56.151163, 0.000000), point2=(55.851163, 2.034794))
s0.Line(point1=(55.851163, 2.034794), point2=(56.300000, 2.050000))
s0.Line(point1=(56.300000, 2.050000), point2=(56.300000, 2.650000))
s0.Line(point1=(56.500000, 2.450000), point2=(56.910557, 2.405279))
s0.Line(point1=(56.910557, 2.405279), point2=(57.210557, 1.805279))
s0.Line(point1=(57.210557, 1.805279), point2=(57.500000, 1.850000))
s0.Line(point1=(57.500000, 1.850000), point2=(57.448550, 1.414251))
s0.Line(point1=(57.448550, 1.414251), point2=(58.198550, 0.964251))
s0.Line(point1=(58.198550, 0.964251), point2=(58.250000, 0.000000))
s0.Line(point1=(58.250000, 0.000000), point2=(56.348837, 0.000000))
s0.Line(point1=(56.348837, 0.000000), point2=(56.048837, 1.865206))
s0.Line(point1=(56.048837, 1.865206), point2=(56.500000, 1.850000))
s0.Line(point1=(56.500000, 1.850000), point2=(56.500000, 2.450000))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(61.800000, 24.000000), point2=(61.800000, 23.100000))
s0.Line(point1=(61.800000, 23.100000), point2=(60.600000, 21.900000))
s0.Line(point1=(60.600000, 21.900000), point2=(58.800000, 22.050000))
s0.Line(point1=(58.800000, 22.050000), point2=(57.900000, 21.150000))
s0.Line(point1=(57.900000, 21.150000), point2=(57.450000, 21.150000))
s0.Line(point1=(57.450000, 21.150000), point2=(56.100000, 22.800000))
s0.Line(point1=(56.100000, 22.800000), point2=(56.250000, 23.700000))
s0.Line(point1=(56.250000, 23.700000), point2=(58.350000, 25.200000))
s0.Line(point1=(58.350000, 25.200000), point2=(60.600000, 25.500000))
s0.Line(point1=(60.600000, 25.500000), point2=(61.800000, 24.000000))
s0.Line(point1=(61.978087, 24.062470), point2=(61.970711, 23.029289))
s0.Line(point1=(61.970711, 23.029289), point2=(60.662406, 21.729635))
s0.Line(point1=(60.662406, 21.729635), point2=(58.862406, 21.879635))
s0.Line(point1=(58.862406, 21.879635), point2=(57.970711, 20.979289))
s0.Line(point1=(57.970711, 20.979289), point2=(57.372604, 20.986676))
s0.Line(point1=(57.372604, 20.986676), point2=(55.923965, 22.753116))
s0.Line(point1=(55.923965, 22.753116), point2=(56.093237, 23.797813))
s0.Line(point1=(56.093237, 23.797813), point2=(58.278660, 25.380496))
s0.Line(point1=(58.278660, 25.380496), point2=(60.664871, 25.661592))
s0.Line(point1=(60.664871, 25.661592), point2=(61.978087, 24.062470))
s0.Line(point1=(61.621913, 23.937530), point2=(61.629289, 23.170711))
s0.Line(point1=(61.629289, 23.170711), point2=(60.537594, 22.070365))
s0.Line(point1=(60.537594, 22.070365), point2=(58.737594, 22.220365))
s0.Line(point1=(58.737594, 22.220365), point2=(57.829289, 21.320711))
s0.Line(point1=(57.829289, 21.320711), point2=(57.527396, 21.313324))
s0.Line(point1=(57.527396, 21.313324), point2=(56.276035, 22.846884))
s0.Line(point1=(56.276035, 22.846884), point2=(56.406763, 23.602187))
s0.Line(point1=(56.406763, 23.602187), point2=(58.421340, 25.019504))
s0.Line(point1=(58.421340, 25.019504), point2=(60.535129, 25.338408))
s0.Line(point1=(60.535129, 25.338408), point2=(61.621913, 23.937530))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(61.350000, 49.800000), point2=(61.350000, 49.200000))
s0.Line(point1=(61.350000, 49.200000), point2=(60.600000, 48.750000))
s0.Line(point1=(60.600000, 48.750000), point2=(60.600000, 48.450000))
s0.Line(point1=(60.600000, 48.450000), point2=(59.400000, 48.300000))
s0.Line(point1=(59.400000, 48.300000), point2=(58.950000, 47.700000))
s0.Line(point1=(58.950000, 47.700000), point2=(58.500000, 47.700000))
s0.Line(point1=(58.500000, 47.700000), point2=(57.450000, 46.200000))
s0.Line(point1=(57.450000, 46.200000), point2=(56.400000, 46.200000))
s0.Line(point1=(56.400000, 46.200000), point2=(56.550000, 47.100000))
s0.Line(point1=(56.550000, 47.100000), point2=(58.350000, 49.050000))
s0.Line(point1=(58.350000, 49.050000), point2=(59.250000, 49.050000))
s0.Line(point1=(59.250000, 49.050000), point2=(60.450000, 49.800000))
s0.Line(point1=(60.450000, 49.800000), point2=(61.350000, 49.800000))
s0.Line(point1=(61.450000, 49.900000), point2=(61.501450, 49.114251))
s0.Line(point1=(61.501450, 49.114251), point2=(60.751450, 48.664251))
s0.Line(point1=(60.751450, 48.664251), point2=(60.712403, 48.350772))
s0.Line(point1=(60.712403, 48.350772), point2=(59.492403, 48.140772))
s0.Line(point1=(59.492403, 48.140772), point2=(59.030000, 47.540000))
s0.Line(point1=(59.030000, 47.540000), point2=(58.581923, 47.542654))
s0.Line(point1=(58.581923, 47.542654), point2=(57.531923, 46.042654))
s0.Line(point1=(57.531923, 46.042654), point2=(56.301361, 46.116440))
s0.Line(point1=(56.301361, 46.116440), point2=(56.377880, 47.184268))
s0.Line(point1=(56.377880, 47.184268), point2=(58.276520, 49.217828))
s0.Line(point1=(58.276520, 49.217828), point2=(59.197000, 49.234800))
s0.Line(point1=(59.197000, 49.234800), point2=(60.397000, 49.984800))
s0.Line(point1=(60.397000, 49.984800), point2=(61.450000, 49.900000))
s0.Line(point1=(61.250000, 49.700000), point2=(61.198550, 49.285749))
s0.Line(point1=(61.198550, 49.285749), point2=(60.448550, 48.835749))
s0.Line(point1=(60.448550, 48.835749), point2=(60.487597, 48.549228))
s0.Line(point1=(60.487597, 48.549228), point2=(59.307597, 48.459228))
s0.Line(point1=(59.307597, 48.459228), point2=(58.870000, 47.860000))
s0.Line(point1=(58.870000, 47.860000), point2=(58.418077, 47.857346))
s0.Line(point1=(58.418077, 47.857346), point2=(57.368077, 46.357346))
s0.Line(point1=(57.368077, 46.357346), point2=(56.498639, 46.283560))
s0.Line(point1=(56.498639, 46.283560), point2=(56.722120, 47.015732))
s0.Line(point1=(56.722120, 47.015732), point2=(58.423480, 48.882172))
s0.Line(point1=(58.423480, 48.882172), point2=(59.303000, 48.865200))
s0.Line(point1=(59.303000, 48.865200), point2=(60.503000, 49.615200))
s0.Line(point1=(60.503000, 49.615200), point2=(61.250000, 49.700000))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(60.600000, 4.350000), point2=(60.600000, 3.600000))
s0.Line(point1=(60.600000, 3.600000), point2=(58.350000, 3.750000))
s0.Line(point1=(58.350000, 3.750000), point2=(57.450000, 3.150000))
s0.Line(point1=(57.450000, 3.150000), point2=(56.850000, 3.150000))
s0.Line(point1=(56.850000, 3.150000), point2=(57.150000, 4.200000))
s0.Line(point1=(57.150000, 4.200000), point2=(58.350000, 5.250000))
s0.Line(point1=(58.350000, 5.250000), point2=(60.000000, 5.100000))
s0.Line(point1=(60.000000, 5.100000), point2=(60.600000, 4.350000))
s0.Line(point1=(60.778087, 4.412470), point2=(60.693348, 3.500221))
s0.Line(point1=(60.693348, 3.500221), point2=(58.398818, 3.567016))
s0.Line(point1=(58.398818, 3.567016), point2=(57.505470, 2.966795))
s0.Line(point1=(57.505470, 2.966795), point2=(56.753848, 3.077472))
s0.Line(point1=(56.753848, 3.077472), point2=(56.987997, 4.302730))
s0.Line(point1=(56.987997, 4.302730), point2=(58.293203, 5.424847))
s0.Line(point1=(58.293203, 5.424847), point2=(60.087140, 5.262059))
s0.Line(point1=(60.087140, 5.262059), point2=(60.778087, 4.412470))
s0.Line(point1=(60.421913, 4.287530), point2=(60.506652, 3.699779))
s0.Line(point1=(60.506652, 3.699779), point2=(58.301182, 3.932984))
s0.Line(point1=(58.301182, 3.932984), point2=(57.394530, 3.333205))
s0.Line(point1=(57.394530, 3.333205), point2=(56.946152, 3.222528))
s0.Line(point1=(56.946152, 3.222528), point2=(57.312003, 4.097270))
s0.Line(point1=(57.312003, 4.097270), point2=(58.406797, 5.075153))
s0.Line(point1=(58.406797, 5.075153), point2=(59.912860, 4.937941))
s0.Line(point1=(59.912860, 4.937941), point2=(60.421913, 4.287530))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(57.600000, 10.950000), point2=(59.100000, 11.700000))
s0.Line(point1=(59.100000, 11.700000), point2=(60.000000, 12.750000))
s0.Line(point1=(60.000000, 12.750000), point2=(61.200000, 12.750000))
s0.Line(point1=(61.200000, 12.750000), point2=(63.000000, 12.150000))
s0.Line(point1=(63.000000, 12.150000), point2=(65.850000, 9.150000))
s0.Line(point1=(65.850000, 9.150000), point2=(67.050000, 6.600000))
s0.Line(point1=(67.050000, 6.600000), point2=(66.450000, 4.500000))
s0.Line(point1=(66.450000, 4.500000), point2=(65.250000, 3.900000))
s0.Line(point1=(65.250000, 3.900000), point2=(60.900000, 6.000000))
s0.Line(point1=(60.900000, 6.000000), point2=(58.650000, 8.100000))
s0.Line(point1=(58.650000, 8.100000), point2=(57.600000, 9.900000))
s0.Line(point1=(57.600000, 9.900000), point2=(57.600000, 10.950000))
s0.Line(point1=(57.455279, 11.039443), point2=(58.979353, 11.854522))
s0.Line(point1=(58.979353, 11.854522), point2=(59.924074, 12.915079))
s0.Line(point1=(59.924074, 12.915079), point2=(61.231623, 12.944868))
s0.Line(point1=(61.231623, 12.944868), point2=(63.104123, 12.313743))
s0.Line(point1=(63.104123, 12.313743), point2=(66.012982, 9.261455))
s0.Line(point1=(66.012982, 9.261455), point2=(67.236634, 6.615108))
s0.Line(point1=(67.236634, 6.615108), point2=(66.590874, 4.383085))
s0.Line(point1=(66.590874, 4.383085), point2=(65.251246, 3.720502))
s0.Line(point1=(65.251246, 3.720502), point2=(60.788293, 5.836839))
s0.Line(point1=(60.788293, 5.836839), point2=(58.495390, 7.976507))
s0.Line(point1=(58.495390, 7.976507), point2=(57.413622, 9.849613))
s0.Line(point1=(57.413622, 9.849613), point2=(57.455279, 11.039443))
s0.Line(point1=(57.744721, 10.860557), point2=(59.220647, 11.545478))
s0.Line(point1=(59.220647, 11.545478), point2=(60.075926, 12.584921))
s0.Line(point1=(60.075926, 12.584921), point2=(61.168377, 12.555132))
s0.Line(point1=(61.168377, 12.555132), point2=(62.895877, 11.986257))
s0.Line(point1=(62.895877, 11.986257), point2=(65.687018, 9.038545))
s0.Line(point1=(65.687018, 9.038545), point2=(66.863366, 6.584892))
s0.Line(point1=(66.863366, 6.584892), point2=(66.309126, 4.616915))
s0.Line(point1=(66.309126, 4.616915), point2=(65.248754, 4.079498))
s0.Line(point1=(65.248754, 4.079498), point2=(61.011707, 6.163161))
s0.Line(point1=(61.011707, 6.163161), point2=(58.804610, 8.223493))
s0.Line(point1=(58.804610, 8.223493), point2=(57.786378, 9.950387))
s0.Line(point1=(57.786378, 9.950387), point2=(57.744721, 10.860557))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(57.750000, 33.750000), point2=(58.650000, 33.750000))
s0.Line(point1=(58.650000, 33.750000), point2=(59.400000, 32.400000))
s0.Line(point1=(59.400000, 32.400000), point2=(59.400000, 29.400000))
s0.Line(point1=(59.400000, 29.400000), point2=(58.800000, 29.400000))
s0.Line(point1=(58.800000, 29.400000), point2=(58.050000, 30.300000))
s0.Line(point1=(58.050000, 30.300000), point2=(57.750000, 33.750000))
s0.Line(point1=(57.650376, 33.841337), point2=(58.737416, 33.898564))
s0.Line(point1=(58.737416, 33.898564), point2=(59.587416, 32.448564))
s0.Line(point1=(59.587416, 32.448564), point2=(59.500000, 29.300000))
s0.Line(point1=(59.500000, 29.300000), point2=(58.723178, 29.235982))
s0.Line(point1=(58.723178, 29.235982), point2=(57.873554, 30.227319))
s0.Line(point1=(57.873554, 30.227319), point2=(57.650376, 33.841337))
s0.Line(point1=(57.849624, 33.658663), point2=(58.562584, 33.601436))
s0.Line(point1=(58.562584, 33.601436), point2=(59.212584, 32.351436))
s0.Line(point1=(59.212584, 32.351436), point2=(59.300000, 29.500000))
s0.Line(point1=(59.300000, 29.500000), point2=(58.876822, 29.564018))
s0.Line(point1=(58.876822, 29.564018), point2=(58.226446, 30.372681))
s0.Line(point1=(58.226446, 30.372681), point2=(57.849624, 33.658663))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(58.050000, 40.800000), point2=(58.650000, 40.950000))
s0.Line(point1=(58.650000, 40.950000), point2=(58.650000, 41.400000))
s0.Line(point1=(58.650000, 41.400000), point2=(59.850000, 40.950000))
s0.Line(point1=(59.850000, 40.950000), point2=(61.200000, 39.750000))
s0.Line(point1=(61.200000, 39.750000), point2=(61.800000, 38.400000))
s0.Line(point1=(61.800000, 38.400000), point2=(60.750000, 38.250000))
s0.Line(point1=(60.750000, 38.250000), point2=(58.350000, 39.600000))
s0.Line(point1=(58.350000, 39.600000), point2=(58.050000, 39.900000))
s0.Line(point1=(58.050000, 39.900000), point2=(58.050000, 40.800000))
s0.Line(point1=(57.925746, 40.897014), point2=(58.525746, 41.047014))
s0.Line(point1=(58.525746, 41.047014), point2=(58.585112, 41.493633))
s0.Line(point1=(58.585112, 41.493633), point2=(59.951549, 41.118374))
s0.Line(point1=(59.951549, 41.118374), point2=(61.357818, 39.865355))
s0.Line(point1=(61.357818, 39.865355), point2=(61.905523, 38.341619))
s0.Line(point1=(61.905523, 38.341619), point2=(60.715116, 38.063847))
s0.Line(point1=(60.715116, 38.063847), point2=(58.230263, 39.442132))
s0.Line(point1=(58.230263, 39.442132), point2=(57.879289, 39.829289))
s0.Line(point1=(57.879289, 39.829289), point2=(57.925746, 40.897014))
s0.Line(point1=(58.174254, 40.702986), point2=(58.774254, 40.852986))
s0.Line(point1=(58.774254, 40.852986), point2=(58.714888, 41.306367))
s0.Line(point1=(58.714888, 41.306367), point2=(59.748451, 40.781626))
s0.Line(point1=(59.748451, 40.781626), point2=(61.042182, 39.634645))
s0.Line(point1=(61.042182, 39.634645), point2=(61.694477, 38.458381))
s0.Line(point1=(61.694477, 38.458381), point2=(60.784884, 38.436153))
s0.Line(point1=(60.784884, 38.436153), point2=(58.469737, 39.757868))
s0.Line(point1=(58.469737, 39.757868), point2=(58.220711, 39.970711))
s0.Line(point1=(58.220711, 39.970711), point2=(58.174254, 40.702986))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(58.800000, 21.600000), point2=(60.000000, 20.850000))
s0.Line(point1=(60.000000, 20.850000), point2=(59.850000, 19.500000))
s0.Line(point1=(59.850000, 19.500000), point2=(58.650000, 19.800000))
s0.Line(point1=(58.650000, 19.800000), point2=(58.200000, 20.400000))
s0.Line(point1=(58.200000, 20.400000), point2=(58.800000, 21.600000))
s0.Line(point1=(58.763557, 21.729521), point2=(60.152388, 20.923757))
s0.Line(point1=(60.152388, 20.923757), point2=(59.925135, 19.391943))
s0.Line(point1=(59.925135, 19.391943), point2=(58.545746, 19.642986))
s0.Line(point1=(58.545746, 19.642986), point2=(58.030557, 20.384721))
s0.Line(point1=(58.030557, 20.384721), point2=(58.763557, 21.729521))
s0.Line(point1=(58.836443, 21.470479), point2=(59.847612, 20.776243))
s0.Line(point1=(59.847612, 20.776243), point2=(59.774865, 19.608057))
s0.Line(point1=(59.774865, 19.608057), point2=(58.754254, 19.957014))
s0.Line(point1=(58.754254, 19.957014), point2=(58.369443, 20.415279))
s0.Line(point1=(58.369443, 20.415279), point2=(58.836443, 21.470479))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(64.800000, 19.050000), point2=(64.650000, 18.300000))
s0.Line(point1=(64.650000, 18.300000), point2=(63.900000, 18.150000))
s0.Line(point1=(63.900000, 18.150000), point2=(63.750000, 17.700000))
s0.Line(point1=(63.750000, 17.700000), point2=(63.300000, 17.700000))
s0.Line(point1=(63.300000, 17.700000), point2=(62.850000, 16.950000))
s0.Line(point1=(62.850000, 16.950000), point2=(61.500000, 16.050000))
s0.Line(point1=(61.500000, 16.050000), point2=(58.650000, 16.200000))
s0.Line(point1=(58.650000, 16.200000), point2=(58.650000, 16.950000))
s0.Line(point1=(58.650000, 16.950000), point2=(61.800000, 19.350000))
s0.Line(point1=(61.800000, 19.350000), point2=(64.200000, 19.650000))
s0.Line(point1=(64.200000, 19.650000), point2=(64.200000, 19.200000))
s0.Line(point1=(64.200000, 19.200000), point2=(64.800000, 19.050000))
s0.Line(point1=(64.922312, 19.127403), point2=(64.767670, 18.182330))
s0.Line(point1=(64.767670, 18.182330), point2=(64.014480, 18.020319))
s0.Line(point1=(64.014480, 18.020319), point2=(63.844868, 17.568377))
s0.Line(point1=(63.844868, 17.568377), point2=(63.385749, 17.548550))
s0.Line(point1=(63.385749, 17.548550), point2=(62.991219, 16.815345))
s0.Line(point1=(62.991219, 16.815345), point2=(61.550214, 15.866933))
s0.Line(point1=(61.550214, 15.866933), point2=(58.544744, 16.100138))
s0.Line(point1=(58.544744, 16.100138), point2=(58.489396, 17.029543))
s0.Line(point1=(58.489396, 17.029543), point2=(61.726992, 19.528771))
s0.Line(point1=(61.726992, 19.528771), point2=(64.287597, 19.749228))
s0.Line(point1=(64.287597, 19.749228), point2=(64.324254, 19.297014))
s0.Line(point1=(64.324254, 19.297014), point2=(64.922312, 19.127403))
s0.Line(point1=(64.677688, 18.972597), point2=(64.532330, 18.417670))
s0.Line(point1=(64.532330, 18.417670), point2=(63.785520, 18.279681))
s0.Line(point1=(63.785520, 18.279681), point2=(63.655132, 17.831623))
s0.Line(point1=(63.655132, 17.831623), point2=(63.214251, 17.851450))
s0.Line(point1=(63.214251, 17.851450), point2=(62.708781, 17.084655))
s0.Line(point1=(62.708781, 17.084655), point2=(61.449786, 16.233067))
s0.Line(point1=(61.449786, 16.233067), point2=(58.755256, 16.299862))
s0.Line(point1=(58.755256, 16.299862), point2=(58.810604, 16.870457))
s0.Line(point1=(58.810604, 16.870457), point2=(61.873008, 19.171229))
s0.Line(point1=(61.873008, 19.171229), point2=(64.112403, 19.550772))
s0.Line(point1=(64.112403, 19.550772), point2=(64.075746, 19.102986))
s0.Line(point1=(64.075746, 19.102986), point2=(64.677688, 18.972597))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(60.000000, 47.550000), point2=(60.750000, 46.950000))
s0.Line(point1=(60.750000, 46.950000), point2=(60.750000, 46.350000))
s0.Line(point1=(60.750000, 46.350000), point2=(60.300000, 45.600000))
s0.Line(point1=(60.300000, 45.600000), point2=(59.400000, 45.600000))
s0.Line(point1=(59.400000, 45.600000), point2=(58.950000, 46.800000))
s0.Line(point1=(58.950000, 46.800000), point2=(60.000000, 47.550000))
s0.Line(point1=(60.004346, 47.709460), point2=(60.912470, 47.028087))
s0.Line(point1=(60.912470, 47.028087), point2=(60.935749, 46.298550))
s0.Line(point1=(60.935749, 46.298550), point2=(60.385749, 45.448550))
s0.Line(point1=(60.385749, 45.448550), point2=(59.306367, 45.464888))
s0.Line(point1=(59.306367, 45.464888), point2=(58.798243, 46.846261))
s0.Line(point1=(58.798243, 46.846261), point2=(60.004346, 47.709460))
s0.Line(point1=(59.995654, 47.390540), point2=(60.587530, 46.871913))
s0.Line(point1=(60.587530, 46.871913), point2=(60.564251, 46.401450))
s0.Line(point1=(60.564251, 46.401450), point2=(60.214251, 45.751450))
s0.Line(point1=(60.214251, 45.751450), point2=(59.493633, 45.735112))
s0.Line(point1=(59.493633, 45.735112), point2=(59.101757, 46.753739))
s0.Line(point1=(59.101757, 46.753739), point2=(59.995654, 47.390540))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(62.550000, 34.800000), point2=(62.250000, 34.050000))
s0.Line(point1=(62.250000, 34.050000), point2=(58.950000, 34.050000))
s0.Line(point1=(58.950000, 34.050000), point2=(59.400000, 34.800000))
s0.Line(point1=(59.400000, 34.800000), point2=(60.900000, 35.850000))
s0.Line(point1=(60.900000, 35.850000), point2=(62.100000, 35.550000))
s0.Line(point1=(62.100000, 35.550000), point2=(62.550000, 34.800000))
s0.Line(point1=(62.728597, 34.814311), point2=(62.342848, 33.912861))
s0.Line(point1=(62.342848, 33.912861), point2=(58.864251, 34.001450))
s0.Line(point1=(58.864251, 34.001450), point2=(59.256904, 34.933373))
s0.Line(point1=(59.256904, 34.933373), point2=(60.866907, 36.028937))
s0.Line(point1=(60.866907, 36.028937), point2=(62.210003, 35.698464))
s0.Line(point1=(62.210003, 35.698464), point2=(62.728597, 34.814311))
s0.Line(point1=(62.371403, 34.785689), point2=(62.157152, 34.187139))
s0.Line(point1=(62.157152, 34.187139), point2=(59.035749, 34.098550))
s0.Line(point1=(59.035749, 34.098550), point2=(59.543096, 34.666627))
s0.Line(point1=(59.543096, 34.666627), point2=(60.933093, 35.671063))
s0.Line(point1=(60.933093, 35.671063), point2=(61.989997, 35.401536))
s0.Line(point1=(61.989997, 35.401536), point2=(62.371403, 34.785689))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(59.700000, 3.150000), point2=(61.500000, 3.150000))
s0.Line(point1=(61.500000, 3.150000), point2=(61.800000, 2.700000))
s0.Line(point1=(61.800000, 2.700000), point2=(62.550000, 2.700000))
s0.Line(point1=(62.550000, 2.700000), point2=(62.850000, 2.100000))
s0.Line(point1=(62.850000, 2.100000), point2=(63.300000, 2.100000))
s0.Line(point1=(63.300000, 2.100000), point2=(63.300000, 1.500000))
s0.Line(point1=(63.300000, 1.500000), point2=(64.950000, 0.300000))
s0.Line(point1=(64.950000, 0.300000), point2=(64.950000, 0.000000))
s0.Line(point1=(64.950000, 0.000000), point2=(59.850000, 0.000000))
s0.Line(point1=(59.850000, 0.000000), point2=(60.600000, 0.750000))
s0.Line(point1=(60.600000, 0.750000), point2=(60.150000, 1.200000))
s0.Line(point1=(60.150000, 1.200000), point2=(60.150000, 2.250000))
s0.Line(point1=(60.150000, 2.250000), point2=(59.700000, 2.550000))
s0.Line(point1=(59.700000, 2.550000), point2=(59.700000, 3.150000))
s0.Line(point1=(59.600000, 3.250000), point2=(61.583205, 3.305470))
s0.Line(point1=(61.583205, 3.305470), point2=(61.883205, 2.855470))
s0.Line(point1=(61.883205, 2.855470), point2=(62.639443, 2.844721))
s0.Line(point1=(62.639443, 2.844721), point2=(62.939443, 2.244721))
s0.Line(point1=(62.939443, 2.244721), point2=(63.400000, 2.200000))
s0.Line(point1=(63.400000, 2.200000), point2=(63.458817, 1.580874))
s0.Line(point1=(63.458817, 1.580874), point2=(65.108817, 0.380874))
s0.Line(point1=(65.108817, 0.380874), point2=(65.050000, 0.000000))
s0.Line(point1=(65.050000, 0.000000), point2=(59.779289, 0.000000))
s0.Line(point1=(59.779289, 0.000000), point2=(60.458579, 0.750000))
s0.Line(point1=(60.458579, 0.750000), point2=(59.979289, 1.129289))
s0.Line(point1=(59.979289, 1.129289), point2=(59.994530, 2.166795))
s0.Line(point1=(59.994530, 2.166795), point2=(59.544530, 2.466795))
s0.Line(point1=(59.544530, 2.466795), point2=(59.600000, 3.250000))
s0.Line(point1=(59.800000, 3.050000), point2=(61.416795, 2.994530))
s0.Line(point1=(61.416795, 2.994530), point2=(61.716795, 2.544530))
s0.Line(point1=(61.716795, 2.544530), point2=(62.460557, 2.555279))
s0.Line(point1=(62.460557, 2.555279), point2=(62.760557, 1.955279))
s0.Line(point1=(62.760557, 1.955279), point2=(63.200000, 2.000000))
s0.Line(point1=(63.200000, 2.000000), point2=(63.141183, 1.419126))
s0.Line(point1=(63.141183, 1.419126), point2=(64.791183, 0.219126))
s0.Line(point1=(64.791183, 0.219126), point2=(64.850000, 0.000000))
s0.Line(point1=(64.850000, 0.000000), point2=(59.920711, 0.000000))
s0.Line(point1=(59.920711, 0.000000), point2=(60.741421, 0.750000))
s0.Line(point1=(60.741421, 0.750000), point2=(60.320711, 1.270711))
s0.Line(point1=(60.320711, 1.270711), point2=(60.305470, 2.333205))
s0.Line(point1=(60.305470, 2.333205), point2=(59.855470, 2.633205))
s0.Line(point1=(59.855470, 2.633205), point2=(59.800000, 3.050000))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(63.900000, 36.000000), point2=(64.950000, 35.250000))
s0.Line(point1=(64.950000, 35.250000), point2=(65.550000, 33.150000))
s0.Line(point1=(65.550000, 33.150000), point2=(66.600000, 31.500000))
s0.Line(point1=(66.600000, 31.500000), point2=(66.600000, 30.750000))
s0.Line(point1=(66.600000, 30.750000), point2=(64.500000, 29.850000))
s0.Line(point1=(64.500000, 29.850000), point2=(64.200000, 29.250000))
s0.Line(point1=(64.200000, 29.250000), point2=(63.000000, 29.250000))
s0.Line(point1=(63.000000, 29.250000), point2=(62.100000, 29.550000))
s0.Line(point1=(62.100000, 29.550000), point2=(60.750000, 30.900000))
s0.Line(point1=(60.750000, 30.900000), point2=(60.000000, 32.250000))
s0.Line(point1=(60.000000, 32.250000), point2=(60.300000, 32.700000))
s0.Line(point1=(60.300000, 32.700000), point2=(61.500000, 32.700000))
s0.Line(point1=(61.500000, 32.700000), point2=(61.950000, 33.000000))
s0.Line(point1=(61.950000, 33.000000), point2=(63.300000, 34.500000))
s0.Line(point1=(63.300000, 34.500000), point2=(63.300000, 35.700000))
s0.Line(point1=(63.300000, 35.700000), point2=(63.900000, 36.000000))
s0.Line(point1=(63.913402, 36.170816), point2=(65.104276, 35.358845))
s0.Line(point1=(65.104276, 35.358845), point2=(65.730519, 33.231160))
s0.Line(point1=(65.730519, 33.231160), point2=(66.784366, 31.553688))
s0.Line(point1=(66.784366, 31.553688), point2=(66.739392, 30.658085))
s0.Line(point1=(66.739392, 30.658085), point2=(64.628835, 29.713364))
s0.Line(point1=(64.628835, 29.713364), point2=(64.289443, 29.105279))
s0.Line(point1=(64.289443, 29.105279), point2=(62.968377, 29.055132))
s0.Line(point1=(62.968377, 29.055132), point2=(61.997667, 29.384421))
s0.Line(point1=(61.997667, 29.384421), point2=(60.591874, 30.780725))
s0.Line(point1=(60.591874, 30.780725), point2=(59.829379, 32.256906))
s0.Line(point1=(59.829379, 32.256906), point2=(60.216795, 32.855470))
s0.Line(point1=(60.216795, 32.855470), point2=(61.444530, 32.883205))
s0.Line(point1=(61.444530, 32.883205), point2=(61.820201, 33.150102))
s0.Line(point1=(61.820201, 33.150102), point2=(63.125671, 34.566896))
s0.Line(point1=(63.125671, 34.566896), point2=(63.155279, 35.789443))
s0.Line(point1=(63.155279, 35.789443), point2=(63.913402, 36.170816))
s0.Line(point1=(63.886598, 35.829184), point2=(64.795724, 35.141155))
s0.Line(point1=(64.795724, 35.141155), point2=(65.369481, 33.068840))
s0.Line(point1=(65.369481, 33.068840), point2=(66.415634, 31.446312))
s0.Line(point1=(66.415634, 31.446312), point2=(66.460608, 30.841915))
s0.Line(point1=(66.460608, 30.841915), point2=(64.371165, 29.986636))
s0.Line(point1=(64.371165, 29.986636), point2=(64.110557, 29.394721))
s0.Line(point1=(64.110557, 29.394721), point2=(63.031623, 29.444868))
s0.Line(point1=(63.031623, 29.444868), point2=(62.202333, 29.715579))
s0.Line(point1=(62.202333, 29.715579), point2=(60.908126, 31.019275))
s0.Line(point1=(60.908126, 31.019275), point2=(60.170621, 32.243094))
s0.Line(point1=(60.170621, 32.243094), point2=(60.383205, 32.544530))
s0.Line(point1=(60.383205, 32.544530), point2=(61.555470, 32.516795))
s0.Line(point1=(61.555470, 32.516795), point2=(62.079799, 32.849898))
s0.Line(point1=(62.079799, 32.849898), point2=(63.474329, 34.433104))
s0.Line(point1=(63.474329, 34.433104), point2=(63.444721, 35.610557))
s0.Line(point1=(63.444721, 35.610557), point2=(63.886598, 35.829184))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(60.750000, 52.200000), point2=(60.900000, 52.500000))
s0.Line(point1=(60.900000, 52.500000), point2=(64.350000, 52.500000))
s0.Line(point1=(64.350000, 52.500000), point2=(64.650000, 50.850000))
s0.Line(point1=(64.650000, 50.850000), point2=(64.050000, 50.100000))
s0.Line(point1=(64.050000, 50.100000), point2=(62.250000, 50.100000))
s0.Line(point1=(62.250000, 50.100000), point2=(60.900000, 50.700000))
s0.Line(point1=(60.900000, 50.700000), point2=(60.750000, 52.200000))
s0.Line(point1=(60.561054, 52.234771), point2=(60.810557, 52.500000))
s0.Line(point1=(60.810557, 52.500000), point2=(64.448387, 52.500000))
s0.Line(point1=(64.448387, 52.500000), point2=(64.826474, 50.805419))
s0.Line(point1=(64.826474, 50.805419), point2=(64.128087, 49.937530))
s0.Line(point1=(64.128087, 49.937530), point2=(62.209386, 49.908619))
s0.Line(point1=(62.209386, 49.908619), point2=(60.759882, 50.598668))
s0.Line(point1=(60.759882, 50.598668), point2=(60.561054, 52.234771))
s0.Line(point1=(60.938946, 52.165229), point2=(60.989443, 52.500000))
s0.Line(point1=(60.989443, 52.500000), point2=(64.251613, 52.500000))
s0.Line(point1=(64.251613, 52.500000), point2=(64.473526, 50.894581))
s0.Line(point1=(64.473526, 50.894581), point2=(63.971913, 50.262470))
s0.Line(point1=(63.971913, 50.262470), point2=(62.290614, 50.291381))
s0.Line(point1=(62.290614, 50.291381), point2=(61.040118, 50.801332))
s0.Line(point1=(61.040118, 50.801332), point2=(60.938946, 52.165229))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(63.300000, 47.100000), point2=(63.600000, 46.050000))
s0.Line(point1=(63.600000, 46.050000), point2=(64.350000, 46.050000))
s0.Line(point1=(64.350000, 46.050000), point2=(64.350000, 45.300000))
s0.Line(point1=(64.350000, 45.300000), point2=(63.150000, 44.100000))
s0.Line(point1=(63.150000, 44.100000), point2=(63.000000, 41.850000))
s0.Line(point1=(63.000000, 41.850000), point2=(62.100000, 41.550000))
s0.Line(point1=(62.100000, 41.550000), point2=(62.100000, 45.750000))
s0.Line(point1=(62.100000, 45.750000), point2=(62.400000, 47.100000))
s0.Line(point1=(62.400000, 47.100000), point2=(63.300000, 47.100000))
s0.Line(point1=(63.396152, 47.227472), point2=(63.696152, 46.177472))
s0.Line(point1=(63.696152, 46.177472), point2=(64.450000, 46.150000))
s0.Line(point1=(64.450000, 46.150000), point2=(64.520711, 45.229289))
s0.Line(point1=(64.520711, 45.229289), point2=(63.320489, 44.022637))
s0.Line(point1=(63.320489, 44.022637), point2=(63.131401, 41.748480))
s0.Line(point1=(63.131401, 41.748480), point2=(62.031623, 41.455132))
s0.Line(point1=(62.031623, 41.455132), point2=(61.902381, 45.771693))
s0.Line(point1=(61.902381, 45.771693), point2=(62.302381, 47.221693))
s0.Line(point1=(62.302381, 47.221693), point2=(63.396152, 47.227472))
s0.Line(point1=(63.203848, 46.972528), point2=(63.503848, 45.922528))
s0.Line(point1=(63.503848, 45.922528), point2=(64.250000, 45.950000))
s0.Line(point1=(64.250000, 45.950000), point2=(64.179289, 45.370711))
s0.Line(point1=(64.179289, 45.370711), point2=(62.979511, 44.177363))
s0.Line(point1=(62.979511, 44.177363), point2=(62.868599, 41.951520))
s0.Line(point1=(62.868599, 41.951520), point2=(62.168377, 41.644868))
s0.Line(point1=(62.168377, 41.644868), point2=(62.297619, 45.728307))
s0.Line(point1=(62.297619, 45.728307), point2=(62.497619, 46.978307))
s0.Line(point1=(62.497619, 46.978307), point2=(63.203848, 46.972528))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(62.250000, 15.750000), point2=(63.300000, 15.750000))
s0.Line(point1=(63.300000, 15.750000), point2=(64.200000, 15.300000))
s0.Line(point1=(64.200000, 15.300000), point2=(64.800000, 14.550000))
s0.Line(point1=(64.800000, 14.550000), point2=(65.250000, 14.550000))
s0.Line(point1=(65.250000, 14.550000), point2=(64.950000, 13.950000))
s0.Line(point1=(64.950000, 13.950000), point2=(65.250000, 13.050000))
s0.Line(point1=(65.250000, 13.050000), point2=(63.300000, 13.350000))
s0.Line(point1=(63.300000, 13.350000), point2=(63.150000, 14.400000))
s0.Line(point1=(63.150000, 14.400000), point2=(62.400000, 14.850000))
s0.Line(point1=(62.400000, 14.850000), point2=(62.250000, 15.750000))
s0.Line(point1=(62.151361, 15.833560), point2=(63.344721, 15.939443))
s0.Line(point1=(63.344721, 15.939443), point2=(64.322808, 15.451912))
s0.Line(point1=(64.322808, 15.451912), point2=(64.878087, 14.712470))
s0.Line(point1=(64.878087, 14.712470), point2=(65.339443, 14.605279))
s0.Line(point1=(65.339443, 14.605279), point2=(65.134311, 13.936901))
s0.Line(point1=(65.134311, 13.936901), point2=(65.329663, 12.982786))
s0.Line(point1=(65.329663, 12.982786), point2=(63.185799, 13.237021))
s0.Line(point1=(63.185799, 13.237021), point2=(62.999555, 14.300109))
s0.Line(point1=(62.999555, 14.300109), point2=(62.249911, 14.747811))
s0.Line(point1=(62.249911, 14.747811), point2=(62.151361, 15.833560))
s0.Line(point1=(62.348639, 15.666440), point2=(63.255279, 15.560557))
s0.Line(point1=(63.255279, 15.560557), point2=(64.077192, 15.148088))
s0.Line(point1=(64.077192, 15.148088), point2=(64.721913, 14.387530))
s0.Line(point1=(64.721913, 14.387530), point2=(65.160557, 14.494721))
s0.Line(point1=(65.160557, 14.494721), point2=(64.765689, 13.963099))
s0.Line(point1=(64.765689, 13.963099), point2=(65.170337, 13.117214))
s0.Line(point1=(65.170337, 13.117214), point2=(63.414201, 13.462979))
s0.Line(point1=(63.414201, 13.462979), point2=(63.300445, 14.499891))
s0.Line(point1=(63.300445, 14.499891), point2=(62.550089, 14.952189))
s0.Line(point1=(62.550089, 14.952189), point2=(62.348639, 15.666440))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(63.300000, 25.050000), point2=(64.800000, 24.600000))
s0.Line(point1=(64.800000, 24.600000), point2=(65.550000, 24.000000))
s0.Line(point1=(65.550000, 24.000000), point2=(66.150000, 22.500000))
s0.Line(point1=(66.150000, 22.500000), point2=(65.850000, 21.450000))
s0.Line(point1=(65.850000, 21.450000), point2=(64.950000, 21.300000))
s0.Line(point1=(64.950000, 21.300000), point2=(64.050000, 21.600000))
s0.Line(point1=(64.050000, 21.600000), point2=(62.550000, 23.100000))
s0.Line(point1=(62.550000, 23.100000), point2=(62.550000, 24.150000))
s0.Line(point1=(62.550000, 24.150000), point2=(63.300000, 25.050000))
s0.Line(point1=(63.251913, 25.209801), point2=(64.891204, 24.773870))
s0.Line(point1=(64.891204, 24.773870), point2=(65.705317, 24.115226))
s0.Line(point1=(65.705317, 24.115226), point2=(66.339000, 22.509667))
s0.Line(point1=(66.339000, 22.509667), point2=(65.962592, 21.323888))
s0.Line(point1=(65.962592, 21.323888), point2=(64.934817, 21.106492))
s0.Line(point1=(64.934817, 21.106492), point2=(63.947667, 21.434421))
s0.Line(point1=(63.947667, 21.434421), point2=(62.379289, 23.029289))
s0.Line(point1=(62.379289, 23.029289), point2=(62.373178, 24.214018))
s0.Line(point1=(62.373178, 24.214018), point2=(63.251913, 25.209801))
s0.Line(point1=(63.348087, 24.890199), point2=(64.708796, 24.426130))
s0.Line(point1=(64.708796, 24.426130), point2=(65.394683, 23.884774))
s0.Line(point1=(65.394683, 23.884774), point2=(65.961000, 22.490333))
s0.Line(point1=(65.961000, 22.490333), point2=(65.737408, 21.576112))
s0.Line(point1=(65.737408, 21.576112), point2=(64.965183, 21.493508))
s0.Line(point1=(64.965183, 21.493508), point2=(64.152333, 21.765579))
s0.Line(point1=(64.152333, 21.765579), point2=(62.720711, 23.170711))
s0.Line(point1=(62.720711, 23.170711), point2=(62.726822, 24.085982))
s0.Line(point1=(62.726822, 24.085982), point2=(63.348087, 24.890199))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
print 200
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(65.400000, 29.100000), point2=(65.400000, 28.350000))
s0.Line(point1=(65.400000, 28.350000), point2=(64.650000, 27.450000))
s0.Line(point1=(64.650000, 27.450000), point2=(63.450000, 26.250000))
s0.Line(point1=(63.450000, 26.250000), point2=(63.000000, 26.250000))
s0.Line(point1=(63.000000, 26.250000), point2=(63.300000, 27.750000))
s0.Line(point1=(63.300000, 27.750000), point2=(63.900000, 28.350000))
s0.Line(point1=(63.900000, 28.350000), point2=(64.500000, 28.350000))
s0.Line(point1=(64.500000, 28.350000), point2=(64.950000, 29.100000))
s0.Line(point1=(64.950000, 29.100000), point2=(65.400000, 29.100000))
s0.Line(point1=(65.500000, 29.200000), point2=(65.576822, 28.285982))
s0.Line(point1=(65.576822, 28.285982), point2=(64.797533, 27.315271))
s0.Line(point1=(64.797533, 27.315271), point2=(63.520711, 26.079289))
s0.Line(point1=(63.520711, 26.079289), point2=(62.901942, 26.169612))
s0.Line(point1=(62.901942, 26.169612), point2=(63.131231, 27.840322))
s0.Line(point1=(63.131231, 27.840322), point2=(63.829289, 28.520711))
s0.Line(point1=(63.829289, 28.520711), point2=(64.414251, 28.501450))
s0.Line(point1=(64.414251, 28.501450), point2=(64.864251, 29.251450))
s0.Line(point1=(64.864251, 29.251450), point2=(65.500000, 29.200000))
s0.Line(point1=(65.300000, 29.000000), point2=(65.223178, 28.414018))
s0.Line(point1=(65.223178, 28.414018), point2=(64.502467, 27.584729))
s0.Line(point1=(64.502467, 27.584729), point2=(63.379289, 26.420711))
s0.Line(point1=(63.379289, 26.420711), point2=(63.098058, 26.330388))
s0.Line(point1=(63.098058, 26.330388), point2=(63.468769, 27.659678))
s0.Line(point1=(63.468769, 27.659678), point2=(63.970711, 28.179289))
s0.Line(point1=(63.970711, 28.179289), point2=(64.585749, 28.198550))
s0.Line(point1=(64.585749, 28.198550), point2=(65.035749, 28.948550))
s0.Line(point1=(65.035749, 28.948550), point2=(65.300000, 29.000000))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(64.950000, 41.100000), point2=(66.750000, 41.100000))
s0.Line(point1=(66.750000, 41.100000), point2=(66.900000, 40.800000))
s0.Line(point1=(66.900000, 40.800000), point2=(67.050000, 36.450000))
s0.Line(point1=(67.050000, 36.450000), point2=(63.600000, 37.200000))
s0.Line(point1=(63.600000, 37.200000), point2=(63.300000, 37.650000))
s0.Line(point1=(63.300000, 37.650000), point2=(63.300000, 38.250000))
s0.Line(point1=(63.300000, 38.250000), point2=(63.600000, 38.250000))
s0.Line(point1=(63.600000, 38.250000), point2=(64.500000, 40.650000))
s0.Line(point1=(64.500000, 40.650000), point2=(64.950000, 41.100000))
s0.Line(point1=(64.879289, 41.270711), point2=(66.839443, 41.244721))
s0.Line(point1=(66.839443, 41.244721), point2=(67.089383, 40.848168))
s0.Line(point1=(67.089383, 40.848168), point2=(67.128698, 36.355729))
s0.Line(point1=(67.128698, 36.355729), point2=(63.495552, 37.046812))
s0.Line(point1=(63.495552, 37.046812), point2=(63.116795, 37.594530))
s0.Line(point1=(63.116795, 37.594530), point2=(63.200000, 38.350000))
s0.Line(point1=(63.200000, 38.350000), point2=(63.506367, 38.385112))
s0.Line(point1=(63.506367, 38.385112), point2=(64.335656, 40.755823))
s0.Line(point1=(64.335656, 40.755823), point2=(64.879289, 41.270711))
s0.Line(point1=(65.020711, 40.929289), point2=(66.660557, 40.955279))
s0.Line(point1=(66.660557, 40.955279), point2=(66.710617, 40.751832))
s0.Line(point1=(66.710617, 40.751832), point2=(66.971302, 36.544271))
s0.Line(point1=(66.971302, 36.544271), point2=(63.704448, 37.353188))
s0.Line(point1=(63.704448, 37.353188), point2=(63.483205, 37.705470))
s0.Line(point1=(63.483205, 37.705470), point2=(63.400000, 38.150000))
s0.Line(point1=(63.400000, 38.150000), point2=(63.693633, 38.114888))
s0.Line(point1=(63.693633, 38.114888), point2=(64.664344, 40.544177))
s0.Line(point1=(64.664344, 40.544177), point2=(65.020711, 40.929289))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(64.200000, 48.900000), point2=(65.400000, 49.500000))
s0.Line(point1=(65.400000, 49.500000), point2=(67.050000, 49.350000))
s0.Line(point1=(67.050000, 49.350000), point2=(67.650000, 48.300000))
s0.Line(point1=(67.650000, 48.300000), point2=(67.200000, 47.400000))
s0.Line(point1=(67.200000, 47.400000), point2=(67.350000, 46.950000))
s0.Line(point1=(67.350000, 46.950000), point2=(66.000000, 47.250000))
s0.Line(point1=(66.000000, 47.250000), point2=(64.200000, 48.900000))
s0.Line(point1=(64.087706, 48.915727), point2=(65.364332, 49.689032))
s0.Line(point1=(65.364332, 49.689032), point2=(67.145878, 49.499203))
s0.Line(point1=(67.145878, 49.499203), point2=(67.826267, 48.304893))
s0.Line(point1=(67.826267, 48.304893), point2=(67.384311, 47.386901))
s0.Line(point1=(67.384311, 47.386901), point2=(67.423175, 46.884004))
s0.Line(point1=(67.423175, 46.884004), point2=(65.910734, 47.078666))
s0.Line(point1=(65.910734, 47.078666), point2=(64.087706, 48.915727))
s0.Line(point1=(64.312294, 48.884273), point2=(65.435668, 49.310968))
s0.Line(point1=(65.435668, 49.310968), point2=(66.954122, 49.200797))
s0.Line(point1=(66.954122, 49.200797), point2=(67.473733, 48.295107))
s0.Line(point1=(67.473733, 48.295107), point2=(67.015689, 47.413099))
s0.Line(point1=(67.015689, 47.413099), point2=(67.276825, 47.015996))
s0.Line(point1=(67.276825, 47.015996), point2=(66.089266, 47.421334))
s0.Line(point1=(66.089266, 47.421334), point2=(64.312294, 48.884273))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(64.650000, 3.000000), point2=(65.700000, 3.000000))
s0.Line(point1=(65.700000, 3.000000), point2=(66.750000, 2.250000))
s0.Line(point1=(66.750000, 2.250000), point2=(66.600000, 0.600000))
s0.Line(point1=(66.600000, 0.600000), point2=(65.850000, 0.600000))
s0.Line(point1=(65.850000, 0.600000), point2=(65.100000, 1.350000))
s0.Line(point1=(65.100000, 1.350000), point2=(64.650000, 3.000000))
s0.Line(point1=(64.553524, 3.073688), point2=(65.758124, 3.181373))
s0.Line(point1=(65.758124, 3.181373), point2=(66.907713, 2.322320))
s0.Line(point1=(66.907713, 2.322320), point2=(66.699589, 0.490946))
s0.Line(point1=(66.699589, 0.490946), point2=(65.779289, 0.429289))
s0.Line(point1=(65.779289, 0.429289), point2=(64.932813, 1.252978))
s0.Line(point1=(64.932813, 1.252978), point2=(64.553524, 3.073688))
s0.Line(point1=(64.746476, 2.926312), point2=(65.641876, 2.818627))
s0.Line(point1=(65.641876, 2.818627), point2=(66.592287, 2.177680))
s0.Line(point1=(66.592287, 2.177680), point2=(66.500411, 0.709054))
s0.Line(point1=(66.500411, 0.709054), point2=(65.920711, 0.770711))
s0.Line(point1=(65.920711, 0.770711), point2=(65.267187, 1.447022))
s0.Line(point1=(65.267187, 1.447022), point2=(64.746476, 2.926312))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(66.150000, 44.850000), point2=(66.900000, 43.950000))
s0.Line(point1=(66.900000, 43.950000), point2=(66.900000, 43.350000))
s0.Line(point1=(66.900000, 43.350000), point2=(65.400000, 42.450000))
s0.Line(point1=(65.400000, 42.450000), point2=(64.800000, 44.400000))
s0.Line(point1=(64.800000, 44.400000), point2=(65.400000, 44.850000))
s0.Line(point1=(65.400000, 44.850000), point2=(66.150000, 44.850000))
s0.Line(point1=(66.226822, 45.014018), point2=(67.076822, 44.014018))
s0.Line(point1=(67.076822, 44.014018), point2=(67.051450, 43.264251))
s0.Line(point1=(67.051450, 43.264251), point2=(65.355872, 42.334842))
s0.Line(point1=(65.355872, 42.334842), point2=(64.644422, 44.450591))
s0.Line(point1=(64.644422, 44.450591), point2=(65.340000, 45.030000))
s0.Line(point1=(65.340000, 45.030000), point2=(66.226822, 45.014018))
s0.Line(point1=(66.073178, 44.685982), point2=(66.723178, 43.885982))
s0.Line(point1=(66.723178, 43.885982), point2=(66.748550, 43.435749))
s0.Line(point1=(66.748550, 43.435749), point2=(65.444128, 42.565158))
s0.Line(point1=(65.444128, 42.565158), point2=(64.955578, 44.349409))
s0.Line(point1=(64.955578, 44.349409), point2=(65.460000, 44.670000))
s0.Line(point1=(65.460000, 44.670000), point2=(66.073178, 44.685982))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(69.750000, 17.400000), point2=(69.600000, 16.350000))
s0.Line(point1=(69.600000, 16.350000), point2=(68.700000, 14.850000))
s0.Line(point1=(68.700000, 14.850000), point2=(67.200000, 14.850000))
s0.Line(point1=(67.200000, 14.850000), point2=(64.950000, 15.450000))
s0.Line(point1=(64.950000, 15.450000), point2=(64.800000, 16.950000))
s0.Line(point1=(64.800000, 16.950000), point2=(65.250000, 17.100000))
s0.Line(point1=(65.250000, 17.100000), point2=(65.550000, 17.850000))
s0.Line(point1=(65.550000, 17.850000), point2=(69.150000, 18.000000))
s0.Line(point1=(69.150000, 18.000000), point2=(69.750000, 17.400000))
s0.Line(point1=(69.919706, 17.456569), point2=(69.784744, 16.284408))
s0.Line(point1=(69.784744, 16.284408), point2=(68.785749, 14.698550))
s0.Line(point1=(68.785749, 14.698550), point2=(67.174234, 14.653377))
s0.Line(point1=(67.174234, 14.653377), point2=(64.824730, 15.343426))
s0.Line(point1=(64.824730, 15.343426), point2=(64.668874, 17.034918))
s0.Line(point1=(64.668874, 17.034918), point2=(65.125530, 17.232007))
s0.Line(point1=(65.125530, 17.232007), point2=(65.452989, 17.987052))
s0.Line(point1=(65.452989, 17.987052), point2=(69.216548, 18.170624))
s0.Line(point1=(69.216548, 18.170624), point2=(69.919706, 17.456569))
s0.Line(point1=(69.580294, 17.343431), point2=(69.415256, 16.415592))
s0.Line(point1=(69.415256, 16.415592), point2=(68.614251, 15.001450))
s0.Line(point1=(68.614251, 15.001450), point2=(67.225766, 15.046623))
s0.Line(point1=(67.225766, 15.046623), point2=(65.075270, 15.556574))
s0.Line(point1=(65.075270, 15.556574), point2=(64.931126, 16.865082))
s0.Line(point1=(64.931126, 16.865082), point2=(65.374470, 16.967993))
s0.Line(point1=(65.374470, 16.967993), point2=(65.647011, 17.712948))
s0.Line(point1=(65.647011, 17.712948), point2=(69.083452, 17.829376))
s0.Line(point1=(69.083452, 17.829376), point2=(69.580294, 17.343431))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(65.700000, 35.550000), point2=(66.900000, 35.250000))
s0.Line(point1=(66.900000, 35.250000), point2=(68.550000, 33.900000))
s0.Line(point1=(68.550000, 33.900000), point2=(68.550000, 33.150000))
s0.Line(point1=(68.550000, 33.150000), point2=(67.650000, 31.800000))
s0.Line(point1=(67.650000, 31.800000), point2=(67.350000, 31.800000))
s0.Line(point1=(67.350000, 31.800000), point2=(65.700000, 34.350000))
s0.Line(point1=(65.700000, 34.350000), point2=(65.400000, 35.250000))
s0.Line(point1=(65.400000, 35.250000), point2=(65.700000, 35.550000))
s0.Line(point1=(65.653543, 35.717725), point2=(66.987577, 35.424410))
s0.Line(point1=(66.987577, 35.424410), point2=(68.713324, 33.977396))
s0.Line(point1=(68.713324, 33.977396), point2=(68.733205, 33.094530))
s0.Line(point1=(68.733205, 33.094530), point2=(67.733205, 31.644530))
s0.Line(point1=(67.733205, 31.644530), point2=(67.266043, 31.645675))
s0.Line(point1=(67.266043, 31.645675), point2=(65.521175, 34.264052))
s0.Line(point1=(65.521175, 34.264052), point2=(65.234421, 35.289088))
s0.Line(point1=(65.234421, 35.289088), point2=(65.653543, 35.717725))
s0.Line(point1=(65.746457, 35.382275), point2=(66.812423, 35.075590))
s0.Line(point1=(66.812423, 35.075590), point2=(68.386676, 33.822604))
s0.Line(point1=(68.386676, 33.822604), point2=(68.366795, 33.205470))
s0.Line(point1=(68.366795, 33.205470), point2=(67.566795, 31.955470))
s0.Line(point1=(67.566795, 31.955470), point2=(67.433957, 31.954325))
s0.Line(point1=(67.433957, 31.954325), point2=(65.878825, 34.435948))
s0.Line(point1=(65.878825, 34.435948), point2=(65.565579, 35.210912))
s0.Line(point1=(65.565579, 35.210912), point2=(65.746457, 35.382275))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(70.050000, 27.000000), point2=(70.050000, 26.250000))
s0.Line(point1=(70.050000, 26.250000), point2=(69.000000, 26.100000))
s0.Line(point1=(69.000000, 26.100000), point2=(68.400000, 26.400000))
s0.Line(point1=(68.400000, 26.400000), point2=(67.500000, 25.650000))
s0.Line(point1=(67.500000, 25.650000), point2=(66.000000, 25.800000))
s0.Line(point1=(66.000000, 25.800000), point2=(65.700000, 26.250000))
s0.Line(point1=(65.700000, 26.250000), point2=(65.700000, 26.850000))
s0.Line(point1=(65.700000, 26.850000), point2=(66.450000, 27.750000))
s0.Line(point1=(66.450000, 27.750000), point2=(66.450000, 28.500000))
s0.Line(point1=(66.450000, 28.500000), point2=(69.600000, 27.450000))
s0.Line(point1=(69.600000, 27.450000), point2=(70.050000, 27.000000))
s0.Line(point1=(70.220711, 27.070711), point2=(70.164142, 26.151005))
s0.Line(point1=(70.164142, 26.151005), point2=(68.969421, 25.911562))
s0.Line(point1=(68.969421, 25.911562), point2=(68.419297, 26.233735))
s0.Line(point1=(68.419297, 26.233735), point2=(67.554068, 25.473674))
s0.Line(point1=(67.554068, 25.473674), point2=(65.906845, 25.645026))
s0.Line(point1=(65.906845, 25.645026), point2=(65.516795, 26.194530))
s0.Line(point1=(65.516795, 26.194530), point2=(65.523178, 26.914018))
s0.Line(point1=(65.523178, 26.914018), point2=(66.273178, 27.814018))
s0.Line(point1=(66.273178, 27.814018), point2=(66.381623, 28.594868))
s0.Line(point1=(66.381623, 28.594868), point2=(69.702333, 27.615579))
s0.Line(point1=(69.702333, 27.615579), point2=(70.220711, 27.070711))
s0.Line(point1=(69.879289, 26.929289), point2=(69.935858, 26.348995))
s0.Line(point1=(69.935858, 26.348995), point2=(69.030579, 26.288438))
s0.Line(point1=(69.030579, 26.288438), point2=(68.380703, 26.566265))
s0.Line(point1=(68.380703, 26.566265), point2=(67.445932, 25.826326))
s0.Line(point1=(67.445932, 25.826326), point2=(66.093155, 25.954974))
s0.Line(point1=(66.093155, 25.954974), point2=(65.883205, 26.305470))
s0.Line(point1=(65.883205, 26.305470), point2=(65.876822, 26.785982))
s0.Line(point1=(65.876822, 26.785982), point2=(66.626822, 27.685982))
s0.Line(point1=(66.626822, 27.685982), point2=(66.518377, 28.405132))
s0.Line(point1=(66.518377, 28.405132), point2=(69.497667, 27.284421))
s0.Line(point1=(69.497667, 27.284421), point2=(69.879289, 26.929289))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(65.700000, 13.200000), point2=(66.750000, 13.350000))
s0.Line(point1=(66.750000, 13.350000), point2=(67.200000, 13.800000))
s0.Line(point1=(67.200000, 13.800000), point2=(68.400000, 13.800000))
s0.Line(point1=(68.400000, 13.800000), point2=(69.000000, 13.200000))
s0.Line(point1=(69.000000, 13.200000), point2=(69.150000, 12.300000))
s0.Line(point1=(69.150000, 12.300000), point2=(67.050000, 12.600000))
s0.Line(point1=(67.050000, 12.600000), point2=(66.900000, 12.300000))
s0.Line(point1=(66.900000, 12.300000), point2=(65.700000, 12.300000))
s0.Line(point1=(65.700000, 12.300000), point2=(65.700000, 13.200000))
s0.Line(point1=(65.585858, 13.298995), point2=(66.665147, 13.519706))
s0.Line(point1=(66.665147, 13.519706), point2=(67.129289, 13.970711))
s0.Line(point1=(67.129289, 13.970711), point2=(68.470711, 13.970711))
s0.Line(point1=(68.470711, 13.970711), point2=(69.169350, 13.287151))
s0.Line(point1=(69.169350, 13.287151), point2=(69.234497, 12.217445))
s0.Line(point1=(69.234497, 12.217445), point2=(67.125301, 12.456284))
s0.Line(point1=(67.125301, 12.456284), point2=(66.989443, 12.155279))
s0.Line(point1=(66.989443, 12.155279), point2=(65.600000, 12.200000))
s0.Line(point1=(65.600000, 12.200000), point2=(65.585858, 13.298995))
s0.Line(point1=(65.814142, 13.101005), point2=(66.834853, 13.180294))
s0.Line(point1=(66.834853, 13.180294), point2=(67.270711, 13.629289))
s0.Line(point1=(67.270711, 13.629289), point2=(68.329289, 13.629289))
s0.Line(point1=(68.329289, 13.629289), point2=(68.830650, 13.112849))
s0.Line(point1=(68.830650, 13.112849), point2=(69.065503, 12.382555))
s0.Line(point1=(69.065503, 12.382555), point2=(66.974699, 12.743716))
s0.Line(point1=(66.974699, 12.743716), point2=(66.810557, 12.444721))
s0.Line(point1=(66.810557, 12.444721), point2=(65.800000, 12.400000))
s0.Line(point1=(65.800000, 12.400000), point2=(65.814142, 13.101005))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(66.750000, 11.550000), point2=(67.800000, 11.400000))
s0.Line(point1=(67.800000, 11.400000), point2=(69.000000, 10.500000))
s0.Line(point1=(69.000000, 10.500000), point2=(67.950000, 8.850000))
s0.Line(point1=(67.950000, 8.850000), point2=(66.450000, 10.350000))
s0.Line(point1=(66.450000, 10.350000), point2=(66.750000, 11.550000))
s0.Line(point1=(66.667128, 11.673249), point2=(67.874142, 11.578995))
s0.Line(point1=(67.874142, 11.578995), point2=(69.144366, 10.526312))
s0.Line(point1=(69.144366, 10.526312), point2=(67.963655, 8.725602))
s0.Line(point1=(67.963655, 8.725602), point2=(66.282275, 10.303543))
s0.Line(point1=(66.282275, 10.303543), point2=(66.667128, 11.673249))
s0.Line(point1=(66.832872, 11.426751), point2=(67.725858, 11.221005))
s0.Line(point1=(67.725858, 11.221005), point2=(68.855634, 10.473688))
s0.Line(point1=(68.855634, 10.473688), point2=(67.936345, 8.974398))
s0.Line(point1=(67.936345, 8.974398), point2=(66.617725, 10.396457))
s0.Line(point1=(66.617725, 10.396457), point2=(66.832872, 11.426751))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(68.250000, 24.750000), point2=(67.650000, 22.800000))
s0.Line(point1=(67.650000, 22.800000), point2=(67.050000, 22.800000))
s0.Line(point1=(67.050000, 22.800000), point2=(66.750000, 24.450000))
s0.Line(point1=(66.750000, 24.450000), point2=(68.250000, 24.750000))
s0.Line(point1=(68.325966, 24.818649), point2=(67.745578, 22.670591))
s0.Line(point1=(67.745578, 22.670591), point2=(66.951613, 22.682111))
s0.Line(point1=(66.951613, 22.682111), point2=(66.632001, 24.530170))
s0.Line(point1=(66.632001, 24.530170), point2=(68.325966, 24.818649))
s0.Line(point1=(68.174034, 24.681351), point2=(67.554422, 22.929409))
s0.Line(point1=(67.554422, 22.929409), point2=(67.148387, 22.917889))
s0.Line(point1=(67.148387, 22.917889), point2=(66.867999, 24.369830))
s0.Line(point1=(66.867999, 24.369830), point2=(68.174034, 24.681351))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(66.900000, 21.150000), point2=(68.100000, 21.150000))
s0.Line(point1=(68.100000, 21.150000), point2=(68.850000, 19.950000))
s0.Line(point1=(68.850000, 19.950000), point2=(69.150000, 19.950000))
s0.Line(point1=(69.150000, 19.950000), point2=(69.600000, 18.450000))
s0.Line(point1=(69.600000, 18.450000), point2=(67.950000, 18.750000))
s0.Line(point1=(67.950000, 18.750000), point2=(67.200000, 19.350000))
s0.Line(point1=(67.200000, 19.350000), point2=(66.900000, 19.650000))
s0.Line(point1=(66.900000, 19.650000), point2=(66.900000, 21.150000))
s0.Line(point1=(66.800000, 21.250000), point2=(68.184800, 21.303000))
s0.Line(point1=(68.184800, 21.303000), point2=(68.934800, 20.103000))
s0.Line(point1=(68.934800, 20.103000), point2=(69.245783, 20.078735))
s0.Line(point1=(69.245783, 20.078735), point2=(69.677894, 18.380348))
s0.Line(point1=(69.677894, 18.380348), point2=(67.869642, 18.573526))
s0.Line(point1=(67.869642, 18.573526), point2=(67.066820, 19.201202))
s0.Line(point1=(67.066820, 19.201202), point2=(66.729289, 19.579289))
s0.Line(point1=(66.729289, 19.579289), point2=(66.800000, 21.250000))
s0.Line(point1=(67.000000, 21.050000), point2=(68.015200, 20.997000))
s0.Line(point1=(68.015200, 20.997000), point2=(68.765200, 19.797000))
s0.Line(point1=(68.765200, 19.797000), point2=(69.054217, 19.821265))
s0.Line(point1=(69.054217, 19.821265), point2=(69.522106, 18.519652))
s0.Line(point1=(69.522106, 18.519652), point2=(68.030358, 18.926474))
s0.Line(point1=(68.030358, 18.926474), point2=(67.333180, 19.498798))
s0.Line(point1=(67.333180, 19.498798), point2=(67.070711, 19.720711))
s0.Line(point1=(67.070711, 19.720711), point2=(67.000000, 21.050000))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(68.550000, 45.450000), point2=(69.000000, 44.250000))
s0.Line(point1=(69.000000, 44.250000), point2=(67.800000, 43.200000))
s0.Line(point1=(67.800000, 43.200000), point2=(67.350000, 44.100000))
s0.Line(point1=(67.350000, 44.100000), point2=(68.250000, 44.850000))
s0.Line(point1=(68.250000, 44.850000), point2=(68.250000, 45.450000))
s0.Line(point1=(68.250000, 45.450000), point2=(68.550000, 45.450000))
s0.Line(point1=(68.643633, 45.585112), point2=(69.159483, 44.209855))
s0.Line(point1=(69.159483, 44.209855), point2=(67.776408, 43.080021))
s0.Line(point1=(67.776408, 43.080021), point2=(67.196539, 44.132101))
s0.Line(point1=(67.196539, 44.132101), point2=(68.085982, 44.926822))
s0.Line(point1=(68.085982, 44.926822), point2=(68.150000, 45.550000))
s0.Line(point1=(68.150000, 45.550000), point2=(68.643633, 45.585112))
s0.Line(point1=(68.456367, 45.314888), point2=(68.840517, 44.290145))
s0.Line(point1=(68.840517, 44.290145), point2=(67.823592, 43.319979))
s0.Line(point1=(67.823592, 43.319979), point2=(67.503461, 44.067899))
s0.Line(point1=(67.503461, 44.067899), point2=(68.414018, 44.773178))
s0.Line(point1=(68.414018, 44.773178), point2=(68.350000, 45.350000))
s0.Line(point1=(68.350000, 45.350000), point2=(68.456367, 45.314888))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(67.800000, 51.300000), point2=(69.150000, 51.450000))
s0.Line(point1=(69.150000, 51.450000), point2=(69.300000, 51.150000))
s0.Line(point1=(69.300000, 51.150000), point2=(70.500000, 51.000000))
s0.Line(point1=(70.500000, 51.000000), point2=(71.400000, 50.550000))
s0.Line(point1=(71.400000, 50.550000), point2=(71.400000, 49.950000))
s0.Line(point1=(71.400000, 49.950000), point2=(70.650000, 49.950000))
s0.Line(point1=(70.650000, 49.950000), point2=(70.650000, 49.350000))
s0.Line(point1=(70.650000, 49.350000), point2=(70.200000, 49.350000))
s0.Line(point1=(70.200000, 49.350000), point2=(69.600000, 49.950000))
s0.Line(point1=(69.600000, 49.950000), point2=(68.100000, 49.950000))
s0.Line(point1=(68.100000, 49.950000), point2=(67.800000, 50.250000))
s0.Line(point1=(67.800000, 50.250000), point2=(67.800000, 51.300000))
s0.Line(point1=(67.688957, 51.399388), point2=(69.228400, 51.594110))
s0.Line(point1=(69.228400, 51.594110), point2=(69.401846, 51.293949))
s0.Line(point1=(69.401846, 51.293949), point2=(70.557125, 51.188671))
s0.Line(point1=(70.557125, 51.188671), point2=(71.544721, 50.639443))
s0.Line(point1=(71.544721, 50.639443), point2=(71.500000, 49.850000))
s0.Line(point1=(71.500000, 49.850000), point2=(70.750000, 49.850000))
s0.Line(point1=(70.750000, 49.850000), point2=(70.750000, 49.250000))
s0.Line(point1=(70.750000, 49.250000), point2=(70.129289, 49.179289))
s0.Line(point1=(70.129289, 49.179289), point2=(69.529289, 49.779289))
s0.Line(point1=(69.529289, 49.779289), point2=(68.029289, 49.779289))
s0.Line(point1=(68.029289, 49.779289), point2=(67.629289, 50.179289))
s0.Line(point1=(67.629289, 50.179289), point2=(67.688957, 51.399388))
s0.Line(point1=(67.911043, 51.200612), point2=(69.071600, 51.305890))
s0.Line(point1=(69.071600, 51.305890), point2=(69.198154, 51.006051))
s0.Line(point1=(69.198154, 51.006051), point2=(70.442875, 50.811329))
s0.Line(point1=(70.442875, 50.811329), point2=(71.255279, 50.460557))
s0.Line(point1=(71.255279, 50.460557), point2=(71.300000, 50.050000))
s0.Line(point1=(71.300000, 50.050000), point2=(70.550000, 50.050000))
s0.Line(point1=(70.550000, 50.050000), point2=(70.550000, 49.450000))
s0.Line(point1=(70.550000, 49.450000), point2=(70.270711, 49.520711))
s0.Line(point1=(70.270711, 49.520711), point2=(69.670711, 50.120711))
s0.Line(point1=(69.670711, 50.120711), point2=(68.170711, 50.120711))
s0.Line(point1=(68.170711, 50.120711), point2=(67.970711, 50.320711))
s0.Line(point1=(67.970711, 50.320711), point2=(67.911043, 51.200612))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(68.250000, 7.650000), point2=(69.300000, 7.350000))
s0.Line(point1=(69.300000, 7.350000), point2=(73.500000, 7.350000))
s0.Line(point1=(73.500000, 7.350000), point2=(75.000000, 6.900000))
s0.Line(point1=(75.000000, 6.900000), point2=(75.000000, 0.000000))
s0.Line(point1=(75.000000, 0.000000), point2=(71.550000, 0.000000))
s0.Line(point1=(71.550000, 0.000000), point2=(68.100000, 1.500000))
s0.Line(point1=(68.100000, 1.500000), point2=(68.250000, 3.900000))
s0.Line(point1=(68.250000, 3.900000), point2=(68.850000, 4.800000))
s0.Line(point1=(68.850000, 4.800000), point2=(68.700000, 5.850000))
s0.Line(point1=(68.700000, 5.850000), point2=(68.100000, 6.900000))
s0.Line(point1=(68.100000, 6.900000), point2=(68.250000, 7.650000))
s0.Line(point1=(68.179414, 7.765764), point2=(69.327472, 7.546152))
s0.Line(point1=(69.327472, 7.546152), point2=(73.528735, 7.545783))
s0.Line(point1=(73.528735, 7.545783), point2=(75.000000, 6.995783))
s0.Line(point1=(75.000000, 6.995783), point2=(75.000000, 0.000000))
s0.Line(point1=(75.000000, 0.000000), point2=(71.510127, 0.000000))
s0.Line(point1=(71.510127, 0.000000), point2=(67.960322, 1.414531))
s0.Line(point1=(67.960322, 1.414531), point2=(68.066990, 3.961708))
s0.Line(point1=(68.066990, 3.961708), point2=(68.667800, 4.841328))
s0.Line(point1=(68.667800, 4.841328), point2=(68.514181, 5.786244))
s0.Line(point1=(68.514181, 5.786244), point2=(67.915118, 6.869998))
s0.Line(point1=(67.915118, 6.869998), point2=(68.179414, 7.765764))
s0.Line(point1=(68.320586, 7.534236), point2=(69.272528, 7.153848))
s0.Line(point1=(69.272528, 7.153848), point2=(73.471265, 7.154217))
s0.Line(point1=(73.471265, 7.154217), point2=(75.000000, 6.804217))
s0.Line(point1=(75.000000, 6.804217), point2=(75.000000, 0.000000))
s0.Line(point1=(75.000000, 0.000000), point2=(71.589873, 0.000000))
s0.Line(point1=(71.589873, 0.000000), point2=(68.239678, 1.585469))
s0.Line(point1=(68.239678, 1.585469), point2=(68.433010, 3.838292))
s0.Line(point1=(68.433010, 3.838292), point2=(69.032200, 4.758672))
s0.Line(point1=(69.032200, 4.758672), point2=(68.885819, 5.913756))
s0.Line(point1=(68.885819, 5.913756), point2=(68.284882, 6.930002))
s0.Line(point1=(68.284882, 6.930002), point2=(68.320586, 7.534236))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(68.400000, 23.100000), point2=(69.000000, 23.550000))
s0.Line(point1=(69.000000, 23.550000), point2=(69.900000, 23.400000))
s0.Line(point1=(69.900000, 23.400000), point2=(69.900000, 22.200000))
s0.Line(point1=(69.900000, 22.200000), point2=(68.850000, 22.350000))
s0.Line(point1=(68.850000, 22.350000), point2=(68.400000, 23.100000))
s0.Line(point1=(68.254251, 23.128550), point2=(68.956440, 23.728639))
s0.Line(point1=(68.956440, 23.728639), point2=(70.016440, 23.498639))
s0.Line(point1=(70.016440, 23.498639), point2=(69.985858, 22.101005))
s0.Line(point1=(69.985858, 22.101005), point2=(68.750109, 22.199555))
s0.Line(point1=(68.750109, 22.199555), point2=(68.254251, 23.128550))
s0.Line(point1=(68.545749, 23.071450), point2=(69.043560, 23.371361))
s0.Line(point1=(69.043560, 23.371361), point2=(69.783560, 23.301361))
s0.Line(point1=(69.783560, 23.301361), point2=(69.814142, 22.298995))
s0.Line(point1=(69.814142, 22.298995), point2=(68.949891, 22.500445))
s0.Line(point1=(68.949891, 22.500445), point2=(68.545749, 23.071450))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(70.200000, 41.700000), point2=(70.500000, 40.500000))
s0.Line(point1=(70.500000, 40.500000), point2=(71.550000, 39.450000))
s0.Line(point1=(71.550000, 39.450000), point2=(71.400000, 36.750000))
s0.Line(point1=(71.400000, 36.750000), point2=(70.050000, 36.900000))
s0.Line(point1=(70.050000, 36.900000), point2=(68.550000, 38.400000))
s0.Line(point1=(68.550000, 38.400000), point2=(68.700000, 39.900000))
s0.Line(point1=(68.700000, 39.900000), point2=(70.200000, 41.700000))
s0.Line(point1=(70.220192, 41.788272), point2=(70.667725, 40.594964))
s0.Line(point1=(70.667725, 40.594964), point2=(71.720557, 39.515164))
s0.Line(point1=(71.720557, 39.515164), point2=(71.488803, 36.645065))
s0.Line(point1=(71.488803, 36.645065), point2=(69.968246, 36.729901))
s0.Line(point1=(69.968246, 36.729901), point2=(68.379786, 38.339240))
s0.Line(point1=(68.379786, 38.339240), point2=(68.523674, 39.973969))
s0.Line(point1=(68.523674, 39.973969), point2=(70.220192, 41.788272))
s0.Line(point1=(70.179808, 41.611728), point2=(70.332275, 40.405036))
s0.Line(point1=(70.332275, 40.405036), point2=(71.379443, 39.384836))
s0.Line(point1=(71.379443, 39.384836), point2=(71.311197, 36.854935))
s0.Line(point1=(71.311197, 36.854935), point2=(70.131754, 37.070099))
s0.Line(point1=(70.131754, 37.070099), point2=(68.720214, 38.460760))
s0.Line(point1=(68.720214, 38.460760), point2=(68.876326, 39.826031))
s0.Line(point1=(68.876326, 39.826031), point2=(70.179808, 41.611728))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(69.000000, 29.550000), point2=(69.750000, 30.000000))
s0.Line(point1=(69.750000, 30.000000), point2=(69.750000, 30.450000))
s0.Line(point1=(69.750000, 30.450000), point2=(70.950000, 30.300000))
s0.Line(point1=(70.950000, 30.300000), point2=(72.600000, 29.100000))
s0.Line(point1=(72.600000, 29.100000), point2=(72.750000, 27.900000))
s0.Line(point1=(72.750000, 27.900000), point2=(71.700000, 27.750000))
s0.Line(point1=(71.700000, 27.750000), point2=(69.750000, 28.350000))
s0.Line(point1=(69.750000, 28.350000), point2=(69.150000, 28.800000))
s0.Line(point1=(69.150000, 28.800000), point2=(69.000000, 29.550000))
s0.Line(point1=(68.850492, 29.616138), point2=(69.598550, 30.085749))
s0.Line(point1=(69.598550, 30.085749), point2=(69.662403, 30.549228))
s0.Line(point1=(69.662403, 30.549228), point2=(71.021221, 30.480101))
s0.Line(point1=(71.021221, 30.480101), point2=(72.758045, 29.193277))
s0.Line(point1=(72.758045, 29.193277), point2=(72.863370, 27.813409))
s0.Line(point1=(72.863370, 27.813409), point2=(71.684734, 27.555427))
s0.Line(point1=(71.684734, 27.555427), point2=(69.660591, 28.174422))
s0.Line(point1=(69.660591, 28.174422), point2=(68.991942, 28.700388))
s0.Line(point1=(68.991942, 28.700388), point2=(68.850492, 29.616138))
s0.Line(point1=(69.149508, 29.483862), point2=(69.901450, 29.914251))
s0.Line(point1=(69.901450, 29.914251), point2=(69.837597, 30.350772))
s0.Line(point1=(69.837597, 30.350772), point2=(70.878779, 30.119899))
s0.Line(point1=(70.878779, 30.119899), point2=(72.441955, 29.006723))
s0.Line(point1=(72.441955, 29.006723), point2=(72.636630, 27.986591))
s0.Line(point1=(72.636630, 27.986591), point2=(71.715266, 27.944573))
s0.Line(point1=(71.715266, 27.944573), point2=(69.839409, 28.525578))
s0.Line(point1=(69.839409, 28.525578), point2=(69.308058, 28.899612))
s0.Line(point1=(69.308058, 28.899612), point2=(69.149508, 29.483862))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(69.750000, 35.100000), point2=(70.350000, 35.100000))
s0.Line(point1=(70.350000, 35.100000), point2=(70.800000, 33.600000))
s0.Line(point1=(70.800000, 33.600000), point2=(71.400000, 33.300000))
s0.Line(point1=(71.400000, 33.300000), point2=(71.400000, 32.250000))
s0.Line(point1=(71.400000, 32.250000), point2=(71.850000, 31.950000))
s0.Line(point1=(71.850000, 31.950000), point2=(72.600000, 30.000000))
s0.Line(point1=(72.600000, 30.000000), point2=(72.000000, 30.000000))
s0.Line(point1=(72.000000, 30.000000), point2=(71.700000, 30.600000))
s0.Line(point1=(71.700000, 30.600000), point2=(70.650000, 30.900000))
s0.Line(point1=(70.650000, 30.900000), point2=(70.050000, 31.650000))
s0.Line(point1=(70.050000, 31.650000), point2=(69.150000, 31.650000))
s0.Line(point1=(69.150000, 31.650000), point2=(69.150000, 32.400000))
s0.Line(point1=(69.150000, 32.400000), point2=(69.750000, 33.300000))
s0.Line(point1=(69.750000, 33.300000), point2=(69.750000, 35.100000))
s0.Line(point1=(69.650000, 35.200000), point2=(70.445783, 35.228735))
s0.Line(point1=(70.445783, 35.228735), point2=(70.940504, 33.718178))
s0.Line(point1=(70.940504, 33.718178), point2=(71.544721, 33.389443))
s0.Line(point1=(71.544721, 33.389443), point2=(71.555470, 32.333205))
s0.Line(point1=(71.555470, 32.333205), point2=(71.998805, 32.069103))
s0.Line(point1=(71.998805, 32.069103), point2=(72.693335, 29.935898))
s0.Line(point1=(72.693335, 29.935898), point2=(71.910557, 29.855279))
s0.Line(point1=(71.910557, 29.855279), point2=(71.583085, 30.459126))
s0.Line(point1=(71.583085, 30.459126), point2=(70.544441, 30.741378))
s0.Line(point1=(70.544441, 30.741378), point2=(69.971913, 31.487530))
s0.Line(point1=(69.971913, 31.487530), point2=(69.050000, 31.550000))
s0.Line(point1=(69.050000, 31.550000), point2=(68.966795, 32.455470))
s0.Line(point1=(68.966795, 32.455470), point2=(69.566795, 33.355470))
s0.Line(point1=(69.566795, 33.355470), point2=(69.650000, 35.200000))
s0.Line(point1=(69.850000, 35.000000), point2=(70.254217, 34.971265))
s0.Line(point1=(70.254217, 34.971265), point2=(70.659496, 33.481822))
s0.Line(point1=(70.659496, 33.481822), point2=(71.255279, 33.210557))
s0.Line(point1=(71.255279, 33.210557), point2=(71.244530, 32.166795))
s0.Line(point1=(71.244530, 32.166795), point2=(71.701195, 31.830897))
s0.Line(point1=(71.701195, 31.830897), point2=(72.506665, 30.064102))
s0.Line(point1=(72.506665, 30.064102), point2=(72.089443, 30.144721))
s0.Line(point1=(72.089443, 30.144721), point2=(71.816915, 30.740874))
s0.Line(point1=(71.816915, 30.740874), point2=(70.755559, 31.058622))
s0.Line(point1=(70.755559, 31.058622), point2=(70.128087, 31.812470))
s0.Line(point1=(70.128087, 31.812470), point2=(69.250000, 31.750000))
s0.Line(point1=(69.250000, 31.750000), point2=(69.333205, 32.344530))
s0.Line(point1=(69.333205, 32.344530), point2=(69.933205, 33.244530))
s0.Line(point1=(69.933205, 33.244530), point2=(69.850000, 35.000000))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(69.300000, 48.750000), point2=(70.350000, 48.300000))
s0.Line(point1=(70.350000, 48.300000), point2=(71.700000, 44.550000))
s0.Line(point1=(71.700000, 44.550000), point2=(72.900000, 42.750000))
s0.Line(point1=(72.900000, 42.750000), point2=(72.900000, 42.150000))
s0.Line(point1=(72.900000, 42.150000), point2=(71.550000, 42.150000))
s0.Line(point1=(71.550000, 42.150000), point2=(69.600000, 43.650000))
s0.Line(point1=(69.600000, 43.650000), point2=(69.300000, 48.750000))
s0.Line(point1=(69.239564, 48.836042), point2=(70.483481, 48.425786))
s0.Line(point1=(70.483481, 48.425786), point2=(71.877294, 44.639342))
s0.Line(point1=(71.877294, 44.639342), point2=(73.083205, 42.805470))
s0.Line(point1=(73.083205, 42.805470), point2=(73.000000, 42.050000))
s0.Line(point1=(73.000000, 42.050000), point2=(71.489029, 41.970738))
s0.Line(point1=(71.489029, 41.970738), point2=(69.439201, 43.564865))
s0.Line(point1=(69.439201, 43.564865), point2=(69.239564, 48.836042))
s0.Line(point1=(69.360436, 48.663958), point2=(70.216519, 48.174214))
s0.Line(point1=(70.216519, 48.174214), point2=(71.522706, 44.460658))
s0.Line(point1=(71.522706, 44.460658), point2=(72.716795, 42.694530))
s0.Line(point1=(72.716795, 42.694530), point2=(72.800000, 42.250000))
s0.Line(point1=(72.800000, 42.250000), point2=(71.610971, 42.329262))
s0.Line(point1=(71.610971, 42.329262), point2=(69.760799, 43.735135))
s0.Line(point1=(69.760799, 43.735135), point2=(69.360436, 48.663958))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
print 220
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(72.300000, 15.150000), point2=(72.450000, 14.400000))
s0.Line(point1=(72.450000, 14.400000), point2=(71.400000, 14.100000))
s0.Line(point1=(71.400000, 14.100000), point2=(70.800000, 13.500000))
s0.Line(point1=(70.800000, 13.500000), point2=(69.900000, 13.650000))
s0.Line(point1=(69.900000, 13.650000), point2=(69.750000, 14.850000))
s0.Line(point1=(69.750000, 14.850000), point2=(70.500000, 15.600000))
s0.Line(point1=(70.500000, 15.600000), point2=(71.250000, 15.750000))
s0.Line(point1=(71.250000, 15.750000), point2=(72.300000, 15.150000))
s0.Line(point1=(72.447672, 15.256436), point2=(72.575530, 14.323459))
s0.Line(point1=(72.575530, 14.323459), point2=(71.498183, 13.933137))
s0.Line(point1=(71.498183, 13.933137), point2=(70.854271, 13.330650))
s0.Line(point1=(70.854271, 13.330650), point2=(69.784332, 13.538957))
s0.Line(point1=(69.784332, 13.538957), point2=(69.580062, 14.908307))
s0.Line(point1=(69.580062, 14.908307), point2=(70.409678, 15.768769))
s0.Line(point1=(70.409678, 15.768769), point2=(71.280002, 15.934882))
s0.Line(point1=(71.280002, 15.934882), point2=(72.447672, 15.256436))
s0.Line(point1=(72.152328, 15.043564), point2=(72.324470, 14.476541))
s0.Line(point1=(72.324470, 14.476541), point2=(71.301817, 14.266863))
s0.Line(point1=(71.301817, 14.266863), point2=(70.745729, 13.669350))
s0.Line(point1=(70.745729, 13.669350), point2=(70.015668, 13.761043))
s0.Line(point1=(70.015668, 13.761043), point2=(69.919938, 14.791693))
s0.Line(point1=(69.919938, 14.791693), point2=(70.590322, 15.431231))
s0.Line(point1=(70.590322, 15.431231), point2=(71.219998, 15.565118))
s0.Line(point1=(71.219998, 15.565118), point2=(72.152328, 15.043564))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(69.900000, 10.650000), point2=(70.350000, 10.650000))
s0.Line(point1=(70.350000, 10.650000), point2=(70.950000, 9.300000))
s0.Line(point1=(70.950000, 9.300000), point2=(72.150000, 8.400000))
s0.Line(point1=(72.150000, 8.400000), point2=(72.150000, 7.800000))
s0.Line(point1=(72.150000, 7.800000), point2=(71.100000, 7.950000))
s0.Line(point1=(71.100000, 7.950000), point2=(70.200000, 8.550000))
s0.Line(point1=(70.200000, 8.550000), point2=(69.900000, 10.650000))
s0.Line(point1=(69.801005, 10.735858), point2=(70.441381, 10.790614))
s0.Line(point1=(70.441381, 10.790614), point2=(71.101381, 9.420614))
s0.Line(point1=(71.101381, 9.420614), point2=(72.310000, 8.480000))
s0.Line(point1=(72.310000, 8.480000), point2=(72.235858, 7.701005))
s0.Line(point1=(72.235858, 7.701005), point2=(71.030388, 7.767800))
s0.Line(point1=(71.030388, 7.767800), point2=(70.045535, 8.452653))
s0.Line(point1=(70.045535, 8.452653), point2=(69.801005, 10.735858))
s0.Line(point1=(69.998995, 10.564142), point2=(70.258619, 10.509386))
s0.Line(point1=(70.258619, 10.509386), point2=(70.798619, 9.179386))
s0.Line(point1=(70.798619, 9.179386), point2=(71.990000, 8.320000))
s0.Line(point1=(71.990000, 8.320000), point2=(72.064142, 7.898995))
s0.Line(point1=(72.064142, 7.898995), point2=(71.169612, 8.132200))
s0.Line(point1=(71.169612, 8.132200), point2=(70.354465, 8.647347))
s0.Line(point1=(70.354465, 8.647347), point2=(69.998995, 10.564142))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(73.350000, 27.300000), point2=(73.350000, 26.850000))
s0.Line(point1=(73.350000, 26.850000), point2=(72.450000, 25.800000))
s0.Line(point1=(72.450000, 25.800000), point2=(71.400000, 25.500000))
s0.Line(point1=(71.400000, 25.500000), point2=(71.250000, 25.050000))
s0.Line(point1=(71.250000, 25.050000), point2=(70.050000, 25.200000))
s0.Line(point1=(70.050000, 25.200000), point2=(70.350000, 26.400000))
s0.Line(point1=(70.350000, 26.400000), point2=(73.350000, 27.300000))
s0.Line(point1=(73.421265, 27.395783), point2=(73.525926, 26.784921))
s0.Line(point1=(73.525926, 26.784921), point2=(72.553398, 25.638768))
s0.Line(point1=(72.553398, 25.638768), point2=(71.522340, 25.372225))
s0.Line(point1=(71.522340, 25.372225), point2=(71.332465, 24.919149))
s0.Line(point1=(71.332465, 24.919149), point2=(69.940582, 25.125026))
s0.Line(point1=(69.940582, 25.125026), point2=(70.224251, 26.520036))
s0.Line(point1=(70.224251, 26.520036), point2=(73.421265, 27.395783))
s0.Line(point1=(73.278735, 27.204217), point2=(73.174074, 26.915079))
s0.Line(point1=(73.174074, 26.915079), point2=(72.346602, 25.961232))
s0.Line(point1=(72.346602, 25.961232), point2=(71.277660, 25.627775))
s0.Line(point1=(71.277660, 25.627775), point2=(71.167535, 25.180851))
s0.Line(point1=(71.167535, 25.180851), point2=(70.159418, 25.274974))
s0.Line(point1=(70.159418, 25.274974), point2=(70.475749, 26.279964))
s0.Line(point1=(70.475749, 26.279964), point2=(73.278735, 27.204217))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(71.400000, 52.500000), point2=(75.000000, 52.500000))
s0.Line(point1=(75.000000, 52.500000), point2=(75.000000, 45.900000))
s0.Line(point1=(75.000000, 45.900000), point2=(72.300000, 47.250000))
s0.Line(point1=(72.300000, 47.250000), point2=(72.150000, 48.000000))
s0.Line(point1=(72.150000, 48.000000), point2=(73.500000, 49.200000))
s0.Line(point1=(73.500000, 49.200000), point2=(73.500000, 49.950000))
s0.Line(point1=(73.500000, 49.950000), point2=(72.150000, 51.600000))
s0.Line(point1=(72.150000, 51.600000), point2=(71.400000, 52.050000))
s0.Line(point1=(71.400000, 52.050000), point2=(71.400000, 52.500000))
s0.Line(point1=(71.300000, 52.500000), point2=(75.000000, 52.500000))
s0.Line(point1=(75.000000, 52.500000), point2=(75.000000, 45.810557))
s0.Line(point1=(75.000000, 45.810557), point2=(72.157221, 47.140946))
s0.Line(point1=(72.157221, 47.140946), point2=(71.985506, 48.055129))
s0.Line(point1=(71.985506, 48.055129), point2=(73.333564, 49.274741))
s0.Line(point1=(73.333564, 49.274741), point2=(73.322604, 49.886676))
s0.Line(point1=(73.322604, 49.886676), point2=(72.021155, 51.450927))
s0.Line(point1=(72.021155, 51.450927), point2=(71.248550, 51.964251))
s0.Line(point1=(71.248550, 51.964251), point2=(71.300000, 52.500000))
s0.Line(point1=(71.500000, 52.500000), point2=(75.000000, 52.500000))
s0.Line(point1=(75.000000, 52.500000), point2=(75.000000, 45.989443))
s0.Line(point1=(75.000000, 45.989443), point2=(72.442779, 47.359054))
s0.Line(point1=(72.442779, 47.359054), point2=(72.314494, 47.944871))
s0.Line(point1=(72.314494, 47.944871), point2=(73.666436, 49.125259))
s0.Line(point1=(73.666436, 49.125259), point2=(73.677396, 50.013324))
s0.Line(point1=(73.677396, 50.013324), point2=(72.278845, 51.749073))
s0.Line(point1=(72.278845, 51.749073), point2=(71.551450, 52.135749))
s0.Line(point1=(71.551450, 52.135749), point2=(71.500000, 52.500000))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(71.700000, 20.550000), point2=(72.750000, 20.700000))
s0.Line(point1=(72.750000, 20.700000), point2=(73.950000, 19.350000))
s0.Line(point1=(73.950000, 19.350000), point2=(75.000000, 18.750000))
s0.Line(point1=(75.000000, 18.750000), point2=(75.000000, 16.350000))
s0.Line(point1=(75.000000, 16.350000), point2=(74.250000, 16.650000))
s0.Line(point1=(74.250000, 16.650000), point2=(71.550000, 19.500000))
s0.Line(point1=(71.550000, 19.500000), point2=(71.400000, 20.250000))
s0.Line(point1=(71.400000, 20.250000), point2=(71.700000, 20.550000))
s0.Line(point1=(71.615147, 20.719706), point2=(72.810599, 20.865431))
s0.Line(point1=(72.810599, 20.865431), point2=(74.074355, 19.503261))
s0.Line(point1=(74.074355, 19.503261), point2=(75.000000, 18.836824))
s0.Line(point1=(75.000000, 18.836824), point2=(75.000000, 16.257152))
s0.Line(point1=(75.000000, 16.257152), point2=(74.140266, 16.488378))
s0.Line(point1=(74.140266, 16.488378), point2=(71.379347, 19.411614))
s0.Line(point1=(71.379347, 19.411614), point2=(71.231231, 20.301099))
s0.Line(point1=(71.231231, 20.301099), point2=(71.615147, 20.719706))
s0.Line(point1=(71.784853, 20.380294), point2=(72.689401, 20.534569))
s0.Line(point1=(72.689401, 20.534569), point2=(73.825645, 19.196739))
s0.Line(point1=(73.825645, 19.196739), point2=(75.000000, 18.663176))
s0.Line(point1=(75.000000, 18.663176), point2=(75.000000, 16.442848))
s0.Line(point1=(75.000000, 16.442848), point2=(74.359734, 16.811622))
s0.Line(point1=(74.359734, 16.811622), point2=(71.720653, 19.588386))
s0.Line(point1=(71.720653, 19.588386), point2=(71.568769, 20.198901))
s0.Line(point1=(71.568769, 20.198901), point2=(71.784853, 20.380294))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(73.050000, 13.050000), point2=(73.800000, 13.050000))
s0.Line(point1=(73.800000, 13.050000), point2=(75.000000, 12.150000))
s0.Line(point1=(75.000000, 12.150000), point2=(75.000000, 8.550000))
s0.Line(point1=(75.000000, 8.550000), point2=(71.400000, 10.800000))
s0.Line(point1=(71.400000, 10.800000), point2=(71.700000, 11.400000))
s0.Line(point1=(71.700000, 11.400000), point2=(72.300000, 11.550000))
s0.Line(point1=(72.300000, 11.550000), point2=(73.050000, 13.050000))
s0.Line(point1=(72.960557, 13.194721), point2=(73.860000, 13.230000))
s0.Line(point1=(73.860000, 13.230000), point2=(75.000000, 12.230000))
s0.Line(point1=(75.000000, 12.230000), point2=(75.000000, 8.465200))
s0.Line(point1=(75.000000, 8.465200), point2=(71.257557, 10.759922))
s0.Line(point1=(71.257557, 10.759922), point2=(71.586304, 11.541736))
s0.Line(point1=(71.586304, 11.541736), point2=(72.186304, 11.691736))
s0.Line(point1=(72.186304, 11.691736), point2=(72.960557, 13.194721))
s0.Line(point1=(73.139443, 12.905279), point2=(73.740000, 12.870000))
s0.Line(point1=(73.740000, 12.870000), point2=(75.000000, 12.070000))
s0.Line(point1=(75.000000, 12.070000), point2=(75.000000, 8.634800))
s0.Line(point1=(75.000000, 8.634800), point2=(71.542443, 10.840078))
s0.Line(point1=(71.542443, 10.840078), point2=(71.813696, 11.258264))
s0.Line(point1=(71.813696, 11.258264), point2=(72.413696, 11.408264))
s0.Line(point1=(72.413696, 11.408264), point2=(73.139443, 12.905279))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(71.700000, 40.950000), point2=(73.050000, 40.500000))
s0.Line(point1=(73.050000, 40.500000), point2=(74.250000, 40.650000))
s0.Line(point1=(74.250000, 40.650000), point2=(73.950000, 38.850000))
s0.Line(point1=(73.950000, 38.850000), point2=(73.350000, 38.250000))
s0.Line(point1=(73.350000, 38.250000), point2=(72.600000, 38.250000))
s0.Line(point1=(72.600000, 38.250000), point2=(72.600000, 39.150000))
s0.Line(point1=(72.600000, 39.150000), point2=(72.300000, 39.150000))
s0.Line(point1=(72.300000, 39.150000), point2=(71.700000, 40.050000))
s0.Line(point1=(71.700000, 40.050000), point2=(71.700000, 40.950000))
s0.Line(point1=(71.631623, 41.044868), point2=(73.069219, 40.694096))
s0.Line(point1=(73.069219, 40.694096), point2=(74.336236, 40.732788))
s0.Line(point1=(74.336236, 40.732788), point2=(74.119350, 38.762849))
s0.Line(point1=(74.119350, 38.762849), point2=(73.420711, 38.079289))
s0.Line(point1=(73.420711, 38.079289), point2=(72.500000, 38.150000))
s0.Line(point1=(72.500000, 38.150000), point2=(72.500000, 39.050000))
s0.Line(point1=(72.500000, 39.050000), point2=(72.216795, 38.994530))
s0.Line(point1=(72.216795, 38.994530), point2=(71.516795, 39.994530))
s0.Line(point1=(71.516795, 39.994530), point2=(71.631623, 41.044868))
s0.Line(point1=(71.768377, 40.855132), point2=(73.030781, 40.305904))
s0.Line(point1=(73.030781, 40.305904), point2=(74.163764, 40.567212))
s0.Line(point1=(74.163764, 40.567212), point2=(73.780650, 38.937151))
s0.Line(point1=(73.780650, 38.937151), point2=(73.279289, 38.420711))
s0.Line(point1=(73.279289, 38.420711), point2=(72.700000, 38.350000))
s0.Line(point1=(72.700000, 38.350000), point2=(72.700000, 39.250000))
s0.Line(point1=(72.700000, 39.250000), point2=(72.383205, 39.305470))
s0.Line(point1=(72.383205, 39.305470), point2=(71.883205, 40.105470))
s0.Line(point1=(71.883205, 40.105470), point2=(71.768377, 40.855132))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(75.000000, 26.550000), point2=(75.000000, 22.650000))
s0.Line(point1=(75.000000, 22.650000), point2=(73.500000, 21.750000))
s0.Line(point1=(73.500000, 21.750000), point2=(72.150000, 21.600000))
s0.Line(point1=(72.150000, 21.600000), point2=(72.000000, 23.400000))
s0.Line(point1=(72.000000, 23.400000), point2=(72.600000, 23.550000))
s0.Line(point1=(72.600000, 23.550000), point2=(73.200000, 25.500000))
s0.Line(point1=(73.200000, 25.500000), point2=(74.250000, 26.550000))
s0.Line(point1=(74.250000, 26.550000), point2=(75.000000, 26.550000))
s0.Line(point1=(75.000000, 26.650000), point2=(75.000000, 22.564251))
s0.Line(point1=(75.000000, 22.564251), point2=(73.562493, 21.564862))
s0.Line(point1=(73.562493, 21.564862), point2=(72.061389, 21.492307))
s0.Line(point1=(72.061389, 21.492307), point2=(71.876092, 23.488710))
s0.Line(point1=(71.876092, 23.488710), point2=(72.480169, 23.676423))
s0.Line(point1=(72.480169, 23.676423), point2=(73.033711, 25.600119))
s0.Line(point1=(73.033711, 25.600119), point2=(74.179289, 26.720711))
s0.Line(point1=(74.179289, 26.720711), point2=(75.000000, 26.650000))
s0.Line(point1=(75.000000, 26.450000), point2=(75.000000, 22.735749))
s0.Line(point1=(75.000000, 22.735749), point2=(73.437507, 21.935138))
s0.Line(point1=(73.437507, 21.935138), point2=(72.238611, 21.707693))
s0.Line(point1=(72.238611, 21.707693), point2=(72.123908, 23.311290))
s0.Line(point1=(72.123908, 23.311290), point2=(72.719831, 23.423577))
s0.Line(point1=(72.719831, 23.423577), point2=(73.366289, 25.399881))
s0.Line(point1=(73.366289, 25.399881), point2=(74.320711, 26.379289))
s0.Line(point1=(74.320711, 26.379289), point2=(75.000000, 26.450000))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
s0 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints
s0.Line(point1=(73.350000, 37.050000), point2=(75.000000, 36.300000))
s0.Line(point1=(75.000000, 36.300000), point2=(75.000000, 31.950000))
s0.Line(point1=(75.000000, 31.950000), point2=(74.250000, 31.950000))
s0.Line(point1=(74.250000, 31.950000), point2=(72.150000, 34.200000))
s0.Line(point1=(72.150000, 34.200000), point2=(72.450000, 36.150000))
s0.Line(point1=(72.450000, 36.150000), point2=(73.350000, 37.050000))
s0.Line(point1=(73.320670, 37.211747), point2=(75.000000, 36.391037))
s0.Line(point1=(75.000000, 36.391037), point2=(75.000000, 31.850000))
s0.Line(point1=(75.000000, 31.850000), point2=(74.176894, 31.781768))
s0.Line(point1=(74.176894, 31.781768), point2=(71.978057, 34.146974))
s0.Line(point1=(71.978057, 34.146974), point2=(72.280452, 36.235916))
s0.Line(point1=(72.280452, 36.235916), point2=(73.320670, 37.211747))
s0.Line(point1=(73.379330, 36.888253), point2=(75.000000, 36.208963))
s0.Line(point1=(75.000000, 36.208963), point2=(75.000000, 32.050000))
s0.Line(point1=(75.000000, 32.050000), point2=(74.323106, 32.118232))
s0.Line(point1=(74.323106, 32.118232), point2=(72.321943, 34.253026))
s0.Line(point1=(72.321943, 34.253026), point2=(72.619548, 36.064084))
s0.Line(point1=(72.619548, 36.064084), point2=(73.379330, 36.888253))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces =f
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)
print 'ok'
p = mdb.models['Model-1'].parts['Part-1']
e=p.edges
e0=e[0:0]
e = p.edges.findAt(
((7.200000, 51.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((7.725000, 49.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((7.575000, 47.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((7.125000, 46.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((6.450000, 45.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((5.100000, 43.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((2.850000, 42.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((1.275000, 43.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((0.375000, 43.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((0.000000, 47.925000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((3.225000, 52.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((0.450000, 35.925000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((0.900000, 35.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((1.275000, 34.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((1.725000, 33.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((2.100000, 33.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((2.100000, 32.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((1.125000, 31.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((0.225000, 30.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((0.000000, 33.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((0.525000, 28.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((1.125000, 28.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((1.725000, 27.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((2.400000, 27.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((2.550000, 27.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((2.175000, 26.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((1.650000, 25.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((1.200000, 25.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((0.450000, 26.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((0.000000, 27.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((0.675000, 11.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((1.575000, 12.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((2.850000, 12.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((4.275000, 13.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((5.550000, 12.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((7.200000, 10.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((9.000000, 7.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((10.050000, 5.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((9.900000, 3.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((9.000000, 3.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((6.900000, 3.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((5.100000, 2.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((3.975000, 1.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((2.775000, 2.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((1.350000, 4.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((0.225000, 6.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((0.000000, 8.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((0.600000, 1.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((1.875000, 0.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((1.275000, 0.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((0.000000, 0.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((0.975000, 39.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((1.875000, 38.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((3.000000, 37.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((3.750000, 37.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((3.825000, 36.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((2.400000, 36.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((0.675000, 36.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((0.450000, 38.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((1.125000, 17.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((2.100000, 17.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((2.925000, 15.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((3.450000, 15.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((3.900000, 14.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((2.775000, 13.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((1.275000, 15.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((0.900000, 16.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((1.800000, 41.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((1.350000, 40.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((1.050000, 41.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((1.500000, 42.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((1.725000, 22.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((2.550000, 22.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((2.925000, 21.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((2.775000, 19.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((2.325000, 19.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((2.100000, 19.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((1.725000, 19.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((1.275000, 20.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((3.225000, 24.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((4.800000, 24.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((5.400000, 23.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((4.950000, 22.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((4.050000, 21.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((3.150000, 22.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((2.475000, 23.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((2.250000, 24.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((3.600000, 41.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((4.800000, 41.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((5.550000, 39.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((5.400000, 39.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((4.425000, 39.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((3.150000, 39.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((2.925000, 41.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((4.500000, 30.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((4.425000, 30.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((4.050000, 30.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((3.525000, 29.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((3.075000, 29.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((3.225000, 30.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((3.675000, 31.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((4.125000, 31.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((3.975000, 20.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((5.250000, 19.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((6.000000, 18.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((5.025000, 17.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((3.975000, 17.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((3.675000, 19.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((8.775000, 2.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((8.400000, 1.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((7.650000, 0.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((5.625000, 0.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((4.275000, 0.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((4.950000, 0.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((6.600000, 1.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((8.100000, 2.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((8.475000, 2.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((5.850000, 33.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((8.850000, 31.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((10.950000, 30.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((11.400000, 28.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((11.100000, 27.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((10.125000, 26.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((8.550000, 24.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((7.125000, 24.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((6.000000, 25.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((5.475000, 27.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((5.100000, 29.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((4.575000, 32.925000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((5.625000, 42.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((6.675000, 41.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((6.450000, 40.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((5.400000, 41.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((4.950000, 42.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((7.200000, 37.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((6.900000, 36.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((6.000000, 36.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((5.475000, 36.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((6.375000, 37.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((6.225000, 22.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((8.250000, 22.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((9.900000, 22.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((10.350000, 21.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((10.800000, 20.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((9.750000, 20.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((8.025000, 20.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((6.600000, 20.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((5.850000, 21.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((7.275000, 35.925000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((8.700000, 35.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((9.600000, 35.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((9.825000, 33.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((9.150000, 32.925000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((7.650000, 33.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((6.600000, 35.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((6.975000, 16.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((8.325000, 15.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((9.300000, 13.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((9.000000, 12.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((8.700000, 12.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((8.400000, 12.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((7.800000, 12.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((7.275000, 14.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((6.825000, 15.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((6.600000, 16.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((7.800000, 19.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((8.025000, 18.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((8.025000, 17.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((8.250000, 17.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((8.400000, 16.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((8.025000, 16.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((7.350000, 17.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((7.050000, 18.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((7.275000, 19.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((12.000000, 45.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((11.475000, 45.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((10.800000, 44.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((9.750000, 43.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((8.625000, 41.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((8.250000, 39.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((7.875000, 39.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((7.650000, 40.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((7.500000, 42.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((7.350000, 42.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((7.500000, 43.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((7.575000, 44.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((8.475000, 45.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((9.825000, 45.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((11.100000, 46.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((8.550000, 49.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((9.600000, 50.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((10.575000, 49.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((10.725000, 48.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((9.750000, 48.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((8.550000, 48.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((8.775000, 38.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((9.525000, 38.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((10.275000, 37.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((10.800000, 36.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((10.500000, 36.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((9.225000, 36.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((9.150000, 19.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((10.425000, 19.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((11.325000, 19.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((11.250000, 18.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((10.500000, 17.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((9.525000, 17.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((8.775000, 18.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((10.800000, 44.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((11.475000, 43.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((12.150000, 42.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((12.750000, 42.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((13.125000, 40.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((12.450000, 40.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((10.875000, 41.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((9.975000, 42.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((10.200000, 43.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((10.575000, 25.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((11.400000, 25.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((12.675000, 25.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((14.475000, 24.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.675000, 22.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.825000, 21.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.525000, 21.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((14.400000, 21.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((12.900000, 21.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((12.300000, 22.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((11.400000, 22.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((10.350000, 24.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((10.650000, 16.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((11.250000, 15.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((11.775000, 15.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((11.850000, 12.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((11.250000, 10.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((10.500000, 10.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((10.200000, 11.925000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((10.425000, 12.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((10.425000, 14.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((10.275000, 15.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((10.500000, 9.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((11.100000, 9.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((11.775000, 9.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((12.150000, 8.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((11.550000, 7.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((10.650000, 7.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((10.275000, 8.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((10.875000, 51.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((11.475000, 51.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((11.625000, 50.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((11.025000, 50.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((10.500000, 51.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((13.350000, 49.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((13.125000, 49.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((12.750000, 48.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((11.925000, 48.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((11.850000, 49.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((12.900000, 49.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((12.150000, 38.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((12.975000, 37.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((13.200000, 37.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((12.450000, 36.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((11.475000, 36.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((11.400000, 37.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.300000, 0.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((13.275000, 0.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((11.325000, 0.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((12.225000, 1.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((13.650000, 2.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((14.775000, 1.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((12.750000, 34.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((14.400000, 35.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.450000, 34.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((16.950000, 34.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((18.150000, 33.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((18.600000, 32.925000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((18.975000, 32.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((19.350000, 31.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((18.975000, 30.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((17.550000, 29.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((16.350000, 28.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.600000, 28.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((14.400000, 28.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((13.800000, 30.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((13.425000, 31.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((12.375000, 32.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((11.550000, 33.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.150000, 5.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((14.775000, 4.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((14.325000, 3.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((13.800000, 2.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((12.450000, 3.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((11.550000, 3.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((11.850000, 4.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((12.975000, 5.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((13.875000, 5.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((14.550000, 6.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((17.700000, 20.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((16.950000, 19.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.300000, 17.925000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((13.650000, 16.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((12.900000, 16.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((12.375000, 17.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((11.925000, 17.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((12.900000, 18.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((14.175000, 18.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((14.550000, 19.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.000000, 19.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.900000, 20.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((17.025000, 20.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((12.525000, 30.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((12.975000, 29.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((13.725000, 28.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((14.250000, 26.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((14.100000, 25.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((13.725000, 25.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((13.050000, 26.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((12.300000, 26.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((12.150000, 28.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((14.850000, 39.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((13.500000, 39.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((12.675000, 39.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((13.575000, 40.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((14.250000, 40.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((14.700000, 40.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((13.950000, 13.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.975000, 12.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((16.800000, 11.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.975000, 9.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((14.325000, 7.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((13.200000, 6.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((13.050000, 10.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((13.050000, 13.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((12.825000, 13.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((13.950000, 47.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((14.400000, 45.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((14.775000, 43.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.000000, 42.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((14.625000, 42.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((14.025000, 41.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((13.800000, 41.925000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((13.350000, 42.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((12.900000, 43.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((13.050000, 44.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((13.050000, 44.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((13.050000, 45.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((13.425000, 46.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((13.650000, 47.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((16.950000, 50.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((16.500000, 50.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.225000, 49.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((14.625000, 51.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.450000, 51.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((16.500000, 51.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((16.800000, 26.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((16.275000, 25.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.150000, 25.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((14.625000, 26.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((14.850000, 27.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.675000, 27.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((16.575000, 27.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.225000, 17.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.900000, 17.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((16.350000, 16.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((16.275000, 16.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.450000, 16.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((14.850000, 16.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.750000, 39.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((17.025000, 39.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((18.000000, 37.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((18.300000, 36.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((18.000000, 35.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((17.325000, 34.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((16.500000, 35.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.900000, 36.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.375000, 37.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.075000, 38.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((16.425000, 14.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((16.350000, 14.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.900000, 13.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.375000, 13.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.300000, 14.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.900000, 14.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((18.075000, 49.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((18.900000, 48.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((19.575000, 47.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((18.975000, 46.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((17.625000, 46.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((16.650000, 45.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.825000, 44.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.300000, 45.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.600000, 46.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.975000, 47.925000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((16.575000, 49.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((17.475000, 50.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((17.100000, 6.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((17.700000, 6.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((18.075000, 5.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((18.375000, 3.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((17.550000, 2.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((16.650000, 3.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((16.500000, 4.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((16.125000, 4.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((15.900000, 5.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((16.275000, 6.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((18.375000, 42.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((17.325000, 41.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((16.125000, 42.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((16.575000, 43.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((17.700000, 43.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((17.775000, 25.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((19.800000, 25.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((21.000000, 24.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((20.700000, 23.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((19.725000, 22.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((18.075000, 23.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((16.875000, 24.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((24.975000, 19.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((25.800000, 17.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((25.500000, 15.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((24.450000, 12.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((22.800000, 9.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((22.050000, 8.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((20.925000, 7.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((19.350000, 7.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((18.525000, 8.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((17.850000, 11.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((17.400000, 14.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((18.450000, 16.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((19.725000, 17.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((21.075000, 18.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((22.425000, 19.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((23.250000, 20.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((23.175000, 42.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((20.325000, 40.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((17.400000, 40.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((18.075000, 41.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((18.750000, 41.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((19.425000, 41.925000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((21.150000, 42.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((22.650000, 42.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((19.275000, 19.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((19.650000, 18.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((19.275000, 18.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((18.825000, 17.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((18.150000, 17.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((17.550000, 17.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((17.775000, 18.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((18.000000, 19.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((18.450000, 19.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((19.125000, 52.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((20.700000, 51.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((21.600000, 50.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((22.725000, 49.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((23.175000, 48.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((22.575000, 48.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((21.675000, 48.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((21.075000, 47.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((20.850000, 48.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((19.350000, 50.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((19.425000, 27.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((18.750000, 26.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((18.000000, 27.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((18.225000, 27.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((19.050000, 28.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((21.750000, 22.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((21.300000, 21.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((20.100000, 21.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((18.675000, 21.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((18.000000, 21.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((19.275000, 22.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((20.850000, 22.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((21.450000, 22.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((19.500000, 38.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((20.100000, 38.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((20.400000, 37.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((20.250000, 36.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((19.650000, 36.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((19.050000, 36.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((18.750000, 37.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((18.900000, 38.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((19.350000, 5.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((19.875000, 5.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((20.550000, 4.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((21.000000, 3.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((20.625000, 2.925000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((20.025000, 3.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((19.425000, 4.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((20.325000, 46.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((21.450000, 46.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((22.350000, 45.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((22.575000, 44.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((21.225000, 44.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((19.800000, 45.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((19.725000, 45.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((20.025000, 1.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((20.625000, 2.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((21.450000, 2.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((21.825000, 2.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((22.200000, 0.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((21.300000, 0.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((19.875000, 0.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((21.075000, 36.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((22.125000, 36.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((22.275000, 35.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((22.500000, 34.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((21.225000, 34.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((19.950000, 35.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((20.400000, 20.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((21.225000, 20.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((21.675000, 19.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((21.000000, 19.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((20.100000, 20.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((21.150000, 34.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((21.900000, 33.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((22.575000, 31.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((23.250000, 30.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((23.400000, 28.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((22.950000, 28.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((22.350000, 27.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((21.450000, 29.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((20.625000, 32.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((20.400000, 33.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((20.550000, 34.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((24.000000, 26.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((24.000000, 25.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((22.650000, 25.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((21.150000, 26.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((21.825000, 26.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((23.325000, 26.925000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((21.900000, 40.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((22.500000, 39.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((22.800000, 38.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((22.425000, 37.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((21.825000, 37.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((21.600000, 39.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((23.775000, 8.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((22.800000, 7.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((22.275000, 7.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((23.250000, 8.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((23.925000, 6.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((25.500000, 6.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((26.025000, 6.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((26.925000, 5.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((27.300000, 4.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((24.675000, 4.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((21.975000, 5.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((22.125000, 6.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((22.350000, 6.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((23.325000, 24.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((23.925000, 23.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((23.775000, 22.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((23.175000, 22.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((22.800000, 24.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((26.100000, 48.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((26.025000, 47.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((25.800000, 46.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((25.500000, 45.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((25.125000, 43.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((24.225000, 43.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((23.850000, 45.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((23.550000, 46.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((23.100000, 47.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((24.375000, 48.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((25.950000, 48.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((23.700000, 37.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((24.300000, 37.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((24.900000, 36.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((25.200000, 36.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((24.225000, 35.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((23.325000, 36.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((24.075000, 50.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((24.600000, 50.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((24.900000, 49.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((24.225000, 49.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((23.475000, 49.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((23.625000, 50.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((23.925000, 34.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((25.725000, 34.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((27.600000, 33.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((27.900000, 31.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((27.075000, 30.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((25.425000, 30.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((24.000000, 31.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((23.700000, 32.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((23.700000, 33.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((26.100000, 42.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((26.625000, 41.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((26.625000, 39.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((25.650000, 37.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((24.375000, 38.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((23.925000, 39.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((24.300000, 41.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((24.600000, 41.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((25.200000, 42.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((25.200000, 11.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((25.050000, 10.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((24.450000, 9.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((24.000000, 10.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((24.225000, 11.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((24.825000, 11.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((26.700000, 23.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((27.525000, 21.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((27.225000, 20.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((26.025000, 19.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((24.525000, 20.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((24.075000, 21.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((24.750000, 22.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((25.575000, 23.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((25.200000, 3.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((25.800000, 3.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((25.875000, 2.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((25.425000, 1.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((24.825000, 2.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((24.675000, 3.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((35.100000, 27.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((34.800000, 24.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.900000, 24.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((30.825000, 24.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((27.300000, 25.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((25.725000, 25.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((25.050000, 26.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((24.825000, 27.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((25.200000, 28.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((27.000000, 29.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((28.650000, 30.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((28.650000, 31.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((28.800000, 32.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((30.900000, 31.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.075000, 30.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.825000, 31.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((34.725000, 30.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((27.300000, 15.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((26.625000, 13.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((25.950000, 13.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((25.725000, 14.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((25.350000, 14.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((26.025000, 15.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((26.700000, 17.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((26.925000, 18.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((31.350000, 10.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((30.975000, 10.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((30.225000, 9.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.025000, 8.925000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((28.050000, 8.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((27.450000, 7.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((26.175000, 8.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((25.575000, 9.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((25.725000, 11.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((26.025000, 12.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((27.150000, 12.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((28.200000, 13.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.925000, 12.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((28.275000, 47.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.025000, 46.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((28.725000, 45.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((27.450000, 44.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((26.550000, 44.925000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((26.325000, 45.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((26.925000, 47.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((27.675000, 48.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((28.650000, 52.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((31.425000, 51.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((32.175000, 49.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((31.950000, 48.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((31.200000, 47.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.025000, 48.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((26.850000, 49.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((26.475000, 51.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((28.200000, 0.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((27.225000, 0.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((26.400000, 0.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((26.700000, 1.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((27.675000, 1.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((27.825000, 38.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((28.500000, 38.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((28.500000, 36.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((28.050000, 36.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((27.450000, 36.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((27.225000, 37.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((28.425000, 35.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.025000, 35.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.175000, 34.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((28.800000, 33.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((28.425000, 33.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((28.125000, 34.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((27.975000, 34.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((28.275000, 17.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.475000, 17.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((30.375000, 16.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((30.225000, 16.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.325000, 16.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((28.350000, 16.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((27.975000, 16.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.175000, 22.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((30.375000, 23.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((30.825000, 22.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((30.750000, 21.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.925000, 20.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((28.950000, 21.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((28.500000, 21.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((28.875000, 15.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.400000, 15.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.925000, 15.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((30.900000, 15.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((31.350000, 15.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((31.125000, 14.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((31.050000, 13.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((30.900000, 12.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.775000, 13.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((28.725000, 14.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((28.425000, 15.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((30.750000, 40.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((30.300000, 39.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.175000, 39.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((28.500000, 39.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((28.950000, 40.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.400000, 40.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((30.075000, 40.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((31.725000, 1.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((31.350000, 1.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((31.050000, 1.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((30.525000, 0.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.925000, 0.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.475000, 0.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.025000, 0.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((28.725000, 1.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((28.800000, 2.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.400000, 2.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.925000, 2.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((30.525000, 2.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((31.350000, 1.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.300000, 43.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((31.050000, 42.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.025000, 42.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.475000, 44.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((30.525000, 44.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((32.325000, 44.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((32.700000, 38.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((34.050000, 36.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((35.025000, 35.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((34.875000, 34.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.675000, 34.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((32.625000, 33.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((31.725000, 32.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((30.525000, 32.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.625000, 35.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((30.225000, 38.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((31.425000, 39.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((31.875000, 39.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.625000, 19.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((30.150000, 18.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.925000, 17.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.550000, 17.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.250000, 18.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.625000, 5.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((30.900000, 5.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((32.175000, 4.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((32.025000, 3.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((30.975000, 3.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.925000, 3.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((29.475000, 4.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((30.975000, 46.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((32.325000, 46.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((32.850000, 45.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((32.250000, 44.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((31.275000, 45.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((30.525000, 46.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((31.950000, 18.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((31.650000, 18.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((30.975000, 18.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((30.825000, 19.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((31.500000, 19.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.450000, 4.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.225000, 3.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((35.850000, 3.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((35.475000, 2.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((35.250000, 0.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.300000, 0.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((31.500000, 0.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((32.700000, 1.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((34.275000, 3.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((35.025000, 3.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((35.625000, 4.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.225000, 5.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((32.175000, 22.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.300000, 21.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((34.200000, 19.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.750000, 18.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((32.775000, 19.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((32.100000, 20.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((31.800000, 21.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.525000, 16.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((32.775000, 15.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((32.175000, 15.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((31.950000, 16.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((32.175000, 16.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.150000, 16.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((35.025000, 8.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((34.800000, 7.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((34.425000, 6.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((34.125000, 4.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.675000, 4.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.450000, 5.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.225000, 6.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((32.925000, 6.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((32.400000, 7.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((31.950000, 7.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.450000, 8.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((32.550000, 51.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.150000, 51.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.675000, 51.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((34.350000, 50.925000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((35.400000, 49.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((35.625000, 48.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((34.575000, 49.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.675000, 49.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.225000, 50.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((32.925000, 50.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((32.475000, 50.925000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((32.175000, 51.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.900000, 14.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((34.425000, 13.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((34.125000, 12.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.600000, 12.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((32.850000, 12.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((32.850000, 13.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((35.550000, 15.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.075000, 14.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.225000, 13.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.750000, 11.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((37.200000, 9.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.375000, 9.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((35.325000, 9.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((34.500000, 9.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.900000, 10.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.225000, 10.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((32.550000, 10.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.300000, 11.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.975000, 11.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((34.125000, 12.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((34.425000, 12.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((34.800000, 13.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((35.100000, 14.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.525000, 47.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.975000, 47.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((34.200000, 46.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.975000, 45.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.450000, 46.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.225000, 47.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((34.125000, 41.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((35.700000, 40.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.900000, 40.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((37.050000, 40.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((37.350000, 40.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((37.725000, 40.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((38.025000, 40.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((38.025000, 39.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((37.500000, 37.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.150000, 38.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((34.200000, 39.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.450000, 40.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.975000, 43.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((34.800000, 43.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((34.725000, 42.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((33.900000, 43.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((35.550000, 38.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.300000, 37.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.450000, 36.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.075000, 36.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((35.400000, 35.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((34.650000, 36.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((34.275000, 37.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((34.650000, 38.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((37.650000, 23.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((37.875000, 22.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((37.425000, 20.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.825000, 20.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.000000, 19.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((34.950000, 20.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((34.500000, 21.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((34.875000, 22.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((35.775000, 23.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.825000, 23.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((35.550000, 33.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.450000, 33.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((35.775000, 32.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((34.875000, 33.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.150000, 46.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((37.800000, 46.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.000000, 45.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.600000, 45.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.675000, 44.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.300000, 43.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((38.700000, 44.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((37.650000, 45.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.075000, 45.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((35.250000, 46.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((38.625000, 43.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((38.175000, 42.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((37.500000, 42.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.225000, 42.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((35.250000, 42.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((35.925000, 43.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((37.200000, 44.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((38.250000, 44.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.450000, 17.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((37.875000, 18.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((38.325000, 18.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.000000, 18.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((40.725000, 17.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.075000, 15.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.100000, 14.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((37.800000, 15.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((35.400000, 16.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((35.250000, 16.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((37.650000, 25.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.750000, 24.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((35.850000, 24.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.150000, 25.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((37.050000, 26.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.300000, 51.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.900000, 51.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.750000, 50.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.150000, 50.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.900000, 31.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((37.425000, 31.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((37.350000, 30.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.750000, 30.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.375000, 31.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((40.800000, 29.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.600000, 27.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((37.350000, 27.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((36.300000, 27.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((37.500000, 28.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.750000, 29.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((38.775000, 8.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.900000, 8.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((40.350000, 6.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((40.125000, 5.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.300000, 4.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((38.025000, 4.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((37.125000, 5.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((37.500000, 7.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((37.650000, 1.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.225000, 2.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((40.800000, 3.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.625000, 5.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.525000, 6.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.175000, 5.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.675000, 4.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((47.625000, 2.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((49.200000, 0.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.275000, 0.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((37.125000, 0.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((38.250000, 49.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.375000, 48.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((40.050000, 47.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.525000, 46.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((38.475000, 46.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((37.650000, 47.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((37.575000, 49.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.675000, 36.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.400000, 34.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.600000, 33.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((38.100000, 34.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((37.350000, 35.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((38.775000, 36.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.550000, 36.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((37.800000, 13.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((38.550000, 13.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.075000, 13.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.900000, 13.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((40.575000, 11.925000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((40.125000, 11.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.000000, 10.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((37.875000, 11.925000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((38.400000, 42.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.225000, 42.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.975000, 41.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.975000, 40.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.225000, 40.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((38.400000, 41.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.400000, 32.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.025000, 32.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((40.650000, 31.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((40.125000, 30.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((38.925000, 31.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((38.325000, 32.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.900000, 33.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.225000, 22.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((40.050000, 22.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((40.950000, 20.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.700000, 19.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.400000, 18.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((40.950000, 19.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((40.500000, 19.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.750000, 19.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.225000, 20.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((38.850000, 21.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((38.550000, 22.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.150000, 26.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.775000, 25.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.100000, 25.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((40.425000, 24.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.600000, 24.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.000000, 24.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.825000, 26.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.100000, 27.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.775000, 27.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((40.275000, 52.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.550000, 51.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.000000, 50.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.700000, 50.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.325000, 49.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.025000, 49.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((40.425000, 49.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.750000, 50.925000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.450000, 51.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((40.125000, 39.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.175000, 39.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.625000, 39.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.475000, 38.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((40.800000, 38.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.900000, 38.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((39.450000, 39.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((40.350000, 43.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.100000, 43.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.925000, 42.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.300000, 42.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.000000, 41.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.250000, 42.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((40.425000, 42.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((40.050000, 42.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.550000, 41.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.025000, 40.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((40.425000, 40.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((40.575000, 41.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.175000, 41.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.275000, 47.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.775000, 46.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.450000, 45.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.775000, 43.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.575000, 42.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.450000, 43.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.475000, 44.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.400000, 45.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.075000, 46.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.450000, 47.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.925000, 22.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.825000, 21.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.425000, 20.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.575000, 19.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.200000, 19.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.750000, 19.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.075000, 20.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.475000, 21.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.375000, 22.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.925000, 21.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.400000, 21.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.725000, 22.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.125000, 22.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.225000, 23.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.550000, 23.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.150000, 24.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.175000, 24.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.050000, 11.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.525000, 11.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((47.475000, 11.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.175000, 10.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.900000, 9.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.775000, 6.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.975000, 4.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((47.700000, 4.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((46.650000, 5.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.075000, 6.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.425000, 7.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.300000, 9.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((41.625000, 10.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.975000, 50.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.500000, 50.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.500000, 49.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.725000, 48.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.100000, 47.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.800000, 47.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.600000, 48.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.150000, 49.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.225000, 13.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.050000, 13.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.800000, 13.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.875000, 13.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.100000, 12.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.400000, 12.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.200000, 12.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.000000, 13.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.400000, 33.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.950000, 32.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.975000, 31.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.300000, 31.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.450000, 32.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.275000, 33.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.100000, 33.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.600000, 18.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.350000, 17.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.650000, 16.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.200000, 16.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.600000, 16.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.300000, 17.925000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.000000, 41.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.700000, 41.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.325000, 40.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.650000, 40.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.825000, 40.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.675000, 41.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.875000, 41.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.350000, 39.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.175000, 38.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.550000, 38.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.075000, 37.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.450000, 36.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.150000, 36.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.025000, 37.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.975000, 38.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.400000, 30.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.850000, 29.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.400000, 28.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.575000, 27.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.050000, 28.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((42.900000, 28.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.425000, 29.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.325000, 27.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.700000, 27.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.225000, 26.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.675000, 25.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.075000, 25.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.250000, 25.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((43.950000, 26.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.850000, 35.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.525000, 35.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.450000, 34.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.000000, 34.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.475000, 34.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.250000, 35.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.750000, 51.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((49.050000, 49.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.900000, 49.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.075000, 48.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((46.725000, 48.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.150000, 48.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.550000, 49.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.850000, 51.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((46.650000, 52.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.450000, 32.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((47.100000, 32.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.375000, 30.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((49.050000, 29.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.750000, 28.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((47.925000, 29.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((46.575000, 30.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.150000, 30.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.400000, 30.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.325000, 31.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.675000, 18.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((46.725000, 16.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((46.200000, 15.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.525000, 14.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.000000, 14.925000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.550000, 16.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((44.325000, 19.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((49.500000, 44.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((49.200000, 43.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.600000, 42.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((47.775000, 41.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((47.100000, 40.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((46.575000, 39.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((46.200000, 39.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.600000, 38.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.075000, 39.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.600000, 40.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((46.650000, 42.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((47.550000, 43.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.375000, 44.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((49.200000, 45.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((46.500000, 33.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.825000, 33.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.225000, 33.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.450000, 34.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((46.200000, 34.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.825000, 29.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((47.025000, 28.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((47.250000, 28.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((46.050000, 28.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((47.775000, 14.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((47.625000, 13.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((46.650000, 12.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.750000, 12.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.750000, 13.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((46.425000, 14.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((47.325000, 14.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.300000, 47.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.150000, 46.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((47.850000, 45.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((47.025000, 45.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((46.050000, 45.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((45.900000, 46.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((46.125000, 46.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((46.875000, 47.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((47.475000, 47.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((47.850000, 48.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.700000, 27.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.250000, 25.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((49.650000, 24.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.675000, 23.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((47.025000, 22.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((46.350000, 23.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((47.775000, 25.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((49.050000, 27.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((49.500000, 28.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.100000, 29.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.625000, 29.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((46.725000, 20.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((47.475000, 21.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.000000, 21.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.225000, 20.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.300000, 20.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.675000, 19.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.900000, 19.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.450000, 18.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.000000, 18.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((47.550000, 19.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((46.725000, 19.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((46.275000, 20.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((49.050000, 39.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((49.275000, 38.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((49.125000, 36.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.750000, 36.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.375000, 37.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.075000, 36.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((47.550000, 36.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((47.025000, 37.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((47.250000, 38.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((47.700000, 39.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.375000, 39.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.900000, 34.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.175000, 33.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.625000, 32.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.400000, 31.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.175000, 31.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((49.350000, 31.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.375000, 31.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.000000, 33.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.150000, 33.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.825000, 17.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((49.800000, 16.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.025000, 16.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((49.950000, 15.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((49.950000, 15.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.100000, 15.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.625000, 14.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.375000, 13.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.825000, 13.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.650000, 12.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.100000, 10.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.500000, 10.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.825000, 10.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.450000, 10.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.075000, 11.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.100000, 13.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((49.050000, 14.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.375000, 15.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.000000, 16.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.450000, 21.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.150000, 20.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.850000, 20.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.100000, 19.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((49.275000, 20.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((48.975000, 21.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((49.275000, 22.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.625000, 22.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.625000, 47.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((49.800000, 46.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((49.200000, 46.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((49.575000, 47.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.175000, 47.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.625000, 47.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.925000, 46.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((49.950000, 45.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.250000, 46.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.225000, 46.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.100000, 42.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.625000, 41.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.775000, 40.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.475000, 39.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.025000, 39.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((49.800000, 41.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.550000, 37.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.075000, 38.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.450000, 38.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.725000, 37.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.775000, 36.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.100000, 35.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.300000, 36.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.175000, 36.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.950000, 18.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.650000, 17.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.450000, 17.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.325000, 17.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.400000, 18.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.300000, 19.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.425000, 18.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.825000, 4.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.500000, 3.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.025000, 2.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.400000, 0.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.850000, 0.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.350000, 0.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.700000, 0.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.075000, 0.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.525000, 2.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.125000, 52.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.700000, 51.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.000000, 51.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.475000, 50.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.725000, 50.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.750000, 50.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((50.925000, 51.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.125000, 44.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.850000, 43.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.450000, 42.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.950000, 42.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.225000, 43.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.000000, 44.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.125000, 49.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.100000, 48.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.175000, 48.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.875000, 48.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.050000, 48.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.375000, 49.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.250000, 41.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.050000, 40.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.900000, 41.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.800000, 42.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.400000, 41.925000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.025000, 34.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.950000, 31.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.025000, 30.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.650000, 29.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.825000, 30.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.300000, 31.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.750000, 33.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.725000, 34.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.125000, 27.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.800000, 25.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.500000, 25.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.825000, 25.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.450000, 26.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.500000, 46.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.975000, 46.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.750000, 47.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.275000, 47.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.100000, 10.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.475000, 10.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.850000, 8.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.625000, 6.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.175000, 6.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((55.350000, 5.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.000000, 5.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.950000, 5.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.575000, 5.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.125000, 5.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((51.750000, 6.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.200000, 6.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.950000, 7.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.550000, 7.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.075000, 9.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.600000, 10.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((55.500000, 11.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.425000, 15.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.025000, 16.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.700000, 17.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.525000, 16.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((55.500000, 16.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((57.675000, 15.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((59.400000, 14.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((59.025000, 13.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((58.200000, 12.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((57.225000, 12.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((55.950000, 12.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.375000, 12.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.250000, 12.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((52.575000, 14.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.450000, 26.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.900000, 25.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.750000, 24.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.225000, 24.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.475000, 24.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.175000, 25.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.625000, 26.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.625000, 21.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.450000, 21.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.525000, 21.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.150000, 20.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.550000, 20.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.100000, 21.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((55.950000, 3.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((55.425000, 2.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.375000, 2.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.625000, 2.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.475000, 3.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.750000, 3.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.400000, 50.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.550000, 48.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.975000, 46.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.925000, 48.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.525000, 50.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((55.425000, 50.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.475000, 42.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.325000, 41.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.825000, 40.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.550000, 39.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((53.850000, 40.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.150000, 41.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.375000, 41.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((55.200000, 42.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.100000, 42.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.625000, 34.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.925000, 32.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.400000, 30.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((55.050000, 29.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.150000, 29.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.000000, 30.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.150000, 32.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.675000, 33.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((55.725000, 34.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((58.275000, 18.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((57.300000, 18.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((55.800000, 17.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.825000, 18.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.525000, 18.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((55.575000, 19.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((57.450000, 19.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.825000, 38.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((55.275000, 37.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((55.800000, 37.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.175000, 36.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.550000, 35.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.775000, 34.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((55.875000, 35.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.825000, 36.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((54.600000, 37.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((55.275000, 21.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((55.950000, 21.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.550000, 21.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.100000, 20.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((55.275000, 20.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((55.050000, 21.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((55.875000, 39.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((57.000000, 39.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((57.600000, 38.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((57.825000, 38.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((58.125000, 38.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((58.500000, 37.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((58.500000, 36.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((58.125000, 35.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((57.375000, 36.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.325000, 37.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((55.500000, 39.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((55.500000, 28.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((55.800000, 28.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((58.725000, 28.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((61.650000, 27.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((59.625000, 26.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.775000, 26.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((55.575000, 26.925000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((55.200000, 27.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((55.875000, 44.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((58.200000, 44.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((60.075000, 44.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((60.525000, 43.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((61.050000, 43.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((60.225000, 42.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((58.650000, 42.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.700000, 43.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((55.500000, 44.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((57.075000, 52.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((58.725000, 52.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((58.950000, 51.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((58.650000, 50.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((57.975000, 50.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.625000, 51.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.700000, 2.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((57.150000, 2.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((57.450000, 1.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((57.600000, 1.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((57.975000, 1.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((58.350000, 0.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((57.300000, 0.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.100000, 0.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.175000, 1.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.400000, 2.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((61.800000, 23.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((61.200000, 22.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((59.700000, 21.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((58.350000, 21.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((57.675000, 21.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.775000, 21.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.175000, 23.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((57.300000, 24.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((59.475000, 25.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((61.200000, 24.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((61.350000, 49.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((60.975000, 48.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((60.600000, 48.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((60.000000, 48.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((59.175000, 48.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((58.725000, 47.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((57.975000, 46.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.925000, 46.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((56.475000, 46.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((57.450000, 48.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((58.800000, 49.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((59.850000, 49.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((60.900000, 49.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((60.600000, 3.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((59.475000, 3.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((57.900000, 3.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((57.150000, 3.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((57.000000, 3.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((57.750000, 4.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((59.175000, 5.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((60.300000, 4.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((58.350000, 11.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((59.550000, 12.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((60.600000, 12.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((62.100000, 12.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((64.425000, 10.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((66.450000, 7.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((66.750000, 5.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((65.850000, 4.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((63.075000, 4.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((59.775000, 7.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((58.125000, 9.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((57.600000, 10.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((58.200000, 33.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((59.025000, 33.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((59.400000, 30.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((59.100000, 29.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((58.425000, 29.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((57.900000, 32.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((58.350000, 40.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((58.650000, 41.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((59.250000, 41.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((60.525000, 40.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((61.500000, 39.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((61.275000, 38.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((59.550000, 38.925000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((58.200000, 39.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((58.050000, 40.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((59.400000, 21.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((59.925000, 20.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((59.250000, 19.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((58.425000, 20.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((58.500000, 21.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((64.725000, 18.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((64.275000, 18.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((63.825000, 17.925000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((63.525000, 17.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((63.075000, 17.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((62.175000, 16.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((60.075000, 16.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((58.650000, 16.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((60.225000, 18.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((63.000000, 19.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((64.200000, 19.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((64.500000, 19.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((60.375000, 47.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((60.750000, 46.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((60.525000, 45.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((59.850000, 45.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((59.175000, 46.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((59.475000, 47.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((62.400000, 34.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((60.600000, 34.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((59.175000, 34.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((60.150000, 35.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((61.500000, 35.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((62.325000, 35.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((60.600000, 3.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((61.650000, 2.925000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((62.175000, 2.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((62.700000, 2.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((63.075000, 2.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((63.300000, 1.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((64.125000, 0.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((64.950000, 0.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((62.400000, 0.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((60.225000, 0.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((60.375000, 0.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((60.150000, 1.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((59.925000, 2.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((59.700000, 2.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((64.425000, 35.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((65.250000, 34.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((66.075000, 32.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((66.600000, 31.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((65.550000, 30.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((64.350000, 29.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((63.600000, 29.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((62.550000, 29.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((61.425000, 30.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((60.375000, 31.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((60.150000, 32.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((60.900000, 32.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((61.725000, 32.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((62.625000, 33.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((63.300000, 35.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((63.600000, 35.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((60.825000, 52.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((62.625000, 52.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((64.500000, 51.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((64.350000, 50.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((63.150000, 50.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((61.575000, 50.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((60.825000, 51.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((63.450000, 46.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((63.975000, 46.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((64.350000, 45.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((63.750000, 44.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((63.075000, 42.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((62.550000, 41.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((62.100000, 43.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((62.250000, 46.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((62.850000, 47.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((62.775000, 15.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((63.750000, 15.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((64.500000, 14.925000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((65.025000, 14.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((65.100000, 14.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((65.100000, 13.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((64.275000, 13.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((63.225000, 13.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((62.775000, 14.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((62.325000, 15.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((64.050000, 24.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((65.175000, 24.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((65.850000, 23.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((66.000000, 21.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((65.400000, 21.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((64.500000, 21.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((63.300000, 22.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((62.550000, 23.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((62.925000, 24.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((65.400000, 28.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((65.025000, 27.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((64.050000, 26.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((63.225000, 26.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((63.150000, 27.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((63.600000, 28.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((64.200000, 28.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((64.725000, 28.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((65.175000, 29.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((65.850000, 41.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((66.825000, 40.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((66.975000, 38.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((65.325000, 36.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((63.450000, 37.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((63.300000, 37.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((63.450000, 38.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((64.050000, 39.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((64.725000, 40.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((64.800000, 49.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((66.225000, 49.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((67.350000, 48.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((67.425000, 47.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((67.275000, 47.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((66.675000, 47.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((65.100000, 48.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((65.175000, 3.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((66.225000, 2.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((66.675000, 1.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((66.225000, 0.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((65.475000, 0.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((64.875000, 2.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((66.525000, 44.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((66.900000, 43.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((66.150000, 42.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((65.100000, 43.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((65.100000, 44.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((65.775000, 44.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((69.675000, 16.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((69.150000, 15.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((67.950000, 14.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((66.075000, 15.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((64.875000, 16.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((65.025000, 17.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((65.400000, 17.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((67.350000, 17.925000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((69.450000, 17.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((66.300000, 35.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((67.725000, 34.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((68.550000, 33.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((68.100000, 32.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((67.500000, 31.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((66.525000, 33.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((65.550000, 34.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((65.550000, 35.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((70.050000, 26.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((69.525000, 26.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((68.700000, 26.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((67.950000, 26.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((66.750000, 25.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((65.850000, 26.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((65.700000, 26.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((66.075000, 27.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((66.450000, 28.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((68.025000, 27.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((69.825000, 27.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((66.225000, 13.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((66.975000, 13.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((67.800000, 13.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((68.700000, 13.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((69.075000, 12.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((68.100000, 12.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((66.975000, 12.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((66.300000, 12.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((65.700000, 12.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((67.275000, 11.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((68.400000, 10.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((68.475000, 9.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((67.200000, 9.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((66.600000, 10.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((67.950000, 23.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((67.350000, 22.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((66.900000, 23.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((67.500000, 24.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((67.500000, 21.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((68.475000, 20.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((69.000000, 19.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((69.375000, 19.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((68.775000, 18.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((67.575000, 19.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((67.050000, 19.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((66.900000, 20.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((68.775000, 44.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((68.400000, 43.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((67.575000, 43.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((67.800000, 44.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((68.250000, 45.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((68.400000, 45.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((68.475000, 51.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((69.225000, 51.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((69.900000, 51.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((70.950000, 50.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((71.400000, 50.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((71.025000, 49.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((70.650000, 49.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((70.425000, 49.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((69.900000, 49.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((68.850000, 49.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((67.950000, 50.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((67.800000, 50.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((68.775000, 7.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((71.400000, 7.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((74.250000, 7.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((75.000000, 3.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((73.275000, 0.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((69.825000, 0.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((68.175000, 2.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((68.550000, 4.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((68.775000, 5.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((68.400000, 6.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((68.175000, 7.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((68.700000, 23.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((69.450000, 23.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((69.900000, 22.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((69.375000, 22.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((68.625000, 22.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((70.350000, 41.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((71.025000, 39.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((71.475000, 38.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((70.725000, 36.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((69.300000, 37.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((68.625000, 39.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((69.450000, 40.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((69.375000, 29.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((69.750000, 30.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((70.350000, 30.375000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((71.775000, 29.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((72.675000, 28.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((72.225000, 27.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((70.725000, 28.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((69.450000, 28.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((69.075000, 29.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((70.050000, 35.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((70.575000, 34.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((71.100000, 33.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((71.400000, 32.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((71.625000, 32.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((72.225000, 30.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((72.300000, 30.000000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((71.850000, 30.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((71.175000, 30.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((70.350000, 31.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((69.600000, 31.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((69.150000, 32.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((69.450000, 32.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((69.750000, 34.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((69.825000, 48.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((71.025000, 46.425000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((72.300000, 43.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((72.900000, 42.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((72.225000, 42.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((70.575000, 42.900000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((69.450000, 46.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((72.375000, 14.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((71.925000, 14.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((71.100000, 13.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((70.350000, 13.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((69.825000, 14.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((70.125000, 15.225000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((70.875000, 15.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((71.775000, 15.450000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((70.125000, 10.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((70.650000, 9.975000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((71.550000, 8.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((72.150000, 8.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((71.625000, 7.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((70.650000, 8.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((70.050000, 9.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((73.350000, 27.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((72.900000, 26.325000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((71.925000, 25.650000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((71.325000, 25.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((70.650000, 25.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((70.200000, 25.800000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((71.850000, 26.850000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((73.200000, 52.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((75.000000, 49.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((73.650000, 46.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((72.225000, 47.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((72.825000, 48.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((73.500000, 49.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((72.825000, 50.775000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((71.775000, 51.825000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((71.400000, 52.275000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((72.225000, 20.625000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((73.350000, 20.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((74.475000, 19.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((75.000000, 17.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((74.625000, 16.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((72.900000, 18.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((71.475000, 19.875000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((71.550000, 20.400000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((73.425000, 13.050000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((74.400000, 12.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((75.000000, 10.350000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((73.200000, 9.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((71.550000, 11.100000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((72.000000, 11.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((72.675000, 12.300000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((72.375000, 40.725000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((73.650000, 40.575000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((74.100000, 39.750000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((73.650000, 38.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((72.975000, 38.250000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((72.600000, 38.700000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((72.450000, 39.150000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((72.000000, 39.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((71.700000, 40.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((75.000000, 24.600000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((74.250000, 22.200000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((72.825000, 21.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((72.075000, 22.500000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((72.300000, 23.475000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((72.900000, 24.525000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((73.725000, 26.025000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((74.625000, 26.550000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((74.175000, 36.675000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((75.000000, 34.125000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((74.625000, 31.950000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((73.200000, 33.075000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((72.300000, 35.175000,0),),
)
e0=e0+e[0:1]
e = p.edges.findAt(
((72.900000, 36.600000,0),),
)
e0=e0+e[0:1]
p.Set(name = 'Edge_origin' , edges=e0[0:len(e0)])
f2=mdb.models['Model-1'].parts['Part-1'].faces
for i in range(len(f2)):
  mdb.models['Model-1'].parts['Part-1'].Set(name = 'Set'+str(i) , faces=f2[i:i+1])
print 'Finish'
