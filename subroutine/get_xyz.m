function [x,y,z] = get_xyz(zp2,P)
% 
xyz=zp2(P,:)';
x=xyz(1,:);
y=xyz(2,:);
z=xyz(3,:);

end

