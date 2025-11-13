---
layout: default
title: Search Results
---

<div id="search-page">
  <h1>🔍 Search Results</h1>
  
  <div class="search-box-container">
    <input type="text" id="search-page-input" placeholder="Search across all pages...">
    <button id="search-page-button">Search</button>
  </div>

  <div id="search-stats"></div>
  
  <div id="search-results">
    <p style="color: #666; text-align: center; padding: 40px;">Enter a search term to find content across all pages.</p>
  </div>
</div>

<style>
#search-page {
  max-width: 900px;
  margin: 0 auto;
}

#search-page h1 {
  text-align: center;
  margin-bottom: 30px;
  color: #1a1a1a;
}

.search-box-container {
  display: flex;
  gap: 0;
  margin-bottom: 30px;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  border-radius: 30px;
}

#search-page-input {
  flex: 1;
  padding: 16px 24px;
  border: 2px solid #e8e8e8;
  border-right: none;
  border-radius: 30px 0 0 30px;
  font-size: 16px;
  outline: none;
  transition: border-color 0.3s;
}

#search-page-input:focus {
  border-color: #333;
}

#search-page-button {
  padding: 16px 32px;
  background: linear-gradient(135deg, #2c3e50 0%, #1a1a1a 100%);
  color: white;
  border: none;
  border-radius: 0 30px 30px 0;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

#search-page-button:hover {
  background: linear-gradient(135deg, #1a1a1a 0%, #000 100%);
  transform: translateX(2px);
}

#search-stats {
  text-align: center;
  margin-bottom: 20px;
  font-size: 14px;
  color: #666;
}

#search-results {
  min-height: 300px;
}

.search-result-item {
  background: white;
  padding: 25px;
  margin-bottom: 20px;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  transition: all 0.3s;
  border-left: 4px solid #333;
}

.search-result-item:hover {
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
  transform: translateY(-3px);
}

.search-result-title {
  font-size: 22px;
  font-weight: 600;
  margin-bottom: 8px;
}

.search-result-title a {
  color: #1a1a1a;
  text-decoration: none;
  border-bottom: 2px solid transparent;
  transition: all 0.3s;
}

.search-result-title a:hover {
  color: #333;
  border-bottom-color: #333;
}

