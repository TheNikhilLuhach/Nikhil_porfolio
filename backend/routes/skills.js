const express = require('express');
const router = express.Router();
const skills = require('../data/skills.json');

// GET all skills
router.get('/', (req, res) => {
  res.json(skills);
});

// GET skills by category
router.get('/category/:category', (req, res) => {
  const category = skills.categories.find(c => 
    c.title.toLowerCase().replace(/\s+/g, '-') === req.params.category.toLowerCase()
  );
  if (!category) {
    return res.status(404).json({ error: 'Category not found' });
  }
  res.json(category);
});

module.exports = router;
