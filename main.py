import os
import subprocess

def run_server():
    try:
       
        
        # Caminho para o arquivo manage.py
        manage_py_path = os.path.join(os.getcwd(), 'manage.py')
        
        # Comando para iniciar o servidor
        command = f'python {manage_py_path} runserver 8080'

        # Inicia o servidor usando subprocess
        subprocess.run(command, shell=True, check=True)
        
    except Exception as e:
        print(f"Erro ao iniciar o servidor: {e}")

if __name__ == "__main__":
    run_server()
