
1、wifi 数据

https://www.kaggle.com/code/devinanzelmo/wifi-features/notebook
https://www.kaggle.com/code/higepon/generate-wifi-features-5-times-faster/notebook
数据为字典，字典的key=building  value=dataframe 结构，其中包含 bssid, rssid, fre, x,  y, floor,path  其中 x y是wifi 时间 找最近的waypoint


2、模型采用 全连接结构

https://www.kaggle.com/code/suryajrrafl/end-to-end-wifi-features-model/notebook


3、结果

For Fold 0, Best validation score of 57.42298889160156 was got at epoch 3
For Fold 1, Best validation score of 60.09745407104492 was got at epoch 4
Best valPosLoss for all folds = [57.42298889 60.09745407]
Mean, std =58.76022148132324, 1.3372325897216797

代码工整 但是模型简单 效果一般 没有没embedding操作
