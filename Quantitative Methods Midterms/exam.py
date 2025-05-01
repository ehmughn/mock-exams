import os
import random
from collections import defaultdict

# Quiz data: List of dictionaries containing question, choices, correct answer, reasoning, and section
quiz = [
    # Section 1: Research Fundamentals (8 questions)
    {
        "section": "Research Fundamentals",
        "question": "What is the primary goal of research as defined in the reviewer?",
        "choices": ["a. To generate subjective opinions", "b. To solve problems systematically and unbiasedly", "c. To conduct experiments only", "d. To analyze qualitative data only"],
        "correct": "b",
        "reasoning": "The reviewer defines research as a systematic and unbiased way of solving a problem through generating verifiable data (page 1)."
    },
    {
        "section": "Research Fundamentals",
        "question": "All of the following are key components of research EXCEPT:",
        "choices": ["a. A question of interest", "b. A claim", "c. A hypothesis test", "d. Evidence"],
        "correct": "c",
        "reasoning": "The reviewer lists a question, claim, evidence, and argument as key components, but not a hypothesis test (page 1)."
    },
    {
        "section": "Research Fundamentals",
        "question": "True or False: Every research study must address a question of interest to the community.",
        "choices": ["a. True", "b. False", "c. Only for quantitative research", "d. Only for qualitative research"],
        "correct": "a",
        "reasoning": "The reviewer states that every piece of research should address a question of interest to the community (page 1)."
    },
    {
        "section": "Research Fundamentals",
        "question": "The process of linking evidence to a claim is called:",
        "choices": ["a. Hypothesis", "b. Argument", "c. Experiment", "d. Observation"],
        "correct": "b",
        "reasoning": "The reviewer defines the argument as showing that evidence supports the claim (page 1)."
    },
    {
        "section": "Research Fundamentals",
        "question": "Which type of research studies the relationships of variables?",
        "choices": ["a. Exploratory", "b. Descriptive", "c. Experimental", "d. Quantitative"],
        "correct": "b",
        "reasoning": "Descriptive research studies the relationships of variables (reviewer, page 1)."
    },
    {
        "section": "Research Fundamentals",
        "question": "Quantitative research is characterized by:",
        "choices": ["a. Descriptive data collection", "b. Inferential statistics", "c. Non-statistical analysis", "d. Text-based data"],
        "correct": "b",
        "reasoning": "Quantitative research uses inferential statistics to determine results (reviewer, page 1)."
    },
    {
        "section": "Research Fundamentals",
        "question": "Qualitative research primarily involves:",
        "choices": ["a. Measurable data", "b. Inferential statistics", "c. Descriptive data like text or audio", "d. Experimental data"],
        "correct": "c",
        "reasoning": "Qualitative research gathers descriptive data such as text, audio, or video (reviewer, page 1)."
    },
    {
        "section": "Research Fundamentals",
        "question": "The claim in research is also known as:",
        "choices": ["a. The hypothesis", "b. The contribution", "c. The evidence", "d. The argument"],
        "correct": "b",
        "reasoning": "The reviewer states that the claim is 'the contribution' of the research (page 1)."
    },
    # Section 2: Measures of Location and Central Tendency (8 questions)
    {
        "section": "Measures of Location and Central Tendency",
        "question": "Measures of location describe:",
        "choices": ["a. The spread of data", "b. The position of values in a frequency distribution", "c. The variability of data", "d. The correlation of variables"],
        "correct": "b",
        "reasoning": "The reviewer defines measures of location as indicating the position of values in a frequency distribution (page 2)."
    },
    {
        "section": "Measures of Location and Central Tendency",
        "question": "The most commonly used measure of central tendency is:",
        "choices": ["a. Median", "b. Mode", "c. Mean", "d. Midrange"],
        "correct": "c",
        "reasoning": "The mean is the most commonly used measure of central tendency (reviewer, page 2)."
    },
    {
        "section": "Measures of Location and Central Tendency",
        "question": "True or False: The mode is the middle value in a dataset.",
        "choices": ["a. True", "b. False", "c. Only for even datasets", "d. Only for odd datasets"],
        "correct": "b",
        "reasoning": "The mode is the most frequent value, not the middle value (which is the median) (reviewer, page 2)."
    },
    {
        "section": "Measures of Location and Central Tendency",
        "question": "The median is defined as:",
        "choices": ["a. The average of all values", "b. The middle value in an ordered dataset", "c. The most frequent value", "d. The range of values"],
        "correct": "b",
        "reasoning": "The median is the middle value in a dataset arranged in ascending or descending order (reviewer, page 2)."
    },
    {
        "section": "Measures of Location and Central Tendency",
        "question": "A dataset with two values appearing most frequently is:",
        "choices": ["a. Unimodal", "b. Bimodal", "c. Multimodal", "d. No mode"],
        "correct": "b",
        "reasoning": "A dataset with two modes is bimodal (reviewer, page 8)."
    },
    {
        "section": "Measures of Location and Central Tendency",
        "question": "All of the following are measures of central tendency EXCEPT:",
        "choices": ["a. Mean", "b. Median", "c. Mode", "d. Range"],
        "correct": "d",
        "reasoning": "Range is a measure of spread, not central tendency (reviewer, page 2)."
    },
    {
        "section": "Measures of Location and Central Tendency",
        "question": "For the dataset {1, 2, 2, 3, 4}, the mode is:",
        "choices": ["a. 1", "b. 2", "c. 3", "d. 4"],
        "correct": "b",
        "reasoning": "The value 2 appears most frequently (twice), so the mode is 2 (reviewer, page 2)."
    },
    {
        "section": "Measures of Location and Central Tendency",
        "question": "If all values in a dataset appear equally often, the dataset has:",
        "choices": ["a. One mode", "b. Two modes", "c. No mode", "d. Infinite modes"],
        "correct": "c",
        "reasoning": "If every measure appears the same number of times, there is no mode (reviewer, page 2)."
    },
    # Section 3: Measures of Spread and Dispersion (8 questions)
    {
        "section": "Measures of Spread and Dispersion",
        "question": "Measures of spread indicate:",
        "choices": ["a. The central value", "b. How close or far apart values are", "c. The probability of an event", "d. The mean of a dataset"],
        "correct": "b",
        "reasoning": "Measures of spread show how close or far apart values are in a frequency distribution (reviewer, page 2)."
    },
    {
        "section": "Measures of Spread and Dispersion",
        "question": "Which of the following is NOT a measure of spread?",
        "choices": ["a. Range", "b. Variance", "c. Standard deviation", "d. Median"],
        "correct": "d",
        "reasoning": "Median is a measure of central tendency, not spread (reviewer, page 2)."
    },
    {
        "section": "Measures of Spread and Dispersion",
        "question": "The standard deviation is:",
        "choices": ["a. The square of variance", "b. The square root of variance", "c. Equal to variance", "d. Unrelated to variance"],
        "correct": "b",
        "reasoning": "Standard deviation is the square root of variance (reviewer, page 2)."
    },
    {
        "section": "Measures of Spread and Dispersion",
        "question": "True or False: A higher standard deviation means data points are closer to the mean.",
        "choices": ["a. True", "b. False", "c. Only for normal distributions", "d. Depends on the dataset"],
        "correct": "b",
        "reasoning": "Higher standard deviation indicates data points are farther from the mean (reviewer, page 2)."
    },
    {
        "section": "Measures of Spread and Dispersion",
        "question": "The range is calculated as:",
        "choices": ["a. Mean minus median", "b. Highest value minus lowest value", "c. Square root of variance", "d. Sum of values divided by count"],
        "correct": "b",
        "reasoning": "Range is the difference between the highest and lowest values (reviewer, page 2)."
    },
    {
        "section": "Measures of Spread and Dispersion",
        "question": "Relative dispersion is used to:",
        "choices": ["a. Measure variability within a dataset", "b. Compare datasets", "c. Calculate the mean", "d. Determine the mode"],
        "correct": "b",
        "reasoning": "Relative dispersion compares a dataset with others (reviewer, page 2)."
    },
    {
        "section": "Measures of Spread and Dispersion",
        "question": "Variance is a measure of:",
        "choices": ["a. Central tendency", "b. Dispersion", "c. Probability", "d. Frequency"],
        "correct": "b",
        "reasoning": "Variance is a measure of dispersion (reviewer, page 2)."
    },
    {
        "section": "Measures of Spread and Dispersion",
        "question": "For a dataset, a higher variance indicates:",
        "choices": ["a. Data points are closer to the mean", "b. Data points are farther from the mean", "c. Data points are evenly distributed", "d. No change in distribution"],
        "correct": "b",
        "reasoning": "Higher variance means data points are farther from the mean (reviewer, page 2)."
    },
    # Section 4: Descriptive Statistics and Frequency Distribution (6 questions)
    {
        "section": "Descriptive Statistics and Frequency Distribution",
        "question": "Frequency distribution displays:",
        "choices": ["a. The mean of a dataset", "b. The number of occurrences of outcomes", "c. The variance", "d. The probability"],
        "correct": "b",
        "reasoning": "Frequency distribution shows the frequency of outcomes in a sample (reviewer, page 2)."
    },
    {
        "section": "Descriptive Statistics and Frequency Distribution",
        "question": "All of the following can be shown in a frequency distribution EXCEPT:",
        "choices": ["a. Raw number of items", "b. Percentage of items", "c. Mean of the dataset", "d. Frequency of outcomes"],
        "correct": "c",
        "reasoning": "Frequency distributions show raw numbers and percentages, not the mean (reviewer, page 2)."
    },
    {
        "section": "Descriptive Statistics and Frequency Distribution",
        "question": "Descriptive statistics are used to:",
        "choices": ["a. Predict outcomes", "b. Summarize population or sample data", "c. Test hypotheses", "d. Conduct experiments"],
        "correct": "b",
        "reasoning": "Descriptive statistics summarize population parameters or sample statistics (reviewer, page 2)."
    },
    {
        "section": "Descriptive Statistics and Frequency Distribution",
        "question": "True or False: Descriptive statistics involve gathering data from concerned parties.",
        "choices": ["a. True", "b. False", "c. Only for quantitative data", "d. Only for qualitative data"],
        "correct": "a",
        "reasoning": "The reviewer states descriptive statistics involve data gathering (page 2)."
    },
    {
        "section": "Descriptive Statistics and Frequency Distribution",
        "question": "A population in a study refers to:",
        "choices": ["a. A subset of individuals", "b. All individuals studied", "c. Only respondents", "d. A sample"],
        "correct": "b",
        "reasoning": "Population includes all items/individuals studied (reviewer, page 3)."
    },
    {
        "section": "Descriptive Statistics and Frequency Distribution",
        "question": "Parameters describe characteristics of:",
        "choices": ["a. A sample", "b. A population", "c. A frequency distribution", "d. A random variable"],
        "correct": "b",
        "reasoning": "Parameters describe population characteristics (reviewer, page 3)."
    },
    # Section 5: Probability Basics (8 questions)
    {
        "section": "Probability Basics",
        "question": "Probability is defined as:",
        "choices": ["a. The sum of outcomes", "b. Favorable outcomes divided by total outcomes", "c. The variance of outcomes", "d. The mean of outcomes"],
        "correct": "b",
        "reasoning": "Probability is the number of favorable outcomes divided by total outcomes (reviewer, page 3)."
    },
    {
        "section": "Probability Basics",
        "question": "True or False: Probabilities are always between 0 and 1.",
        "choices": ["a. True", "b. False", "c. Only for discrete probabilities", "d. Only for continuous probabilities"],
        "correct": "a",
        "reasoning": "Probabilities are proportions between 0 and 1 (reviewer, page 3)."
    },
    {
        "section": "Probability Basics",
        "question": "The set of all possible outcomes is called:",
        "choices": ["a. An event", "b. A sample space", "c. A random variable", "d. A probability distribution"],
        "correct": "b",
        "reasoning": "The sample space is the set of all possible outcomes, denoted S (reviewer, page 3)."
    },
    {
        "section": "Probability Basics",
        "question": "An event is:",
        "choices": ["a. The entire sample space", "b. A subset of the sample space", "c. A single outcome", "d. A probability value"],
        "correct": "b",
        "reasoning": "An event is any subset of a sample space (reviewer, page 3)."
    },
    {
        "section": "Probability Basics",
        "question": "The sample space for rolling a die is:",
        "choices": ["a. {1, 2}", "b. {1, 2, 3}", "c. {1, 2, 3, 4, 5, 6}", "d. {1, 6}"],
        "correct": "c",
        "reasoning": "The sample space for a die includes all possible outcomes: {1, 2, 3, 4, 5, 6} (reviewer, page 3)."
    },
    {
        "section": "Probability Basics",
        "question": "A simple event contains:",
        "choices": ["a. Multiple outcomes", "b. One outcome", "c. No outcomes", "d. All outcomes"],
        "correct": "b",
        "reasoning": "A simple event is a set with one element of the sample space (reviewer, page 4)."
    },
    {
        "section": "Probability Basics",
        "question": "All of the following are true about sample spaces EXCEPT:",
        "choices": ["a. They contain all possible outcomes", "b. They are denoted by S", "c. They are always finite", "d. Each outcome is a sample point"],
        "correct": "c",
        "reasoning": "Sample spaces can be infinite (e.g., continuous distributions), not always finite (reviewer, page 3)."
    },
    {
        "section": "Probability Basics",
        "question": "A compound event is:",
        "choices": ["a. A single outcome", "b. The union of simple events", "c. An empty set", "d. The entire sample space"],
        "correct": "b",
        "reasoning": "A compound event is the union of simple events (reviewer, page 4)."
    },
    # Section 6: Counting Techniques (8 questions)
    {
        "section": "Counting Techniques",
        "question": "Counting Rule #1 states the number of outcomes for n trials is:",
        "choices": ["a. The sum of outcomes", "b. The product of outcomes", "c. The factorial of n", "d. The square of outcomes"],
        "correct": "b",
        "reasoning": "Counting Rule #1 uses the product of outcomes per trial (reviewer, page 4)."
    },
    {
        "section": "Counting Techniques",
        "question": "How many outcomes are possible for two coin tosses?",
        "choices": ["a. 2", "b. 4", "c. 6","d. 8"],
        "correct": "b",
        "reasoning": "Each toss has 2 outcomes (H, T), so 2 × 2 = 4 (reviewer, page 4)."
    },
    {
        "section": "Counting Techniques",
        "question": "The number of ways to arrange 3 books is:",
        "choices": ["a. 3", "b. 6", "c. 9", "d. 12"],
        "correct": "b",
        "reasoning": "3! = 3 × 2 × 1 = 6 (reviewer, page 4)."
    },
    {
        "section": "Counting Techniques",
        "question": "The formula for linear permutation is:",
        "choices": ["a. n! / (n - x)!", "b. n! / x!(n - x)!", "c. (n - 1)!", "d. n!"],
        "correct": "a",
        "reasoning": "Linear permutation: P(n, x) = n! / (n - x)! (reviewer, page 5)."
    },
    {
        "section": "Counting Techniques",
        "question": "How many ways can 2 books be arranged from 4 books (order matters)?",
        "choices": ["a. 6", "b. 12", "c. 24", "d. 4"],
        "correct": "b",
        "reasoning": "P(4, 2) = 4! / (4 - 2)! = 4 × 3 = 12 (reviewer, page 5)."
    },
    {
        "section": "Counting Techniques",
        "question": "The number of ways to arrange 4 people in a circle is:",
        "choices": ["a. 6", "b. 12", "c. 24", "d. 3"],
        "correct": "d",
        "reasoning": "Circular permutation: (4 - 1)! = 3! = 6 (reviewer, page 5)."
    },
    {
        "section": "Counting Techniques",
        "question": "The combination formula is used when:",
        "choices": ["a. Order matters", "b. Order does not matter", "c. Outcomes are mutually exclusive", "d. Trials are independent"],
        "correct": "b",
        "reasoning": "Combinations are used when order does not matter (reviewer, page 5)."
    },
    {
        "section": "Counting Techniques",
        "question": "How many ways can 3 books be chosen from 5 (order does not matter)?",
        "choices": ["a. 10", "b. 20", "c. 15", "d. 5"],
        "correct": "a",
        "reasoning": "C(5, 3) = 5! / (3!(5 - 3)!) = 10 (reviewer, page 5)."
    },
    # Section 7: Probability Distributions (8 questions)
    {
        "section": "Probability Distributions",
        "question": "A random variable is:",
        "choices": ["a. A fixed value", "b. A numerical outcome of an experiment", "c. The mean of a dataset", "d. The variance"],
        "correct": "b",
        "reasoning": "A random variable is a numerical value determined by an experiment’s outcome (reviewer, page 6)."
    },
    {
        "section": "Probability Distributions",
        "question": "Discrete probability distributions are for random variables with:",
        "choices": ["a. Continuous values", "b. Countable values", "c. Infinite values", "d. Normal distribution"],
        "correct": "b",
        "reasoning": "Discrete distributions apply to countable values (reviewer, page 6)."
    },
    {
        "section": "Probability Distributions",
        "question": "All of the following are discrete random variables EXCEPT:",
        "choices": ["a. Number of students", "b. Number of children", "c. Weight of a person", "d. Number of dice rolls"],
        "correct": "c",
        "reasoning": "Weight is continuous; others are discrete (reviewer, page 6)."
    },
    {
        "section": "Probability Distributions",
        "question": "The binomial distribution requires:",
        "choices": ["a. Continuous outcomes", "b. Independent trials with two outcomes", "c. Variable probability", "d. Dependent trials"],
        "correct": "b",
        "reasoning": "Binomial requires independent trials with two mutually exclusive outcomes (reviewer, page 6)."
    },
    {
        "section": "Probability Distributions",
        "question": "The Poisson distribution is used for:",
        "choices": ["a. High probability events", "b. Events in a continuous interval with small probability", "c. Dependent trials", "d. Fixed trials"],
        "correct": "b",
        "reasoning": "Poisson applies to events in a continuous interval with small probability (reviewer, page 6)."
    },
    {
        "section": "Probability Distributions",
        "question": "True or False: The Poisson distribution is always skewed to the right.",
        "choices": ["a. True", "b. False", "c. Only for small λ", "d. Only for large λ"],
        "correct": "a",
        "reasoning": "The Poisson distribution is always skewed to the right (reviewer, page 6)."
    },
    {
        "section": "Probability Distributions",
        "question": "Continuous probability distributions are represented by:",
        "choices": ["a. A frequency table", "b. Area under a curve", "c. A single value", "d. Countable outcomes"],
        "correct": "b",
        "reasoning": "Continuous distributions use the area under a curve (reviewer, page 7)."
    },
    {
        "section": "Probability Distributions",
        "question": "The normal distribution is characterized by:",
        "choices": ["a. A rectangular shape", "b. A bell-shaped curve", "c. A skewed curve", "d. Equal probabilities"],
        "correct": "b",
        "reasoning": "The normal distribution is bell-shaped and symmetric (reviewer, page 7)."
    },
    # Section 8: Specific Probability Distributions (6 questions)
    {
        "section": "Specific Probability Distributions",
        "question": "The uniform distribution is concerned with:",
        "choices": ["a. Skewed outcomes", "b. Equally likely outcomes", "c. Bell-shaped outcomes", "d. Discrete outcomes"],
        "correct": "b",
        "reasoning": "Uniform distribution has equally likely outcomes over a domain (reviewer, page 7)."
    },
    {
        "section": "Specific Probability Distributions",
        "question": "The exponential distribution is often used to model:",
        "choices": ["a. Number of successes", "b. Lifetimes or times to an event", "c. Heights of students", "d. Dice rolls"],
        "correct": "b",
        "reasoning": "Exponential distribution models lifetimes or times to an event (reviewer, page 7)."
    },
    {
        "section": "Specific Probability Distributions",
        "question": "The memoryless property is a feature of:",
        "choices": ["a. Normal distribution", "b. Binomial distribution", "c. Exponential distribution", "d. Poisson distribution"],
        "correct": "c",
        "reasoning": "The exponential distribution has the memoryless property (reviewer, page 7)."
    },
    {
        "section": "Specific Probability Distributions",
        "question": "The normal distribution is important because it:",
        "choices": ["a. Models discrete data", "b. Fits mound-shaped, symmetric data", "c. Is always skewed", "d. Has fixed range"],
        "correct": "b",
        "reasoning": "Normal distribution fits mound-shaped, symmetric datasets (reviewer, page 7)."
    },
    {
        "section": "Specific Probability Distributions",
        "question": "The cumulative distribution function (cdf) is used to:",
        "choices": ["a. Calculate the mean", "b. Evaluate probability as area", "c. Find the mode", "d. Compute variance"],
        "correct": "b",
        "reasoning": "The cdf evaluates probability as area under the curve (reviewer, page 7)."
    },
    {
        "section": "Specific Probability Distributions",
        "question": "All of the following are true for continuous distributions EXCEPT:",
        "choices": ["a. Outcomes are measured", "b. Area under curve equals 1", "c. Probabilities for individual values", "d. Graph is a curve"],
        "correct": "c",
        "reasoning": "Continuous distributions use intervals, not individual values, for probabilities (reviewer, page 7)."
    },
    # Section 9: Calculations and Examples (8 questions)
    {
        "section": "Calculations and Examples",
        "question": "The mean of {2, 4, 6, 8, 10} is:",
        "choices": ["a. 4", "b. 5", "c. 6", "d. 7"],
        "correct": "c",
        "reasoning": "Mean = (2 + 4 + 6 + 8 + 10) / 5 = 30 / 5 = 6 (reviewer, page 8)."
    },
    {
        "section": "Calculations and Examples",
        "question": "The mode of {5, 5, 6, 7, 8} is:",
        "choices": ["a. 5", "b. 6", "c. 7", "d. 8"],
        "correct": "a",
        "reasoning": "Mode is 5, appearing twice (reviewer, page 8)."
    },
    {
        "section": "Calculations and Examples",
        "question": "The median of {1, 3, 5, 7, 9} is:",
        "choices": ["a. 3", "b. 4", "c. 5", "d. 6"],
        "correct": "c",
        "reasoning": "Median is the middle value: 5 (reviewer, page 8)."
    },
    {
        "section": "Calculations and Examples",
        "question": "The range of {2, 4, 6, 8, 10} is:",
        "choices": ["a. 6", "b. 8", "c. 10", "d. 12"],
        "correct": "b",
        "reasoning": "Range = 10 - 2 = 8 (reviewer, page 2)."
    },
    {
        "section": "Calculations and Examples",
        "question": "The probability of rolling a 3 on a die is:",
        "choices": ["a. 1/6", "b. 1/4", "c. 1/3", "d. 1/2"],
        "correct": "a",
        "reasoning": "Probability = 1 favorable outcome / 6 total outcomes = 1/6 (reviewer, page 3)."
    },
    {
        "section": "Calculations and Examples",
        "question": "How many ways can 2 items be selected from 4 (order does not matter)?",
        "choices": ["a. 4", "b. 6", "c. 8", "d. 12"],
        "correct": "b",
        "reasoning": "C(4, 2) = 4! / (2!(4 - 2)!) = 6 (reviewer, page 5)."
    },
    {
        "section": "Calculations and Examples",
        "question": "The number of ways to arrange 3 people in a circle is:",
        "choices": ["a. 2", "b. 3", "c. 6", "d. 9"],
        "correct": "a",
        "reasoning": "(3 - 1)! = 2! = 2 (reviewer, page 5)."
    },
    {
        "section": "Calculations and Examples",
        "question": "The variance of a dataset is calculated by:",
        "choices": ["a. Squaring the standard deviation", "b. Summing squared differences from mean divided by count", "c. Finding the range", "d. Averaging absolute differences"],
        "correct": "b",
        "reasoning": "Variance sums squared differences from the mean, divided by count (reviewer, page 8)."
    },
    # Section 10: Advanced Probability Concepts (6 questions)
    {
        "section": "Advanced Probability Concepts",
        "question": "Conditional probability is the probability of an event:",
        "choices": ["a. Independent of others", "b. Given another event occurred", "c. Mutually exclusive", "d. Equal to 1"],
        "correct": "b",
        "reasoning": "Conditional probability is the probability of an event given another has occurred (reviewer, page 5)."
    },
    {
        "section": "Advanced Probability Concepts",
        "question": "Bayes’ Theorem is used to find:",
        "choices": ["a. The mean", "b. Conditional probability given reverse probability", "c. The variance", "d. The mode"],
        "correct": "b",
        "reasoning": "Bayes’ Theorem determines conditional probability given the reverse (reviewer, page 5)."
    },
    {
        "section": "Advanced Probability Concepts",
        "question": "A null space is:",
        "choices": ["a. A subset with no elements", "b. The entire sample space", "c. A single outcome", "d. A compound event"],
        "correct": "a",
        "reasoning": "Null space is a subset with no elements (reviewer, page 4)."
    },
    {
        "section": "Advanced Probability Concepts",
        "question": "True or False: A Venn diagram illustrates relationships between events.",
        "choices": ["a. True", "b. False", "c. Only for simple events", "d. Only for compound events"],
        "correct": "a",
        "reasoning": "Venn diagrams show event relationships (reviewer, page 4)."
    },
    {
        "section": "Advanced Probability Concepts",
        "question": "The number of license plate combinations (2 letters, 2 digits) is:",
        "choices": ["a. 6,760", "b. 67,600", "c. 676,000", "d. 6,760,000"],
        "correct": "a",
        "reasoning": "26 × 26 × 10 × 10 = 6,760 (reviewer, page 4, adapted)."
    },
    {
        "section": "Advanced Probability Concepts",
        "question": "All of the following are true for combinations EXCEPT:",
        "choices": ["a. Order does not matter", "b. Formula is n! / (x!(n - x)!)", "c. Used for permutations", "d. Selects x objects from n"],
        "correct": "c",
        "reasoning": "Combinations are not used for permutations, which consider order (reviewer, page 5)."
    },
    # Section 11: Mixed Concepts (6 questions)
    {
        "section": "Mixed Concepts",
        "question": "The mean is the ___ while the median is the ___.",
        "choices": ["a. Middle value, average", "b. Average, middle value", "c. Most frequent, average", "d. Average, most frequent"],
        "correct": "b",
        "reasoning": "Mean is the average, median is the middle value (reviewer, page 8)."
    },
    {
        "section": "Mixed Concepts",
        "question": "Variance measures ___ while standard deviation measures ___.",
        "choices": ["a. Spread in squared units, spread in original units", "b. Central tendency, spread", "c. Spread in original units, spread in squared units", "d. Probability, dispersion"],
        "correct": "a",
        "reasoning": "Variance uses squared units, standard deviation uses original units (reviewer, page 8)."
    },
    {
        "section": "Mixed Concepts",
        "question": "A sample is ___ while a population is ___.",
        "choices": ["a. All individuals, a subset", "b. A subset, all individuals", "c. A random variable, a distribution", "d. A distribution, a sample space"],
        "correct": "b",
        "reasoning": "Sample is a subset, population is all individuals (reviewer, page 3)."
    },
    {
        "section": "Mixed Concepts",
        "question": "Quantitative research uses ___ while qualitative research uses ___.",
        "choices": ["a. Descriptive data, measurable data", "b. Inferential statistics, descriptive data", "c. Non-statistical data, statistical data", "d. Measurable data, experimental data"],
        "correct": "b",
        "reasoning": "Quantitative uses inferential statistics, qualitative uses descriptive data (reviewer, page 1)."
    },
    {
        "section": "Mixed Concepts",
        "question": "The Poisson distribution is ___ while the binomial distribution is ___.",
        "choices": ["a. For fixed trials, for continuous intervals", "b. For continuous intervals, for fixed trials", "c. Always symmetric, always skewed", "d. For high probability, for low probability"],
        "correct": "b",
        "reasoning": "Poisson is for continuous intervals, binomial is for fixed trials (reviewer, pages 6–7)."
    },
    {
        "section": "Mixed Concepts",
        "question": "The normal distribution is ___ while the uniform distribution is ___.",
        "choices": ["a. Rectangular, bell-shaped", "b. Bell-shaped, rectangular", "c. Skewed, symmetric", "d. Discrete, continuous"],
        "correct": "b",
        "reasoning": "Normal is bell-shaped, uniform is rectangular (reviewer, page 7)."
    }
]

