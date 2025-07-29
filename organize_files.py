import os
import shutil
from collections import defaultdict

def reorganize_polymnist(source_base_path, target_base_path):
    for split in ['train', 'test']:
        for class_num in range(10):
            os.makedirs(os.path.join(target_base_path, split, str(class_num)), exist_ok=True)

    for split in ['train', 'test']:
        split_source_path = os.path.join(source_base_path, split)
        split_target_path = os.path.join(target_base_path, split)

        for m_folder in ['m0', 'm1', 'm2', 'm3', 'm4']:
            m_path = os.path.join(split_source_path, m_folder)
            if not os.path.exists(m_path):
                print("No path with: ", m_path)
                continue

            for filename in os.listdir(m_path):
                if filename.endswith('.png'):
                    label = filename.split('.')[-2]
                    new_filename = f"{m_folder}_{filename}"
                    target_folder = os.path.join(split_target_path, label)
                    src_path = os.path.join(m_path, filename)
                    dst_path = os.path.join(target_folder, new_filename)
                    shutil.copy(src_path, dst_path)

# Rutas
source_base_path = 'img/PolyMNIST/MMNIST' 
target_base_path = 'img/numbers'   

# Nota mmuy importante, es necesario tener la estructura correcta de los archivos.
# MUY IMPORTANTE img debe ser el nombre de la carpeta con la data, ya que esa carpeta
# la puse en el git ignore, si commiteamos las imagenes seguramente se muera el repositorio 

# Al descargar el set de datos con las imagenes, la carpeta con toda la data debe llamarse img y debe
# estar en el root del repo

# este script, tambien debe ejecutarse desde la root del repo, ya que pues, este archiivo
# tambien está dentro del root.

# la carpeta nueva que se genera se guarda dentro de img/numbers
# el script toma todas las fotos y las calsifica en carpetas de train y test con los numeros del 
# 0 al 9, cualquier duda me decis. 

reorganize_polymnist(source_base_path, target_base_path)
print("\n¡Reorganización completada!")

