clc;
clear all;
close all;
%% Problem Definition
X = [10 0 0;
     10 0 1;
     10 1 0;
     2 10 0;
     2 10 1;
     2 11 0;
     5 0 10;
     5 0 11;
     5 1 10]; % [9x3] data matrix 9 observations, each is of 3 dimensional features
k = 2; % no. of clusters
% opt.Exponent = NaN;
% opt.MaxNumIteration = 15;
% opt.MinImprovement = 0.001;
% opt.Verbose = 0;
options=[NaN 25 0.001 1];
[centers] = fcm(X,k,options);
distancemat = dist(centers,X');
[~,indx] = min(distancemat',[],2);
indx'