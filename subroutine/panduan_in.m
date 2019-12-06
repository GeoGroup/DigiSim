function [ pos ] = panduan_in(dat,vert)
%judge the existence of Line
if size(vert,2)==1
    T1=dat(:,1)-vert(1,1);
    T1=sum(abs(T1),2);    
    pos=find(T1==0);
elseif size(vert,2)==2
    T1=[dat(:,1)-vert(1,1),dat(:,2)-vert(1,2)];
    T1=sum(abs(T1),2);    
    pos=find(T1==0);
elseif size(vert,2)==4
    T1=[dat(:,1)-vert(1,1),dat(:,2)-vert(1,2),dat(:,3)-vert(1,3),dat(:,4)-vert(1,4)];
    T1=sum(abs(T1),2);    
    pos=find(T1==0);
end    
end

