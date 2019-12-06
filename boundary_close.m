function [x,y] = boundary_close(x,y,P,err)
%UNTITLED7 此处显示有关此函数的摘要
L=max(P{2,size(P,2)});
lx=L(1);ly=L(2);
for i=1:length(x)
    if abs(x(i)-0)<=err
        x(i)=0;
    elseif abs(x(i)-lx)<=err
        x(i)=lx;
    end
end
for i=1:length(y)
    if abs(y(i)-0)<=err
        y(i)=0;
    elseif abs(y(i)-ly)<=err
        y(i)=ly;
    end
    
end

