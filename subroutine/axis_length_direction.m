function [ e,l,w,alpha,beta] = axis_length_direction( p )
% Get the boundary of polygon
% (y-y2)/(y1-y2) = (x-x2)/(x1-x2)
% 1/(x1-x2)*x+[-1/(y1-y2)]*y+y2/(y1-y2)-x2/(x1-x2)
e=zeros(5,2);
n=size(p,1);
D=pdist(p);
D=squareform(D);
T=max(D(:));
[row,col]=find(D==T);
% row=sort(row);
x1=p(row(1),1);x2=p(col(1),1);
y1=p(row(1),2);y2=p(col(1),2);
% plot(p(:,1),p(:,2),'-o');hold on
% plot([x1,x2],[y1,y2],'-o');hold on
l=sqrt((x2-x1)^2+(y2-y1)^2);
A=1/(x1-x2);B=-1/(y1-y2);C=y2/(y1-y2)-x2/(x1-x2);
if row(1)<col(1)
    up=row(1)+1:col(1)-1;
else
    up=col(1)+1:row(1)-1;
end
all=setdiff(1:n,[row(1),col(1)]);
down=setdiff(all,up);
dist=zeros(length(up),1);
maxv=0;point=[0,0];
for i=1:length(up)
    dist(i)=(A*p(up(i),1)+B*p(up(i),2)+C)/sqrt(A^2+B^2);
    if abs(dist(i))>maxv
        maxv=abs(dist(i));
        point=p(up(i),:);
%         maxi=i;
    end
end
w=maxv;
% plot(point(1),point(2),'b*'); hold on
a=[x2-x1,y2-y1];
b=[point(1)-x1,point(2)-y1];
c=dot(a,b)/norm(a)/norm(b)*norm(b)*a/norm(a);
d=b-c;
x1n=x1+d(1);y1n=y1+d(2);
x2n=x2+d(1);y2n=y2+d(2);
% plot([x1n,x2n],[y1n,y2n],'-*');hold on

e(1,:)=[x2n,y2n];
e(2,:)=[x1n,y1n];

e(5,:)=e(1,:);
maxv=0;point=[0,0];
for i=1:length(down)
    dist(i)=(A*p(down(i),1)+B*p(down(i),2)+C)/sqrt(A^2+B^2);
    if abs(dist(i))>maxv
        maxv=abs(dist(i));
        point=p(down(i),:);
%         maxi=i;
    end
end
w=w+maxv;
a=[x2-x1,y2-y1];
b=[point(1)-x1,point(2)-y1];
c=dot(a,b)/norm(a)/norm(b)*norm(b)*a/norm(a);
d=b-c;
x1n=x1+d(1);y1n=y1+d(2);
x2n=x2+d(1);y2n=y2+d(2);
% plot([x1n,x2n],[y1n,y2n],'-*');hold on
% hold on;plot([x1n,x2n],[y1n,y2n],'-*');
e(4,:)=[x2n,y2n];
e(3,:)=[x1n,y1n];
% calcualte the axis direction
if e(2,2)>=e(1,2)
    axis=e(2,:)-e(1,:);
else
    axis=e(1,:)-e(2,:);
end
alpha=acos(axis(1)/norm(axis))*180/pi;
if e(3,2)>=e(2,2)
    axis=e(3,:)-e(2,:);
else
    axis=e(2,:)-e(3,:);
end
beta=acos(axis(1)/norm(axis))*180/pi;
% plot(e(:,1),e(:,2));
end

