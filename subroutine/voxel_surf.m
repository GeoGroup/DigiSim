function [surf,center] = voxel_surf(x,y,z)
% Change voxel to surfaces
% and centers
%
%           P8 .......P7
%      P5 ........ P6  .
%       .   P4.........P3
%       P1.........P2
p1=[x-1;y-1;z-1];
p2=[x;y-1;z-1];
p3=[x;y;z-1];
p4=[x-1;y;z-1];
p5=[x-1;y-1;z];
p6=[x;y-1;z];
p7=[x;y;z];
p8=[x-1;y;z];
% surfs=cell(1,6);
% surf{1}=[p1,p2,p3,p4];
% surf{2}=[p5,p6,p7,p8];
% surf{3}=[p1,p4,p8,p5];
% surf{4}=[p2,p3,p7,p6];
% surf{5}=[p1,p2,p6,p5];
% surf{6}=[p4,p3,p7,p8];
surf=[p1,p2,p3,p4, ...
      p5,p6,p7,p8, ...
      p1,p4,p8,p5, ...
      p2,p3,p7,p6, ...
      p1,p2,p6,p5, ...
      p4,p3,p7,p8];
center=[(p1+p2+p3+p4)/4, ...
        (p5+p6+p7+p8)/4, ...
        (p1+p4+p8+p5)/4, ...
        (p2+p3+p7+p6)/4, ...
        (p1+p2+p6+p5)/4, ...
        (p4+p3+p7+p8)/4];
end

% x = [0 1 1 0];
% y = [0 0 1 1];
% z = [1 1 1 1];
% patch(x,y,z,'red');
% z = [0 0 0 0];
% patch(x,y,z,'red');