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
    "title": "Welcome to David's Cubicle \u2615",
    "url": "./index.html",
    "content": "Welcome to David's Cubicle \u2615 I'm Hanchen David Wang, a PhD student at Vanderbilt University working on eXplainable AI and Healthcare applications. This is my digital space where I share my research, projects, and thoughts. --- Quick Links - Download my CV - View my Publications - Check out my Projects - Leadership & Service - Learn more About Me --- Recent Highlights Latest Research Explainable AI for First-Person Video Segmentation in Nursing Simulations (Jul 2024 - Present) Developing explainable AI methods to analyze video segments from Tobii Glasses' first-person perspective during nursing simulation training sessions Recent Publication SmartSeg: A Non-Parametric Approach for Smart Glass Video Segmentation Pervasive and Mobile Computing - Under Review Current Position PhD Software Engineering Intern @ Google (May 2025 - Aug 2025) Architected an end-to-end autonomous agent to accelerate debugging by automating the root cause analysis of internal server failures. The agent intelligen",
    "type": "Home"
  },
  {
    "title": "About",
    "url": "./about.html",
    "content": "Hanchen David Wang {{ site.description }} LinkedIn Download CV GitHub \ud83d\udc4b About Me Welcome! My name is David. I am currently a PhD student at Vanderbilt University working with Prof. Meiyi Ma on eXplainable AI in Healthcare and Deep Learning research. I am passionate about advancing the fields of eXplainable AI (XAI), healthcare, and machine learning. My work focuses on leveraging cutting-edge machine learning techniques to improve physical therapy, nursing simulations, and formal verification in AI. \ud83c\udfaf Research Interests My research spans across multiple areas of artificial intelligence and computer science, with a focus on making AI systems more explainable, reliable, and beneficial for healthcare applications. Key Areas: Explainable AI (XAI), Healthcare AI, Machine Learning, Physical Therapy & Motion Analysis, Nursing Education Simulations, Formal Verification, Multimodal Learning, Continual Learning \ud83c\udf93 Education Ph.D. in Computer Science Vanderbilt University 2021 - Present Advisor: Pr",
    "type": "About"
  },
  {
    "title": "Database Management System",
    "url": "./projects/database-management-system.html",
    "content": "This project is a Project Course referred to CS 122C from Prof. Chen Li at the University of California, Irvine. I will explain my implementation of a database system ground up from the simplest basis (Page File Mangement)... WITHOUT SHARING ANY OF MY CODE. Because it is a on-going class and for the best of student fairness, I do not want student to have any unfair advatange using my code. Please understand this is a explanatory page for people wanting to learn and understand how database system works and why it is efficient. Last but not least, here is a overall image of how this project looks like: We will work from the bottom, disk space management, and in our case, we call it page file management. Part 1 (Project 1) Page File Management (PFM): PFM contains 4 functions that act with clear purpose: create, destroy, open, and close the file. Particularly, this is a single instance in the later object class that will only does these functionalities to create separation of layers for cl",
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
    "content": "Projects A collection of my software engineering and development projects, showcasing work across various technologies and domains. --- PhysiQ December 2022 Off-site quality assessment framework for physical therapy exercises using smartwatch and multi-task spatiotemporal Siamese Neural Network Technologies: Deep Learning, Wearable Sensors, Python, Siamese Networks --- Database Management System Fall 2020 Implemented paged file (PF) and record-based file (RBF) management systems in C/C++. Upgraded relation manager (RM) designs to store catalog information by columns with hidden metadata Technologies: C/C++, Git --- B+ Tree for Database Management 2020 Developed a B+ tree data structure for efficient database management with optimized insertion, deletion, and search operations, significantly improving database performance Technologies: C/C++, Data Structures, Algorithm Optimization --- Process and Resource Manager 2020 Implemented Python data structures to manage processes and resources",
    "type": "Projects"
  },
  {
    "title": "Publications",
    "url": "./publications.html",
    "content": "Publications A comprehensive list of my research publications in artificial intelligence, machine learning, and healthcare applications. --- 1. SmartSeg: A Non-Parametric Approach for Smart Glass Video Segmentation Wang, Hanchen David, Liu, Yilin, Fu, Haowei, Mason, Madison Lee, Li, Fanjie, Wise, Alyssa, Levin, Daniel T, Biswas, Gautam, Ma, Meiyi Pervasive and Mobile Computing, Under Review. 2. Decoding Human Motion: A Scoping Review of Explainable AI Methods in Movement Analysis Wang, Hanchen David, Khan, Nibraas, Ghosh, Ritam, Tauseef, Mahrukh, Mion, Lorraine, Ma, Meiyi, Sarkar, Nilanjan Pervasive and Mobile Computing, Under Review. 3. Towards Verified and Targeted Explanations through Formal Methods Wang, Hanchen David, Robinette, Preston K., Lopez, Diego Manzanas, Oguz, Ipek, Johnson, Taylor T., Ma, Meiyi JAIR, Major Revision. 4. Learning with Preserving for Continual Multitask Learning Wang, Hanchen David, Bae, Siwoo, Chen, Zirong, Ma, Meiyi AAAI, Accepted (Oral). 5. Multimodal Me",
    "type": "Publications"
  },
  {
    "title": "Leadership & Service",
    "url": "./service.html",
    "content": "Leadership & Service My contributions to the academic community through mentoring, volunteering, and service activities. --- Mentor, Students Projects Vanderbilt University | Nashville, TN Aug 2021 - Present - (2024\u2013Present) Mentored master's student Yiling Liu and undergraduates Haowei Fu and Christin Ann Sanchez on \"SmartSeg: A Non-Parametric Approach for Smart Glass Video Segmentation,\" an event segmentation project for a nursing training simulation. - (2024\u2013Present) Mentored undergraduate Haoran (Max) Ma on an IMU-guided video classification project to improve model accuracy. - (2024\u20132025) Mentored undergraduate Siwoo Bae on \"Learning with Preserving for Continual Multitask Learning,\" focused on preserving representational space in continual learning. The work was presented at the Vanderbilt Undergraduate Research Fair, earning a poster award. - (2022\u20132024) Mentored undergraduate Xutong (Helen) Sun and Yashvitha Thatigotla on \"EXACT: A Meta-Learning Framework for Precise Exercise S",
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
