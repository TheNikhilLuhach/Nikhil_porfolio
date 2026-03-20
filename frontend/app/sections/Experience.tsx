'use client';

import { motion, useInView } from 'framer-motion';
import { useRef } from 'react';
import { Briefcase, Calendar, MapPin, Building2 } from 'lucide-react';

const experiences = [
  {
    id: 1,
    role: 'Generative AI Trainee',
    company: 'LinuxWorld Informatics Pvt Ltd',
    location: 'Remote',
    duration: 'May 2025 – Aug 2025',
    description: 'Worked on Generative AI concepts and automation-based solutions using Python. Focused on building real-world use cases and understanding AI-driven workflows.',
    responsibilities: [
      'Developed AI-based automation systems',
      'Worked with Python for implementing AI use cases',
      'Built prompt-based and logic-driven solutions',
      'Explored real-world AI applications and integrations',
    ],
    skills: ['Generative AI', 'Python', 'Automation', 'AI Workflows', 'Prompt Engineering'],
  },
  {
    id: 2,
    role: 'Frontend Developer Intern',
    company: '1Stop.ai',
    location: 'Remote',
    duration: 'Mar 2024 – Apr 2024',
    description: 'Worked on frontend development, building responsive and user-friendly web interfaces using core web technologies.',
    responsibilities: [
      'Developed responsive websites using HTML, CSS, JavaScript',
      'Designed UI components and layouts',
      'Improved user experience and visual structure',
      'Worked on real-time frontend mini projects',
    ],
    skills: ['HTML', 'CSS', 'JavaScript', 'UI Design', 'Responsive Design'],
  },
  {
    id: 3,
    role: 'Linux & AWS Intern',
    company: 'Tech Organization',
    location: 'Remote',
    duration: '2024',
    description: 'Gained hands-on experience with AWS services including EC2, S3, and IAM. Managed Linux servers and implemented security best practices.',
    responsibilities: [
      'Managed AWS EC2 instances and S3 buckets',
      'Implemented IAM policies and security groups',
      'Automated deployment workflows with Bash scripting',
      'Configured Linux server environments',
    ],
    skills: ['AWS', 'Linux', 'EC2', 'S3', 'IAM', 'Server Management'],
  },
];

export default function Experience() {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, margin: '-100px' });

  return (
    <section id="experience" className="py-24 relative overflow-hidden">
      {/* Background */}
      <div className="absolute top-0 left-0 w-full h-full grid-overlay opacity-30" />
      <div className="absolute top-1/2 right-0 w-96 h-96 bg-accent-cyan/10 rounded-full blur-3xl" />

      <div className="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <motion.div
          ref={ref}
          initial={{ opacity: 0, y: 40 }}
          animate={isInView ? { opacity: 1, y: 0 } : {}}
          className="max-w-4xl mx-auto"
        >
          {/* Section Header */}
          <div className="text-center mb-16">
            <motion.span
              initial={{ opacity: 0 }}
              animate={isInView ? { opacity: 1 } : {}}
              transition={{ delay: 0.2 }}
              className="inline-block px-4 py-1.5 rounded-full glass text-accent-cyan text-sm font-medium mb-4"
            >
              <Briefcase className="w-4 h-4 inline mr-2" />
              Experience
            </motion.span>
            <motion.h2
              initial={{ opacity: 0, y: 20 }}
              animate={isInView ? { opacity: 1, y: 0 } : {}}
              transition={{ delay: 0.3 }}
              className="text-4xl sm:text-5xl font-bold mb-6"
            >
              Work <span className="text-gradient">Experience</span>
            </motion.h2>
          </div>

          {/* Timeline */}
          <div className="relative">
            {/* Timeline Line */}
            <div className="absolute left-4 sm:left-8 top-0 bottom-0 w-0.5 bg-gradient-to-b from-accent-cyan via-accent-purple to-transparent" />

            {/* Experience Items */}
            {experiences.map((exp, index) => (
              <motion.div
                key={exp.id}
                initial={{ opacity: 0, x: -30 }}
                animate={isInView ? { opacity: 1, x: 0 } : {}}
                transition={{ delay: 0.4 + index * 0.2 }}
                className="relative pl-12 sm:pl-20 pb-12 last:pb-0"
              >
                {/* Timeline Dot */}
                <div className="absolute left-2 sm:left-6 top-2 w-4 h-4 rounded-full bg-accent-cyan border-4 border-dark-900 shadow-lg shadow-accent-cyan/50" />

                {/* Card */}
                <motion.div
                  whileHover={{ y: -5 }}
                  className="glass rounded-2xl p-6 sm:p-8 hover:border-accent-cyan/30 transition-all duration-300"
                >
                  <div className="flex flex-col sm:flex-row sm:items-start sm:justify-between mb-4">
                    <div>
                      <h3 className="text-xl sm:text-2xl font-semibold text-white mb-1">
                        {exp.role}
                      </h3>
                      <div className="flex items-center gap-2 text-accent-cyan">
                        <Building2 className="w-4 h-4" />
                        <span className="font-medium">{exp.company}</span>
                      </div>
                    </div>
                    <div className="flex flex-col sm:items-end mt-2 sm:mt-0">
                      <div className="flex items-center gap-2 text-gray-400 text-sm">
                        <Calendar className="w-4 h-4" />
                        <span>{exp.duration}</span>
                      </div>
                      <div className="flex items-center gap-2 text-gray-500 text-sm mt-1">
                        <MapPin className="w-4 h-4" />
                        <span>{exp.location}</span>
                      </div>
                    </div>
                  </div>

                  <p className="text-gray-300 leading-relaxed mb-4">
                    {exp.description}
                  </p>

                  {/* Responsibilities */}
                  <ul className="space-y-2 mb-4">
                    {exp.responsibilities.map((item, idx) => (
                      <li key={idx} className="flex items-start gap-2 text-gray-400 text-sm">
                        <span className="w-1.5 h-1.5 rounded-full bg-accent-cyan mt-2 flex-shrink-0" />
                        <span>{item}</span>
                      </li>
                    ))}
                  </ul>

                  {/* Skills */}
                  <div className="flex flex-wrap gap-2">
                    {exp.skills.map((skill) => (
                      <span
                        key={skill}
                        className="px-3 py-1 rounded-full text-xs font-medium bg-dark-700 text-gray-300 border border-dark-600"
                      >
                        {skill}
                      </span>
                    ))}
                  </div>
                </motion.div>
              </motion.div>
            ))}
          </div>
        </motion.div>
      </div>
    </section>
  );
}
