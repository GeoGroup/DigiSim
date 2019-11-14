function mp=boundary_smooth(vert,error)
%
multi_point=vert(1:size(vert,1)-1,:);
%
D=pdist(multi_point);
D=squareform(D);
T=max(D(:));
[row,col]=find(D==T);
%
[P]=sort([row(1),col(1)]);
line{1}=vert(P(1):P(2),:);
line{2}=vert([P(1),P(2)],:);
line2_1=vert(P(2):size(vert,1),:);
line2_2=vert(2:P(1),:);
line{3}=[line2_1;line2_2];
line{4}=vert([P(2),P(1)],:);
% error=1.4;
LM=10;
K=0;
tline{1000}=0;
while LM>error
    K=0;
    LM=0;
    for i=1:length(line)/2
%         i
        a=line{2*i-1};
        b=line{2*i};
        [lj,pos]=dis_cal(a,b);
        if lj>error
            tline{K+1}=a(1:pos,:);
            tline{K+2}=a([1,pos],:);
            tline{K+3}=a(pos:size(a,1),:);
            tline{K+4}=a([pos,size(a,1)],:);        
            K=K+4;
        else
            tline{K+1}=a;
            tline{K+2}=b;
            K=K+2;
        end
        if LM<lj
            LM=lj;
        end
    end    
    line=tline(1,1:K); 
%     disp(LM);
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
mp=zeros(K/2+1,2);
for i=1:K/2
    tmp=tline{i*2-1};
    mp(i,:)=tmp(1,:);
end
mp(i+1,:)=mp(1,:);
end

