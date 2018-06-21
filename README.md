# Jakecarios McBar
This script is for playing around with DialogFlow. The steps for using it are as follows:

0. Install dependencies with `npm install`
1. Copy and paste your email into `input/text.js`
2. Make sure there is no `output/sample_output.json`. Output from DialogFlow will be written to this file, but it won't write if there is an existing file already.
3. When you are ready to run the script, type `npm run dev`
4. Check the output folder for your output

<br />

## Notes
- This script can be improved by going into `server.js` and modifying the `preprocess()` function <br />
- You will need a `creds/development/dialogflow_config.js` credentials file
