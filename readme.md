# Proyecto de Conversión de Divisas

## Juan Camilo Ramírez Rátiva - 20181020089
### Universidad Distrital Francisco José de Caldas

Este proyecto es un servicio de conversión de divisas construido con Flask, SQLAlchemy y SQLite.

## Cómo ejecutar el proyecto

1. **Clonar el repositorio**
    ```
    git clone https://github.com/your-repository-url
    ```

2. **Crear un entorno virtual (opcional)**
    ```
    python3 -m venv venv
    source venv/bin/activate  # En Windows, usa `venv\Scripts\activate`
    ```

3. **Instalar las dependencias**
    ```
    pip install -r requirements.txt
    ```

4. **Establecer la variable de entorno FLASK_APP**
    ```
    export FLASK_APP=app.py  # En Windows, usa `set FLASK_APP=app.py`
    ```

5. **Ejecutar las migraciones de la base de datos**
    ```
    flask db upgrade
    ```

6. **Ejecutar la aplicación**
    ```
    flask run
    ```

Ahora puedes acceder a la aplicación en tu navegador en `http://localhost:5000`.

## Endpoints

- `/currency`: Permite añadir una nueva moneda a la base de datos o obtener los detalles de una moneda específica.
- `/exchange_rate`: Permite añadir una nueva tasa de cambio a la base de datos o obtener los detalles de una tasa de cambio específica.
- `/convert`: Convierte una cantidad de una moneda a varias otras monedas.

Para más detalles sobre estos endpoints, consulta la documentación de la API en Swagger UI en `http://localhost:5000/api/docs`.

¡Espero que disfrutes del proyecto! Si tienes alguna pregunta o sugerencia, no dudes en ponerse en contacto.
