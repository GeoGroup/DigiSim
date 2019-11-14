function [boun_line] = sort_boun(pline,pboun)
% sort the line
pboun=pboun';
boun_line=zeros(length(pboun),2);
boun_line(1,1)=pboun(1);boun_line(1,2)=1;
vert2=pline(pboun(1),2);
pboun(1)=[];
for i=2:size(pboun,1)+1
%     disp(i);
  line=pline(pboun,:);
  [row,col]=find(line==vert2);
%   disp(row);
  boun_line(i,1)=pboun(row);
  if line(row,1)==vert2
    boun_line(i,2)=1;
    vert2=line(row,2);
  else
    boun_line(i,2)=-1;
    vert2=line(row,1);
  end
  pboun(row)=[];
end
boun_line=boun_line(:,1).*boun_line(:,2);
end