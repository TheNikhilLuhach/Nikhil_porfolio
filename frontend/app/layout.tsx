import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Nikhil Kumar | Full Stack Developer & Cybersecurity Enthusiast',
  description: 'Portfolio of Nikhil Kumar - Full Stack Developer, Cybersecurity Enthusiast, AWS & Automation Specialist',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className="scroll-smooth">
      <body className={`${inter.className} bg-dark-900 text-white antialiased`}>
        {children}
      </body>
    </html>
  )
}
