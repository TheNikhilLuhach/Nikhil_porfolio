const express = require('express');
const router = express.Router();
const experience = require('../data/experience.json');

// GET all experience
router.get('/', (req, res) => {
  res.json(experience);
});

// GET experience by ID
router.get('/:id', (req, res) => {
  const exp = experience.find(e => e.id === parseInt(req.params.id));
  if (!exp) {
    return res.status(404).json({ error: 'Experience not found' });
  }
  res.json(exp);
});

module.exports = router;
