利用wifi定位的方法1，

1、数据集的准备 
    
    方法1
        数据：indoor-unified-wifi-ds
        code: Create Unified WiFi Features Example
        这里会将原始的wifi数据进行处理，These features are WiFi BSSID ordered by RSSI strength.For example, bssid_0 has the strongest RSSI for the x, y, floor.  取每个位置降序前100的wifi，如果不到100，填充-999
        train 数据：BSSID 1到BSSID 100，RSSI 1到RSSI 100，pdr插值出来的x,y，楼层floor, 轨迹path,商场site
        test 数据：BSSID 1到BSSID 100，RSSI 1到RSSI 100，site_path_timestamp，商场site

    
    方式2
        Make dataset with Wi-Fi and Beacon 
        方式和上述相同，只是多了beacon 


2、算法
https://www.kaggle.com/code/luffy521/lstm-by-pytorch-with-unified-wi-fi-feats ，但是从验证结果看mean position error =30米，文件lstm-by-pytorch-with-unified-wi-fi-feats.ipynb是增加了注释的代码

建模，代码中将【1，batch_size,维度】作为输入进入lstm 相当于 batch_sie=1 seq_len=batch_size,那么每条轨迹作为一个序列，轨迹上每个点作为序列的每一个点


3、mean position error=30
