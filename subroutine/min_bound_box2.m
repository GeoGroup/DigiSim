function mg=min_bound_box2(P)
% Get the  microstructures geometry
% bbox=cell(size(P,2)-1,1);
Lx=max(P{2,size(P,2)}(:,1));
Ly=max(P{2,size(P,2)}(:,2));
mg=cell(size(P,2)-1,6);
for i=1:size(P,2)-1
    X=P{2,i};
    bb = minBoundingBox(X');
    bb(:,5)=bb(:,1);
    % anlysis the axis information
    t1=norm(bb(:,2)-bb(:,1));
    t2=norm(bb(:,3)-bb(:,2));
    if t1>t2
        l=t1;w=t2;
        axis=bb(:,2)-bb(:,1);
        if axis(2)<0
            axis=-axis;
        end
        alpha=acos(axis(1)/norm(axis))*180/pi;
        if alpha>90
            beta=alpha-90;
        else
            beta=alpha+90;
        end
    else
        l=t2;w=t1;
        axis=bb(:,3)-bb(:,2);
        if axis(2)<0
            axis=-axis;
        end
        alpha=acos(axis(1)/norm(axis))*180/pi;
        if alpha>90
            beta=alpha-90;
        else
            beta=alpha+90;
        end
    end
        
%     bbox{i}=bb';
    mg{i,1}=bb';
    mg{i,2}=l;
    mg{i,3}=w;
    mg{i,4}=alpha;
    mg{i,5}=beta;
    % judge wether at the boundary
    tmp=P{2,i};
    x1=min(tmp(:,1));x2=max(tmp(:,1));
    y1=min(tmp(:,2));y2=max(tmp(:,2));
    isb=0;
    if x1==0 && y1==0
        isb=1;
    elseif x1==0 && y2==Ly
        isb=1;
    elseif x2==Lx && y2==Ly
        isb=1;
    elseif x2==Lx && y1==0
        isb=1;
    elseif x1==0 && (y1~=0 || y2~=Ly)
        isb=1;
    elseif x2==Lx && (y1~=0 || y2~=Ly)
        isb=1;
    elseif (x1 ~=0 || x2~=Lx) && y1==0
        isb=1;
    elseif (x1 ~=0 || x2~=Lx) && y2==Ly
        isb=1;
    end
    mg{i,6}=isb;
%     plot(bb(1,:),bb(2,:),'-*');hold on
end


end

