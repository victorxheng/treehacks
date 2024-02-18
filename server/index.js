const express = require('express');
const { exec } = require('child_process');
const app = express();
const cors = require('cors');

app.use(cors());
const port = 3001; // Ensure this port is different from your React app's port

app.use(express.json());
require('dotenv').config();
const { Configuration, OpenAI } = require("openai");

const openai = new OpenAI(process.env.OPENAI_API_KEY);


app.post('/create-structure', (req, res) => {
  exec('node create-structure.js', (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      return res.status(500).send('Failed to create structure');
    }
    console.log(`stdout: ${stdout}`);
    console.error(`stderr: ${stderr}`);
    res.send('Project structure created successfully');
  });
});


app.post('/addServerFiles', (req, res) => {
  exec('node functions/addServerFiles.js', (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      return res.status(500).send('Failed to create structure');
    }
    console.log(`stdout: ${stdout}`);
    console.error(`stderr: ${stderr}`);
    res.send('Project structure created successfully');
  });
});

app.post('/addFrontendFiles', (req, res) => {
  exec('node functions/addFrontendFiles.js', (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      return res.status(500).send('Failed to create structure');
    }
    console.log(`stdout: ${stdout}`);
    console.error(`stderr: ${stderr}`);
    res.send('Project structure created successfully');
  });
});

// generateDescriptionsForProjectStructure(projectStructure)
//   .then(fileList => console.log(fileList))
//   .catch(error => console.error(error));

// GET route to fetch description
// look at prompt1.txt for a prompt example
app.get('/generate-description', async (req, res) => {
  try {
    // Extracting query parameters from the GET request
    const { prompt } = req.query;

    if (!prompt) {
      return res.status(400).json({ error: "Prompt is required" });
    }

    const response = await openai.createCompletion({
      model: "text-davinci-003",
      prompt: prompt,
      max_tokens: 1024,
      temperature: 0.5,
    });

    const description = response.data.choices[0].text.trim();

    // Sending back the generated description as JSON
    res.json({ description });
  } catch (error) {
    console.error("Error generating description:", error);
    res.status(500).json({ error: "Failed to generate description" });
  }
});

app.listen(port, () => {
  console.log(`Backend server listening at http://localhost:${port}`);
});
