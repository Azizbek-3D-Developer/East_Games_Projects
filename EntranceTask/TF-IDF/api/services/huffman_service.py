import heapq
from collections import defaultdict
from typing import Dict, List, Optional


class Node:
    def __init__(self, char: Optional[str] = None, freq: int = 0):
        self.char = char
        self.freq = freq
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def __lt__(self, other):
        return self.freq < other.freq


def printable_char(char: str) -> str:
    if char == ' ':
        return '[space]'
    elif char == '\n':
        return '[newline]'
    elif char == '\t':
        return '[tab]'
    elif char == '':
        return '[empty]'
    else:
        return char




def build_frequency_map(text: str) -> Dict[str, int]:
    freq_map = defaultdict(int)
    for char in text:
        freq_map[char] += 1
    return freq_map


def build_huffman_tree(freq_map: Dict[str, int]) -> Optional[Node]:
    heap = [Node(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(heap)

    if not heap:
        return None

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]


def generate_code_map(root: Optional[Node], current_code: str = "", code_map: Dict[str, str] = None) -> Dict[str, str]:
    if code_map is None:
        code_map = {}

    if root is None:
        return code_map

    if root.char is not None:
        code_map[root.char] = current_code
    else:
        generate_code_map(root.left, current_code + "0", code_map)
        generate_code_map(root.right, current_code + "1", code_map)

    return code_map


def encode_text(text: str, code_map: Dict[str, str]) -> str:
    return ''.join(code_map[char] for char in text)


def huffman_encode(text: str) -> Dict[str, List[Dict[str, str]]]:
    freq_map = build_frequency_map(text)
    root = build_huffman_tree(freq_map)
    code_map = generate_code_map(root)

    # Convert to list of dicts format
    # code_list = [{"letter": k, "code": v} for k, v in code_map.items()]
    code_list = [{"letter": printable_char(k), "code": v} for k, v in code_map.items()]

    encoded_text = encode_text(text, code_map)

    return {
        "encoded_text": encoded_text,
        "code_map": code_list
    }


def huffman_decode(code_map: List[Dict[str, str]], encoded_text: str) -> str:
    # Convert list of dicts to a lookup map
    reverse_map = {entry["code"]: entry["letter"] for entry in code_map}

    decoded_text = ""
    current_bits = ""
    for bit in encoded_text:
        current_bits += bit
        if current_bits in reverse_map:
            decoded_text += reverse_map[current_bits]
            current_bits = ""
    return decoded_text


async def compute_huffman_from_text(text: str) -> List[Dict[str, str]]:
    """
    Returns the Huffman code map (list of dicts) from the input text.
    The encoded text is not stored for now.
    """
    result = huffman_encode(text)
    return result["code_map"]