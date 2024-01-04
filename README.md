# OpenAI and Python Practice

## Usage

1. Clone the repository
```bash
git clone https://github.com/pavangudiwada/openai-python-cli.git
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Add OpenAI API key as an environment variable
```bash
export OPENAI_API_KEY="YOUR_KEY_HERE"
```
4. Run the app
```
python file.py
```

## Get Answers CLI

You will be prompted to enter a query and a response will be displayed in the terminal itself. 

Run using 

```
python get_answers.py
```

### Options

Use `--role` to give the AI more context. By default, it acts as a Professional DevOps Engineer with expert level Prometheus and Kube Prometheus Stack knowledge. 

```
python get_answers.py --role "Python FastAPI expert"
```

Run `--help` to get all options, defaults and descriptions. 

## PromQL expression generator

Takes a query and generates a PromQL expression. Works sometimes.

Modify `content` and run 
```
python prometheus_call.py
```

## Browse a Website

Identifies a website in your query, looks it up and returns a response based on your initial query

Modify `user_input` and run

```
python internet_call.py
```
### Sample Queries and Responses
<details>
  <summary>summarize whats on www.theverge.com/tech into a bedtime story for a navi child on pandora
</summary>

Once upon a time in a world far, far away, a place just like the magical land of Pandora but filled with technology and gadgets, existed a realm named "The Verge's Tech Pages". This realm was a treasure trove of tales about wondrous creations and epic battles.

The kingdom overflowed with stories of novel inventions and discoveries, like LG's 2024 OLED TVs that had a keen focus on AI processing. Their star creation was a delightful wireless TV, which was available in a smaller 65-inch model for those who enjoyed coziness in their nests.

The year 2023 rang the bell for many memorable moments and notable releases. One such story revolved around Google's Pixel 8. The inhabitants could now repair their Pixel 8 phones with genuine parts from a place known as iFixit, ensuring their beloved devices would last them through many adventures.

But things weren't always rosy in the kingdom. Apple found itself in the middle of a storm, agreeing to settle a lawsuit about gift card scammers. It was a tumultuous time, filled with urgent callers and countless victims fooled into buying gift cards.

The land of the Strava users held onto their old magical artefacts - the Garmin Foreruners, devices with a long-lasting power that was cherished by the masses.

Amidst this, there were whispers of deceit and trouble. The inhabitants were warned about more convincing crypto scams, as they promised a treasure that didn't exist. Despite this, the inhabitants of the kingdom pressed onward and continued to build and create.

Far away in another kingdom, TikTok, they decided to take a bigger slice of the coin from their sellers. The fee was to be increased from two to six percent in April and then eight percent in July on many commodities, adding to the strife of the sellers but also sparking creativity and competition.

And so, the stories continued in the kingdom. These tales were filled with triumph and struggles, inventions and issues, excitement and caution, woven together into the tapestry of technology, served on the platter of The Verge. This, dear child, is but a glimpse into that realm, a place much like Pandora but gifted with the magic of technology

</details>


<details>
<summary>Get me the top tech news today in https://lwn.net/ and write a Cloud Native rhyme based on the news today</summary>

Today's top tech news from https://lwn.net/ mentions several advancements in Linux and related programming endeavours:

1. The LWN.net Weekly Edition for January 4, 2024 discussed their tech predictions for the year.
2. A new vulnerability in SMTP Smuggling was reported, observed as problematic for multiple open-source mailers.
3. The Linux graphics stack had some noteworthy advancements with respect to display settings synchronization.
4. The tool 'perf' added data-type profiling to enable a deeper understanding of memory usage.
5. Introduction to 'Maestro', a Unix-like operating system created from scratch in Rust, was shared.
6. Vim 9.1 was released with enhanced support for classes and objects in the scripting language.
7. There were important security updates for popular software and libraries.

Finally, let's get to the rhyme:

In the realm of code, so pristine,
To make changes, we're ever keen.
From SMTP flaws that we fight,
To Rust-built systems taking flight.

Graphics stack with a new rendition,
Predictions filled with intuition,
Profiling memory, a new direction,
In a world of code, it’s all for correction.

In class-support Vim does invest,
Security fixes lay threats to rest.
Maestro’s song in Rust does play,
In our Cloud Native world today.
</details>
