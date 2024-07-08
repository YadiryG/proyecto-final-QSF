<?php
-- Active: 1720312009847@@127.0.0.1@3306@tabla_sql
// Configuración de la conexión a la base de datos
servername = "localhost";
username = "root";
password = "";
dbname = "tabla_qsf";

// Crear conexión
conn = new mysqli(servername, username, password, dbname);

// Verificar conexión
if (conn->connect_error) {
    die("Conexión fallida: " . conn->connect_error);
}

// Obtener datos del formulario
procedencia = request.form['procedencia']
celular = request.form['celular']
email = request.form['email']
rol = request.form['rol']
tipo_solicitud = request.form['tipo_solicitud']
descripcion = request.form['descripcion']

// Preparar y ejecutar la consulta SQL
sql = "INSERT INTO my_table (name, email) VALUES ('$procedencia', '$celular', '$email', '$rol', '$tipo_solicitud', '$descripcion)";

if (conn->query(sql) === TRUE) {
    echo "Datos insertados correctamente";
} else {
    echo "Error: " . sql . "<br>" . conn->error;
}

// Cerrar la conexión
conn->close();
?>