function write_abaqus_2d_refinement(fpy,Polygon,thick)
% to abaqus python
% if nargin==2
    edge_center=zeros(100000,2);en=0;
    fid=fopen(fpy,'wt');
    fprintf(fid,'from abaqus import *\n');
    fprintf(fid,'from abaqusConstants import *\n');
    % Generate the rectangle
    
    tmp=Polygon{2,size(Polygon,2)};
    lmax=max(tmp);
    fprintf(fid,'s = mdb.models[''Model-1''].ConstrainedSketch(name=''__profile__'', sheetSize=10.0)\n');
    fprintf(fid,'s.rectangle(point1=(%f, %f), point2=(%f, %f))\n',0,0,lmax(1),lmax(2));
    fprintf(fid,'p = mdb.models[''Model-1''].Part(name=''Part-1'',dimensionality=TWO_D_PLANAR,type=DEFORMABLE_BODY) \n');
    fprintf(fid,'p.BaseShell(sketch=s)\n');
%     % Generate particle
%     fprintf(fid,'s0 = mdb.models[''Model-1''].ConstrainedSketch(name=''__profile__'',sheetSize=200.0)\n');
%     fprintf(fid,'g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints\n');
    
for i=1:size(Polygon,2)-1
    if mod(i,20)==0
        fprintf(fid,'print %d\n',i);
    end
    fprintf(fid,'s0 = mdb.models[''Model-1''].ConstrainedSketch(name=''__profile__'',sheetSize=200.0)\n');
    fprintf(fid,'g, v, d, c = s0.geometry, s0.vertices, s0.dimensions, s0.constraints\n');
    
    for j=1:Polygon{1,i}
        points=Polygon{1+j,i};
        x=points(:,1);y=points(:,2);
        for jj=1:length(x)-1
            fprintf(fid,'s0.Line(point1=(%f, %f), point2=(%f, %f))\n',x(jj),y(jj),x(jj+1),y(jj+1));
            en=en+1;
            edge_center(en,:)=[(x(jj)+x(jj+1))/2,(y(jj)+y(jj+1))/2];
        end
    end
    for j=1:Polygon{1,i}
        points=Polygon{1+j,i};
        points(size(points,1),:)=[];
        pin=addthick(points,-thick);
        pin(size(pin,1)+1,:)=pin(1,:);
        x=pin(:,1);y=pin(:,2);
        [x,y] = boundary_close(x,y,Polygon,2*thick);
        for jj=1:length(x)-1
            fprintf(fid,'s0.Line(point1=(%f, %f), point2=(%f, %f))\n',x(jj),y(jj),x(jj+1),y(jj+1));
        end
        pin2=addthick(points,thick);
        pin2(size(pin2,1)+1,:)=pin2(1,:);
        x=pin2(:,1);y=pin2(:,2);
        [x,y] = boundary_close(x,y,Polygon,2*thick);
        for jj=1:length(x)-1
            fprintf(fid,'s0.Line(point1=(%f, %f), point2=(%f, %f))\n',x(jj),y(jj),x(jj+1),y(jj+1));
        end
    end
    
    fprintf(fid,'p = mdb.models[''Model-1''].parts[''Part-1'']\n');
    fprintf(fid,'f = p.faces\n');
    fprintf(fid,'pickedFaces =f\n');
    fprintf(fid,'p.PartitionFaceBySketch(faces=pickedFaces, sketch=s0)\n');
    
end
fprintf(fid,'print ''ok''\n');

fprintf(fid,'p = mdb.models[''Model-1''].parts[''Part-1'']\n');

fprintf(fid,'e=p.edges\n');
fprintf(fid,'e0=e[0:0]\n');
for i=1:en
    fprintf(fid,'e = p.edges.findAt(\n');
    fprintf(fid,'((%f, %f,0),),\n',edge_center(i,1),edge_center(i,2));
    fprintf(fid,')\n');
    fprintf(fid,'e0=e0+e[0:1]\n');
end
fprintf(fid,'p.Set(name = ''Edge_origin'' , edges=e0[0:len(e0)])\n');

% ·Ö×é particlenum+1
    fprintf(fid,'f2=mdb.models[''Model-1''].parts[''Part-1''].faces\n');
    fprintf(fid,'for i in range(len(f2)):\n');
    fprintf(fid,'  mdb.models[''Model-1''].parts[''Part-1''].Set(name = ''Set''+str(i) , faces=f2[i:i+1])\n');
fprintf(fid,'print ''Finish''\n');
    fclose(fid);


end

