# ICC-pto100


El archivo README.md en un proyecto Django es una excelente manera de proporcionar información sobre el proyecto, cómo configurarlo, ejecutarlo y cualquier otro detalle relevante para los desarrolladores que colaboran en el proyecto. Aquí tienes un ejemplo de cómo podría verse un archivo README.md típico para un proyecto Django:


Descripción corta del proyecto y su propósito.

## Configuración

### Requisitos Previos
- Python 3.10.12
- Django 5.0.4
- Postgres
- Docker 20.10.21
- Docker Compose 2.26.1
- Guinicorn
- Nginx

### Instalación de Dependencias y Despliegue de la app
1. Clona este repositorio.
	
	- git clone https://github.com/AlecoG/ICC-pto100.git
	
2. Abre la consola en la raíz del proyecto y despligar en servicio docker:

	- docker-compose up -d

3. Configurar :

	- sudo apt install nginx                             --> instalar nginx bare-metal en el server
	
	- cp nginx/certs/ /etc/nginx/                        --> copiar los certificados pata https (es un autofirmado)
	
	- verificar los permisos de los certificados
   	
   	- cp nginx/icc.conf /etc/nginx/conf.d		    --> copiar configuracion del nginx
   	
   	- systemctl enable nginx                            --> habilitar el nginx y reiniciarlo para que cargue la configuración
   	
   	- systemctl restart nginx
   	
   	  
### Configuración de la Base de Datos   -->(Esto va por ROBERTO)
1. Configura las variables de entorno para la base de datos en settings.py.
2. Ejecuta las migraciones:
   bash
   python manage.py migrate
   
## Ejecución

Para iniciar el servidor en producción solo hay que abrir consola en la raíz del proyecto, ejecuta el siguiente comando:
	
	bash
	-docker-compose up -d

Accede a la aplicación en tu navegador web en https://sgicp100.das.cb

	-docker-compose down para apagar el servicio
	
## Contribuciones

Si deseas contribuir al proyecto, sigue estos pasos:
1. Haz un fork del repositorio.
2. Crea una nueva rama para tu función o corrección de errores.
3. Envía un pull request para revisión.

## Licencia

Este proyecto está licenciado bajo la [Licencia XYZ]. Puedes consultar el archivo LICENSE para más detalles.


