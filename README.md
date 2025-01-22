# Run Custom Odoo Module Locally

This guide will help you set up Odoo 18 locally and create a custom module. Follow these steps to clone the Odoo repository, configure your environment, and run a custom Odoo module.

## Prerequisites

- Git
- PostgreSQL
- Python 3.7 or higher
- A suitable IDE (e.g., Visual Studio Code, PyCharm)

---

## Step 1: Clone Odoo 18 Repository

First, clone the Odoo 18 repository to your local machine:

```bash
git clone https://github.com/odoo/odoo.git --branch 18.0 --depth 1
```

# Custom Odoo Module Setup Guide

## Step 1: Project Structure

Create a folder called `customModule` in your project directory. Inside this folder, create the following structure:

```bash
customModule
    ├── conf
    │   └── odoo.conf
    ├── custom_addons
    │   └── <your_custom_module>
    └── odoo
```

## Step 2: Set Up Custom Module Structure

### 2.1. `odoo.conf` Configuration File

1. Open your IDE and create a `conf` folder inside `customModule`.
2. Copy the contents of `customModule/odoo/debian/odoo.conf` into the newly created `conf/odoo.conf` file.
3. Edit the `odoo.conf` file with your PostgreSQL configuration and add the paths for your custom addons.

Example of `odoo.conf`:

```ini
[options]
; Add PostgreSQL settings
db_host = False
db_port = False
db_user = odoo
db_password = odoo_password

; Add the paths to your addons
addons_path = /customModule/odoo/addons,/customModule/custom_addons

; Additional settings
admin_passwd = admin
```
### Create Your Custom Module

Create your custom Odoo module inside `custom_addons/<your_custom_module>`. This is where your custom module's code and assets will reside.

## Step 3: Set Up PostgreSQL

You need to create a PostgreSQL user for Odoo and configure the database. Run the following commands in your PostgreSQL shell:

1. Create a PostgreSQL user for Odoo:

    ```sql
    postgres=# create user odoo with password 'odoo';
    ```

2. Give the user superuser privileges:

    ```sql
    postgres=# alter user odoo with superuser;
    ```
## Step 4: Configure IDE

You need to update your IDE configuration with the following:

1. **Odoo executable path**: Set it to `/customModule/odoo/odoo-bin`.
2. **Script parameter**: Add the parameter `-c /customModule/conf/odoo.conf` to point to your configuration file.

## Step 5: Run Odoo Locally

Now, you can run Odoo locally with your custom module. In your IDE, run the Odoo server and navigate to: http://localhost:8069/


This should bring up the Odoo interface, where you can install and manage your custom module.



