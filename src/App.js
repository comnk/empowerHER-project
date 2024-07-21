import React, { useState } from 'react';
import Tabs from "./components/Tabs/Tabs";
import ProfessorComponent from './components/ProfessorComponent/ProfessorComponent';
import professorData from "./professor_data.json";
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
  const [searchItem, setSearchItem] = useState('');
  const [professor_data, setFilteredUsers] = useState(professorData)

  const handleInputChange = (e) => { 
    const searchTerm = e.target.value;
    setSearchItem(searchTerm)

    const filteredItems = professors_list.filter((user) =>
    user.name.toLowerCase().includes(searchTerm.toLowerCase())
    );

    setFilteredUsers(filteredItems);
  }

  return (
    <div className="App">
      <h1>Professor Listings & Rankings</h1>
      <Tabs>
        <div label="Gender & Computing" class="topic">
        <input type="text" value={searchItem} onChange={handleInputChange} placeholder='Type to search'/>
          {professor_data.map((professor) => {
          return <ProfessorComponent key={professor.name} professorInformation={professor}></ProfessorComponent>;
        })}
        </div>
        <div label="Human-Computer Interaction" class="topic">
        <input type="text" value={searchItem} onChange={handleInputChange} placeholder='Type to search'/>
        {professor_data.map((professor) => {
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
        {professor_data.map((professor) => {
          return <ProfessorComponent key={professor.name} professorInformation={professor}></ProfessorComponent>;
        })}
        </div>
      </Tabs>
    </div>
  );
}

export default App;
