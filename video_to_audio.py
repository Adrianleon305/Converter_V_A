import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip

def convert_to_audio():
    # Seleccionar el archivo de video
    video_file = filedialog.askopenfilename(title="Seleccionar archivo de video", filetypes=(("Archivos de video", "*.mp4"),))
    
    if video_file:
        try:
            # Crear un objeto VideoFileClip
            video_clip = VideoFileClip(video_file)
            
            # Extraer el audio del clip de video
            audio_clip = video_clip.audio
            
            # Guardar el archivo de audio
            audio_file = video_file.replace(".mp4", ".mp3")
            audio_clip.write_audiofile(audio_file)
            
            # Mostrar mensaje de éxito
            result_label.config(text="¡Conversión exitosa!")
        except Exception as e:
            # Mostrar mensaje de error
            result_label.config(text=f"Error: {str(e)}")
    else:
        # Mostrar mensaje si no se seleccionó ningún archivo
        result_label.config(text="No se seleccionó ningún archivo de video")

# Crear la ventana principal
root = tk.Tk()
root.title("Conversor de Video a Audio")

# Crear etiqueta de resultado
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Crear botón de selección de archivo
select_button = tk.Button(root, text="Seleccionar archivo de video", command=convert_to_audio)
select_button.pack(pady=10)

# Ejecutar la ventana principal
root.mainloop()
