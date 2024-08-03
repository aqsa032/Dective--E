chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.action === 'detectDarkPatterns') {
      // Implement logic to detect dark patterns on the webpage
      const detectedPatterns = detectDarkPatterns();
      const message = `Detected ${detectedPatterns.length} dark patterns.`;
      sendResponse({ message });
    }
  });
  

 

// Function to detect deceptive buttons
function detectDeceptiveButtons() {
    const deceptiveButtons = document.querySelectorAll('button.deceptive');
    return Array.from(deceptiveButtons).map(button => button.innerText);
  }
  
  // Send detected deceptive buttons to background script
  chrome.runtime.sendMessage({ action: 'deceptiveButtons', buttons: detectDeceptiveButtons() });
  