import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import shutil
import requests
import zipfile
import io
import threading

# Dicionário de traduções
translations = {
    "pt-br": {
        "title": "Atualizar Mapa sem perder marcações",
        "combine_with_tibiamaps": "Combinar marcações com TibiaMaps.io",
        "update_and_combine": "Atualizar Mapa e Combinar Marcações",
        "advanced_options": "Mostrar Opções Avançadas",
        "select_minimap_file": "Selecione um minimapmarkers.bin:",
        "use_custom_tibia_path": "Usar caminho diferente do padrão para a pasta do Tibia",
        "select_tibia_folder": "Selecione a pasta do Tibia:",
        "use_custom_output_path": "Selecionar uma pasta específica para salvar o arquivo combinado",
        "select_output_folder": "Selecione a pasta de saída do arquivo combinado:",
        "combine_files": "Combinar Arquivos",
        "error_title": "Erro",
        "success_title": "Sucesso",
        "combine_error": "Ocorreu um erro durante a combinação dos arquivos: ",
        "combine_success": "Arquivo combinado salvo como {output_file_path} e substituído na pasta do Tibia.\nBackup criado como {backup_file_path}",
        "download_error": "Ocorreu um erro ao baixar o arquivo: ",
        "developer_info": "Desenvolvido por: Nescau Concertado\nEmail: grodriguesc@outlook.com.br"
    },
    "en": {
        "title": "Update Map Without Losing Markers",
        "combine_with_tibiamaps": "Combine markers with TibiaMaps.io",
        "update_and_combine": "Update Map and Combine Markers",
        "advanced_options": "Show Advanced Options",
        "select_minimap_file": "Select a minimapmarkers.bin:",
        "use_custom_tibia_path": "Use a different path for the Tibia folder",
        "select_tibia_folder": "Select the Tibia folder:",
        "use_custom_output_path": "Select a specific folder to save the combined file",
        "select_output_folder": "Select the output folder for the combined file:",
        "combine_files": "Combine Files",
        "error_title": "Error",
        "success_title": "Success",
        "combine_error": "An error occurred while combining the files: ",
        "combine_success": "Combined file saved as {output_file_path} and replaced in the Tibia folder.\nBackup created as {backup_file_path}",
        "download_error": "An error occurred while downloading the file: ",
        "developer_info": "Developed by: Nescau Concertado\nEmail: grodriguesc@outlook.com.br"
    },
    "es": {
        "title": "Actualizar el Mapa sin perder Marcadores",
        "combine_with_tibiamaps": "Combinar marcadores con TibiaMaps.io",
        "update_and_combine": "Actualizar Mapa y Combinar Marcadores",
        "advanced_options": "Mostrar Opciones Avanzadas",
        "select_minimap_file": "Seleccione un minimapmarkers.bin:",
        "use_custom_tibia_path": "Usar una ruta diferente para la carpeta de Tibia",
        "select_tibia_folder": "Seleccione la carpeta de Tibia:",
        "use_custom_output_path": "Seleccionar una carpeta específica para guardar el archivo combinado",
        "select_output_folder": "Seleccione la carpeta de salida para el archivo combinado:",
        "combine_files": "Combinar Archivos",
        "error_title": "Error",
        "success_title": "Éxito",
        "combine_error": "Ocurrió un error al combinar los archivos: ",
        "combine_success": "Archivo combinado guardado como {output_file_path} y reemplazado en la carpeta de Tibia.\nBackup creado como {backup_file_path}",
        "download_error": "Ocurrió un error al descargar el archivo: ",
        "developer_info": "Desarrollado por: Nescau Concertado\nEmail: grodriguesc@outlook.com.br"
    },
    "pl": {
        "title": "Aktualizacja Mapy Bez Utraty Znaczników",
        "combine_with_tibiamaps": "Połącz znaczniki z TibiaMaps.io",
        "update_and_combine": "Aktualizuj Mapę i Połącz Znaczniki",
        "advanced_options": "Pokaż Zaawansowane Opcje",
        "select_minimap_file": "Wybierz minimapmarkers.bin:",
        "use_custom_tibia_path": "Użyj innej ścieżki dla folderu Tibia",
        "select_tibia_folder": "Wybierz folder Tibia:",
        "use_custom_output_path": "Wybierz konkretny folder do zapisania połączonego pliku",
        "select_output_folder": "Wybierz folder wyjściowy dla połączonego pliku:",
        "combine_files": "Połącz Pliki",
        "error_title": "Błąd",
        "success_title": "Sukces",
        "combine_error": "Wystąpił błąd podczas łączenia plików: ",
        "combine_success": "Połączony plik zapisany jako {output_file_path} i zastąpiony w folderze Tibia.\nBackup utworzony jako {backup_file_path}",
        "download_error": "Wystąpił błąd podczas pobierania pliku: ",
        "developer_info": "Opracowane przez: Nescau Concertado\nEmail: grodriguesc@outlook.com.br"
    },
    "de": {
        "title": "Karte Aktualisieren Ohne Marker Zu Verlieren",
        "combine_with_tibiamaps": "Marker mit TibiaMaps.io kombinieren",
        "update_and_combine": "Karte aktualisieren und Marker kombinieren",
        "advanced_options": "Erweiterte Optionen anzeigen",
        "select_minimap_file": "Wählen Sie eine minimapmarkers.bin:",
        "use_custom_tibia_path": "Verwenden Sie einen anderen Pfad für den Tibia-Ordner",
        "select_tibia_folder": "Wählen Sie den Tibia-Ordner:",
        "use_custom_output_path": "Wählen Sie einen bestimmten Ordner zum Speichern der kombinierten Datei",
        "select_output_folder": "Wählen Sie den Ausgabefolder für die kombinierte Datei:",
        "combine_files": "Dateien Kombinieren",
        "error_title": "Fehler",
        "success_title": "Erfolg",
        "combine_error": "Beim Kombinieren der Dateien ist ein Fehler aufgetreten: ",
        "combine_success": "Kombinierte Datei gespeichert als {output_file_path} und im Tibia-Ordner ersetzt.\nBackup erstellt als {backup_file_path}",
        "download_error": "Beim Herunterladen der Datei ist ein Fehler aufgetreten: ",
        "developer_info": "Entwickelt von: Nescau Concertado\nEmail: grodriguesc@outlook.com.br"
    }
}

