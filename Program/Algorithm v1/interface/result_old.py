from tkinter import *
from tkinter import ttk
import interface.home
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append("..") # Adds higher directory to python modules path.
import jupyter_import
import main_program

#====================( Class )====================
class Result():
    #====================( Functions )====================
    def __init__(self, result, fs_res, pred_res, train_res):
        self.fs_res = fs_res
        self.pred_res = pred_res
        self.train_res = train_res
        self.width = 25
        #================( Root Reference )================
        self.root = result
        #====================( Main Frame )====================
        self.frame_main = LabelFrame(result, text="Result", padx = 10, pady = 10)
        self.backbutton = Frame(result)
        #====================( Notebook )====================
        self.tabControl = ttk.Notebook(self.frame_main)
        #====================( Tabs )====================
        tab_table = ttk.Frame(self.tabControl)
        tab_chart = ttk.Frame(self.tabControl)
        self.tabControl.add(tab_table, text='Table View')
        self.tabControl.add(tab_chart, text='Chart View')
        #====================( Frames )====================
        self.frame_table = Frame(tab_table)
        #====================( Widgets )====================
        #Button
        '''
        @Attributes
        text: The displayed text
        state: DISABLED/ENABLED
        padx: Performs padding on x-axis (*.px)
        pady: Performs padding on y-axis (*.px)
        command: Function to execute
        '''
        but_cv_chart = Button(tab_chart, text="Show chart", command=lambda: self.chart())
        button_goback = Button(self.backbutton, text = "Go Back", width = 10, command = lambda: self.back())
        #====================( Display )====================
        '''
        @Functions
        .pack(padx, pady)
        .grid(row, column, columnspan)
        '''
        but_cv_chart.pack()
        button_goback.pack()
        self.backbutton.pack()
        self.run_algo()
        self.table()
        self.frame_table.pack()
        self.tabControl.grid(row = 0, column = 1)
        self.frame_main.pack(fill=BOTH, pady = 10)

    def run_algo(self):
        print(self.fs_res)
        print(self.pred_res)
        print(self.train_res)
        self.filenames = []
        self.results = []
        self.pp_names = []
        for i,filename in enumerate(self.train_res['uploads']):
            fs_res = self.fs_res['result'][i]
            pos = filename.rfind('/')
            self.filenames.append(filename[pos+1:])
            self.model_name, pp_name, result = main_program.main_algo_run(filename,fs_res,self.pred_res,self.train_res)
            self.results.append(result)
            self.pp_names.append(pp_name)
            print(self.model_name)
            print("*"*50)
            print(pp_name)
            print("*"*50)
            print(result)

    def create_table_headers(self,name,row_num):
        entry = Entry(self.frame_table, bg='light gray')
        entry.grid(row=row_num,column=0)
        entry.insert(END,name)

        for i in range(len(self.model_name)):
            entry = Entry(self.frame_table, bg='light gray',width=self.width)
            entry.grid(row=row_num,column=i+1)
            entry.insert(END,self.model_name[i])

        return row_num

    def create_table_content(self,row_num,score,k):
        col_num = 0
        for i in range(len(self.pp_names[k])):
            entry = Entry(self.frame_table)
            entry.grid(row=row_num, column=0)
            entry.insert(END,f'{self.filenames[k]} ({self.pp_names[k][i]})')
            for m in range(len(self.model_name)):
                entry = Entry(self.frame_table,width=self.width)
                entry.grid(row=row_num, column=m+1)
                entry.insert(END,score[col_num-1])
                col_num += 1
            row_num += 1
        return row_num

    def table(self):
        sum_pp = sum([len(listElem) for listElem in self.pp_names])
        spaces = sum_pp * len(self.filenames) + 3
        auc_header_num = 0
        auc_row_num = 1
        f1_header_num = spaces
        f1_row_num = f1_header_num + 1
        fpr_header_num = spaces * 2
        fpr_row_num = fpr_header_num + 1
        fnr_header_num = spaces * 3
        fnr_row_num = fnr_header_num + 1
        for k in range(len(self.filenames)):
            (self.auc_name,self.auc_score) = self.results[k][0]
            (self.f1_name,self.f1_score)= self.results[k][1]
            (self.fpr_name,self.fpr) = self.results[k][2]
            (self.fnr_name,self.fnr) = self.results[k][3]

            # ========= AUC ========== #
            auc_row_num = self.create_table_content(auc_row_num,self.auc_score,k)
            # ======================== #

            # ========= F1-Score ======== #
            f1_row_num = self.create_table_content(f1_row_num,self.f1_score,k)
            # =========================== #

            # ========= False Positive Rate ========= #
            fpr_row_num = self.create_table_content(fpr_row_num,self.fpr,k)
            # ======================================= #

            # ========= False Negative Rate ========= #
            fnr_row_num = self.create_table_content(fnr_row_num,self.fnr,k)
            # ======================================= #

        self.create_table_headers(self.auc_name,auc_header_num)
        self.create_table_headers(self.f1_name,f1_header_num)
        self.create_table_headers(self.fpr_name,fpr_header_num)
        self.create_table_headers(self.fnr_name,fnr_header_num)

    def create_bars(self,name,score,labels):
        flatten_list = [item for items in score for item in items]
        n = len(self.model_name)
        new_score = [flatten_list[i:i+n] for i in range(0,len(flatten_list),n)]

        print('%'*50)
        print(name)
        print(self.model_name)
        print(labels)
        print(new_score)
        ypos = np.arange(len(self.model_name))
        print('%'*50)

        bar_width = 0.25

        def sub_bar(x,vals,width=0.8):
            n = len(vals)
            xpos = np.arange(len(x))
            for i in range(n):
                plt.bar(xpos - width/2 + i/float(n)*width, vals[i],
                        width=width/float(n),align='edge')

        sub_bar(self.model_name,new_score)
        plt.show()
        pass
            
        
    def chart(self):
        labels = []
        auc_data = []
        f1_data = []
        fpr_data = []
        fnr_data = []
        for k in range(len(self.filenames)):
            auc_data.append(self.results[k][0][1])
            f1_data.append(self.results[k][1][1])
            fpr_data.append(self.results[k][2][1])
            fnr_data.append(self.results[k][3][1])
            
            for i in range(len(self.pp_names[k])):
                labels.append(f'{self.filenames[k]} ({self.pp_names[k][i]})')

        self.create_bars(self.auc_name,auc_data,labels)


        # name = ['DT','lR','MLP','NB']
        # temp1 = [90,20,21,22]
        # temp2 = [60,70,100,89]
        # ypos = np.arange(len(name))
        # #plt.legend(labels=["a","b"])
        # plt.subplot(1,2,1) #row, column, position
        # plt.xticks(ypos, name)
        # plt.title('AUC-score')
        # plt.xlabel('Model')
        # plt.ylabel('Score')
        # plt.bar(ypos,temp1,color='blue')
        # plt.subplot(1,2,2) #row, column, position
        # plt.xticks(ypos, name)
        # plt.title('F1-score')
        # plt.xlabel('Model')
        # plt.ylabel('Score')
        # plt.bar(ypos,temp2,color='orange')
        # plt.show()
    
    def back(self):
        self.frame_main.destroy()
        self.backbutton.destroy()
        interface.home.Home(self.root)

#====================( Main )====================
if __name__=='__main__':
    root = Tk()
    sm = Result(root, [])
    root.mainloop()
