// Simple search functionality - opens dedicated search page
document.addEventListener('DOMContentLoaded', function() {
  const searchInput = document.getElementById('search-input');
  const searchButton = document.getElementById('search-button');
  
  if (!searchInput || !searchButton) return;

  function performSearch() {
    const query = searchInput.value.trim();
    
    if (!query) {
      showNotification('Please enter a search term', 'error');
      return;
    }

    // Open search results page in new tab with query parameter
    const searchUrl = `./search.html?q=${encodeURIComponent(query)}`;
    window.open(searchUrl, '_blank');
    
    // Clear the search input
    searchInput.value = '';
    
    // Show feedback
    showNotification(`Searching for "${query}"...`, 'success');
  }

  // Show notification function
  function showNotification(message, type) {
    // Remove any existing notification
    const existingNotif = document.querySelector('.search-notification');
    if (existingNotif) {
      existingNotif.remove();
    }

    const notification = document.createElement('div');
    notification.className = `search-notification ${type}`;
    notification.textContent = message;
    notification.style.cssText = `
      position: fixed;
      top: 80px;
      right: 20px;
      padding: 12px 20px;
      background-color: ${type === 'success' ? '#d4edda' : '#f8d7da'};
      color: ${type === 'success' ? '#155724' : '#721c24'};
      border: 1px solid ${type === 'success' ? '#c3e6cb' : '#f5c6cb'};
      border-radius: 4px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.15);
      z-index: 10000;
      font-size: 14px;
      max-width: 300px;
      animation: slideIn 0.3s ease-out;
    `;

    document.body.appendChild(notification);

    // Remove notification after 2 seconds
    setTimeout(() => {
      notification.style.animation = 'slideOut 0.3s ease-out';
      setTimeout(() => notification.remove(), 300);
    }, 2000);
  }

  // Add CSS animations
  const style = document.createElement('style');
  style.textContent = `
    @keyframes slideIn {
      from {
        transform: translateX(400px);
        opacity: 0;
      }
      to {
        transform: translateX(0);
        opacity: 1;
      }
    }
    @keyframes slideOut {
      from {
        transform: translateX(0);
        opacity: 1;
      }
      to {
        transform: translateX(400px);
        opacity: 0;
      }
    }
  `;
  document.head.appendChild(style);

  // Search on button click
  searchButton.addEventListener('click', performSearch);
  
  // Search on Enter key
  searchInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
      performSearch();
    }
  });

  // Clear search on Escape key
  searchInput.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
      searchInput.value = '';
    }
  });
});
