#!/home/edd1e/Desktop/stuff/work/programming_work/python_work/unify_excel/venv_unifyE/bin/python

import settings as s
import functionss as func

import argparse
import subprocess 


class module_prompt:

    def __init__(self):
        pass

    @classmethod
    def prompt_listener(cls):

        p = argparse.ArgumentParser(
            prog="unify_excel",
            description="Handle Excel files and some more...")
        p.add_argument("-d", "--divide", metavar='<input_file>', type=str, help='Divide an excel file into a duplicates dataframe, and one without duplicate.')
        p.add_argument("-m", "--merge", metavar='', type=str, help='Merges both duplicate and non-duplicate excel files into one.')
        p.add_argument("-l", "--list", metavar='[exf, dup, nondup]', type=str, help='Lists document files.')
        args = p.parse_args()



        try:

            if args.divide:

                # print(s.root_path)
                driver = func.document_handling(document_name=f"{args.divide}", 
                            document_columns=s.document_columns)
                driver.export_df_data(input_file_name=args.divide,
                                    path_to_duplicates=f"{s.duplicates_path}/{args.divide.split('.xlsx')[0]}_duplicados.xlsx",
                                    path_to_non_duplicates=f"{s.non_duplicates_path}/{args.divide.split('.xlsx')[0]}_no_duplicados.xlsx")

            elif args.merge:

                driver = func.document_handling(document_name=f"{args.merge}", 
                            document_columns=s.document_columns)

                driver.import_df_data(path_of_curated_duplicates=f"{s.curated_duplicates_path}/{args.merge.split('.xlsx')[0]}_duplicados_depurados.xlsx",
                        path_of_non_duplicates=f"{s.non_duplicates_path}/{args.merge.split('.xlsx')[0]}_no_duplicados.xlsx")



            elif args.list == 'exf':
                list_process = subprocess.run(f'ls {s.excel_files_path}', shell=True)

            elif args.list == 'nondup':
                list_process = subprocess.run(f'ls {s.non_duplicates_path}', shell=True)


            elif args.list == 'dup':
                list_process = subprocess.run(f'ls {s.duplicates_path}', shell=True)





        except KeyboardInterrupt:
            print(f"[USER HAS EXITED]\n")

        except FileNotFoundError as FileErr:
            print(f"[NO SUCH FILE OR DIRECTORY] {FileErr}\n")


if __name__ == '__main__':
    module_prompt().prompt_listener()





