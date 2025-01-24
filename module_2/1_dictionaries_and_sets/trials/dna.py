# BEGIN (write your solution here)
def to_rna(dna: str) -> str:
    result = ""
    translation = {
        "G" : "C",
        "C" : "G",
        "T" : "A",
        "A" : "U"
    }
    for element in dna:
        result += translation[element]
    return result
# END


def main():
    print(to_rna('ACGTGGTCTTAA'))

if __name__ == "__main__":
    main()


# def to_rna(dna: str) -> str:
#     result = ""
#     for element in dna:
#         if element == "G":
#             result += "C"
#         if element == "C":
#             result += "G"
#         if element == "T":
#             result += "A"
#         if element == "A":
#             result += "U"
#     return result
