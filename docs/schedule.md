---
layout: default
title: Schedule
permalink: /schedule/
---

There will be 30 class sessions over 16 weeks. A tentative schedule is below.

Lecture slides and exercise notebooks should be available below after the class period. If they are not, please let me know.

There are optional deadlines to submit drafts. If you submit a draft by the optional deadline, I plan to provide feedback within two days about whether the draft is satisfactory and the steps that you could take to make it satisfactory.

| ---- | | |
{% for module in site.data.modules -%} |
{%- if module.day %}{{ module.day }}{% endif %} |
{%- if module.date %}{{ module.date }}{% endif %} | <b>{{ module.title }}</b>
{%- if module.description %} {{ module.description }} {% endif -%}
{%- if module.teacher %} ({{ module.teacher }}){% endif -%}
{%- if module.basename %} [[key](https://github.com/daveminh/Chem456-2026S/raw/main/slides/{{ module.basename }}.key)/[pdf](https://github.com/daveminh/Chem456-2026S/raw/main/slides/{{ module.basename }}.pdf)]. {% endif %}
{%- if module.exercise %} Exercise {{ module.exercise }}.{% endif -%}
{%- if module.notebook %} [[Notebook](https://github.com/daveminh/Chem456-2026S/blob/main/exercises/{{ module.notebook }}.ipynb)]. {% endif -%}
{%- if module.due %} <u>Due:</u> {{ module.due }}. {% endif %}
{%- if module.quiz %} <u>Quiz:</u> {{ module.quiz }}. {% endif %} |
{% endfor %}

During the final exam period (TBD), students will give a final presentation. Exercise 14 is due on May 4 at noon. If you submit a draft of the final report by May 5, I will give you feedback by May 7. The final report and individual contribution report are due on May 11 at noon.