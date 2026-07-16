---
layout: landing
title: Research
description: The Spacetime Symphony...
scrolline: During my Ph.D., I studied Gravitational Waves &mdash; ripples in the fabric of spacetime. <br> Scroll down to read more &dArr;
image: assets/images/research-2.jpg
centering: right bottom
tag: 3
nav-menu: true
show_tile: true
nav-order: 4
---


<!-- Main -->
<style>
#background-video {
  width: 100vw;
  height: 100vh;
  object-fit: cover;
  position: fixed;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  z-index: -1;
}
</style> 
<div id="main" class="alt" style="display:inline-block">

<video id="background-video" autoplay loop muted playsinline poster="../assets/images/bbhspins_poster.png">
<source src="../assets/images/bbhspins_background.mp4" type="video/mp4">
</video>
</div>

<!-- One -->
<section id="one">
  <div class="inner">
 

     
<h2> The Spacetime Symphony... </h2>
      
When two black holes orbit each other, their extreme compactness and density causes ripples in the fabric of spacetime around them. These ripples, called <i>Gravitational Waves</i>, were first predicted by Albert Einstein in his general theory of relativity. But he never thought we could actually detect them---when these vibrations in spacetime reach the Earth from billions of light-years away, they become incredulously tiny. Physicists, however, like proving everyone wrong, be it Einstein. In 2015, the LIGO experiment---a pair of detectors, one in Livingston, Louisiana and the other in Hanford, Washington, which shoot lasers along L-shaped arms 2.5 miles in length along the ground---detected gravitational waves for the first time ever. These waves were given off by the motion of two black holes around each other, each about 15 times the mass of our Sun. The gravitational ripples carried energy away from the orbiting black holes, pulling them tighter, making them move faster, and thus creating even larger ripples. Eventually, they collided and merged to form one larger black hole that vibrated like a struck gong before settling down. This collision resulted in a huge amount of energy: for a fleeting moment, it was the most powerful event in the universe, more so than the combined light given off by all the stars in our universe! As the gravitational waves waves flew away into the cosmos and made their long journey towards the Earth, they weakened considerably, shaking the LIGO detectors by an amount smaller than the width of a proton.
<br><br>
The direct detection of gravitational waves is an insanely precise endeavour, one that won the Physics Nobel Prize in 2017. My research within LIGO has traversed various aspects of this challenge, from <b> using machine learning to tackle noise in the detector</b>, to <b>applying statistical data analysis techniques in figuring out the astrophysical properties of black holes</b> hidden within the detected gravitational wave signals. 

<p><br>
<b> For a more detailed introduction to the physics behind gravitational waves, I have created this this interactive learning module: </b> 
   <br>
        A lot of physics concepts taught at the middle- and high-school level are also applied in cutting-edge research such as the detection of gravitational waves by LIGO. This online, interactive module uses Streamlit, a python-based library to connect the astrophysics of black holes to the properties of waves that they emit, forming a toolkit for teaching physics in an engaging way. 
    <br> <b>Link:</b>
    <a href="https://gravitational-waves-tutorial.streamlit.app/" target="_blank" rel="noopener">https://gravitational-waves-tutorial.streamlit.app/</a>
<br><br>
            </p>


<p>
    
<h3> Summary of Research Projects:</h3>
      
<h4> Random Projections </h4>
<p><span class="image left"><img src="{% link assets/images/RPPlanes.jpg %}" alt="" /></span> My Masters' Thesis project borowed the idea of <i>Random Projections</i> from data science. In broad terms, it says that the structural distribution of high volumes of data is retained when we transform or <i>project</i> it randomly into a lower-dimensional subspace. The relationship between any two data points, for instance, how far apart they lie, is not affected by this projection, making it a lot easier to carry out data analysis with lesser computing power. I applied this technique to the needle-in-the-haystack search for gravitational waves. You can read more about my work in the article published in <a href="https://journals.aps.org/prd/abstract/10.1103/PhysRevD.99.101503" target="_blank" rel="noopener"><i>Physical Review D</i></a>. Open Access available on <a href="https://arxiv.org/abs/1801.04506" target="_blank" rel="noopener">ArXiv</a></p>

