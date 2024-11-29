import re

def f(first_letter, last_letter):
    with open('data.txt', 'r', encoding='utf-8') as data:
        content = data.read()
        
        # Construct the regex pattern
        pattern = fr'\b{first_letter}\w*{last_letter}\b'
        
        # Find all matching words
        matches = re.findall(pattern, content, re.IGNORECASE)
    
    return len(matches)  # Return the count of matches

if __name__ == "__main__":
    # Example usage
    print(f('w', 'd'))