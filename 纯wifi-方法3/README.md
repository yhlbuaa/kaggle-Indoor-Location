利用wifi定位的方法3

1、数据集
Fix data quality issues and reformat the training data through C++ custom code @ https://www.kaggle.com/oxzplvifi/indoor-cpp The procedure is shown @ https://www.kaggle.com/oxzplvifi/indoor-preprocessing-and-eda And the result is located @ https://www.kaggle.com/oxzplvifi/indoor-xy-floor
File names are in the format "building_floor.csv"
Columns are:
    X,Y = coordinates.
    count = amount of Wifi bssids detected (NaN means only beacons were detected there).
    magn = magnetic strength (i.e. magnitude).
    Wifi rssi values per bssid.
    Beacon rssi values per ID i.e. "UUID_MajorID_MinorID".

数据转化成上述格式，每一个build_每一个floor 一个文件夹


2、首先进行楼层判断
https://www.kaggle.com/code/oxzplvifi/indoor-kmeans-gbm-floor-prediction
对于给定（x，y）的给定wifi bssid，rssi在楼上或楼下的强度可能比在同一楼层的远处更强。因此，在预测之前根据（x，y）对整个建筑进行聚类是有意义的，然后将楼层附加到聚类上，例如，楼层0将变为0_0,0_1,0_2,0_3
每一层聚成4类


3、用LightGBM 进行回归
https://www.kaggle.com/code/wduuah/indoor 注释版见indoor.ipynb


4、结果


9	5a0546857ecc773753327266 xrmse = 1.82449793497846, yrmse = 1.369805772619651

9	5c3c44b80379370013e0fd2b xrmse = 2.0403003602545633, yrmse = 1.523308453747644

9	5d27075f03f801723c2e360f xrmse = 2.0309404492473164, yrmse = 1.5815331395520864

9	5d27096c03f801723c31e5e0 xrmse = 1.3353284858376195, yrmse = 1.340746563418705

9	5d27097f03f801723c320d97 xrmse = 2.04041479570027, yrmse = 2.670134380894907

9	5d27099f03f801723c32511d xrmse = 1.043434975359525, yrmse = 1.6290263275635406

9	5d2709a003f801723c3251bf xrmse = 1.5508846037271633, yrmse = 1.3269377854300837


9	5d2709b303f801723c327472 xrmse = 1.8427973576649186, yrmse = 1.6028528139415867

9	5d2709bb03f801723c32852c xrmse = 1.7687189186267633, yrmse = 1.8480131935406667

9	5d2709c303f801723c3299ee xrmse = 1.4152768341539135, yrmse = 1.7844748476006422

9	5d2709d403f801723c32bd39 xrmse = 1.4898544616157696, yrmse = 1.4772767631772616

9	5d2709e003f801723c32d896 xrmse = 1.987249753457309, yrmse = 1.116336755378228


9	5da138274db8ce0c98bbd3d2 xrmse = 1.9973497180062834, yrmse = 1.4093344997762494

9	5da1382d4db8ce0c98bbe92e xrmse = 1.7749780092697653, yrmse = 1.7527572902322852

9	5da138314db8ce0c98bbf3a0 xrmse = 1.3645405731322626, yrmse = 1.39789044469558

9	5da138364db8ce0c98bc00f1 xrmse = 1.3251676369986691, yrmse = 1.206545381608366

9	5da1383b4db8ce0c98bc11ab xrmse = 1.7060469857619764, yrmse = 1.4766159755333954

9	5da138754db8ce0c98bca82f xrmse = 2.082289754882825, yrmse = 1.5611764560703127

9	5da138764db8ce0c98bcaa46 xrmse = 1.6735496899421682, yrmse = 1.8069041694782368

9	5da1389e4db8ce0c98bd0547 xrmse = 2.157438745541535, yrmse = 2.0723487587611884

9	5da138b74db8ce0c98bd4774 xrmse = 1.855891780980467, yrmse = 2.2878995868116063

9	5da958dd46f8266d0737457b xrmse = 1.3160862439714014, yrmse = 1.7620170645969637

9	5dbc1d84c1eb61796cf7c010 xrmse = 2.205847361330448, yrmse = 2.131575246578836

9	5dc8cea7659e181adb076a3f xrmse = 2.2900081745215046, yrmse = 2.0358131658324403




太复杂，运行太慢
