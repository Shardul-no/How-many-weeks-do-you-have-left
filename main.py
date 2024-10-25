import datetime
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#adjust to your country
AVERAGE_LIFESPAN_WEEKS = 70 * 52

#how many weeks are left
def calculate_weeks(birthdate):
    today = datetime.date.today()
    weeks_lived = (today - birthdate).days // 7
    weeks_remaining = AVERAGE_LIFESPAN_WEEKS - weeks_lived
    return weeks_lived, weeks_remaining

#tells matplot to visualise
def visualize_weeks(weeks_lived, weeks_remaining):
    total_weeks = weeks_lived + weeks_remaining
    boxes_per_row = 52  
    rows = total_weeks // boxes_per_row + 1
    box_size = 0.8  

    fig, ax = plt.subplots(figsize=(15, rows / 2))
    ax.set_xlim(0, boxes_per_row)
    ax.set_ylim(0, rows)
    ax.axis("off")

    #lived is green
    for week in range(weeks_lived):
        row = week // boxes_per_row
        col = week % boxes_per_row
        ax.add_patch(mpatches.Rectangle((col, rows - row - 1), box_size, box_size, color="green"))

    #remaining is gray
    for week in range(weeks_lived, total_weeks):
        row = week // boxes_per_row
        col = week % boxes_per_row
        ax.add_patch(mpatches.Rectangle((col, rows - row - 1), box_size, box_size, color="lightgray"))

    plt.title(f"Your Life in Weeks\n{weeks_lived} weeks lived, {weeks_remaining} weeks remaining")
    plt.show()

#takes input
birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.datetime.strptime(birthdate_input, "%Y-%m-%d").date()

#calculates
weeks_lived, weeks_remaining = calculate_weeks(birthdate)

#display
visualize_weeks(weeks_lived, weeks_remaining)