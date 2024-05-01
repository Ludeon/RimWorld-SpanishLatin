import os
import re

# Create a temporary folder
temp_dir = os.path.join(os.environ['temp'], str(uuid.uuid4()))
os.makedirs(temp_dir)

# Create WordInfo/Gender folder
main_dir = "Core/WordInfo/Gender"
os.makedirs(main_dir, exist_ok=True)

# Paths of the XML files in which the words should be searched
# "*\Backstories" won't be used for now
paths = [
    "*\DefInjected\PawnKindDef",
    "*\DefInjected\FactionDef",
    "*\DefInjected\ThingDef",
    "*\DefInjected\WorldObjectDef",
    "*\DefInjected\GameConditionDef"
    "*\DefInjected\BodyPartDef"
    "*\DefInjected\BodyDef"
]

# Search words in the XML files and save them in different lists of words depending on their gender
for path in paths:
    # unknown gender
    with open(os.path.join(temp_dir, "all_unknown.txt"), "a") as unknown_file:
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith(".xml"):
                    with open(os.path.join(root, file), "r", encoding="utf-8") as xml_file:
                        for match in re.finditer(r"<(.*(\.label|\.pawnSingular|title|titleShort|\.chargeNoun))>(.*?)</\1>", xml_file.read(), re.IGNORECASE):
                            unknown_file.write(match.group(3).lower() + "\n")

    # male gender
    with open(os.path.join(temp_dir, "all_males.txt"), "a") as males_file:
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith(".xml"):
                    with open(os.path.join(root, file), "r", encoding="utf-8") as xml_file:
                        for match in re.finditer(r"<(.*(labelMale))>(.*?)</\1>", xml_file.read(), re.IGNORECASE):
                            males_file.write(match.group(3).lower() + "\n")

    # female gender
    with open(os.path.join(temp_dir, "all_females.txt"), "a") as females_file:
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith(".xml"):
                    with open(os.path.join(root, file), "r", encoding="utf-8") as xml_file:
                        for match in re.finditer(r"<(.*(\.labelFemale|titleFemale|titleShortFemale))>(.*?)</\1>", xml_file.read(), re.IGNORECASE):
                            females_file.write(match.group(3).lower() + "\n")

# Save a list of all found words
all_files = [os.path.join(temp_dir, file) for file in os.listdir(temp_dir) if file.startswith("all")]
all_words = set()
for file in all_files:
    with open(file, "r") as word_file:
        all_words.update(word_file.read().splitlines())
with open(os.path.join(temp_dir, "all.txt"), "w") as all_file:
    all_file.write("\n".join(sorted(all_words)))

# Create files
for file_name in ["Male", "Female", "Neuter", "Other", "new_words"]:
    file_path = os.path.join(main_dir, f"{file_name}.txt")
    if not os.path.exists(file_path):
        open(file_path, "w").close()

# Merge found male words into the list of male words
with open(os.path.join(main_dir, "Male.txt"), "a+") as male_file:
    for file in ["all_males.txt", "Male.txt"]:
        with open(os.path.join(temp_dir, file), "r") as source_file:
            male_file.writelines(sorted(set(source_file.readlines())))

# Merge found female words into the list of female words
with open(os.path.join(main_dir, "Female.txt"), "a+") as female_file:
    for file in ["all_females.txt", "Female.txt"]:
        with open(os.path.join(temp_dir, file), "r") as source_file:
            female_file.writelines(sorted(set(source_file.readlines())))

# Sort the list of neuter words
with open(os.path.join(main_dir, "Neuter.txt"), "r+") as neuter_file:
    neuter_file.writelines(sorted(set(neuter_file.readlines())))

# Sort the list of other words
with open(os.path.join(main_dir, "Other.txt"), "r+") as other_file:
    other_file.writelines(sorted(set(other_file.readlines())))

# Save a list of words already classified
with open(os.path.join(temp_dir, "wordinfo.txt"), "w") as wordinfo_file:
    for file in ["Male.txt", "Female.txt", "Neuter.txt", "Other.txt"]:
        with open(os.path.join(main_dir, file), "r") as source_file:
            wordinfo_file.writelines(sorted(set(source_file.readlines())))

# Save a list of words not classified
reference_words = set(open(os