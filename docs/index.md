---
layout: default
---

<style>
  @keyframes typing {
    0%, 100% { max-width: 0; }
    20%, 80% { max-width: 100%; }
  }
  
  @keyframes blink-caret {
    from, to { border-color: transparent; }
    50% { border-color: #4a9eff; }
  }
  
  .typing-name {
    display: inline-block;
    overflow: hidden;
    border-right: 3px solid #4a9eff;
    white-space: nowrap;
    max-width: fit-content;
    animation: 
      typing 6s steps(20, end) infinite,
      blink-caret .75s step-end infinite;
  }
  
  .profile-header h1 {
    font-family: 'Courier New', monospace;
    color: #2c3e50;
  }
  
  .profile-header .typing-name {
    display: inline-block;
  }
  
  .profile-header {
    padding: 20px 30px !important;
  }
  
  .profile-photo {
    margin-bottom: 15px !important;
    width: 180px !important;
    height: 180px !important;
  }
  
  .profile-header h1 {
    margin: 5px 0 5px 0 !important;
  }
  
  .profile-header .tagline {
    margin-bottom: 10px !important;
  }
  
  /* Fancy section headers */
  section h2 {
    font-family: 'Courier New', monospace;
    font-size: 24px;
    font-weight: 700;
    color: #2c3e50;
    border-left: 4px solid #4a9eff;
    padding-left: 15px;
    margin-top: 0 !important;
    margin-bottom: 15px;
    position: relative;
    background: linear-gradient(to right, rgba(74, 158, 255, 0.1) 0%, transparent 100%);
    padding: 8px 12px;
    border-radius: 4px;
  }
  
  section h2::before {
    content: '>';
    color: #4a9eff;
    margin-right: 8px;
    font-weight: bold;
  }
  
  /* Fancy content boxes */
  section {
    background: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 12px 20px 20px 20px;
    margin-bottom: 12px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  
  section:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(74, 158, 255, 0.15);
  }
  
  .education-item, .highlight-item {
    background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
    border-left: 3px solid #4a9eff;
    padding: 15px 18px;
    margin-bottom: 15px;
    border-radius: 6px;
    transition: all 0.2s ease;
  }
  
  .education-item:hover, .highlight-item:hover {
    border-left-width: 5px;
    padding-left: 16px;
    background: linear-gradient(135deg, #e3f2fd 0%, #ffffff 100%);
  }
  
  .education-item h3, .highlight-item h3 {
    color: #2c3e50;
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 6px;
    margin-top: 0;
  }
  
  .highlight-item p {
    margin: 5px 0;
    line-height: 1.5;
    font-size: 14px;
  }
  
  .highlight-item p:last-child {
    margin-bottom: 0;
  }
  
  /* Make all section content more compact */
  section p {
    margin: 8px 0;
    line-height: 1.5;
    font-size: 14px;
  }
  
  section p:first-of-type {
    margin-top: 0;
  }
  
  section p:last-of-type {
    margin-bottom: 0;
  }
  
  .quick-links ul {
    list-style: none;
    padding: 0;
  }
  
  .quick-links li {
    margin-bottom: 10px;
  }
  
  .quick-links a {
    display: inline-block;
    padding: 8px 15px;
    background: linear-gradient(135deg, #4a9eff 0%, #357abd 100%);
    color: white;
    text-decoration: none;
    border-radius: 5px;
    transition: all 0.3s ease;
    font-weight: 500;
  }
  
  .quick-links a:hover {
    transform: translateX(5px);
    box-shadow: 0 4px 12px rgba(74, 158, 255, 0.3);
  }
</style>

<div class="about-page">
  <div class="profile-header">
    <img src="./assets/portfolio.png" alt="Hanchen David Wang" class="profile-photo">
    <h1><span class="typing-name">Hanchen David Wang</span></h1>
    <p class="tagline">{{ site.description }}</p>
    
    <!-- Social Links -->
    <div class="social-links-large">
      <a href="https://www.linkedin.com/in/hanchendavidwang/" target="_blank" title="LinkedIn">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
          <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
        </svg>
        <span>LinkedIn</span>
      </a>
      <a href="./Resume.pdf" target="_blank" title="Curriculum Vitae">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
          <path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/>
        </svg>
        <span>Curriculum Vitae</span>
      </a>
      <a href="https://github.com/HCWDavid" target="_blank" title="GitHub">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
        </svg>
        <span>GitHub</span>
      </a>
    </div>
  </div>

  <section class="bio">
    <h2>About Me</h2>
    <p>Welcome! My name is David. I am currently a PhD student at Vanderbilt University working with Prof. <a href="https://meiyima.github.io" target="_blank">Meiyi Ma</a> on <strong>eXplainable AI in Healthcare</strong> and <strong>Deep Learning research</strong>. Outside of research, I love staying active through workouts, expressing creativity through drawing, and exploring the outdoors. I'm also a big cat lover! Whether it's grabbing boba or coffee, I'm always up for a good conversation. ☕🧋</p>
  </section>

  <section class="interests">
    <h2>Research Interests</h2>
    <p>My research spans across multiple areas of artificial intelligence and computer science, with a focus on making AI systems more explainable, reliable, and beneficial for healthcare applications.</p>
    <p><strong>Key Areas:</strong> Explainable AI (XAI), Healthcare AI, Machine Learning, Physical Therapy & Motion Analysis, Nursing Education Simulations, Formal Verification, Multimodal Learning, Continual Learning</p>
  </section>

  <section class="education">
    <h2>Education</h2>
    <div class="education-item">
      <h3>Dual Program of Master's and Ph.D. in Computer Science (Ongoing)</h3>
      <p class="institution">Vanderbilt University</p>
      <p class="date">Aug 2021 - 2026-05 (Expected)</p>
      <p>Advisor: Prof. Meiyi Ma</p>
      <p>Focus: Representation Learning in DL, Open Source Imaging, HCI, Internet of Medical Things</p>
    </div>
    <div class="education-item">
      <h3>Bachelor of Science in Computer Science, Magna cum Laude (top 6%) GPA: 3.89</h3>
      <p class="institution">University of California, Irvine</p>
      <p class="date">Aug 2017 - Jun 2021</p>
    </div>
  </section>

  <section class="recent-highlights">
    <h2>Recent Highlights</h2>
    
    <div class="highlight-item">
      <h3>Latest Research</h3>
      <p><strong>BEAGLE: Behavioral Explanation via Agent Graph Learning</strong> (Aug 2025 - Present)</p>
      <p>Developing a novel framework to make AI tutors both interpretable and verifiable through behavioral explanation</p>
    </div>

    <div class="highlight-item">
      <h3>Recent Publication</h3>
      <p><strong>Learning with Preserving for Continual Multitask Learning</strong></p>
      <p>AAAI - Accepted (Oral)</p>
    </div>

    <div class="highlight-item">
      <h3>Current Position</h3>
      <p><strong>PhD Software Engineering Intern @ Google</strong> (May 2025 - Aug 2025)</p>
      <p>Architected an end-to-end autonomous agent to accelerate debugging by automating the root cause analysis of internal server failures. The agent intelligently triages issues by processing complex performance and reliability logs from large-scale benchmarking systems, significantly reducing manual effort for engineering teams.</p>
    </div>

  </section>

  <section class="quick-links">
    <h2>Quick Links</h2>
    <ul>
      <li><a href="./publications.html">View my Publications</a></li>
      <li><a href="./projects.html">Check out my Projects</a></li>
      <li><a href="./service.html">Service</a></li>
    </ul>
  </section>
</div>

<div style="text-align: center; margin-top: 30px; padding: 20px; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 8px; border: 1px solid #dee2e6;">
  <p style="font-size: 16px; color: #495057; margin: 0;">
    <strong>Let's connect!</strong> Feel free to reach out for collaborations or discussions about AI and healthcare.
  </p>
</div>
