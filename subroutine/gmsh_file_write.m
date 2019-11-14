function gmsh_file_write(P,gmsh_file,lc,lc2)
% Write polygon information to gmsh file
[Pleft,Pright,Pdown,Pup,P1,P2,P3,P4,Pmain,Pmain2,PB,k1,k2,k3,k4,k5]  = classify_poly5( P );
gmsh_write4(Pleft,Pright,Pdown,Pup,P1,P2,P3,P4,Pmain,Pmain2,PB,k1,k2,k3,k4,k5,gmsh_file,lc,lc2);
end

