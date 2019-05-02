const KerasJS = require('keras-js')

const model = new KerasJS.Model({
  filepath: 'C:/Users/Krishna/Desktop/DBMS/sentimentanalysis.bin',
  filesystem: true,
  pauseAfterLayerCalls: true
})

model
  .ready()
  .then(() => {
    // input data object keyed by names of the input layers
    // or `input` for Sequential models
    // values are the flattened Float32Array data
    // (input tensor shapes are specified in the model config)
    data = ["It is a very bad movie and very disgusting"]
    vocabulary = data[0].split()
    const parse = (t) => vocabulary.map((w, i) => t.reduce((a, b) => b === w ? ++a : a , 0))
    data = parse(data)
    const inputData = {
     input_1:  new Float32Array(data)
   }
    // make predictions
    return model.predict(inputData)
  })
  .then(outputData => {
      console.log(outputData)
  })
  .catch(err => {
    console.log(err)
  })
