function particle = merge_surf(particle)
%   merge the surfces in a plane into a surf
K=particle.conn;
PT=particle.vert;
% trisurf(K,PT(:,1),PT(:,2),PT(:,3)); hold on
direct=zeros(size(K));
for i=1:size(K,1)
    tmp=K(i,:);
    p=PT(tmp,:);
    vect=cross(p(2,:)-p(1,:),p(3,:)-p(1,:));
    direct(i,:)=round(vect/norm(vect)*1000)/1000;
end
[dir,ia,ib]=unique(direct,'rows');
n=length(ia);
ar=cell(length(ia),1);
K2=cell(length(ia),1);
for i=1:n
    tmp=find(ib==i);
    ar{i}=tmp;
    if length(tmp)==1
        K2{i}=K(tmp,:);
    else
        edges=zeros(length(tmp)*3,2);
        for j=1:length(tmp)
            edges(3*(j-1)+1,:)=[K(tmp(j),1),K(tmp(j),2)];
            edges(3*(j-1)+2,:)=[K(tmp(j),2),K(tmp(j),3)];
            edges(3*(j-1)+3,:)=[K(tmp(j),3),K(tmp(j),1)];
        end
        edges=sort(edges,2);
        [C,IA,IC]=unique(edges,'rows');
        index=1:1:length(tmp)*3;
        irep=setdiff(index,IA);
        tirep=edges(irep,:);
        [c]=setdiff(C,tirep,'rows');
        [C,iaa,ibb] = intersect(edges,c,'rows');
        mline=edges(iaa,:);
        [vert] = sort_line(mline);vert(length(vert))=[];
        K2{i}=vert';
    end
end
particle.poly=K2;
end


