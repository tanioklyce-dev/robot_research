# Capture: https://www.liquid.ai/blog/d1-decision-model
Captured 2026-10-13 via curl; article text extracted from HTML (nav/share chrome trimmed).

Author: Liquid AI. Published 2026-10-05.
Today, we introduce d1, our first decision model, now supporting both text and images. With last week's experimental release, d1 became the first model to rival Jev on text decisions, and it is now the first to extend these capabilities to images. You can try it today at console.liquid.ai and in the d1 Playground.
We tested d1 against GPT-6.1 Sol and Claude Opus 5.5 on six real applications, from filtering support tickets to inspecting circuit boards. d1 matches or beats GPT-6.1 Sol on four of them. It costs 19x to 200x less than both models and answers significantly faster on every task.
How the d1 decision model works
Decision models answer questions about a situation with a probability for each possible answer. The d1 decision model takes unstructured data (e.g., text, images, or both) and one or more questions as input, reads them in one forward pass, and returns the probabilities, without generating any tokens. A text decision takes 200 to 300 ms, fast enough for real-time applications.
Figure 2: How the d1 decision model turns text and image inputs into decisions.
d1 answers three types of questions:
Noul: a yes/no question, answered with a probability between 0 and 1.
Choice: pick one label among many, answered with a probability per label.
Score: a position on a scale, weighted by the probability of each level.
One request can ask several questions about the same state, saving input tokens.
d1 in action
Decision models can replace expensive calls to language models when the answer is a structured decision. They also enable a variety of new use cases, some shown in this section. Every demo below runs live in the d1 Playground.
Visual inspection. This industrial application reviews parts from four production lines that pass under a camera: circuit boards, candles, cashews, and chewing gum (public VisA dataset). d1 sorts good and defective parts with 85-97% accuracy. The most interesting part is that the model was never trained for this. Thanks to its excellent generalizability, it understands the task from a short description.
Text applications. Five applications use d1 for every decision:
Smart Filter: d1 becomes a function in a SQL query, WHERE d1(ticket, 'the customer wants to cancel). It answers yes or no for each of 150 support tickets.
Code Search: d1 browses the Hugging Face transformers repository (6,511 files) one folder at a time, down to the function that answers a question.
Smart Folders: d1 files each new document into a folder, then a subfolder. It files search questions the same way, so keyword search only looks in one subfolder.
Web Agent: d1 operates a flight-search website from a one-sentence goal. At each step, it picks the next action among everything the page allows.
Context Compaction: d1 reads each tool output in a coding agent's session and keeps, trims, or drops it for the next task. It removes 52% of the tokens and keeps every output the task needs.
We adapted four of these applications from the following open-source projects: pg-jev, jevgrep, jev-ultrafast, and fast-jev-compaction.
Games. d1 plays eight classic games live and picks every move. Vision helps it in two ways:
Better decisions: Tetris can be fully described in text, but adding the screen raises d1's score from 70 to 81 cleared lines.
Simpler integration: In Wordle, d1 reads the board directly from a screenshot. Developers don't need to write a text version of the game, and d1 still solved 12 of 12 games in 3.8 guesses on average.
d1 also handles purely visual tasks. In Quick, Draw!, it guesses what a player's doodle shows among 62 words, and recognizes 5.2 of 6 drawings (random guessing gets 0.6).
Availability and pricing
Start building today with the d1 decision model, available on the  Liquid AI API as d1. Create an API key at console.liquid.ai (Dashboard > API Keys).
To use vision, you can simply send images as base64 data URLs in images:
import base64, os, requests
image = base64.b64encode(open("board.jpg", "rb").read()).decode()
response = requests.post(
    "https://api.liquid.ai/decisions/v1/systemone",
    headers={"Authorization": f"Bearer {os.environ['LIQUID_API_KEY']}"},
    json={
        "model": "d1",
        "images": [f"data:image/jpeg;base64,{image}"],
        "state": "Camera image of a circuit board on the production line.",
        "questions": 
            {"defect": {
                "type": "noul", 
                "instructions": "Does this circuit board have a defect?"
             }
         },
    },
)
print(response.json()["answers"]["defect"]["noul"])
The full API reference is in the decision models documentation.
d1 is billed on input tokens only, with no output tokens. Images are counted as input tokens at the same rate as text: 1.5 tokens per 32×32-pixel patch, so a 1024×1024 image costs 1,536 tokens. Each question is billed as its own prompt, including its text and all images.
d1 is also available through Vercel and OpenRouter, with text only for now. Vision is coming to both soon.
This is an exciting time for creativity and exploration in AI, and d1 is only the beginning. We're continuing our work on decision models across a range of sizes, with new features, higher decision quality, and lower latency, and we plan to release open weights for upcoming models on Hugging Face soon.Try on Liquid ConsoleRead our docs
Citation
For citations, please use the following reference or BibTeX:
Liquid AI, "Introducing d1: The most capable decision model, now with vision", Liquid AI Blog, Oct 2026.
@article{liquidAI2026d1,
  author = {Liquid AI},
  title = {Introducing d1: The most capable decision model, now with vision},
  journal = {Liquid AI Blog},
  year = {2026},
  note = {www.liquid.ai/blog/d1-decision-model},
}
Methodology. We ran each application once per model on October 5, 2026, with the d1 Playground's comparison script. GPT-6.1 Sol and Claude Opus 5.5 get each request as one chat message and answer in JSON, at their default reasoning setting. Where many questions share one input, such as the filter's tickets or the folders' passages, the chat models answer them in batches. Costs use list prices, without prompt-cache discounts. d1's costs use $0.04 per million input tokens. Time is per run, with up to 8 requests in flight. A Smart Filter run is one query over 150 tickets. A Smart Folders run files 105 passages, and its cost is per 1,000 passages. The filter's quality is its F1 score against hand labels, which counts both missed and wrong matches. The other text applications count the goals, questions, passages or needed outputs handled correctly. We wrote six of the 15 code questions and two of the four compaction sessions after d1's pipeline was set. In Visual Inspection, every model sees a good part from the same line next to the part to inspect.

## Figure data (comparison chart, from page source)
quality = % (F1 for Smart Filter); cost = USD per 1,000 runs; time = seconds per run

{app:"Visual Inspection", quality:{d1:91,gpt:82,claude:92}, cost:{d1:0.048,gpt:2.56,claude:6.17}, time:{d1:0.8,gpt:3.3,claude:4.0}},
    {app:"Smart Filter", quality:{d1:95,gpt:95,claude:98}, cost:{d1:0.85,gpt:45,claude:142}, time:{d1:6.0,gpt:6.6,claude:7.8}},
    {app:"Code Search", quality:{d1:80,gpt:87,claude:100}, cost:{d1:1.25,gpt:68,claude:251}, time:{d1:2.2,gpt:17.8,claude:24.3}},
    {app:"Web Agent", quality:{d1:100,gpt:100,claude:100}, cost:{d1:0.76,gpt:30,claude:86}, time:{d1:5.1,gpt:31.8,claude:35.0}},
    {app:"Context Compaction", quality:{d1:100,gpt:86,claude:100}, cost:{d1:0.31,gpt:5.89,claude:19}, time:{d1:0.5,gpt:6.0,claude:7.6}},
    {app:"Smart Folders", quality:{d1:96,gpt:98,claude:100}, cost:{d1:0.025,gpt:1.44,claude:4.54}, time:{d1:7.9,gpt:19.3,claude:15.8}}
