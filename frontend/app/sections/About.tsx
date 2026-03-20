'use client';

import { motion } from 'framer-motion';
import { useInView } from 'framer-motion';
import { useRef } from 'react';
import { Shield, Cloud, Terminal, Zap, Award, BookOpen } from 'lucide-react';

const stats = [
  { icon: Zap, value: '2+', label: 'Years Experience' },
  { icon: Award, value: '15+', label: 'Projects Completed' },
  { icon: BookOpen, value: '10+', label: 'Technologies' },
];

const highlights = [
  {
    icon: Shield,
    title: 'Ethical Hacking',
    description: 'Skilled in penetration testing, vulnerability assessment, and security analysis using Kali Linux, Burp Suite, and Metasploit.',
  },
  {
    icon: Terminal,
    title: 'Automation Projects',
    description: 'Built Python automation tools for email processing, WhatsApp messaging, and security task automation to boost productivity.',
  },
  {
    icon: Cloud,
    title: 'Cloud Skills',
    description: 'Hands-on experience with AWS services (EC2, S3, IAM, CLI) and Linux server management from internship experience.',
  },
];

export default function About() {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, margin: '-100px' });

  return (
    <section id="about" className="py-24 relative overflow-hidden">
      {/* Background Elements */}
      <div className="absolute top-0 left-0 w-full h-full grid-overlay opacity-50" />
      <div className="absolute top-1/2 left-0 w-96 h-96 bg-accent-purple/10 rounded-full blur-3xl" />

      <div className="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <motion.div
          ref={ref}
          initial={{ opacity: 0, y: 40 }}
          animate={isInView ? { opacity: 1, y: 0 } : {}}
          transition={{ duration: 0.8 }}
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
              About Me
            </motion.span>
            <motion.h2
              initial={{ opacity: 0, y: 20 }}
              animate={isInView ? { opacity: 1, y: 0 } : {}}
              transition={{ delay: 0.3 }}
              className="text-4xl sm:text-5xl font-bold mb-6"
            >
              Passionate <span className="text-gradient">Developer</span> & Security Enthusiast
            </motion.h2>
          </div>

          {/* Stats */}
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={isInView ? { opacity: 1, y: 0 } : {}}
            transition={{ delay: 0.4 }}
            className="grid grid-cols-3 gap-6 mb-16"
          >
            {stats.map((stat, index) => (
              <motion.div
                key={stat.label}
                initial={{ opacity: 0, scale: 0.9 }}
                animate={isInView ? { opacity: 1, scale: 1 } : {}}
                transition={{ delay: 0.5 + index * 0.1 }}
                className="text-center p-6 glass rounded-2xl"
              >
                <stat.icon className="w-8 h-8 text-accent-cyan mx-auto mb-3" />
                <div className="text-3xl sm:text-4xl font-bold text-white mb-1">{stat.value}</div>
                <div className="text-sm text-gray-400">{stat.label}</div>
              </motion.div>
            ))}
          </motion.div>

          {/* Introduction */}
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={isInView ? { opacity: 1, y: 0 } : {}}
            transition={{ delay: 0.6 }}
            className="glass rounded-3xl p-8 sm:p-12 mb-16"
          >
            <p className="text-lg sm:text-xl text-gray-300 leading-relaxed mb-6">
              I&apos;m a passionate <span className="text-accent-cyan font-semibold">Full Stack Developer</span> with a strong foundation in modern web technologies and an insatiable curiosity for cybersecurity and cloud computing. My journey in tech is driven by the desire to create secure, efficient, and scalable solutions that make a real impact.
            </p>
            <p className="text-lg text-gray-400 leading-relaxed">
              With hands-on experience in both frontend and backend development, I bring ideas to life through clean, maintainable code and intuitive user experiences. My expertise spans from building responsive web applications to implementing robust security measures and automating complex workflows.
            </p>
          </motion.div>

          {/* Highlights */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {highlights.map((item, index) => (
              <motion.div
                key={item.title}
                initial={{ opacity: 0, y: 30 }}
                animate={isInView ? { opacity: 1, y: 0 } : {}}
                transition={{ delay: 0.8 + index * 0.1 }}
                whileHover={{ y: -5 }}
                className="glass rounded-2xl p-6 hover:border-accent-cyan/30 transition-all duration-300"
              >
                <div className="w-12 h-12 rounded-xl bg-gradient-to-br from-accent-cyan/20 to-accent-purple/20 flex items-center justify-center mb-4">
                  <item.icon className="w-6 h-6 text-accent-cyan" />
                </div>
                <h3 className="text-xl font-semibold text-white mb-2">{item.title}</h3>
                <p className="text-gray-400 text-sm leading-relaxed">{item.description}</p>
              </motion.div>
            ))}
          </div>
        </motion.div>
      </div>
    </section>
  );
}
