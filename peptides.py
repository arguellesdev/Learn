"""Aminoacids classification and performance
in this code we want to create an interaction with aminoacis while
we are defining how many aminoacids conforms dfferent type of molecules
such as peptides or proteins"""
def classify_aminoacid():
    """This function is to defining amino acids long chain clasification """
    aminoacids = {"Oligopeptide": range(10, 20),
                "Peptide": range(2, 50),
                "Polypeptide": range(20, 50),
                "Protein": range(51, 100)}
    a_count = int(input("What is the number of amino acids? "))
    check_if_therapeutic(aminoacids, a_count)

def check_if_therapeutic(aminoacids, a_count):
    """conditionals about length for therapeutic system"""
    for key in aminoacids:
        if a_count in aminoacids[key]:
            print ("you have", key, "by having", a_count,
                    "aminoacids, you are doing good, now lets find separation process to continue")
            return True
        if max(aminoacids["Polypeptide"]) < a_count or a_count < min(aminoacids["Oligopeptide"]):
            print("Your amino acid chaing lenght does not fit on therapeutic purposes")
            print ("Consult a specialist to determine the appropriate synthesis performance.")
            return False
classify_aminoacid()