def randomize_questions(quiz_list):
    """
    Randomizes the order of questions in the quiz list in place.
    
    Args:
        quiz_list (list): List of dictionaries containing quiz questions
    """
    random.shuffle(quiz_list)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_quiz():
    score = 0
    results = []
    section_scores = defaultdict(lambda: {"correct": 0, "total": 0})
    
    # Randomize the quiz questions
    randomize_questions(quiz)
    
    for i, item in enumerate(quiz, 1):
        clear_screen()
        print(f"Question {i} of {len(quiz)}: {item['section']}")
        print(item['question'])
        for choice in item['choices']:
            print(choice)
        print("\nEnter your answer (a, b, c, or d): ", end="")
        
        while True:
            answer = input().strip().lower()
            if answer in ['a', 'b', 'c', 'd']:
                break
            print("Invalid input. Please enter a, b, c, or d: ", end="")
        
        correct = item['correct']
        section = item['section']
        section_scores[section]["total"] += 1
        
        if answer == correct:
            print("\nCorrect!")
            score += 1
            section_scores[section]["correct"] += 1
            results.append((i, True, answer, correct, ""))
        else:
            print(f"\nIncorrect! The correct answer is {correct}.")
            print(f"Reasoning: {item['reasoning']}")
            results.append((i, False, answer, correct, item['reasoning']))
        
        print("\nPress Enter to continue...", end="")
        input()

    # Display results
    clear_screen()
    print("=== Quiz Results ===")
    print(f"Total Questions: {len(quiz)}")
    print(f"Correct Answers: {score}")
    print(f"Incorrect Answers: {len(quiz) - score}")
    print(f"Percentage Score: {(score / len(quiz)) * 100:.2f}%")
    
    print("\nSection-wise Breakdown:")
    print("-" * 50)
    print(f"{'Section':<40} {'Correct':<10} {'Total':<10} {'Percentage':<10}")
    print("-" * 50)
    for section, data in section_scores.items():
        correct = data['correct']
        total = data['total']
        percentage = (correct / total) * 100 if total > 0 else 0
        print(f"{section:<40} {correct:<10} {total:<10} {percentage:.2f}%")
    
    print("\nDetailed Results:")
    print("-" * 50)
    for result in results:
        q_num, is_correct, user_answer, correct_answer, reasoning = result
        status = "Correct" if is_correct else f"Incorrect (Your answer: {user_answer}, Correct: {correct_answer})"
        print(f"Question {q_num}: {status}")
        if not is_correct:
            print(f"Reasoning: {reasoning}")
        print()

if __name__ == "__main__":
    print("Welcome to the Quantitative Methods Quiz Bee!")
    print("Answer each question with a, b, c, or d. Press Enter to proceed after each question.")
    print("Press Enter to start...", end="")
    input()
    run_quiz()