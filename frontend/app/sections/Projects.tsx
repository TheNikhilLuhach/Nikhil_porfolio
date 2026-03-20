'use client';

import { motion, useInView, AnimatePresence } from 'framer-motion';
import { useRef, useEffect, useState } from 'react';
import { 
  ExternalLink, 
  Github, 
  Layers, 
  Loader2,
  Folder,
  Code,
  Sparkles
} from 'lucide-react';
import { getProjects, Project } from '@/app/services/api';

const techColors: Record<string, string> = {
  Python: 'bg-yellow-500/20 text-yellow-300 border-yellow-500/30',
  JavaScript: 'bg-yellow-400/20 text-yellow-200 border-yellow-400/30',
  React: 'bg-cyan-500/20 text-cyan-300 border-cyan-500/30',
  'Next.js': 'bg-gray-500/20 text-gray-300 border-gray-500/30',
  Node: 'bg-green-500/20 text-green-300 border-green-500/30',
  Express: 'bg-gray-400/20 text-gray-300 border-gray-400/30',
  MongoDB: 'bg-green-600/20 text-green-400 border-green-600/30',
  MySQL: 'bg-blue-500/20 text-blue-300 border-blue-500/30',
  Flask: 'bg-gray-300/20 text-gray-200 border-gray-300/30',
  FastAPI: 'bg-teal-500/20 text-teal-300 border-teal-500/30',
  Docker: 'bg-blue-600/20 text-blue-400 border-blue-600/30',
  AWS: 'bg-orange-500/20 text-orange-300 border-orange-500/30',
  Automation: 'bg-purple-500/20 text-purple-300 border-purple-500/30',
  'Machine Learning': 'bg-pink-500/20 text-pink-300 border-pink-500/30',
  AI: 'bg-rose-500/20 text-rose-300 border-rose-500/30',
  Security: 'bg-red-500/20 text-red-300 border-red-500/30',
  'Computer Vision': 'bg-indigo-500/20 text-indigo-300 border-indigo-500/30',
};

function getTechColor(tech: string): string {
  return techColors[tech] || 'bg-accent-cyan/20 text-accent-cyan border-accent-cyan/30';
}

function ProjectCard({ project, index }: { project: Project; index: number }) {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, margin: '-50px' });
  const [isHovered, setIsHovered] = useState(false);

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 40 }}
      animate={isInView ? { opacity: 1, y: 0 } : {}}
      transition={{ delay: index * 0.1, duration: 0.6 }}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
      className="group relative glass rounded-2xl overflow-hidden hover:border-accent-cyan/30 transition-all duration-500"
    >
      {/* Glow Effect */}
      <div className={`absolute inset-0 bg-gradient-to-br from-accent-cyan/10 to-accent-purple/10 opacity-0 group-hover:opacity-100 transition-opacity duration-500`} />
      
      <div className="relative p-6">
        {/* Icon */}
        <div className="w-14 h-14 rounded-xl bg-gradient-to-br from-accent-cyan/20 to-accent-purple/20 flex items-center justify-center mb-4 group-hover:scale-110 transition-transform duration-300">
          <Folder className="w-7 h-7 text-accent-cyan" />
        </div>

        {/* Title */}
        <h3 className="text-xl font-semibold text-white mb-2 group-hover:text-accent-cyan transition-colors">
          {project.name}
        </h3>

        {/* Description */}
        <p className="text-gray-400 text-sm mb-4 line-clamp-3 leading-relaxed">
          {project.description}
        </p>

        {/* Tech Stack */}
        <div className="flex flex-wrap gap-2 mb-6">
          {project.tech.slice(0, 4).map((tech) => (
            <span
              key={tech}
              className={`px-2.5 py-1 rounded-full text-xs font-medium border ${getTechColor(tech)}`}
            >
              {tech}
            </span>
          ))}
          {project.tech.length > 4 && (
            <span className="px-2.5 py-1 rounded-full text-xs font-medium bg-dark-600 text-gray-400">
              +{project.tech.length - 4}
            </span>
          )}
        </div>

        {/* Links */}
        <div className="flex gap-3">
          {project.githubLink && (
            <motion.a
              href={project.githubLink}
              target="_blank"
              rel="noopener noreferrer"
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              className="flex-1 flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-dark-700 hover:bg-dark-600 text-gray-300 hover:text-white transition-all text-sm font-medium"
            >
              <Github className="w-4 h-4" />
              Code
            </motion.a>
          )}
          {project.liveLink && (
            <motion.a
              href={project.liveLink}
              target="_blank"
              rel="noopener noreferrer"
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              className="flex-1 flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-gradient-to-r from-accent-cyan to-accent-purple text-white text-sm font-medium hover:shadow-lg hover:shadow-accent-cyan/25 transition-all"
            >
              <ExternalLink className="w-4 h-4" />
              Live Demo
            </motion.a>
          )}
        </div>
      </div>
    </motion.div>
  );
}

