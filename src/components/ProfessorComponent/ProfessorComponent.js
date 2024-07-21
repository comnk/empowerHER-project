import React, { useState } from 'react';
import "./ProfessorComponent.css";

function ProfessorComponent(props) {
    const [expanded, setExpanded] = useState(false);
    const { professorInformation } = props;
    return (
      <div className="card">
        <p>{professorInformation.name}</p>
        <span className="showMore" onClick={() => setExpanded(!expanded)}>
          <b>Read More</b>
        </span>
        {expanded ? (
          <div className="expandable">
            <p><strong>Number of Publications:</strong> {professorInformation.number_of_publications}</p>
            <p><strong>University:</strong> {professorInformation.university}</p>
            <p><strong>Papers:</strong></p>
            <ul>
              {professorInformation.top_papers.map((paper) => (
                <li key={paper}>{paper}</li>
              ))}
            </ul>
          </div>
        ) : null}
      </div>
    );
}

export default ProfessorComponent;