def set_language(lang):
    global translation
    translation = translations[lang]
    update_texts()

def update_texts():
    app.title(translation["title"])
    chk_use_downloaded_file.config(text=translation["combine_with_tibiamaps"])
    chk_copy_minimap_content.config(text=translation["update_and_combine"])
    chk_show_advanced.config(text=translation["advanced_options"])
    label_minimap_file.config(text=translation["select_minimap_file"])
    chk_use_custom_tibia_path.config(text=translation["use_custom_tibia_path"])
    label_tibia_folder.config(text=translation["select_tibia_folder"])
    chk_use_custom_output_path.config(text=translation["use_custom_output_path"])
    label_output_folder.config(text=translation["select_output_folder"])
    btn_combine_files.config(text=translation["combine_files"])
    developer_info.config(text=translation["developer_info"])

def read_bin_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

def extract_markers(file_content):
    markers = []
    i = 0
    while i < len(file_content):
        if file_content[i:i+4] == b'\x1A\x00\x20\x00':
            markers.append(file_content[i:i+4])
            i += 4
        else:
            end_idx = file_content.find(b'\x20\x00', i)
            if end_idx == -1:
                markers.append(file_content[i:])
                break
            else:
                markers.append(file_content[i:end_idx+2])
                i = end_idx + 2
    return markers

def combine_markers(markers1, markers2):
    combined_markers = set(markers1) | set(markers2)
    return list(combined_markers)

def write_bin_file(file_path, markers):
    with open(file_path, 'wb') as file:
        for marker in markers:
            file.write(marker)

def select_file(entry):
    file_path = filedialog.askopenfilename(filetypes=[("BIN Files", "*.bin")])
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

def select_folder(entry):
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry.delete(0, tk.END)
        entry.insert(0, folder_path)

def download_file(url, extract_to, progress_var):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        downloaded_size = 0
        
        zip_file = io.BytesIO()
        
        for chunk in response.iter_content(chunk_size=8192):
            downloaded_size += len(chunk)
            progress_var.set(int(downloaded_size * 50 / total_size))
            zip_file.write(chunk)
        
        zip_file.seek(0)
        
        with zipfile.ZipFile(zip_file) as z:
            z.extractall(extract_to)
        
        progress_var.set(50)
        return os.path.join(extract_to, "minimap", "minimapmarkers.bin")
    except Exception as e:
        messagebox.showerror(translation["error_title"], f"{translation['download_error']}: {str(e)}")
        return None

