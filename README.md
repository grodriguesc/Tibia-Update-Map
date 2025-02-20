﻿# Tibia Update Map

Este programa combina marcações de mapas do jogo Tibia, permitindo que os jogadores atualizem suas marcações sem perder os pontos personalizados. Além disso, o programa pode baixar automaticamente as marcações mais recentes do site TibiaMaps.io e combinar com as marcações existentes.

## Funcionalidades

- Combina marcações de mapas de dois arquivos `.bin`.
- Baixa automaticamente as marcações mais recentes de TibiaMaps.io.
- Permite a seleção de um arquivo de marcações local.
- Copia todo o conteúdo da pasta `minimap` baixada, exceto `minimapmarkers.bin`, para a pasta do Tibia.
- Faz backup do arquivo `minimapmarkers.bin` original antes de substituí-lo.
- Interface gráfica amigável para selecionar arquivos e pastas.

## Requisitos

- Windows
- Python 3.7 ou superior (para desenvolvimento e compilação)

## Como Usar

### 1. Baixar o Executável

Se você já possui o executável compilado, siga os passos abaixo. Caso contrário, consulte a seção "Como Compilar" para criar o executável.

### 2. Executar o Programa

1. **Abrir o Executável**

   - Dê um duplo clique no arquivo executável para abrir o programa.

2. **Combinar Marcações com TibiaMaps.io**

   - Marque a opção "Combinar marcações com TibiaMaps.io" para baixar automaticamente as marcações mais recentes do site TibiaMaps.io.

3. **Atualizar Mapa e Combinar Marcações**

   - Marque a opção "Atualizar Mapa e Combinar Marcações" para copiar todo o conteúdo da pasta `minimap` baixada, exceto o `minimapmarkers.bin`, para a pasta do Tibia.

4. **Selecionar um Arquivo Local de Marcações (Opcional)**

   - Se desejar, selecione um arquivo `minimapmarkers.bin` local para combinar com as marcações baixadas.

5. **Usar Caminho Diferente do Padrão para a Pasta do Tibia (Opcional)**

   - Marque esta opção se quiser selecionar uma pasta diferente do padrão para a pasta do Tibia.

6. **Selecionar uma Pasta Específica para Salvar o Arquivo Combinado (Opcional)**

   - Marque esta opção se quiser selecionar uma pasta específica para salvar o arquivo combinado.

7. **Combinar Arquivos**

   - Clique no botão "Combinar Arquivos" para iniciar o processo. A barra de progresso exibirá o andamento do download e da combinação dos arquivos.

8. **Mensagem de Sucesso ou Erro**
   - Ao final do processo, uma mensagem informará se a combinação dos arquivos foi bem-sucedida ou se ocorreu algum erro.

### Como Compilar

Se você precisar compilar o programa a partir do código-fonte, siga os passos abaixo:

1. **Instalar o PyInstaller**

   - No prompt de comando, execute:
     ```bash
     pip install pyinstaller
     ```

2. **Compilar o Script**

   - No prompt de comando, navegue até o diretório onde o script `tibia-update-map.py` está localizado e execute:
     ```bash
     pyinstaller --onefile --noconsole tibia-update-map.py
     ```

3. **Executável Gerado**
   - O executável será gerado na pasta `dist` dentro do diretório onde o script está localizado.

## Contribuições

Sinta-se à vontade para contribuir com melhorias para este projeto. Para contribuir:

