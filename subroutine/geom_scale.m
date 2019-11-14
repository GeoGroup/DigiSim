function P=geom_scale(P,scale)
% Geometry rescale with a uniform factor
for i=1:size(P,2)
    for j=1:P{1,i}
%         tmp=P{j+1,i};
%         plot(tmp(:,1),tmp(:,2),'-o');hold on
        P{j+1,i}=P{j+1,i}*scale;
    end
end

end

