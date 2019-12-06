function [ P] = vectorization2(x1,error)%,frac
% vectorization
% x1=imread('2000-4.jpg');

err=error;
% frac=sum(x1(:))/size(x1,1)/size(x1,2);
% sscale=2.5;
% x1= imresize(x1,[round(size(x1,1)/sscale),round(size(x1,2)/sscale)]);
% imwrite(x1,'J14aa.bmp');
% pause;
% global L;
[L, num]=bwlabel(x1,4);

% disp(['Particle Fraction is ', num2str(frac)]);
disp(['Particle Number is ', num2str(num)]);
RS=zeros(1,num);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
LINE_OUT=cell(10,num);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Total_Line=zeros(1000000,4);K1=1;K2=1;
% fid=fopen('2000-23.dxf','wt+');
% write_dxf_head(fid);
for I=1:num
    if mod(I,10)==0
        disp(['Num ',num2str(I),' / ',num2str(num)]);
    end
    T=L;
    T(T~=I)=255;T(T==I)=0;
    % image(T)
    [r,c]=find(T==0);
    alength=size(r,1);    Line=ones(alength*4,4);
    RS(1,I)=alength;
    for i=1:alength
        %LINE 1
        Line(4*(i-1)+1,2)=r(i)-1;Line(4*(i-1)+1,1)=c(i)-1;        Line(4*(i-1)+1,4)=r(i)-1;Line(4*(i-1)+1,3)=c(i)+1-1;
        %LINE 2
        Line(4*(i-1)+2,2)=r(i)-1;Line(4*(i-1)+2,1)=c(i)+1-1;        Line(4*(i-1)+2,4)=r(i)+1-1;Line(4*(i-1)+2,3)=c(i)+1-1;
        %LINE 3
        Line(4*(i-1)+3,2)=r(i)+1-1;Line(4*(i-1)+3,1)=c(i)-1;        Line(4*(i-1)+3,4)=r(i)+1-1;Line(4*(i-1)+3,3)=c(i)+1-1;
        %LINE 4
        Line(4*(i-1)+4,2)=r(i)-1;Line(4*(i-1)+4,1)=c(i)-1;        Line(4*(i-1)+4,4)=r(i)+1-1;Line(4*(i-1)+4,3)=c(i)-1;    
    end
    [C,IA,IC]=unique(Line,'rows');
    index=1:1:alength*4;
    irep=setdiff(index,IA);
    tirep=Line(irep,:);
    [c]=setdiff(C,tirep,'rows');
    [C,ia,ib] = intersect(Line,c,'rows');
    FLine=Line(ia,:);
%     k=4;
%     for i=2:alength
%         tmp=zeros(4,4);
%         tmp(1,1:4)=[c(i)-1,r(i)-1,c(i)+1-1,r(i)-1];        tmp(2,1:4)=[c(i)+1-1,r(i)-1,c(i)+1-1,r(i)+1-1];
%         tmp(3,1:4)=[c(i)-1,r(i)+1-1,c(i)+1-1,r(i)+1-1];        tmp(4,1:4)=[c(i)-1,r(i)-1,c(i)-1,r(i)+1-1];
%         for j=1:4
%             t=tmp(j,:);
%             pos=panduan_in(Line,t);
%             if isempty(pos)==1
%                 k=k+1; 
%                 Line(k,:)=t;
%             else
%                 k=k-1;
%                 Line(pos,:)=[];
%             end
%         end
%         %         disp(i);
%     end
%     FLine=Line(1:k,:);
    
%         Vert_Polyline=sort_line(FLine);
    Vert_Polyline=sort_line_mod2(FLine,error);
    LINE_OUT{1,I}=length(Vert_Polyline);
    for ii=1:length(Vert_Polyline)
        tmp=Vert_Polyline{ii};
%         LINE_OUT{1+i,I}=tmp;
%         plot(tmp(:,1),size(L,1)-tmp(:,2),'-o');hold on
        
        if size(tmp,2)~=0  %%%%%%%%
            x=tmp(:,1);
            y=size(L,1)-tmp(:,2);
            for i=1:size(x,1)
                if abs(x(i)-0)<=err
                    x(i)=0;
                elseif abs(x(i)-size(L,2))<=err
                    x(i)=size(L,2);
                end
            end
            for i=1:size(y,1)
                if abs(y(i)-0)<=err
                    y(i)=0;
                elseif abs(y(i)-size(L,1))<=err
                    y(i)=size(L,1);
                end
            end
%             plot(x,y); hold on
            LINE_OUT{1+ii,I}=[x,y];
%             PT{J}=[x,y];%size(L,1)-
            %   text(mean(x(:)),mean(y(:)),num2str(I)) ;
            %   hold on
        else
            break;  %%%%%%%
        end    %%%%%%%%        
    end
end
%     LINE_OUT{1,I}=Vert_Polyline;
%     write_dxf_poly_line(fid,Vert_Polyline)
%     disp(I);

% BJ=[0 0  0 size(L,1);
%     0 size(L,1)  size(L,2) size(L,1) ;
%     size(L,2) size(L,1) size(L,2) 0 ;
%     size(L,2) 0  0 0];
% write_dxf_sline(fid,BJ)
% write_dxf_end(fid);
vert_bou=[0 0;0 size(L,1);size(L,2) size(L,1) ;size(L,2) 0;0 0];
% x=vert_bou(:,1);y=vert_bou(:,2);
% plot(x,y); hold on
LINE_OUT{1,I+1}=1;
LINE_OUT{2,I+1}=vert_bou;
% num=num+1;
P=LINE_OUT;
for i=1:size(LINE_OUT,2)
    sarea=zeros(1,LINE_OUT{1,i});
    for j=1:LINE_OUT{1,i}
%         tmp=P{j+1,i};
%         plot(tmp(:,1),tmp(:,2),'-o');hold on
        tmp=LINE_OUT{j+1,i};
        sarea(j)=polyarea(tmp(:,1),tmp(:,2));
    end
    pos=find(sarea==max(sarea));
    LINE_OUT{2,i}=LINE_OUT{1+pos,i};
    kk=0;
    for k=1:pos-1
        kk=kk+1;
        P{2+kk,i}=LINE_OUT{1+k,i};
    end
    for k=pos+1:LINE_OUT{1,i}
        kk=kk+1;
        P{2+kk,i}=LINE_OUT{1+k,i};
    end
        
end


% P=LINE_OUT;
end
