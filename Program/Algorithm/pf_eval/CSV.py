import csv

def write_results(header,result):
    filters = ['No filter','CFS','RFE']
    #header = ['Dataset', 'Algo 1', 'Algo 2','Algo 3']
    #dummy = [['CM1','95%','92%','87%'], ['KC1','Trying','To','Test'],['KC4','90%','80%','70%']]
    with open('pred_results.csv','w',encoding='UTF8', newline='') as file:
        res = csv.writer(file)
        for i in range(len(filters)):
            res.writerow('')
            res.writerow([filters[i]])
            res.writerow(header)
            res.writerow([result[0][0]] + result[0][1][i*8:i*8+8])
            res.writerow([result[1][0]] + result[1][1][i*8:i*8+8])