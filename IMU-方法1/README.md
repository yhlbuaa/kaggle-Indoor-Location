1、数据集
https://www.kaggle.com/code/suryajrrafl/interpolated-imu-data
对原始数据进行了线性插值
数据中为什么陀螺仪只用z轴，因为数据采集时候，手机是端平的，所以z轴基本就是航向转动 ，参考https://www.kaggle.com/c/indoor-location-navigation/discussion/236096
imuDataOutput['path'] = pathNameList   #保存path
imuDataOutput['building'] = buildingList #保存 building 
imuDataOutput['encoderData'] = encoderDataList #encoder输入 [100,7] 设置长度为100 ，特征为'delta_time（时间增量）','lin_ax', 'lin_ay'，'gz_s'，'roll', 'pitch', 'yaw'
imuDataOutput['decoderData'] = decoderDataList #decoder 输出 【107，3】 特征为'delta_x','delta_y', 'floor'
imuDataOutput['inferenceTsList'] = inferenceTsList #decoder的输入 为【107，1】 特征为'delta_time（时间增量）'
imuDataOutput['numWayPoints'] = numWayPointsList # decoderDataList中每条轨迹实际长度
imuDataOutput['pathInitialTime'] = pathInitialTimeList #每条轨迹初始时间

2、模型
采用 Conv-se2seq-Attention mode 
模型介绍https://blog.csdn.net/u010417185/article/details/83089986


3、结果
Fold 0 -> trainData shape = (8701, 7), validationData shape = (2176, 7)
100%|██████████| 50/50 [21:34<00:00, 25.89s/it]
  0%|          | 0/50 [00:00<?, ?it/s]
For Fold 0, Best position validation score of 7.698928627745829 was got at epoch 48

Fold 1 -> trainData shape = (8701, 7), validationData shape = (2176, 7)
100%|██████████| 50/50 [22:02<00:00, 26.45s/it]
  0%|          | 0/50 [00:00<?, ?it/s]
For Fold 1, Best position validation score of 8.024622592554955 was got at epoch 38

Fold 2 -> trainData shape = (8702, 7), validationData shape = (2175, 7)
100%|██████████| 50/50 [21:59<00:00, 26.39s/it]
  0%|          | 0/50 [00:00<?, ?it/s]
For Fold 2, Best position validation score of 8.491038546538185 was got at epoch 49
Fold 3 -> trainData shape = (8702, 7), validationData shape = (2175, 7)
 16%|█▌        | 8/50 [03:35<19:02, 27.20s/it]