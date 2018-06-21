const axios = require('axios')
const intentTemplate = require('./input/intentTemplate')
const DEVELOPER_ACCESS_KEY = require('./creds/'+process.env.NODE_ENV+'/dialogflow_config').DEVELOPER_ACCESS_KEY

const headers = {
  headers: {
    Authorization: `Bearer ${DEVELOPER_ACCESS_KEY}`
  }
}

const body = intentTemplate

axios.post('https://api.dialogflow.com/v1/intents', body, headers)
