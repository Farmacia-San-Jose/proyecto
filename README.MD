# PROYECTO PARA LA FARMACIA SAN JOSE
Este proyecto contempla manejar el tema de invetario.

## CREACION AL ENTORNO VIRTUAL
```bash
python -m venv venv
```

## ACTIVAR EL ENTORNO VIRTUAL
```bash
venv\scripts\activate

```

## INSTALAR TODAS LAS HERRAMIENTOS
```bash
python -m pip install -r requirements.txt
```

## AGREGAR MAS HERRAMIENTAS
```bash
pip freeze > requirements.txt
```

## COMANDOS EN DOCKER

Iniciar docker
```bash
docker compose up -d

```

Apagar el docker
```bash
docker compose down
```

Mostrar informacion en consola
```bash
docker logs <name_container>
```

```bash
docker logs -f <name_container>
```

Ingresar shell de un contenedor
```bash
docker exec -it <container_name> bash
```

Ingresar a la shell de MYSQL
```bash
mysql -h <host> -u <user> -p
```

Limpiar consola
```bash
CTRL +L
clear
cls
\! cls
```