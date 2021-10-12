from tkinter import *
from tkinter import ttk
import interface.home
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append("..") # Adds higher directory to python modules path.
from tkinter import messagebox
import main_program
import os

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
        tab_csv = ttk.Frame(self.tabControl)
        self.tabControl.add(tab_table, text='Table View')
        self.tabControl.add(tab_chart, text='Chart View')
        self.tabControl.add(tab_csv, text = 'CSV Results')
        #====================( Frames )====================
        self.frame_table = Frame(tab_table)
        #====================( Widgets )====================
        #Label
        lab_cv_auc = Label(tab_chart, text="AUC")
        lab_cv_f1 = Label(tab_chart, text="F1 score")
        lab_cv_fpr = Label(tab_chart, text="False Positive Rate")
        lab_cv_fnr = Label(tab_chart, text="False Negative Rate")

        # CSV File path
        csvfilepath = os.getcwd() + '\csv_results\\' + train_res['pfn'] +'.csv'
        csvfilepath = csvfilepath.replace('\\\\','\\')
        lab_cv_csv = Label(tab_csv, text=f'CSV File Location\n{csvfilepath}')
        
        #Button
        '''
        @Attributes
        text: The displayed text
        state: DISABLED/ENABLED
        padx: Performs padding on x-axis (*.px)
        pady: Performs padding on y-axis (*.px)
        command: Function to execute
        '''
        but_cv_auc = Button(tab_chart, text="Show chart", command=lambda: self.chart(0))
        but_cv_f1 = Button(tab_chart, text="Show chart", command=lambda: self.chart(1))
        but_cv_fpr = Button(tab_chart, text="Show chart", command=lambda: self.chart(2))
        but_cv_fnr = Button(tab_chart, text="Show chart", command=lambda: self.chart(3))
        button_goback = Button(self.backbutton, text = "Go Back", width = 10, command = lambda: self.back())
        #====================( Display )====================
        '''
        @Functions
        .pack(padx, pady)
        .grid(row, column, columnspan)
        '''
        #Chart view
        lab_cv_auc.grid(row = 0, column = 0)
        but_cv_auc.grid(row = 0, column = 1)
        lab_cv_f1.grid(row = 1, column = 0)
        but_cv_f1.grid(row = 1, column = 1)
        lab_cv_fpr.grid(row = 2, column = 0)
        but_cv_fpr.grid(row = 2, column = 1)
        lab_cv_fnr.grid(row = 3, column = 0)
        but_cv_fnr.grid(row = 3, column = 1)

        # CSV View
        lab_cv_csv.grid(row = 0, column = 0)

        #Remaining
        button_goback.pack()
        self.backbutton.pack()
        if self.run_algo():
            self.run_csv()
            self.table()
            self.frame_table.pack()
            self.tabControl.grid(row = 0, column = 1)
            self.frame_main.pack(fill=BOTH, pady = 10)

    def run_algo(self):
        self.filenames = []
        self.results = []
        self.pp_names = []
        for i,filename in enumerate(self.train_res['uploads']):
            fs_res = self.fs_res['result'][i]
            pos = filename.rfind('/')
            self.filenames.append(filename[pos+1:])
            try:
                main_res = main_program.main_algo_run(filename,fs_res,self.pred_res,self.train_res)
            except Exception as e:
                return self.main_error(3, i, e)
            if len(main_res)==2 and main_res[0] == False:
                return self.main_error(main_res[1], i)
            self.model_name, pp_name, result = main_res
            self.results.append(result)
            self.pp_names.append(pp_name)
        return True

    def main_error(self, error_type, ds_number, error_msg = ""):
        if ds_number == 0:
            ord_ind = "st"
        elif ds_number == 1: 
            ord_ind = "nd"
        elif ds_number == 2:
            ord_ind = "rd"
        else:
            ord_ind = "th"
        #Error type 0: Invalid dataset
        if error_type == 0:
            error_msg = "The " + str(ds_number+1) + ord_ind + " dataset is invalid"
        #Error type 1: Invalid k-fold
        elif error_type == 1:
            error_msg = "There are insufficient samples in the " + str(ds_number+1) + ord_ind + " dataset (Lowering the folds may also be a valid fix)"
        #Error type 2: Invalid feature reduction
        elif error_type == 2:
            error_msg = "The " + str(ds_number+1) + ord_ind + " dataset has less features than the number of features to be reduced"
        #Error type 3: Unknown error
        elif error_type == 3:
            error_msg = "An unknown error occured when processing the " + str(ds_number+1) + ord_ind + " dataset, the error message is as followed: " + str(error_msg)
        messagebox.showerror("An error occured",error_msg)
        return False


    def run_csv(self):
        self.csv_filename = self.train_res['pfn']
        main_program.csv_writer(self.filenames,self.csv_filename,self.results,self.model_name,self.pp_names)

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
                entry.insert(END,score[col_num])
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

    def create_bars(self,score,labels):
        flatten_list = [item for items in score for item in items]
        n = len(self.model_name)
        new_score = [flatten_list[i:i+n] for i in range(0,len(flatten_list),n)]
        def sub_bar(x,vals,width=0.8):
            n = len(vals)
            xpos = np.arange(len(x))
            colors = []
            plt.xticks(xpos, self.model_name)
            for i in range(n):
                temp = plt.bar(xpos - width/2 + i/float(n)*width, vals[i],
                        width=width/float(n),align='edge')
                colors.append(temp.patches[0].get_facecolor())
            handles = [plt.Rectangle((0,0),1,1, color=col) for col in colors]
            plt.legend(handles, labels)
        sub_bar(self.model_name,new_score)
        plt.show()
        pass
            
        
    def chart(self, score):
        plt.close('all')
        labels = []
        data = []
        for k in range(len(self.filenames)):
            data.append(self.results[k][score][1])
            for i in range(len(self.pp_names[k])):
                labels.append(f'{self.filenames[k]} ({self.pp_names[k][i]})')
        plt.title(['AUC','F1 score','False Positive Rate','False Negative Rate'][score])
        plt.ylim(0,1)
        self.create_bars(data,labels)
    
    def back(self):
        self.frame_main.destroy()
        self.backbutton.destroy()
        interface.home.Home(self.root)

#====================( Main )====================
if __name__=='__main__':
    root = Tk()
    sm = Result(root, [])
    root.mainloop()
