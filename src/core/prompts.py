pro_opening_prompt= """
Debate topic: {topic}
Round 1 - Opening Argument (Pro)
Give a clear opening statement supporting the topic.
Use 1 concise point with a short evidence or example.
Limit response to 50 words.
"""

con_opening_prompt= """
Debate topic: {topic}
Round 1 - Opening Argument (Con)
Give a clear opening statement opposing the topic.
Use 1 concise point with a short evidence or example.
Limit response to 50 words.
"""

pro_rebuttal_prompt= """
Debate topic: {topic}
Round 2 - Rebuttal (Pro)
Respond directly to the Con opening argument from the context.
Explicitly mention at least one Con claim before rebutting it.
Limit response to 50 words.
"""

con_rebuttal_prompt= """
Debate topic: {topic}
Round 2 - Rebuttal (Con)
Respond directly to the Pro opening argument from the context.
Explicitly mention at least one Pro claim before rebutting it.
Limit response to 50 words.
"""

host_final_prompt= """
Debate topic: {topic}
Final Round - Host summary and Conclusion
Speak like a debate host.
Summarize key points from both sides fairly, then provide a balanced conclusion without declaring a winner.
Limit response to 50 words.
"""