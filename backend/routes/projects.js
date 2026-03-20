const express = require('express');
const router = express.Router();
const projects = require('../data/projects.json');

// GET all projects
router.get('/', (req, res) => {
  res.json(projects);
});

// GET project by ID
router.get('/:id', (req, res) => {
  const project = projects.find(p => p.id === parseInt(req.params.id));
  if (!project) {
    return res.status(404).json({ error: 'Project not found' });
  }
  res.json(project);
});

module.exports = router;