def combine_files_thread(progress_var):
    tibia_folder = entry_tibia_folder.get()
    use_custom_tibia_path = var_use_custom_tibia_path.get()
    use_custom_output_path = var_use_custom_output_path.get()
    copy_minimap_content = var_copy_minimap_content.get()
    file2_path = download_file("https://tibiamaps.io/downloads/minimap-with-markers", temp_dir, progress_var)

    if not file2_path:
        progress_var.set(0)
        return

    if use_custom_tibia_path:
        tibia_folder = entry_tibia_folder.get()
    else:
        tibia_folder = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Tibia', 'packages', 'Tibia', 'minimap')

    if use_custom_output_path:
        output_folder_path = entry_output.get()
        output_file_path = os.path.join(output_folder_path, 'minimapmarkers.bin')
    else:
        output_file_path = os.path.join(tibia_folder, 'minimapmarkers.bin')

    if not os.path.exists(tibia_folder):
        messagebox.showerror(translation["error_title"], f"{translation['combine_error']} {tibia_folder}")
        progress_var.set(0)
        return

    file1_path = os.path.join(tibia_folder, 'minimapmarkers.bin')
    if not os.path.exists(file1_path):
        messagebox.showerror(translation["error_title"], f"{translation['combine_error']} {tibia_folder}")
        progress_var.set(0)
        return

    try:
        # Criar backup do arquivo original
        backup_file_path = os.path.join(tibia_folder, 'minimapmarkers-backup.bin')
        shutil.copy(file1_path, backup_file_path)

        file1_content = read_bin_file(file1_path)
        file2_content = read_bin_file(file2_path)

        markers1 = extract_markers(file1_content)
        markers2 = extract_markers(file2_content)

        combined_markers = combine_markers(markers1, markers2)

        # Escrever o arquivo combinado no local de saída
        write_bin_file(output_file_path, combined_markers)
        progress_var.set(80)

        # Copiar o arquivo combinado para a pasta do Tibia, evitando copiar para ele mesmo
        if output_file_path != file1_path:
            shutil.copy(output_file_path, file1_path)
        
        # Copiar conteúdo da pasta minimap, exceto minimapmarkers.bin
        if copy_minimap_content:
            downloaded_minimap_dir = os.path.join(temp_dir, 'minimap')
            for item in os.listdir(downloaded_minimap_dir):
                s = os.path.join(downloaded_minimap_dir, item)
                d = os.path.join(tibia_folder, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, dirs_exist_ok=True)
                elif item != 'minimapmarkers.bin':
                    shutil.copy2(s, d)

        progress_var.set(100)
        messagebox.showinfo(translation["success_title"], translation["combine_success"].format(output_file_path=output_file_path, backup_file_path=backup_file_path))
    except Exception as e:
        messagebox.showerror(translation["error_title"], f"{translation['combine_error']} {str(e)}")
    finally:
        progress_var.set(0)

def start_combination():
    progress_var.set(0)
    threading.Thread(target=combine_files_thread, args=(progress_var,)).start()

app = tk.Tk()
app.title("Atualizar Mapa sem perder marcações")

# Seletor de idioma
tk.Label(app, text="Idioma / Language:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
lang = tk.StringVar(value="pt-br")
languages = {"Português": "pt-br", "English": "en", "Español": "es", "Polski": "pl", "Deutsch": "de"}
lang_menu = ttk.Combobox(app, textvariable=lang, values=list(languages.keys()), state="readonly")
lang_menu.grid(row=0, column=1, padx=10, pady=5, sticky='w')
lang_menu.bind("<<ComboboxSelected>>", lambda event: set_language(languages[lang_menu.get()]))

# Checkbox para usar arquivo baixado
var_use_downloaded_file = tk.BooleanVar(value=True)
chk_use_downloaded_file = tk.Checkbutton(app, text="Combinar marcações com TibiaMaps.io", variable=var_use_downloaded_file)
chk_use_downloaded_file.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

# Checkbox para copiar conteúdo da pasta minimap
var_copy_minimap_content = tk.BooleanVar(value=True)
chk_copy_minimap_content = tk.Checkbutton(app, text="Atualizar Mapa e Combinar Marcações", variable=var_copy_minimap_content)
chk_copy_minimap_content.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

# Checkbox para mostrar opções avançadas
var_show_advanced = tk.BooleanVar()
chk_show_advanced = tk.Checkbutton(app, text="Mostrar Opções Avançadas", variable=var_show_advanced, command=lambda: toggle_advanced_options())
chk_show_advanced.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

# LabelFrame para opções avançadas
advanced_frame = ttk.LabelFrame(app, text="Opções Avançadas")
advanced_frame.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky='ew')

