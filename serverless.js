const axios = require('axios')
const DEVELOPER_ACCESS_KEY = require('./creds/'+process.env.NODE_ENV+'/dialogflow_config_staging').DEVELOPER_ACCESS_KEY
const SAMPLE_TEXT = require('./input/text')

const headers = {
  headers: {
    Authorization: `Bearer ${DEVELOPER_ACCESS_KEY}`
  }
}

const body = {
  content: SAMPLE_TEXT
}

function find_duplicates(arr) {
  let i;
  const len=arr.length;
  const result = [];
  const obj = {};
  for (i=0; i<len; i++)
  {
  obj[arr[i]]=0;
  }
  for (i in obj) {
  result.push(i);
  }
  return result;
}

axios.post('https://4htchmg8u3.execute-api.us-east-1.amazonaws.com/Dev', body, headers)
  .then((data) => {
    var inputResponses =[]
    var results = []
    for (var i = 0; i < data.data.length; i++){
      inputResponses.push(data.data[i].result.resolvedQuery)
      if (data.data[i].result.resolvedQuery.includes('\n')){
        console.log('>>>' + data.data[i].result.resolvedQuery.split('\n')[1])
      }
      else{
        console.log('>>>' + data.data[i].result.resolvedQuery)
      }
      results.push(data.data[i].result.fulfillment.speech)
      console.log('\n')
      console.log(data.data[i].result.fulfillment.speech)
      console.log('\n')
    }
  })
  .catch((err) => {
    console.log(err)
  })
