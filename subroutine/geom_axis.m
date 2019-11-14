function paxis=geom_axis(P)
%calculate the axis information of polygon
% first cell is the bound box with maximum and minimum aixs
% second cell is the length of long axis
% third cell is the length of short axis
% forth cell is the angle of long axis
% fifth cell is the angle of short axis
paxis=cell(size(P,2)-1,5);
for i=1:size(P,2)-1
    p=P{2,i};
    [ b,l,w,alpha,beta] = axis_length_direction( p );
    paxis{i,1}=b;
    paxis{i,2}=l;
    paxis{i,3}=w;
    paxis{i,4}=alpha;
    paxis{i,5}=beta;
end
    
    


end

