import React, { useState, useEffect } from 'react';
import Tabs from "./components/Tabs/Tabs";
import ProfessorComponent from './components/ProfessorComponent/ProfessorComponent';
import "./App.css";

// hardcoded to test component, replace this later
const professors_list = [
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
  const [searchItem, setSearchItem] = useState('')
  const [currentTime, setCurrentTime] = useState(0);
  const [professors, setFilteredUsers] = useState(professors_list)

  const handleInputChange = (e) => { 
    const searchTerm = e.target.value;
    setSearchItem(searchTerm)

    const filteredItems = professors_list.filter((user) =>
    user.name.toLowerCase().includes(searchTerm.toLowerCase())
    );

    setFilteredUsers(filteredItems);
  }

  useEffect(() => {
    fetch('time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

  return (
    <div className="App">
      <h1>Professor Listings & Rankings</h1>
      <Tabs>
        <div label="Gender & Computing" class="topic">
        <input type="text" value={searchItem} onChange={handleInputChange} placeholder='Type to search'/>
          {professors.map((professor) => {
          return <ProfessorComponent key={professor.name} professorInformation={professor}></ProfessorComponent>;
        })}
        </div>
        <div label="Human-Computer Interaction" class="topic">
        <input type="text" value={searchItem} onChange={handleInputChange} placeholder='Type to search'/>
        {professors.map((professor) => {
          return <ProfessorComponent key={professor.name} professorInformation={professor}></ProfessorComponent>;
        })}
        </div>
        <div label="Computer Vision" class="topic">
          Nothing to see here, this tab is <em>extinct</em>!
        </div>
        <div label="Quantum Computing" class="topic">
          Nothing to see here, this tab is <em>extinct</em>!
        </div>
        <div label="AI" class="topic">
        <input type="text" value={searchItem} onChange={handleInputChange} placeholder='Type to search'/>
        {professors.map((professor) => {
          return <ProfessorComponent key={professor.name} professorInformation={professor}></ProfessorComponent>;
        })}
        </div>
      </Tabs>
      <p>The current time is {currentTime}.</p>
    </div>
  );
}

export default App;
