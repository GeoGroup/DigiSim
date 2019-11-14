function [parea,fraction]=geom_area(P)
%  area of microstructure geometry
parea=zeros(size(P,2),1);
for i=1:size(P,2)
    tmp=P{2,i};
    parea(i)=polyarea(tmp(:,1)',tmp(:,2)',2);
    if P{1,i}>1
        for j=1:P{1,i}-1
            tmp=P{2+j,i};
            parea(i)=parea(i)-polyarea(tmp(:,1)',tmp(:,2)',2);
        end
    end
end
fraction=sum(parea(1:size(P,2)-1))/parea(size(P,2));
end

