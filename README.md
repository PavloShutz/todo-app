# todo-app 📝

### Installation and preparation

1) ```commandline
    git clone https://github.com/PavloShutz/todo-app.git
    ```
2) Use [pipenv](https://pypi.org/project/pipenv/) to install dependencies:
    ```commandline
    pipenv shell
    pipenv install
    ```
3) Create a database in PostgreSQL
* Create ``.env`` file 
```
todo_app
├───__pycache__
└─── .env
```
* Fill in these parameters:
```python
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_HOST=
DATABASE_PORT=
```