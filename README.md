# Color Game

## Description
This project is a game where the player must change colors to navigate through obstacles, reaching the required score in each level to increase difficulty. It utilizes Python, Object-Oriented Programming (OOP), pygame, and is designed for single-player gameplay.

## Installation
1. Clone the repository.
   ```bash
   git clone https://github.com/JuanPabloGomezHaroCabrera/Color-Game.git

2. Navigate to the project directory
    ```bash
    cd Color-Game

3. Create your venv.
   ```bash
   python -m venv venv

4. Activate your venv (windows).
   ```bash
   call venv/Scripts/activate

5. Install the requirements.
   ```bash
   pip install -r requirements.txt

## Run the game
1. Run the game.
    ```bash
   python ColorGame.py

## Usage
1. Start the game by running the ColorGame.py script.
2. Follow the instructions in the terminal to complete each level.
3. Enjoy.

## Project Structure
- 📂 src
    - 📂 Assets
        - 📂 Audio
            - 🎵 Musica_Ganador.wav
            - 🎵 MusicaDeEspera_ChallengeColor.wav
            - 🎵 MusicaJuego.wav
        - 📂 Imagenes
            - 🖼️ estrella.png
            - 🖼️ universo.png
        - 📂 Prefabs
            - 📄 Fugaz.py
            - 📄 Obstaculo.py
            - 📄 Player.py
    - 📂 Game
        - 📄 GameController.py
    - 📂 Resources
        - 📄 Colors.py
        - 📄 Fonts.py
        - 📄 Ventana.py
    - 📄 ColorGame.py


1. `Assets`: Contains the Audio, Images and Prefabs (player, obstacle...).
2. `Game`: Contain the class Game Controller to manage the game.
3. `Resources`: Contains the Fonts, Texts and Colors that the game uses.
4. `ColorGame.py`: Contains the main class to init the game.
5. `.gitignore`: Python and VisualStudioCode.
6. `README.md`: Project documentation.
7. `requirements.txt`: The requirements to run this project.

## Dependencies
This project uses the following standard Python libraries:

* `pygame`: For managing graphics, sound, events.
* `sys`: For quit the game.
