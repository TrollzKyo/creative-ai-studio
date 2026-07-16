from app.plugins.registry import register

from app.research_agent import generate_research
from app.script_agent import generate_script
from app.broll_agent import generate_broll
from app.shot_agent import generate_shotlist
from app.premiere_agent import generate_premiere


register("research", generate_research)
register("script", generate_script)
register("broll", generate_broll)
register("shot", generate_shotlist)
register("premiere", generate_premiere)