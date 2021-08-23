# -*- coding: utf-8 -*-
"""
Created on Sun Nov  29 22:46:07 2020

@author: Ritwick
"""
#
#  KMeans clustering
#  Data Scaling: Min-Max, Standardized or No scaling
#  The datapoints are randomly assigned k clusters initially 
#  % change in inertia is computed at each iteration
#  Iterations stop when:
#       1. % change in model inertia is < 0.1%   or
#       2. number of iterations exceeds user specified 
#          maximum number of iterations.
#  Output is written to a spreadsheet with an additional column 
#  named "Cluster" with integer cluster labels. 
#  output excel spreadsheet:  KMeansOutputFile.xlsx
#
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random
import statistics
#
class kmeans:
    def __init__(self,df,ncl,niter):
        self.df = df
        self.nrows = self.df.shape[0]
        self.ncols = self.df.shape[1]
        self.ScaleOpt = 1
        self.columns = list(self.df)
        self.ScaleParam1 = [0.0 for i in range (self.ncols)]
        self.ScaleParam2 = [0.0 for i in range (self.ncols)]
        self.nclusters = ncl
        self.ClusterCenter =np.zeros((self.nclusters, self.ncols))
        self.v1 = np.zeros(self.ncols)
        self.v2 = np.zeros(self.ncols)
        self.distVal = 0.0
        self.dist = np.zeros(self.nclusters)
        self.CL = np.zeros(self.nclusters, dtype = int)
        self.CCount = np.zeros(self.nclusters, dtype = int)
        self.distMax = np.zeros(self.nclusters) 
        self.distMin = np.zeros(self.nclusters) 
        self.AvgClusterDist = np.zeros(self.nclusters)
        self.NewCluster = 0
        L = range(0,self.nclusters)
        self.randarr = random.choices(L,k=self.nrows)
        self.df['Cluster']=self.randarr
        self.Inertia = 0.0
        self.Inertia_old = np.finfo(type(self.Inertia)).max
        self.tol = 0.1
        self.IsNotConverged = True
        self.IterMax = niter
#
#   0 -  no scaling
#   1 -  min-max scaling
#   2 -  standard scaling
#
    def Read_options(self):
        print("data-scaling option:")
        print(" 0 -  no scaling")
        print(" 1 -  min-max scaling")
        print(" 2 -  standard scaling")
        txt = input("data scaling option: ")
        self.ScaleOpt = int(txt)
#     
#   Compute Scaling parameter for each feature vector
#
    def ScaleParams(self):
        for iC in range (self.ncols):
            if self.ScaleOpt == 2:
                self.ScaleParam1[iC] = self.df[self.columns[iC]].mean()
                self.ScaleParam2[iC] = self.df[self.columns[iC]].std()
            elif self.ScaleOpt == 1:
                self.ScaleParam1[iC] = self.df[self.columns[iC]].min()
                self.ScaleParam2[iC] = self.df[self.columns[iC]].max()
#
#   Transform feature data based on the specified scaling option
#        
    def ScaleFeaturedata (self):
#

        if self.ScaleOpt == 1:
            for i in range (self.nrows):
                for j in range (self.ncols):
                    d_max_min = self.ScaleParam2[j]-self.ScaleParam1[j]
                    self.df.iloc[i,j] = (self.df.loc[i,self.columns[j]]-self.ScaleParam1[j])/d_max_min
        elif self.ScaleOpt == 2:
            for i in range (self.nrows):
                for j in range (self.ncols):
                    self.df.iloc[i,j] = (self.df.loc[i,self.columns[j]]-self.ScaleParam1[j])/self.ScaleParam2[j]
#
#
#   Compute square of Euclidean distance between two vectors
#
    def EuclidDist(self):
        distV = 0.0
        for i in range (self.ncols):
            distV += (self.v1[i] - self.v2[i])**2
        self.distVal = distV   
#
#    Compute Euclid distance between a Feature vector and a Cluster Center
#
    def ComputeDist(self,ir):
        self.dist.fill(0.0)
        self.CL.fill(0)
        for i in range(self.nclusters):
            for j in range(self.ncols):
                self.v2[j] = self.ClusterCenter[i,j]
            self.EuclidDist()
            self.dist[i] = self.distVal
            self.CL[i] = i
            if self.df.iloc[ir,self.ncols] == i:
                self.AvgClusterDist[i] = self.AvgClusterDist[i] + self.distVal
                self.distMax[i] = max(self.distMax[i],self.dist[i]) 
                self.distMin[i] = min(self.distMin[i],self.dist[i]) 
#
#    Compute each cluster center
#
    def ComputeClusterCenter(self):
        for i in range (self.nclusters):
            cond = self.df.loc[:,'Cluster'] == i
            dft = self.df[cond]
            self.CCount[i] = dft.shape[0]
            c = []
            for j in range (self.ncols):
                self.ClusterCenter[i,j] = dft.iloc[:,j].mean()
                c.append(self.ClusterCenter[i,j])
            print('Cluster',i,' No. of datapoints:',dft.shape[0],' Center:','  '.join(str(value) for value in c))
#
#    Assign a feature datapoint to its nearest Cluster Center
#
    def AssignNewCluster(self):
        df_L = pd.DataFrame({'dist':self.dist,'CLabel':self.CL})
        df_L.sort_values('dist',ascending=True,inplace=True)
        self.NewCluster = df_L.iloc[0,1]
#
#   Driver method for distance calculation and cluster assignment
#
    def DistToClusterCenter(self):
        self.AvgClusterDist.fill(0.0)
        self.distMax.fill(-np.finfo(type(self.Inertia)).max)
        self.distMin.fill(np.finfo(type(self.Inertia)).max) 
        for i in range (self.nrows):
            for j in range(self.ncols):
                self.v1[j] = self.df.iloc[i,j]
            self.ComputeDist(i)
            self.AssignNewCluster()
            self.df.iloc[i,self.ncols] = self.NewCluster
#
#   Compute model inertia
#
    def ComputeInertia(self):
        self.Inertia = 0.0
        for i in range(self.nclusters): 
            self.Inertia += self.AvgClusterDist[i]
        print('Inertia:',self.Inertia)
        print(' ')
#
#   Iterate and check convergence against tolerance
#
    def IterCheckConvergence(self):
        Iter = 0
        while self.IsNotConverged:
            self.ComputeClusterCenter()
            self.DistToClusterCenter()
            self.Inertia_old = self.Inertia
            self.ComputeInertia()
            convTol = 100.0*abs(self.Inertia_old - self.Inertia)/self.Inertia
            print('*** iteration:',Iter,' Percent change in model Inertia:',convTol,'%')
            Iter += 1
            if (convTol < self.tol) | (self.IterMax < Iter ):
                self.IsNotConverged = False
#
#   Write output excel spreadsheet with cluster labels
#
    def WriteOutput(self):
        self.df.to_excel('KMeansOutputFile.xlsx',sheet_name='Sheet1')
#
#  Read Data-Set
#
u_str = input('Number of Clusters:  ')
nClust = int(u_str)
u_str = input('Max Number of iterations:  ')
niter = int(u_str)
u_str = input('enter Excel filename: ')
df = pd.read_excel(u_str, sheet_name = 'Sheet1')  
#
kmeans_do = kmeans(df,nClust,niter)
kmeans_do.Read_options()
kmeans_do.ScaleParams()
kmeans_do.ScaleFeaturedata()
kmeans_do.IterCheckConvergence()
kmeans_do.WriteOutput()


