# Odooexamen

Jancarlos Antonio Velasquez Soto
0715200500242

Parte 1 y 2

<img width="1876" height="880" alt="Screenshot 2026-11-13 183906" src="https://github.com/user-attachments/assets/88a4a10f-66b2-49c3-9b95-bc8c2dc5db79" />


<img width="1912" height="788" alt="Screenshot 2026-11-13 181545" src="https://github.com/user-attachments/assets/2d23bd53-2d57-4073-b1f3-a554b5292686" />



¿Qué diferencia hay entre _name y _inherit? ¿Por qué tienda.convenio necesita el archivo ir.access.csv y res.partner no?

bueno en Odoo, cada modelo necesita reglas que digan qué grupos de usuarios pueden leer, crear, modificar o borrar sus registros. Si un modelo no tiene ninguna regla de acceso, los usuarios normales no pueden usarlo, _name define un modelo nuevo Odoo crea una tabla propia en la base de datos (tienda_convenio) y registra el modelo tiendaconvenio en el caso de TiendaConvenio, inherit extiende un modelo que ya existe. Si se usa solo, sin _name, no se crea ninguna tabla.
que si tiendaconvenio si lo necesita el archivo ir.access.csv y res.partner no.