1. Faça um fork deste repositório.
2. Crie um branch para sua feature (`git checkout -b minha-feature`).
3. Faça commit das suas alterações (`git commit -am 'Adicionar feature'`).
4. Faça push para o branch (`git push origin minha-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.

---

# # Tibia Update Map

This program combines map markers for the Tibia game, allowing players to update their markers without losing custom points. Additionally, the program can automatically download the latest markers from TibiaMaps.io and combine them with existing markers.

## Features

- Combines map markers from two `.bin` files.
- Automatically downloads the latest markers from TibiaMaps.io.
- Allows selection of a local markers file.
- Copies all content from the downloaded `minimap` folder, except `minimapmarkers.bin`, to the Tibia folder.
- Backs up the original `minimapmarkers.bin` file before replacing it.
- User-friendly graphical interface for selecting files and folders.

## Requirements

- Windows
- Python 3.7 or higher (for development and compilation)

## How to Use

### 1. Download the Executable

If you already have the compiled executable, follow the steps below. If not, see the "How to Compile" section to create the executable.

### 2. Run the Program

1. **Open the Executable**

   - Double-click the executable file to open the program.

2. **Combine Markers with TibiaMaps.io**

   - Check the option "Combine markers with TibiaMaps.io" to automatically download the latest markers from TibiaMaps.io.

3. **Update Map and Combine Markers**

   - Check the option "Update Map and Combine Markers" to copy all content from the downloaded `minimap` folder, except `minimapmarkers.bin`, to the Tibia folder.

4. **Select a Local Markers File (Optional)**

   - If desired, select a local `minimapmarkers.bin` file to combine with the downloaded markers.

5. **Use a Different Path for the Tibia Folder (Optional)**

   - Check this option if you want to select a different path for the Tibia folder.

6. **Select a Specific Folder to Save the Combined File (Optional)**

   - Check this option if you want to select a specific folder to save the combined file.

7. **Combine Files**

   - Click the "Combine Files" button to start the process. The progress bar will show the download and combination progress.

8. **Success or Error Message**
   - At the end of the process, a message will inform you whether the file combination was successful or if an error occurred.

### How to Compile

If you need to compile the program from the source code, follow the steps below:

1. **Install PyInstaller**

   - In the command prompt, run:
     ```bash
     pip install pyinstaller
     ```

2. **Compile the Script**

   - In the command prompt, navigate to the directory where the `tibia-update-map.py` script is located and run:
     ```bash
     pyinstaller --onefile --noconsole tibia-update-map.py
     ```

3. **Generated Executable**
   - The executable will be generated in the `dist` folder within the directory where the script is located.

## Contributions

Feel free to contribute improvements to this project. To contribute:

1. Fork this repository.
2. Create a branch for your feature (`git checkout -b my-feature`).
3. Commit your changes (`git commit -am 'Add feature'`).
4. Push to the branch (`git push origin my-feature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

---

# # Tibia Update Map

Este programa combina marcadores de mapas para el juego Tibia, permitiendo a los jugadores actualizar sus marcadores sin perder puntos personalizados. Además, el programa puede descargar automáticamente los marcadores más recientes de TibiaMaps.io y combinarlos con los marcadores existentes.

## Funcionalidades

- Combina marcadores de mapas de dos archivos `.bin`.
- Descarga automáticamente los marcadores más recientes de TibiaMaps.io.
- Permite seleccionar un archivo de marcadores local.
- Copia todo el contenido de la carpeta `minimap` descargada, excepto `minimapmarkers.bin`, a la carpeta de Tibia.
- Realiza una copia de seguridad del archivo `minimapmarkers.bin` original antes de reemplazarlo.
- Interfaz gráfica amigable para seleccionar archivos y carpetas.

## Requisitos

- Windows
- Python 3.7 o superior (para desarrollo y compilación)

## Cómo Usar

### 1. Descargar el Ejecutable

Si ya tienes el ejecutable compilado, sigue los pasos a continuación. De lo contrario, consulta la sección "Cómo Compilar" para crear el ejecutable.

### 2. Ejecutar el Programa

1. **Abrir el Ejecutable**

   - Haz doble clic en el archivo ejecutable para abrir el programa.

2. **Combinar Marcadores con TibiaMaps.io**

   - Marca la opción "Combinar marcadores con TibiaMaps.io" para descargar automáticamente los marcadores más recientes de TibiaMaps.io.

3. **Actualizar Mapa y Combinar Marcadores**

   - Marca la opción "Actualizar Mapa y Combinar Marcadores" para copiar todo el contenido de la carpeta `minimap` descargada, excepto `minimapmarkers.bin`, a la carpeta de Tibia.

4. **Seleccionar un Archivo Local de Marcadores (Opcional)**

   - Si lo deseas, selecciona un archivo `minimapmarkers.bin` local para combinar con los marcadores descargados.

5. **Usar una Ruta Diferente para la Carpeta de Tibia (Opcional)**

   - Marca esta opción si deseas seleccionar una ruta diferente para la carpeta de Tibia.

6. **Seleccionar una Carpeta Específica para Guardar el Archivo Combinado (Opcional)**

   - Marca esta opción si deseas seleccionar una carpeta específica para guardar el archivo combinado.

7. **Combinar Archivos**

   - Haz clic en el botón "Combinar Archivos" para iniciar el proceso. La barra de progreso mostrará el avance de la descarga y combinación de los archivos.

8. **Mensaje de Éxito o Error**
   - Al final del proceso, un mensaje informará si la combinación de archivos fue exitosa o si ocurrió algún error.

### Cómo Compilar

Si necesitas compilar el programa desde el código fuente, sigue los pasos a continuación:

1. **Instalar PyInstaller**

   - En el símbolo del sistema, ejecuta:
     ```bash
     pip install pyinstaller
     ```

2. **Compilar el Script**

   - En el símbolo del sistema, navega hasta el directorio donde se encuentra el script `tibia-update-map.py` y ejecuta:
     ```bash
     pyinstaller --onefile --noconsole tibia-update-map.py
     ```

3. **Ejecutable Generado**
   - El ejecutable se generará en la carpeta `dist` dentro del directorio donde se encuentra el script.

## Contribuciones

Siéntete libre de contribuir con mejoras a este proyecto. Para contribuir:

1. Haz un fork de este repositorio.
2. Crea una rama para tu funcionalidad (`git checkout -b mi-funcionalidad`).
3. Haz commit de tus cambios (`git commit -am 'Agregar funcionalidad'`).
4. Haz push a la rama (`git push origin mi-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo `LICENSE` para obtener más información.
