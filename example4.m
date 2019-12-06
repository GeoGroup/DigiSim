clear;clc
tic;
addpath subroutine
addpath subroutine\rayTriangleIntersection
% image_file='DigiSim.jpg';
image_file='Image3D.mat';error=2.5;
fn=image_file(1:length(image_file)-4);
[particle,V] =vectorization3(image_file,error);
fout=[fn,'.py'];
out_abaqus_python( particle,V,fout);
toc;