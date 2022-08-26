#!/home/edd1e/Desktop/stuff/work/programming_work/python_work/unify_excel/venv_unifyE/bin/python

from tempfile import TemporaryFile
import settings as s
import multiprocessing
import os
import ast
import re


import openpyxl
import xlsxwriter
import pandas as pd



class document_handling:

    def __init__(self, document_name:str, document_columns:list, sheet_name:str=None, document_path:str=f"{s.excel_files_path}/"):
        
        
        self.document_name = document_name.split('/')[-1]
        self.excel_document = f"{document_name}"
        self.document_columns = document_columns





    # ========================================================================================


        #Get all duplicated data and return the columns along with their respective rows
   
   
    # ========================================================================================
    
    def get_duplicated_df_data(self, column_id):
        issued_column = self.book.iloc[:, column_id]
        book_with_only_column_duplicates = issued_column.duplicated(keep=False)
        duplicated_row_ids = [k for k, v in book_with_only_column_duplicates.to_dict().items() if v == True]
        amount_of_rows = len(self.book.iloc[duplicated_row_ids])

        column = []
        for row in range(0, amount_of_rows):
            inserted_row = []
            for col in self.book.iloc[duplicated_row_ids[row]]:
                inserted_row.append(col)

            column.append(inserted_row)

        return column

    # ========================================================================================


        # Divide an excel file into one duplicates dataframe, and another one without duplicate.
   
   
    # ========================================================================================
    def export_df_data(self, path_to_duplicates, path_to_non_duplicates, column_id=None):

        self.book = pd.read_excel(f'{self.excel_document}')
       
        print("[SELECT THE KEY COLUMN TO CHECK FOR DUPLICATES]\n")
        for index, col in enumerate(self.book.columns):
            print(f"[{index}] {col}")



        column_id = int(input("\n>>>")) 


        print(f"[EXPORTING DATAFRAMES FROM INPUT FILE '{self.document_name}']...\n [FILE LOCATED AT '{self.excel_document}']\n\n\n")

        df_with_duplicated_rows = pd.DataFrame(data=self.get_duplicated_df_data(column_id), columns=self.document_columns)
        df_with_duplicated_rows.to_excel(path_to_duplicates, index=False)
        print(f"[DATAFRAME WITH DUPLICATED ROWS HAS BEEN CREATED AND EXPORTED TO {path_to_duplicates}]\n")

        book_with_only_column_duplicates = self.book.iloc[:, column_id].duplicated(keep=False)

        duplicated_row_ids = [k for k, v in book_with_only_column_duplicates.to_dict().items() if v == True]
        
        issued_column_name = self.book.columns[column_id]

        book_without_duplicates = self.book.drop_duplicates(subset=f"{issued_column_name}", keep=False)


        book_without_duplicates.to_excel(path_to_non_duplicates, index=False)
        print(f"[DATAFRAME WITH NON-DUPLICATED ROWS HAS BEEN CREATED AND EXPORTED TO {path_to_non_duplicates}]\n")





    # ========================================================================================


        # Curates a specified dataframe from all its duplicates and saves it to a excel file.
   
   
    # ========================================================================================


    def curate_duplicates(self, path_to_curated_file):

        # try:
            
        self.book = pd.read_excel(f'{self.excel_document}')
        
        
        ## REMOVE ALL NaN values from the book
        self.book = self.book.fillna("")
        

        # SELECT RANGE AND CHOOSE KEY COLUMN WITH DUPLICATE RECORDS #
        print("[SELECT RANGE AND CHOOSE KEY COLUMN WITH DUPLICATE RECORDS (please insert values with spaces)]\n")
        for index, col in enumerate(self.book.columns):
            print(f"[{index}] {col}")

        key_column_id = int(input("\n>>>"))



        # CHOOSE KEY COLUMNS WITH VALUES TO MERGE #
        print("[CHOOSE KEY COLUMNS WITH VALUES TO MERGE (please insert values with spaces)]\n")
        for index, col in enumerate(self.book.columns):
            print(f"[{index}] {col}")
        

        key_column = self.book.iloc[:, key_column_id]
        columns_to_merge = input("\n>>>")
        columns_to_merge = columns_to_merge.split()

        columns_to_merge_as_dict = {}
        for col in columns_to_merge:

            # Here we add the column names to the created dictionary (We have to do this in order to pass it to agg())
            columns_to_merge_as_dict.update({f"{self.book.iloc[:, int(col)].name}":list})


        
        ## 
        df_with_curated_values = self.book.groupby(key_column.name,as_index=False).agg(columns_to_merge_as_dict)



        # REMOVER: REMOVE BLANK SPACES, DASHES, and other useless elements
        def char_remover(col_name, char_to_remove):
            for entry in df_with_curated_values[col_name]:

                for index, item in enumerate(entry):

                    if not isinstance(item, int):
                        entry[index] = entry[index].replace(char_to_remove, '')
                
                        if item == '':
                            entry.pop(index)

                        elif item == char_to_remove:
                            entry.pop(index)

        ### Develop a way to only remove certain characters on very specific columns
        ### Such as a TLF columns, and ommit the other columns, and develop a prompt for
        ### whether or not use char_remover()
        for column in columns_to_merge_as_dict:
            char_remover(column, '-')




        ## CURATE COLUMN DUPLICATE VALUES 
        def curate_col(col):

            for index, _ in enumerate(col):
                # print(index)
                col[index] = '|'.join(map(str,col[index]))


       
        for col_index in columns_to_merge:
            curate_col(df_with_curated_values[self.book.iloc[:, int(col_index)].name])



        # print(self.book.iloc[:, 11].name)
        print(df_with_curated_values)


        # for id in columns_to_merge:






        # except Exception as ex:
        #     print(ex)







    # ========================================================================================


        # Merges both curated and non-duplicate excel files into one.
   
   
    # ========================================================================================


    def merge_duplicate_and_nonduplicate(self, path_of_curated_duplicates, path_of_non_duplicates):
        

        
        is_file_extension = re.search(".xlsx", self.document_name) 

        if is_file_extension:

            pass
        
        else:
            self.document_name = f"{self.document_name}.xlsx"
      
      
        print(f"[READING DATAFRAMEs] ...\n[{path_of_curated_duplicates}]\n[{path_of_non_duplicates}]\n")
        curated_duplicates_file = pd.read_excel(f'{path_of_curated_duplicates}')
        to_merge_file = pd.read_excel(f'{path_of_non_duplicates}')
        curated_duplicates_file.columns = s.document_columns
        to_merge_file.columns = s.document_columns


        print(f"[PROCEDING TO MERGE DATAFRAMES to {s.excel_files_path}/result_{self.document_name}] ...\n")
        result_file = pd.concat([curated_duplicates_file, to_merge_file], sort=False)

        result_file_path = f"{s.excel_files_path}/result_{self.document_name}"

        result_file.to_excel(result_file_path, index=False)

        print("[MERGING COMPLETED!] ...\n")