<br><br><br>
      
<h4> Explaining the Mass Gap </h4>
<p><span class="image right"><img src="{% link assets/images/massgap.jpg %}" alt="" /></span> We do not know where the dividing line between neutron stars and black holes lies in terms of their mass. Theoretically, the heaviest a neutron star can be is about three times the mass of the sun. The lightest black holes we’ve seen weigh around five solar masses. We’ve never observed anything using telescopesin the space between three and five—a range we call the <i>'mass gap'</i>. That is, until now. The LIGO-Virgo gravitational wave observatories have detected compact objects with masses in this range. We are still unsure whether they are heavy neutron stars or lightweight black holes. It is still unclear on how they form. One possibility is of them being 'second-generation' compact objects formed out of the merger of two smaller neutron stars. I'm working on creating models to explain how the mass gap objects we are detecing in LIGO-Virgo may have formed, and how many we could detect using future, 3rd generation gravitational wave detectors.</p>

<br> 
      
<h4> Inferring the spin tilts of Black Holes </h4>
<p><span class="image left"><img src="{% link assets/images/spintilts.gif %}" alt="" /></span> You may be wondering why the black holes on this page have arrows on them? These arrows represent the spin axes of rotating black holes. Just like the Earth spins around an axis that is tilted with respect to its orbit around the Sun, black holes orbiting each other also have their spins inclined. Further, since they're moving rapidly, they can influence each other's spins, causing them to <i>precess</i> like a spinning top. In my research, I simulate these black hole spin tilts forward and backward in time, using full numerical relativity models as well as its approximate solutions at large separations. Evolving black holes backward in time and looking at how their spins are inclined can help us understand how such binary systems form.</p>
      
<br>

<h4> NNETFIX: A Neural Network to 'Fix' contaminated Gravitational Wave signals </h4>
<p><span class="image right"><img src="{% link assets/images/nnetfix.gif %}" alt="" /></span> The increased rate of detections by the Advanced LIGO and Virgo observatories means that incoming gravitational-wave signals more likely to be overlapping with or contaminated by <i>glitches</i>: transient noise bursts that frequently affect the detector for a variety of reasons, like wind, earthquakes, laser scattering, or even birds pecking at ice forming on the detector 
wall! The presence of a glitch on top of a signal distorts our initial estimation of the source parameters, particularly the sky position. 
This means we cannot send accurate alerts to our astronomer friends to search for it. I have developed a scikit-learn basedneural network 
to subtract an overlapping glitch from an astrophysical gravitational-wave signal. The method cuts off the glitch and identifies features of the gravitational-wave signal to 'fill in the gap' and reconstruct the portion of the data affected by the glitch.</p>

<br>
      
<h4> Calculating the "kicks" of Binary Neutron Star remnants </h4>
<p><span class="image left"><img src="{% link assets/images/bnskick_0.png %}" alt="" width="1000"/></span> When two neutron stars merge, they also radiate gravitational waves before forming a remnant object which is typically a black hole. This collision is accompanied by an explosion of matter known as a <i>kilonova</i> around the black hole. This mass often ejected asymmetrically. The emitted gravitational waves are also not symmetric unless the two neutron stars are exactly the same. Due to conservation of momentum, the remnant black hole gets recoiled (or "kicked") in a direction opposite to the ejection of matter and the radiated gravitational waves. If these kicks are too large and exceed the typical escape speeds of galaxies, the black hole can get ejected. Using state-of-the-art general-relativistic magnetohydrodynamic (GRMHD) simulations, we have estimated the magnitude of such kicks in binary neutron star remnants for the first time. <i> The image on the left represents the distribution of ejected matter around the remnant black hole in the center, drawn on a mollweide projection (like a world atlas). The darker patches indicate places where there is more ejecta, while the star represents the direction of the kick.</i></p>



<p>
<br><br>
<h3> List of Publications </h3>

{% include_relative _includes/publications.md %}

</p>
