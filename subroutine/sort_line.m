function [vert] = sort_line(mline)
%SORT_LINE 根据边界线条生成闭合多段线的点
vert=zeros(size(mline,1)+1,2);
vert(1,1)=mline(1,1);vert(1,2)=mline(1,2);
%把线两端的点分开
P1=mline(:,1:2);P2=mline(:,3:4);k=1;
for i=2:size(mline,1)
    %找到相连的点
    pos_1=panduan_in(P1,vert(i-1,:));
    pos_2=panduan_in(P2,vert(i-1,:));
    vert_maybe=[P2(pos_1,:);P1(pos_2,:)];
    pos=panduan_in(vert,vert_maybe(1,:));
    if isempty(pos)==1
        k=k+1;
        vert(k,:)=vert_maybe(1,:);
    else
        k=k+1;
        vert(k,:)=vert_maybe(2,:);
    end
end
vert(i+1,:)=vert(1,:);
%  取中点 可要可不要
% t1=vert(1:size(mline,1),:);t2=vert(2:size(mline,1)+1,:);
% vert(1:size(mline,1),:)=[(t1(:,1)+t2(:,1))/2,(t1(:,2)+t2(:,2))/2];
% vert(size(mline,1)+1,:)=vert(1,:);
end

