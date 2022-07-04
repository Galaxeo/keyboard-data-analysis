# Keyboard Study Project
## Goal of the study
The goal of the study is to figure out the actual correlation among the hobbies that people have in relation to what type of mechanical keyboard they may prefer. The Cherry MX Red and other linears have always been marketed towards gamers whereas light tactiles like the Cherry MX Browns have been marketed as a switch meant for typing/productivity.

In addition, this study will be used to reinforce Numpy, Pandas, and Matplotlib skills learned in previous projects. Python will be used in order to help present results produced from the data gathered.

The goal of this is to get some data so I can draw conclusions off of it using Numpy, Pandas, and Matplotlib. 
## Gathering Data
This should be done by using a survey through Google Forms, asking a couple of questions regarding the main thing that people do with their keyboard, whether that be for primarily gaming or productivity purposes.
- What keyboard do you use? (Mechanical keyboard, laptop keyboard, membrane keyboard)
  - To understand if the person is someone who uses a mechanical keyboard or not, and try to see how they feel about certain aspects of a mechanical keyboard.
- If a Mechanical keyboard is used, what type of switch do you prefer? Linear (red, no bump), tactile (brown, slight bump), clicky (blue, very clicky)
  - To see what type of switch they prefer
- Reasons behind the purchase of the keyboard
  - Understanding why people buy a keyboard, specifically for those who bought a mechanical keyboard, why did they buy it?
- How much time do you spend on an average day on the computer? Productivity, gaming, youtube.
  - Understand the priorities of the user - if they spend most of their time using the keyboard to game or their main usage of the keyboard is for work-related subjects.
- Have you heard of custom keyboards?
  - Better way to ask this question is to see if they're in the hobby or not. This question was switched to "Have you heard of a JWK switch?"
  - This way, we can understand whether or not the person is someone who is knowledgable about the hobby or not.
- What would you think is a justifiable price for a custom keyboard?
  - Understanding what people think is a good price to spend on a custom keyboard.
## Using the data
The main questions I wanted answered was the reasoning behind why people wanted to buy tactile switches over linears. Through all of the commissions that I've done for custom keyboards, all but two of them had tactiles (the other two having linears). Many of these individuals who these keyboards belonged to were gamers, which led me to wonder why it was tactiles were so favored throughout these builds as it had heavily contrasted with my prior beliefs that many gamers would prefer linears due to the marketing surrounding the linear switch and tactile switch in the mid 2010s.

I had decided to use violin plots for the majority of these data visualizations for a couple of reasons, but mainly due to its ability to visualize a larger distribution with a smaller sample size (in this case, our sample size was 40 entries). The peaks outside of the box-plot part of the violin plot indicate the possibility of someone in another sample having that data value. If you're curious, WISC has a magnificent write-up on the math behind Gaussian kernels, which are used to estimate the distribution of the violin plot (and other KDE plots on seaborn/pandas/matplotlib).
## Lessons learned
A large takeaway was understanding why I was asking each question. After the first group of answers, I had a sudden realization that the questions that were being asked didn't give me the data that I necessarily wanted. I switched some of the questions to a different format, and luckily, some of the previous answers had adapted to this as well. One example of this was the price range for a custom keyboard question, where those who took the survey earlier had likely seen this as a short answer question, however I later broke this down into two multiple choice questions, where the minimum and maximum were answered based off of a range given from 1-10. Other questions were fixed when I had gone to each question, and listed the reason each question was being asked.
