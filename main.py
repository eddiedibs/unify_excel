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
        p.add_argument("-d", "--divide", metavar='<input_file>', type=str, help='Divide an excel file into one duplicates dataframe, and another one without duplicate.')
        p.add_argument("-m", "--merge", metavar='', type=str, help='Merges both duplicate and non-duplicate excel files into one.')
        p.add_argument("-aS", "--add-sheets", nargs=3, metavar='', type=str, help='Adds all files in the specified path into sheets for one document [xlsxs=, res_path=, f_name=]')
        p.add_argument("-cD", "--concat-docs", nargs=3, metavar='', type=str, help='Adds all files in the specified path into one whole document [xlsxs=, res_path=, f_name=]')
        p.add_argument("-l", "--list", metavar='[exf, dup, nondup]', choices=['exf', 'dup', 'nondup'], type=str, help='Lists document files.')
        args = p.parse_args()



        try:

            if args.divide:

                file_name = args.divide.split('/')[-1]

                driver = func.document_handling(document_name=f"{args.divide}", 
                            document_columns=s.document_columns)
                driver.export_df_data(path_to_duplicates=f"{s.duplicates_path}/{file_name.split('.xlsx')[0]}_duplicados.xlsx",
                                    path_to_non_duplicates=f"{s.non_duplicates_path}/{file_name.split('.xlsx')[0]}_no_duplicados.xlsx")

            elif args.merge:

                file_name = args.divide.split('/')[-1]

                driver = func.document_handling(document_name=f"{args.merge}", 
                            document_columns=s.document_columns)

                driver.import_df_data(path_of_curated_duplicates=f"{s.curated_duplicates_path}/{file_name.split('.xlsx')[0]}_duplicados_depurados.xlsx",
                        path_of_non_duplicates=f"{s.non_duplicates_path}/{file_name.split('.xlsx')[0]}_no_duplicados.xlsx")



            elif args.list == 'exf':
                list_process = subprocess.run(f'ls {s.excel_files_path}', shell=True)

            elif args.list == 'nondup':
                list_process = subprocess.run(f'ls {s.non_duplicates_path}', shell=True)


            elif args.list == 'dup':
                list_process = subprocess.run(f'ls {s.duplicates_path}', shell=True)


            elif args.add_sheets:


                if args.add_sheets[0].split("=")[0] == 'xlsxs' and args.add_sheets[1].split("=")[0] == 'res_path' and args.add_sheets[2].split("=")[0] == 'f_name':
                    driver = func.unify_files()

                    opt_args = {'xlsxs_path': args.add_sheets[0].split("=")[1],
                                'res_path': args.add_sheets[1].split("=")[1],
                                'f_name': args.add_sheets[2].split("=")[1]}



                    driver.concat_files(opt_args.get("xlsxs_path"), opt_args.get("res_path"), opt_args.get("f_name"), 'concat_sheet')
        

            elif args.concat_docs:

                if args.concat_docs[0].split("=")[0] == 'xlsxs' and args.concat_docs[1].split("=")[0] == 'res_path' and args.concat_docs[2].split("=")[0] == 'f_name':
                    driver = func.unify_files()

                    opt_args = {'xlsxs_path': args.concat_docs[0].split("=")[1],
                                'res_path': args.concat_docs[1].split("=")[1],
                                'f_name': args.concat_docs[2].split("=")[1]}



                    driver.concat_files(opt_args.get("xlsxs_path"), opt_args.get("res_path"), opt_args.get("f_name"), 'concat_whole')



        except KeyboardInterrupt:
            print(f"[USER HAS EXITED]\n")

        except FileNotFoundError as FileErr:
            print(f"[NO SUCH FILE OR DIRECTORY] {FileErr}\n")


        except IndexError:
            print(dir(IndexError.with_traceback))


if __name__ == '__main__':
    module_prompt().prompt_listener()





