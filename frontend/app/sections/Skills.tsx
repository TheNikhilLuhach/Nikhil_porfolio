'use client';

import { motion, useInView } from 'framer-motion';
import { useRef, useState } from 'react';
import { 
  Code2, 
  Globe, 
  Wrench, 
  Cloud, 
  Shield, 
  Database,
  Cpu,
  ChevronRight
} from 'lucide-react';

const skillCategories = [
  {
    icon: Code2,
    title: 'Programming Languages',
    color: 'from-accent-cyan to-accent-purple',
    skills: [
      { name: 'Python', level: 90 },
      { name: 'JavaScript', level: 85 },
      { name: 'Java', level: 75 },
      { name: 'C / C++', level: 70 },
      { name: 'Bash/Shell', level: 65 },
    ],
  },
  {
    icon: Globe,
    title: 'Web Development',
    color: 'from-accent-purple to-accent-pink',
    skills: [
      { name: 'React / Next.js', level: 85 },
      { name: 'HTML5 / CSS3', level: 90 },
      { name: 'Node.js', level: 80 },
      { name: 'Flask / FastAPI', level: 85 },
      { name: 'REST APIs', level: 88 },
    ],
  },
  {
    icon: Wrench,
    title: 'Tools & Platforms',
    color: 'from-accent-pink to-accent-emerald',
    skills: [
      { name: 'Git & GitHub', level: 90 },
      { name: 'Docker', level: 75 },
      { name: 'VS Code', level: 95 },
      { name: 'Postman', level: 85 },
      { name: 'VirtualBox', level: 80 },
    ],
  },
  {
    icon: Cloud,
    title: 'Cloud & DevOps',
    color: 'from-accent-emerald to-accent-cyan',
    skills: [
      { name: 'AWS (EC2, S3, IAM)', level: 80 },
      { name: 'Linux Server Mgmt', level: 85 },
      { name: 'CI/CD (GitHub Actions)', level: 70 },
      { name: 'AWS CLI', level: 75 },
    ],
  },
  {
    icon: Shield,
    title: 'Cybersecurity',
    color: 'from-accent-cyan to-accent-purple',
    skills: [
      { name: 'Kali Linux', level: 85 },
      { name: 'Burp Suite', level: 80 },
      { name: 'Nmap / Wireshark', level: 75 },
      { name: 'Metasploit', level: 70 },
      { name: 'Vulnerability Analysis', level: 78 },
    ],
  },
  {
    icon: Database,
    title: 'Databases',
    color: 'from-accent-purple to-accent-pink',
    skills: [
      { name: 'MongoDB', level: 85 },
      { name: 'MySQL', level: 80 },
      { name: 'Database Design', level: 75 },
    ],
  },
];

function SkillCard({ category, index }: { category: typeof skillCategories[0]; index: number }) {
  const [isExpanded, setIsExpanded] = useState(false);
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, margin: '-50px' });

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 40 }}
      animate={isInView ? { opacity: 1, y: 0 } : {}}
      transition={{ delay: index * 0.1, duration: 0.6 }}
      className="glass rounded-2xl overflow-hidden"
    >
      <button
        onClick={() => setIsExpanded(!isExpanded)}
        className="w-full p-6 text-left flex items-center justify-between group"
      >
        <div className="flex items-center gap-4">
          <div className={`w-12 h-12 rounded-xl bg-gradient-to-br ${category.color} p-0.5`}>
            <div className="w-full h-full rounded-xl bg-dark-800 flex items-center justify-center">
              <category.icon className="w-6 h-6 text-white" />
            </div>
          </div>
          <h3 className="text-lg font-semibold text-white">{category.title}</h3>
        </div>
        <ChevronRight 
          className={`w-5 h-5 text-gray-400 transition-transform duration-300 ${isExpanded ? 'rotate-90' : ''}`} 
        />
      </button>
      
      <motion.div
        initial={false}
        animate={{ height: isExpanded ? 'auto' : 0, opacity: isExpanded ? 1 : 0 }}
        className="overflow-hidden"
      >
        <div className="px-6 pb-6 space-y-4">
          {category.skills.map((skill, skillIndex) => (
            <div key={skill.name}>
              <div className="flex justify-between mb-1.5">
                <span className="text-sm text-gray-300">{skill.name}</span>
                <span className="text-sm text-accent-cyan">{skill.level}%</span>
              </div>
              <div className="h-2 bg-dark-600 rounded-full overflow-hidden">
                <motion.div
                  initial={{ width: 0 }}
                  animate={isExpanded ? { width: `${skill.level}%` } : { width: 0 }}
                  transition={{ delay: skillIndex * 0.1, duration: 0.6, ease: 'easeOut' }}
                  className={`h-full rounded-full bg-gradient-to-r ${category.color}`}
                />
              </div>
            </div>
          ))}
        </div>
      </motion.div>
    </motion.div>
  );
}

export default function Skills() {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, margin: '-100px' });

  return (
    <section id="skills" className="py-24 relative overflow-hidden">
      {/* Background */}
      <div className="absolute top-0 left-0 w-full h-full grid-overlay opacity-30" />
      <div className="absolute top-1/3 right-0 w-96 h-96 bg-accent-cyan/10 rounded-full blur-3xl" />

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
              <Cpu className="w-4 h-4 inline mr-2" />
              Technical Expertise
            </motion.span>
            <motion.h2
              initial={{ opacity: 0, y: 20 }}
              animate={isInView ? { opacity: 1, y: 0 } : {}}
              transition={{ delay: 0.3 }}
              className="text-4xl sm:text-5xl font-bold mb-6"
            >
              Skills & <span className="text-gradient">Technologies</span>
            </motion.h2>
            <motion.p
              initial={{ opacity: 0 }}
              animate={isInView ? { opacity: 1 } : {}}
              transition={{ delay: 0.4 }}
              className="text-gray-400 max-w-2xl mx-auto"
            >
              A comprehensive toolkit spanning development, security, and cloud infrastructure.
              Click on any category to explore detailed proficiency levels.
            </motion.p>
          </div>

          {/* Skills Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {skillCategories.map((category, index) => (
              <SkillCard key={category.title} category={category} index={index} />
            ))}
          </div>
        </motion.div>
      </div>
    </section>
  );
}
