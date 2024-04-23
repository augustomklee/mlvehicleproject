// // Get the image element
// const imageElement = document.getElementById('image');

// // Function to handle button click event
// function handleButtonClick() {
//   // Call the Flask backend API for model prediction with correct settings
//   fetch('http://localhost:5000/api/predict')
//   .then(response => response.json())
//   .then(prediction => {
//     // Handle the prediction result
//     console.log(prediction);
//     // Do something with the prediction result, e.g., display it on the webpage
//     document.getElementById('prediction-result').textContent = 'Prediction: ' + prediction.prediction;
//   })
//   .catch(error => {
//     console.error('Error:', error);
//     document.getElementById('prediction-result').textContent = 'Error retrieving prediction.';
//   });
// }

// // Add event listener to the button
// const buttonElement = document.getElementById('guess-button');
// buttonElement.addEventListener('click', handleButtonClick);
// Function to handle button click event
function handleButtonClick() {
  // Call the Flask backend API for model prediction with correct settings
  fetch('http://localhost:5000/api/predict')
  .then(response => response.json())
  .then(data => {
    // Handle the prediction results
    const predictions = data.predictions; // Adjust this if the key is different
    const resultsContainer = document.getElementById('prediction-result');
    
    // Clear previous results
    resultsContainer.innerHTML = '';

    // Create and append a list item for each prediction
    predictions.forEach((item, index) => {
      const [imageName, prediction] = item; // Destructure the tuple
      const listItem = document.createElement('li');
      listItem.textContent = `${imageName}: ${prediction}`;
      resultsContainer.appendChild(listItem);
    });
  })
  .catch(error => {
    console.error('Error:', error);
    document.getElementById('prediction-result').textContent = 'Error retrieving predictions.';
  });
}

// Add event listener to the button
const buttonElement = document.getElementById('guess-button');
buttonElement.addEventListener('click', handleButtonClick);
