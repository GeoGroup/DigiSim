function dxf_file_write(P,dxf_file)
% Write into dxf
fid=fopen(dxf_file,'wt+');
write_dxf_head(fid);
for i=1:size(P,2)
    for j=1:P{1,i}
%         tmp=P{j+1,i};
%         plot(tmp(:,1),tmp(:,2),'-o');hold on
        Vert_Polyline=P{j+1,i};
        Vert_Polyline=Vert_Polyline;
        write_dxf_poly_line(fid,Vert_Polyline);
    end
end

% for i=1:length(P)
% Vert_Polyline=P{1,i};
% Vert_Polyline=Vert_Polyline*scale;
% write_dxf_poly_line(fid,Vert_Polyline);
% end
write_dxf_end(fid);


end

