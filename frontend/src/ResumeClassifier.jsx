import React, { useState } from 'react';
import axios from 'axios';

function ResumeClassifier() {
  const [file, setFile] = useState(null);
  const [category, setCategory] = useState('');
  const [confidence, setConfidence] = useState('');
  const [fileLink, setFileLink] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:5000/predict', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setCategory(response.data.category);
      setConfidence(response.data.confidence_score);
      setFileLink(response.data.file);
    } catch (error) {
      console.error('There was an error!', error);
    }
  };

  return (
    <div>
      <h1>Resume Classifier</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">Upload Resume</button>
      </form>
      {category && (
        <div>
          <h2>Predicted Category: {category}</h2>
          <h3>Confidence Score: {confidence}</h3>
          <a href={`http://localhost:5000${fileLink}`} target="_blank" rel="noopener noreferrer">
            View Resume
          </a>

        </div>
      )}
    </div>
  );
}

export default ResumeClassifier;
