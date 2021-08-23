# my_public_workspace

Input spreadsheet format:

KMeans clustering
#
#    input is an Excel spreadsheet (Sheet1)
#    column 1: Feature 1
#    column 2: Feature 2
#    column 3: .....       
#    column n: Feature n
#
#    see sample input excel file: IrisCluster.xlsx
#    This is the iris dataset without the labels
#    User input choices:
#            Number of clusters
#            Maximum number of iterations
#            data scaler: 0: no scaling
#                         1: Min-Max normalized scaling
#                         2: Standard Scaler
#
Required packages:

numpy, pandas and xlrd. 
To install these packages:
pip install pandas
pip install numpy
pip install xlrd

Program execution:
python KMeans.py

Sample output:

Number of Clusters:  3

Max Number of iterations:  10

enter Excel filename: IrisCluster.xlsx
data-scaling option:
 0 -  no scaling
 1 -  min-max scaling
 2 -  standard scaling

data scaling option: 2
Cluster 0  No. of datapoints: 50  Center: 0.0056356207662562885  -0.26291857852530387  0.0653661293131321  0.05678139737214015
Cluster 1  No. of datapoints: 49  Center: -0.003039620529907204  0.13903714302966924  -0.05406951736978964  -0.05708446919485027
Cluster 2  No. of datapoints: 51  Center: -0.002604698673481924  0.12417860623159105  -0.012135296363473462  -0.0008221740795972603
Inertia: 590.1223194156966
 
*** iteration: 0  Percent change in model Inertia: 100.0 %
Cluster 0  No. of datapoints: 84  Center: 0.3804044017223945  -0.657186622345619  0.570617701101397  0.5196433816650436
Cluster 1  No. of datapoints: 49  Center: -0.9987207238395798  0.8921157782614696  -1.298624580616197  -1.25243539346551
Cluster 2  No. of datapoints: 17  Center: 0.9990203366740036  0.6758825377776329  0.9235716210397676  1.042311189408604
Inertia: 192.46150096416824
 
*** iteration: 1  Percent change in model Inertia: 206.61837118560317 %
Cluster 0  No. of datapoints: 64  Center: 0.0967364368136633  -0.7984133807300724  0.4245846538964899  0.3579957909318538
Cluster 1  No. of datapoints: 50  Center: -1.0111913832028148  0.8394944086246475  -1.3005214861029293  -1.2509378621062446
Cluster 2  No. of datapoints: 36  Center: 1.232456589001835  0.2534371093192224  1.0514626793269684  1.1009767357131541
Inertia: 145.25814058011161
 
*** iteration: 2  Percent change in model Inertia: 32.496189332689 %
Cluster 0  No. of datapoints: 59  Center: 0.025448989658765114  -0.8320673301352355  0.38269316699267475  0.3171170714254273
Cluster 1  No. of datapoints: 50  Center: -1.0111913832028148  0.8394944086246475  -1.3005214861029293  -1.2509378621062446
Cluster 2  No. of datapoints: 41  Center: 1.1965385065920333  0.17359151333527492  1.0352970110384978  1.0691947778344384
Inertia: 140.61582708138354
 
*** iteration: 3  Percent change in model Inertia: 3.301416060399277 %
Cluster 0  No. of datapoints: 57  Center: 0.009110214020640595  -0.8649851295343062  0.3793900258703866  0.3097919477680042
Cluster 1  No. of datapoints: 50  Center: -1.0111913832028148  0.8394944086246475  -1.3005214861029293  -1.2509378621062446
Cluster 2  No. of datapoints: 43  Center: 1.1637276037433488  0.17045190586564715  1.0093219262914928  1.0439244670357197
Inertia: 140.35166848700263
 
*** iteration: 3  Percent change in model Inertia: 3.301416060399277 %
Cluster 0  No. of datapoints: 57  Center: 0.009110214020640595  -0.8649851295343062  0.3793900258703866  0.3097919477680042
Cluster 1  No. of datapoints: 50  Center: -1.0111913832028148  0.8394944086246475  -1.3005214861029293  -1.2509378621062446
Cluster 2  No. of datapoints: 43  Center: 1.1637276037433488  0.17045190586564715  1.0093219262914928  1.0439244670357197
Inertia: 140.35166848700263
 
*** iteration: 4  Percent change in model Inertia: 0.18821193736316627 %
Cluster 0  No. of datapoints: 56  Center: -0.011357501034041368  -0.8699705596441877  0.3756258413625896  0.3106129627676014
Cluster 1  No. of datapoints: 50  Center: -1.0111913832028148  0.8394944086246475  -1.3005214861029293  -1.2509378621062446
Cluster 2  No. of datapoints: 44  Center: 1.1635361185919733  0.15326433883731566  0.9997960724736639  1.0261947088710568
Inertia: 140.21315027966057
 
*** iteration: 5  Percent change in model Inertia: 0.09879116692391512 %

#############################################

The assigned cluster for each datapoint is written to an additional column named 'Cluster'
output spreadsheet: KMeansOutputFile.xlsx





