To test this application, follow the steps bellow:

## 1. Project Configuration

<details>
  <summary><strong>Project Dependencies</strong></summary>

### 1.1 Installing project dependencies

- Install [Python](https://www.python.org/downloads/)
- Install [Docker](https://docs.docker.com/desktop/install/windows-install/)
- Install [Node](https://nodejs.org/en)


### 1.2 DataBase Configuration
- Install [MariaDB](https://mariadb.org/download/?t=mariadb&o=true&p=mariadb&r=10.3.13&os=windows&cpu=x86&pkg=msi)
- After that, open the HeidiSQL application and configure with this information:
```sh
User: root
Password: 123456
Port: 3307
```
- This information can be checked in `ecommerce_fastapi_angular\api\src\config\configDB.py`
- Create a new database in the root with the name ecommercedb
- You don't need create the tables, just the database. More, in the next section

#### 1.2.2 To create database tables it's necessary perform the bellow command
- Open cmd in the `ecommerce_fastapi_angular\api` directory again
- perform `alembic upgrade head` command 
- For more information about alembic, see the section `2.1 About Alembic`

```sh
alembic upgrade head
```

**obs:** Using this command, the required tables will be created in the database.

</details>

<details>
<summary><strong>Start Application with Docker</strong></summary>

To start application with docker:
- Open cmd in the `ecommerce_fastapi_angular\` directory
- and perform:
```sh
npm run dev
```

This command run the application in dev mode. To start application in production and test mode, change thw word from **dev** to **prod** or **test**:

To delete containers and stop application, use the command:
```sh
npm run down
```

</details>

<details>
<summary><strong>Start Application individually</strong></summary>

### 1.3 Starting the BackEnd application

- Open cmd in the `ecommerce_fastapi_angular\api` directory
- Create a python virtual enviroment with: `py -m venv venv`
- Open the virtual enviroment with: `venv\Scripts\activate` (on Windows)
- Install the project dependencies with: `pip install -r requirements.txt`

```sh
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
- To start backend performing the command
```sh
uvicorn src.api:app --reload
```
- The server will open on http://127.0.0.1:8000
- Open your browser at http://127.0.0.1:8000/docs
- Then, you can create, read, update or delete users (Be happy!)
### 1.4 FrontEnd

To install the FrontEnd dependencies, check the Readme in the `ecommerce_fastapi_angular\frontend` directory.
___

</details>