// background.js

// Listen for messages from content script
chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.action === 'deceptiveButtons') {
      // Log or process the detected deceptive buttons
      console.log('Detected Deceptive Buttons:', request.buttons);
    }
  });
  