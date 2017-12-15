clc;
clearvars;
close all;
allcentroids=zeros(1000,2,1000);
centroids=zeros(1000,2);
count=0;
x=0;
c=1;
n=1;
plotcount=1;
objcount=0;
bbox=zeros(1,4);
cent1=0;
cent2=0;
c1last=0;
c2last=0;
diffc1=0;
diffc2=0;
bcent1=0;
bcent2=0;
cam=webcam(1);
cam.Resolution='320x240';
%cam.WhiteBalance=5000;
cam.Hue=-40;
cam.Saturation=60;
while(1)
    pic=snapshot(cam);
    count=0;
    objcount=0;
if (c==0)
    n=n+1;
end
c=c+1;
allcentroids(:,:,n)=centroids;

for row = 1 : size(pic, 1)
  for col = 1 : size(pic, 2)
    if (pic(row,col,3) > (pic(row,col,1)+10) && pic(row,col,3) > (pic(row,col,2)+10) && pic(row,col,3) > 30 && pic(row,col,2) < 190 && pic(row,col,1) < 190  && pic(row,col,1) > 10 && pic(row,col,2) > 10)
        pic(row,col,1)=0;
        pic(row,col,2)=0;
        pic(row,col,3)=255;
        plotcount=0;
        %count=count+1;
    else
        %pic(row,col,1)=0;
        %pic(row,col,2)=0;
        pic(row,col,3)=0;
    end
  end
end

img=imsubtract(pic(:,:,3),rgb2gray(pic));
img=medfilt2(img,[3,3]);
img=im2bw(img,0.13);
img=bwareaopen(img,100);
bw=bwlabel(img,8);
stats=regionprops(bw,'BoundingBox','Centroid');
imshow(pic);
hold on

for object=1:length(stats)
    if (objcount==0)
    bb=stats(object).BoundingBox;
    bc=stats(object).Centroid;
    centroids(c,1)=bc(1);
    centroids(c,2)=bc(2);
    rectangle('Position',bb,'EdgeColor','b','LineWidth',3)
    plot(bc(1),bc(2),'-m+')
    bcent1=bc(1);
    bcent2=bc(2);
    end
    objcount=1;
end
%{/
if (plotcount==0)
for i=1:c
    plot(centroids(i,1),centroids(i,2),'-m+')
    if (i>1 && centroids(i-1,1)~=0 && centroids(i-1,2)~=0 && centroids(i,1)~=0 && centroids(i,2)~=0)
    line([centroids(i-1,1),centroids(i,1)],[centroids(i-1,2),centroids(i,2)])
    end
end
plotcount=1;
end
%}
if (c>1)
if (centroids(c,1)==0 && centroids(c-1,1)~=0 && centroids(c,2)==0 && centroids(c-1,2)~=0)
    c1last=centroids(c-1,1);
    c2last=centroids(c-1,2);
    diffc1=c1last-cent1;
    diffc2=c2last-cent2;
    c=0;
    centroids=zeros(1000,2);
end
end

hold off
end