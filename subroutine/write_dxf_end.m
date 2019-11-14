function write_dxf_end(fid)
fprintf(fid,'  0\n');fprintf(fid,'ENDSEC\n');
fprintf(fid,'  0\n');fprintf(fid,'EOF\n');
fclose(fid);
end

