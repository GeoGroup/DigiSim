clear;clc
tic;
addpath subroutine
% image_file='DigiSim.jpg';
image_file='3phase.jpg';
scale=0.1;  error=3.5;
fn=image_file(1:length(image_file)-4);
x1=imread(image_file);
x=x1(:,:,1);
% Vectorization bitmap
x1=x;
x1(x1<240)=0;
x1(x1>240)=1;
[P1] = vectorization2(x1,error);
% imshow(x1*255);
x2=x;
x2(x2<195)=1;
x2(x2>195)=0;
[P2] = vectorization2(x2,error);
P1(:,size(P1,2))=[];
P=[P1,P2];
group=[ones(1,size(P1,2)),ones(1,size(P2,2))*2];
% 
P=geom_scale(P,scale);
figure(1);
geom_plot(P,group);
% Geometry information analysis
[parea,fraction]=geom_area(P);
mg=min_bound_box2(P);
% Geometry information OutPut
dxf_file=[fn,'.dxf'];
dxf_file_write(P,dxf_file);
abaqus_file=[fn,'.py'];
write_abaqus_2d(abaqus_file,P,group);
toc;