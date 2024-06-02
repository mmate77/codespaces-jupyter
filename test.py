print("Hello")
name = 'Agile Game'
print(name)

try:
    count = int(input('Enter the number of team members: '))
    if count == 8:
        print("Within 8")
    else:
        print("Game Started")
    print(count)

    # Create an empty dictionary to store team member information
    team_members = {}
    for i in range(count):
        role = input(f"Enter the role of team member {i + 1}: ")
        member_name = input(f"Enter the name of team member {i + 1}: ")
        team_members[member_name] = role

    print("Team members and their roles:")
    for member, role in team_members.items():
        print(f"{member}: {role}")

    # Input user stories
    user_stories = []
    for i in range(2):
        user_story = input(f"Enter User Story {i + 1} (in the format 'As a <role>, I want, so that'): ")
        user_stories.append(user_story)

    # Assign user stories to team members
    for story in user_stories:
        assigned_member = input(f"Assign '{story}' to which team member? (Enter name): ")
        if assigned_member in team_members:
            print(f"'{story}' assigned to {assigned_member}.")
        else:
            print(f"Error: Team member '{assigned_member}' not found.")

except ValueError:
    print("Please enter a valid integer for the number of team members.")

import pandas as pd

# Read the Excel file (replace 'your_file.xlsx' with the actual file path)
file_path = 'backlog.xlsx'
df = pd.read_excel(file_path)

# Assuming your Excel file has columns 'As a user', 'I want', and 'So that'
user_stories = df[['As a user', 'I want', 'So that']].values.tolist()

# Print the user stories
for i, story in enumerate(user_stories, start=1):
    print(f"User Story {i}:")
    print(f"As a {story[0]}, I want {story[1]}, so that {story[2]}")
    print()

# Now you can process the user stories further as needed
