const axios = require('axios')
const fs = require('fs')
const DEVELOPER_ACCESS_KEY = require('./creds/'+process.env.NODE_ENV+'/dialogflow_config').DEVELOPER_ACCESS_KEY
const SAMPLE_TEXT = require('./input/text')

const headers = {
  headers: {
    Authorization: `Bearer ${DEVELOPER_ACCESS_KEY}`
  }
}

const callDialogFlow = (texts) => {
  console.log('worked')
  const allTexts = texts.map((text) => {
    const params = {
      "contexts": [],
      "lang": "en",
      "query": text,
      "sessionId": 'PLACEHOLDER_SESSION_ID',
      "timezone": "America/New_York"
    }
    return axios.post(`https://api.dialogflow.com/api/query?v=20150910`, params, headers)
  })
  Promise.all(allTexts).then((data) => {
    console.log('======== SUCCESSFULLY HIT DIALOGFLOW FOR ALL SENTENCES ========')
    const allResults = data.map(d => d.data)
    console.log(allResults)
    fs.writeFile(`./output/sample_output.json`, JSON.stringify(allResults, null, 4), function(err) {
      if(err) {
          return console.log(err);
      }
      console.log('---> Saved the responses from DialogFlow (output/sample_output.json)')
      console.log('======== DONE ========')
    })
  })
  .catch((err) => {
    console.log('======== ERROR OCCURRED ========')
    console.log(err)
  })
}

const preprocess = (string) => {
  // this function could be improved to actually split on . , ! ?
  var seperators = []
  var segments = []

  //stores index location of punctuation, so string can be seperated at those indices
  for (var i = 0; i < string.length; i++) {
    if (string[i] === '.' || string[i] === '!' || string[i] === '?') {
      seperators.push(i)
    }
  }

  //adds seperated strings to segments list object for the start, middle and end elements
  for (var n = 0; n < seperators.length; n++) {
    if ((n-1) < 0) {

      segments.push(string.slice(0,seperators[n]) + string[seperators[n]])
    }
    else if (n >= seperators.length) {
      segments.push(string.slice(seperators[n-1]+1,string.length) + string[len(seperators)+1])
    }
    else {
      segments.push(string.slice(seperators[n-1]+1,seperators[n]) + string[seperators[n]])
    }
  }
  console.log(segments)
  return segments
}

// RUN THE SCRIPT
callDialogFlow(preprocess(SAMPLE_TEXT))
