# Restaurant_Dishes APIs Repository

The project consists of creating some APIs using the Django Rest Framework to register restaurants and their dishes, where users give the dish a rating from 1 to 5.

Each dish contains its average rating.



## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env

`SECRET_KEY='django-insecure-%^xzd&me8!b8)@!0#l+@xu$1k8+_6j+7w8kzjndnsf9*#e)ado'`

`DEBUG='True'`


## Instalação

To start the procject you need first create and activate a venv using the following commands:

```
    python -m venv venv
    . venv/Scripts/Activate.ps1
```

Once you are in the virtual environment, you must install the libraries using the command:

```
    pip install -r requirements.txt
```
Once finished, just run the server using:
```
    python manage.py runserver
```

## Routes

- ' ' -> link to the APIs
- /swagger
- /admin