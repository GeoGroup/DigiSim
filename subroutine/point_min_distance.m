function points = point_min_distance(N,distance)
% points with minimum distance
x = rand(1, 100000);
y = rand(1, 100000);
minAllowableDistance = distance; %0.05
numberOfPoints = N;
% Initialize first point.
keeperX = x(1);
keeperY = y(1);
% Try dropping down more points.
counter = 2;
for k = 2 : numberOfPoints
  % Get a trial point.
  thisX = x(k);
  thisY = y(k);
  % See how far is is away from existing keeper points.
  distances = sqrt((thisX-keeperX).^2 + (thisY - keeperY).^2);
  minDistance = min(distances);
  if minDistance >= minAllowableDistance
    keeperX(counter) = thisX;
    keeperY(counter) = thisY;
    counter = counter + 1;
  end
end
% plot(keeperX, keeperY, 'b*');grid on;
points=[keeperX',keeperY'];
end

