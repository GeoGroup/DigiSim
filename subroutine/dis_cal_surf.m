function [jl,pos]=dis_cal_surf(a,b,option)
%  point with maximum distance to a plane
%  option== 1 means total; 2 means negative direction ; 3 means positive direction
va=[b(2,1)-b(1,1),b(2,2)-b(1,2),b(2,3)-b(1,3)];
vb=[b(3,1)-b(1,1),b(3,2)-b(1,2),b(3,3)-b(1,3)];
vc=cross(va,vb);
jl=0;pos=1;
if option==1
for i=1:size(a,1)
    t=a(i,:);
    vt=vc(1)*(t(1,1)-b(1,1))+vc(2)*(t(1,2)-b(1,2))+vc(3)*(t(1,3)-b(1,3));
    lt=abs(vt)/sqrt(vc(1)^2+vc(2)^2+vc(3)^2);
    if jl<lt
        jl=lt;
        pos=i;
    end
end
elseif option==2
    for i=1:size(a,1)
        t=a(i,:);
        vt=vc(1)*(t(1,1)-b(1,1))+vc(2)*(t(1,2)-b(1,2))+vc(3)*(t(1,3)-b(1,3));
        lt=(vt)/sqrt(vc(1)^2+vc(2)^2+vc(3)^2);
        if lt>0
            if jl<lt
                jl=lt;
                pos=i;
            end
        end
    end
elseif option==3
    for i=1:size(a,1)
        t=a(i,:);
        vt=vc(1)*(t(1,1)-b(1,1))+vc(2)*(t(1,2)-b(1,2))+vc(3)*(t(1,3)-b(1,3));
        lt=(vt)/sqrt(vc(1)^2+vc(2)^2+vc(3)^2);
        if lt<0
            lt=abs(lt);
            if jl<lt
                jl=lt;
                pos=i;
            end
        end
    end
end
end

