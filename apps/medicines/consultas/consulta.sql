SELECT M.medicine_name AS 'NOMBRE DEL MEDICAMENTO', 
M.description AS 'DESCRIPCION DEL MEDICAMENTO',
H.brand AS 'MARCA',
H.cost_price AS 'PRECIO DE COSTO',
HI.sale_price AS 'PRECIO DE VENTA',
HI.quantity_stock AS 'CANTIDAD',
P.presentation_type AS 'TIPO DE PRESENTACION',
H.expiration_date AS 'FECHA DE VENCIMIENTO',
FA.type_adminstrationform AS 'FORMA DE ADMINISTRACION', 
UT.type_therepeuticuse AS 'USO TERAPEUTICO',
H.medication_code AS 'CODIGO DE MEDICAMENTO',
CONCAT(PR.first_name,' ', IF(PR.last_name != 'NULL', PR.last_name, '') )AS 'NOMBRE DEL PROVEEDOR'
FROM medicines_medicamento M 
INNER JOIN classifications_clasificacion C ON M.id = C.medicine_id_id
INNER JOIN classifications_formaadministracion FA on FA.id = C.formadministration_id_id
INNER JOIN classifications_usoterapeutico UT on UT.id = C.therepeuticuse_id_id
INNER JOIN medicines_historialmedicamento H on M.id = H.medicine_id_id
INNER JOIN presentations_presentacion P on P.id = H.presentation_id_id
INNER JOIN locations_historialinvetario HI on M.id = HI.medicine_id_id
INNER JOIN suppliers_proveedor PR on PR.id = H.supplier_id_id\G;

-- OBTENER TODOS LOS MEDICAMENTOS 

SELECT 
M.id AS 'id',
M.medicine_name AS 'medicamento',
M.description AS 'description',
M.creation_date AS 'fecha_creacion'
FROM medicines_medicamento AS M;

-- OBTENIENDO LA CLASIFICACION DE UN MEDICAMENTO SEGUN SU ID
SELECT 
C.id AS 'classification_id',
F.id AS 'forma_id',
F.type_adminstrationform AS 'forma_administracion',
F.description AS 'description',
U.id AS 'uso_id',
U.type_therepeuticuse AS 'uso_terapeutico',
U.description AS 'description',
C.medicine_id_id AS 'medicine_id'
FROM classifications_clasificacion AS C
INNER JOIN classifications_formaadministracion AS F ON F.id = C.formadministration_id_id
INNER JOIN classifications_usoterapeutico AS U ON U.id = C.therepeuticuse_id_id
WHERE C.medicine_id_id = 1;

-- OBTENER EL HISTORIAL DEL MEDICAMENTO SEGUN SU ID
SELECT 
H.id AS 'historial_id',
P.id AS 'supplier_id',
P.first_name,
P.last_name,
P.company,
P.telephone,
P.email,
PR.id AS 'presentation_id',
PR.presentation_type,
PR.description,
H.cost_price,
H.brand,
H.medication_code,
H.expiration_date
FROM medicines_historialmedicamento AS H
INNER JOIN suppliers_proveedor AS P ON P.id = H.supplier_id_id
INNER JOIN presentations_presentacion AS PR ON PR.id = H.presentation_id_id
WHERE H.medicine_id_id = 1;

-- OBTENER EL HISTORIAL DEL INVETARIO SEGUN SU ID

SELECT 
HI.id AS 'historial_invetario_id',
S.id AS 'seccion_id',
S.location_section,
U.id as 'ubicacion_id',
U.type_location,
HI.quantity_stock,
HI.row,
HI.column,
HI.sale_price,
HI.medicine_id_id
FROM locations_historialinvetario AS HI
INNER JOIN locations_seccion AS S ON S.id = HI.locationsection_id_id
INNER JOIN locations_ubicacion AS U ON U.id = HI.location_id_id;
WHERE HI.medicine_id_id = 1;