function [K,PT] = regulization(pcenter,K,PT,error)
% Remove small edges
% K=particle{II}.conn;
% PT=particle{II}.vert;
% pcenter=particle{II}.pcenter;
% error=5;
LT=error-0.001;
while LT<error
    ibreak=0;
    for i=1:size(K,1)
        vt=K(i,:);
        vt(length(vt)+1)=vt(1);
        for j=1:length(vt)-1
            lt=norm(PT(vt(j+1),:)-PT(vt(j),:));
            if lt>LT
                LT=lt;
            end
            if lt<error
%                 disp(lt);
                id_ori=[vt(j),vt(j+1)];                
                PT(size(PT,1)+1,:)=(PT(vt(j+1),:)+PT(vt(j),:))/2;
                PT(id_ori,:)=[];
                [azimuth,elevation,r] = cart_sph(PT,pcenter);
                [x,y,z]=sph2cart(azimuth,elevation,ones(size(r)));
                PR=[x,y,z]; % PR means the Cartesian Coordinates on a unit sphere
                X=PR;K = convhulln(X);                
                ibreak=1;LT=error-0.001;
                break;
            end
        end
        if ibreak==1            
            break;
        end
%         disp(LT);
    end
end
% trisurf(K,PT(:,1),PT(:,2),PT(:,3));
end

