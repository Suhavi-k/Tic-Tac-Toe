
**📌 Tic-Tac-Toe: Three Marks**
A unique twist on Tic-Tac-Toe where each player can only have **three marks** on the board at a time! Once a fourth mark is placed, the oldest mark is removed. Play **against a friend** or challenge an **AI opponent** with adjustable difficulty levels.[difficulty levels are yet to be added]
ps. This is a school project
---

## **📜 Features**
✅ **Two Game Modes**: Play against another player or challenge the AI  
✅ **Dynamic Rules**: Each player can only maintain 3 marks at a time  
✅ **AI Bot Levels**: Choose between **Easy, Medium, or Hard** difficulty[not yet added]  
✅ **Customizable Sound & Music**: Change background music and sound effects from `settings.json`    

---

## **🛠 Installation**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/tic-tac-toe-three-marks.git
cd tic-tac-toe-three-marks
```

### **2️⃣ Install Dependencies**
Ensure you have **Python 3.10+** installed. Then, install **Pygame**:
```sh
pip install pygame
```

---

## **🚀 How to Run**
```sh
python main.py
```
- Choose **Single-Player** (vs AI) or **Multi-Player** (vs a friend).  
- Select **Rules** to see the game instructions.  
- Adjust **music, sound effects, and AI difficulty** in `settings.json`.

---

## **🎵 Customizing Music & Sound**
Modify `settings.json` to change **music, sound effects, or volume**.

```json
{
    "Sound_effect": {
        "Blank": "./Sounds/Sound_effects/Blank_Shot_SFX.mp3",
        "Live": "./Sounds/Sound_effects/Live_Shot_SFX_One.mp3",
        "Victory": "./Sounds/Sound_effects/Victory_SFX.mp3",
        "Volume": 1.0
    },
    "Background Music": {
        "Track": "./Sounds/Music/Buckshot_mini_SoundTrack.mpeg",
        "Volume": 0.5
    },
    "bot_level": "medium"
}
```
🎯 **To change music dynamically** in the game, call:
```python
import sound
sound.restart_music()  # Restart music after updating settings.json
```

---

## **🤖 AI Bot Difficulty Levels**
- **Easy** → Random moves  
- **Medium** → Basic strategy  
- **Hard** → Smarter moves with a winning strategy  

Change difficulty in `settings.json`:
```json
"bot_level": "hard"
```
---

## **📝 Contribution**
Want to improve this project? Contributions are welcome!  

1. **Fork** the repo  
2. **Create** a new branch (`feature-new-option`)  
3. **Commit** your changes  
4. **Push** to your fork  
5. **Open a Pull Request**  

---

## **📧 Contact**
Have questions? Reach out to:  
📩 **Email:** suhavikaur30@gmail.com  

---

Enjoy **Tic-Tac-Toe: Three Marks**!
