# todo Get Student Top Notes
#  todo Create a function that takes a list of student dictionaries and returns a list of their top notes. 
#  todo If the student does not have notes then let's assume their top note is equal to 0.

# ? Examples
# * get_student_top_notes([
#   {
#     "id": 1,
#     "name": "Jacek",
#     "notes": [5, 3, 4, 2, 5, 5]
#   },
#   {
#     "id": 2,
#     "name": "Ewa",
#     "notes": [2, 3, 3, 3, 2, 5]
#   },
#   {
#     "id": 3,
#     "name": "Zygmunt",
#     "notes": [2, 2, 4, 4, 3, 3]
#   }
# ]) ➞ [5, 5, 4]
# ! Notes
# N/A

# !  ////////////////////////////////////////////////////////////////////////////////

def get_student_top_notes(students):
     nots=[]
     for itme in students:
         tito = itme.get("notes")
         nots.append(max(tito))
     return nots




print(get_student_top_notes([
  {
    "id": 1,
    "name": "Jacek",
    "notes": [5, 3, 4, 2, 5, 5]
  },
  {
    "id": 2,
    "name": "Ewa",
    "notes": [2, 3, 3, 3, 2, 5]
  },
  {
    "id": 3,
    "name": "Zygmunt",
    "notes": [2, 2, 4, 4, 3, 3]
  }
]))



def get_student_top_notes(students):
    
    return [max(itme.get("notes")) for itme in students]


print(get_student_top_notes([
  {
    "id": 1,
    "name": "Jacek",
    "notes": [5, 3, 4, 2, 5, 5]
  },
  {
    "id": 2,
    "name": "Ewa",
    "notes": [2, 3, 3, 3, 2, 5]
  },
  {
    "id": 3,
    "name": "Zygmunt",
    "notes": [2, 2, 4, 4, 3, 3]
  }
]))


# !  ////////////////////////////////////////////////////////////////////////////////




def get_student_top_notes(students):
    nots = []
    for item in students:
        tito = item.get("notes", [])  # Get the notes or an empty list if missing
        if tito:  # If there are notes
            nots.append(max(tito))
        else:  # If the list is empty, append 0
            nots.append(0)
    return nots

# Test cases
print(get_student_top_notes([
    {
        "id": 1,
        "name": "Jacek",
        "notes": [5, 3, 4, 2, 5, 5]
    },
    {
        "id": 2,
        "name": "Ewa",
        "notes": [2, 3, 3, 3, 2, 5]
    },
    {
        "id": 3,
        "name": "Zygmunt",
        "notes": [2, 2, 4, 4, 3, 3]
    }
]))  # ➞ [5, 5, 4]

print(get_student_top_notes([
    {
        "id": 1,
        "name": "Alice",
        "notes": []
    },
    {
        "id": 2,
        "name": "Bob",
        "notes": [1, 2, 3]
    }
]))  # ➞ [0, 3]





# !  ////////////////////////////////////////////////////////////////////////////////




def get_student_top_notes(students):
    top_notes = []
    for student in students:
        if student['notes']:  # Check if the student has any notes
            top_notes.append(max(student['notes']))  # Append the highest note
        else:
            top_notes.append(0)  # If no notes, append 0
    return top_notes

# Test cases
print(get_student_top_notes([
    {
        "id": 1,
        "name": "Jacek",
        "notes": [5, 3, 4, 2, 5, 5]
    },
    {
        "id": 2,
        "name": "Ewa",
        "notes": [2, 3, 3, 3, 2, 5]
    },
    {
        "id": 3,
        "name": "Zygmunt",
        "notes": [2, 2, 4, 4, 3, 3]
    }
]))  # ➞ [5, 5, 4]

print(get_student_top_notes([
    {
        "id": 1,
        "name": "Alice",
        "notes": []
    },
    {
        "id": 2,
        "name": "Bob",
        "notes": [1, 2, 3]
    }
]))  # ➞ [0, 3]
