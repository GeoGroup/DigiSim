function [particle,D] =vectorization3(filename,error)
% 3D voxel vectorization
% addpath('rayTriangleIntersection');
% filename='dat.mat';
load(filename);
D=V;
T=bwlabeln(D,6);
% error=2.5;
particle=cell(max(T(:)),1);
for II=1:max(T(:))
    disp(['Particle number is ',num2str(II),'/',num2str(max(T(:)))]);
    particle{II} = get_particle(T,II,error);
    K=particle{II}.conn;
    PT=particle{II}.vert;
    K2=particle{II}.poly;
    for i=1:length(K2)
        xyz=PT(K2{i},:)';
        x=xyz(1,:);
        y=xyz(2,:);
        z=xyz(3,:);
        patch(x,y,z,'blue'); hold on
    end
    fname=['particle-',num2str(II),'.stl'];
%     out_particle_stl(fname,K,PT)
end
alpha(0.1);
end