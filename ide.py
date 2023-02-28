import os
# alias ide='python3 /home/lucas/workspace/config-lucas/ide.py'
# alias ide='python3 /home/lucas/.lucas/ide.py'
# alias proyecto='python3 /home/lucas/workspace/config-lucas/ide.py'
'''
Agregar:
    . en la ventana svr, activar el entorno virtual y ejecutar el servidor (para django)
    . en la ventana db, ejecutar el gestor de base de datos
'''

os.system('''
tmux start-server;
tmux new-session -d -s IDE -n vim -d vim .;
tmux new-window -ad -n term;
tmux new-window -ad -n db;
tmux new-window -ad -n svr;
tmux attach -tIDE;
''')

#tmux split-window -h -t {v}:0 -d;

#tmux select-layout -t IDE:0 tiled;
#tmux attach -tIDE;




