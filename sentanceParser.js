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

  return segments
}
console.log(preprocess('Hello there. Is this working? Let me check! Testing! One. Two? Three!'))