# Seleção do segundo arquivo de marcações
label_minimap_file = tk.Label(advanced_frame, text="Selecione um minimapmarkers.bin:")
label_minimap_file.grid(row=0, column=0, padx=10, pady=5, sticky='e')
entry_file2 = tk.Entry(advanced_frame, width=50, state='disabled')
entry_file2.grid(row=0, column=1, padx=10, pady=5)
tk.Button(advanced_frame, text="Procurar", command=lambda: select_file(entry_file2), state='disabled').grid(row=0, column=2, padx=10, pady=5)

# Checkbox para usar caminho diferente do padrão para a pasta do Tibia
var_use_custom_tibia_path = tk.BooleanVar()
chk_use_custom_tibia_path = tk.Checkbutton(advanced_frame, text="Usar caminho diferente do padrão para a pasta do Tibia", variable=var_use_custom_tibia_path)
chk_use_custom_tibia_path.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

# Campo de entrada para a pasta do Tibia
label_tibia_folder = tk.Label(advanced_frame, text="Selecione a pasta do Tibia:")
label_tibia_folder.grid(row=2, column=0, padx=10, pady=5, sticky='e')
entry_tibia_folder = tk.Entry(advanced_frame, width=50)
entry_tibia_folder.grid(row=2, column=1, padx=10, pady=5)
tk.Button(advanced_frame, text="Procurar", command=lambda: select_folder(entry_tibia_folder)).grid(row=2, column=2, padx=10, pady=5)

# Checkbox para selecionar uma pasta específica para o arquivo combinado
var_use_custom_output_path = tk.BooleanVar()
chk_use_custom_output_path = tk.Checkbutton(advanced_frame, text="Selecionar uma pasta específica para salvar o arquivo combinado", variable=var_use_custom_output_path)
chk_use_custom_output_path.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

# Campo de entrada para o local de saída do arquivo combinado
label_output_folder = tk.Label(advanced_frame, text="Selecione a pasta de saída do arquivo combinado:")
label_output_folder.grid(row=4, column=0, padx=10, pady=5, sticky='e')
entry_output = tk.Entry(advanced_frame, width=50)
entry_output.grid(row=4, column=1, padx=10, pady=5)
tk.Button(advanced_frame, text="Salvar em", command=lambda: select_folder(entry_output)).grid(row=4, column=2, padx=10, pady=5)

# Barra de progresso
progress_var = tk.IntVar()
progress_bar = ttk.Progressbar(app, variable=progress_var, maximum=100)
progress_bar.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky='ew')

# Botão para combinar os arquivos
btn_combine_files = tk.Button(app, text="Combinar Arquivos", command=start_combination)
btn_combine_files.grid(row=6, column=0, columnspan=3, pady=20)

# Função para habilitar/desabilitar campos com base nos checkboxes
def toggle_entries():
    if var_use_custom_tibia_path.get():
        entry_tibia_folder.config(state='normal')
    else:
        entry_tibia_folder.config(state='disabled')

    if var_use_custom_output_path.get():
        entry_output.config(state='normal')
    else:
        entry_output.config(state='disabled')
    
    if var_use_downloaded_file.get():
        entry_file2.config(state='disabled')
    else:
        entry_file2.config(state='normal')

# Função para mostrar/ocultar opções avançadas
def toggle_advanced_options():
    if var_show_advanced.get():
        advanced_frame.grid()
    else:
        advanced_frame.grid_remove()

# Monitorar mudanças nas checkboxes
var_use_custom_tibia_path.trace_add("write", lambda *args: toggle_entries())
var_use_custom_output_path.trace_add("write", lambda *args: toggle_entries())
var_use_downloaded_file.trace_add("write", lambda *args: toggle_entries())
var_show_advanced.trace_add("write", lambda *args: toggle_advanced_options())

# Inicialmente desabilitar os campos
toggle_entries()
toggle_advanced_options()

# Informação do Desenvolvedor
developer_info = tk.Label(app, text="Desenvolvido por: Nescau Concertado\nEmail: grodriguesc@outlook.com.br", font=("Arial", 10), fg="gray")
developer_info.grid(row=7, column=0, columnspan=3, pady=10)

# Pasta temporária para downloads
temp_dir = os.path.join(os.path.expanduser('~'), 'TibiaMapTemp')
os.makedirs(temp_dir, exist_ok=True)

# Definir idioma inicial
set_language("pt-br")

app.mainloop()

# Limpar pasta temporária ao fechar o aplicativo
shutil.rmtree(temp_dir, ignore_errors=True)
