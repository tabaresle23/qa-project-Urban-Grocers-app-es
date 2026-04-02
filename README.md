# Proyecto Urban Grocers

## Descripción del Proyecto
En este proyecto se diseñó y ejecutó un framework de pruebas para la API de la aplicación Urban.Grocers. El objetivo principal fue validar la lógica de negocio de las nuevas funciones del backend, asegurando la integridad de los datos y el correcto funcionamiento de los flujos críticos de la plataforma.

## Tecnologías Utilizadas
- Postman: Para el diseño y ejecución de la colección de pruebas de API.
- JavaScript: Para la creación de scripts de validación (tests) dentro de Postman.
- SQL: Para la validación de la persistencia de datos en el backend.
-Jira: Para la gestión de defectos e informes de incidencias.

## Funcionalidades Probadas
- Gestión de Carritos: Validación de la creación y actualización de carritos de compras.
- Catálogo de Productos: Consulta de disponibilidad y filtrado de productos.
- Perfil de Usuario: Actualización de datos del cliente y validación de sesiones.
-Logística de Envío: Verificación del cálculo de tarifas y tiempos de entrega.
- Integridad de Base de Datos: Validación de registros mediante consultas SQL directas.
 
## Cómo Ejecutar las Pruebas
- Importar Colección: Descargar el archivo JSON de la colección y el entorno (environment) e importarlos en Postman.
- Configurar URL: Actualizar la variable de entorno baseUrl con la dirección del servidor activo.
- Ejecutar Pruebas: Iniciar el "Collection Runner" de Postman para ejecutar todos los tests de forma secuencial.
- Verificar Resultados: Revisar la pestaña de "Test Results" para confirmar el estado de las aserciones (Status Codes, JSON Schema, Response Time).

Autor
Luis E. Tabares H.
