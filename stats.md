---
layout: page
title: Blog Stats
description: A build-time snapshot of the blog
permalink: /stats/
nav-menu: false
show_tile: false
---

<!-- Main -->
<div id="main" class="alt">

<!-- One -->
<section id="one">
    <div class="inner">
        <header class="major">
            <h1>Blog Stats</h1>
        </header>
        <p>Generated automatically from the site's posts each time it is built.</p>

        {%- assign total_words = 0 -%}
        {%- for post in site.posts -%}
            {%- assign wc = post.content | strip_html | number_of_words -%}
            {%- assign total_words = total_words | plus: wc -%}
        {%- endfor -%}

        <ul>
            <li><strong>Total posts:</strong> {{ site.posts | size }}</li>
            <li><strong>Total words across all posts:</strong> {{ total_words }}</li>
            <li><strong>Distinct tags:</strong> {{ site.tags | size }}</li>
        </ul>

        <h2>Posts per tag</h2>
        {% if site.tags == empty %}
        <p><em>No tags yet.</em></p>
        {% else %}
        <table>
            <thead><tr><th>Tag</th><th>Posts</th></tr></thead>
            <tbody>
            {% assign sorted_tags = site.tags | sort %}
            {% for tag in sorted_tags %}
                <tr>
                    <td><a href="{{ '/blog/tags/' | append: tag[0] | slugify | prepend: site.baseurl }}/"><code>{{ tag[0] }}</code></a></td>
                    <td>{{ tag[1] | size }}</td>
                </tr>
            {% endfor %}
            </tbody>
        </table>
        {% endif %}

        <h2>Posting timeline</h2>
        {% if site.posts == empty %}
        <p><em>No posts yet.</em></p>
        {% else %}
        <table>
            <thead><tr><th>Month</th><th>Posts</th></tr></thead>
            <tbody>
            {% assign by_month = site.posts | group_by_exp: "post", "post.date | date: '%Y-%m'" %}
            {% assign months = by_month | sort: "name" | reverse %}
            {% for month in months %}
                <tr>
                    <td>{{ month.items[0].date | date: "%B %Y" }}</td>
                    <td>{{ month.items | size }}</td>
                </tr>
            {% endfor %}
            </tbody>
        </table>
        {% endif %}
    </div>
</section>

</div>