.search-result-page {
  font-size: 13px;
  color: #666;
  margin-bottom: 10px;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.search-result-snippet {
  color: #444;
  line-height: 1.7;
  font-size: 15px;
}

.search-result-snippet mark {
  background-color: #fff3cd;
  padding: 2px 4px;
  border-radius: 3px;
  font-weight: 600;
}

.no-results {
  text-align: center;
  padding: 60px 20px;
  color: #666;
}

.no-results h3 {
  font-size: 24px;
  margin-bottom: 15px;
  color: #999;
}

.loading {
  text-align: center;
  padding: 40px;
  color: #666;
  font-size: 16px;
}

.loading::after {
  content: '...';
  animation: dots 1.5s infinite;
}

@keyframes dots {
  0%, 20% { content: '.'; }
  40% { content: '..'; }
  60%, 100% { content: '...'; }
}
</style>

<script>
// Search data - will be populated from all pages
const searchData = {
  pages: [
  {
    "title": "Index",
    "url": "./index.html",
    "content": "@keyframes typing { 0%, 100% { max-width: 0; } 20%, 80% { max-width: 100%; } } @keyframes blink-caret { from, to { border-color: transparent; } 50% { border-color: #4a9eff; } } .typing-name { display: inline-block; overflow: hidden; border-right: 3px solid #4a9eff; white-space: nowrap; max-width: fit-content; animation: typing 6s steps(20, end) infinite, blink-caret .75s step-end infinite; } .profile-header h1 { font-family: 'Courier New', monospace; color: #2c3e50; } .profile-header .typing-name { display: inline-block; } .profile-header { padding: 20px 30px !important; } .profile-photo { margin-bottom: 15px !important; width: 180px !important; height: 180px !important; } .profile-header h1 { margin: 5px 0 5px 0 !important; } .profile-header .tagline { margin-bottom: 10px !important; } / Fancy section headers / section h2 { font-family: 'Courier New', monospace; font-size: 24px; font-weight: 700; color: #2c3e50; border-left: 4px solid #4a9eff; padding-left: 15px; margin-top: 0 !import",
    "type": "Home"
  },
  {
    "title": "About",
    "url": "./about.html",
    "content": "Hanchen David Wang {{ site.description }} LinkedIn Download CV GitHub \ud83d\udc4b About Me Welcome! My name is David. I am currently a PhD student at Vanderbilt University working with Prof. Meiyi Ma on eXplainable AI in Healthcare and Deep Learning research. I am passionate about advancing the fields of eXplainable AI (XAI), healthcare, and machine learning. My work focuses on leveraging cutting-edge machine learning techniques to improve physical therapy, nursing simulations, and formal verification in AI. \ud83c\udfaf Research Interests My research spans across multiple areas of artificial intelligence and computer science, with a focus on making AI systems more explainable, reliable, and beneficial for healthcare applications. Key Areas: Explainable AI (XAI), Healthcare AI, Machine Learning, Physical Therapy & Motion Analysis, Nursing Education Simulations, Formal Verification, Multimodal Learning, Continual Learning \ud83c\udf93 Education Dual Program of Master's and Ph.D. in Computer Science (Ongoing) Vanderbil",
    "type": "About"
  },
  {
    "title": "Career",
    "url": "./career.html",
    "content": "/ Fancy section styling / .career-item { background: #ffffff; border: 1px solid #e0e0e0; border-radius: 8px; padding: 25px; margin-bottom: 25px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05); transition: transform 0.2s ease, box-shadow 0.2s ease; } .career-item:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(74, 158, 255, 0.15); } .career-item h2 { font-family: 'Courier New', monospace; color: #2c3e50; border-left: 4px solid #4a9eff; padding-left: 15px; margin-bottom: 15px; background: linear-gradient(to right, rgba(74, 158, 255, 0.1) 0%, transparent 100%); padding: 10px 15px; border-radius: 4px; } .career-item h2::before { content: '>'; color: #4a9eff; margin-right: 8px; font-weight: bold; } h1 { font-family: 'Courier New', monospace; color: #2c3e50; border-left: 4px solid #4a9eff; padding-left: 15px; background: linear-gradient(to right, rgba(74, 158, 255, 0.1) 0%, transparent 100%); padding: 10px 15px; border-radius: 4px; } h1::before { content: '>'; color: #4a9eff; mar",
    "type": "Page"
  },
  {
    "title": "Database Management System",
    "url": "./projects/database-management-system.html",
    "content": "This project is a Project Course referred to CS 122C from Prof. Chen Li at the University of California, Irvine. I will explain my implementation of a database system ground up from the simplest basis (Page File Mangement)... WITHOUT SHARING ANY OF MY CODE. Because it is a on-going class and for the best of student fairness, I do not want student to have any unfair advatange using my code. Please understand this is a explanatory page for people wanting to learn and understand how database system works and why it is efficient. Last but not least, here is a overall image of how this project looks like: We will work from the bottom, disk space management, and in our case, we call it page file management. Part 1 (Project 1) Page File Management (PFM): PFM contains 4 functions that act with clear purpose: create, destroy, open, and close the file. Particularly, this is a single instance in the later object class that will only does these functionalities to create separation of layers for cl",
    "type": "Project"
  },
  {
    "title": "EXACT: A Meta-Learning Framework for Precise Exercise Segmentation in Physical Therapy",
    "url": "./projects/EXACT.html",
    "content": "EXACT: A Meta-Learning Framework for Precise Exercise Segmentation in Physical Therapy ![DOI](https://doi.org/10.5281/zenodo.14834927) Overview EXACT is a meta-learning framework designed to precisely segment exercises in physical therapy using IMU (Inertial Measurement Unit) sensor data. The framework addresses the critical challenge of automatically identifying exercise boundaries and transitions in continuous sensor data streams, enabling accurate assessment and feedback for remote physical therapy. The Challenge Physical therapy exercises need precise temporal segmentation to: - Accurately count repetitions - Assess exercise quality - Provide timely feedback - Track patient progress over time However, traditional supervised learning approaches struggle with: - Limited labeled data for each new patient or exercise type - High inter-patient variability in movement patterns - Computational constraints for real-time on-device processing - Need for rapid adaptation to new exercises with",
    "type": "Project"
  },
  {
    "title": "Learning with Preserving (LwP)",
    "url": "./projects/LearningWithPreserving.html",
    "content": "Learning with Preserving (LwP) Overview Learning with Preserving (LwP) is a novel continual learning framework designed to address catastrophic forgetting in continual multitask learning (CMTL) scenarios. Unlike traditional approaches that focus on preserving task-specific outputs, LwP fundamentally shifts the paradigm by maintaining the geometric structure of learned representations through Dynamic Weighted Distance Preservation (DWDP). The Problem In real-world applications like autonomous driving and medical imaging, AI systems must continuously learn new tasks using shared input streams without forgetting previously acquired knowledge. For example, after learning to detect traffic signs, a model must later learn to classify traffic lights using the same camera feed. This scenario presents unique challenges: - Catastrophic Forgetting: Neural networks tend to forget previously learned tasks when adapting to new ones - Task Interference: Learning fragmented, task-specific features tha",
    "type": "Project"
  },
  {
    "title": "PhysiQ: Off-Site Quality Assessment of Exercise in Physical Therapy",
    "url": "./projects/PhysiQ.html",
    "content": "PhysiQ: Off-Site Quality Assessment of Exercise in Physical Therapy Overview Welcome to PhysiQ \u2014 a groundbreaking framework that revolutionizes physical therapy by enabling patients to effectively continue their therapy at home. PhysiQ addresses a critical challenge in physical therapy: providing quality assessment and feedback for exercises performed outside the clinic. Video Talk The Problem Traditional physical therapy relies heavily on in-person supervision to ensure correct exercise execution. However, patients spend most of their recovery time at home, where the lack of expert supervision often leads to inaccuracies in posture and performance. Existing solutions like Human Activity Recognition (HAR) in wearable devices recognize basic activities but don't cater to therapeutic rehabilitation needs. Vision-based tracking systems are cumbersome and not user-friendly for patients with limited mobility. Our Solution PhysiQ uses passive sensory detection through a smartwatch to track a",
    "type": "Project"
  },
  {
    "title": "Sso",
    "url": "./projects/SSO.html",
    "content": "Single Sign-On, aka SSO, is a session and user authentication service that permits a user to use one set of login credentials to access multiple applications. A great example is Google; Google has many services, such as Google Play, Gmail, and YouTube. Once a user has successfully login into one of the applications via Google Account, it would seamlessly go into the application. The benefits of that are greater security and compliance, improvement of usability, and lower IT costs. SSO is mostly managed by Active Directory Federation Service, aka AD FS. First of all, before explaining AD FS, let's talk about Active Directory. It is a hierarchical structure that stores information about objects on the network. It provides the methods for storing directory data and making data to administrators and users via the network. Nextly, AD FS is the service provided by Microsoft for SSO solution using Active Directory. It provides users with authenticated access to applications. idP-initiated SSO",
    "type": "Project"
  },
  {
    "title": "Stay Together",
    "url": "./projects/stay-together.html",
    "content": "This is my first healthcare related competition that work closely on helping patients to refrain their opioid addiction, more details in Opioid Hackathon. \"The Opioid Hackathon is a nearly 30-hour collaborative computer-programming event focused on tackling the opioid epidemic. Interdisciplinary teams of students, researchers, health and law enforcement professionals, and patients and family members were gathered to develop innovative solutions using data and technology. With more than 130 lives lost daily to opioid-related drug overdoses in the U.S., the need for novel approaches is clear. At the hackathon, registered teams will compete in one of a number of tracks, receiving appropriate datasets based on the selected track. They will then have 24 hours to use the data to develop their solution.\" Our team's solution post a social media like platform to support patients closely with the help of family members, doctors, friends, and other patients to create a friendly and positive envir",
    "type": "Project"
  },
  {
    "title": "web.xml",
    "url": "./projects/Online-Movies-Store-Web-Application.html",
    "content": "This project is the 122B project class, called \"Project in Databases and Web Applications\". I also had a awesome partner who has helped me to develop this project along the way and was able to make it work! This project introduces the modern data management techniques, such as database connectivity, web application development, extending database functions, database administration, and XML. In addition, I have been explosed to cloud services, such as Amazon AWS and Google Cloud Platform. Launched instances on AWS to deploy the project, I was able to use my application through cloud and did some modification through it. Here is a picture of my AMIs/used instances on AWS. P.S.: I have deleted my instances because of the monthly payment that I had to pay, so I created an image as a backup in case I want to have it back. This is our front-end pages look like (we also implemented fuzzy search and autocomplete in the main search bar): Of course, it is the most simple and static web page we f",
    "type": "Project"
  },
  {
    "title": "Projects",
    "url": "./projects.html",
    "content": "/ Fancy section styling / .project-item { background: #ffffff; border: 1px solid #e0e0e0; border-radius: 8px; padding: 25px; margin-bottom: 25px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05); transition: transform 0.2s ease, box-shadow 0.2s ease; } .project-item:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(74, 158, 255, 0.15); } .project-item h2 { font-family: 'Courier New', monospace; color: #2c3e50; border-left: 4px solid #4a9eff; padding-left: 15px; margin-bottom: 15px; background: linear-gradient(to right, rgba(74, 158, 255, 0.1) 0%, transparent 100%); padding: 10px 15px; border-radius: 4px; } .project-item h2::before { content: '>'; color: #4a9eff; margin-right: 8px; font-weight: bold; } h1 { font-family: 'Courier New', monospace; color: #2c3e50; border-left: 4px solid #4a9eff; padding-left: 15px; background: linear-gradient(to right, rgba(74, 158, 255, 0.1) 0%, transparent 100%); padding: 10px 15px; border-radius: 4px; } h1::before { content: '>'; color: #4a9eff;",
    "type": "Projects"
  },
  {
    "title": "Publications",
    "url": "./publications.html",
    "content": "/ Fancy section styling / .publication-list { background: #ffffff; border: 1px solid #e0e0e0; border-radius: 8px; padding: 30px; margin-bottom: 25px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05); } .publication-item { background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%); border-left: 3px solid #4a9eff; padding: 15px 20px; margin-bottom: 20px; border-radius: 6px; transition: all 0.2s ease; } .publication-item:hover { border-left-width: 5px; padding-left: 18px; background: linear-gradient(135deg, #e3f2fd 0%, #ffffff 100%); transform: translateY(-2px); box-shadow: 0 4px 12px rgba(74, 158, 255, 0.15); } h1 { font-family: 'Courier New', monospace; color: #2c3e50; border-left: 4px solid #4a9eff; padding-left: 15px; background: linear-gradient(to right, rgba(74, 158, 255, 0.1) 0%, transparent 100%); padding: 10px 15px; border-radius: 4px; } h1::before { content: '>'; color: #4a9eff; margin-right: 8px; font-weight: bold; } Publications A comprehensive list of my research publications in ",
    "type": "Publications"
  },
  {
    "title": "Service",
    "url": "./service.html",
    "content": "/ Fancy section styling / .service-item { background: #ffffff; border: 1px solid #e0e0e0; border-radius: 8px; padding: 25px; margin-bottom: 25px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05); transition: transform 0.2s ease, box-shadow 0.2s ease; } .service-item:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(74, 158, 255, 0.15); } .service-item h2 { font-family: 'Courier New', monospace; color: #2c3e50; border-left: 4px solid #4a9eff; padding-left: 15px; margin-bottom: 15px; background: linear-gradient(to right, rgba(74, 158, 255, 0.1) 0%, transparent 100%); padding: 10px 15px; border-radius: 4px; } .service-item h2::before { content: '>'; color: #4a9eff; margin-right: 8px; font-weight: bold; } h1 { font-family: 'Courier New', monospace; color: #2c3e50; border-left: 4px solid #4a9eff; padding-left: 15px; background: linear-gradient(to right, rgba(74, 158, 255, 0.1) 0%, transparent 100%); padding: 10px 15px; border-radius: 4px; } h1::before { content: '>'; color: #4a9eff;",
    "type": "Service"
  }
]
};

document.addEventListener('DOMContentLoaded', function() {
  const searchInput = document.getElementById('search-page-input');
  const searchButton = document.getElementById('search-page-button');
  const resultsContainer = document.getElementById('search-results');
  const statsContainer = document.getElementById('search-stats');

  // Get query from URL parameter
  const urlParams = new URLSearchParams(window.location.search);
  const queryParam = urlParams.get('q');
  
  if (queryParam) {
    searchInput.value = queryParam;
    performSearch(queryParam);
  }

  function performSearch(query = null) {
    const searchQuery = query || searchInput.value.trim().toLowerCase();
    
    if (!searchQuery) {
      resultsContainer.innerHTML = '<p style="color: #666; text-align: center; padding: 40px;">Please enter a search term.</p>';
      statsContainer.innerHTML = '';
      return;
    }

    // Show loading
    resultsContainer.innerHTML = '<div class="loading">Searching</div>';
    statsContainer.innerHTML = '';

    // Simulate a small delay for better UX
    setTimeout(() => {
      const results = [];
      
      // Search through all pages
      searchData.pages.forEach(page => {
        const content = page.content.toLowerCase();
        const title = page.title.toLowerCase();
        const pageType = page.type || 'Page';
        
        if (content.includes(searchQuery) || title.includes(searchQuery)) {
          // Create snippet with context
          const index = content.indexOf(searchQuery);
          const start = Math.max(0, index - 60);
          const end = Math.min(content.length, index + searchQuery.length + 100);
          let snippet = content.substring(start, end);
          
          // Add ellipsis
          if (start > 0) snippet = '...' + snippet;
          if (end < content.length) snippet = snippet + '...';
          
          // Highlight the search term
          const regex = new RegExp(`(${searchQuery})`, 'gi');
          snippet = snippet.replace(regex, '<mark>$1</mark>');
          
          results.push({
            title: page.title,
            url: page.url,
            snippet: snippet,
            type: pageType
          });
        }
      });

      // Display results
      if (results.length === 0) {
        resultsContainer.innerHTML = `
          <div class="no-results">
            <h3>No results found</h3>
            <p>Try different keywords or check your spelling.</p>
          </div>
        `;
        statsContainer.innerHTML = '';
      } else {
        statsContainer.innerHTML = `Found <strong>${results.length}</strong> result${results.length !== 1 ? 's' : ''} for "<strong>${searchQuery}</strong>"`;
        
        let html = '';
        results.forEach(result => {
          html += `
            <div class="search-result-item">
              <div class="search-result-page">${result.type || 'Page'}</div>
              <div class="search-result-title">
                <a href="${result.url}">${result.title}</a>
              </div>
              <div class="search-result-snippet">${result.snippet}</div>
            </div>
          `;
        });
        
        resultsContainer.innerHTML = html;
      }
    }, 300);
  }

  // Search on button click
  searchButton.addEventListener('click', () => performSearch());
  
  // Search on Enter key
  searchInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
      performSearch();
    }
  });
});
</script>
