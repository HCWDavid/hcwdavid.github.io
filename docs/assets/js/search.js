// Simple search functionality
document.addEventListener('DOMContentLoaded', function() {
  const searchInput = document.getElementById('search-input');
  const searchButton = document.getElementById('search-button');
  
  if (!searchInput || !searchButton) return;

  function performSearch() {
    const query = searchInput.value.trim().toLowerCase();
    
    if (!query) {
      alert('Please enter a search term');
      return;
    }

    // Get all text content on the page
    const sections = document.querySelectorAll('section p, section h1, section h2, section h3, section li');
    let found = false;
    
    // Clear previous highlights
    sections.forEach(section => {
      const text = section.textContent || section.innerText;
      section.style.backgroundColor = '';
    });

    // Search and highlight
    sections.forEach(section => {
      const text = (section.textContent || section.innerText).toLowerCase();
      if (text.includes(query)) {
        section.style.backgroundColor = '#fff3cd';
        section.style.transition = 'background-color 0.3s';
        if (!found) {
          section.scrollIntoView({ behavior: 'smooth', block: 'center' });
          found = true;
        }
        
        // Clear highlight after 3 seconds
        setTimeout(() => {
          section.style.backgroundColor = '';
        }, 3000);
      }
    });

    if (!found) {
      alert(`No results found for "${query}"`);
    }
  }

  // Search on button click
  searchButton.addEventListener('click', performSearch);
  
  // Search on Enter key
  searchInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
      performSearch();
    }
  });
});
