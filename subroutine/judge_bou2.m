function bou_judge = judge_bou2( line,lx,ly )
% judge whether a line is boundary line
% global L;
% lx=max(PB(:,1));
% ly=max(PB(:,2));
bou_judge=0;
if line(1)==line(3)
    if line(1)==lx || line(1)==0
        bou_judge=1;
    end
elseif    line(2)==line(4)
    if line(2) ==ly || line(2)==0
        bou_judge=1;
    end
end
end

