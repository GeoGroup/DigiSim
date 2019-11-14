function geo_sta_plot(mg,parea)
% plot the geometry statistic information
x=zeros(size(mg,1),5);
for i=1:size(mg,1)
    x(i,1)=parea(i);
    x(i,2)=mg{i,2};
    x(i,3)=mg{i,3};
    x(i,4)=mg{i,4};
    x(i,5)=mg{i,6};
end
x(x(:,5)==1,:)=[];
x=sortrows(x,3);
radius=x(:,3);
area=x(:,1);
s=cumsum(area);
s=s/s(length(s));
figure(2)
semilogx(radius,s*100,'LineWidth',1.5);
set(gca, 'YTick', [0 20 40 60 80 100]);
set(gca,'FontSize',12,'Fontname', 'Times New Roman');
xlabel('Particle Size');
ylabel('Cumulative percentage(%)');
xlim([0.1 10]);
grid on
% % plot(radius,s*100);
set(gca,'xdir','reverse')

figure(3)
theta=x(:,4);
theta1=[theta;theta+180];
polarhistogram(theta1*pi/180,24)

end

