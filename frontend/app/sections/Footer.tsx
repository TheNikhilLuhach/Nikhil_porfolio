'use client';

import { motion } from 'framer-motion';
import { Github, Linkedin, Twitter, Mail, ArrowUp } from 'lucide-react';

const socialLinks = [
  { icon: Github, href: 'https://github.com/TheNikhilLuhach', label: 'GitHub' },
  { icon: Linkedin, href: '#', label: 'LinkedIn' },
  { icon: Twitter, href: '#', label: 'Twitter' },
  { icon: Mail, href: 'mailto:nikuluhach.86209@gmail.com', label: 'Email' },
];

const navLinks = [
  { label: 'Home', href: '#home' },
  { label: 'About', href: '#about' },
  { label: 'Skills', href: '#skills' },
  { label: 'Projects', href: '#projects' },
  { label: 'Experience', href: '#experience' },
  { label: 'Contact', href: '#contact' },
];

export default function Footer() {
  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <footer className="relative py-16 overflow-hidden">
      {/* Background */}
      <div className="absolute inset-0 bg-gradient-to-t from-dark-900 via-dark-800 to-transparent" />
      <div className="absolute top-0 left-1/2 transform -translate-x-1/2 w-full max-w-4xl h-px bg-gradient-to-r from-transparent via-accent-cyan/30 to-transparent" />

      <div className="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div className="max-w-6xl mx-auto">
          {/* Main Footer Content */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-12 mb-12">
            {/* Brand */}
            <div>
              <h3 className="text-2xl font-bold text-white mb-4">
                Nikhil <span className="text-accent-cyan">Kumar</span>
              </h3>
              <p className="text-gray-400 text-sm leading-relaxed mb-6">
                Full Stack Developer & Cybersecurity Enthusiast passionate about building secure, scalable solutions.
              </p>
              {/* Social Links */}
              <div className="flex gap-3">
                {socialLinks.map((social) => (
                  <motion.a
                    key={social.label}
                    href={social.href}
                    target={social.href.startsWith('http') ? '_blank' : undefined}
                    rel={social.href.startsWith('http') ? 'noopener noreferrer' : undefined}
                    whileHover={{ scale: 1.1, y: -2 }}
                    whileTap={{ scale: 0.95 }}
                    className="w-10 h-10 rounded-lg bg-dark-700 flex items-center justify-center text-gray-400 hover:text-accent-cyan hover:bg-dark-600 transition-all"
                    aria-label={social.label}
                  >
                    <social.icon className="w-5 h-5" />
                  </motion.a>
                ))}
              </div>
            </div>

            {/* Quick Links */}
            <div>
              <h4 className="text-lg font-semibold text-white mb-4">Quick Links</h4>
              <ul className="space-y-2">
                {navLinks.map((link) => (
                  <li key={link.label}>
                    <a
                      href={link.href}
                      className="text-gray-400 hover:text-accent-cyan transition-colors text-sm"
                    >
                      {link.label}
                    </a>
                  </li>
                ))}
              </ul>
            </div>

            {/* Contact Info */}
            <div>
              <h4 className="text-lg font-semibold text-white mb-4">Contact</h4>
              <ul className="space-y-3 text-sm">
                <li className="text-gray-400">
                  <span className="text-gray-500">Email:</span>{' '}
                  <a href="mailto:nikuluhach.86209@gmail.com" className="hover:text-accent-cyan transition-colors">
                    nikuluhach.86209@gmail.com
                  </a>
                </li>
                <li className="text-gray-400">
                  <span className="text-gray-500">Phone:</span>{' '}
                  <a href="tel:+917297072067" className="hover:text-accent-cyan transition-colors">
                    +91 7297072067
                  </a>
                </li>
                <li className="text-gray-400">
                  <span className="text-gray-500">Location:</span> India
                </li>
              </ul>
            </div>
          </div>

          {/* Bottom Bar */}
          <div className="pt-8 border-t border-dark-600 flex flex-col sm:flex-row items-center justify-between gap-4">
            <p className="text-gray-500 text-sm">
              © {new Date().getFullYear()} Nikhil Kumar. All rights reserved.
            </p>
            
            {/* Back to Top */}
            <motion.button
              onClick={scrollToTop}
              whileHover={{ scale: 1.1, y: -2 }}
              whileTap={{ scale: 0.95 }}
              className="flex items-center gap-2 px-4 py-2 rounded-lg bg-dark-700 text-gray-400 hover:text-accent-cyan hover:bg-dark-600 transition-all text-sm"
            >
              Back to Top
              <ArrowUp className="w-4 h-4" />
            </motion.button>
          </div>
        </div>
      </div>
    </footer>
  );
}
