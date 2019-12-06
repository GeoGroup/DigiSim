function [boun_line]=gmsh_write4(Pleft,Pright,Pdown,Pup,P1,P2,P3,P4,Pmain,Pmain2,PB,k1,k2,k3,k4,k5,gmsh_file,lc,lc2)
%write the file into gmsh

fid=fopen(gmsh_file,'wt+');
fprintf(fid,'lc = %10.4f;\n',lc);
fprintf(fid,'lc2 = %10.4f;\n',lc2);
line_remove=[];
point=zeros(10000,2);
pline=zeros(10000,2);
np=0; %number of point
nl=0; % number of line
ns=0; %number of surface
lp=0;
kp=1; %point number index
kl=1;  % line number index
ini_num=0; % initial boundary line number
% write the aggregate in domain
lx=max(PB(:,1));
ly=max(PB(:,2));

RK=zeros(k5,1);
for i=1:k5   
    if Pmain2{1,i}==0
        ptmp=Pmain{1,i};
        for j=1:size(ptmp,1)-1
            np=np+1;
            point(np,:)=ptmp(j,:);
            fprintf(fid,'%s\n',['Point(',num2str(np),')={', ...
                num2str(ptmp(j,1)), ',' , num2str(ptmp(j,2)) ,',', '0,lc};']);
        end
        for j=1:size(ptmp,1)-2
            nl=nl+1;
            pline(nl,:)=[nl,nl+1];
            fprintf(fid,'%s\n',['Line(',num2str(nl),')={', ...
                num2str(nl), ',' , num2str(nl+1) , ' };']);
        end
        nl=nl+1;
        pline(nl,:)=[nl,kp];
        fprintf(fid,'%s\n',['Line(',num2str(nl),')={', ...
            num2str(nl), ',' , num2str(kp) , ' };']);
        kp=np+1;
        lp=lp+1;
        fprintf(fid,'%s',['Line Loop(',num2str(lp),')={' ]);
        for j=kl:nl-1
            fprintf(fid,'%s',[num2str(j),',']);
        end
        fprintf(fid,'%s\n',[num2str(j+1),'};']);
        kl=nl+1;
        %%%%%%%%%%%%%%%%%%%%%%%%%
        fprintf(fid,'%s\n',['Plane Surface(',num2str(lp),')={',num2str(lp),'};' ]);
        RK(i)=lp;
    else
        rk=zeros(1,1);irk=0;
        for ii=1:Pmain2{1,i}
            ptmp=Pmain2{1+ii,i};ptmp=ptmp{1};
            for j=1:size(ptmp,1)-1
                np=np+1;
                point(np,:)=ptmp(j,:);
                fprintf(fid,'%s\n',['Point(',num2str(np),')={', ...
                    num2str(ptmp(j,1)), ',' , num2str(ptmp(j,2)) ,',', '0,lc};']);
            end
            for j=1:size(ptmp,1)-2
                nl=nl+1;
                pline(nl,:)=[nl,nl+1];
                fprintf(fid,'%s\n',['Line(',num2str(nl),')={', ...
                    num2str(nl), ',' , num2str(nl+1) , ' };']);
            end
            nl=nl+1;
            pline(nl,:)=[nl,kp];
            fprintf(fid,'%s\n',['Line(',num2str(nl),')={', ...
                num2str(nl), ',' , num2str(kp) , ' };']);
            kp=np+1;
            lp=lp+1;
            fprintf(fid,'%s',['Line Loop(',num2str(lp),')={' ]);
            for j=kl:nl-1
                fprintf(fid,'%s',[num2str(j),',']);
            end
            fprintf(fid,'%s\n',[num2str(j+1),'};']);
            kl=nl+1;
            %%%%%%%%%%%%%%%%%%%%%%%%%
            fprintf(fid,'%s\n',['Plane Surface(',num2str(lp),')={',num2str(lp),'};' ]);
            irk=irk+1;
            rk(irk)=lp;
        end
        %%%%%%%%%%%%%%%%%%%%%%%%%%%
        %%%%%%%%%%%%%%%%%fprintf(fid,'OK\n');
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        ptmp=Pmain{1,i};
        for j=1:size(ptmp,1)-1
            np=np+1;
            point(np,:)=ptmp(j,:);
            fprintf(fid,'%s\n',['Point(',num2str(np),')={', ...
                num2str(ptmp(j,1)), ',' , num2str(ptmp(j,2)) ,',', '0,lc};']);
        end
        for j=1:size(ptmp,1)-2
            nl=nl+1;
            pline(nl,:)=[nl,nl+1];
            fprintf(fid,'%s\n',['Line(',num2str(nl),')={', ...
                num2str(nl), ',' , num2str(nl+1) , ' };']);
        end
        nl=nl+1;
        pline(nl,:)=[nl,kp];
        fprintf(fid,'%s\n',['Line(',num2str(nl),')={', ...
            num2str(nl), ',' , num2str(kp) , ' };']);
        kp=np+1;
        lp=lp+1;
        fprintf(fid,'%s',['Line Loop(',num2str(lp),')={' ]);
        for j=kl:nl-1
            fprintf(fid,'%s',[num2str(j),',']);
        end
        fprintf(fid,'%s\n',[num2str(j+1),'};']);
        kl=nl+1;
        %%%%%%%%%%%%%%%%%%%%%%%%%
        fprintf(fid,'%s',['Plane Surface(',num2str(lp),')={',num2str(lp)]);
        for ii=1:irk
            fprintf(fid,'%s',[',', num2str(rk(ii))]);
        end
        fprintf(fid,'%s\n','};');
        RK(i)=lp;
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    end
end
%%%%%%%%%%%%%%fclose(fid);
ini_num=nl;
% disp(ini_num);
fprintf(fid,'%s\n','/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////');
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% write boundary polylines
% Corner  poly 1
if  isempty(P1{1}) ~= 1
    ptmp=P1{1};
    for j=1:size(ptmp,1)-1
        np=np+1;
        point(np,:)=ptmp(j,:);
        fprintf(fid,'%s\n',['Point(',num2str(np),')={', ...
            num2str(ptmp(j,1)), ',' , num2str(ptmp(j,2)) ,',', '0,lc};']);
    end
    for j=1:size(ptmp,1)-2
        nl=nl+1;
        %%%%%%%%%%%%%   judge the boundary line      %%%%%%%%%%%
        line=[ptmp(j,1),ptmp(j,2),ptmp(j+1,1),ptmp(j+1,2)];
        bou_judge = judge_bou2( line,lx,ly );
        if bou_judge==1
            line_remove=[line_remove,nl];
        end
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        pline(nl,:)=[nl,nl+1];
        fprintf(fid,'%s\n',['Line(',num2str(nl),')={', ...
            num2str(nl), ',' , num2str(nl+1) , ' };']);
    end
    nl=nl+1;
    
    %%%%%%%%%%%%%   judge the boundary line      %%%%%%%%%%%
    line=[ptmp(j+1,1),ptmp(j+1,2),ptmp(1,1),ptmp(1,2)];
    bou_judge = judge_bou2( line,lx,ly );
    if bou_judge==1
        line_remove=[line_remove,nl];
    end
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    pline(nl,:)=[nl,kp];
    fprintf(fid,'%s\n',['Line(',num2str(nl),')={', ...
        num2str(nl), ',' , num2str(kp) , ' };']);
    kp=np+1;
    lp=lp+1;
    fprintf(fid,'%s',['Line Loop(',num2str(lp),')={' ]);
    for j=kl:nl-1
        fprintf(fid,'%s',[num2str(j),',']);
    end
    fprintf(fid,'%s\n',[num2str(j+1),'};']);
    kl=nl+1;
    fprintf(fid,'%s\n',['Plane Surface(',num2str(lp),')={',num2str(lp),'};' ]);
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%left boundary
if k1 ~= 0
    for i=1:k1
        ptmp=Pleft{1,i};
        for j=1:size(ptmp,1)-1
            np=np+1;
            point(np,:)=ptmp(j,:);
            fprintf(fid,'%s\n',['Point(',num2str(np),')={', ...
                num2str(ptmp(j,1)), ',' , num2str(ptmp(j,2)) ,',', '0,lc};']);
        end
        for j=1:size(ptmp,1)-2
            nl=nl+1;
            %%%%%%%%%%%%%   judge the boundary line      %%%%%%%%%%%
            line=[ptmp(j,1),ptmp(j,2),ptmp(j+1,1),ptmp(j+1,2)];
            bou_judge = judge_bou2( line,lx,ly );
            if bou_judge==1
                line_remove=[line_remove,nl];
            end
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            pline(nl,:)=[nl,nl+1];
            fprintf(fid,'%s\n',['Line(',num2str(nl),')={', ...
                num2str(nl), ',' , num2str(nl+1) , ' };']);
        end
        nl=nl+1;
        %%%%%%%%%%%%%   judge the boundary line      %%%%%%%%%%%
        line=[ptmp(j+1,1),ptmp(j+1,2),ptmp(1,1),ptmp(1,2)];
        bou_judge = judge_bou2( line,lx,ly );
        if bou_judge==1
            line_remove=[line_remove,nl];
        end
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        pline(nl,:)=[nl,kp];
        fprintf(fid,'%s\n',['Line(',num2str(nl),')={', ...
            num2str(nl), ',' , num2str(kp) , ' };']);
        kp=np+1;
        lp=lp+1;
        fprintf(fid,'%s',['Line Loop(',num2str(lp),')={' ]);
        for j=kl:nl-1
            fprintf(fid,'%s',[num2str(j),',']);
        end
        fprintf(fid,'%s\n',[num2str(j+1),'};']);
        kl=nl+1;
        %%%%%%%%%%%%%%%%%%%%%%%%%
        fprintf(fid,'%s\n',['Plane Surface(',num2str(lp),')={',num2str(lp),'};' ]);
    end
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Corner  poly 2
if  isempty(P2{1}) ~= 1
    ptmp=P2{1};
    for j=1:size(ptmp,1)-1
        np=np+1;
        point(np,:)=ptmp(j,:);
        fprintf(fid,'%s\n',['Point(',num2str(np),')={', ...
            num2str(ptmp(j,1)), ',' , num2str(ptmp(j,2)) ,',', '0,lc};']);
    end
    for j=1:size(ptmp,1)-2
        nl=nl+1;
        %%%%%%%%%%%%%   judge the boundary line      %%%%%%%%%%%
        line=[ptmp(j,1),ptmp(j,2),ptmp(j+1,1),ptmp(j+1,2)];
        bou_judge = judge_bou2( line,lx,ly );
        if bou_judge==1
            line_remove=[line_remove,nl];
        end
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        pline(nl,:)=[nl,nl+1];
        fprintf(fid,'%s\n',['Line(',num2str(nl),')={', ...
            num2str(nl), ',' , num2str(nl+1) , ' };']);
    end
    nl=nl+1;    
    %%%%%%%%%%%%%   judge the boundary line      %%%%%%%%%%%
    line=[ptmp(j+1,1),ptmp(j+1,2),ptmp(1,1),ptmp(1,2)];
    bou_judge = judge_bou2( line,lx,ly );
    if bou_judge==1
        line_remove=[line_remove,nl];
    end
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    pline(nl,:)=[nl,kp];
    fprintf(fid,'%s\n',['Line(',num2str(nl),')={', ...
        num2str(nl), ',' , num2str(kp) , ' };']);
    kp=np+1;
    lp=lp+1;
    fprintf(fid,'%s',['Line Loop(',num2str(lp),')={' ]);
    for j=kl:nl-1
        fprintf(fid,'%s',[num2str(j),',']);
    end
    fprintf(fid,'%s\n',[num2str(j+1),'};']);
    kl=nl+1;
    fprintf(fid,'%s\n',['Plane Surface(',num2str(lp),')={',num2str(lp),'};' ]);
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%up boundary
if k4 ~=0
    for i=1:k4
        ptmp=Pup{1,i};
        for j=1:size(ptmp,1)-1
            np=np+1;
            point(np,:)=ptmp(j,:);
            fprintf(fid,'%s\n',['Point(',num2str(np),')={', ...
                num2str(ptmp(j,1)), ',' , num2str(ptmp(j,2)) ,',', '0,lc};']);
        end
        for j=1:size(ptmp,1)-2
            nl=nl+1;
            %%%%%%%%%%%%%   judge the boundary line      %%%%%%%%%%%
            line=[ptmp(j,1),ptmp(j,2),ptmp(j+1,1),ptmp(j+1,2)];
            bou_judge = judge_bou2( line,lx,ly );
            if bou_judge==1
                line_remove=[line_remove,nl];
            end
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            pline(nl,:)=[nl,nl+1];
            fprintf(fid,'%s\n',['Line(',num2str(nl),')={', ...
                num2str(nl), ',' , num2str(nl+1) , ' };']);
        end
        nl=nl+1;
        %%%%%%%%%%%%%   judge the boundary line      %%%%%%%%%%%
        line=[ptmp(j+1,1),ptmp(j+1,2),ptmp(1,1),ptmp(1,2)];
        bou_judge = judge_bou2( line,lx,ly );
        if bou_judge==1
            line_remove=[line_remove,nl];
        end
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        pline(nl,:)=[nl,kp];
        fprintf(fid,'%s\n',['Line(',num2str(nl),')={', ...
            num2str(nl), ',' , num2str(kp) , ' };']);
        kp=np+1;
        lp=lp+1;
        fprintf(fid,'%s',['Line Loop(',num2str(lp),')={' ]);
        for j=kl:nl-1
            fprintf(fid,'%s',[num2str(j),',']);
        end
        fprintf(fid,'%s\n',[num2str(j+1),'};']);
        kl=nl+1;
        %%%%%%%%%%%%%%%%%%%%%%%%%
        fprintf(fid,'%s\n',['Plane Surface(',num2str(lp),')={',num2str(lp),'};' ]);
    end
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Corner  poly 3
if  isempty(P3{1}) ~= 1
    ptmp=P3{1};
    for j=1:size(ptmp,1)-1
        np=np+1;
        point(np,:)=ptmp(j,:);
        fprintf(fid,'%s\n',['Point(',num2str(np),')={', ...
            num2str(ptmp(j,1)), ',' , num2str(ptmp(j,2)) ,',', '0,lc};']);
    end
    for j=1:size(ptmp,1)-2
        nl=nl+1;
        %%%%%%%%%%%%%   judge the boundary line      %%%%%%%%%%%
        line=[ptmp(j,1),ptmp(j,2),ptmp(j+1,1),ptmp(j+1,2)];
        bou_judge = judge_bou2( line,lx,ly );
        if bou_judge==1
            line_remove=[line_remove,nl];
        end
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        pline(nl,:)=[nl,nl+1];
        fprintf(fid,'%s\n',['Line(',num2str(nl),')={', ...
            num2str(nl), ',' , num2str(nl+1) , ' };']);
    end
    nl=nl+1;    
    %%%%%%%%%%%%%   judge the boundary line      %%%%%%%%%%%
    line=[ptmp(j+1,1),ptmp(j+1,2),ptmp(1,1),ptmp(1,2)];
    bou_judge = judge_bou2( line,lx,ly );
    if bou_judge==1
        line_remove=[line_remove,nl];
    end
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    pline(nl,:)=[nl,kp];
    fprintf(fid,'%s\n',['Line(',num2str(nl),')={', ...
        num2str(nl), ',' , num2str(kp) , ' };']);
    kp=np+1;
    lp=lp+1;
    fprintf(fid,'%s',['Line Loop(',num2str(lp),')={' ]);
    for j=kl:nl-1
        fprintf(fid,'%s',[num2str(j),',']);
    end
    fprintf(fid,'%s\n',[num2str(j+1),'};']);
    kl=nl+1;
    fprintf(fid,'%s\n',['Plane Surface(',num2str(lp),')={',num2str(lp),'};' ]);
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%right boundary
if k2 ~=0
    for i=1:k2
        ptmp=Pright{1,i};
        for j=1:size(ptmp,1)-1
            np=np+1;
            point(np,:)=ptmp(j,:);
            fprintf(fid,'%s\n',['Point(',num2str(np),')={', ...
                num2str(ptmp(j,1)), ',' , num2str(ptmp(j,2)) ,',', '0,lc};']);
        end
        for j=1:size(ptmp,1)-2
            nl=nl+1;
            %%%%%%%%%%%%%   judge the boundary line      %%%%%%%%%%%
            line=[ptmp(j,1),ptmp(j,2),ptmp(j+1,1),ptmp(j+1,2)];
            bou_judge = judge_bou2( line,lx,ly );
            if bou_judge==1
                line_remove=[line_remove,nl];
            end
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            pline(nl,:)=[nl,nl+1];
            fprintf(fid,'%s\n',['Line(',num2str(nl),')={', ...
                num2str(nl), ',' , num2str(nl+1) , ' };']);
        end
        nl=nl+1;
        %%%%%%%%%%%%%   judge the boundary line      %%%%%%%%%%%
        line=[ptmp(j+1,1),ptmp(j+1,2),ptmp(1,1),ptmp(1,2)];
        bou_judge = judge_bou2( line,lx,ly );
        if bou_judge==1
            line_remove=[line_remove,nl];
        end
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        pline(nl,:)=[nl,kp];
        fprintf(fid,'%s\n',['Line(',num2str(nl),')={', ...
            num2str(nl), ',' , num2str(kp) , ' };']);
        kp=np+1;
        lp=lp+1;
        fprintf(fid,'%s',['Line Loop(',num2str(lp),')={' ]);
        for j=kl:nl-1
            fprintf(fid,'%s',[num2str(j),',']);
        end
        fprintf(fid,'%s\n',[num2str(j+1),'};']);
        kl=nl+1;
        %%%%%%%%%%%%%%%%%%%%%%%%%
        fprintf(fid,'%s\n',['Plane Surface(',num2str(lp),')={',num2str(lp),'};' ]);
    end
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Corner  poly 4
if  isempty(P4{1}) ~= 1
    ptmp=P4{1};
    for j=1:size(ptmp,1)-1
        np=np+1;
        point(np,:)=ptmp(j,:);
        fprintf(fid,'%s\n',['Point(',num2str(np),')={', ...
            num2str(ptmp(j,1)), ',' , num2str(ptmp(j,2)) ,',', '0,lc};']);
    end
    for j=1:size(ptmp,1)-2
        nl=nl+1;
        %%%%%%%%%%%%%   judge the boundary line      %%%%%%%%%%%
        line=[ptmp(j,1),ptmp(j,2),ptmp(j+1,1),ptmp(j+1,2)];
        bou_judge = judge_bou2( line,lx,ly );
        if bou_judge==1
            line_remove=[line_remove,nl];
        end
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        pline(nl,:)=[nl,nl+1];
        fprintf(fid,'%s\n',['Line(',num2str(nl),')={', ...
            num2str(nl), ',' , num2str(nl+1) , ' };']);
    end
    nl=nl+1;    
    %%%%%%%%%%%%%   judge the boundary line      %%%%%%%%%%%
    line=[ptmp(j+1,1),ptmp(j+1,2),ptmp(1,1),ptmp(1,2)];
    bou_judge = judge_bou2( line,lx,ly );
    if bou_judge==1
        line_remove=[line_remove,nl];
    end
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    pline(nl,:)=[nl,kp];
    fprintf(fid,'%s\n',['Line(',num2str(nl),')={', ...
        num2str(nl), ',' , num2str(kp) , ' };']);
    kp=np+1;
    lp=lp+1;
    fprintf(fid,'%s',['Line Loop(',num2str(lp),')={' ]);
    for j=kl:nl-1
        fprintf(fid,'%s',[num2str(j),',']);
    end
    fprintf(fid,'%s\n',[num2str(j+1),'};']);
    kl=nl+1;
    fprintf(fid,'%s\n',['Plane Surface(',num2str(lp),')={',num2str(lp),'};' ]);
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%down boundary
if k3 ~=0
    for i=1:k3
        ptmp=Pdown{1,i};
        for j=1:size(ptmp,1)-1
            np=np+1;
            point(np,:)=ptmp(j,:);
            fprintf(fid,'%s\n',['Point(',num2str(np),')={', ...
                num2str(ptmp(j,1)), ',' , num2str(ptmp(j,2)) ,',', '0,lc};']);
        end
        for j=1:size(ptmp,1)-2
            nl=nl+1;
            %%%%%%%%%%%%%   judge the boundary line      %%%%%%%%%%%
            line=[ptmp(j,1),ptmp(j,2),ptmp(j+1,1),ptmp(j+1,2)];
            bou_judge = judge_bou2( line,lx,ly );
            if bou_judge==1
                line_remove=[line_remove,nl];
            end
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            pline(nl,:)=[nl,nl+1];
            fprintf(fid,'%s\n',['Line(',num2str(nl),')={', ...
                num2str(nl), ',' , num2str(nl+1) , ' };']);
        end
        nl=nl+1;
        %%%%%%%%%%%%%   judge the boundary line      %%%%%%%%%%%
        line=[ptmp(j+1,1),ptmp(j+1,2),ptmp(1,1),ptmp(1,2)];
        bou_judge = judge_bou2( line,lx,ly );
        if bou_judge==1
            line_remove=[line_remove,nl];
        end
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        pline(nl,:)=[nl,kp];
        fprintf(fid,'%s\n',['Line(',num2str(nl),')={', ...
            num2str(nl), ',' , num2str(kp) , ' };']);
        kp=np+1;
        lp=lp+1;
        fprintf(fid,'%s',['Line Loop(',num2str(lp),')={' ]);
        for j=kl:nl-1
            fprintf(fid,'%s',[num2str(j),',']);
        end
        fprintf(fid,'%s\n',[num2str(j+1),'};']);
        kl=nl+1;
        %%%%%%%%%%%%%%%%%%%%%%%%%
        fprintf(fid,'%s\n',['Plane Surface(',num2str(lp),')={',num2str(lp),'};' ]);
    end
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%% WRITE  BOUNDARY %%%%%%%%%%%%%%%%%%%%%%%%

