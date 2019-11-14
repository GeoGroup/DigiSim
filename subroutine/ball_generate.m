function ballid=ball_generate(P,radius)
% radius=2;
tmp=P{2,size(P,2)};
domain.size1=max(tmp(:,1));
domain.size2=max(tmp(:,2));
nx=floor(domain.size1/radius/2);
ny=floor(domain.size2/radius/sqrt(3));
nball=0;%kk=0;
% I=length(Polygon.poly);
ball=zeros(100000,2);
for i=1:ny%ny
    if mod(i,2)==1
        for j=1:nx%nx
            index=0;
            x=radius+(j-1)*2*radius;
            y=radius+(i-1)*sqrt(3)*radius;
            nball=nball+1;
            ball(nball,:)=[x,y];
        end
    else
        for j=1:nx-1
            index=0;
            x=(j-1)*2*radius+2*radius;
            y=radius+(i-1)*sqrt(3)*radius;%-sqrt(3)/2*radius;         
            nball=nball+1;
            ball(nball,:)=[x,y];
        end
    end
end
ball=ball(1:nball,:);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

ballid=cell(size(P,2),1);

for i=1:size(P,2)-1
    tmp=P{2,i};
    xv=tmp(:,1);yv=tmp(:,2);
%     plot(xv,yv,'-');hold on
    if P{1,i}>1
        in=inpolygon(ball(:,1),ball(:,2),xv,yv);
        btmp=ball(in,:);
        bleft=ball(~in,:);
        for j=1:P{1,i}-1
            tmp=P{2+j,i};
            xv=tmp(:,1);yv=tmp(:,2);
%             plot(xv,yv,'-');hold on            
            in=inpolygon(btmp(:,1),btmp(:,2),xv,yv);
            bleft=[bleft;btmp(in,:)];
            btmp=btmp(~in,:);
        end
%         plot(btmp(:,1),btmp(:,2),'o'); hold on
        ball=bleft;
    else
        in=inpolygon(ball(:,1),ball(:,2),xv,yv);
        btmp=ball(in,:);
%         plot(btmp(:,1),btmp(:,2),'o'); hold on
        ball=ball(~in,:);
    end
    ballid{i}=btmp;
end
ballid{i+1}=ball;
% plot(ball(:,1),ball(:,2),'o','Color',[0.5 0.5 0.5]);
% axis off
end

