function [jl,pos]=dis_cal(a,b)
v=[b(2,1)-b(1,1),b(2,2)-b(1,2)];
vl=sqrt(v(1)^2+v(2)^2);
jl=0;pos=1;
for i=1:size(a,1);
    t=a(i,:);
    vt=[t(1,1)-b(1,1),t(1,2)-b(1,2)];
    cost=vt*v'/vl/sqrt(vt(1)^2+vt(2)^2);
    sint=sqrt(1-cost^2);
    lt=sqrt(vt(1)^2+vt(2)^2)*sint;
    if jl<lt
        jl=lt;
        pos=i;
    end    
end
end

