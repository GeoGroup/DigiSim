function [vert] = sort_line_mod2(mline,error)
%SORT_LINE ?
P1=mline(:,1:2);P2=mline(:,3:4);
PV=[P1;P2];
PV = unique(PV,'rows');
PL=PV;lline=mline;
t=size(PL,1);
pvert=cell(10,1);mp=pvert;np=0;
% while isempty(PL)
while ~isempty(lline)
np=np+1;
vert(1,1)=lline(1,1);vert(1,2)=lline(1,2);
vert2=[lline(1,3),lline(1,4)];
% lline=setdiff(lline,lline(1,:),'rows');
lline(1,:)=[];
k=1; ij=1;
while ij==1
    P1=lline(:,1:2);P2=lline(:,3:4);
    %找到相连的点
    pos_1=panduan_in(P1,vert(k,:));
    pos_2=panduan_in(P2,vert(k,:));
    if isempty(pos_1)
        if ~isempty(pos_2)
            k=k+1;
            vert(k,:)=P1(pos_2,:);
            lline(pos_2,:)=[];
            %lline=setdiff(lline,lline(pos_2,:),'rows');
        end
    else
        k=k+1;
        vert(k,:)=P2(pos_1,:);
        lline(pos_1,:)=[];
        %lline=setdiff(lline,lline(pos_1,:),'rows');
    end
    if vert(k,:)==vert2
        k=k+1;
        vert(k,:)=vert(1,:);
%         lline=setdiff(lline,lline(1,:),'rows');
        ij=0;
    end
end
% plot(vert(1:k,1),vert(1:k,2),'-o'); hold on
pvert{np}=vert(1:k,:);
mp{np}=boundary_smooth(pvert{np},error);
end

vert=mp(1:np);
end

