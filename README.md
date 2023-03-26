## Inspiration
We want to help kids and teens get easy access to empathetic support. This is because many of them (our younger selves included) don't actively seek for professional support out of consideration for embarrassment, potential social judgement by peers and limited counseling resources in schools. Currently, they can go onto online forums such as Reddit for support, which can be problematic since they might receive toxic responses from anonymous forum users, at a time when they are most vulnerable.

## What it does
Skypup makes use of the power of LLMs to give highly situated responses to individual situations. Users can go in the SkyPup UI to talk to SkyPup, in a similar way to ChatGPT, while guaranteeing that the responses are more empathetic, positive and mostly important - safe for them.

## How we built it
When users ask SkyPup about their unique situation, SkyPup first looks up a dense retrieval system to find a situation that's most similar to their situation. We then make use of this nearest neighbor as well as its response, which has been professionally annotated (found in an open source dataset https://arxiv.org/pdf/2009.08441.pdf). Attaching this to the prompt (which has been crafted to support chatGPT to play the role of an empathetic companion) allows ChatGPT to know what kind of responses are considered to be more empathetic. Finally, we call a moderation API to check that the ChatGPT response does not contain any traces of topics that would potential harm the user such as any sexual/violence topics.

## Challenges we ran into
One challenge we encountered that it was difficult to specify what is empathetic. Empathy is a highly complex concept that's difficult to specify to LLMs using prompts alone because it's highly contextual. After trying a lot of prompts and failing to get a good response from ChatGPT, we reflected what it means to be empathetic and realized that the few shot capabilities of ChatGPT means that it could be productive to show it examples of what it needs to do. This inspired our retrieval based approach.

## Accomplishments that we're proud of
We are really proud of the overall system we build which balances empathy and safety. Users can already use ChatGPT but it's not entirely instruction trained for the purpose of being empathetic. With a simple retrieval system as well as moderation support, we managed to adapt this wildly powerful system to guarantee users a safe and empathetic experience. We cannot stress enough how important both of these are, especially for our target audience of teens looking for support at a time when they are most vulnerable.

## What we learned
We learned the immense power of existing LLM/AI tools such as Langchain, Openai and Anthropic for making the next generation of Apps. At the same time, they are not meant to be all-encompassing so we need to carefully work with them to help users gain the most benefit from them while minimizing the potential downsides.

## What's next for SkyPup
The next step would be to integrate multi-modal support into SkyPup. A lot of time, it can be helpful for users to explain to LLMs what they are facing using images, videos and even sounds (like music they are listening to). With the upcoming wave of LLMs being multimodal (such as GPT4), this could really be a game changer.

Built With
