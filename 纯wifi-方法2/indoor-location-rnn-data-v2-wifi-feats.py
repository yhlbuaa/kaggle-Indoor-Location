import numpy as np
import pandas as pd
import time
from pathlib import Path
#from indoor_location_github_script import read_data_file, compute_step_positions
from compute_f import split_ts_seq, compute_step_positions
from io_f import read_data_file
import pickle

def save_pickle(obj, filename):
    outfile = open(filename,'wb')
    pickle.dump(obj, outfile)
    outfile.close()

test_buildings = [
    '5a0546857ecc773753327266',
    '5c3c44b80379370013e0fd2b',
    '5d27075f03f801723c2e360f',
    '5d27096c03f801723c31e5e0',
    '5d27097f03f801723c320d97',
    '5d27099f03f801723c32511d',
    '5d2709a003f801723c3251bf',
    '5d2709b303f801723c327472',
    '5d2709bb03f801723c32852c',
    '5d2709c303f801723c3299ee',
    '5d2709d403f801723c32bd39',
    '5d2709e003f801723c32d896',
    '5da138274db8ce0c98bbd3d2',
    '5da1382d4db8ce0c98bbe92e',
    '5da138314db8ce0c98bbf3a0',
    '5da138364db8ce0c98bc00f1',
    '5da1383b4db8ce0c98bc11ab',
    '5da138754db8ce0c98bca82f',
    '5da138764db8ce0c98bcaa46',
    '5da1389e4db8ce0c98bd0547',
    '5da138b74db8ce0c98bd4774',
    '5da958dd46f8266d0737457b',
    '5dbc1d84c1eb61796cf7c010',
    '5dc8cea7659e181adb076a3f'
]

floor_map = {"B2":-2, "B1":-1, "F1":0, "F2": 1, "F3":2, "F4":3, "F5":4, "F6":5, "F7":6,"F8":7, "F9":8,
             "1F":0, "2F":1, "3F":2, "4F":3, "5F":4, "6F":5, "7F":6, "8F": 7, "9F":8}


wifi_ts_cutoff = 5000 # do not include wifi data out of this range (in ms)

bssid_map = {}
xy_data = {}
timestamps = {}
path_data = {}
path_name = {}

for building in test_buildings:
    #     print(building)
    start = time.time()
    for trace_path in Path(f'/Users/heliang.yuan/Downloads/indoor/indoor-location-navigation/train/{building}').glob('*/*.txt'):
        str_split = str(trace_path).split('/')
        floor = floor_map[str_split[-2]]
        trace = str_split[-1][:-4]

        path_datas = read_data_file(trace_path)
        wifi_datas = path_datas.wifi
        if len(wifi_datas) == 0:
            continue
        acce_datas = path_datas.acce
        #         magn_datas = path_datas.magn
        ahrs_datas = path_datas.ahrs
        #         ibeacon_datas = path_datas.ibeacon
        posi_datas = path_datas.waypoint
        step_positions = compute_step_positions(acce_datas, ahrs_datas, posi_datas)

        path_key = len(path_data)
        path_value = []

        for pos in step_positions:
            used_bssids = set()
            X = []
            y = np.insert(pos[1:], 0, floor)#将pos第一列的时间替换成楼层
            pos_id = len(xy_data)#每一个位置index
            pos_ts = int(pos[0])
            close_wifis = wifi_datas[np.abs(wifi_datas[:, -1].astype(int) - pos_ts) < wifi_ts_cutoff]#根据wifi 的lastseen 找每个定位点最近的Wi-Fi
            if len(close_wifis) == 0:
                continue
            for idx in np.argsort(np.abs(close_wifis[:, -1].astype(int) - pos_ts)):#按照lastseen 于pos_ts的差值进行wifi排序
                wifi = close_wifis[idx]
                bssid = wifi[-3]
                if bssid in bssid_map:
                    bssid = bssid_map[bssid]
                else:
                    i = len(bssid_map)#将bssid 转化为 1 2 3 。。。的序列号，bssid_map为字典，key为bssid ,value为序列号,所有轨迹公用
                    bssid_map[bssid] = i
                    bssid = i

                if bssid in used_bssids:
                    continue
                else:
                    used_bssids.add(bssid)
                    rssi = wifi[-2]
                    X.append([floor, bssid, int(rssi)])
            X = np.array(X)
            xy_data[pos_id] = (X, y)#x 为【楼层 bssid rssi】 y为【楼层，经度,纬度】
            timestamps[pos_id] = pos[0]#每个位置时间
            path_value.append(pos_id)#记录每一个位置点index 记录0，1，2.。。。，所有轨迹公用
        path_data[path_key] = path_value
        path_name[path_key] = trace_path
    #         break
    #     break
    print(f'{building} took {time.time() - start} seconds\n')
    save_pickle(xy_data, 'data.pickle')
    save_pickle(bssid_map, 'bssids.pickle')
    save_pickle(timestamps, 'timestamps.pickle')
    save_pickle(path_data, 'path_data.pickle')
    save_pickle(path_name, 'path_name.pickle')