class unify_files:

    def __init__(self):
        pass




    def concat_files(self, path_of_xlsx_files, result_path, name_of_final_document, reason):


        if reason == 'concat_sheet':

            print(f"[UNIFYING ALL XLSX FILES IN '{path_of_xlsx_files}']...\n")
            final_document_path = f"{result_path}/{name_of_final_document}"
            final_document = pd.ExcelWriter(f"{final_document_path}", engine = 'xlsxwriter')
            



            for f in os.listdir(path_of_xlsx_files):
                print("[LISTING ALL VALIDATED XLSX FILES]...\n")
                contains_ext = re.search(".xlsx", f)
                if contains_ext:
                        path_of_sheet = f"{path_of_xlsx_files}/{f}"
                        print(f"[SETTING RESULT FILE AT {path_of_sheet}]...\n")
                        xlsx_file = pd.read_excel(f"{path_of_sheet}")


                        # xlsx_file_name = f.split('.xlsx')[0]
                        # print(f"[SAVING SHEET OF NAME {xlsx_file_name} to {final_document_path}]...\n")
                        # xlsx_file.to_excel(final_document, sheet_name=f"{xlsx_file_name}")

                else:
                    pass
            final_document.save()
            final_document.close()
            

        elif reason == 'concat_whole':


            print(f"[UNIFYING ALL XLSX FILES IN '{path_of_xlsx_files}']...\n")
            final_document_path = f"{result_path}/{name_of_final_document}"
            final_document = pd.ExcelWriter(f"{final_document_path}", engine = 'xlsxwriter')
            

            df = pd.read_excel(f"{path_of_xlsx_files}/Contactos_VTIGER_segmentado.xlsx", None);
            print(df.keys())    

            # for f in os.listdir(path_of_xlsx_files):
            #     print("[LISTING ALL VALIDATED XLSX FILES]...\n")
            #     contains_ext = re.search(".xlsx", f)
            #     if contains_ext:
            #             path_of_sheet = f"{path_of_xlsx_files}/{f}"
            #             print(f"[SETTING RESULT FILE AT {path_of_sheet}]...\n")
            #             xlsx_file = pd.read_excel(f"{path_of_sheet}")


            #             # xlsx_file_name = f.split('.xlsx')[0]
            #             # print(f"[SAVING SHEET OF NAME {xlsx_file_name} to {final_document_path}]...\n")
            #             # xlsx_file.to_excel(final_document, sheet_name=f"{xlsx_file_name}")

            #     else:
            #         pass
            # final_document.save()
            # final_document.close()



