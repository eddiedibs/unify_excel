#!/home/edd1e/Desktop/stuff/work/programming_work/python_work/unify_excel/venv_unifyE/bin/python

# _________________________________________________________________________


#                             SETINGS FILE

# _________________________________________________________________________

import os
from pathlib import Path





root_path = Path(__file__).resolve().parent

excel_files_path = f'{root_path}/excel_files/regiones'


document_columns = ["Clave", "CEDULA O RIF", "Nombre de cliente", "Cuenta Contrato", "Actividad Economica", "CNAE", 
"Direccion Prestacion de Servicio", "Persona Contacto", "Municipio", "Tipo de Pago", "Tipo de Gestion", "Primary Phone", 
"Secondary Phone",  "Telefono 3", "TEL REPRESENTANTE", "Primary Email", "Secondary Email", "Organization Name", 
"Campaña", "Deuda Total", "Estatus de Campaña", "Lote", "Agrupado", "Telefono 4", "Tipo de Cliente", "Telefono Alt. 1", 
"Telefono Alt. 2", "Email Alt.1", "Email Alt.2", "FECHA DE MODIFICACION", "Last Modified By", "Turno", "Turno New"]

duplicates_path = f'{root_path}/excel_files/regiones/duplicados'
curated_duplicates_path = f'{root_path}/excel_files/regiones/duplicados_unificados'

depurated_results = f'{root_path}/excel_files/regiones/depurado'

non_duplicates_path = f'{root_path}/excel_files/regiones/no_duplicados'

united_depurated_path = f'{root_path}/excel_files/completos_unificados'


















