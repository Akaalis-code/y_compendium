# 2023 :
    > Claude 1 Family : 100K token context window, larger than competitors at the time .

    > Claude 2 Family : 200K token context window with improved coding and math skills .

# 2024 : 
    > Claude 3 Series : 3 tier naming convention
            - Opus  : Top-tier reasoning and coding.
            - Sonnet: Balanced speed and intelligence.
            - Haiku : Fastest and most cost-effective for simple tasks.

    > Claude 3.5 Series :
            - 3.5 Sonnet famous for outperforming 3 OPUS
            - 3.5 Sonnet has introduced "Computer Use",
              allowing the AI to control a mouse and keyboard

# 2025 :
    > Claude 4 Family : 
            - Claude 4 Opus and Sonnet were designed for deep agentic tasks, 
              featuring native memory capabilities to manage long-running projects

# 2026 :
    > Claude MYTHOS : 
            - RIP Software industry 




Check later :
    Claude Desktop Application 
    Claude Projects 
    Claude Artifacts
    Claude Cowork 
    Claude Dispatch
    Claude Code
    Claude Plugins
    Claude Skills


Check what is firecrawl 

    Claude desktop --> settings --> capabilities --> understand all the underlying options 

Social media carousel 

When to use What :

    Claude OPUS : 
        -Complex research and reasoning 
        -Multi step tasks
        -Quality over Speed or low cost

    Claude SONNET :
        -Everyday tasks 
        -Solid balance of quality and speed
        -writing, coding, and analysis where Opus is overkill

    Claude HAIKU :
        -Fast, real-time responses 
        -For simple questions and quick discussions
        -High-volume or cost-sensitive building with the API


Some Links :
    https://claude.ai/new
    https://claude.ai/upgrade
    platform.claude.com/usage

# CLAUDE USAGE and BILLING :
    - Consumer subscriptions (Subscription Model (Pro/Max)):
        - Claude Pro or Max subscription authenticating via your gmail accounts 
          It doesnt track the cost through API usage , it has flat fee and usage limit per time .
            - Check usage in claude code :
                > /usage
    - Developer API platform (API / Pay-Per-Token Model):
        - You can buy API credits and use that money in form of API communication to LLM .
          Keep in mind this is different from your SUBSCRIPTION model of (PRO , MAX) etc
        - For Claude code to take the API key , you need to set it ".bashrc" file as below 
          > export ANTHROPIC_API_KEY="your_sk_ant_key_here"
          Save the file as .bashrc itself
          > source .bashrc
        
    Note : (subject to correction)
        If claude code notices that API key , it prefers to use Pay per token model through API .
        In my experience Pay per token used up all 5 dollars in span of 15 mins work .
        But if ANthropic has to support your code outside of CLAUDE code it needs API .
        other wise if you are using just claude code  prefer subscription model over pay per token model.

        If you want your claude code to use "Subscription Model" over its prefered "API / Pay-Per-Token Model"
        >/logout
        and enter into claude once again and do web authentication.
        >claude