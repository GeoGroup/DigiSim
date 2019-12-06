function [azimuth,elevation,r] = cart_sph(PT,pcenter)
% Translate cart to sphere
[azimuth,elevation,r]=cart2sph(PT(:,1)-pcenter(1),PT(:,2)-pcenter(2),PT(:,3)-pcenter(3));
end

