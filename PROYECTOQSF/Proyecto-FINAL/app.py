from flask import Flask, render_template, request
import random
from datetime import datetime

app = Flask(__name__)

# Ruta para el formulario
@app.route('/', methods=['GET', 'POST'])
def complaint_form():
    if request.method == 'POST':
        # Obtener datos del formulario
        procedencia = request.form['procedencia']
        celular = request.form['celular']
        email = request.form['email']
        rol = request.form['rol']
        tipo_solicitud = request.form['tipo_solicitud']
        descripcion = request.form['descripcion']
        
        # Generar número de radicado aleatorio (simulado)
        numero_radicado = random.randint(100000, 999999)
        
        # Obtener fecha de radicación
        fecha_radicacion = datetime.now().strftime('%d/%m/%Y')
        
        # Estado inicial de la solicitud
        estado_solicitud = 'Pendiente'
        
        # Inicialmente no hay tratamiento realizado ni fecha de respuesta
        tratamiento_realizado = ''
        fecha_respuesta = ''
        
        # Renderizar la plantilla de confirmación
        return render_template('confirmacion.html', 
                               procedencia=procedencia,
                               celular=celular,
                               email=email,
                               rol=rol,
                               tipo_solicitud=tipo_solicitud,
                               descripcion=descripcion,
                               numero_radicado=numero_radicado,
                               fecha_radicacion=fecha_radicacion,
                               estado_solicitud=estado_solicitud)
    
    # Renderizar el formulario HTML
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)