for i=1:size(PB,1)/2
%     t1=0;   t2=0;
    Ptmp=[PB(2*i-1,1),PB(2*i-1,2)];
%     disp(Ptmp);
    [ pos] = panduan_in(point(1:np,:),Ptmp);    
    if isempty(pos)~=1
        t1=pos;
    else
        np=np+1;
        point(np,:)=Ptmp;
        t1=np;
        fprintf(fid,'%s\n',['Point(',num2str(np),')={', ...
            num2str(Ptmp(1,1)), ',' , num2str(Ptmp(1,2)) ,',', '0,lc2};']);
%         disp( [num2str(np),'   ', num2str(point(np,1)),'    ',num2str(point(np,2))]);
    end     
    Ptmp=[PB(2*i,1),PB(2*i,2)];
%     disp(Ptmp);
    [ pos ] = panduan_in(point(1:np,:),Ptmp); 
    if isempty(pos)~=1
        t2=pos;
    else
        np=np+1;
        point(np,:)=Ptmp;
        t2=np;
        fprintf(fid,'%s\n',['Point(',num2str(np),')={', ...
            num2str(Ptmp(1,1)), ',' , num2str(Ptmp(1,2)) ,',', '0,lc2};']);
%         disp( [num2str(np),'   ', num2str(point(np,1)),'    ',num2str(point(np,2))]);
    end  
    nl=nl+1;
