function write_dxf_poly_line(fid,vert)
global L;
%WRITE_DXF_POLY_LINE  把结果写入dxf文件
        fprintf(fid,'  0\n');fprintf(fid,'POLYLINE\n');
        fprintf(fid,'  8\n');fprintf(fid,'2\n');
        fprintf(fid,'  62\n');fprintf(fid,'0\n');
        fprintf(fid,'  66\n');fprintf(fid,'1\n');
%         fprintf(fid,'  10\n');fprintf(fid,'    %f\n',vert(1,1)); 
%         fprintf(fid,'  20\n');fprintf(fid,'    %f\n',vert(1,2)); 
%         fprintf(fid,'  30\n');fprintf(fid,'    %f\n',0);
        for i=1:size(vert,1)-1
            fprintf(fid,'  0\n');fprintf(fid,'VERTEX\n');
            fprintf(fid,'  8\n');fprintf(fid,'2\n');
            fprintf(fid,'  62\n');fprintf(fid,'0\n');
            fprintf(fid,'  10\n');fprintf(fid,'    %f\n',vert(i,1)); 
            fprintf(fid,'  20\n');fprintf(fid,'    %f\n',vert(i,2)); 
            fprintf(fid,'  30\n');fprintf(fid,'    %f\n',0); 
        end
        fprintf(fid,'  0\n');fprintf(fid,'VERTEX\n');
        fprintf(fid,'  8\n');fprintf(fid,'2\n');
        fprintf(fid,'  62\n');fprintf(fid,'0\n');
        fprintf(fid,'  10\n');fprintf(fid,'    %f\n',vert(i+1,1)); 
        fprintf(fid,'  20\n');fprintf(fid,'    %f\n',vert(i+1,2)); 
        fprintf(fid,'  30\n');fprintf(fid,'    %f\n',0);
        fprintf(fid,'  0\n');fprintf(fid,'SEQEND\n');
end

