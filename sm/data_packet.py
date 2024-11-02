def convert_to_bit(text: str) -> str:
    return "".join(format(ord(i), "08b") for i in text)


def header(seq: int, size: int) -> dict:
    return {
        "sender_ip": "172.8.0.5",
        "receiver_ip": "240.20.9.155",
        "sequence_num": seq,
        "size": size,
    }


def trailer(num_of_one_bit: int) -> str:
    return f"{hex(num_of_one_bit)}10001"


if __name__ == "__main__":
    text = """Sat ga dawt no dae
  cus i pone gye kyaung
  but Sun can"""
    text_list = text.split("\n")
    for idx, val in enumerate(text_list):
        in_bit = convert_to_bit(val.strip())
        head = header(seq=idx + 1, size=int(len(in_bit) / 8))
        trail = trailer(in_bit.count("1"))

        print(head)
        print("\n")
        print(in_bit + "\n")
        print(trail)
        print("-------------------------------------")
