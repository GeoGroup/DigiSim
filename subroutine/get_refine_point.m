function pts=get_refine_point(P,N,distance)
% N=300;   distance=0.05;
points = point_min_distance(N,distance);
l=P{2,size(P,2)};
lxy=max(l);
pts=[points(:,1)*lxy(1),points(:,2)*lxy(2)];
% plot(pts(:,1),pts(:,2),'b*'); hold on
for i=1:size(P,2)-1
    vt=P{2,i};
    [in,~] = inpolygon(pts(:,1),pts(:,2),vt(:,1),vt(:,2));
    pts=pts(~in,:);
end
% plot(pts(:,1),pts(:,2),'ro'); hold on
end
