---
layout: page
title: About
description: 
image: assets/images/sumeet2.jpg
tag: 1
nav-menu: true
nav-order: 2
---

<!-- Main -->
<div id="main" class="alt" display:inline-block>

<!-- One -->
<section id="one">
        <div class="inner">

<!-- Content -->
<h2 id="content">About Me</h2>
<p><span class="image right"><img src="{% link assets/images/sumeet3.jpg %}" alt="Sumeet Kulkarni" class="profile-image-round" /></span>I'm a graduate researcher, science writer, and astrophotographer based in Oxford, MS. As a Physics PhD candidate at the University of Mississippi, I research various aspects of gravitational wave astrophysics as well as the noise characterization of the LIGO detectors. I'm a current AAAS Mass Media Fellow at the Los Angeles Times, and my science writing has also been featured in Scientific American, Astrobites, and India Bioscience. I run a science cafe featuring monthly public talks for the local community here in Oxford, MS, and an accompanying podcast called Ssippin' Science. My other interests include playing musical instruments, reading, cooking, cats and coffee.</p>


You can also find me on the following:
<br>

 <footer id="footer">
                <div class="inner">
                        <ul class="icons">
                                {% if site.instagram_url %}
                                <li><a href="{{ site.instagram_url }}" class="icon alt fa-instagram" target="_blank"><span class="label">Instagram</span></a></li>
                                {% endif %}
                                {% if site.github_url %}
                                <li><a href="{{ site.github_url }}" class="icon alt fa-github" target="_blank"><span class="label">GitHub</span></a></li>
                                {% endif %}
                                {% if site.linkedin_url %}
                                <li><a href="{{ site.linkedin_url }}" class="icon alt fa-linkedin" target="_blank"><span class="label">LinkedIn</span></a></li>
                                {% endif %}

                        </ul>
                </div>
</footer>

<!-- Education Section -->
<section id="education">
    <div class="inner"> <!-- Using 'inner' class for consistency if it provides padding/styling -->
        <h2 id="education-heading">Education</h2> <!-- Changed from h4 to h2 for better document structure -->
        <p>
            <i>2017-2023</i><br>
            Doctor of Philosophy (Ph.D.) in Astrophysics, <br>
            <a href="https://olemiss.edu/physics/" target="_blank" rel="noopener noreferrer">University of Mississippi</a>, Oxford, MS, USA
        </p>
        <p>
            <i>2020-2021</i><br>
            Master of Education (M.Ed.) in Science Education and Curriculum Instruction, <br>
            <a href="https://education.olemiss.edu/" target="_blank" rel="noopener noreferrer">University of Mississippi</a>, Oxford, MS, USA
        </p>
        <p>
            <i>2012-2017</i><br>
            Integrated Bachelor of Science and Master of Science (B.S.-M.S.), <br>
            <a href="https://www.iiserpune.ac.in/" target="_blank" rel="noopener noreferrer">Indian Institute of Science Education and Research</a>, Pune, India
        </p>
    </div>
</section>
