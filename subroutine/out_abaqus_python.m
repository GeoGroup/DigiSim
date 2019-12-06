function out_abaqus_python( Particle,V,fpy )
% Write the polyhedron and domain inro pythonscript
% fpy='testpoly.py';
% Particle=particle;
[domain_size,domain_size2,domain_size3]=size(V);
fid=fopen(fpy,'wt');
fprintf(fid,'#***************************************************\n');
fprintf(fid,'#**              Written By MQX                   **\n');
fprintf(fid,'#**               Hohai University                **\n');
fprintf(fid,'#**           %s                     **\n',datestr(now));
fprintf(fid,'#***************************************************\n');
fprintf(fid,'from abaqus import *\n');
fprintf(fid,'from abaqusConstants import *\n');
%fprintf(fid,'session.Viewport(name=''Viewport: 1'', origin=(0.0, 0.0), width=187.938018798828, \n');
%fprintf(fid,'    height=229.658340454102)\n');
fprintf(fid,'session.viewports[''Viewport: 1''].makeCurrent()\n');
fprintf(fid,'session.viewports[''Viewport: 1''].maximize()\n');
fprintf(fid,'from caeModules import *\n');
fprintf(fid,'from driverUtils import executeOnCaeStartup\n');
fprintf(fid,'executeOnCaeStartup()\n');
%fprintf(fid,'session.viewports[''Viewport: 1''].partDisplay.geometryOptions.setValues(\n');
%fprintf(fid,'    referenceRepresentation=ON)\n');
fprintf(fid,'Mdb()\n');
fprintf(fid,'session.viewports[''Viewport: 1''].setValues(displayedObject=None)\n');
fprintf(fid,'p = mdb.models[''Model-1''].Part(name=''Part-%d'', dimensionality=THREE_D, \n',1);
fprintf(fid,'    type=DEFORMABLE_BODY)\n');
fprintf(fid,'p = mdb.models[''Model-1''].parts[''Part-%d'']\n',1);
for i=1:length(Particle)
    tp=Particle{i}.vert;
    tc=Particle{i}.poly;
    tpc=zeros(length(tc),3);
    for j=1:length(tc)
        tv=tc{j};
        tpc(j,:)=sum(tp(tv,:))/length(tv);
        tv(length(tv)+1)=tv(1);tlc=zeros(3,3);
        for k=1:length(tv)-1
            tpos1=tp(tv(k),:);
            tpos2=tp(tv(k+1),:);
            tlc(k,:)=(tpos1+tpos2)/2;
            fprintf(fid,'p.WirePolyLine(points=(((%f, %f, %f), (%f, %f, %f)), ), mergeType=IMPRINT)\n',tpos1(1),tpos1(2),tpos1(3),tpos2(1),tpos2(2),tpos2(3));
        end
        fprintf(fid,'e = p.edges\n');
        fprintf(fid,'e1 = e.findAt(\n');
        for k=1:length(tv)-1
            fprintf(fid,'((%f, %f, %f),),\n',tlc(k,1),tlc(k,2),tlc(k,3));
%             fprintf(fid,'((%f, %f, %f),),\n',tlc(2,1),tlc(2,2),tlc(2,3));
%             fprintf(fid,'((%f, %f, %f),),\n',tlc(3,1),tlc(3,2),tlc(3,3));
        end
        fprintf(fid,')\n');
%         p.CoverEdges(edgeList = e1, tryAnalytical=True)
%         for k=1:3            
%             fprintf(fid,'e%d = e.findAt(((%f, %f, %f), )) \n',k,tlc(k,1),tlc(k,2),tlc(k,3));
%         end
        fprintf(fid,'p.CoverEdges(edgeList = e1, tryAnalytical=True)\n');
    end
end
%     fprintf(fid,'f = p.faces\n');
%% Write the domain

    fprintf(fid,'s = mdb.models[''Model-1''].ConstrainedSketch(name=''__profile__'', \n');
    fprintf(fid,'    sheetSize=200.0)\n');
    fprintf(fid,'g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints\n');
    fprintf(fid,'s.setPrimaryObject(option=STANDALONE)\n');
    fprintf(fid,'s.rectangle(point1=(%f, %f), point2=(%f, %f))\n',0,0,domain_size,domain_size2);
    fprintf(fid,'p = mdb.models[''Model-1''].Part(name=''Part-%d'', dimensionality=THREE_D, \n',2);
    fprintf(fid,'    type=DEFORMABLE_BODY)\n');
    fprintf(fid,'p = mdb.models[''Model-1''].parts[''Part-%d'']\n',2);
    fprintf(fid,'p.BaseSolidExtrude(sketch=s, depth=%f)\n',domain_size3);


 %% Assembly the model
fprintf(fid,'a = mdb.models[''Model-1''].rootAssembly\n');
for i=1:2
    fprintf(fid,'p = mdb.models[''Model-1''].parts[''Part-%d'']\n',i);
    fprintf(fid,'a.Instance(name=''Part-%d-1'', part=p, dependent=ON)\n',i);
end

fprintf(fid,'a = mdb.models[''Model-1''].rootAssembly\n');
fprintf(fid,'a.InstanceFromBooleanMerge(name=''Part-%d'', instances=(\n',3);
for i=1:2
    fprintf(fid,'    a.instances[''Part-%d-1''],\n',i);
end
fprintf(fid,'    ), keepIntersections=ON,originalInstances=DELETE, domain=GEOMETRY)\n');
% ins=mdb.models['Model-1'].rootAssembly.allinstances
fprintf(fid,'v=mdb.models[''Model-1''].rootAssembly.instances[''Part-%d-1''].cells\n',3);
fprintf(fid,'for i in range(len(v)):\n');
fprintf(fid,'  mdb.models[''Model-1''].rootAssembly.Set(name = ''Set''+str(i+1) , cells=v[i:i+1])\n');

fclose(fid);
end