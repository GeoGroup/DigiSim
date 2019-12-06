function geom_plot(P,group)
% Plot the geometry information
if nargin==1
    for i=1:size(P,2)
        for j=1:P{1,i}
            tmp=P{j+1,i};
            plot(tmp(:,1),tmp(:,2),'-');hold on
        end
    end
    % tmp=P{2,size(P,2)};
    % axis([0 max(tmp(:,1))*1.2 0 max(tmp(:,2))*1.2]);
    axis off
elseif nargin==2
    for i=1:size(P,2)
        if group(i)==1
            for j=1:P{1,i}
                tmp=P{j+1,i};
                plot(tmp(:,1),tmp(:,2),'r-');hold on
            end
        else
            for j=1:P{1,i}
                tmp=P{j+1,i};
                plot(tmp(:,1),tmp(:,2),'b-');hold on
            end
        end
    end
    % tmp=P{2,size(P,2)};
    axis off
end

end