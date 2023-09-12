# VM Setup Guide

This repository contains scripts to set up a Docker container and other utilities on a Google Cloud Platform (GCP) Deep Learning VM. Ensure that your VM has GPU drivers installed.

## Prerequisites

- Google Cloud Platform account
- Deep Learning VM with GPU drivers installed

## Installation Steps

### 1. Position the Scripts

Place all the scripts in the home directory of your VM.

### 2. Make the Shell Script Executable

To ensure the shell script is executable, run the following command:

\`\`\`bash
chmod +x startupScript.sh
\`\`\`

### 3. Build the Docker Container

To build a Docker container called \`recognition\` (required for shell script), execute the following command:

\`\`\`bash
docker build -t recognition .
\`\`\`
