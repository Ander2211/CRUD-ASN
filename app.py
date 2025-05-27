# pip install flask psycopg2-binary

from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# Conexión
def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="ans",
        user="postgres",           # ← Cambia por tu usuario
        password="123"     # ← Cambia por tu contraseña
    )

# Mostrar todos los estudiantes
@app.route('/')
def index():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM estudiantes ORDER BY id")
    estudiantes = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', estudiantes=estudiantes)

# Formulario para agregar nuevo
@app.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        data = request.form
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO estudiantes (apellido, nombre, edad, numero_carne, correo)
            VALUES (%s, %s, %s, %s, %s)
        """, (data['apellido'], data['nombre'], data['edad'], data['numero_carne'], data['correo']))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('form.html', estudiante=None)

# Editar estudiante
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    conn = get_connection()
    cur = conn.cursor()
    if request.method == 'POST':
        data = request.form
        cur.execute("""
            UPDATE estudiantes SET apellido=%s, nombre=%s, edad=%s, numero_carne=%s, correo=%s
            WHERE id=%s
        """, (data['apellido'], data['nombre'], data['edad'], data['numero_carne'], data['correo'], id))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    else:
        cur.execute("SELECT * FROM estudiantes WHERE id = %s", (id,))
        estudiante = cur.fetchone()
        cur.close()
        conn.close()
        return render_template('form.html', estudiante=estudiante)

# Eliminar
@app.route('/eliminar/<int:id>')
def eliminar(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM estudiantes WHERE id = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

# Ejecutar
if __name__ == '__main__':
    app.run(debug=True)