%     disp([num2str(PB(2*i-1,1)),'  ', num2str(PB(2*i-1,2)),' ' , num2str(PB(2*i,1)),'  ',num2str(PB(2*i,2))]);
%     disp([num2str(t1),'    ', num2str(t2)]);
%disp(t1);
%disp(t2);
    pline(nl,:)=[t1;t2];
    fprintf(fid,'%s\n',['Line(',num2str(nl),')={', ...
        num2str(t1), ',' , num2str(t2) , ' };']);
end
pline=pline(1:nl,:);
% disp(line_remove);
%    output
pboun=[];
%     fprintf(fid,'%s',['Line Loop(',num2str(lp+1),')={' ]);
for j=ini_num+1:nl-1
    tmp_judge = find(line_remove==j);
    if  isempty(tmp_judge)==1
        pboun=[pboun,j];
        %             fprintf(fid,'%s',[num2str(j),',']);
    end
end
pboun=[pboun,j+1];
%      fprintf(fid,'%s',[num2str(j+1)]);
%      fprintf(fid,'%s\n','};');

%  for i=1:size(pline,1)
%     tmp=pline(i,:);
%     plot(point(tmp,1),point(tmp,2),'-');hold on;
%     text(mean(point(tmp,1)),mean(point(tmp,2)),num2str(i)) ;
%  end
%  for i=1:length(pboun)
%      tmp=pline(pboun(i),:);
%      plot(point(tmp,1),point(tmp,2),'-');hold on;
%      text(mean(point(tmp,1)),mean(point(tmp,2)),num2str(pboun(i))) ;
%  end

[boun_line] = sort_boun(pline,pboun);
 lp=lp+1;
 fprintf(fid,'%s',['Line Loop(',num2str(lp),')={' ]);
for j=1:size(boun_line,1)-1
     fprintf(fid,'%s',[num2str(boun_line(j)),',']);
end
fprintf(fid,'%s',[num2str(boun_line(j+1))]);
fprintf(fid,'%s\n','};');
fprintf(fid,'%s',['Plane Surface(',num2str(lp),')={',num2str(lp)]);
for i=1:k5
    fprintf(fid,'%s',[',', num2str(RK(i))]);
end
fprintf(fid,'%s\n','};');


fclose(fid);

% point=point(1:np,:);
% pline=pline(1:nl,:);

end

