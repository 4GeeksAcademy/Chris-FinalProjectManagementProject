import React, { useEffect, useState } from "react";
import API from "../api";

function Projects() {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    API.get("/projects")
      .then((res) => setProjects(res.data))
      .catch((err) => console.error("Error fetching projects:", err));
  }, []);

  return (
    <div>
      <h2>Projects</h2>
      <ul>
        {projects.map((project) => (
          <li key={project.id}>
            <strong>{project.name}</strong><br />
            Manager: {project.project_manager}<br />
            Client: {project.client}<br />
            Budget: ${project.budget}<br />
            Tasks: {project.tasks}<br />
            Preferred Skills: {project.preferred_skills}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Projects;
