import os
import numpy as np
import glob
import math

sumsq = 0
file_number = 0
correct = 0
result_g = np.zeros(100)

#用いるデータセットによってディレクトリのパスを変更する。
for input_datas in glob.glob('city_mcepdata/city012/*.txt'):
    input_data = np.loadtxt(input_datas,skiprows=3)
    count = 0
    print('file_number:')
    print(file_number)
    for template_datas in glob.glob\
                ('city_mcepdata/city011/*.txt'):
        print(count)
        template_data = np.loadtxt(template_datas,skiprows=3)

        dist = np.zeros((template_data.shape[0],input_data.shape[0]))
        #dist
        for i in range(template_data.shape[0]):
            for j in range(input_data.shape[0]):
                for k in range(15):
                    tmp = template_data[i,k] - input_data[j,k]
                    sumsq += pow(tmp,2)
                dist[i,j] = math.sqrt(sumsq)
                sumsq = 0
        g = np.zeros((template_data.shape[0],input_data.shape[0]))
        #g
        g[0,0] = dist[0,0]
        for i in range(1,template_data.shape[0]):
            g[i,0] = g[i-1,0] + dist[i,0]

        for j in range(1,input_data.shape[0]):
            g[0,j] = g[0,j-1] + dist[0,j-1]

        for i in range(1,template_data.shape[0]):
            for j in range(1,input_data.shape[0]):
                g[i,j] = min(g[i-1,j]+dist[i,j],g[i-1,j-1]+2*dist[i,j],\
                                                    g[i,j-1]+dist[i,j])

        hoge = template_data.shape[0]-1
        huge = input_data.shape[0]-1
        result_g[count] = g[hoge,huge]/(template_data.shape[0]+input_data.shape[0])
count += 1

    #evaluation
    print('output:')
    print(np.argmin(result_g))
    if file_number == np.argmin(result_g):
        correct += 1
    file_number += 1
print('result\n')
print(correct)

