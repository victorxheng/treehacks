const fs = require('fs');
const path = require('path');

const projectStructure = {
  src: {
    'assets': {},
    'components': {},
    'config': {},
    'features': {
      'awesome-feature': {
        'api': {},
        'assets': {},
        'components': {},
        'hooks': {},
        'routes': {},
        'stores': {},
        'types': {},
        'utils': {},
        'index.ts': `// Export the public API of the awesome-feature\n`
      }
    },
    'hooks': {},
    'lib': {},
    'providers': {},
    'routes': {},
    'stores': {},
    'test': {},
    'types': {},
    'utils': {},
  },
  server: {
    'controllers': {},
    'middlewares': {},
    'models': {},
    'routes': {},
    'services': {},
    'utils': {}
  }
};


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

createDirectoryContents(projectStructure, '.');
console.log('Project structure created successfully.');
