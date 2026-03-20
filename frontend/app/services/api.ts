export interface Project {
  id: number;
  name: string;
  description: string;
  tech: string[];
  liveLink: string;
  githubLink: string;
}

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:5000';

export async function getProjects(): Promise<Project[]> {
  try {
    const response = await fetch(`${API_BASE_URL}/api/projects`);
    if (!response.ok) {
      throw new Error('Failed to fetch projects');
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching projects:', error);
    throw error;
  }
}

export async function getSkills() {
  try {
    const response = await fetch(`${API_BASE_URL}/api/skills`);
    if (!response.ok) {
      throw new Error('Failed to fetch skills');
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching skills:', error);
    throw error;
  }
}

export async function getExperience() {
  try {
    const response = await fetch(`${API_BASE_URL}/api/experience`);
    if (!response.ok) {
      throw new Error('Failed to fetch experience');
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching experience:', error);
    throw error;
  }
}
