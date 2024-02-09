import json

class VolunteerActivity:
    def __init__(self, name, hours, impact_score):
        self.name = name
        self.hours = hours
        self.impact_score = impact_score

    def to_dict(self):
        return {
            'name': self.name,
            'hours': self.hours,
            'impact_score': self.impact_score
        }

def log_activity(activities, activity):
    activities.append(activity.to_dict())

def calculate_total_impact(activities):
    total_hours = sum(activity['hours'] for activity in activities)
    total_impact = sum(activity['impact_score'] for activity in activities)
    return total_hours, total_impact

def main():
    activities = []

    while True:
        print("\nVolunteer Impact Tracker")
        name = input("Enter activity name (or 'exit' to end): ")
        if name.lower() == 'exit':
            break

        hours = float(input("Enter number of hours: "))
        impact_score = float(input("Enter impact score (1-10): "))

        activity = VolunteerActivity(name, hours, impact_score)
        log_activity(activities, activity)

    total_hours, total_impact = calculate_total_impact(activities)
    print(f"\nTotal Volunteer Hours: {total_hours}")
    print(f"Total Impact Score: {total_impact}")

    # Optionally save the activities to a file
    with open('activities.json', 'w') as f:
        json.dump(activities, f, indent=4)

if __name__ == "__main__":
    main()
