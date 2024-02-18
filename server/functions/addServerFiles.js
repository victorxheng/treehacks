
const fs = require('fs');
const path = require('path');

function loadJSON(filename = '') {
    try {
      const content = fs.readFileSync(filename, 'utf-8');
      return JSON.parse(content);
    } catch (err) {
      console.error('Error loading JSON file:', err);
      process.exit(1); // Exit the process with an error code
    }
  }

function isFile(filePath) {
    try {
          const stat = fs.lstatSync(filePath);
          return stat.isFile();
    } catch (error) {
          if (error.code === 'ENOENT') {
              // The file or directory does not exist
              return false;
          }
          throw error; // Re-throw the error if it is not an ENOENT error
      }
  }
  
  function createDirectoryContents(structure, rootPath) {
    Object.entries(structure).forEach(([key, value]) => {
        const currentPath = path.join(rootPath, key);

        if (typeof value === 'object' && !isFile(currentPath)) {
            if (!fs.existsSync(currentPath)) {
                fs.mkdirSync(currentPath, { recursive: true });
            }
            createDirectoryContents(value, currentPath);
        } else {
            // Ensure the directory exists before trying to write the file
            const dir = path.dirname(currentPath);
            if (!fs.existsSync(dir)) {
                fs.mkdirSync(dir, { recursive: true });
            }
            fs.writeFileSync(currentPath, value, 'utf8');
        }
    });
  }
  
  var projectStructure = loadJSON('./data/server.json');
  createDirectoryContents(projectStructure, '.');
  console.log('Project structure created successfully.');
  