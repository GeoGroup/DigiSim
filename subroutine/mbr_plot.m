function mbr_plot(mg)
% Plot the geometry information
for i=1:size(mg,1)
    tmp=mg{i,1};
    plot(tmp(:,1),tmp(:,2),'-','color',[0.5 0.5 0.5]);hold on
end
axis off
end