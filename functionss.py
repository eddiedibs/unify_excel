#!/home/edd1e/Desktop/stuff/work/programming_work/python_work/unify_excel/venv_unifyE/bin/python

import settings as s
import multiprocessing
import ast
import re

import openpyxl
import xlsxwriter
import pandas as pd




class document_handling:

    def __init__(self, document_name:str, document_columns:list, sheet_name:str=None, document_path:str=f"{s.excel_files_path}/"):
        
        
        self.document_name = document_name
        self.excel_document = f"{document_path}{document_name}"
        self.book = pd.read_excel(f'{self.excel_document}')
        self.document_columns = document_columns





    def get_duplicated_df_data(self):
        cedula_column = self.book.iloc[:, 1]
        book_with_only_cedula_duplicates = cedula_column.duplicated(keep=False)
        duplicated_row_ids = [k for k, v in book_with_only_cedula_duplicates.to_dict().items() if v == True]
        amount_of_rows = len(self.book.iloc[duplicated_row_ids])

        column = []
        for row in range(0, amount_of_rows):
            inserted_row = []
            for col in self.book.iloc[duplicated_row_ids[row]]:
                inserted_row.append(col)

            column.append(inserted_row)

        return column


    def export_df_data(self, path_to_duplicates, path_to_non_duplicates, input_file_name):


       

        print(f"[EXPORTING DATAFRAMES FROM INPUT FILE '{input_file_name}']...\n [FILE LOCATED AT '{self.excel_document}']\n\n\n")

        df_with_duplicated_rows = pd.DataFrame(data=self.get_duplicated_df_data(), columns=self.document_columns)
        df_with_duplicated_rows.to_excel(path_to_duplicates, index=False)
        print(f"[DATAFRAME WITH DUPLICATED ROWS HAS BEEN CREATED AND EXPORTED TO {path_to_duplicates}]\n")

        book_with_only_cedula_duplicates = self.book.iloc[:, 1].duplicated(keep=False)

        duplicated_row_ids = [k for k, v in book_with_only_cedula_duplicates.to_dict().items() if v == True]
        
        cedulas_column_name = self.book.columns[1]

        book_with_no_cedula_duplicates = self.book.drop_duplicates(subset=f"{cedulas_column_name}", keep=False)


        book_with_no_cedula_duplicates.to_excel(path_to_non_duplicates, index=False)
        print(f"[DATAFRAME WITH NON-DUPLICATED ROWS HAS BEEN CREATED AND EXPORTED TO {path_to_non_duplicates}]\n")




    def import_df_data(self, path_of_curated_duplicates, path_of_non_duplicates):
        
      
        is_file_extension = re.search(".xlsx", self.document_name) 

        if is_file_extension:

            pass
        
        else:
            self.document_name = f"{self.document_name}.xlsx"
      
      
        print("[READING DATAFRAMES] ...\n")
        curated_duplicates_file = pd.read_excel(f'{path_of_curated_duplicates}')
        to_merge_file = pd.read_excel(f'{path_of_non_duplicates}')
        curated_duplicates_file.columns = s.document_columns
        to_merge_file.columns = s.document_columns


        print("[PROCEDING TO MERGE DATAFRAMES] ...\n")
        result_file = pd.concat([curated_duplicates_file, to_merge_file], sort=False)

        result_file_path = f"{s.excel_files_path}/result_{self.document_name}"

        result_file.to_excel(result_file_path, index=False)

        print("[MERGING COMPLETED!] ...\n")
        



if __name__ == '__main__':
    obj_1 = document_handling(document_path=f"{s.excel_files_path}/",
                            document_name="test.xlsx", 
                            document_columns=s.document_columns)
    
    # obj_1.export_df_data(path_to_duplicates=f"{s.duplicates_path}/chacao_duplicados.xlsx",
    #                      path_to_non_duplicates=f"{s.non_duplicates_path}/chacao_no_duplicados.xlsx")
    
    obj_1.import_df_data(path_of_curated_duplicates=f"{s.curated_duplicates_path}/test_duplicados_depurados.xlsx",
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
#     if cedula_column[index] == cedula:
#         print(f"{cedula_column[index]} ES IGUAL A {cedula}")
#         file.close()
#         return True

#     else:
#         print(f"{cedula_column[index]} NO ES IGUAL A {cedula}")
#         file.close()
#         return False




# if __name__ == '__main__':
#     count = 0
#     for entry in range(len(cedula_column)):
#         file = open('text.tmp', 'w')
#         file.write(cedula_column[entry])
#         print("[LA CEDULA HA SIDO ESCRITA] Chequeando...\n")
#         file.close()

#         p = multiprocessing.Pool()
#         result = p.map(checkID, range(0, len(list(cedula_column))))

#         with open('text.tmp', 'r') as f:
#             print(f'[EL PROCESO HA ACABADO USANDO LA CEDULA {f.readline()}]\n\n')
#         count += int(result.count(True))
#     print(f"[SE HAN ENCONTRADO {count} ENTRADAS DUPLICADAS]")
    


    

