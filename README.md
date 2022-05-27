# Ubicación
Componente de ubicación de capa 2

## Development

I decided to use pipenv because I find the installation of dependencies and its 
app setup very easy and convenient.

### Setup

1. Install pipenv
    ```shell
    pip install pipenv
    ```
2. Install the dependencies:
    ```shell
    cd <project_dir>
    pipenv install --three
    ```

### Run it

If you are not already in the `Ubicacion` directory:

```shell
cd <project_dir>
```
In this moment you have two options to run the app:

#### Activating the virtual environment
Activate the pipenv shell and run the python file.
```shell
pipenv shell
python runserver.py
```
#### Running directly the app

or as an alternative, you can try this:
```shell
pipenv run python runserver.py
```

## App Architecture
In this case I decided to use the Flask framework because it is a lightweight framework 
which fits quite small projects like this one.
Flask as such does not have a defined architecture. But in my case I made a prototype of 
MVC but without the view, only with controller and model, adding a service that is the 
MQTT subscriber in the sensors.py section.

The following is its deployment diagram:

![Deployment Diagram1](https://user-images.githubusercontent.com/38623131/170610085-8e843a17-765a-45ba-8d91-a2f6286bcd29.png)

An additional feature of this component is that it is ready to be deployed on a Linux server 
through ```Gunicorn``` which allows us to deploy with web workers.

## Author
* Oscar Pacheco
