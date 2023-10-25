# empabee_back
Backend para el proyecto empabee

## INSTALACION
Para correr este proyecto luego de hacer git clone se debe correr los siguientes comandos  en nuestro entorno de desarrollo

### instalar dependencias:
* pip install -r requirements.txt

### instalar nuevas dependencias al proyecto
Es recomendable que si instalaste algo nuevo, antes de hacer commit ejecutes el siguiente comando
* pip freeze > requirements.txt

### Crear una nueva key: 
* python -c "import random; print('SECRET_KEY=' + ''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)))" >> .env
    

