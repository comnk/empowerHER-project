import React, { useState } from 'react';
import Tabs from "./components/Tabs/Tabs";
import ProfessorComponent from './components/ProfessorComponent/ProfessorComponent';
import genderInequalityCSData from "./gender-inequality-cs-20.json";
import womenInComputingData from "./women-in-computing-20.json";
import deiData from './dei-20.json';
import "./App.css";

function App() {
  const [searchItem, setSearchItem] = useState('');
  const [professor_data, setFilteredUsers] = useState(genderInequalityCSData);

  const handleInputChange = (e) => { 
    const searchTerm = e.target.value;
    setSearchItem(searchTerm)

    const filteredItems = genderInequalityCSData.filter((user) =>
    user.name.toLowerCase().includes(searchTerm.toLowerCase())
    );

    setFilteredUsers(filteredItems);
  }

  return (
    <div className="App">
      <h1>Professor Listings & Rankings</h1>
      <Tabs>
        <div label="Gender Inequality (Computer Science)" class="topic">
          {Object.keys(genderInequalityCSData).map((id) => {
          return <ProfessorComponent key={genderInequalityCSData[id].name} professorInformation={genderInequalityCSData[id]}></ProfessorComponent>;
        })}
        </div>
        <div label="Women in Computing" class="topic">
        {Object.keys(womenInComputingData).map((id) => {
          return <ProfessorComponent key={womenInComputingData[id].name} professorInformation={womenInComputingData[id]}></ProfessorComponent>;
        })}
        </div>
        <div label="Diversity Equity Inclusion" class="topic">
        {Object.keys(deiData).map((id) => {
          return <ProfessorComponent key={deiData[id].name} professorInformation={deiData[id]}></ProfessorComponent>;
        })}
        </div>
      </Tabs>
    </div>
  );
}

export default App;
