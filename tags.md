---
layout: page
title: Tags
description: Browse blog posts by topic
permalink: /blog/tags/
nav-menu: false
show_tile: false
---

<style>
.tag-cloud { list-style: none; padding: 0; display: flex; flex-wrap: wrap; gap: 0.5em 1.25em; }
.tag-cloud li { margin: 0; }
.tag-cloud .tag-count { opacity: 0.7; font-size: 0.9em; }
</style>

<!-- Main -->
<div id="main" class="alt">

<!-- One -->
<section id="one">
    <div class="inner">
        <header class="major">
            <h1>Tags</h1>
        </header>
        <p>Browse posts by topic. {{ site.tags | size }} tag{% if site.tags.size != 1 %}s{% endif %} across the blog.</p>

        {% assign sorted_tags = site.tags | sort %}
        <ul class="tag-cloud">
        {% for tag in sorted_tags %}
            {% assign tag_name = tag[0] %}
            {% assign tag_posts = tag[1] %}
            <li>
                <a href="{{ tag_name | slugify | prepend: '/blog/tags/' | prepend: site.baseurl | append: '/' }}">
                    <code>{{ tag_name }}</code>
                </a>
                <span class="tag-count">({{ tag_posts | size }})</span>
            </li>
        {% endfor %}
        </ul>

        {% if site.tags == empty %}
        <p><em>No tags yet.</em></p>
        {% endif %}
    </div>
</section>

</div>
