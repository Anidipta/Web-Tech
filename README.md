
# 🌌 Cosmic Clicker

**Cosmic Clicker** is a fast-paced web game where you catch stars, dodge asteroids, and climb the global leaderboard. Built with the **MERN stack**, it features immersive visuals, sound effects, and persistent scoring.

---

## 🚀 Features

* **Gameplay**: Control a ring with your mouse, catch stars (+1 to +10 points), avoid asteroids (−points).
* **Visuals & Audio**: Animated cosmic background, glowing effects, particle bursts, and procedural sounds.
* **Leaderboard**: MongoDB-powered global scores with local storage fallback.

---

## 🛠 Tech Stack

**Frontend**: HTML5, Tailwind CSS, JavaScript (ES6+), Tone.js
**Backend**: Node.js, Express.js, MongoDB (Mongoose)

---

## ⚙️ Setup

### Frontend

Open `index.html` in a modern browser.

### Backend

```bash
cd backend
npm install express mongoose cors dotenv
```

Create `.env`:

```env
MONGO_URI=mongodb://localhost:27017/cosmic_clicker
PORT=3000
```

Run server:

```bash
node server.js
```

---

## 🎮 How to Play

1. Start game → Move ring with mouse.
2. Click to collect stars.
3. Score as high as possible in **30s**.
4. Submit score → See ranking on leaderboard.

---

## 📜 License

MIT License