export default function Projects() {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, margin: '-100px' });
  const [projects, setProjects] = useState<Project[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchProjects = async () => {
      try {
        setLoading(true);
        const data = await getProjects();
        setProjects(data);
        setError(null);
      } catch (err) {
        setError('Failed to load projects. Please try again later.');
        // Fallback data
        setProjects([
          {
            id: 1,
            name: 'Python Automation Tool',
            description: 'A comprehensive automation suite for email processing, WhatsApp messaging, and security task automation with scheduling capabilities.',
            tech: ['Python', 'Automation', 'Security'],
            liveLink: '',
            githubLink: 'https://github.com/TheNikhilLuhach',
          },
          {
            id: 2,
            name: 'Hand Gesture Control',
            description: 'Computer vision application that enables touchless control of computer functions using hand gestures and MediaPipe.',
            tech: ['Python', 'Computer Vision', 'AI', 'OpenCV'],
            liveLink: '',
            githubLink: 'https://github.com/TheNikhilLuhach',
          },
          {
            id: 3,
            name: 'Voice Command System',
            description: 'Voice-controlled automation system for hands-free computer operation using speech recognition and NLP.',
            tech: ['Python', 'AI', 'Automation', 'NLP'],
            liveLink: '',
            githubLink: 'https://github.com/TheNikhilLuhach',
          },
          {
            id: 4,
            name: 'AI Resume Builder',
            description: 'Next-generation resume builder with AI-powered content suggestions and modern template designs.',
            tech: ['React', 'Node', 'AI', 'MongoDB'],
            liveLink: '',
            githubLink: 'https://github.com/TheNikhilLuhach',
          },
        ]);
      } finally {
        setLoading(false);
      }
    };

    fetchProjects();
  }, []);

  return (
    <section id="projects" className="py-24 relative overflow-hidden">
      {/* Background */}
      <div className="absolute top-0 left-0 w-full h-full grid-overlay opacity-30" />
      <div className="absolute bottom-0 left-1/4 w-96 h-96 bg-accent-purple/10 rounded-full blur-3xl" />

      <div className="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <motion.div
          ref={ref}
          initial={{ opacity: 0, y: 40 }}
          animate={isInView ? { opacity: 1, y: 0 } : {}}
          className="max-w-6xl mx-auto"
        >
          {/* Section Header */}
          <div className="text-center mb-16">
            <motion.span
              initial={{ opacity: 0 }}
              animate={isInView ? { opacity: 1 } : {}}
              transition={{ delay: 0.2 }}
              className="inline-block px-4 py-1.5 rounded-full glass text-accent-cyan text-sm font-medium mb-4"
            >
              <Layers className="w-4 h-4 inline mr-2" />
              Featured Work
            </motion.span>
            <motion.h2
              initial={{ opacity: 0, y: 20 }}
              animate={isInView ? { opacity: 1, y: 0 } : {}}
              transition={{ delay: 0.3 }}
              className="text-4xl sm:text-5xl font-bold mb-6"
            >
              My <span className="text-gradient">Projects</span>
            </motion.h2>
            <motion.p
              initial={{ opacity: 0 }}
              animate={isInView ? { opacity: 1 } : {}}
              transition={{ delay: 0.4 }}
              className="text-gray-400 max-w-2xl mx-auto"
            >
              A showcase of my best work, featuring automation tools, AI applications,
              and full-stack development projects.
            </motion.p>
          </div>

          {/* Loading State */}
          <AnimatePresence>
            {loading && (
              <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
                className="flex flex-col items-center justify-center py-20"
              >
                <Loader2 className="w-10 h-10 text-accent-cyan animate-spin mb-4" />
                <p className="text-gray-400">Loading projects...</p>
              </motion.div>
            )}
          </AnimatePresence>

          {/* Projects Grid */}
          {!loading && (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ delay: 0.5 }}
              className="grid grid-cols-1 md:grid-cols-2 gap-6"
            >
              {projects.map((project, index) => (
                <ProjectCard key={project.id} project={project} index={index} />
              ))}
            </motion.div>
          )}

          {/* View More */}
          {!loading && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.8 }}
              className="text-center mt-12"
            >
              <motion.a
                href="https://github.com/TheNikhilLuhach"
                target="_blank"
                rel="noopener noreferrer"
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
                className="inline-flex items-center gap-2 px-8 py-4 glass rounded-full text-gray-300 hover:text-white hover:border-accent-cyan/50 transition-all"
              >
                <Github className="w-5 h-5" />
                View More on GitHub
                <Sparkles className="w-4 h-4 text-accent-cyan" />
              </motion.a>
            </motion.div>
          )}
        </motion.div>
      </div>
    </section>
  );
}