if __name__ == '__main__':
    obj_1 = document_handling(document_path=f"{s.excel_files_path}/",
                            document_name="test.xlsx", 
                            document_columns=s.document_columns)
    
    # obj_1.export_df_data(path_to_duplicates=f"{s.duplicates_path}/chacao_duplicados.xlsx",
    #                      path_to_non_duplicates=f"{s.non_duplicates_path}/chacao_no_duplicados.xlsx")
    
    obj_1.merge_duplicate_and_nonduplicate(path_of_curated_duplicates=f"{s.united_duplicates_path}/test_duplicados_depurados.xlsx",
                        path_of_non_duplicates=f"{s.non_duplicates_path}/test_no_duplicados.xlsx")


###########################################
# TO PASS TO 'document_handling' instance:#
###########################################

    # excel_document = f"{s.excel_files_path}{s.document_files.get('unificacion')}"
    # self.book = pd.read_excel('test.xlsx')
    # sheet_name(Optional)




















































######################################################################################################################################################


# def get_cleaned_data_to_df(data_to_dataframe):


#     cleaned_data = pd.DataFrame(data=get_duplicated_df_data(), columns=self.document_columns)
#     return cleaned_data



# def check_row_columns(cedula):
    # duplicated_cedula_row = df_with_duplicated_rows.loc[df_with_duplicated_rows[:, 1] == cedula]
    # duplicated_cedula_row = df_with_duplicated_rows.loc[df_with_duplicated_rows.iloc[:, 1] == cedula]
    # print(f"[LAS COLUMNAS DE LA FILA DE CEDULA {cedula} VAN A SER PROCESADAS] Chequeando...\n")
    # print(duplicated_cedula_row.iloc[:, 11])
    # for item in self.document_columns:
    #     get_cleaned_data_to_df(duplicated_cedula_row.to_dict().get(item))
    # for item in self.document_columns:
    #     if item != ''
    #     list_of_cleaned_values = [v for k, v in duplicated_cedula_row.to_dict().get(item).items()]
    #     get_cleaned_data_to_df(list_of_cleaned_values)



# def get_row_index(dataframe, value):
#     row_position = [k for k, v in dataframe.to_dict().items() if v == value]
#     return row_position

# def find_duplicated_rows():
#     cedula_list = []
#     for index, cedula in enumerate(df_with_duplicated_rows.iloc[:, 1]):
#         cedula_list.append(cedula)

#     cedula_list = list(set(cedula_list)) 

#     for i in range(0, len(cedula_list)):
#         for index, cedula in enumerate(df_with_duplicated_rows.iloc[:, 1]):
#             if cedula == cedula_list[i]:
#                 print(f"[{cedula} is EQUAL to {cedula_list[i]}] checking columns...\n")
#                 check_row_columns(df_with_duplicated_rows.iloc[:, 1][index])
#                 break
#             elif cedula != cedula_list[i]:
#                 print(f"[{cedula} is NOT equal to {cedula_list[i]}] Next Cedula...\n")



# find_duplicated_rows()

# print(df_with_duplicated_rows.iloc[:, 1])


# path_to_duplicates = 'duplicates.xlsx'
# df.to_excel(path_to_duplicates, index=False)





# print(duplicates)
# final_keys = list(map(lambda x: x+2, duplicated_row_ids))
# print(final_keys)   

# first_row = self.book.loc[duplicated_row_ids[0]]
# sec_col = self.book.iloc[duplicated_row_ids[0]]

# print(duplicated_row_ids[0])




# xlwriter = pd.ExcelWriter('severalDFs.xlsx')





# print(duplicates.to_dict())

# c = []
# for i in range(0, amount_of_duplicates):
    
#     if duplicates.loc[i] == True:
#         print(duplicates.loc[i])
#         c.append('1')
#     else:
#         pass    

# print(c.count('1'))



# def checkID(index):
#     file = open('text.tmp', 'r')
#     cedula = file.readline()
#     if issued_column[index] == cedula:
#         print(f"{issued_column[index]} ES IGUAL A {cedula}")
#         file.close()
#         return True

#     else:
#         print(f"{issued_column[index]} NO ES IGUAL A {cedula}")
#         file.close()
#         return False




# if __name__ == '__main__':
#     count = 0
#     for entry in range(len(issued_column)):
#         file = open('text.tmp', 'w')
#         file.write(issued_column[entry])
#         print("[LA CEDULA HA SIDO ESCRITA] Chequeando...\n")
#         file.close()

#         p = multiprocessing.Pool()
#         result = p.map(checkID, range(0, len(list(issued_column))))

#         with open('text.tmp', 'r') as f:
#             print(f'[EL PROCESO HA ACABADO USANDO LA CEDULA {f.readline()}]\n\n')
#         count += int(result.count(True))
#     print(f"[SE HAN ENCONTRADO {count} ENTRADAS DUPLICADAS]")
    


    

