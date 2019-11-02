clc;
clear all;
close all;
%% Problem Definition
img= double(imread('pcb1missingpinhole.jpg'));
[s1,s2,s3]=size(img);
% image normalization
Rplane = img(:,:,1);
Gplane = img(:,:,1);
Bplane = img(:,:,1);
X1 = (Rplane-min(Rplane(:)))/(max(Rplane(:))-min(Rplane(:))); 
X2 = (Gplane-min(Gplane(:)))/(max(Gplane(:))-min(Gplane(:))); 
X3 = (Bplane-min(Bplane(:)))/(max(Bplane(:))-min(Bplane(:)));  
% taking R-plane, B-plane, G-plane values as features
X = [X1(:) X2(:) X3(:)]; % [(s1*s2)x3]
k = 2; % no. of clusters
% Setting the c-Means Algorithms
% opt.Exponent = NaN;
% opt.MaxNumIteration = 15;
% opt.MinImprovement = 0.001;
% opt.Verbose = 0;
options=[NaN 25 0.001 1];
[centers] = fcm(X,k,options);
distancemat = dist(centers,X');
[~,indx] = min(distancemat',[],2);
outimgindx=reshape(indx,s1,s2); % pixel indexed image
outimg=zeros(s1,s2);
    for i=1:s1
        for j=1:s2
            if outimgindx(i,j)== 1
                outimg(i,j)= 62;
            elseif outimgindx(i,j)== 2
                outimg(i,j)= 124;
            elseif outimgindx(i,j)== 3
                outimg(i,j)= 186;
            elseif outimgindx(i,j)== 4
                outimg(i,j)= 255;
            end
        end
    end
figure;imshow(uint8(img)); % original image
figure;imshow(uint8(outimg)); % segmented image