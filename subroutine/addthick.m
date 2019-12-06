function pf=addthick(p,thick)
% Add thickness of a polygon
pf=p;
for i=1:length(p)
    if i==1
        a=[p(i,1)-p(length(p),1),p(i,2)-p(length(p),2)];
        b=-[p(i,1)-p(i+1,1),p(i,2)-p(i+1,2)];
    elseif i==length(p)
        a=[p(i,1)-p(i-1,1),p(i,2)-p(i-1,2)];
        b=-[p(i,1)-p(1,1),p(i,2)-p(1,2)];
    else
        a=[p(i,1)-p(i-1,1),p(i,2)-p(i-1,2)];
        b=-[p(i,1)-p(i+1,1),p(i,2)-p(i+1,2)];
    end
    a=[a(2),-a(1)];
    b=[b(2),-b(1)];
    a=a/norm(a);
    b=b/norm(b);
    a=a*thick;
    b=b*thick;
%     disp(a);
    pf(i,1)=p(i,1)+a(1)+b(1);
    pf(i,2)=p(i,2)+a(2)+b(2);
%     direction=(a+b);
%     direction=direction/norm(direction);
%     theta=acos(dot(a,b)/norm(a)/norm(b))/2;
%     tmp=a(1)*b(2)-a(2)*b(1);
    %http://blog.csdn.net/hy3316597/article/details/52732963
%     if tmp>0
%         leng=thick/sin(theta);
%     else
%        leng=-thick/sin(theta);
%     end
%     pf(i,1)=p(i,1)+a+b;
%     pf(i,2)=p(i,2)+direction(2)*leng;
end

end

