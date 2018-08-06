function f = WhiteBalance()
% % I=imread(path);
% % y=GrayWorld(I);
% % figure(1);imshow(I);
% % figure(2);imshow(y);
% imwrite(y,'./WB_result/new5.jpg')
Files = dir(strcat('C:\Users\Thomas\Desktop\8.5\\','*.jpg'));
LengthFiles = length(Files);
for i = 1:LengthFiles;
    img = imread(strcat('C:\Users\Thomas\Desktop\8.5\',num2str(i),'.jpg'));
    y=GrayWorld(img);
    imwrite(y,strcat('C:\Users\Thomas\Desktop\WB_result\',num2str(i),'.jpg'));
end
function y=GrayWorld(Image)
r=Image(:,:,1);
g=Image(:,:,2);
b=Image(:,:,3);
avgR = mean(mean(r));
avgG = mean(mean(g));
avgB = mean(mean(b));
avgRGB = [avgR avgG avgB];
grayValue = (avgR + avgG + avgB)/3
scaleValue = grayValue./avgRGB;
newI(:,:,1) = scaleValue(1) * r;
newI(:,:,2) = scaleValue(2) * g;
newI(:,:,3) = scaleValue(3) * b;
y=newI;