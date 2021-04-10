# A-B-Testing-at-Nosh-Mish-Mosh
A/B Testing at Nosh Mish Mosh
The Nosh Mish Mosh is a recipe and ingredient meal delivery service. They ship the raw materials and you get to cook them at your home! They’ve decided to hire a data analyst to help make product and interface decisions. Get started to help them figure out the amount of data they’ll need to make meaningful decisions.

Note that a solution.py file is loaded for you in the workspace, which contains solution code for this project. We highly recommend that you complete the project on your own without checking the solution, but feel free to take a look if you get stuck or want to check your answers when you’re done!``

Tasks
16/16 Complete
Mark the tasks as complete by checking them off
Nosh Mish Mosh: An Assortment of Edible Aliments
1.
We’ve collected customer data for the past week and exposed it through a Python library, so first import noshmishmosh.


Stuck? Get a hint
2.
Next, we’ll need to do a little bit of data analysis — let’s use numpy to help. Import numpy into your workspace as np.


Stuck? Get a hint
A/B Testing at Nosh Mish Mosh
3.
Nosh Mish Mosh wants to run an experiment to see if we can convince more people to purchase meal plans if we use a more artisanal-looking vegetable selection. We’ve photographed these modern meals with blush tomatoes and graffiti eggplants, but aren’t sure if this strategy will sell enough units to benefit from establishing a business relationship with a new provider.

Before running this experiment, of course, we need to know the sample size that will be required to detect the difference we are hoping for. There are three things we need to know before we can determine that number.

the Baseline Conversion Rate
Minimum Detectable Effect (desired lift)
and the Statistical Significance Threshold
4.
Let’s get the ball rolling on finding those numbers! In order to get our baseline, we need to first know how many users visit the site in a typical week. Let’s grab that logged information, which is stored in noshmishmosh.customer_visits. Assign that to a new variable called all_visitors.


Stuck? Get a hint
5.
Next we need to know how many visitors to the site ultimately end up buying a meal or set of meals in a typical week. We have that information saved into purchasing_customers field on noshmishmosh. Save that information into a variable called paying_visitors.


Stuck? Get a hint
6.
Calculate the lengths of the two lists, saving the results into variables called total_visitor_count and paying_visitor_count, respectively.


Stuck? Get a hint
7.
Now to get the baseline: Divide the number of purchasing visitors by the number of total visitors. Save the result in a variable called baseline_percent. Since we want a percentage as our answer, multiply the result by 100.0.


Stuck? Get a hint
8.
Print out the baseline_percent so we know what to use for our baseline percentage in the A/B Sample Size Calculator.


Stuck? Get a hint
Mish Mosh B'Gosh: The Effect Size
9.
These rainbow fingerling potatoes don’t come cheap. We’d like to know for sure that, with this change, we’ll be pulling in at least $1240 more every week. In order to figure out how many more customers we need, we’ll have to investigate the average revenue generated from a given sale. Luckily we have a list of the money spent by each customer in a typical week: noshmishmosh.money_spent. Save that list into a variable called payment_history.


Stuck? Get a hint
10.
We need to find how many purchases it would take to reach $1240 in additional revenue using our historical data.

Let’s start with computing the average payment per paying customer using np.mean, saving it as average_payment.


Stuck? Get a hint
11.
We want to know how many of these “usual” payments it would take to clear our $1240 mark. Round the number up using np.ceil (because that’s how many new customers it takes to bring in more than $1240). Save that value into a new_customers_needed variable.


Stuck? Get a hint
12.
Now find the additional percent of weekly visitors who must make a purchase in order to make this change worthwhile. Do this by dividing the number of customers by the total visitor count for a typical week (calculated earlier), and multiplying by 100. Save the result in a variable called percentage_point_increase. Print percentage_point_increase to see what it is.


Stuck? Get a hint
13.
In order to find our minimum detectable effect/desired lift, we need to express percentage_point_increase as a percent of baseline_percent. You can do this by dividing percentage_point_increase by baseline_percent and multiplying by 100.0.

Store the results in a variable called mde.


Stuck? Get a hint
14.
Print out the result mde.


Stuck? Get a hint
Nosh Mish Mosh: Tying It All Together
15.
The last thing we need to calculate the sample size for Nosh Mish Mosh’s artisanal rebranding is our statistical significance threshold. We’d like to be fairly certain, but this isn’t going to be a million dollar decision, so let’s go with 10%.

16.
Now put it all together! Punch the baseline, the minimum detectable effect, and the statistical significance threshold into the calculator and evaluate how many people need to be shown the new assets before we can check if the results are a significant improvement. Save the results in a variable called ab_sample_size.
