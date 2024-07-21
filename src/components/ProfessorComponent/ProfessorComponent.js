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
            <p><strong>Paper Count:</strong> {professorInformation.paper_count}</p>
            <p><strong>Theme Papers:</strong> {professorInformation.theme_papers}</p>
            <p><strong> Most Recent Papers (Top 3):</strong></p>
            <ul>
              {professorInformation.top_papers.map((paper) => (
                <li key={paper}>{paper}</li>
              ))}
            </ul>

            <p><strong> Most Cited Papers (Top 3):</strong></p>
            <ul>
              {professorInformation.top_3_citation.map((paper) => (
                <li key={paper}>{paper}</li>
              ))}
            </ul>
          </div>
        ) : null}
      </div>
    );
}

export default ProfessorComponent;