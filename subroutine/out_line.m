function [ P ] = out_line( LINE_OUT,num )
%UNTITLED Summary of this function goes here
global L;
error=2;
P=cell(1,size(LINE_OUT,2));
for I = 1: num
  tmp=LINE_OUT{1,I};
  if size(tmp,2)~=0  %%%%%%%%
  x=tmp(:,1);
  y=size(L,1)-tmp(:,2);
  for i=1:size(x,1)    if abs(x(i)-0)<=error
      x(i)=0;
    elseif abs(x(i)-size(L,2))<=error
      x(i)=size(L,2);
    end
  end
  for i=1:size(y,1)
    if abs(y(i)-0)<=error
      y(i)=0;
    elseif abs(y(i)-size(L,1))<=error
      y(i)=size(L,1);
    end
  end
  plot(x,y);
  P{I}=[x,y];
  text(mean(x(:)),mean(y(:)),num2str(I)) ;
  hold on
  else 
      break;  %%%%%%%
  end    %%%%%%%%
end

end

