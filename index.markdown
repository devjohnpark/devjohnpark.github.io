---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default

---
<span style="color:#303030;font-weight:600;font-size:40px"> 
CUP-BOT
</span>
<br>
We inform you of future schedules of the World Cup matches you want to know and whether such game tickets are sold out or not, through telegram bot we made.

{% include button.html %}
<br>
<span style="color:#303030;font-weight:600;font-size:40px"> 
Latest News
</span>
{% for post in site.posts %}
<li style="list-style:none;"><a href="{{ post.url }}" style="color:black;">{{ post.title }}</a></li>
{{ post.date }}
<hr>
{% endfor %}