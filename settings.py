#!/home/edd1e/Desktop/stuff/work/programming_work/python_work/unify_excel/venv_unifyE/bin/python

# _________________________________________________________________________


#                             SETINGS FILE

# _________________________________________________________________________

import os
from pathlib import Path





root_path = Path(__file__).resolve().parent

excel_files_path = f'{root_path}/excel_files'


# document_columns = ["Clave", "CEDULA O RIF", "Nombre de cliente", "Cuenta Contrato", "Actividad Economica", "CNAE", 
# "Direccion Prestacion de Servicio", "Persona Contacto", "Municipio", "Tipo de Pago", "Tipo de Gestion", "Primary Phone", 
# "Secondary Phone",  "Telefono 3", "TEL REPRESENTANTE", "Primary Email", "Secondary Email", "Organization Name", 
# "Campaña", "Deuda Total", "Estatus de Campaña", "Lote", "Agrupado", "Telefono 4", "Tipo de Cliente", "Telefono Alt. 1", 
# "Telefono Alt. 2", "Email Alt.1", "Email Alt.2", "FECHA DE MODIFICACION", "Last Modified By", "Turno", "Turno New"]

# document_columns = ["CLAVE", "CEDULA O RIF", "NOMBRE DEL CLIENTE", "CUENTA CONTRATO", "ACTIVIDAD ECONÓMICA", "CNAE", 
# "DIRECCIÓN PRESTACIÓN DE SERVICIO", "PERSONA CONTÁCTO", "MUNICIPIO", "TIPO DE PAGO", "TIPO DE GESTIÓN", "PRIMER TELÉFONO", 
# "SEGUNDO TELÉFONO",  "TERCER TELÉFONO", "TEL REPRESENTANTE", "PRIMER EMAIL", "SEGUNDO EMAIL", "NOMBRE DE ORGANIZACIÓN", 
# "CAMPAÑA", "DEUDA TOTAL", "ESTATUS DE CAMPAÑA", "LOTE", "AGRUPADO", "CUARTO TELÉFONO ", "TIPO DE CLIENTE", "TELÉFONO ALT. 1", 
# "TELÉFONO ALT. 2", "EMAIL ALT.1", "EMAIL ALT.2", "FECHA DE MODIFICACIÓN", "MODIFICADO POR", "TURNO", "NUEVO TURNO", "NOMBRES",
#  "APELLIDOS", "ACTIVO", "ESPECIAL"]

# document_columns = ["CEDULA O RIF", "NOMBRE DEL CLIENTE", "ACTIVIDAD ECONÓMICA", 
# "DIRECCIÓN PRESTACIÓN DE SERVICIO", "PERSONA CONTÁCTO", "MUNICIPIO", "TIPO DE GESTIÓN", "PRIMER TELÉFONO", 
# "SEGUNDO TELÉFONO",  "TERCER TELÉFONO", "TEL REPRESENTANTE", "PRIMER EMAIL", "SEGUNDO EMAIL", "NOMBRE DE ORGANIZACIÓN",
#  "AGRUPADO", "CUARTO TELÉFONO ", "TIPO DE CLIENTE", "TELÉFONO ALT. 1", 
# "TELÉFONO ALT. 2", "EMAIL ALT.1", "EMAIL ALT.2", "TURNO", "NUEVO TURNO", "NOMBRES",
#  "APELLIDOS", "ACTIVO", "ESPECIAL"]



document_columns = ["RIF", "RAZON SOCIAL", "CEDULA", 
"CUENTA CONTRATO", "ACTIVIDAD ECONOMICA", "CNAE", "DIRECCION PRESTACION DE SERVICIO", "PERSONA CONTACTO", 
"MUNICIPIO",  "TIPO DE PAGO", "TIPO DE GESTION", "TLF 1", "TLF 2", "TLF 3",
 "EMAIL 1", "ACTIVO", "ESPECIAL", "EMAIL 2", 
"ORG NAME", "CAMPAÑA", "DEUDA TOTAL", "ESTATUS DE CAMPAÑA", "LOTE", "AGRUPADO",
 "TELF 4", "TIPO DE CLIENTE", "TLF ALT 1", "TLF ART 2", "EMAIL ART 1", "EMAIL ART 2", "FECHA DE MODIFICACION",
 "LAST MODIFIED BY ", "TURNO", "TURNO NEW"]

duplicates_path = f'{root_path}/excel_files/duplicados'

non_duplicates_path = f'{root_path}/excel_files/no_duplicados'

depurated_duplicates_path = f'{root_path}/excel_files/depurado'

united_duplicates_path = f'{root_path}/excel_files/output'





















