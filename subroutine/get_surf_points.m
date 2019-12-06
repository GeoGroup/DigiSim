function [jl,pos]=get_surf_points(a,b,error)
% maximum point to a plane
va=[b(2,1)-b(1,1),b(2,2)-b(1,2),b(2,3)-b(1,3)];
vb=[b(3,1)-b(1,1),b(3,2)-b(1,2),b(3,3)-b(1,3)];
vc=cross(va,vb);
% jl=0;pos=1;
pos=zeros(100,1);
jl=0;
for i=1:size(a,1)
    t=a(i,:);
    vt=vc(1)*(t(1,1)-b(1,1))+vc(2)*(t(1,2)-b(1,2))+vc(3)*(t(1,3)-b(1,3));
    lt=abs(vt)/sqrt(vc(1)^2+vc(2)^2+vc(3)^2);
    if lt<error
        jl=jl+1;
        pos(jl)=i;
    end
end
pos=pos(1:jl);
end

