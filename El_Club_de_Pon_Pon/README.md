# El Club de Pon Pon — Visual Studio Code

## Abrir y ejecutar

1. Extrae todo el ZIP.
2. En VS Code selecciona Archivo → Abrir carpeta y abre El_Club_de_Pon_Pon.
3. Instala Node.js 20 o superior si no lo tienes.
4. Abre Terminal → Nueva terminal y ejecuta:

```sh
npm start
```

5. Abre http://localhost:3000 en tu navegador. Para detenerlo, presiona Ctrl+C.

No requiere npm install. También puedes presionar F5 con la configuración incluida. Alternativa: abrir dist/index.html con Live Server. No abras index.html con doble clic: los módulos JavaScript necesitan servidor local.

## Incluye

- Roles Administrador, Ventas y Logística con navegación restringida.
- Catálogo visual, búsqueda, categorías y disponibilidad.
- Crear y editar clientes.
- Cotizaciones con varios productos e imágenes.
- Anticipos, reservas y validación de traslapes.
- Pagos parciales, saldo restante, liquidación e historial, incluso tras despacho o retorno.
- Hojas de eventos con animadores individuales y chofer separado.
- Entradas y salidas con estados, observaciones y hojas PDF.
- Mantenimiento e incidencias graves separados.
- Altas, ajustes y bajas reversibles de productos con motivo en bitácora.
- Reportes, bitácora y cuentas de prueba.

## Archivos

- dist/index.html: página principal.
- dist/app.js: interfaz y eventos.
- dist/core.js: reglas, permisos y datos de ejemplo.
- dist/style.css: diseño.
- dist/movement-pdf.js: hojas PDF.
- dist/pdf-fonts.js y PDF-FONT-LICENSE.txt: fuentes incluidas y licencia.
- server.mjs: servidor local sin dependencias.
- tests/flows.test.mjs: pruebas funcionales.
- scripts/prepare-pdf-fonts.py: regeneración opcional de fuentes; no se necesita para ejecutar. Requiere Python, fontTools y fuentes DejaVu en Linux.

## Pruebas

```sh
npm test
```

Los PDF de prueba se crean en test-output/. Las pruebas no modifican los datos del navegador.

## Datos y alcance

Es el prototipo completo de la última versión. Los roles e inicio de sesión son simulados; los datos se guardan en localStorage de cada navegador. No incluye PostgreSQL, API Express ni autenticación real. Los registros que hayas creado en el sitio alojado no se transfieren a localhost: se inicia con datos de ejemplo. Usa siempre el mismo puerto y dirección para conservar tus datos locales.

El servidor escucha solo en tu computadora (127.0.0.1). La protección de acceso privado de Sites no se traslada como autenticación al ZIP. Para producción se requiere autenticación y autorización en servidor, API y base de datos.

Fuente exportada: bc322f9232a337bc77d4e74c5ebe9dc2c98db49a. No contiene credenciales, configuración de alojamiento ni historial Git.
