---
layout: default
title: Schedule
permalink: /schedule/
---

There will be 26 class sessions over 15 weeks. There will be no class during the first week. On 8/28, we will have two class sessions, one during lunch. It will be recorded for those unable to attend.  A tentative schedule is below.

Lecture slides and exercise notebooks should be available below after the class period. If they are not, please let me know.

| ---- | | |
{% for module in site.data.modules -%} |
{%- if module.day %}{{ module.day }}{% endif %} |
{%- if module.date %}{{ module.date }}{% endif %} | <b>{{ module.title }}</b>
{%- if module.description %} {{ module.description }} {% endif -%}
{%- if module.teacher %} ({{ module.teacher }}){% endif -%}
{%- if module.basename %} [[key](https://github.com/daveminh/Chem456-2024F/raw/main/slides/{{ module.basename }}.key)/[ppt](https://github.com/daveminh/Chem456-2024F/raw/main/slides/{{ module.basename }}.ppt)/[pdf](https://github.com/daveminh/Chem456-2024F/raw/main/slides/{{ module.basename }}.pdf)]. {% endif %}
{%- if module.exercise %} Exercise {{ module.exercise }}{% endif -%}
{%- if module.notebook %} [[colab](https://colab.research.google.com/github/daveminh/Chem456-2024F/blob/main/exercises/{{ module.notebook }}.ipynb)]. {% endif -%}
{%- if module.panopto %} [[Recording](https://iit.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id={{module.panopto}})]{% endif -%}
{%- if module.due %} <u>Due:</u> {{ module.due }}. {% endif %}
{%- if module.quiz %} <u>Quiz:</u> {{ module.quiz }}. {% endif %} |
{% endfor %}

During the final exam period (December 2 from 2-4 pm), students will give a final presentation. Exercise 12 and 13 are due on December 5 at noon. The final report and individual contribution report is due on December 9 at noon.