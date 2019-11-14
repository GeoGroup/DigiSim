function [Pleft,Pright,Pdown,Pup,P1,P2,P3,P4,Pmain,Pmain2,PB,k1,k2,k3,k4,k5] = classify_poly5( P )
% % change all the poly to five parts
% % global L;
PM=P;
PT=cell(1,size(P,2));
for i=1:size(P,2)
    PT{1,i}=P{2,i};
end
P=PT;
Lx=max(P{length(P)}(:,1));
Ly=max(P{length(P)}(:,2));
% size(L,1)=P{length(P)}[4,1];
% size(L,2)=P{length(P)}[4,2];
%                       2....................3
%                       .                      .       
%                       .                      .   
%                       1.................... 4 
% k1-4denote the particle number at four noudanry direction k5 means the interier particle
k1=0;k2=0;k3=0;k4=0;k5=0; 
Pleft=cell(1,1);Pright=cell(1,1);
Pdown=cell(1,1);Pup=cell(1,1);
P1=cell(1,1);P2=cell(1,1);
P3=cell(1,1);P4=cell(1,1);
Pmain=cell(1,1);
Pmain2=cell(10,1);
%%%%%%%%%%%%%%%%%%%%%

for i=1:size(P,2)-1
    
    tmp=P{1,i};
    if size(tmp,2)~=0 %%%%
    x1=min(tmp(:,1));x2=max(tmp(:,1));
    y1=min(tmp(:,2));y2=max(tmp(:,2));
    if x1==0 && y1==0
        P1{1}=P{1,i};
    elseif x1==0 && y2==Ly
        P2{1}=P{1,i};
    elseif x2==Lx && y2==Ly
        P3{1}=P{1,i};
    elseif x2==Lx && y1==0
        P4{1}=P{1,i};
    elseif x1==0 && (y1~=0 || y2~=Ly)
        k1=k1+1;
        Pleft{k1}=P{1,i};
    elseif x2==Lx && (y1~=0 || y2~=Ly)
        k2=k2+1;
        Pright{k2}=P{1,i};
    elseif (x1 ~=0 || x2~=Lx) && y1==0
        k3=k3+1;
        Pdown{k3}=P{1,i};
    elseif (x1 ~=0 || x2~=Lx) && y2==Ly
        k4=k4+1;
        Pup{k4}=P{1,i};
    else
        k5=k5+1;
        Pmain{k5}=P{1,i};
        Pmain2{1,k5}=PM{1,i}-1;
        for ii=1:PM{1,i}-1
            Pmain2{1+ii,k5}=PM(2+ii,i);
        end
            
    end
    else
        break %%%%%
    end %%%
end
%fprintf('%d %d %d %d %d\n',k1,k2,k3,k4,k5);
%sort the poly
% find the point of four corner
%Corner 1
PT1=zeros(2,2);
if  isempty(P1{1}) ~= 1
    K=0;
    tmp=P1{1};
    x=tmp(:,1); y=tmp(:,2);
    %    Point 1
    K=K+1;
    pos= (y==0);
    xmax=max(x(pos));
    PT1(K,1:2)=[ xmax,0];
    %    Point 2
    K=K+1;
    pos= (x==0);
    ymax=max(y(pos));
    PT1(K,1:2)=[ 0,ymax];
end
%Corner 2
PT2=zeros(2,2);
if  isempty(P2{1}) ~= 1
    K=0;
    tmp=P2{1};
    x=tmp(:,1); y=tmp(:,2);
    %    Point 1
    K=K+1;
    pos= (x==0);
    ymin=min(y(pos));
    PT2(K,1:2)=[ 0,ymin];
    %    Point 2
    K=K+1;
    pos= (y==Ly);
    xmax=max(x(pos));
    PT2(K,1:2)=[ xmax,0+Ly];
end
%Corner 3
PT3=zeros(2,2);
if  isempty(P3{1}) ~= 1
    K=0;
    tmp=P3{1};
    x=tmp(:,1); y=tmp(:,2);
    %    Point 1
    K=K+1;
    pos= (y==Ly);
    xmin=min(x(pos));
    PT3(K,1:2)=[ xmin,0+Ly];
    %    Point 2
    K=K+1;
    pos= (x==Lx);
    ymin=min(y(pos));
    PT3(K,1:2)=[ 0+Lx,ymin];
end
%Corner 4
PT4=zeros(2,2);
if  isempty(P4{1}) ~= 1
    K=0;
    tmp=P4{1};
    x=tmp(:,1); y=tmp(:,2);
    %    Point 1
    K=K+1;
    pos= (x==Lx);
    ymax=max(y(pos));
    PT4(K,1:2)=[ 0+Lx,ymax];
    %    Point 2
    K=K+1;
    pos= (y==0);
    xmin=min(x(pos));
    PT4(K,1:2)=[ xmin,0];
end
%%%%%%%%%%%%%%%%%%%%%%
%Left Boundary
if k1 ~=0
    PTleft=zeros(2*k1,2);
    for i=1:k1
        tmp=Pleft{1,i};
        x=tmp(:,1); y=tmp(:,2);
        pos= (x==0);
        yp=(y(pos));
        PTleft(2*i-1,:)=[0,min(yp)];
        PTleft(2*i,:)=[0,max(yp)];
    end
    ytmp=PTleft(:,2);
    ytmp=sort(ytmp);
    PTleft=[PTleft(:,1),ytmp];
    ytmp=ytmp(1:2:(size(ytmp,1)-1));
    [TMP,PL_INDEX]=sort(ytmp);
    for m=1:k1
        pn{1,m}=Pleft{1,PL_INDEX(m)};
    end
    Pleft=pn;
