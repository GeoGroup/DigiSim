function geom_plot(P)
% Plot the geometry information
for i=1:size(P,2)
   for j=1:P{1,i}
        tmp=P{j+1,i};
        plot(tmp(:,1),tmp(:,2),'-');hold on
   end
end
tmp=P{2,size(P,2)};
% axis([0 max(tmp(:,1))*1.2 0 max(tmp(:,2))*1.2]);
axis off
end