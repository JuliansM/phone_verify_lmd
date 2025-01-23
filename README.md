# Phone Verify Lambda

Este proyecto utiliza Terraform para desplegar una función Lambda escrita en Python que simula la respuesta de una Api Pública (numVerify). A continuación, se describen los pasos necesarios para configurar y desplegar la infraestructura.

## Estructura del Proyecto

```plaintext
├── lambda/               # Directorio que contiene el código fuente de la función Lambda
│   ├── index.py          # Archivo principal de la función Lambda
├── data.tf               # Definiciones de datos de Terraform
├── locals.tf             # Definiciones de variables locales
├── main.tf               # Configuración principal de Terraform
├── outputs.tf            # Salidas de Terraform
├── provider.tf           # Configuración del proveedor (AWS)
├── README.md  
├── .gitignore    
```

## Prerrequisitos
Antes de empezar, debemos asegurarnos de tener instalado lo siguiente en la máquina local:

1. Terraform (versión recomendada: >= 5.84.0)
2. AWS CLI configurado con credenciales válidas.
3. Python (versión recomendada: >= 3.12) y pip para gestionar dependencias.
4. Acceso a una cuenta de AWS con permisos para gestionar Lambdas e infraestructura asociada.

## Configuración inicial

### Clonar el repositorio:
```bash
git clone https://github.com/JuliansM/phone_verify_lmd.git
cd phone_verify_lmd
```

## Pasos para desplegar

### 1. Inicializar terraform
Desde la raíz del proyecto, ejecutar:
```bash
terraform init
```
Esto descargará los proveedores y módulos necesarios.

### 2. Planificar el despliegue
Se puede verificar antes del despliegue cuales serán los recursos que se crearán o actualizarán. Para ello, se debe ejecutar el siguiente comando:
```bash
terraform plan
```

### 3. Aplicar el despliegue
Ejecutar el siguiente comando para desplegar la infraestructura:
```bash
terraform apply
```
Confirma la ejecución tipeando ```yes``` cuando se solicite.

### 3. Verificar los recursos
Una vez desplegado, se puede obtener detalles de la lambda y otros recursos asociados desde la salida de Terraform o mediante la consola de AWS.

### 4. Limpieza de recursos (opcional)
Para eliminar los recursos creados puede hacer ejecutando el siguiente comando:
```bash
terraform destroy
```
Se debe confirmar la acción de eliminar tipeando ```yes``` cuando sea solicitado.

## Notas Adicionales
- Logs de la Lambda: Se puede inspeccionar los logs de ejecución de la Lambda desde CloudWatch Logs en la consola de AWS.

## Problemas Comunes

### Error de permisos:
Asegurarse de que el usuario o rol de AWS tenga permisos suficientes para crear y gestionar Lambdas.