end
%Right Boundary
if k2 ~=0
    PTright=zeros(2*k2,2);
    for i=1:k2
        tmp=Pright{1,i};
        x=tmp(:,1); y=tmp(:,2);
        pos= (x==Lx);
        yp=(y(pos));
        PTright(2*i-1,:)=[Lx,min(yp)];
        PTright(2*i,:)=[Lx,max(yp)];
    end
    ytmp=PTright(:,2);
    ytmp=sort(ytmp,'descend');
    PTright=[PTright(:,1),ytmp];
    ytmp=ytmp(1:2:size(ytmp,1)-1);
    [TMP,PR_INDEX]=sort(ytmp,'descend');
    for m=1:k2
        pn{1,m}=Pright{1,PR_INDEX(m)};
    end
    Pright=pn;
end
%Down Boundary
if k3 ~=0
    PTdown=zeros(2*k3,2);
    for i=1:k3
        tmp=Pdown{1,i};
        x=tmp(:,1); y=tmp(:,2);
        pos= (y==0);
        xp=(x(pos));
        PTdown(2*i-1,:)=[min(xp),0];
        PTdown(2*i,:)=[max(xp),0];
    end
    xtmp=PTdown(:,1);
    xtmp=sort(xtmp,'descend');
    PTdown=[xtmp,PTdown(:,2)];
    xtmp=xtmp(1:2:size(xtmp,1)-1);
    [TMP,PD_INDEX]=sort(xtmp);
    pn=cell(1,1);
    for m=1:k3
        pn{1,m}=Pdown{1,PD_INDEX(m)};
    end
    Pdown=pn;
end
%UP Boundary
if k4 ~=0
    PTup=zeros(2*k4,2);
    for i=1:k4
        tmp=Pup{1,i};
        x=tmp(:,1); y=tmp(:,2);
        pos= (y==Ly);
        xp=(x(pos));
        PTup(2*i-1,:)=[min(xp),Ly];
        PTup(2*i,:)=[max(xp),Ly];
    end
    xtmp=PTup(:,1);
    xtmp=sort(xtmp);
    PTup=[xtmp,PTup(:,2)];
    xtmp=xtmp(1:2:size(xtmp,1)-1);
    [TMP,PU_INDEX]=sort(xtmp);
    for m=1:k4
        pn{1,m}=Pup{1,PU_INDEX(m)};
    end
    Pup=pn;
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% obtain the outline
PB=zeros(10000,2);IN=0;
% Corner 1

if sum(PT1(:))~=0
    IN=IN+1;
    PB(IN,:)=PT1(2,:);
    PB(10000,:)=PT1(1,:);
else
    IN=IN+1;
    PB(IN,:)=[0,0];
    PB(10000,:)=[0,0];
end
% left boundary
if k1~=0
    for k=1:size(PTleft,1)
        IN=IN+1;
        PB(IN,:)=PTleft(k,:);
    end
% else
%     IN=IN+1;
%     PB(IN,:)=[0,0];
%     IN=IN+1;
%     PB(IN,:)=[0,Ly];
end
% Corner 2
if sum(PT2(:))~=0
    IN=IN+1;
    PB(IN,:)=PT2(1,:);
    IN=IN+1;
    PB(IN,:)=PT2(2,:);
else
    IN=IN+1;
    PB(IN,:)=[0,Ly];
    IN=IN+1;
    PB(IN,:)=[0,Ly];
end
% UP boundary
if k4~=0
    for k=1:size(PTup,1)
        IN=IN+1;
        PB(IN,:)=PTup(k,:);
    end
%  else
%     IN=IN+1;
%     PB(IN,:)=[0,Ly];
%     IN=IN+1;
%     PB(IN,:)=[Lx,Ly];
end
% Corner 3
if sum(PT3(:))~=0
    IN=IN+1;
    PB(IN,:)=PT3(1,:);
    IN=IN+1;
    PB(IN,:)=PT3(2,:);
else
    IN=IN+1;
    PB(IN,:)=[Lx,Ly];
    IN=IN+1;
    PB(IN,:)=[Lx,Ly];
end
% right boundary
if k2~=0
    for k=1:size(PTright,1)
        IN=IN+1;
        PB(IN,:)=PTright(k,:);
    end
% else
%     IN=IN+1;
%     PB(IN,:)=[Lx,Ly];
%     IN=IN+1;
%     PB(IN,:)=[Lx,0];
end
% Corner 4
if sum(PT4(:))~=0
    IN=IN+1;
    PB(IN,:)=PT4(1,:);
    IN=IN+1;
    PB(IN,:)=PT4(2,:);
else
    IN=IN+1;
    PB(IN,:)=[Lx,0];
    IN=IN+1;
    PB(IN,:)=[Lx,0];
end
% DOWN boundary
if k3~=0
    for k=1:size(PTdown,1)
        IN=IN+1;
        PB(IN,:)=PTdown(k,:);
    end
% else
%     IN=IN+1;
%     PB(IN,:)=[Lx,0];
%     IN=IN+1;
%     PB(IN,:)=[0,0];
end
PB(IN+1:9999,:)=[];
end

