'use client';

import { motion, useInView } from 'framer-motion';
import { useRef, useState } from 'react';
import { 
  Mail, 
  Github, 
  Linkedin, 
  Phone, 
  MapPin, 
  MessageSquare,
  Send,
  ArrowUpRight
} from 'lucide-react';

const contactLinks = [
  {
    icon: Mail,
    label: 'Email',
    value: 'nikuluhach.86209@gmail.com',
    href: 'mailto:nikuluhach.86209@gmail.com',
    color: 'from-red-500 to-orange-500',
  },
  {
    icon: Github,
    label: 'GitHub',
    value: '@TheNikhilLuhach',
    href: 'https://github.com/TheNikhilLuhach',
    color: 'from-gray-600 to-gray-800',
  },
  {
    icon: Linkedin,
    label: 'LinkedIn',
    value: 'Nikhil Kumar',
    href: '#',
    color: 'from-blue-600 to-blue-800',
  },
  {
    icon: Phone,
    label: 'Phone',
    value: '+91 7297072067',
    href: 'tel:+917297072067',
    color: 'from-green-500 to-emerald-600',
  },
];

export default function Contact() {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, margin: '-100px' });
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    subject: '',
    message: '',
  });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSubmitting(true);
    
    // Simulate form submission
    await new Promise((resolve) => setTimeout(resolve, 1500));
    
    setIsSubmitting(false);
    setSubmitted(true);
    setFormData({ name: '', email: '', subject: '', message: '' });
    
    setTimeout(() => setSubmitted(false), 5000);
  };

  return (
    <section id="contact" className="py-24 relative overflow-hidden">
      {/* Background */}
      <div className="absolute top-0 left-0 w-full h-full grid-overlay opacity-30" />
      <div className="absolute bottom-0 left-1/3 w-96 h-96 bg-accent-purple/10 rounded-full blur-3xl" />
      <div className="absolute top-1/4 right-0 w-96 h-96 bg-accent-cyan/10 rounded-full blur-3xl" />

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
              <MessageSquare className="w-4 h-4 inline mr-2" />
              Get in Touch
            </motion.span>
            <motion.h2
              initial={{ opacity: 0, y: 20 }}
              animate={isInView ? { opacity: 1, y: 0 } : {}}
              transition={{ delay: 0.3 }}
              className="text-4xl sm:text-5xl font-bold mb-6"
            >
              Let&apos;s <span className="text-gradient">Connect</span>
            </motion.h2>
            <motion.p
              initial={{ opacity: 0 }}
              animate={isInView ? { opacity: 1 } : {}}
              transition={{ delay: 0.4 }}
              className="text-gray-400 max-w-2xl mx-auto"
            >
              I&apos;m always open to discussing new projects, creative ideas, or opportunities to be part of your visions.
            </motion.p>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
            {/* Contact Info */}
            <motion.div
              initial={{ opacity: 0, x: -30 }}
              animate={isInView ? { opacity: 1, x: 0 } : {}}
              transition={{ delay: 0.5 }}
              className="space-y-4"
            >
              {contactLinks.map((link, index) => (
                <motion.a
                  key={link.label}
                  href={link.href}
                  target={link.href.startsWith('http') ? '_blank' : undefined}
                  rel={link.href.startsWith('http') ? 'noopener noreferrer' : undefined}
                  initial={{ opacity: 0, y: 20 }}
                  animate={isInView ? { opacity: 1, y: 0 } : {}}
                  transition={{ delay: 0.6 + index * 0.1 }}
                  whileHover={{ x: 5 }}
                  className="group flex items-center gap-4 p-4 glass rounded-xl hover:border-accent-cyan/30 transition-all"
                >
                  <div className={`w-12 h-12 rounded-xl bg-gradient-to-br ${link.color} flex items-center justify-center`}>
                    <link.icon className="w-6 h-6 text-white" />
                  </div>
                  <div className="flex-1">
                    <p className="text-sm text-gray-400">{link.label}</p>
                    <p className="text-white font-medium">{link.value}</p>
                  </div>
                  <ArrowUpRight className="w-5 h-5 text-gray-400 group-hover:text-accent-cyan transition-colors" />
                </motion.a>
              ))}

              {/* Location Card */}
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={isInView ? { opacity: 1, y: 0 } : {}}
                transition={{ delay: 1 }}
                className="p-4 glass rounded-xl"
              >
                <div className="flex items-center gap-3 mb-2">
                  <MapPin className="w-5 h-5 text-accent-cyan" />
                  <span className="text-white font-medium">Location</span>
                </div>
                <p className="text-gray-400 pl-8">India</p>
              </motion.div>
            </motion.div>

            {/* Contact Form */}
            <motion.div
              initial={{ opacity: 0, x: 30 }}
              animate={isInView ? { opacity: 1, x: 0 } : {}}
              transition={{ delay: 0.5 }}
              className="glass rounded-2xl p-6 sm:p-8"
            >
              <h3 className="text-xl font-semibold text-white mb-6">
                Send a Message
              </h3>

              {submitted ? (
                <motion.div
                  initial={{ opacity: 0, scale: 0.9 }}
                  animate={{ opacity: 1, scale: 1 }}
                  className="text-center py-12"
                >
                  <div className="w-16 h-16 rounded-full bg-accent-emerald/20 flex items-center justify-center mx-auto mb-4">
                    <Send className="w-8 h-8 text-accent-emerald" />
                  </div>
                  <h4 className="text-xl font-semibold text-white mb-2">Message Sent!</h4>
                  <p className="text-gray-400">Thank you for reaching out. I&apos;ll get back to you soon.</p>
                </motion.div>
              ) : (
                <form onSubmit={handleSubmit} className="space-y-4">
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <input
                      type="text"
                      placeholder="Your Name"
                      required
                      value={formData.name}
                      onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                      className="w-full px-4 py-3 rounded-xl bg-dark-800 border border-dark-600 text-white placeholder-gray-500 focus:outline-none focus:border-accent-cyan/50 transition-colors"
                    />
                    <input
                      type="email"
                      placeholder="Your Email"
                      required
                      value={formData.email}
                      onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                      className="w-full px-4 py-3 rounded-xl bg-dark-800 border border-dark-600 text-white placeholder-gray-500 focus:outline-none focus:border-accent-cyan/50 transition-colors"
                    />
                  </div>
                  <input
                    type="text"
                    placeholder="Subject"
                    required
                    value={formData.subject}
                    onChange={(e) => setFormData({ ...formData, subject: e.target.value })}
                    className="w-full px-4 py-3 rounded-xl bg-dark-800 border border-dark-600 text-white placeholder-gray-500 focus:outline-none focus:border-accent-cyan/50 transition-colors"
                  />
                  <textarea
                    placeholder="Your Message"
                    required
                    rows={5}
                    value={formData.message}
                    onChange={(e) => setFormData({ ...formData, message: e.target.value })}
                    className="w-full px-4 py-3 rounded-xl bg-dark-800 border border-dark-600 text-white placeholder-gray-500 focus:outline-none focus:border-accent-cyan/50 transition-colors resize-none"
                  />
                  <motion.button
                    type="submit"
                    disabled={isSubmitting}
                    whileHover={{ scale: 1.02 }}
                    whileTap={{ scale: 0.98 }}
                    className="w-full py-4 bg-gradient-to-r from-accent-cyan to-accent-purple rounded-xl font-semibold text-white hover:shadow-lg hover:shadow-accent-cyan/25 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
                  >
                    {isSubmitting ? (
                      <>
                        <div className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                        Sending...
                      </>
                    ) : (
                      <>
                        <Send className="w-5 h-5" />
                        Send Message
                      </>
                    )}
                  </motion.button>
                </form>
              )}
            </motion.div>
          </div>
        </motion.div>
      </div>
    </section>
  );
}
