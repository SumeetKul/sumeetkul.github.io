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

<!-- One -->
<section id="one">
        <div class="inner">


<h4> Explaining the Mass Gap </h4>
<p><span class="image left"><img src="{% link assets/images/massgap.jpg %}" alt="" /></span> We do not know where the dividing line between neutron stars and black holes lies in terms of their mass. Theoretically, the heaviest a neutron star can be is about three times the mass of the sun. The lightest black holes we’ve seen weigh around five solar masses. We’ve never observed anything using telescopesin the space between three and five—a range we call the <i>'mass gap'</i>. That is, until now. The LIGO-Virgo gravitational wave observatories have detected compact objects with masses in this range. We are still unsure whether they are heavy neutron stars or lightweight black holes. It is still unclear on how they form. One possibility is of them being 'second-generation' compact objects formed out of the merger of two smaller neutron stars. I'm working on creating models to explain how the mass gap objects we are detecing in LIGO-Virgo may have formed, and how many we could detect using future, 3rd generation gravitational wave detectors.</p>

<br>

<h4> NNETFIX: A Neural Network to 'Fix' contaminated Gravitational Wave signals </h4>
<p><span class="image right"><img src="{% link assets/images/nnetfix.gif %}" alt="" /></span> The increased rate of detections by the Advanced LIGO and Virgo observatories means that incoming gravitational-wave signals more likely to be overlapping with or contaminated by <i>glitches</i>: transient noise bursts that frequently affect the detector for a variety of reasons, like wind, earthquakes, laser scattering, or even birds pecking at ice forming on the detector wall! The presence of a glitch on top of a signal distorts our initial estimation of the source parameters, particularly the sky position. This means we cannot send accurate alerts to our astronomer friends to search for it. I have developed a scikit-learn basedneural network to subtract an overlapping glitch from an astrophysical gravitational-wave signal. The method cuts off the glitch and identifies features of the gravitational-wave signal to 'fill in the gap' and reconstruct the portion of the data affected by the glitch.</p>

<br>

<h4> Random Projections </h4>
<p><span class="image left"><img src="{% link assets/images/RPPlanes.jpg %}" alt="" /></span> My Masters' Thesis project followed the idea of <i>Random Projections</i>, long utilized in data science, which says that the structural distribution of a high volume of data is retained when we project it randomly onto a lower-dimensional subspace. The relationship between any two data points, for instance how far apart they lie, is not affected by this projection, making it a lot easier to carry out data analysis with lesser computing power. I applied this technique to the needle-in-the-haystack search for gravitational waves. You can read more about my work in the article published in <a href="https://journals.aps.org/prd/abstract/10.1103/PhysRevD.99.101503" target="_blank"><i>Physical Review D</i></a>. Open Access available on <a href="https://arxiv.org/abs/1801.04506" target="_blank">ArXiv</a></p>
</div>

<br>
<h3 id="content">[Under Construction...]</h3>
