function geom_stas(geo_file,parea,fraction,mg,P)
% output the geometry information to xls file
filename =geo_file;
% filename = 'testdata.xlsx';
%area, length, width, alpha, beta
MS=cell(5,size(P,2)-1);
MS{1,1}='area';
MS{1,2}='length';
MS{1,3}='width';
MS{1,4}='alpha';
MS{1,5}='isboundary';
for i=2:size(P,2)
    MS{i,1}=parea(i-1);
    MS{i,2}=mg{i-1,2};
    MS{i,3}=mg{i-1,3};
    MS{i,4}=mg{i-1,4};
    MS{i,5}=mg{i-1,6};
end
% A = {'Time','Temperature'; 12,98; 13,99; 14,97};
sheet = 'Sheet1';
xlRange = 'A1';
xlswrite(filename,MS,sheet,xlRange)
F={'Fraction(%)';fraction*100};
xlswrite(filename,F,sheet,'F1');
% minimum boundary rectangle

end