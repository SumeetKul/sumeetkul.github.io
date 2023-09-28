---
layout: page
title: Research
description: The Spacetime Symphony...
image: assets/images/gw170817.jpg
tag: 3
nav-menu: true
---


<!-- Main -->
<div id="main" class="alt" display:inline-block>
    
<style>
body {
  background-image: url('../bbhspins_bg.gif');background-repeat:no-repeat;
}
</style> 


<!-- One -->
<section id="one">
  <div class="inner">
 

     
<h2> Gravitational Wave Data Analysis & Visualization</h2>

When two black holes orbit each other, their extreme compactness and density causes ripples in the fabric of spacetime around them. These ripples, called <i>Gravitational Waves</i>, were first predicted by Albert Einstein in his general theory of relativity. When these vibrations in spacetime reach the Earth, they are so incredibly tiny that Einstein thought we would never detect them. But in 2015, the LIGO experiment---a pair of detectors, one in Livingston, Louisiana and the other in Hanford, Washington, which shoot lasers along L-shaped arms 2.5 miles in length along the ground---detected gravitational waves for the first time ever. These waves were given off by the motion of two black holes, each about 15 times the mass of our Sun, merging to form one larger black hole about 1.3 billion light-years away. This collision resulted in a huge amount of energy---for a moment totalling more than the light given off by all the stars in our Universe---being carried away in these gravitational waves. As these waves flew away into the cosmos and made their long journey towards the Earth, they weakened considerably, shaking the LIGO detectors by an amount smaller than the width of a proton. 
<br><br>
The direct detection of gravitational waves is an insanely precise endeavour, one that won the Physics Nobel Prize in 2017. My research within LIGO has traversed various aspects of this challenge, from tackling noise in the detector, to figuring out the astrophysical properties of black holes hidden within the detected gravitational wave signals.

<p><br>
<b> For a more detailed and pedagogical introduction to gravitational wave physics, check out this interactive learning module I have created: </b> 
   <br>
        A lot of physics concepts taught at the middle- and high-school level are also applied in cutting-edge research such as the detection of gravitational waves by LIGO. This online, interactive module uses Streamlit, a python-based library to connect the astrophysics of black holes to the properties of waves that they emit, forming a toolkit for teaching physics in an engaging way. 
    <br> <b>Link:</b>
    <a href="https://gravitational-waves-tutorial.streamlit.app/" target="_blank" rel="noopener">https://gravitational-waves-tutorial.streamlit.app/</a>
<br><br>
            </p>


<p>
    
<h3> Summary of Research Projects:</h3>

<h4> Explaining the Mass Gap </h4>
<p><span class="image left"><img src="{% link assets/images/massgap.jpg %}" alt="" /></span> We do not know where the dividing line between neutron stars and black holes lies in terms of their mass. Theoretically, the heaviest a neutron star can be is about three times the mass of the sun. The lightest black holes we’ve seen weigh around five solar masses. We’ve never observed anything using telescopesin the space between three and five—a range we call the <i>'mass gap'</i>. That is, until now. The LIGO-Virgo gravitational wave observatories have detected compact objects with masses in this range. We are still unsure whether they are heavy neutron stars or lightweight black holes. It is still unclear on how they form. One possibility is of them being 'second-generation' compact objects formed out of the merger of two smaller neutron stars. I'm working on creating models to explain how the mass gap objects we are detecing in LIGO-Virgo may have formed, and how many we could detect using future, 3rd generation gravitational wave detectors.</p>

<br>

<h4> NNETFIX: A Neural Network to 'Fix' contaminated Gravitational Wave signals </h4>
<p><span class="image right"><img src="{% link assets/images/nnetfix.gif %}" alt="" /></span> The increased rate of detections by the Advanced LIGO and Virgo observatories means that incoming gravitational-wave signals more likely to be overlapping with or contaminated by <i>glitches</i>: transient noise bursts that frequently affect the detector for a variety of reasons, like wind, earthquakes, laser scattering, or even birds pecking at ice forming on the detector 
wall! The presence of a glitch on top of a signal distorts our initial estimation of the source parameters, particularly the sky position. 
This means we cannot send accurate alerts to our astronomer friends to search for it. I have developed a scikit-learn basedneural network 
to subtract an overlapping glitch from an astrophysical gravitational-wave signal. The method cuts off the glitch and identifies features of the gravitational-wave signal to 'fill in the gap' and reconstruct the portion of the data affected by the glitch.</p>

<br>

<h4> Random Projections </h4>
<p><span class="image left"><img src="{% link assets/images/RPPlanes.jpg %}" alt="" /></span> My Masters' Thesis project followed the idea of <i>Random Projections</i>, long utilized in data science, which says that the structural distribution of a high volume of data is retained when we project it randomly onto a lower-dimensional subspace. The relationship between any two data points, for instance how far apart they lie, is not affected by this projection, making it a lot easier to carry out data analysis with lesser computing power. I applied this technique to the needle-in-the-haystack search for gravitational waves. You can read more about my work in the article published in <a href="https://journals.aps.org/prd/abstract/10.1103/PhysRevD.99.101503" target="_blank" rel="noopener"><i>Physical Review D</i></a>. Open Access available on <a href="https://arxiv.org/abs/1801.04506" target="_blank" rel="noopener">ArXiv</a></p>

<p>
<br><br>
<h3> List of Publications </h3>

{% include_relative _includes/publications.md %}

</p>
