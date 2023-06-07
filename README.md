# Documentación de la API Expedientes JNAF1

Esta es una API REST para interactuar con la base de datos de expedientes publicados por el Juzgado de Niñez, Adolescencia y Familia n° 01. 

Esta API utiliza Flask y SQLAlchemy para interactuar con una base de datos PostgreSQL.

La API se estructura alrededor de dos recursos principales: Expedientes individuales y Listas de expedientes por fecha.

## Requisitos

- Docker y Docker Compose instalados en su sistema.

## Pasos para ejecutar la aplicación

- Clonar el repositorio:

    ```    
    git clone https://github.com/primercado/nao_proyecto_final.git  
    ```


## Crear y configurar Varibles de Entorno

Las variables de entorno son una parte fundamental para la configuración de la aplicación.

Son necesarias para configurar la conexión a la base de datos PostgreSQL.

Para configurar las variables de entorno:

- Navegar al directorio de la aplicación:

    ```
    cd app/  
    ```

- En el directorio cree un archivo .env.

- Abra el archivo .env y defina las siguientes variables con sus propios valores:

    
    ```
    POSTGRES_USER= usuario
    POSTGRES_PASSWORD= password
    POSTGRES_DB= nombre_base_datos
    SQLALCHEMY_DATABASE_URI=postgresql://usuario:password@db:5432/nombre_base_datos
    ```



- Guarde y cierre el archivo .env.

En su aplicación, puede acceder a estas variables de entorno usando os.environ.get.

## Archivo .env.prueba

Para ayudarle a entender mejor, aquí tiene un ejemplo de cómo debería verse un archivo .env.prueba. Esta es una versión de prueba del archivo .env con datos ficticios. No debe usar estos valores en su configuración real.


    ```
    POSTGRES_USER= usuario
    POSTGRES_PASSWORD= contrasena
    POSTGRES_DB= bbdd_prueba
    SQLALCHEMY_DATABASE_URI= postgresql://usuario:contrasenad@db:5432/bbdd_prueba
    ```
    
Tenga en cuenta que el archivo .env.prueba es solo un ejemplo. Debe crear su propio archivo .env con sus propias variables de entorno para su configuración específica.


## Construir y levantar la aplicación con Docker Compose:

- Dirígite al directorio app/ y ejecuta:

docker-compose up --build

Nota: La opción --build se utiliza para construir las imágenes antes de iniciar los contenedores. Solo es necesario hacerlo la primera vez que se inicia la aplicación o cuando se han realizado cambios en el código.

Una vez que los contenedores están en funcionamiento, puedes acceder a la aplicación en http://localhost:5000.

- Para ejecutarla luego, solo debes ubicarte en el directorio app/ y ejecutar el siguiente código y acceder a la aplicación en http://localhost:5000

docker-compose up


## Endpoints de la API

### /expediente/<expte>

Este endpoint te permite obtener la información de un expediente en particular.

- **URL:** /expediente/<expte>
- **Método:** GET
- **URL Params:** `expte` - El número del expediente, con las barras ("/") reemplazadas por guiones ("-").
- **Ejemplo:** `/expediente/999-17`
- **Respuesta de éxito:**
    - **Código:** 200
    - **Contenido:**
    
    ```
    `[ { "Fecha": "fecha", "Orden": "orden", }, ...]`
    ```
    
- **Respuesta de error:**
    - **Código:** 404
    - **Contenido:** `{"mensaje": "Expediente no encontrado"}`

### /expedientes/<fecha>

Este endpoint te permite obtener una lista de todos los expedientes para una fecha en particular.

- **URL:** /expedientes/<fecha>
- **Método:** GET
- **URL Params:** `fecha` - La fecha, con las barras ("/") reemplazadas por guiones ("-").
- **Ejemplo:** `/expedientes/05-06-2023`
- **Respuesta de éxito:**
    - **Código:** 200
    - **Contenido:**
    
       
- `[ { "Orden": "orden", "Expediente": "expediente", "Caratula": "caratula", }, ...]`

- **Respuesta de error:**
    - **Código:** 404
    - **Contenido:** `{"mensaje": "No se encontraron expedientes para esta fecha"}`

---

# Documentación de la Interacción con la Base de Datos

Esta API utiliza SQLAlchemy, un ORM (Object-Relational Mapper) para Python, para interactuar con una base de datos PostgreSQL.

## Configuración de la Base de Datos

La configuración de la base de datos se encuentra en `config.py`:

`SQLALCHEMY_DATABASE_URI` es la URI de la base de datos que se utilizará para conectarse a PostgreSQL. `SQLALCHEMY_TRACK_MODIFICATIONS` se establece en `False` para desactivar las notificaciones de cambio de SQLAlchemy, que no son necesarias para esta aplicación.

## Modelo de la Base de Datos

No se utiliza un modelo explícito de SQLAlchemy en esta aplicación, sino que se interactúa directamente con la base de datos utilizando consultas SQL.

## Interacción con la Base de Datos

Las interacciones con la base de datos ocurren en las funciones `get_expediente` y `get_expedientes` e `aplicacion.py`. Ambas funciones utilizan la función `execute` de SQLAlchemy para ejecutar consultas SQL en la base de datos.

- `get_expediente` realiza una consulta que selecciona las columnas "Fecha" y "Orden" de la tabla de despachos para un número de expediente específico, ordenado por "Fecha" en orden descendente.
- `get_expedientes` realiza una consulta que selecciona las columnas "Orden", "Expediente" y "Caratula" de la tabla de despachos para una fecha específica.

Ambas funciones procesan el resultado de la consulta y devuelven los datos como un objeto JSON, o un mensaje de error si no se encuentran filas correspondientes.

Espero que esto te sea de ayuda y te proporcione una visión más clara de cómo la aplicación interactúa con la base de datos.
