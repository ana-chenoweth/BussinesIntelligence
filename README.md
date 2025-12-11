# Proyecto: BussinesIntelligence

## Descripción General
Este proyecto implementa un agente inteligente capaz de analizar datos transaccionales de la empresa Peiix mediante técnicas de Business Intelligence asistidas por modelos de lenguaje.  
El agente opera dentro de **OpenWebUI**, permitiendo que cualquier usuario interactúe con los datos usando lenguaje natural, sin necesidad de conocimientos de programación.

El agente:
- Carga datos desde un archivo CSV.
- Genera automáticamente código en Pandas.
- Ejecuta ese código mediante una herramienta personalizada.
- Produce análisis, métricas y recomendaciones.

El documento **Reporte.pdf** describe a detalle el proceso, arquitectura y funcionamiento. :contentReference[oaicite:0]{index=0}


## Objetivo
Peiix es una empresa que provee servicios de pago y terminales a negocios. Su reto es analizar transacciones sin contar con un analista o un área dedicada a BI.  

Este proyecto crea un **agente que actúa como analista de negocios**, con capacidades para:
- Explorar los datos.
- Calcular métricas relevantes.
- Identificar patrones y anomalías.
- Generar recomendaciones basadas en evidencia.
- Automatizar análisis repetitivos.

El usuario únicamente formula preguntas en lenguaje natural dentro de OpenWebUI.


## Arquitectura del Sistema
El reporte incluye dos diagramas de arquitectura (página 3) que muestran dos opciones de despliegue:

### External Provider
- El usuario interactúa con OpenWebUI.
- OpenWebUI utiliza un modelo en AWS EC2.
- El modelo accede a APIs externas (OpenAI, Anthropic, Google).

### Self-Hosting
- El usuario interactúa con OpenWebUI.
- El modelo corre localmente (por ejemplo usando Ollama).
- Todo el procesamiento ocurre dentro de la infraestructura del usuario.

Ambas arquitecturas son compatibles con este sistema.  
:contentReference[oaicite:1]{index=1}


## Archivos del Proyecto
```
.
├── datos_sept.csv # Datos transaccionales
├── tool_Acceder_a_los_datos.py # Tool Pandas del agente
├── requirements.txt # Dependencias de Python
├── Makefile # Ejecuta la aplicación con Docker
├── LICENSE # Licencia
├── Reporte.pdf # Reporte del proyecto
└── README.md # Este archivo
```


## Makefile
Este proyecto incluye un Makefile para facilitar la ejecución de la aplicación completa utilizando Docker.

### Contenido del Makefile

```makefile
run:
        sudo docker run -d -p 80:8080 -e WEBUI_AUTH=False -e OPEN_WEBUI_DISABLE_CHAT_TITLE_GENERATION=true -e OPEN_WEBUI_REQUEST_TIMEOUT=600000 -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:main
        sudo docker cp /home/ec2-user/datos/* open-webui:/app/

down:
        sudo docker stop open-webui
        sudo docker rm open-webui

logs:
        sudo docker logs open-webui --tail 100

pull:
        docker pull ghcr.io/open-webui/open-webui:main-slim

```

Explicación de cada comando
`make run`

- Levanta el contenedor de OpenWebUI en modo detach.

- Expone la interfaz en el puerto 80.

- Desactiva autenticación para pruebas internas.

- Monta un volumen persistente.

- Copia los datos desde /home/ec2-user/datos/ al contenedor.

- Deja todo listo para usar el agente.

`make down`

- Detiene y elimina el contenedor open-webui.

`make logs`

-Muestra los últimos 100 logs del contenedor para depuración.

`make pull` 

- Actualiza la imagen de OpenWebUI a la versión más reciente (main-slim).

Herramienta: `tool_Acceder_a_los_datos.py`

- Esta herramienta permite que el agente:

  - Cargue datos_sept.csv como DataFrame.

  - Genere y ejecute código Pandas.

  - Devuelva resultados tabulares, métricas y resúmenes.

  - Es el puente entre el modelo y los datos reales.


### Instalación
1. Crear entorno Python
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
2. Ejecutar el sistema con Docker

`make run`

3. Abrir OpenWebUI

Una vez levantado el contenedor, abrir en el navegador:

http://localhost/

Uso

    Abrir OpenWebUI.

    Seleccionar el agente.

    Escribir consultas como:

        Calcula la rentabilidad por giro.

        ¿Qué negocios generan el 80 por ciento de las ganancias?

        Dame análisis temporal del volumen de transacciones.

    El agente generará el código Pandas necesario, lo ejecutará y presentará los resultados.

Licencia

Este proyecto se distribuye bajo la licencia incluida en el archivo `LICENSE`.
