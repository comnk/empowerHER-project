import React, { useState } from 'react';
import "./ProfessorComponent.css";

function ProfessorComponent(props) {
    const [expanded, setExpanded] = useState(false);
    const { professorInformation } = props;
    return (
      <div className="movie">
        <p>{professorInformation.name}</p>
        <span className="showMore" onClick={() => setExpanded(!expanded)}>
          <b>Read More</b>
        </span>
        {expanded ? (
          <div className="expandable">
            <p><strong>Number of Publications:</strong> {professorInformation.number_of_publications}</p>
            <p><strong>University:</strong> {professorInformation.university}</p>
            <p><strong>Actors:</strong></p>
            <ul>
              {professorInformation.top_papers.map((actor) => (
                <li key={actor}>{actor}</li>
              ))}
            </ul>
          </div>
        ) : null}
      </div>
    );
}

export default ProfessorComponent;