import json

File_Name = "quests.json"

def load_quests():
    with open(File_Name, 'r') as f:
        return json.load(f)
    
def save_quests():
    with open(File_Name, 'w') as f:
        json.dump(quests, f, indent=4)

def main():
    quests = load_quests()

    total_xp = sum([q['xp'] for q in quests if q['status'] == 'completed'])
    try:
        quest_id = int(input("\n⚔️ Enter Quest ID to complete (0 to exit): "))
    except ValueError:
        return

    if quest_id == 0:
        return

    found = False
    for q in quests:
        if q['id'] == quest_id:
            q['status'] = 'completed' # 6. MUTATION
            print(f"✅ Quest '{q['task']}' Complete! XP Gained.")
            found = True
            break
            
    if found:
        save_quests(quests) # Save the progress
    else:
        print("❌ Quest ID not found.")

if __name__ == "__main__":
    main()