<!DOCTYPE html>
<html>
<head>
</head>
<body>
  <h1>Chicken Disease Classification</h1>
  
  <h2>Project Overview</h2>
  <p>The project focuses on the classification of poultry diseases using the VGG16 model. It aims to predict whether a chicken is healthy or has a specific disease based on fecal images. The dataset consists of poultry fecal images captured using the Open Data Kit (ODK) app on mobile phones in Arusha and Kilimanjaro regions in Tanzania between September 2020 and February 2021.</p>
  
  <h2>Data Details</h2>
  <ul>
    <li>Classes: Coccidiosis, Healthy, New Castle Disease, Salmonella</li>
    <li>Image Size: 224px by 224px</li>
  </ul>
  
  <h2>Project Structure</h2>
  <ul>
    <li>config.yaml: Configuration file for project settings</li>
    <li>secrets.yaml: Optional file for storing sensitive information</li>
    <li>params.yaml: Parameter file for model training</li>
    <li>entity: Directory for storing entities related to the project</li>
    <li>src/config: Configuration manager for the project</li>
    <li>src/components: Components of the project (data ingestion, model preparation, training, evaluation)</li>
    <li>src/pipeline: Pipeline for executing the project workflow</li>
    <li>main.py: Main script to run the project</li>
    <li>dvc.yaml: YAML file for versioning the project using DVC (Data Version Control)</li>
  </ul>
  
  <h2>Getting Started</h2>
  <p>To run the project, follow these steps:</p>
  <ol>
    <li>Update the necessary configuration files: config.yaml, secrets.yaml (optional), params.yaml</li>
    <li>Update the configuration manager in src/config</li>
    <li>Update the components for data ingestion, model preparation, training, and evaluation</li>
    <li>Update the pipeline for executing the project workflow</li>
    <li>Run main.py to start the project</li>
    <li>Use dvc.yaml for versioning and managing the project</li>
  </ol>
  
  <h2>Contributing</h2>
  <p>We welcome contributions from the community to improve our chicken disease classification project. If you have any suggestions, bug reports, or feature requests, please feel free to open an issue or submit a pull request.</p>
  
  <h2>License</h2>
  <p>This project is licensed under the MIT License.</p>
</body>
</html>
