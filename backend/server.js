const express = require('express');
    const mongoose = require('mongoose');
    const cors = require('cors');
    require('dotenv').config();
    require('dotenv').config({ path: __dirname + '/.env' });
    const app = express();
    const PORT = process.env.PORT || 5000;

    app.use(cors());
    app.use(express.json());

    const MONGO_URI = process.env.MONGO_URI;
    mongoose.connect(MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected successfully.'))
    .catch(err => console.error('MongoDB connection error:', err));

    const scoreSchema = new mongoose.Schema({
        name: { type: String, required: true, trim: true, maxLength: 15 },
        score: { type: Number, required: true },
        timestamp: { type: Date, default: Date.now },
    });

    const Score = mongoose.model('Score', scoreSchema);

    app.get('/api/scores', async (req, res) => {
        try {
            const topScores = await Score.find().sort({ score: -1 }).limit(10);
            res.json(topScores);
        } catch (error) {
            res.status(500).json({ message: 'Error fetching scores', error });
        }
    });

    app.post('/api/scores', async (req, res) => {
        try {
            const { name, score } = req.body;
            if (!name || score === undefined) {
                return res.status(400).json({ message: 'Name and score are required.' });
            }
            const newScore = new Score({ name, score }); // timestamp will be added by default
            await newScore.save();
            res.status(201).json(newScore);
        } catch (error) {
            res.status(500).json({ message: 'Error saving score', error });
        }
    });

    app.listen(PORT, () => {
        console.log(`Server is running on port ${PORT}`);
    });