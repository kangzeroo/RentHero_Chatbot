# RentHero_Chatbot
Chatbot AI for responding to rental inquiries, pre/post processing of data, ML pipeline and general infrastructure endpoints.

The steps for using it are as follows:

0. Install dependencies with `npm install`
1. Copy and paste your email into `input/text.js`
2. Make sure there is no `output/sample_output.json`. Output from DialogFlow will be written to this file, but it won't write if there is an existing file already.
3. When you are ready to run the script, type `npm run dev`
4. Check the output folder for your output

<br />

## Notes
- You will need to add `creds/development/dialogflow_config.js` & `creds/staging/development/dialogflow_config_staging.js` credential files with the correct keys.
```javascript
const CLIENT_ACCESS_KEY = 'COPY_PASTE_KEY'
const DEVELOPER_ACCESS_KEY = 'COPY_PASTE_KEY'

module.exports = { CLIENT_ACCESS_KEY, DEVELOPER_ACCESS_KEY }
```
