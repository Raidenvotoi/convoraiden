// Find all elements with jsname="N9Xkfe"
var elements = document.querySelectorAll('[jsname="N9Xkfe"]');

// Loop through each element
for (let index = 0; index < elements.length; index++) {
    

  // Get the source of the image
  var imageUrl = element[index].src;

  // Fetch the image data
  fetch(imageUrl)
    .then(response => response.blob())
    .then(blob => {
      // Create a URL for the blob
      var blobUrl = URL.createObjectURL(blob);

      // Create an anchor element to download the image
      var a = document.createElement('a');
      a.href = blobUrl;
      a.download = 'image_' + index + '.jpg'; // You can change the filename as needed
      document.body.appendChild(a);
      a.click();

      // Cleanup
      window.URL.revokeObjectURL(blobUrl);
      document.body.removeChild(a);
    })
    .catch(error => {
      console.error('Error fetching image:', error);
    });
};