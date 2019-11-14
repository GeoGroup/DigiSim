clear;clc
tic;
addpath subroutine
image_file='concrete.jpg';
% image_file='DigiSim.jpg';
fn=image_file(1:length(image_file)-4);
% Vectorization bitmap
scale=1/10;error=1.4;
[ P] = vectorization2(image_file,error);
P=geom_scale(P,scale);
figure(1);
geom_plot(P);
% Geometry information analysis
[parea,fraction]=geom_area(P);
mg=min_bound_box2(P);
mbr_plot(mg);
geo_file='geometry.xls';
geom_stas(geo_file,parea,fraction,mg,P);
geo_sta_plot(mg,parea);
% Geometry information OutPut
dxf_file=[fn,'.dxf'];
dxf_file_write(P,dxf_file);
gmsh_file=[fn,'.geo'];
lc=5;lc2=10;
gmsh_file_write(P,gmsh_file,lc,lc2);
abaqus_file=[fn,'.py'];
write_abaqus_2d(abaqus_file,P);
pfc_file=[fn,'.p2dat'];
radius=1;
write_pfc_2d_group(P,radius,pfc_file);
toc;