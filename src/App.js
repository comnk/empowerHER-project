import React, { useState, useEffect } from 'react';
import Tabs from "./components/Tabs";
import ProfessorComponent from './components/ProfessorComponent/ProfessorComponent';
import "./App.css";

// hardcoded to test component, replace this later
const professors = [
  {
    name: "Steven Dow",
    number_of_publications: 4,
    university: 'University of California, San Diego',
    top_papers: ["Jennifer Coolidge", "Michael Imperioli", "Aubrey Plaza"]
  },
  {
    name: "Nadir Weibel",
    number_of_publications: 5,
    university: 'University of California, San Diego',
    top_papers: ["Brian Cox", "Sarah Snook", "Jeremy Strong"]
  },
  {
    name: "Edward Wang",
    number_of_publications: 3,
    university: 'University of California, San Diego',
    top_papers: ["Pedro Pascal", "Bella Ramsey", "Nick Offerman"]
  }
];

function App() {

  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch('time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

  return (
    <div className="App">
      <h1>Professor Listings & Rankings</h1>
      <Tabs>
        <div label="Gender & Computing">
          {professors.map((professor) => {
          return <ProfessorComponent key={professor.name} professorInformation={professor}></ProfessorComponent>;
        })}
        </div>
        <div label="Human-Computer Interaction">
          After 'while, <em>Crocodile</em>!
        </div>
        <div label="Computer Vision">
          Nothing to see here, this tab is <em>extinct</em>!
        </div>
        <div label="Quantum Computing">
          Nothing to see here, this tab is <em>extinct</em>!
        </div>
        <div label="AI">
          See ya later, <em>Alligator</em>!
        </div>
      </Tabs>
      <p>The current time is {currentTime}.</p>
    </div>
  );
}

export default App;
