#!/home/edd1e/Desktop/stuff/work/programming_work/python_work/unify_excel/venv_unifyE/bin/python

from audioop import mul
from hashlib import new
import settings as s
import multiprocessing
import ast


# from openpyxl import load_workbook
import openpyxl
import xlsxwriter
import pandas as pd



# class document_handling:

#     def __init__(self):
#         pass


#     def 

excel_document = f"{s.excel_files_path}{s.document_files.get('unificacion')}"


document_names = ["Clave", "CEDULA O RIF", "Nombre de cliente", "Cuenta Contrato", "Actividad Economica", "CNAE", 
"Direccion Prestacion de Servicio", "Persona Contacto", "Municipio", "Tipo de Pago", "Tipo de Gestion", "Primary Phone", 
"Secondary Phone",  "Telefono 3", "TEL REPRESENTANTE", "Primary Email", "Secondary Email", "Organization Name", 
"Campaña", "Deuda Total", "Estatus de Campaña", "Lote", "Agrupado", "Telefono 4", "Tipo de Cliente", "Telefono Alt. 1", 
"Telefono Alt. 2", "Email Alt.1", "Email Alt.2", "FECHA DE MODIFICACION", "Last Modified By", "Turno", "Turno New"]


book = pd.read_excel(excel_document, sheet_name="maneiro")
# book2 = pd.read_table(excel_document, sheet_name="iribarren", names=document_names)


# book_to_modify = book.to_dict()
cedula_col = book.iloc[:, 1]


amount_of_duplicates = book.iloc[:, 1].duplicated(keep=False).sum()
# duplicates = book.iloc[:, 1].duplicated(keep='first')
book_with_only_cedula_duplicates = book.iloc[:, 1].duplicated(keep=False)

# vals = [v for k, v in book.iloc[:, 1].to_dict().items()]
duplicated_row_ids = [k for k, v in book_with_only_cedula_duplicates.to_dict().items() if v == True]

book_with_no_cedula_duplicates = book.drop_duplicates(subset="CEDULA O RIF", keep=False)


path_to_non_duplicates = 'non_duplicates.xlsx'
book_with_no_cedula_duplicates.to_excel(path_to_non_duplicates, index=False)


amount_of_rows = len(book.iloc[duplicated_row_ids])
# for i in range(0, amount_of_rows):
#     print(book.iloc[duplicated_row_ids[i]])

def get_duplicated_df_data():

    column = []
    for row in range(0, amount_of_rows):
        inserted_row = []
        for col in book.iloc[duplicated_row_ids[row]]:
            inserted_row.append(col)

        column.append(inserted_row)

    return column

df_with_duplicated_rows = pd.DataFrame(data=get_duplicated_df_data(), columns=document_names)

cedula_list = []
for index, cedula in enumerate(df_with_duplicated_rows.iloc[:, 1]):
    cedula_list.append(cedula)
    # print(index, cedula)

# print(f"[THE LIST BEFORE REMOVING DUPLICATES IS]...\n{cedula_list}\n\n")
cedula_list = list(set(cedula_list)) 
# print(f"[THE LIST AFTER REMOVING DUPLICATES IS]...\n{cedula_list}\n\n")


def get_cleaned_data_to_df(data_to_dataframe):


    cleaned_data = pd.DataFrame(data=get_duplicated_df_data(), columns=document_names)
    return cleaned_data



def check_row_columns(cedula):
    # duplicated_cedula_row = df_with_duplicated_rows.loc[df_with_duplicated_rows[:, 1] == cedula]
    duplicated_cedula_row = df_with_duplicated_rows.loc[df_with_duplicated_rows.iloc[:, 1] == cedula]
    # print(f"[LAS COLUMNAS DE LA FILA DE CEDULA {cedula} VAN A SER PROCESADAS] Chequeando...\n")
    # print(duplicated_cedula_row.iloc[:, 11])
    # for item in document_names:
    #     get_cleaned_data_to_df(duplicated_cedula_row.to_dict().get(item))
    for item in document_names:
        if item != ''
        list_of_cleaned_values = [v for k, v in duplicated_cedula_row.to_dict().get(item).items()]
        get_cleaned_data_to_df(list_of_cleaned_values)



# def get_row_index(dataframe, value):
#     row_position = [k for k, v in dataframe.to_dict().items() if v == value]
#     return row_position

def find_duplicated_rows():
    for i in range(0, len(cedula_list)):
        for index, cedula in enumerate(df_with_duplicated_rows.iloc[:, 1]):
            if cedula == cedula_list[i]:
                print(f"[{cedula} is EQUAL to {cedula_list[i]}] checking columns...\n")
                check_row_columns(df_with_duplicated_rows.iloc[:, 1][index])
                break
            elif cedula != cedula_list[i]:
                print(f"[{cedula} is NOT equal to {cedula_list[i]}] Next Cedula...\n")



find_duplicated_rows()

# print(df_with_duplicated_rows.iloc[:, 1])


# path_to_duplicates = 'duplicates.xlsx'
# df.to_excel(path_to_duplicates, index=False)





# print(duplicates)
# final_keys = list(map(lambda x: x+2, duplicated_row_ids))
# print(final_keys)   

# first_row = book.loc[duplicated_row_ids[0]]
# sec_col = book.iloc[duplicated_row_ids[0]]

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
    


    

