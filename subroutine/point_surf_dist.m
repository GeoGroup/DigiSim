function dist = point_surf_dist(a,b)
% a is the Cartesian Coordinates
% b is the surf with three points
va=[b(2,1)-b(1,1),b(2,2)-b(1,2),b(2,3)-b(1,3)];
vb=[b(3,1)-b(1,1),b(3,2)-b(1,2),b(3,3)-b(1,3)];
vc=cross(va,vb);
vt=vc(1)*(a(:,1)-b(1,1))+vc(2)*(a(:,2)-b(1,2))+vc(3)*(a(:,3)-b(1,3));
dist=abs(vt)/sqrt(vc(1)^2+vc(2)^2+vc(3)^2);

end

