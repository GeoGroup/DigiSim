function [particle] = get_particle(T,iparticle,error)
% get one particle
[l,m,n] = ind2sub(size(T),find(T == iparticle));
view(3)
t_surf=cell(length(l)*6,1);
t_center=zeros(3,length(l)*6);
for I=1:length(m)
    [surfs,center] = voxel_surf(l(I),m(I),n(I));
    for i=1:6
        x=surfs(1,(i-1)*4+1:4*i);
        y=surfs(2,(i-1)*4+1:4*i);
        z=surfs(3,(i-1)*4+1:4*i);
        t_surf{(I-1)*6+i}=[x;y;z];
    end
    t_center(:,(I-1)*6+1:(I-1)*6+6)=center;
end
t_center=t_center';
[C,IA,IC]=unique(t_center,'rows');
index=1:1:length(l)*6;
irep=setdiff(index,IA);
tirep=t_center(irep,:);
[c]=setdiff(C,tirep,'rows');
[C,ia,ib] = intersect(t_center,c,'rows');

zp=zeros(3,4*length(ia));
for i=1:length(ia)
    xyz=t_surf{ia(i)};
    zp(:,4*(i-1)+1:4*i)=xyz;
    x=xyz(1,:);
    y=xyz(2,:);
    z=xyz(3,:);
    %     patch(x,y,z,'blue'); hold on
    %     plot3(t_center(ia(i),1),t_center(ia(i),2),t_center(ia(i),3),'*'); hold on
end
alpha(0.2);
% plot3(zp(1,:),zp(2,:),zp(3,:),'*');hold on;
zp2=unique(zp','rows');
% plot3(zp2(:,1),zp2(:,2),zp2(:,3),'*');
D=pdist(zp2);
D=squareform(D);
TD=max(D(:));
[row,col]=find(D==TD);
[P]=sort([row(1),col(1)]);
% plot3(zp2(P,1),zp2(P,2),zp2(P,3),'-o'); hold on
line1=zp2(P,:);
% add two points into maximum octahedron
PT=zeros(6,3);
PT(1,:)=line1(1,:);
PT(3,:)=line1(2,:);

[~,pos]=dis_cal(zp2,line1);
P=[P,pos];

surf1=zp2(P,:);
[~,pos]=get_surf_points(zp2,surf1,0.1);
zp3=zp2(pos,:);
%     [x,y,z]= get_xyz(zp2,pos); %plot3(x,y,z,'o');hold on
[~,pos]=dis_cal_surf(zp2,surf1,1);
% [x,y,z]= get_xyz(zp2,pos); plot3(x,y,z,'*');hold on
surf2=zp2([P(1),P(2),pos],:);
[~,pos]=dis_cal_surf(zp3,surf2,2);
% [x,y,z]= get_xyz(zp3,pos); plot3(x,y,z,'*');hold on
% add a new point into maximum octahedron
PT(2,:)=zp3(pos,:);

[~,pos]=dis_cal_surf(zp3,surf2,3);
% [x,y,z]= get_xyz(zp3,pos); plot3(x,y,z,'*');hold on
% add a new point into maximum octahedron
PT(4,:)=zp3(pos,:);

% get the point out of surf
[~,pos]=dis_cal_surf(zp2,surf1,2);
% [x,y,z]= get_xyz(zp2,pos); plot3(x,y,z,'*');hold on
PT(5,:)=zp2(pos,:);
[jl,pos]=dis_cal_surf(zp2,surf1,3);
% [x,y,z]= get_xyz(zp2,pos); plot3(x,y,z,'*');hold on
PT(6,:)=zp2(pos,:);

pcenter=sum(PT)/length(PT);

%% get first polyhedron
% error=1.8;
TV=error+0.001;
I=size(PT,1);
while TV>error
%     disp('OK');
    [azimuth,elevation,r] = cart_sph(PT,pcenter);
    [x,y,z]=sph2cart(azimuth,elevation,ones(size(r)));
    PR=[x,y,z]; % PR means the Cartesian Coordinates on a unit sphere
    X=PR;
    K = convhulln(X);
    % X=PT;
    % trisurf(K,X(:,1),X(:,2),X(:,3));
    Pseg=cell(size(K,1),1);
    Pdis=zeros(size(K,1),1);
    tp=zp2;
    for i=1:size(K,1)
        it=0;tmp=tp;
        v1=PT(K(i,1),:);v2=PT(K(i,2),:);v3=PT(K(i,3),:);
        for j=1:size(tp,1)
            direction=tp(j,:)-pcenter;
            [flag, ~, ~, dist] = rayTriangleIntersection(pcenter, direction, v1, v2, v3);
            if flag==1 && dist>0
                it=it+1;
                tmp(it,:)=tp(j,:);
            end
        end
        Pseg{i,1}=tmp(1:it,:);
        
        [jl,pos]=dis_cal_surf(Pseg{i,1},PT(K(i,:),:),1);
        if jl>error
            I=I+1;
            PT(I,:)=tmp(pos,:);
        end
        Pdis(i,1)=jl;
        tp=setdiff(tp,Pseg{i,1},'rows');
    end
    TV=max(Pdis);
%     disp(TV);
end

[azimuth,elevation,r] = cart_sph(PT,pcenter);
[x,y,z]=sph2cart(azimuth,elevation,ones(size(r)));
PR=[x,y,z]; % PR means the Cartesian Coordinates on a unit sphere
X=PR;
K = convhulln(X);
% X=PT;


[K,PT] = regulization(pcenter,K,PT,3);

error=3;
[lx,ly,lz]=size(T);
for i=1:size(PT,1)
    tmp=PT(i,:);
    if abs(tmp(1))<error
        tmp(1)=0;
    elseif abs(tmp(1)-lx)<error
        tmp(1)=lx;
    end
    if abs(tmp(2))<error
        tmp(2)=0;
    elseif abs(tmp(2)-ly)<error
        tmp(2)=ly;
    end
    if abs(tmp(3))<error
        tmp(3)=0;
    elseif abs(tmp(3)-lz)<error
        tmp(3)=lz;
    end
    PT(i,:)=tmp;
end

particle.conn=K;
particle.vert=PT;
particle.pcenter=pcenter;
particle = merge_surf(particle);
% trisurf(K,PT(:,1),PT(:,2),PT(:,3)); hold on
end

