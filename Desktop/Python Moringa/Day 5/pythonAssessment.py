import re
from collections import Counter

def count_specific_word(text, word):
    """Counts the number of occurrences of the specified word in the text."""
    if not text:
        return 0
    # Find all words, convert to lowercase, and count matches
    words = re.findall(r'\b\w+\b', text.lower())
    return words.count(word.lower())

def identify_most_common_word(text):
    """Identifies the most common word in the text."""
    if not text:
        return None
    words = re.findall(r'\b\w+\b', text.lower())
    if not words:
        return None
    # Counter returns a list of tuples: [('word', count)]
    most_common = Counter(words).most_common(1)
    return most_common[0][0]

def calculate_average_word_length(text):
    """Calculates the average length of words, excluding punctuation."""
    if not text:
        return 0.0
    words = re.findall(r'\b\w+\b', text)
    if not words:
        return 0.0
    total_length = sum(len(word) for word in words)
    return float(total_length / len(words))

def count_paragraphs(text):
    """Counts paragraphs based on empty lines between blocks of text."""
    if not text:
        return 1
    # Split by double newlines and filter out empty strings
    paragraphs = [p for p in text.split('\n\n') if p.strip()]
    return len(paragraphs) if paragraphs else 1

def count_sentences(text):
    """Counts sentences based on periods, exclamation marks, and question marks."""
    if not text:
        return 1
    # Find all occurrences of sentence-ending punctuation
    sentences = re.findall(r'[.!?]', text)
    return len(sentences) if sentences else 1

# --- News Article Data ---
article_text = """
ACME Inc. Unveils Revolutionary Apple Pie Machine, Transforming Baking with Automation

ACME Inc., a leading innovator in culinary technology, has launched a groundbreaking new device that promises to revolutionize the way apple pies are made. Dubbed the “Apple Pie Master,” this machine combines cutting-edge technology with traditional baking techniques to automate the entire pie-making process, ensuring perfect pies every time.

At a press conference held at ACME Inc.'s headquarters in Springfield, the company's CEO, Jane Doe, introduced the Apple Pie Master to an eager audience of journalists, culinary experts, and industry insiders. "Our goal has always been to make cooking and baking accessible and enjoyable for everyone, and with the Apple Pie Master, we are making a giant leap forward," Doe stated.

The Apple Pie Master is designed to simplify the baking process while maintaining the quality and taste of a homemade pie. The machine is equipped with AI-driven sensors that can analyze the quality of ingredients, adjust cooking times, and even replicate intricate baking techniques perfected by master chefs. “This isn't just about saving time; it's about enhancing the baking experience and ensuring consistent results,” Doe explained.

## Unpacking the Technology

The heart of the Apple Pie Master lies in its advanced artificial intelligence system. This system is programmed to perform tasks such as peeling and slicing apples, mixing ingredients, and rolling out pie crusts. According to ACME Inc.'s head of product development, Dr. Emily Clark, “The AI not only replicates human actions but learns from each pie made, adjusting its techniques to improve the next one”.

Another innovative feature of the Apple Pie Master is its real-time monitoring capabilities. Cameras and sensors inside the machine provide continuous feedback during the pie-making process, allowing the AI to make micro-adjustments to the temperature and cooking times as needed. This ensures that each pie is baked to golden perfection.

## User-Friendly Features

ACME Inc. has designed the Apple Pie Master with user experience in mind. The machine features a sleek, user-friendly interface with pre-programmed settings for different pie recipes. Users can select options for crust type, spice levels, and even the variety of apples they want to use. “We want to cater to all taste preferences, from the traditional to the adventurous,” said marketing director, Tom Nguyen.

The machine also includes a mobile app, allowing users to start the baking process from their smartphones. This app not only controls the machine but also provides users with tips, recipes, and the option to order ingredients directly through ACME Inc.'s partners.

## Environmental and Economic Impact

ACME Inc. is also proud of the Apple Pie Master’s environmental credentials. The machine is built from recycled materials and designed to operate with minimal energy consumption. “Sustainability is at the core of all our product designs,” emphasized environmental consultant Lisa Green, who collaborated on the project.

Economically, the Apple Pie Master could have significant implications for both commercial and home bakers. By reducing the time and skill required to make high-quality pies, it opens up new business opportunities for small bakeries and restaurants, and it provides a cost-effective solution for busy consumers who crave homemade desserts without the fuss.

## Market Response and Availability

The response to the Apple Pie Master has been overwhelmingly positive. Early adopters and reviewers have praised its ease of use and the quality of the pies it produces. Culinary blogger Mark Spencer commented, “It’s like having a professional baker in your kitchen. The pies are consistently excellent, with perfectly flaky crusts and rich, flavorful fillings”.

ACME Inc. plans to make the Apple Pie Master available online and in select retail stores starting next month. The company has set a competitive price point to make this innovative technology accessible to a broad audience.

## The Future of Automated Baking

Looking ahead, ACME Inc. plans to expand its range of automated baking machines. “The Apple Pie Master is just the beginning,” said CEO Jane Doe. “We’re exploring machines for other types of desserts and complex dishes. Our vision is to automate parts of the cooking process without sacrificing the art of cooking”.

The Apple Pie Master from ACME Inc. represents a significant advancement in the field of culinary technology. By automating the process of baking apple pies, this machine not only makes baking more accessible but also sets a new standard for the integration of technology in traditional cooking practices. As more consumers and businesses adopt this technology, it could well redefine our cooking experiences and expectations.
"""

if __name__ == "__main__":
    # Example TBD word to search for: "apple"
    search_word = "apple"
    
    print(f"--- Text Analysis Results ---")
    print(f"Occurrences of '{search_word}': {count_specific_word(article_text, search_word)}")
    print(f"Most Common Word: {identify_most_common_word(article_text)}")
    print(f"Average Word Length: {calculate_average_word_length(article_text):.2f}")
    print(f"Paragraph Count: {count_paragraphs(article_text)}")
    print(f"Sentence Count: {count_sentences(article_text)}")