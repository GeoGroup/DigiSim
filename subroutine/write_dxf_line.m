function write_dxf_line(line)
%WRITE_DXF_LINE  把结果写入dxf文件
%     fid=fopen('line.dxf','wt');
%     fprintf(fid,'  0\n');fprintf(fid,'SECTION\n');
%     fprintf(fid,'  2\n');fprintf(fid,'ENTITIES\n');
    for i=1:size(line)
        fprintf(fid,'  0\n');fprintf(fid,'LINE\n');
        fprintf(fid,'  8\n');fprintf(fid,'2\n');
        fprintf(fid,'  62\n');fprintf(fid,'0\n');
        %第一个点
        fprintf(fid,'  10\n');fprintf(fid,'    %f\n',line(i,1)); 
        fprintf(fid,'  20\n');fprintf(fid,'    %f\n',line(i,2)); 
        fprintf(fid,'  30\n');fprintf(fid,'    %f\n',0); 
        %第二个点
        fprintf(fid,'  11\n');fprintf(fid,'    %f\n',line(i,3)); 
        fprintf(fid,'  21\n');fprintf(fid,'    %f\n',line(i,4)); 
        fprintf(fid,'  31\n');fprintf(fid,'    %f\n',0); 
    end
    fprintf(fid,'  0\n');fprintf(fid,'ENDSEC\n');
    fprintf(fid,'  0\n');fprintf(fid,'EOF\n');
    fclose(fid);
end

