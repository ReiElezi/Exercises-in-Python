sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

# Access the value associated with the key 'history'
history_mark = sampleDict["class"]["student"]["marks"]["history"]

# Print the value of key 'history'
print("Value of key 'history':", history_mark)
